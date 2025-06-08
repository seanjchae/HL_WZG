channel = ['eee','eem','emm','mmm']
'''
eee = [274.1499339990662/3000, 1133.2251472877688/3000] # done
eem = [491.0448353205153/3000, 1785.5928646240206/3000]
emm = [ 501.34843466994346/3000, 2096.027392136818/3000]
mmm = [1160.3069944936603/3000, 4091.917726318415/3000] # done
'''

eee = [110.66791106679216/3000, 184.66220818289125/3000] # done
eem = [127.42347674233343 /3000, 84.04852793532187/3000] # done
emm = [242.37858023783565 /3000, 474.9761710995058/3000] # done
mmm = [350.4589550458947 /3000, 383.29236727030093/3000] # done


def makecard(cha,yields):

	for lumi in range(150, 3100, 150):

		sig = yields[0] * lumi
		bkg = yields[1] * lumi

		L = str(lumi)
		S = str(sig)
		B = str(bkg)

		if cha == 'eee':

			input_txt ="""
imax 1  number of channels
jmax 1  number of backgrounds
kmax 5  number of nuisance parameters (sources of systematical uncertainties)
-----------------------------------------------------------------------------
bin                  """+cha+"""
observation          0
-----------------------------------------------------------------------------
bin                  """+cha+"""   """+cha+"""
process              WZG   BKG
process              0     1
rate                 """+S+"""    """+B+"""
----------------------------------------------------------------------------
lumi        lnN      1.010   1.010
lep         lnN      1.015   1.015
pho         lnN      1.010   1.010
MET         lnN      1.100   1.100
pu          lnN      1.010   1.010"""

		elif cha == 'mmm':
		 
			input_txt ="""
imax 1  number of channels
jmax 1  number of backgrounds
kmax 5  number of nuisance parameters (sources of systematical uncertainties)
-----------------------------------------------------------------------------
bin                  """+cha+"""
observation          0
-----------------------------------------------------------------------------
bin                  """+cha+"""   """+cha+"""
process              WZG   BKG
process              0     1
rate                 """+S+"""   """+B+"""
----------------------------------------------------------------------------
lumi        lnN      1.010   1.010
lep         lnN      1.015   1.015
pho         lnN      1.010   1.010
MET         lnN      1.100   1.100
pu          lnN      1.010   1.010"""

		else:

			input_txt ="""
imax 1  number of channels
jmax 1  number of backgrounds
kmax 5  number of nuisance parameters (sources of systematical uncertainties)
-----------------------------------------------------------------------------
bin                  """+cha+"""
observation          0
-----------------------------------------------------------------------------
bin                  """+cha+"""   """+cha+"""
process              WZG   BKG
process              0     1
rate                 """+S+"""   """+B+"""
----------------------------------------------------------------------------
lumi        lnN      1.010   1.010
lep         lnN      1.011180339887499   1.011180339887499
pho         lnN      1.010   1.010
MET         lnN      1.100   1.100
pu          lnN      1.010   1.010"""

#		inputfile = open("/u/user/dylee/workspace/WZG/cutbase/hct/storage/card_storage/{0}_{1}_card.txt".format(cha,lumi),'w')
		inputfile = open("/u/user/yeobi97/JKPS_WZG/WZG/eta_phi_ML/after_ML/card_storage/{0}_{1}_card.txt".format(cha,lumi),'w')
		inputfile.write(input_txt)
		inputfile.close()

	return sig, bkg

def com_makecard(y1,y2,y3,y4):

	for lumi in range(150, 3100, 150):

		eee_sig = y1[0] * lumi
		eee_bkg = y1[1] * lumi
		
		eem_sig = y2[0] * lumi
		eem_bkg = y2[1] * lumi

		emm_sig = y3[0]	* lumi
		emm_bkg = y3[1] * lumi

		mmm_sig = y4[0] * lumi
		mmm_bkg = y4[1] * lumi
	
		L = str(lumi)
		eee_S = str(eee_sig)
		eee_B = str(eee_bkg)
		
		eem_S = str(eem_sig)
		eem_B = str(eem_bkg)

		emm_S = str(emm_sig)
		emm_B = str(emm_bkg)

		mmm_S = str(mmm_sig)
		mmm_B = str(mmm_bkg)
		
		input_txt ="""
imax *  number of channels
jmax *  number of backgrounds
kmax 5  number of nuisance parameters (sources of systematical uncertainties)
----------------------------------------------------------------------------------------------------------------------------------------------------------
bin                  eee   eem   emm   mmm
observation          0     0     0     0
----------------------------------------------------------------------------------------------------------------------------------------------------------
bin                  eee   eee   eem   eem   emm   emm   mmm   mmm
process              WZG   BKG   WZG   BKG   WZG   BKG   WZG   BKG
process              0     1     0     1     0     1     0     1
rate                 """+eee_S+"""   """+eee_B+"""   """+eem_S+"""   """+eem_B+"""   """+emm_S+"""   """+emm_B+"""   """+mmm_S+"""   """+mmm_B+"""
---------------------------------------------------------------------------------------------------------------------------------------------------------
lumi        lnN      1.010   1.010   1.010   1.010   1.010   1.010   1.010   1.010
lep         lnN      1.015   1.015   1.011180339887499   1.011180339887499   1.011180339887499   1.011180339887499   1.015     1.015
pho         lnN      1.010   1.010   1.010   1.010   1.010   1.010   1.010   1.010
MET         lnN      1.100   1.100   1.100   1.100   1.100   1.100   1.100   1.100
pu          lnN      1.010   1.010   1.010   1.010   1.010   1.010   1.010   1.010"""

#		inputfile = open("/u/user/dylee/workspace/WZG/cutbase/hct/storage/card_storage/com_{0}_card.txt".format(lumi),'w')
		inputfile = open("/u/user/yeobi97/JKPS_WZG/WZG/eta_phi_ML/after_ML/card_storage/com_{0}_card.txt".format(lumi),'w')
		inputfile.write(input_txt)
		inputfile.close()

	return lumi


makecard(channel[0],eee)
makecard(channel[1],eem)
makecard(channel[2],emm)
makecard(channel[3],mmm)

#jiwan added
#com_makecard(eee)
com_makecard(eee,eem,emm,mmm)
#com_makecard(mmm)

