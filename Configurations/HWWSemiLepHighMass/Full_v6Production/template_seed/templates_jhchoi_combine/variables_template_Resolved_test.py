variables={}
#OnlyFinalVariable=True
#OnlyFinalVariable=True






import os
import sys
sys.path.append(os.getcwd())


#-----Variable Deinition-----#
from WPandCut2016 import *

print "OnlyFinalVariable=",OnlyFinalVariable

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
            
if Resolved:
    variables['HadronicW_Score']['xaxis']='#chi^{2}'
    if 'chi2' in ALGO :
        variables['HadronicW_Score']['range']=(40,0,200)
    else:
        variables['HadronicW_Score']['range']=(40,0,40)
##--nBjet

variables['nBJet']={
    'name':'nBJet',
    'range':(5,0,5),
    'xaxis':'number of btagged AK4 Jet',
    'fold':3,
}



##--ak4jet
variables['nAK4Jet']={
    'name':'nAK4Jet',
    'range':(10,0,10),
    'xaxis':'number of AK4 Jet',
    'fold':3,
}
variables['nAK4Jet_eta4p7']={
    'name':'nAK4Jet_eta4p7',
    'range':(10,0,10),
    'xaxis':'number of AK4 Jet',
    'fold':3,
}
##--leading ak4jet
variables['LeadingJet_pt']={
    'name':'LeadingJet_pt',
    'range':(100,25,600),
    'xaxis':'P_{T}(Leading AK4 Jet) [GeV]',
    'fold':3,
}
variables['LeadingJet_eta']={
    'name':'LeadingJet_eta',
    'range':(30,-5,5),
    'xaxis':'#eta(Leading AK4 Jet)',
    'fold':3,
}
variables['LeadingJet_BtagScore']={
    'name':'LeadingJet_BtagScore',
    'range':(20,0,1),
    'xaxis':bAlgo+'(Leading AK4 Jet)',
    'fold':3,
}
##--subleading ak4jets
variables['SubLeadingJet_pt']={
    'name':'SubLeadingJet_pt',
    'range':(100,25,600),
    'xaxis':'P_{T}(SubLeading AK4 Jet) [GeV]',
    'fold':3,
}
variables['SubLeadingJet_eta']={
    'name':'SubLeadingJet_eta',
    'range':(30,-5,5),
    'xaxis':'#eta(SubLeading AK4 Jet)',
    'fold':3,
}
variables['SubLeadingJet_BtagScore']={
    'name':'SubLeadingJet_BtagScore',
    'range':(20,0,1),
    'xaxis':bAlgo+'(SubLeading AK4 Jet)',
    'fold':3,
}


##---ak4jet not in Wtag
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
variables['AddJet_BtagScore']={
    'name':'AddJet_BtagScore',
    'range':(20,0,1),
    'xaxis':bAlgo+'(AK4 Jet Not Wtagged)',
    'fold':3,
}

##--Leading addjet
variables['LeadingAddJet_pt']={
    'name':'LeadingAddJet_pt',
    'range':(100,25,600),
    'xaxis':'P_{T}(1st AK4 Jet Not Wtagged) [GeV]',
    'fold':3,
}
variables['LeadingAddJet_eta']={
    'name':'LeadingAddJet_eta',
    'range':(30,-5,5),
    'xaxis':'#eta(1st AK4 Jet Not Wtagged)',
    'fold':3,
}
variables['LeadingAddJet_BtagScore']={
    'name':'LeadingAddJet_BtagScore',
    'range':(20,0,1),
    'xaxis':bAlgo+'(1stAK4 Jet Not Wtagged)',
    'fold':3,
}
##--Subleading addjet
variables['SubLeadingAddJet_pt']={
    'name':'SubLeadingAddJet_pt',
    'range':(100,25,600),
    'xaxis':'P_{T}(2nd AK4 Jet Not Wtagged) [GeV]',
    'fold':3,
}
variables['SubLeadingAddJet_eta']={
    'name':'SubLeadingAddJet_eta',
    'range':(30,-5,5),
    'xaxis':'#eta(2nd AK4 Jet Not Wtagged)',
    'fold':3,
}
variables['SubLeadingAddJet_BtagScore']={
    'name':'SubLeadingAddJet_BtagScore',
    'range':(20,0,1),
    'xaxis':bAlgo+'(2nd AK4 Jet Not Wtagged)',
    'fold':3,
}


##--Lepton
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

##--MET


variables[METtype]={
    'name' : METtype+'_nom_pt',
    'range':(30,0,600),
    'xaxis':METtype+' [GeV]',
    'fold':3
}


##--Leptonic W
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

##-nPV
variables ['PV_npvs']={
    'name' : 'PV_npvs',
    'range' : (80,0,80),
    'xaxis' : 'PV_npvs',
    'fold':0
}

##--WW
variables['WW_pt_over_mass']={
    'name':'WW_pt_over_mass',
    'range':(20,0,1),
    'xaxis':'min(P_T{W}/M(WW))',
    'fold':0
}
variables['WW_mass']={
    'name': 'WW_mass',
    'range':([0,400,450,500,550,600,650,700,750,800,900,1000,1500,2000,4000],),
    'divideByBinWidth':1,
    'xaxis': 'M(WW) [GeV]',
    'fold':3
}
if (not 'SR' in configration_py):
    variables['WW_mass']['range']=(40,200,1000)

if Resolved:
    variables['WW_Mt']={
        'name': 'WW_Mt',
        'range':(20,0,200),
        #'divideByBinWidth':1,
        'xaxis': 'M_{T}(WW) [GeV]',
        'fold':3
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
            variables['MEKD_Res_C_'+C+'_M'+str(M)]={
                'name':'MEKD_Res_C_'+C+'_M'+str(M),
                'range':(10,0,1),
                'xaxis':'MELA KD',
                'fold':0
            }


if OnlyFinalVariable: 
    VtoDraw=['WW_mass','Event']
    for v in sorted(variables):
        if v in VtoDraw: continue
        del variables[v]





print "len(variables)=",len(variables)
for v in variables:
    print v

