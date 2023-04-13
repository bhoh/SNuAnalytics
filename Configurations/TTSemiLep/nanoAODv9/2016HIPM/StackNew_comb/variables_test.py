#-----Variable Deinition-----#
try:
  from WPandCut2016 import *
except ImportError:
  import os, sys
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv9/2016HIPM/SKIM7"
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
    'range':(100,-5,5),
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
    'range':(100,-5,5),
    'xaxis':'2^{nd} leading lepton #eta',
    'fold':0
}

variables ['nCleanJet25_2p4']={
    'name' : 'nCleanJet25_2p4',
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

variables['PVs']={
    'name' : 'PV_npvs',
    'range':(80,0,80),
    'xaxis':'Number of primary vertices [GeV]',
    'fold': 1
}

variables['run_period']={
    'name' : 'run_period',
    'range':(10,0,10),
    'xaxis':'Run period',
    'fold': 1
}

variables['btagDeepFlavB']={
    'name' : 'Jet_btagDeepFlavB[SelectedJetIdx[0]]',
    'range':(100,-1,1),
    'xaxis':'btag score',
    'fold': 0
}

variables['1st_leading_jet_pt']={
    'name' : 'Jet_pt_nom[SelectedJetIdx[0]]',
    'range':(50,25,600),
    'xaxis':'1^{st} leading jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown','dbl_2j','dbl_4j','dbl_4j_eeORmmORemORme'],
    'fold':0

}

common_KF_cuts = '(status_nom==0)'
name_template = "{0}*({1}==1) + (-9999)*({1}==0)"
for key in ['hadronic_top_pt_nom']:
    variables[key.replace("_nom","")] = {
        'name': name_template.format(key,common_KF_cuts),
        'range':(60,0,600),
        'xaxis': 'hadronic top p_{T} [GeV]',
        'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown'],
        'fold': 0
    }















































































































































































































print "len(variables)=",len(variables)
