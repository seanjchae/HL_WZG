import pandas as pd
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
from torch import from_numpy
import math

#need to check SF from ntuple level 

#channel = ['eee', 'eem', 'emm', 'mmm']
#SF = [242.63153870289298,711.9921839035441,235.82572970062492,808.6588336625248]

channel =['eee']
SF = [242.631538]


#this area is for aQGC

#tunning_512 = ['512_2','512_3','512_4','512_5']
#tunning_1024 = ['1024_2','1024_3','1024_4','1024_5']
#tunning_2048 = ['2048_2','2048_3','2048_4','2048_5']
#tunning_4096 = ['4096_2','4096_3','4096_4','4096_5']


lumi = 3000000
genevt = 9999999
xsec = 0.004228


#def infile(cha):

#	infile = '/u/user/dylee/workspace/WZG/ML/storage/'+cha+'/best/'+cha+'_prediction.csv'
#	df = pd.read_csv(infile)

#	return df

#def infile(cha):

#	infile = '/u/user/yeobi97/JKPS_WZG/WZG/ML_finalized/opte_run/for_compare_DNN/'+cha+'_prediction_Train_Adagrad.csv'
#	infile ='/u/user/yeobi97/JKPS_WZG/WZG/ML_finalized/opte_run/Eval/'+cha+'_prediction_Adam.csv'	
#	infile ='/u/user/yeobi97/JKPS_WZG/WZG/ML_finalized/opte_run/Eval/'+cha+'_prediction_RMSPROP.csv'

#	df = pd.read_csv(infile)

#	return df 

# to optimize train result (to get signiciant point with train result-->yield taking)

def infile(cha):
	infile = './eee_prediction_Train_Adagrad.csv'
	df = pd.read_csv(infile)
	return df

def aftertrain(cha):

	df = infile(cha)
	tpr,fpr,thr = roc_curve(df['label'], df['prediction'], sample_weight=df['weight'], pos_label=0)
	auc = roc_auc_score(df['label'], df['prediction'], sample_weight=df['weight'])
	
	plt.plot(fpr, tpr, '.', linewidth=2, label='%s %.3f' % ('auc', auc))
	plt.xlim(0, 1.000)
	plt.ylim(0, 1.000)
	plt.xlabel('False Positive Rate', fontsize=17)
	plt.ylabel('True Positive Rate', fontsize=17)
	plt.text(0.55,0.3,'({0} channel)'.format(cha), fontsize=18)
	plt.legend(fontsize =17)
#	plt.savefig("{0}_ROC.png".format(cha))
	plt.show()
	plt.close()

	return tpr, fpr, thr, auc

def dnn(cha,sf):

	df = infile(cha)
	bkg = df[df.label == 0]
	sig = df[df.label == 1]
	new_bkg = bkg[bkg['weight'] != sf]
	
	plt.rcParams['figure.figsize'] = (8,8)

	hbkg = plt.hist(bkg['prediction'], histtype='step', range =(0,1),weights=bkg['weight']*5/sf, bins=100, linewidth=3, color='crimson', label='Backgrounds')
	hsig = plt.hist(sig['prediction'], histtype='step', range =(0,1),weights=sig['weight']*5 * lumi * xsec/genevt, bins=100, linewidth=3, color='royalblue', label='Signal')

#visualizing DNN score 
#################################################################################################3
#	if cha == 'eee':
#		plt.axvline(x=0.85, color='black', linestyle=':', linewidth=2, label='Threshold')
#	elif cha == 'eem':
#		plt.axvline(x=0.87, color='black', linestyle=':', linewidth=2, label='Threshold')
#	elif cha == 'emm':
#		plt.axvline(x=0.70, color='black', linestyle=':', linewidth=2, label='Threshold')
#	elif cha == 'mmm':
#		plt.axvline(x=0.56, color='black', linestyle=':', linewidth=2, label='Threshold')
###############################################################################################

	plt.title("$\sqrt{s}=14$ TeV, L=3000 $fb^{-1}$", fontsize=13, loc='right')
	plt.xlabel('DNN score', fontsize=17)
	plt.ylabel('Expected Yield | 0.01 Score', fontsize=17)
	plt.ylim(0.1, 100)
	
	if cha == 'eee':
		plt.text(0.4, 70, '(eee channel)', fontsize=15)
	elif cha == 'eem':
		plt.text(0.4, 70, '(ee$\mu$ channel)', fontsize=15)
	elif cha == 'emm':
		plt.text(0.4, 70, '(e$\mu\mu$ channel)', fontsize=15)
	elif cha == 'mmm':
		plt.text(0.65, 70, '($\mu\mu\mu$ channel)', fontsize=18)

	plt.legend(fontsize=14, loc='upper left')
	plt.yscale('log')
#	plt.savefig("{0}_Adagrad_Nor_TrainDNN_score_b10.png".format(cha))
	plt.show()
	plt.close()

	return hbkg, hsig

def sigma(cha,sf):

	hbkg = dnn(cha,sf)[0]
	hsig = dnn(cha,sf)[1]
	N_bkg = hbkg[0]
	N_sig = hsig[0]

	arr_sig = []

	for cut in range(0,len(N_bkg),1):
		sig_integral = sum(N_sig[cut:])
		bkg_integral = sum(N_bkg[cut:])
		
		if sig_integral + bkg_integral == 0:
			significance = 0

		else:
			significance = sig_integral / math.sqrt(sig_integral + bkg_integral)

		arr_sig.append(significance)
		print(cut, sig_integral, bkg_integral, significance)

	print(arr_sig.index(max(arr_sig)))
	print('thisisit',max(arr_sig))

	return arr_sig

eee = sigma(channel[0],SF[0])
#eem = sigma(channel[1],SF[1])
#emm = sigma(channel[2],SF[2])
#mmm = sigma(channel[3],SF[3])

plt.rcParams["legend.loc"] = 'lower left'
plt.title("$\sqrt{s}=14$ TeV, L=3000 $fb^{-1}$", fontsize=13, loc='right')
#need to check
plt.plot(list([round(i*0.01,2) for i in range(0,100)]),eee,'--',color='red', label='eee channel', linewidth=2)
plt.plot(list([round(i*0.01,2) for i in range(0,100)]),eem,'-.',color='blue', label='ee$\mu$ channel', linewidth=2)
plt.plot(list([round(i*0.01,2) for i in range(0,100)]),emm,':',color='green', label='e$\mu\mu$ channel', linewidth=2)
plt.plot(list([round(i*0.01,2) for i in range(0,100)]),mmm,'-',color='purple', label='$\mu\mu\mu$ channel', linewidth=2)
plt.xlabel('DNN score',fontsize=20)
plt.ylabel('Expected Significance',fontsize=20)
plt.legend(fontsize=17)
#plt.savefig('sig')
plt.show()
plt.close()

eee = aftertrain(channel[0])
#eem = aftertrain(channel[1])
#emm = aftertrain(channel[2])
#mmm = aftertrain(channel[3])

