import pandas as pd
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
from torch import from_numpy
import math

#need to check SF from ntuple level

channel = ['mmm', 'mmm', 'mmm', 'mmm']
SF = [242.63153870289298,711.9921839035441,235.82572970062492,808.6588336625248]

lumi = 3000000
genevt = 9999999
xsec = 0.004228


train_result = '/u/user/yeobi97/JKPS_WZG/WZG/final_trial/run/Eval_train/TrainSET_mmm_prediction_Adagrad.csv'
eval_result = '/u/user/yeobi97/JKPS_WZG/WZG/final_trial/run/Eval_norm/TestSET_mmm_prediction_Adagrad.csv'	


df_train = pd.read_csv(train_result)
df_eval = pd.read_csv(eval_result)

bkg_train = df_train[df_train.label == 0]
sig_train = df_train[df_train.label == 1]
new_bkg = bkg_train[bkg_train['weight'] != SF[0]]

bkg_eval = df_eval[df_eval.label == 0]
sig_eval = df_eval[df_eval.label == 1]
new_bkg_eval = bkg_eval[bkg_eval['weight'] != SF[0]]



plt.rcParams['figure.figsize'] = (8,8)

hbkg = plt.hist(bkg_train['prediction'], histtype='step', range =(0,1),weights=bkg_train['weight']*5/(3*SF[0]), bins=10, linewidth=3, color='orange', label='Backgrounds:Train')
hsig = plt.hist(sig_train['prediction'], histtype='step', range =(0,1),weights=sig_train['weight']*5/3 * lumi * xsec/genevt, bins=10, linewidth=3, color='royalblue', label='Signal:Train')
hbkg2 =plt.hist(bkg_eval['prediction'], histtype='step', range =(0,1),weights=bkg_eval['weight']*5/SF[0], bins=10, linewidth=3, color='crimson', label='Backgrounds:Eval')
hsig2 = plt.hist(sig_eval['prediction'], histtype='step', range =(0,1),weights=sig_eval['weight']*5 * lumi * xsec/genevt, bins=10, linewidth=3, color='skyblue', label='Signal:Eval')


plt.title("$\sqrt{s}=14$ TeV, L=3000 $fb^{-1}$", fontsize=13, loc='right')
plt.xlabel('DNN score', fontsize=17)
plt.ylabel('Expected Yield | 0.1 Score', fontsize=17)
plt.ylim(0.1, 1000)
plt.text(0.4,70,'{mmm channel}', fontsize=15)
plt.legend(fontsize=14, loc = 'upper right')
plt.yscale('log')
plt.savefig('mmm_DNNscore_comparison')
plt.show()
plt.close()

