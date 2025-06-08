import os, sys
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep

# Setting
CMSSTYLE = True
nEpoch = 10
colorset = ['royalblue'] #['orange', 'grey','red','blue']
files = 'eee_history.csv'
# Reverse order
#files = files[::-1]
#colorset = colorset[::-1]

def drawAcc(files):
    ## plot
    plt.figure(figsize=(12,10))
    if CMSSTYLE:
        plt.style.use(hep.style.CMS)
        hep.cms.label(loc=0, data=False,llabel="Simulation", rlabel="(14 TeV)", ax=None)
    #plt.ylim(0.8,1.02)
    xran = np.arange(0, nEpoch, 1)
    for i, file in enumerate(files):
        df = pd.read_csv(file)
        plt.plot(xran, df['train_accuracy'], label='eee_train', linewidth=2, marker='o',color=colorset[i])
        plt.plot(xran, df['val_accuracy'], label='eee_valid',linewidth=2, marker='v',linestyle='dashed',color=colorset[i])
    plt.xlim(-0.5,10.5)
    plt.xlabel('Epoch', fontsize=20)
    plt.ylabel('Accuracy', fontsize=20)
    plt.legend(loc='lower right', fontsize=20)
    plt.grid()
    plt.tight_layout()
    plt.savefig('eee_trainACC.png')
    plt.close()

def drawLoss(files):
    ## plot
    plt.figure(figsize=(12,10))
    if CMSSTYLE:
        plt.style.use(hep.style.CMS)
        hep.cms.label(loc=0, data=False,llabel="Simulation", rlabel="(14 TeV)", ax=None)
    xran = np.arange(0, nEpoch, 1)
    for i, file in enumerate(files):
        df = pd.read_csv(file)
        plt.plot(xran, df['train_loss'], label='eee_train', linewidth=2, marker='o',color=colorset[i])
        plt.plot(xran, df['val_loss'], label = 'eee_valid',linewidth=2, marker='v',linestyle='dashed',color=colorset[i])
    plt.xlim(-0.5,10.5)
    plt.xlabel('Epoch', fontsize=20)
    plt.ylabel('Loss', fontsize=20)
    plt.yscale('log')
    plt.legend(loc='upper right', fontsize=20)
    plt.grid(axis='y',which='both')
    plt.grid(axis='x')
    plt.tight_layout()
    plt.savefig('eee_trainLOSS.png')
    plt.close()

def timingPlot(history):
    file = 'time.csv'
    df = pd.read_csv(file)
    # sorting by time
    df = df.sort_values(by=['time'])
    colorset = ['red','green','orange','grey','pink','blue']
    colorset = colorset[::-1]
    plt.figure(figsize=(12,8))
    if CMSSTYLE:
        plt.style.use(hep.style.CMS)
        hep.cms.label(loc=0, data=False,llabel="Simulation", rlabel="(14 TeV)", ax=None)
    plt.bar(df['Optimizer'], df['time'], color=colorset,alpha=0.5,align='center',edgecolor='black',linewidth=2)
    plt.text(-0.3,74,'Geforce RTX 4060 Ti\n \nInputs: 4772269\nBatchsize: 4096',fontsize=20,horizontalalignment='left',verticalalignment='center')
    plt.ylim(65,76)
    plt.xlabel('Optimizer', fontsize=20)
    plt.ylabel('Time (s)', fontsize=20)
    plt.tight_layout()
    plt.savefig('time.png')
    plt.close()


if __name__ == '__main__':
    drawAcc(files)
    drawLoss(files)
    #timingPlot(files)
