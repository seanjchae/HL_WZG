import numpy as np
import pandas as pd
import sys, os
import csv

import torch
from torch.utils.data import Dataset, DataLoader
from torch import nn, from_numpy, optim
from torch.utils.data.dataset import random_split
import torch.nn.functional as F
from sklearn.metrics import accuracy_score


## Check GPU
def GPU_check():
    if torch.cuda.is_available():

        nGPU = torch.cuda.device_count()
        print("Number of GPU : {0}".format(nGPU))

        for i,j in enumerate(range(nGPU)):
            print("Device", i, torch.cuda.get_device_name(i))

    else:
        print("No GPU for use")

GPU_check()
use_gpu=True

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--epoch', type=int,default=200,
            help="--epoch EPOCH")
parser.add_argument('--batch', type=int,default=8192,
            help="--batch BATCH_SIZE")
parser.add_argument('--lr', type=float,default=0.01,
            help="--lr LEARNING_RATE")

args = parser.parse_args()

## Hyperparameter
batch_size = args.batch
LR = args.lr
EPOCH = args.epoch

##  Data load
# jiwan added : for only mmm channel training
sys.path.append("/u/user/yeobi97/JKPS_WZG/WZG/eta_phi_ML/python/mmm")

from DataSet import TrainDataset, ValDataset

train_dataset = TrainDataset()
val_dataset = ValDataset()

train_loader = DataLoader(dataset=train_dataset,batch_size=batch_size,shuffle=False,num_workers=2)
val_loader = DataLoader(dataset=val_dataset,batch_size=batch_size*2,shuffle=False,num_workers=2)


## Model load
from Model import Model

device = 'cpu'
print(torch.cuda.is_available() & use_gpu)
if torch.cuda.is_available() & use_gpu:
    model = Model()
    model = model.to('cuda')
    device = 'cuda'

    optm = optim.Adagrad(model.parameters(), lr=LR)

# EarlyStopping 클래스 정의
class EarlyStopping:
    def __init__(self, patience=5, verbose=False, delta=0):
        self.patience = patience
        self.verbose = verbose
        self.delta = delta
        self.counter = 0
        self.best_loss = None
        self.early_stop = False
        self.best_weights = None

    def __call__(self, val_loss, model):
        if self.best_loss is None:
            self.best_loss = val_loss
            self.best_weights = model.state_dict()
        elif val_loss < self.best_loss - self.delta:
            self.best_loss = val_loss
            self.best_weights = model.state_dict()
            self.counter = 0
        else:
            self.counter += 1
            if self.counter >= self.patience:
                self.early_stop = True
        return self.early_stop

# EarlyStopping 인스턴스 생성
early_stopping = EarlyStopping(patience=10, verbose=True)

bestWeight, bestLoss = {}, 1e9
try:
    history = {'train_loss': [], 'train_accuracy': [], 'val_loss': [], 'val_accuracy': []}

    # Start EPOCH
    for epoch in range(1, EPOCH + 1):

        # Training Stage
        model.train()
        optm.zero_grad()  # initialize grad data
        train_loss, train_acc = 0., 0.

        for i, (train_x, label, train_w) in enumerate(train_loader):

            train_x = train_x.float().to(device)  # Make tensor on the gpu or cpu
            label = label.float().to(device)
            weight = train_w.float().to(device)

            pred = model(train_x)
            crit = torch.nn.BCELoss(weight=weight)  # binary cross entropy

            if device == 'cuda': crit = crit.cuda()  # GPU case
            loss = crit(pred, label)
            loss.backward()

            optm.step()

            train_loss += loss.item()
            train_acc += accuracy_score(label.to('cpu'), np.where(pred.to('cpu') > 0.5, 1, 0), sample_weight=weight.view(-1).to('cpu'))

        train_loss /= len(train_loader)
        train_acc /= len(train_loader)

        # Validation Stage
        model.eval()
        val_loss, val_acc = 0., 0.

        for i, (val_x, label, val_w) in enumerate(val_loader):
            val_x = val_x.float().to(device)
            label = label.float().to(device)
            weight = val_w.float().to(device)

            pred = model(val_x)
            crit = torch.nn.BCELoss(weight=weight)

            loss = crit(pred, label)
            val_loss += loss.item()
            val_acc += accuracy_score(label.to('cpu'), np.where(pred.to('cpu') > 0.5, 1, 0), sample_weight=weight.view(-1).to('cpu'))

        val_loss /= len(val_loader)
        val_acc /= len(val_loader)

        # Update weight of best epoch checking validation loss
        if bestLoss > val_loss:
            bestWeight = model.state_dict()
            bestLoss = val_loss

            torch.save(bestWeight, 'mmm_weightFile.pth')

        history['train_loss'].append(train_loss)
        history['train_accuracy'].append(train_acc)
        history['val_loss'].append(val_loss)
        history['val_accuracy'].append(val_acc)

        if epoch % 10 == 1:
            print(f"Epoch: {epoch}, Train Loss: {train_loss}, Val Loss: {val_loss}, Train Acc: {train_acc}, Val Acc: {val_acc}")

        with open('mmm_history.csv', 'w') as f:
            writer = csv.writer(f)
            keys = history.keys()
            writer.writerow(keys)
            for row in zip(*[history[key] for key in keys]):
                writer.writerow(row)

        # Early stopping check
        if early_stopping(val_loss, model):
            print(f"Early stopping at epoch {epoch}")
            model.load_state_dict(early_stopping.best_weights)
            break

except KeyboardInterrupt:
    print("Muyaho!")

