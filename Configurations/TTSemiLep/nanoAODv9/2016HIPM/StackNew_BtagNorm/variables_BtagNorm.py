#-----Variable Deinition-----#
try:
  from WPandCut2016 import *
except ImportError:
  import os, sys
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv9/2016/StackNew_BtagNorm"
  sys.path.append(BASE_PATH)
  from WPandCut2016 import *


#------End of Variable Definition-----#
#variables={}

variables['Event'] = {
    'name' : '1',
    'range':(1,0,2),
    'xaxis':'1',
    'fold': 0
}

variables ['nCleanJet25_2p4']={
    'name' : 'nCleanJet25_2p4',
    'range' : (8,2,10),
    'xaxis' : 'jet multiplicity',
    'fold':0
}

variables ['nBJets_WP_M']={
    'name' : 'nBJets_WP_M',
    'range' : (8,0,8),
    'xaxis' : 'b tagged jet multiplicity',
    'fold':0
}

variables['btagDeepFlavB']={
    'name' : 'Jet_btagDeepFlavB[SelectedJetIdx[0]]',
    'range':(100,-1,1),
    'xaxis':'btag score',
    'fold': 1
}



print "len(variables)=",len(variables)
