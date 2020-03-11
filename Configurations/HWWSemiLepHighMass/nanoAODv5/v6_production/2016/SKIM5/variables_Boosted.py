#-----Variable Deinition-----#
from WPandCut2016 import *


#------End of Variable Definition-----#
#variables={}

variables['Event'] = {
    'name' : '1',
    'range':(1,0,2),
    'xaxis':'1',
    'fold': 0
}
variables['WtaggerFatjet_pt']={
    'name':'WtaggerFatjet_pt',
    'range':(100,0,1000),
    'xaxis':'WtaggerFatjet_pt',
    'fold': 0,

}
variables['WtaggerFatjet_mass']={
    'name':'WtaggerFatjet_mass',
    'range':(42,40,250),
    'xaxis':'WtaggerFatjet_mass',
    'fold': 0,

}
variables['WtaggerFatjet_tau21']={
    'name':'WtaggerFatjet_tau21',
    'range':(100,0,1),
    'xaxis':'WtaggerFatjet_tau21',
    'fold': 0,

}



variables['nBJetBoosted']={
    'name':'nBJetBoosted',
    'range':(5,0,5),
    'xaxis':'nBJetBoosted',
    'fold':0,
}

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

variables['bjet_'+bAlgo]={
    'name' : 'Jet_btag'+bAlgo+'[CleanJet_jetIdx[BJetBoosted_cjidx]]',
    'range':(25,0,1),
    'xaxis':'bjet_'+bAlgo,
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
    'range':(60,0,300),
    'xaxis':'Wlep_Mt',
    'fold':0
}
variables['Wlep_mass']={
    'name' : 'Wlep_mass',
    'range':(60,0,300),
    'xaxis':'Wlep_mass',
    'fold':0
}
variables['Wlep_pt']={
    'name' : 'Wlep_pt',
    'range':(100,0,300),
    'xaxis':'Wlep_pt',
    'fold':0
}

variables ['PV_npvs']={
    'name' : 'PV_npvs',
    'range' : (80,0,80),
    'xaxis' : 'PV_npvs',
    'fold':0
}


variables['minPtWOverMlnJ_MW']={
    'name':'minPtWOverMlnJ_MW',
    'range':(20,0,100),
    'xaxis':'minPtWOverMlnJ_MW',
    'fold':0
}

variables['lnJ_mass_MW']={
    'name': 'lnJ_mass_MW',
    'range':([0,200,210,230,250,300,350,400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000],),
    'divideByBinWidth':1,
    'xaxis': 'lnJ_mass_MW',
    'fold':1
}

##--For cut stury
variables['dR_l_F_MW']={
    'name': 'dR_l_F_MW',
    'range':(50,0,5),
    'xaxis': 'dR_l_F_MW',
    'fold':1
}
variables['dR_Wlep_F_MW']={
    'name': 'dR_Wlep_F_MW',
    'range':(50,0,5),
    'xaxis': 'dR_Wlep_F_MW',
    'fold':1
}
variables['dPhi_l_F_MW']={
    'name': 'dPhi_l_F_MW',
    'range':(50,0,5),
    'xaxis': 'dR_l_F_MW',
    'fold':1
}
variables['dPhi_Wlep_F_MW']={
    'name': 'dR_Wlep_F_MW',
    'range':(50,0,5),
    'xaxis': 'dR_Wlep_F_MW',
    'fold':1
}

'''
for sel in FatSel:
    #CleanFatJet_mass[FinalFatJet_'+sel+'_cfjidx]
    variables['CleanFatJet_pt[FinalFatJet_'+sel+'_cfjidx']={
        'name':'CleanFatJet_pt[FinalFatJet_'+sel+'_cfjidx]',
        'range':(100,0,1000),
        'xaxis':'CleanFatJet_pt[FinalFatJet_'+sel+'_cfjidx]',
        'fold': 0,

    }
    variables['CleanFatJet_mass[FinalFatJet_'+sel+'_cfjidx]']={
        'name':'CleanFatJet_mass[FinalFatJet_'+sel+'_cfjidx]',
        'range':(42,40,250),
        'xaxis':'CleanFatJet_mass[FinalFatJet_'+sel+'_cfjidx]',
        'fold': 0,

    }
    variables['CleanFatJet_tau21[FinalFatJet_'+sel+'_cfjidx]']={
        'name':'CleanFatJet_tau21[FinalFatJet_'+sel+'_cfjidx]',
        'range':(100,0,1),
        'xaxis':'CleanFatJet_tau21[FinalFatJet_'+sel+'_cfjidx]',
        'fold': 0,

    }

    variables['lnJ_mass_'+sel]={
        'name': 'lnJ_mass_'+sel,
        'range':([0,200,210,230,250,300,350,400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000],),
        'divideByBinWidth':1,
        'xaxis': 'lnJ_mass_'+sel,
        'fold':1
    }
'''



print "len(variables)=",len(variables)
