#-----Variable Deinition-----#
try:
  from WPandCut2018 import *
except ImportError:
  import os, sys
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv6/2018/SKIM5"
  sys.path.append(BASE_PATH)
  from WPandCut2018 import *


#------End of Variable Definition-----#
#variables={}

variables['Event'] = {
    'name' : '1',
    'range':(1,0,2),
    'xaxis':'1',
    'fold': 0
}
#variables['Whad_pt']={
#    'name':'Whad_pt',
#    'range':(100,0,1000),
#    'xaxis':'Whad_pt',
#    'fold': 0,
#
#}
#variables['Whad_mass']={
#    'name':'Whad_mass',
#    'range':(42,40,250),
#    'xaxis':'Whad_mass',
#    'fold': 0,
#
#}


#variables['nBJetResolved']={
#    'name':'Sum$(BJetResolved_cjidx)',
#    'range':(5,0,5),
#    'xaxis':'nBJetResolved',
#    'fold':0,
#}

variables['Lepton_pt[0]']={
    'name' : 'Lepton_pt[0]',
    'range':(50,25,600),
    'xaxis':'Lepton P_{T} [GeV]',
    'fold':0

}
variables['Lepton_eta[0]']={
    'name' : 'Lepton_eta[0]',
    'range':(100,-5,5),
    'xaxis':'Lepton #eta',
    'fold':0
}

#variables['bjet_'+bAlgo]={
#    'name' : 'Jet_btag'+bAlgo+'[CleanJet_jetIdx[BJetResolved_cjidx]]',
#    'range':(25,0,1),
#    'xaxis':'bjet_'+bAlgo,
#    'fold':0
#
#}

variables['PuppiMet']={
    'name' : 'PuppiMET_pt',
    'range':(50,0,600),
    'xaxis':'MET [GeV]',
    'fold':0
}

#variables['Wlep_Mt']={
#    'name' : 'Wlep_Mt',
#    'range':(100,0,300),
#    'xaxis':'Wlep_Mt',
#    'fold':0
#}
#variables['Wlep_mass']={
#    'name' : 'Wlep_mass',
#    'range':(100,0,300),
#    'xaxis':'Wlep_mass',
#    'fold':0
#}
#variables['Wlep_pt']={
#    'name' : 'Wlep_pt',
#    'range':(100,0,300),
#    'xaxis':'Wlep_pt',
#    'fold':0
#}

variables ['PV_npvs']={
    'name' : 'PV_npvs',
    'range' : (80,0,80),
    'xaxis' : 'PV_npvs',
    'fold':0
}

variables ['nCleanJet30_2p5']={
    'name' : 'nCleanJet30_2p5',
    'range' : (6,4,10),
    'xaxis' : 'jet multiplicity',
    'fold':0
}

#variables['lnjj_Mt_alt']={
#    'name': 'lnjj_Mt_alt',
#    'range':(100,0.,500.),
#    'xaxis': 'lnjj_Mt_alt',
#    'fold':1
#}
#variables['lnjj_mass']={
#    'name': 'lnjj_mass',
#    'range':([0,200,210,230,250,300,350,400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000],),
#    'divideByBinWidth':1,
#    'xaxis': 'lnjj_mass',
#    'fold':1
#}
#
#variables['minPtWOverMlnjj']={
#    'name':'minPtWOverMlnjj',
#    'range':(20,0,1),
#    'xaxis':'minPtWOverMlnjj',
#    'fold':0
#}
#
#variables['dR_l_Whad']={
#    'name':'dR_l_Whad',
#    'range':(50,0,5),
#    'xaxis':'dR_l_Whad',
#    'fold':0,
#}
#variables['dR_Wlep_Whad']={
#    'name':'dR_Wlep_Whad',
#    'range':(50,0,5),
#    'xaxis':'dR_Wlep_Whad',
#    'fold':0,
#}
#
#
#variables['dPhi_l_Whad']={
#    'name':'dPhi_l_Whad',
#    'range':(50,0,5),
#    'xaxis':'dPhi_l_Whad',
#    'fold':0,
#}
#variables['dPhi_Wlep_Whad']={
#    'name':'dPhi_Wlep_Whad',
#    'range':(50,0,5),
#    'xaxis':'dPhi_Wlep_Whad',
#    'fold':0,
#}




print "len(variables)=",len(variables)
