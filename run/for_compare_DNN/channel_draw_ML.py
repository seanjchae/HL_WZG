import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
import awkward as ak
import math
import pandas as pd

process = ['WZG','ZZZ','WZZ','WWW','WWZ','WG','WW','ttbarG','ZG','ZZ']
#channel = ['eee','eem','emm','mmm']
#for eee_result : jiwan
channel = ['eee']

lumi = 3000000

EventDict = {
"WZG" : 9999999/5,
"WG" : 10010000/5,
"ZG" : 10010000/5,
"WW" : 10010000/5,
"ZZ" : 10010000/5,
"WWW" : 10003323/5,
"WWZ" : 9995610/5,
"WZZ" : 10010000/5,
"ZZZ" : 10010000/5,
"ttbarG" : 10010000/5,
}

xsecDict = {
"WZG" : 0.004228,
"WG" : 23.08,
"ZG" : 4.977,
"WW" : 3.356,
"ZZ" : 0.04642,
"WWW" : 0.001335,
"WWZ" : 0.0003067,
"WZZ" : 0.00002989,
"ZZZ" : 0.000003157,
"ttbarG" : 2.445,
}

def data(cha):

#	infile = "/u/user/dylee/workspace/WZG/ML/storage/"+cha+"/best/"+cha+"_prediction.csv"
	#for result of jiwan
#	infile = "/u/user/yeobi97/JKPS_WZG/WZG/ML_finalized/opte_run/Eval_norm/"+cha+"_prediction_Adagrad.csv"
#	df = pd.read_csv(infile)

#for train yield taking
	infile ="./"+cha+"_prediction_Train_Adagrad.csv"
	df = pd.read_csv(infile)
#   significant point with validation set evaluation: only for eee channel
	if cha == 'eee':
		cut_df = df[df['prediction'] >= 0.64]

	if cha == 'eem':
		cut_df = df[df['prediction'] >= 0.87]

	if cha == 'emm':
		cut_df = df[df['prediction'] >= 0.70]

	if cha == 'mmm':
		cut_df = df[df['prediction'] >= 0.56]

	idx = cut_df.iloc[:,[0]].values.flatten()

#	testset = "/u/user/dylee/workspace/WZG/ML/storage/"+cha+"/best/"+cha+"_testset.h5"
    #for result of jiwan
#	testset = "/u/user/yeobi97/JKPS_WZG/WZG/ML_finalized/opte_run/Eval_norm/"+cha+"_testset.h5"
#	test_df = pd.read_hdf(testset)

#	after = test_df.iloc[idx]
	
#	return after
# add for train yield taking
	testset = "/u/user/yeobi97/JKPS_WZG/WZG/ML_finalized/opte_run/Eval_norm/"+cha+"_trainset.h5"
	test_df = pd.read_hdf(testset)

	after = test_df.iloc[idx]

	return after


def variable(proc,cha):

	procdata = data(cha)[data(cha)['xsec'] == xsecDict['{0}'.format(proc)]]

	trilep = procdata['trilep_mass'].to_numpy()
	zgamma = procdata['zgamma'].to_numpy()
	wzgamma = procdata['wzgamma'].to_numpy()
	dilep = procdata['dilep_mass'].to_numpy()
	MT = procdata['MT'].to_numpy()
	wgamma = procdata['wgamma'].to_numpy()
		
	lep1_pt = procdata['lep1_pt'].to_numpy()
	lep1_eta = procdata['lep1_eta'].to_numpy()
	lep2_pt = procdata['lep2_pt'].to_numpy()
	lep2_eta = procdata['lep2_eta'].to_numpy()
	lep3_pt = procdata['lep3_pt'].to_numpy()
	lep3_eta = procdata['lep3_eta'].to_numpy()

	pho_pt = procdata['pho_pt'].to_numpy()
	pho_eta = procdata['pho_eta'].to_numpy()
	met = procdata['MET_MET'].to_numpy()

	print("{0} channel {1} Nevt: {2}".format(cha,proc,len(trilep)))

	return trilep, zgamma, wzgamma, dilep, MT, lep1_pt, lep1_eta, lep2_pt, lep2_eta, lep3_pt, lep3_eta, pho_pt, pho_eta, met, wgamma	

def scale(proc,cha):

	trilep = variable(proc,cha)[0]
	
	scales = np.ones(len(trilep)) * lumi * xsecDict["{0}".format(proc)] / EventDict["{0}".format(proc)]
	yields = len(trilep) * lumi * xsecDict["{0}".format(proc)] / EventDict["{0}".format(proc)]

	print("{0} channel {1} yields: {2}".format(cha,proc,yields))

	return scales, yields

