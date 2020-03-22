#-----Variable Deinition-----#
import sys
try:
  from WPandCut2018 import *
except ImportError:
  import os
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv6/2018/SKIM5"
  sys.path.append(BASE_PATH)
  from WPandCut2018 import *

#cuts={}


scriptname=opt.cutsFile

LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepCut="(  Lepton_pt[0]>30 \
&& ( fabs(Lepton_eta[0])  < 2.1*(abs(Lepton_pdgId[0])==11) \
||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
&& ( ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
||   ( Alt$( Lepton_pt[1],-1) < 10*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
)\
)"
LepPtCut='(Lepton_pt[0] > ('+elePtCut+'*(abs(Lepton_pdgId[0])==11) + '+muPtCut+'*(abs(Lepton_pdgId[0])==13)) )'

SingleLepTrigCut = "(  (abs(Lepton_pdgId[0])==11)*(Trigger_sngEl && !Trigger_sngMu)\
|| (abs(Lepton_pdgId[0])==13)*(!Trigger_sngEl && Trigger_sngMu)\
)"



JetCut='nCleanJet30_2p5 >=4'

#------End of Variable Definition-----#
#supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut+'&&isFatJetEvent[0]'
supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut+'&&'+JetCut
METtype="PuppiMET"
supercut +='&&'+"( %s_pt > 20 )"%METtype

##---Lepton Categorization---##



LepCats={}
if 'ele' in scriptname:
    LepCats['eleCH']='(Lepton_isTightElectron_'+eleWP+'[0]>0.5)'
elif 'mu' in scriptname:
    LepCats['muCH']='(Lepton_isTightMuon_'+muWP+'[0]>0.5)'
else:
    LepCats={
        #'_':'1',
        'eleCH':'(Lepton_isTightElectron_'+eleWP+'[0]>0.5)',
        'muCH':'(Lepton_isTightMuon_'+muWP+'[0]>0.5)',
    }

##-----Basic categorization-----##

TopRegionCats={}
TopRegionCats['Top4j'] = '1'
TopRegionCats['Top4j2b'] = '( nBJets_WP_M == 2)'
TopRegionCats['Top4j3b'] = '( nBJets_WP_M >= 3)'

#HEMweight={}
#HEMweight['HEMnoWeight'] = '( 1 )'
#HEMweight['HEMWeight']   = '( HEMweight )'
TrigCuts={}
TrigCuts['noTrigDecision'] = '( 1 )'
TrigCuts['TrigDecision'] = SingleLepTrigCut

for LepCut in LepCats:
    for TopCut in TopRegionCats:
        for TrigCut in TrigCuts:
            cuts[LepCut+'__'+TopCut+'__'+TrigCut] = "(%s && %s)*%s"%(
                                                                      LepCats[LepCut],
                                                                      TopRegionCats[TopCut],
                                                                      TrigCuts[TrigCut]
                                                                   )

#cuts['isVBF']='isVBF'
print "Ncuts=",len(cuts)

