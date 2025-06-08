import sys, os
import glob
import re
import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep

def extractLumi(clist):
	out = []
	for c in clist:
		numbers = re.sub(r'[^0-9]', '', c)
		out.append(int(numbers))
	out = np.sort(out)
	return out

def extractNumber(slist):
	out = []
	for s in slist:
		numbers = float(s.split(' ')[-1].replace('\n', ''))
		out.append(numbers)
	return out

def doHiggs(channel, lumis):
	out = []
	for idx, lumi in enumerate(lumis):
		print('calculating', lumi, 'fb-1')
		if idx == 0:
			os.system('combine -M Significance card_storage/'+str(channel)+'_'+str(lumi)+'_card.txt -t -1 --expectSignal=1 | grep Significance: > temp.txt')
		else:
			os.system('combine -M Significance card_storage/'+str(channel)+'_'+str(lumi)+'_card.txt -t -1 --expectSignal=1 | grep Significance: >> temp.txt')

		#if idx == 2:
			#break
	with open('temp.txt','r') as f:
		original = f.readlines()
		significance = extractNumber(original)
	return lumis[:idx+1], significance

def mainRun(channel):
	cardlist = glob.glob('./card_storage/{}*.txt'.format(channel))
	lumis = extractLumi(cardlist)
	lumi,sig = doHiggs(channel,lumis)
	return lumi, sig

#pro_list = ['com','eee','eem','emm','mmm']

com_lumi, com_sig = mainRun('com')
print(com_lumi, com_sig)
eee_lumi, eee_sig = mainRun('eee')
print(eee_lumi, eee_sig)
eem_lumi, eem_sig = mainRun('eem')
print(eem_lumi, eem_sig)
emm_lumi, emm_sig = mainRun('emm')
print(emm_lumi, emm_sig)
mmm_lumi, mmm_sig = mainRun('mmm')
print(mmm_lumi, mmm_sig)

plt.figure(figsize=(10,8))
plt.style.use(hep. style.CMS)
plt.plot(eee_lumi, eee_sig , label='eee channel',color='red', linewidth=2, linestyle='--')
plt.plot(eem_lumi, eem_sig, label='ee$\mu$ channel',color='blue', linewidth=2, linestyle='-.')
plt.plot(emm_lumi, emm_sig, label='e$\mu\mu$ channel',color='green', linewidth=2, linestyle=':')
plt.plot(mmm_lumi, mmm_sig, label='$\mu\mu\mu$ channel',color='purple', linewidth=2, linestyle='-')
plt.plot(com_lumi, com_sig, label='combine channel',color='darkslategray', linewidth=3)

plt.axhline(5, 0, 10000, color='black', linestyle='-', linewidth=1, label='5 $\sigma$ line')

plt.legend(fontsize=17, loc='lower right')
plt.xlim(0,3000)
plt.ylim(0,7)
plt.xlabel("Luminosity [$fb^{-1}$]", fontsize=20, loc='center')
plt.ylabel("Expected Significance", fontsize=20, loc='center')

plt.savefig("jiwani_ml_hct_result")
plt.show()


