import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep

lumi_com = [ 150,  300,  450,  600,  750,  900, 1050, 1200, 1350, 1500, 1650, 1800, 1950, 2100, 2250, 2400, 2550, 2700, 2850, 3000] 
com = [2.67105, 3.58659, 4.30536, 4.91742, 5.45933, 5.95048, 6.40267, 6.82367, 7.219, 7.59267, 7.94776, 8.28667, 8.61134, 8.92331, 9.22391, 9.5142, 9.79513, 10.0675, 10.3319, 10.5891]

#lumi_eee

plt.figure(figsize=(10,8))
plt.style.use(hep. style.CMS)
#plt.plot(lumi, eee , label='eee channel',color='red', linewidth=2, linestyle='--')
#plt.plot(lumi, eem, label='ee$\mu$ channel',color='blue', linewidth=2, linestyle='-.')
#plt.plot(lumi, emm, label='e$\mu\mu$ channel',color='green', linewidth=2, linestyle=':')
#plt.plot(lumi, mmm, label='$\mu\mu\mu$ channel',color='purple', linewidth=2, linestyle='-')
plt.plot(lumi, com, label='combine channel',color='darkslategray', linewidth=3)

plt.axhline(5, 0, 10000, color='black', linestyle='-', linewidth=1, label='5 $\sigma$ line')

plt.legend(fontsize=17, loc='lower right')
plt.xlim(0,3000)
plt.ylim(0,7)
plt.xlabel("Luminosity [$fb^{-1}$]", fontsize=20, loc='center')
plt.ylabel("Expected Significance", fontsize=20, loc='center')

plt.savefig("ml_hct_result")
plt.show()
