import glob
import numpy as np
import awkward as ak
from numba import jit
from tqdm import tqdm
import time

def Loop(process):
	
	infile = '/u/user/yeobi97/SE_UserHome/fin_WZG_nTuple/mmm_'+process+'_updated_nTuple.npy'
	arrays = np.load(infile,allow_pickle=True)[()]
	# photon,met object --> made by +1 dimension. --> need to flatten once again
	f_photon_pt = ak.flatten(arrays['photon_pt'])
	f_photon_eta = ak.flatten(arrays['photon_eta'])
	f_photon_phi = ak.flatten(arrays['photon_phi'])
	f_met = ak.flatten(arrays['met'])
	f_met_phi = ak.flatten(arrays['met_phi'])

	histo = {}
	print('start_{}'.format(process))
	try :
		lep1_pt = arrays['lep1_pt'   ]
		lep1_eta = arrays['lep1_eta']
		lep1_phi = arrays['lep1_phi']
		lep1_charge = arrays['lep1_charge']
		lep2_pt = arrays['lep2_pt'   ]
		lep2_eta = arrays['lep2_eta'  ]
		lep2_phi = arrays['lep2_phi'  ]
		lep2_charge = arrays['lep2_charge']
		lep3_pt = arrays['lep3_pt'   ]
		lep3_eta = arrays['lep3_eta'  ]
		lep3_phi = arrays['lep3_phi'  ]
		lep3_charge = arrays['lep3_charge']
		photon_pt = f_photon_pt
		photon_eta = f_photon_eta
		photon_phi = f_photon_phi 

		met = f_met
		met_phi = f_met_phi

		dR1 = arrays['dR1']
		dR2 = arrays['dR2']
		dR3 = arrays['dR3']

		M_Z = np.array(arrays['M_Z'], dtype=float)
		M_W = np.array(arrays['M_W'], dtype=float)
		M_lll = np.array(arrays['M_lll'],dtype=float)
		M_lllr = np.array(arrays['M_lllr'], dtype=float)
		M_Zr = np.array(arrays['M_Zr'], dtype=float)
		M_Wr = np.array(arrays['M_Wr'], dtype=float)

		if len(histo) == 0 :
			histo['lep1_pt'] = lep1_pt
			histo['lep1_eta'] = lep1_eta
			histo['lep1_phi'] = lep1_phi
			histo['lep1_charge'] = lep1_charge
			histo['lep2_pt'] = lep2_pt
			histo['lep2_eta'] = lep2_eta
			histo['lep2_phi'] = lep2_phi
			histo['lep2_charge'] = lep2_charge
			histo['lep3_pt'] = lep3_pt
			histo['lep3_eta'] = lep3_eta
			histo['lep3_phi'] = lep3_phi
			histo['lep3_charge'] = lep3_charge
			histo['photon_pt'] = photon_pt
			histo['photon_eta'] = photon_eta
			histo['photon_phi'] = photon_phi
			histo['met'] = met
			histo['met_phi'] = met_phi
			histo['dR1'] = dR1
			histo['dR2'] = dR2
			histo['dR3'] = dR3
			histo['M_Z'] = M_Z
			histo['M_W'] = M_W
			histo['M_lll'] = M_lll
			histo['M_lllr'] = M_lllr
			histo['M_Zr'] = M_Zr
			histo['M_Wr'] = M_Wr

		else :
			print('shit')

	except KeyError :
		print('shit')

	return histo

WZG = Loop('signal')
ZG = Loop('ZG')
ZZ = Loop('ZZ')
WWW = Loop('WWW')
WWZ = Loop('WWZ')
WZZ = Loop('WZZ')
ZZZ = Loop('ZZZ')
ttbarG = Loop('ttbarG')
mmm = {}
mmm['WZG'] = WZG
mmm['ZG'] = ZG
mmm['ZZ'] = ZZ
mmm['WWW'] = WWW
mmm['WWZ'] = WWZ
mmm['WZZ'] = WZZ
mmm['ZZZ'] = ZZZ
mmm['ttbarG'] = ttbarG

outname = "./mmm_channel_fin.npy"
np.save(outname,mmm)

print('muyaho')
