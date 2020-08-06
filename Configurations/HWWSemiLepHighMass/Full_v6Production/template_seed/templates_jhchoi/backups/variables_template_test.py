variables={}
isFinal=True
#isFinal=True
print "isFinal=",isFinal
import os
import sys
sys.path.append(os.getcwd())


#-----Variable Deinition-----#
from WPandCut2016 import *

if 'opt' in globals():
    configration_py=opt.variablesFile
else:
    configration_py=sys.argv[0]
print "configration_py=",configration_py

Boosted=False
Resolved=False
if 'Boosted' in configration_py:
    Boosted=True
if 'Resolved' in configration_py:
    Resolved=True
#scriptname=opt.variablesFile

#------End of Variable Definition-----#
#variables={}

variables['Event'] = {
    'name' : '1',
    'range':(1,0,2),
    'xaxis':'1',
    'fold': 3,
}
##Wtagger kin##

variables['HadronicW_pt']={
    'name':'HadronicW_pt',
    #'range':(100,0,1000),
    'range':([200,230,260,290,320,350,380,410,500,700,1000],),
    'xaxis':'P_{T}(Hadronic W boson) [GeV]',
    'fold': 3,

}

variables['HadronicW_mass']={
    'name':'HadronicW_mass',
    'range':([40,45,50,55,65,70,75,80,85,90,95,100,105,110,115,120,125,130,150,170,200,250],),
    'xaxis':'M(Hadronic W boson) [GeV]',
    'fold': 3,
}

##Change range of Wmass -> SR/TOP : Wmass 65-105
if ('TOP' in configration_py) or ('SR' in configration_py) :
    variables['HadronicW_mass']['range']=(8,65,105)



variables['HadronicW_Score']={
    'name':'HadronicW_Score',
    'range':(20,0,1),
    'xaxis':'HadronicW_Score',
    'fold': 3,
    
}
if Boosted:
    if 'HP' in WTAG:
        variables['HadronicW_Score']['xaxis']='#tau_{21}'
    if 'DDT' in WTAG:
        variables['WtaggerFatjet_'+WTAG+'_nom_tau21ddt']['xaxis']+='(DDT)'
    if 'DeepAK8' in WTAG:
        variables['HadronicW_Score']['xaxis']='deepTagAK8'
            

##--Bjet

variables['nBJet']={
    'name':'nBJet',
    'range':(5,0,5),
    'xaxis':'number of btagged AK4 Jet',
    'fold':3,
}


variables['nJet']={
    'name':'nJet',
    'range':(10,0,10),
    'xaxis':'number of AK4 Jet',
    'fold':3,
}
variables['nJet_eta4p7']={
    'name':'nJet_eta4p7',
    'range':(10,0,10),
    'xaxis':'number of AK4 Jet',
    'fold':3,
}
variables['nAddJet']={
    'name':'nAddJet',
    'range':(10,0,10),
    'xaxis':'number of AK4 Jet Not Wtagged',
    'fold':3,
}

variables['AddJet_pt']={
    'name':'AddJet_pt',
    'range':(100,25,600),
    'xaxis':'P_{T}(AK4 Jet Not Wtagged) [GeV]',
    'fold':3,
}


variables['AddJet_eta']={
    'name':'AddJet_eta',
    'range':(30,-5,5),
    'xaxis':'#eta(AK4 Jet Not Wtagged)',
    'fold':3,
}

variables['Lepton_pt[0]']={
    'name' : 'Lepton_pt[0]',
    'range':(20,25,600),
    'xaxis':'P_{T}(Lepton) [GeV]',
    'fold':3

}
variables['Lepton_eta[0]']={
    'name' : 'Lepton_eta[0]',
    'range':(30,-5,5),
    'xaxis':'#eta(Lepton)',
    'fold':3
}



variables[bAlgo]={
    'name' : 'Jet_btag'+bAlgo+'[CleanJet_jetIdx[AddJetBoost_'+WTAG+'_nom_cjidx]]',
    'range':(20,0,1),
    'xaxis':bAlgo+'(AK4 Jet Not Wtagged)',
    'fold':3

}

variables['PuppiMet']={
    'name' : 'PuppiMET_nom_pt',
    'range':(30,0,600),
    'xaxis':'PuppiMET [GeV]',
    'fold':3
}

variables['Wlep_Mt']={
    'name' : 'Wlep_nom_Mt',
    'range':(20,0,200),
    'xaxis':'M_{T}(LeptonicW) [GeV]',
    'fold':3
}

variables['Wlep_nom_pt']={
    'name' : 'Wlep_nom_pt',
    'range':(35,150,500),
    'xaxis':'P_{T}(LeptonicW) [GeV]',
    'fold':3
}

variables['Wlep_nom_mass']={
    'name' : 'Wlep_nom_mass',
    'range':(10,70,90),
    'xaxis':'M(LeptonicW) [GeV]',
    'fold':3
}


variables ['PV_npvs']={
    'name' : 'PV_npvs',
    'range' : (80,0,80),
    'xaxis' : 'PV_npvs',
    'fold':0
}


variables['MWW_pt_over_mass']={
    'name':'MWW_pt_over_mass',
    'range':(20,0,1),
    'xaxis':'min(P_T{W}/M(WW))',
    'fold':0
}

variables['dEta_jj_VBF']={
    'name':'dEta_jj_VBF',
    'range':(20,0,8),
    'xaxis':'#delta(#eta)(jj) VBF',
    'fold':3
}
variables['mass_jj_VBF']={
    'name':'mass_jj_VBF',
    'range':(40,0,1400),
    'xaxis':'M(jj) VBF [GeV])',
    'fold':3
}


if Boosted:
    for M_MELA in MELA_MASS_BOOST:
        for C in MELA_C_BOOST:
        
            #'MEKD_'+str(M)    
            M=str(M_MELA)
            C=str(C)
            variables['MEKD_Bst_C_'+C+'_M'+str(M)]={
                'name':'MEKD_Bst_C_'+C+'_M'+str(M),
                'range':(10,0,1),
                'xaxis':'MELA KD',
                'fold':0
            }
if Resolved:
    for M_MELA in MELA_MASS_RESOL:
        for C in MELA_C_RESOL:
        
            #'MEKD_'+str(M)    
            M=str(M_MELA)
            C=str(C)
            variables['MEKD_Bes_C_'+C+'_M'+str(M)]={
                'name':'MEKD_Bes_C_'+C+'_M'+str(M),
                'range':(10,0,1),
                'xaxis':'MELA KD',
                'fold':0
            }


if isFinal: variables={}

variables['MWW']={
    'name': 'MWW',
    'range':([0,400,450,500,550,600,650,700,750,800,900,1000,1500,2000,4000],),
    'divideByBinWidth':1,
    'xaxis': 'M(WW) [GeV]',
    'fold':3
}
variables['Event'] = {
    'name' : '1',
    'range':(1,0,2),
    'xaxis':'1',
    'fold': 3
}

if (not 'SR' in configration_py):
    variables['MWW']['range']=(40,200,1000)





print "len(variables)=",len(variables)
for v in variables:
    print variables[v]['name'] 

