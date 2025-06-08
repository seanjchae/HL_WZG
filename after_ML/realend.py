import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mplhep as hep


lumi = [1050,1200,1350,1500,150,1650,1800,1950,2100,2250,2400,2550,2700,2850,3000,300,450,600,750,900]

#com = [8.94934,9.27006,9.55004,9.79865,4.37477,10.0247,10.2421,10.453,10.6578,10.857,11.0509,11.2397,11.4238,11.6035,11.7789,5.87163,6.85215,7.56879,8.12481,8.57435]

#eee = [3.04359,3.21964,3.37966,3.52617,1.22922,3.66112,3.78603,3.90213,4.01044,4.11178,4.20688,4.29633,4.38067,4.46032,4.5357,1.71865,2.08132,2.3767,2.62822,2.84808]

#eem = [5.95419,6.33503,6.68738,7.01564,2.31574,7.32314,7.61248,7.88578,8.14472,8.39073,8.62499,8.84853,9.06221,9.26679,9.46295,3.25939,3.97295,4.56576,5.08041,5.53885]

#emm = [4.74941,4.99385,5.21158,5.40706,1.99802,5.58372,5.74426,5.89085,6.02527,6.14899,6.26325,6.36911,6.46743,6.55901,6.6445,2.77317,3.33454,3.78157,4.15385,4.47223]

#mmm = [7.09064,7.40757,7.68341,7.92564,3.12232,8.14003,8.33104,8.50222,8.65647,8.79611,8.92309,9.039,9.14522,9.24315,9.33778,4.29772,5.12607,5.76809,6.28867,6.72242]

eee = [3.2704, 3.45483,3.62173,3.77388,1.33299,3.91345,4.04211,4.16122,4.27192,4.37511, 4.47161,4.56205,4.64703,4.72705, 4.80252,1.86068,2.24971,2.56502,2.83222,3.06465]

lumi = np.sort(lumi)
#com = np.sort(com)
eee = np.sort(eee)
#eem = np.sort(eem)
#emm = np.sort(emm)
#mmm = np.sort(mmm)

plt.figure(figsize=(10,8))
plt.style.use(hep. style.CMS)
plt.plot(lumi, eee , label='eee channel',color='red', linewidth=2, linestyle='--')
#plt.plot(lumi, eem, label='ee$\mu$ channel',color='blue', linewidth=2, linestyle='-.')
#plt.plot(lumi, emm, label='e$\mu\mu$ channel',color='green', linewidth=2, linestyle=':')
#plt.plot(lumi, mmm, label='$\mu\mu\mu$ channel',color='purple', linewidth=2, linestyle='-')
#plt.plot(lumi, com, label='combine channel',color='darkslategray', linewidth=3)

plt.axhline(5, 0, 10000, color='black', linestyle='-', linewidth=1, label='5 $\sigma$ line')

plt.legend(fontsize=17, loc='lower right')
plt.xlim(0,3000)
plt.ylim(0,7)
plt.xlabel("Luminosity [$fb^{-1}$]", fontsize=20, loc='center')
plt.ylabel("Expected Significance", fontsize=20, loc='center')

plt.savefig("ml_hct_result")
plt.show()