def stack(proc,cha):

	lll, llg, lllg, lg = [],[],[],[]
	ll, mt = [],[]
	l1pt, l2pt, l3pt, gpt, MET = [],[],[],[],[]
	l1eta, l2eta, l3eta, geta = [],[],[],[]
	
	we,la,co = [],[],[]
	colors = ['red','indigo', 'maroon', 'darkslategray', 'darkorange', 'aqua', 'yellow', 'blue', 'darkgreen', 'dodgerblue']
	Y = []

	for i in range(len(proc)):

		trilep, zgamma, wzgamma, dilep, MT, lep1_pt, lep1_eta, lep2_pt, lep2_eta, lep3_pt, lep3_eta, pho_pt, pho_eta, met, wgamma = variable(proc[i],cha)
		
		lll_clip = np.clip(trilep,0,1000,trilep)		
		llg_clip = np.clip(zgamma,0,1000,zgamma)
		lllg_clip = np.clip(wzgamma,0,1200,wzgamma)	
		lg_clip = np.clip(wgamma,0,1000,wgamma)	
	
		ll_clip = np.clip(dilep,0,200,dilep)
		MT_clip = np.clip(MT,0,300,MT)

		l1pt_clip = np.clip(lep1_pt,0,600,lep1_pt)
		l2pt_clip = np.clip(lep2_pt,0,400,lep2_pt)
		l3pt_clip = np.clip(lep3_pt,0,600,lep3_pt)
		gpt_clip = np.clip(pho_pt,0,600,pho_pt)
		MET_clip = np.clip(met,0,600,met)

		l1eta_clip = np.clip(lep1_eta,-2.5,2.5,lep1_eta)
		l2eta_clip = np.clip(lep2_eta,-2.5,2.5,lep2_eta)
		l3eta_clip = np.clip(lep3_eta,-2.5,2.5,lep3_eta)
		geta_clip = np.clip(pho_eta,-2.5,2.5,pho_eta)

		lll.append(lll_clip)
		llg.append(llg_clip)
		lllg.append(lllg_clip)
		ll.append(ll_clip)
		mt.append(MT_clip)
		lg.append(lg_clip)

		l1pt.append(l1pt_clip)
		l2pt.append(l2pt_clip)
		l3pt.append(l3pt_clip)
		gpt.append(gpt_clip)
		MET.append(MET_clip)

		l1eta.append(l1eta_clip)
		l2eta.append(l2eta_clip)
		l3eta.append(l3eta_clip)
		geta.append(geta_clip)

		yields = scale(proc[i],cha)[1]
		Y.append(yields)

		weight = scale(proc[i],cha)[0]
		we.append(weight)

		la = ['$WZ\gamma$','ZZZ','WZZ','WWW','WWZ','$W\gamma$','WW','$t\overline{t}+\gamma$','$Z\gamma$','ZZ']
		
		color = colors[i]
		co.append(color)
	
	sig = Y[0]
	bkg = Y[1] + Y[2] + Y[3] + Y[4] + Y[5] +Y[6] + Y[7] +Y[8] + Y[9]

	print(sig, bkg)
	print(sig / math.sqrt(sig + bkg))

	return lll, llg, lllg, lg, ll, mt, l1pt, l2pt, l3pt, gpt, MET, l1eta, l2eta, l3eta, geta, we, la, co

def draw(cha):

	lll,llg,lllg,lg,ll,mt,l1pt,l2pt,l3pt,gpt,MET,l1eta,l2eta,l3eta,geta,we,la,co = stack(process,cha)
	
	name = ['lll','llg','lllg','lg','ll','mt','l1pt','l2pt','l3pt','gpt','MET','l1eta','l2eta','l3eta','geta']

	kk = ['$M_{lll}$','$M_{ll\gamma}$','$M_{lll\gamma}$','$M_{l\gamma}$','$M_{ll}$','$M_{T}$','Leading Z Lepton $P_{T}$','Subleading Z Lepton $ P_{T}$','W Lepton $P_{T}$','Photon $P_{T}$','$E^{miss}_{T}$','Leading Z Lepton $\eta$','Subleading Z Lepton $\eta$','W Lepton $\eta$','Photon $\eta$']

	tc = ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black','black']
	
	for i in range(0,15,1):

		b = 20

		if i==0 or i==1 or i==3:
			r1,r2 = 0,1000
		
		if i==2:
			r1,r2 = 0,1200

		if i==4:
			r1,r2 = 91.1876-15,91.1876+15

		if i==5:
			r1,r2 = 0,300

		if i==6 or i==8 or i==9 or i==10:
			r1,r2 = 0,600
		
		if i==7:
			r1,r2 = 0,400
		
		if i==11 or i==12 or i==13 or i==14:
			r1,r2,b = -2.5,2.5,100

		plt.figure(figsize=(8,8))
		plt.style.use(hep.style.CMS)
		bins = np.linspace(0,50,100)
		plt.hist(stack(process,cha)[i][0], range=(r1, r2), alpha=1, weights=we[0], bins=b, label=la[0], histtype='step', linewidth=2, color=co[0])
		plt.hist(stack(process,cha)[i][1:], range=(r1, r2), alpha=0.8, weights=we[1:], bins=b, label=la[1:], stacked=True, linewidth=2, color=co[1:])
		plt.hist(stack(process,cha)[i][1:], range=(r1, r2), alpha=1, weights=we[1:], bins=b, stacked=True, linewidth=0.5, color=tc[1:], histtype='step')
		plt.title("$\sqrt{s}=14$ TeV, $L=3000$ $fb^{-1}$", fontsize=13, loc='right')
		plt.xlim(r1,r2)
		plt.ylim(0.01, 1000)
		plt.xlabel("{0} [GeV]".format(kk[i]),fontsize=20, loc='center')
		plt.ylabel("Expected Yield | {0} GeV".format((r2-r1)/b),fontsize=20, loc='center')
		plt.legend(fontsize=12, loc='upper right', ncol=2, handleheight=2)
		plt.yscale('log')
		#plt.savefig("{0}_{1}".format(cha,name[i]))
		#plt.show()
		plt.close()

	return kk

draw(channel[0])
#draw(channel[1])
#draw(channel[2])
#draw(channel[3])


