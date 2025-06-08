import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sklearn

# Data Load
eee_infile = "./coladd_out/"+"eee_binary.h5" 
eem_infile = "./coladd_out/"+"eem_binary.h5"
emm_infile = "./coladd_out/"+"emm_binary.h5"
mmm_infile = "./coladd_out/"+"mmm_binary.h5"

eee_df = pd.read_hdf(eee_infile)
eem_df = pd.read_hdf(eem_infile)
emm_df = pd.read_hdf(emm_infile)
mmm_df = pd.read_hdf(mmm_infile)

'''
# use pandas 
df_shuffled_pd = df.sample(frac=1).reset_index(drop=True)

# use numpy 
df_shuffled_np = df.iloc[np.random.permutation(df.index)].reset_index(drop=True)
'''
# use sklearn
eee_df_shuffled_sk = sklearn.utils.shuffle(eee_df)
eem_df_shuffled_sk = sklearn.utils.shuffle(eem_df)
emm_df_shuffled_sk = sklearn.utils.shuffle(emm_df)
mmm_df_shuffled_sk = sklearn.utils.shuffle(mmm_df)

print(eee_df_shuffled_sk)
print(eem_df_shuffled_sk)
print(emm_df_shuffled_sk)
print(mmm_df_shuffled_sk)

print(eee_df_shuffled_sk.columns)

eee_df_shuffled_sk.to_hdf('eee_binary.h5', key = 'df', mode = 'w')
eem_df_shuffled_sk.to_hdf('eem_binary.h5', key = 'df', mode = 'w')
emm_df_shuffled_sk.to_hdf('emm_binary.h5', key = 'df', mode = 'w')
mmm_df_shuffled_sk.to_hdf('mmm_binary.h5', key = 'df', mode = 'w')

