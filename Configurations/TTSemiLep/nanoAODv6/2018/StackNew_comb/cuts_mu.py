#-----Variable Deinition-----#
import sys
try:
  from WPandCut2018 import *
except ImportError:
  import os
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv6/2018/StackNew_comb"
  sys.path.append(BASE_PATH)
  from WPandCut2018 import *

#cuts={}

scriptname=opt.cutsFile

LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepCut="(  Lepton_pt[0]>30 \
&& ( fabs(Lepton_eta[0])  < 2.5*(abs(Lepton_pdgId[0])==11) \
||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
&& ( ( ( Alt$( Lepton_pt[1],-1) <= 10 || Alt$(Lepton_isLoose[1], -1)<=0.5)*( abs( Alt$(Lepton_pdgId[1], 11)) ==11 )  )\
||   ( ( Alt$( Lepton_pt[1],-1) <= 10 || Alt$(Lepton_isLoose[1], -1)<=0.5)*( abs( Alt$(Lepton_pdgId[1], 13)) ==13 ) )\
)\
)\
"
LepPtCut='(Lepton_pt[0] > ('+elePtCut+'*(abs(Lepton_pdgId[0])==11) + '+muPtCut+'*(abs(Lepton_pdgId[0])==13)) )'


#JetCut='nCleanJet30_2p5 >=4'

#------End of Variable Definition-----#
#supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut+'&&isFatJetEvent[0]'
#supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut+'&&'+JetCut
supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut
##---Lepton Categorization---##



LepCats={}
if 'ele' in scriptname:
    LepCats['eleCH']='(Lepton_isTightElectron_'+eleWP+'[0]>0.5)'
elif 'mu' in scriptname:
    LepCats['muCH']='(Lepton_isTightMuon_'+muWP+'[0]>0.5)'
else:
    LepCats={
        'sngCH':'1',
        'eleCH':'(Lepton_isTightElectron_'+eleWP+'[0]>0.5)',
        'muCH':'(Lepton_isTightMuon_'+muWP+'[0]>0.5)',
    }

##-----Basic categorization-----##

TopRegionCats={}
#TopRegionCats['Top4j'] = '1'
TopRegionCats['Top4j2b'] = '( nBJets_WP_M == 2)'
TopRegionCats['Top4j3b'] = '( nBJets_WP_M >= 3)'

HEMCats={}
#HEMCats['noHEMveto'] = '1'
HEMCats['HEMveto']   = '(((RunPeriod_HEM==3 || RunPeriod_HEM==4) && (HEMweight==1)) || (RunPeriod_HEM==1 || RunPeriod_HEM==2))'

common_cut = '(nCleanJet30_2p5 >=4) &&( nBJets_WP_M >= 2) && (METAlias > 20.)'
for LepCut in LepCats:
    for TopCut in TopRegionCats:
        for HEMcut in HEMCats:
                cut = "(%s && %s && %s && %s)"%(
                                                 common_cut,
                                                 LepCats[LepCut],
                                                 TopRegionCats[TopCut],
                                                 HEMCats[HEMcut],
                                               )
                cuts[LepCut+'__'+TopCut+'__'+HEMcut] = cut
#cuts['isVBF']='isVBF'
print "Ncuts=",len(cuts)

