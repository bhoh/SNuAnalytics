#ONLY_FINALCUT=True

import os
import sys
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/../')


#-----Variable Deinition-----#
from WPandCut2016 import *

cuts={}


if 'opt' in globals():
    configration_py=opt.cutsFile
else:
    configration_py=sys.argv[0]
print "configration_py=",configration_py


LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'

#------End of Variable Definition-----#
#supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut+'&&isFatJetEvent[0]'
supercut = LepWPCut+'&& Lepton_promptgenmatched[0]' ##prompt truth matched


##---Lepton Categorization---##



LepCuts={}
#if 'ele' in configration_py:
LepCuts['eleCH']='(Lepton_isTightElectron_'+eleWP+'[0]>0.5)'
#if 'mu' in configration_py:
LepCuts['muCH']='(Lepton_isTightMuon_'+muWP+'[0]>0.5)'

elePtCuts = {}
#elePtBins=[0., 30., 35., 36.,37.,38.,40.,42.,45.,50.,65.,70.,80.,100.,200.,]
for idx in range(0,len(elePtBins)-1):
    #elePtCuts['elePt'+str(int(elePtBins[idx]))+'to'+str(int(elePtBins[idx+1]))] =\
        elePtCuts['elePtBin'+str(idx)] =\
                  '(Lepton_pt[0] <= '+str(elePtBins[idx+1])+\
                  ' && Lepton_pt[0]>'+str(elePtBins[idx])+')'
             
eleEtaCuts={}
#eleEtaBins=[-2.5, -2.1, -1.570, -1.440, -0.800, 0., 0.800, 1.440, 1.570, 2.100, 2.500]
for idx in range(0,len(eleEtaBins)-1):
    #eleEtaCuts['eleEta'+str((eleEtaBins[idx]))+'to'+str((eleEtaBins[idx+1]))] =\
                  eleEtaCuts['eleEtaBin'+str(idx)]=\
                                                                                     '(Lepton_etaSC[0] <= '+str(eleEtaBins[idx+1])+\
                                                                                     ' && Lepton_etaSC[0]>'+str(eleEtaBins[idx])+')'


##--BoostedProdCats, BoostedRegionCats, BoostedPtOverMlnJCat
for LepCut in LepCuts:
    if 'ele' in LepCut:
        for elePt in elePtCuts:
            for eleEta in eleEtaCuts:
                print "!"
                cutname=LepCut+'__'+elePt+'__'+eleEta
                formula=LepCuts[LepCut]+'&&'+elePtCuts[elePt]+'&&'+eleEtaCuts[eleEta]
                cuts[cutname]=formula




print "Ncuts=",len(cuts)

for c in sorted(cuts):
    print c
