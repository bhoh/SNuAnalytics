#-----Variable Deinition-----#
try:
  from WPandCut2017 import *
except ImportError:
  import os, sys
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv7/2017/StackNew_comb"
  sys.path.append(BASE_PATH)
  from WPandCut2017 import *


#------End of Variable Definition-----#
#variables={}
variables['EleSCEta'] = {
        'name' : 'Lepton_eta[0]+(Lepton_electronIdx[0]>=0)*Alt$(Electron_deltaEtaSC[(Lepton_electronIdx[0]>=0)*Lepton_electronIdx[0]],0)',
    'range':(50,-2.5,2.5),
    'xaxis':'1',
    'fold': 0
}

variables['MuonEta'] = {
    'name' : 'Lepton_eta[0]',
    'range':(48,-2.4,2.4),
    'xaxis':'1',
    'fold': 0
}

variables['EleSCEta_2l'] = {
    'name' : '(Iteration$<2 && abs(Lepton_pdgId)==11)*(Lepton_eta + Electron_deltaEtaSC[(Lepton_electronIdx>=0)*Lepton_electronIdx])+999*(Iteration$>=2 || abs(Lepton_pdgId)!=11)',
    'range':(50,-2.5,2.5),
    'xaxis':'1',
    'fold': 0
}

variables['MuonEta_2l'] = {
    # put 0 for negative Lepton_electronIdx. this can cause not zero events in muon channel.
    'name' : '(Iteration$<2 && abs(Lepton_pdgId)==13)*Lepton_eta + 999*(Iteration$>=2 || abs(Lepton_pdgId)!=13)',
    'range':(48,-2.4,2.4),
    'xaxis':'1',
    'fold': 0
}
variables['mll'] = {
     'name' : 'mll',
     'range':(40,0,200),
     'xaxis':'m_{ll}',
     'fold': 1
}





print "len(variables)=",len(variables)
