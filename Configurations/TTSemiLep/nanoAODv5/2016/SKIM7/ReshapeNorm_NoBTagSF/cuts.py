#-----Variable Deinition-----#
import sys
try:
  from WPandCut2016 import *
except ImportError:
  import os
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv5/2016/SKIM7"
  sys.path.append(BASE_PATH)
  from WPandCut2016 import *

#cuts={}


scriptname=opt.cutsFile

LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepCut="(  Lepton_pt[0]>27 \
&& ( fabs(Lepton_eta[0])  < 2.5*(abs(Lepton_pdgId[0])==11) \
||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
&& ( ( Alt$( Lepton_pt[1],-1) < 10*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
||   ( Alt$( Lepton_pt[1],-1) < 10*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
)\
)"
LepPtCut='(Lepton_pt[0] > ('+elePtCut+'*(abs(Lepton_pdgId[0])==11) + '+muPtCut+'*(abs(Lepton_pdgId[0])==13)) )'

JetCut='(nCleanJet20_2p4 >=4)'

#------End of Variable Definition-----#
supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut
supercut += "&&"+JetCut
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

