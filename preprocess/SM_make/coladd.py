import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

channel = ['eee','eem','emm','mmm']

def Load(cha):

	infile ='./SM_make_out/'+ cha+'_binary.h5'
	df = pd.read_hdf(infile)
	print(df)
	print(df.columns)
	# Add necessary columns
	df['weight'] = (df['xsec'] * 3000000)/df['Event']
	sigY = df[df['y'] == 1]['weight'].sum(axis = 0, skipna = False)
	bkgY = df[df['y'] == 0]['weight'].sum(axis = 0, skipna = False)

	sf = sigY/bkgY

	data = []

	for i in df['y']:
	
		if i ==1:
			data.append(1)

		else:
			data.append(sf)

	
	df['SF'] = data
	
	signal_N = len(df['weight'][df['y'] == 1])
	bkg_N = df['weight'][df['y'] == 0].sum()
	SF = signal_N / bkg_N

	print("{0} signal : {1}, bkg : {2}, SF : {3}".format(cha, signal_N, bkg_N, SF))

	df['weight'][df['y'] == 1] = 1
	df['weight'][df['y'] == 0] = df['weight'][df['y'] == 0] * SF

	df_weight = df['weight']
	df = df.drop(['weight', 'SF'], axis=1)

	df['weight'] = df_weight
	eta1 = df['lep1_eta']
	eta2 = df['lep2_eta']
	eta3 = df['lep3_eta']
	peta = df['photon_eta']
	#wzgamma_mass = df['wzgamma']
	#zgamma_mass = df['zgamma']

	phi1 = df['lep1_phi']
	phi2 = df['lep2_phi']
	phi3 = df['lep3_phi']
	pphi = df['photon_phi']
	mphi = df['met_phi']

	# Remove unnecessary columns
	df = df.drop(['lep1_charge','lep2_charge','lep3_charge'],axis=1)
	#df['lep2_eta'] = eta2
	#df['wzgamma'] = wzgamma_mass
	#df['lep1_eta'] = eta1
	#df['lep3_eta'] = eta3
	#df['photon_eta'] = peta
	#df['zgamma'] = zgamma_mass

	#df['lep1_phi'] = phi1
	#df['lep2_phi'] = phi2
	#df['lep3_phi'] = phi3
	#df['photon_phi'] = pphi
	#df['met_phi'] = mphi

	print(df)
	print(df.columns)
	df.to_hdf('{0}_binary.h5'.format(cha), key = 'df', mode = 'w')

	return df

Load(channel[0])
Load(channel[1])
Load(channel[2])
Load(channel[3])



