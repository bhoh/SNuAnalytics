#-----Variable Deinition-----#
from WPandCut2017 import *


#------End of Variable Definition-----#
#variables={}

variables['Event'] = {
    'name' : '1',
    'range':(1,0,2),
    'xaxis':'1',
    'fold': 0
}

variables['nJetPassBKin']={
    'name':'nJetPassBKin',
    'range':(10,0,10),
    'xaxis':'nJetPassBKin',
    'fold':0,
}


variables['Lepton_pt[0]']={
    'name' : 'Lepton_pt[0]',
    'range':(50,25,600),
    'xaxis':'Lepton P_{T} [GeV]',
    'fold':0

}


variables['Lepton_pt[1]']={
    'name' : 'Alt$(Lepton_pt[1],-1)',
    'range':(50,0,100),
    'xaxis':'Lepton P_{T} [GeV]',
    'fold':0

}


variables['Lepton_eta[0]']={
    'name' : 'Lepton_eta[0]',
    'range':(100,-5,5),
    'xaxis':'Lepton #eta',
    'fold':0
}

variables['ak4Jet_pt']={
    'name' : 'CleanJet_pt',
    'range':(50,25,600),
    'xaxis':'ak4Jet_pt',
    'fold':0

}


variables['ak4Jet_eta']={
    'name' : 'CleanJet_eta',
    'range':(50,-5,5),
    'xaxis':'ak4Jet_eta',
    'fold':0

}


variables[bAlgo]={
    'name' : 'Jet_btag'+bAlgo+'[CleanJet_jetIdx]',
    'range':(25,0,1),
    'xaxis':bAlgo,
    'fold':0

}

variables['PuppiMet']={
    'name' : 'PuppiMET_pt',
    'range':(50,0,600),
    'xaxis':'MET [GeV]',
    'fold':0
}

variables['Wlep_Mt']={
    'name' : 'Wlep_Mt',
    'range':(100,0,300),
    'xaxis':'Wlep_Mt',
    'fold':0
}

variables['Wlep_Mt_50To110']={
    'name' : 'Wlep_Mt',
    'range':(60,50,110),
    'xaxis':'Wlep_Mt',
    'fold':0
}

variables ['PV_npvs']={
    'name' : 'PV_npvs',
    'range' : (80,0,80),
    'xaxis' : 'PV_npvs',
    'fold':0
}



print "len(variables)=",len(variables)
