#-----Variable Deinition-----#
try:
  from WPandCut2016 import *
except ImportError:
  import os, sys
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv7/2016/StackNew_comb"
  sys.path.append(BASE_PATH)
  from WPandCut2016 import *


#------End of Variable Definition-----#
#variables={}

common_KF_cuts = '(status_nom==0)'
name_template = "{0}*({1}==1) + (-9999)*({1}==0)"
#( down_type_jet_b_tagged_nom>2 && down_type_jet_b_tagged_nom==1)


for key in ['hadronic_top_pt_nom']:
    variables[key.replace("_nom","")] = {
        'name': name_template.format(key,common_KF_cuts),
        'range':(60,0,600),
        'xaxis': key,
        'fold': 0
    }

variables['1st_leading_jet_pt']={
    'name' : 'Jet_pt_nom[SelectedJetIdx[0]]',
    'range':(50,30,600),
    'xaxis':'1^{st} leading jet P_{T} [GeV]',
    'fold':0

}
variables['1st_leading_jet_eta']={
    'name' : 'Jet_eta[SelectedJetIdx[0]]',
    'range':(50,-2.5,2.5),
    'xaxis':'1^{st} leading jet eta [GeV]',
    'fold':0

}
variables['Lepton_pt[0]']={
    'name' : 'Lepton_pt[0]',
    'range':(50,25,600),
    'xaxis':'Lepton P_{T} [GeV]',
    'fold':0

}
variables['Lepton_eta[0]']={
    'name' : 'Lepton_eta[0]',
    'range':(50,-2.5,2.5),
    'xaxis':'Lepton #eta',
    'fold':0
}
variables['Lepton_pt[1]']={
    'name' : 'Lepton_pt[1]',
    'range':(50,25,600),
    'xaxis':'Lepton P_{T} [GeV]',
    'fold':0

}
variables['Lepton_eta[1]']={
    'name' : 'Lepton_eta[1]',
    'range':(50,-2.5,2.5),
    'xaxis':'Lepton #eta',
    'fold':0
}

variables['PuppiMet']={
    'name' : 'MET_CHToCB_pt_nom',
    'range':(50,0,600),
    'xaxis':'MET [GeV]',
    'fold':0
}



print "len(variables)=",len(variables)
