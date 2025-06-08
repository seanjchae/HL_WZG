import numpy as np

infile = '/u/user/yeobi97/SE_UserHome/fin_WZG_nTuple/eee_signal_updated_nTuple.npy'
arrays = np.load(infile,allow_pickle=True)[()]

print(arrays)
