import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

channel = ['eee','eem','emm','mmm']

def Load(cha):
    infile = './SM_make_out/' + cha + '_binary.h5'
    df = pd.read_hdf(infile)
    print(df)
    print(df.columns)

    # Set all weights to 1
    df['weight'] = 1

    eta1 = df['lep1_eta']
    eta2 = df['lep2_eta']
    eta3 = df['lep3_eta']
    peta = df['photon_eta']
    phi1 = df['lep1_phi']
    phi2 = df['lep2_phi']
    phi3 = df['lep3_phi']
    pphi = df['photon_phi']
    mphi = df['met_phi']

    # Remove unnecessary columns
    df = df.drop(['lep1_charge','lep2_charge','lep3_charge','lep1_eta','lep2_eta','lep3_eta','lep1_phi','lep2_phi','lep3_phi','photon_eta','photon_phi','met_phi'], axis=1)

    # Restore necessary columns
    df['lep2_eta'] = eta2
    df['lep1_eta'] = eta1
    df['lep3_eta'] = eta3
    df['photon_eta'] = peta
    df['lep1_phi'] = phi1
    df['lep2_phi'] = phi2
    df['lep3_phi'] = phi3
    df['photon_phi'] = pphi
    df['met_phi'] = mphi

    print(df)
    print(df.columns)
    df.to_hdf('{0}_binary.h5'.format(cha), key='df', mode='w')

    return df

Load(channel[0])
Load(channel[1])
Load(channel[2])
Load(channel[3])
