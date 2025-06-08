import numpy as np
import pandas as pd
import sys, os
import matplotlib.pyplot as plt

import torch
from torch.utils.data import Dataset, DataLoader
from torch import nn, from_numpy, optim
from torch.utils.data.dataset import random_split
import torch.nn.functional as F

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
parser.add_argument('--batch', type=int,default=1024,
            help="--batch BATCH_SIZE")
parser.add_argument('--lr', type=float,default=0.01,
            help="--lr LEARNING_RATE")
parser.add_argument('--channel', type=str, default='eee', help="--channel CHANNEL")

parser.add_argument('--GPU', type=str, default='0', help="--GPU GPU_NUMBER")

args = parser.parse_args()

## Hyperparameter
batch_size = args.batch
LR = args.lr
EPOCH = args.epoch
channel = args.channel
GPU_num = args.GPU

#Load Dataset for Evaluation

#####################################################################################################
#sys.path.append("../python/")
#from DataSet import TestDataset


#test_dataset = TestDataset()

#test_loader = DataLoader(dataset=test_dataset,batch_size=batch_size,shuffle=False,num_workers=2)
####################################################################################################

#jiwan added for evaluating with test  set

sys.path.append("/u/user/yeobi97/JKPS_WZG/WZG/final_trial/python/eee")

from DataSet import TestDataset

test_dataset = TestDataset()

test_loader = DataLoader(dataset=test_dataset,batch_size=batch_size,shuffle=False,num_workers=2)

####################################################################################################


## Device set and Optimizer set
from Model import Model

device = 'cpu'
if torch.cuda.is_available() & use_gpu:
        model = Model()
        model = model.to('cuda:' + GPU_num + '')
        device = 'cuda:' + GPU_num+ ''

#for Adam
#model.load_state_dict(torch.load('/u/user/yeobi97/JKPS_WZG/WZG/ML_finalized/opte_run/Train/eee_weightFile_Adam_b8192_n2048.pth'))

#optm = optim.Adam(model.parameters(), lr=LR)

#for Adagrad
model.load_state_dict(torch.load('/u/user/yeobi97/JKPS_WZG/WZG/final_trial/run/Train/eee_weightFile.pth'))

optm = optim.Adagrad(model.parameters(), lr=LR)

#for RMSprop
#model.load_state_dict(torch.load('/u/user/yeobi97/JKPS_WZG/WZG/ML_finalized/opte_run/Train/eee_weightFile_RMSPROP_b8192_n2048.pth'))

#optm = optim.RMSprop(model.parameters(), lr=LR)


# Evaluation
from tqdm.auto import tqdm
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix

labels, preds = [], []
weights, scaleWeights = [], []
#for Adam
#predFile = 'eee_prediction_Adam.csv'

#for Adagrad/RMSPROP
predFile = 'TestSET_eee_prediction_Adagrad.csv'

model.eval()

for i, (test_x, label, weight) in enumerate(tqdm(test_loader)):
	test_x = test_x.float().to(device)
	weight = weight.float()
	pred = model(test_x).detach().to('cpu').float()

	labels.extend([x.item() for x in label])
	preds.extend([x.item() for x in pred.view(-1)])
	weights.extend([x.item() for x in weight.view(-1)]) 

df = pd.DataFrame({'label': labels, 'prediction': preds, 'weight': weights})
df.to_csv(predFile, index=True)

