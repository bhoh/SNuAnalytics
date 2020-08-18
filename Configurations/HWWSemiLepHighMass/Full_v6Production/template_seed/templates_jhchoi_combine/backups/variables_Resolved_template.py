isFinal=True
print "isFinal=",isFinal
import os
import sys
sys.path.append(os.getcwd())

#-----Variable Deinition-----#
CUTFLOW=False
from WPandCut2016 import *

if 'opt' in globals():
    configration_py=opt.variablesFile
else:
    configration_py=sys.argv[0]
print "configration_py=",configration_py


_ALGO="_"+ALGO
_ALGO_="_"+ALGO+"_"
#------End of Variable Definition-----#
#variables={}

variables['Event'] = {
    'name' : '1',
    'range':(1,0,2),
    'xaxis':'1',
    'fold': 3
}

variables['Whad'+_ALGO_+'nom_pt']={
    'name':'Whad'+_ALGO_+'nom_pt',
    'range':(25,150,400),#10gev
    'xaxis':'Whad_pt',
    'fold': 3,

}

variables['Whad'+_ALGO_+'nom_mass']={
    'name':'Whad'+_ALGO_+'nom_mass',
    'range':([40,45,50,55,65,70,75,80,85,90,95,100,105,110,115,120,125,130,150,170,200,250],),
    'xaxis':'Whad_mass',
    'fold': 3,

}
if ('TOP' in configration_py) or ('SR' in configration_py) :
    variables['Whad'+_ALGO_+'nom_mass']['range']=(8,65,105)


variables['nBJetResol'+_ALGO_+'nom']={
    'name':'nBJetResol'+_ALGO_+'nom',
    'range':(5,0,5),
    'xaxis':'nBJetResol'+_ALGO_+'nom',
    'fold':3,
}


variables['nAddJetResol'+_ALGO_+'nom']={
    'name':'nAddResol'+_ALGO_+'nom',
    'range':(10,0,10),
    'xaxis':'nAddJetResol',
    'fold':3,
}

variables['JetMultplicity']={
    'name':'JetMultplicity',
    'range':(10,0,10),
    'xaxis':'JetMultplicity',
    'fold':3,
}
variables['JetMultplicity_eta4p7']={
    'name':'JetMultplicity_eta4p7',
    'range':(10,0,10),
    'xaxis':'JetMultplicity_eta4p7',
    'fold':3,
}


variables['Lepton_pt[0]']={
    'name' : 'Lepton_pt[0]',
    'range':(30,0,300), #12GeV
    'xaxis':'Lepton P_{T} [GeV]',
    'fold':3

}
variables['Lepton_eta[0]']={
    'name' : 'Lepton_eta[0]',
    'range':(30,-5,5),
    'xaxis':'Lepton #eta',
    'fold':3
}



variables ['PV_npvs']={
    'name' : 'PV_npvs',
    'range' : (80,0,80),
    'xaxis' : 'PV_npvs',
    'fold':3
}


variables[bAlgo]={
    'name' : 'Jet_btag'+bAlgo+'[CleanJet_jetIdx[AddJetResol_'+ALGO+'_nom_cjidx]]',
    'range':(20,0,1),
    'xaxis':bAlgo,
    'fold':3

}

variables['PuppiMet']={
    'name' : 'PuppiMET_nom_pt',
    'range':(30,0,300),
    'xaxis':'MET [GeV]',
    'fold':3
}

variables['Wlep_Mt']={
    'name' : 'Wlep_nom_Mt',
    'range':(20,0,200),
    'xaxis':'Wlep_Mt',
    'fold':3
}
variables['Wlep_nom_mass']={
    'name' : 'Wlep_nom_mass',
    'range':(15,70,100),
    'xaxis':'Wlep_mass',
    'fold':3
}

variables['Wlep_nom_pt']={
    'name' : 'Wlep_nom_pt',
    'range':(60,100,400),
    'xaxis':'Wlep_pt',
    'fold':3
}



variables['lnjj'+_ALGO_+'nom_minPtWOverM']={
    'name':'lnjj'+_ALGO_+'nom_minPtWOverM',
    'range':(20,0,1),
    'xaxis':'minPtWOverMlnjj',
    'fold':3
}

for M_MELA in MELA_MASS_RESOL:
    for C in MELA_C_RESOL:
        #'MEKD_'+str(M)        
        C=str(C)
        M=str(M_MELA)
        variables['MEKD_Res_C_'+C+'_M'+str(M)]={
            'name':'MEKD_Res_C_'+C+'_M'+str(M),
            'range':(10,0,1),
            'xaxis':'MEKD_Res_C_'+C+'_M'+str(M),
            'fold':3
        }



variables['VBFjjResol_dEta_'+ALGO+'_nom']={
    'name':'VBFjjResol_dEta_'+ALGO+'_nom',
    'range':(20,0,8),
    'xaxis':'VBFjjResol_dEta_'+ALGO+'_nom',
    'fold':3
}
variables['VBFjjResol_mjj_'+ALGO+'_nom']={
    'name':'VBFjjResol_mjj_'+ALGO+'_nom',
    'range':(40,0,1400),
    'xaxis':'VBFjjResol_mjj_'+ALGO+'_nom',
    'fold':3
}



if isFinal:
    variables={}


variables['lnjj'+_ALGO_+'nom_mass']={
    'name': 'lnjj'+_ALGO_+'nom_mass',
    'range':([0,200,210,230,250,300,350,400,450,500,550,600,650,700,750,800,900,1000,1500,2000,4000],),
    #'divideByBinWidth':1,
    'xaxis': 'lnjj_mass',
    'fold':3
}

if not ('SR' in configration_py):
    variables['lnjj'+_ALGO_+'nom_mass']['range']=(40,200,1000)


variables['Event'] = {
    'name' : '1',
    'range':(1,0,2),
    'xaxis':'1',
    'fold': 3
}


if CUTFLOW:
    variables={}
    variables['Event'] = {
        'name' : '1',
        'range':(1,0,2),
        'xaxis':'1',
        'fold': 0
    }





print "len(variables)=",len(variables)
