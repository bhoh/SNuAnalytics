#-----Variable Deinition-----#
import sys
try:
  from WPandCut2017 import *
except ImportError:
  import os
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv5/v6_production/2017/NJET_biined_WJets/SKIM7/HMVar5"
  sys.path.append(BASE_PATH)
  from WPandCut2017 import *

#cuts={}


LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepCut="(  Lepton_pt[0]>30 \
&& ( fabs(Lepton_eta[0])  < 2.1*(abs(Lepton_pdgId[0])==11) \
||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
&& ( ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
||   ( Alt$( Lepton_pt[1],-1) < 10*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
)\
)"
LepPtCut='(Lepton_pt[0] > ('+elePtCut+'*(abs(Lepton_pdgId[0])==11) + '+muPtCut+'*(abs(Lepton_pdgId[0])==13)) )'


#------End of Variable Definition-----#
#supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut+'&&isFatJetEvent[0]'
supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut
#METtype="PuppiMET"
#supercut +='&&'+"( %s_pt > 20 )"%METtype

##---Lepton Categorization---##



LepCats={}
LepCats['Lep'] = '1'

##-----Basic categorization-----##

TopRegionCats={}
TopRegionCats['Top'] = '1'

#HEMweight={}
#HEMweight['HEMWeight']   = '( HEMweight )'

for LepCut in LepCats:
    for TopCut in TopRegionCats:
        cuts[LepCut+'__'+TopCut] = "(%s && %s)"%(
                                                  LepCats[LepCut],
                                                  TopRegionCats[TopCut]
                                                )

#cuts['isVBF']='isVBF'
print "Ncuts=",len(cuts)

