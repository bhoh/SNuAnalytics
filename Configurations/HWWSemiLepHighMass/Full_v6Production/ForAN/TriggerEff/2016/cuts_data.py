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

#Lepton_isTightElectron_cutFall17V2Iso_Tight
#LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 ) && (Lepton_isTightElectron_'+eleWP+'[1]>0.5)'

#------End of Variable Definition-----#
#supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut+'&&isFatJetEvent[0]'
supercut = 'nLepton==2 && abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==11'


##---Lepton Categorization---##



#TnPCats={}
#TnPCats['Tag0Pass']='eleTrigMatch0 && (Lepton_isTightElectron_cutFall17V2Iso_Tight[0]>0.5) && eleTrigMatch1'
#TnPCats['Tag1Pass']='eleTrigMatch1 && (Lepton_isTightElectron_cutFall17V2Iso_Tight[1]>0.5) && eleTrigMatch0'


TnPCats={}
TnPCats['Tag0Pass1']='(eleTrigMatch0 && (Lepton_isTightElectron_'+eleTagWP+'[0]>0.5) && (Lepton_pt[0]>35.) && eleTrigMatch1 && Lepton_isTightElectron_'+eleWP+'[1]>0.5)'
TnPCats['Tag1Pass0']='!(eleTrigMatch0 && (Lepton_isTightElectron_'+eleTagWP+'[0]>0.5) && (Lepton_pt[0]>35.))'+'&&'+'(eleTrigMatch1 && (Lepton_isTightElectron_'+eleTagWP+'[1]>0.5)&&(Lepton_pt[1] >35. ) && eleTrigMatch0 && Lepton_isTightElectron_'+eleWP+'[0]>0.5)' ##not tag0 case

TnPCats['Tag0Fail1']='(eleTrigMatch0 && (Lepton_isTightElectron_'+eleTagWP+'[0]>0.5) &&(Lepton_pt[0] > 35.) && !eleTrigMatch1 && Lepton_isTightElectron_'+eleWP+'[1]>0.5)'
TnPCats['Tag1Fail0']='!(eleTrigMatch0 && (Lepton_isTightElectron_'+eleTagWP+'[0]>0.5)&&(Lepton_pt[0] > 35.))'+'&&'+'(eleTrigMatch1 && (Lepton_isTightElectron_'+eleTagWP+'[1]>0.5) && (Lepton_pt[1]>35.) && !eleTrigMatch0 && Lepton_isTightElectron_'+eleWP+'[0]>0.5)' ##not tag0 case

#LepCuts['eleCH']='(Lepton_isTightElectron_'+eleWP+'[0]>0.5)'


MllCuts={}
MllCuts['mll60120']='(mll>60. && mll<120.)'
MllCuts['mll70110']='(mll>70. && mll<110.)'

ele0PtCuts = {}
for idx in range(0,len(elePtBins)-1):
        ele0PtCuts['ele0PtBin'+str(idx)] =\
                  '(Lepton_pt[0] <= '+str(elePtBins[idx+1])+\
                  ' && Lepton_pt[0]>'+str(elePtBins[idx])+')'

ele1PtCuts = {}
for idx in range(0,len(elePtBins)-1):
        ele1PtCuts['ele1PtBin'+str(idx)] =\
                  '(Lepton_pt[1] <= '+str(elePtBins[idx+1])+\
                  ' && Lepton_pt[1]>'+str(elePtBins[idx])+')'

ele0EtaCuts={}
for idx in range(0,len(eleEtaBins)-1):
    ele0EtaCuts['ele0EtaBin'+str(idx)]=\
                                        '(Lepton_eta[0]+Electron_deltaEtaSC[Lepton_electronIdx[0]] <= '+str(eleEtaBins[idx+1])+\
                                        ' && Lepton_eta[0]+Electron_deltaEtaSC[Lepton_electronIdx[0]] >'+str(eleEtaBins[idx])+')'

ele1EtaCuts={}
for idx in range(0,len(eleEtaBins)-1):
    ele1EtaCuts['ele1EtaBin'+str(idx)]=\
                                        '( Lepton_eta[1]+Electron_deltaEtaSC[Lepton_electronIdx[1]] <= '+str(eleEtaBins[idx+1])+\
                                        ' && Lepton_eta[1]+Electron_deltaEtaSC[Lepton_electronIdx[1]] >'+str(eleEtaBins[idx])+')'

##--BoostedProdCats, BoostedRegionCats, BoostedPtOverMlnJCat
LepCut='eleCH'
for Mll in MllCuts:

    for idx_eta in range(0,len(eleEtaBins)-1):
        for idx_pt in range(0,len(elePtBins)-1):

            ##--Pass -> (Tag0Pass1&&ptetabin1) || (Tag1Pass0&&ptetabin0)
            cutname='Pass__eleEtaBin'+str(idx_eta)+'__'+'elePtBin'+str(idx_pt)+'__'+Mll
            formula0='('+TnPCats['Tag1Pass0']+'&&'+ele0EtaCuts['ele0EtaBin'+str(idx_eta)]+'&&'+ele0PtCuts['ele0PtBin'+str(idx_pt)]+')' ##probe0
            formula1='('+TnPCats['Tag0Pass1']+'&&'+ele1EtaCuts['ele1EtaBin'+str(idx_eta)]+'&&'+ele1PtCuts['ele1PtBin'+str(idx_pt)]+')' ##probe1
            cuts[cutname]='('+formula0+'||'+formula1+')'+'&&'+'('+MllCuts[Mll]+')'

            ##--Fail -> (Tag0Fail1&&ptetabin1) || (Tag1Fail0||ptetabin0)
            cutname='Fail__eleEtaBin'+str(idx_eta)+'__'+'elePtBin'+str(idx_pt)+'__'+Mll
            formula0='('+TnPCats['Tag1Fail0']+'&&'+ele0EtaCuts['ele0EtaBin'+str(idx_eta)]+'&&'+ele0PtCuts['ele0PtBin'+str(idx_pt)]+')' ##probe0
            formula1='('+TnPCats['Tag0Fail1']+'&&'+ele1EtaCuts['ele1EtaBin'+str(idx_eta)]+'&&'+ele1PtCuts['ele1PtBin'+str(idx_pt)]+')' ##probe1
            cuts[cutname]='('+formula0+'||'+formula1+')'+'&&'+'('+MllCuts[Mll]+')'



print "Ncuts=",len(cuts)

for c in sorted(cuts):
    print c, cuts[c]
