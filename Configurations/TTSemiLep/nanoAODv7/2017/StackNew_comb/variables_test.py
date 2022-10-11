#-----Variable Deinition-----#
try:
  from WPandCut2016 import *
except ImportError:
  import os, sys
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv5/2016/SKIM7"
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

variables['Lepton_pt[0]']={
    'name' : 'Lepton_pt[0]',
    'range':(50,15,600),
    'xaxis':'1^{st} leading lepton P_{T} [GeV]',
    'fold':0

}
variables['Lepton_eta[0]']={
    'name' : 'Lepton_eta[0]',
    'range':(20,-3,3),
    'xaxis':'1^{st} leading lepton #eta',
    'fold':0
}

variables['Lepton_pt[1]']={
    'name' : 'Lepton_pt[1]',
    'range':(50,15,600),
    'xaxis':'2^{nd} leading lepton P_{T} [GeV]',
    'fold':0

}
variables['Lepton_eta[1]']={
    'name' : 'Lepton_eta[1]',
    'range':(20,-3,3),
    'xaxis':'2^{nd} leading lepton #eta',
    'fold':0
}

variables ['nCleanJet_2p4']={
    'name' : 'nCleanJet_2p4',
    'range' : (8,2,10),
    'xaxis' : 'jet multiplicity',
    'fold':0
}

variables ['nBJets_WP_M']={
    'name' : 'nBJets_WP_M',
    'range' : (6,2,8),
    'xaxis' : 'b tagged jet multiplicity',
    'fold':0
}

variables['PuppiMet']={
    'name' : 'MET_CHToCB_pt_nom',
    'range':(50,0,600),
    'xaxis':'MET [GeV]',
    'fold':0
}

variables['OTF_SingleEleTrig_SF']={
    'name' : 'OTF_SingleEleTrig_SF',
    'range':(100,0,2.0),
    'xaxis':'SF',
    'fold':0
}
#aliases['OTF_SingleEleTrig_SF'] = {









































































































































































































































print "len(variables)=",len(variables)
