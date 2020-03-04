#-----Variable Deinition-----#
from WPandCut2017 import *


#------End of Variable Definition-----#
#variables={}


##---VBF---##
'''
variables['VBF_jjdEta']={
    'name':'VBF_jjdEta',
    'range':(100,0,10),
    'xaxis':'VBF_jjdEta',
    'fold': 0,

}


variables['VBF_Mjj']={
    'name':'VBF_Mjj',
    'range':(100,500,1000),
    'xaxis':'VBF_Mjj',
    'fold': 0,


}

'''

variables['WW_Mt']={
    'name' : 'WW_Mt',
    'range':(50,0,500),
    'xaxis':'WW_mass',
    'fold' : 0,
    
}




variables['WW_mass']={
    'name' : 'WW_mass',
    'range':(100,0,1000),
    'xaxis':'WW_mass',
    'fold' : 0,
    
}


variables['Event'] = {
    'name' : '1',
    'range':(1,0,2),
    'xaxis':'1',
    'fold': 0
}

'''
variables['NJet']={
    'name':'NJet',
    'range':(10,0,10),
    'xaxis':'NJet',
    'fold':0,
}

'''
variables['NBJet']={
    'name':'NBJet',
    'range':(5,0,5),
    'xaxis':'NBJet',
    'fold':0,
}
'''
variables['lepton_pt[0]']={
    'name' : 'Lepton_pt[0]',
    'range':(50,25,600),
    'xaxis':'lepton P_{T} [GeV]',
    'fold':0

}
variables['lepton_eta[0]']={
    'name' : 'Lepton_eta[0]',
    'range':(100,-5,5),
    'xaxis':'lepton #eta',
    'fold':0
}
'''


variables['bjet_'+bAlgo]={
    'name' : 'Jet_btag'+bAlgo,
    'range':(25,0,1),
    'xaxis':'bjet_'+bAlgo,
    'fold':0

}

variables['WlepPuppi_pt']={
    'name' : 'WlepPuppi_pt',
    'range':(100,0,1000),
    'xaxis':'WlepPuppi_pt',
    'fold':0
    
}



variables['PuppiMet']={
    'name' : 'PuppiMET_pt',
    'range':(50,0,600),
    'xaxis':'MET [GeV]',
    'fold':0
}

variables['Mt']={
    'name' : 'Mt[0]',
    'range':(100,0,300),
    'xaxis':'Mt [GeV]',
    'fold':0
}

variables ['PV_npvs']={
    'name' : 'PV_npvs',
    'range' : (80,0,80),
    'xaxis' : 'PV_npvs',
    'fold':0
}



variables['WResolved_pt']={
    'name':'WResolved_pt',
    'range':(100,0,1000),
    'xaxis' : 'WResolved_pt',
    'fold':0
}


'''
variables['WResolved_eta']={
    'name':'WResolved_eta',
    'range':(60,-3,3),
    'xaxis' : 'WResolved_eta',
    'fold':0
}

variables['WResolved_phi']={
    'name':'WResolved_phi',
    'range':(80,-4,4),
    'xaxis' : 'WResolved_phi',
    'fold':0
}
'''

variables['WResolved_mass']={
    'name':'WResolved_mass',
    'range':(42,40,250),
    'xaxis' : 'WResolved_mass',
    'fold':0
}

variables['WptOverMWW']={
    'name':'WptOverMWW',
    'range':(100,0,1),
    'xaxis':'WptOverMWW',
    'fold':0
}






print "len(variables)=",len(variables)
Nbin=0
for v in variables:
    #print v
    Nbin+=variables[v]['range'][0]

print "Nbin=",Nbin
