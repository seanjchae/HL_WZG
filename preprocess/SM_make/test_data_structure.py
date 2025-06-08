import numpy as np
import awkward as ak 
import vector

eee_infile='/u/user/yeobi97/JKPS_WZG/WZG/lightend_ML/SM_sum/eee_channel.npy'
eee_data = np.load(eee_infile,allow_pickle=True)[()]

print(eee_data['ZZ'].keys())
