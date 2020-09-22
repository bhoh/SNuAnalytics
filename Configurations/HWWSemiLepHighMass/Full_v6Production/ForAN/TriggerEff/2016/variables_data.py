variables={}




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


#------End of Variable Definition-----#
#variables={}

variables['Event'] = {
    'name' : '1',
    'range':(1,0,2),
    'xaxis':'1',
    'fold': 3,
}
##--Lepton
variables['TagLepton_pt']={
    'name' : '(eleTrigMatch0 && (Lepton_isTightElectron_'+eleTagWP+'[0]>0.5) && (Lepton_pt[0]> 35.))*Lepton_pt[0] +\
    !(eleTrigMatch0 && (Lepton_isTightElectron_'+eleTagWP+'[0]>0.5) && (Lepton_pt[0]> 35.))*(eleTrigMatch1 && (Lepton_isTightElectron_'+eleTagWP+'[1]>0.5) && (Lepton_pt[1] > 35.))*Lepton_pt[1]',
    'range':(200,0,200),
    'xaxis':'P_{T}(TagLepton) [GeV]',
    'fold':3

}

variables['TagLepton_eta']={
    'name' : '(eleTrigMatch0 && (Lepton_isTightElectron_'+eleTagWP+'[0]>0.5) && (Lepton_pt[0]> 35.))*Lepton_eta[0] +\
    !(eleTrigMatch0 && (Lepton_isTightElectron_'+eleTagWP+'[0]>0.5) && (Lepton_pt[0]> 35.))*(eleTrigMatch1 && (Lepton_isTightElectron_'+eleTagWP+'[1]>0.5) && (Lepton_pt[1] > 35.))*Lepton_eta[1]',
    'range':(100,-2.5,2.5),
    'xaxis':'#eta(Lepton)',
    'fold':3

}


variables['ProbeLepton_pt']={
    'name' : '(eleTrigMatch0 && (Lepton_isTightElectron_'+eleTagWP+'[0]>0.5) && (Lepton_pt[0]> 35.))*Lepton_pt[1] +\
    !(eleTrigMatch0 && (Lepton_isTightElectron_'+eleTagWP+'[0]>0.5) && (Lepton_pt[0]> 35.))*(eleTrigMatch1 && (Lepton_isTightElectron_'+eleWP+'[1]>0.5) && (Lepton_pt[1] > 35.))*Lepton_pt[0]',
    'range':(200,0,200),
    'xaxis':'P_{T}(TagLepton) [GeV]',
    'fold':3

}

variables['ProbeLepton_eta']={
    'name' : '(eleTrigMatch0 && (Lepton_isTightElectron_'+eleTagWP+'[0]>0.5) && (Lepton_pt[0]> 35.))*Lepton_eta[1] +\
    !(eleTrigMatch0 && (Lepton_isTightElectron_'+eleTagWP+'[0]>0.5) && (Lepton_pt[0]> 35.))*(eleTrigMatch1 && (Lepton_isTightElectron_'+eleWP+'[1]>0.5) && (Lepton_pt[1] > 35.))*Lepton_eta[0]',
    'range':(100,-2.5,2.5),
    'xaxis':'#eta(Lepton)',
    'fold':3

}


variables['mll']={
    'name' : 'mll',
    'range':(60,60,120),
    'xaxis':'mll',
    'fold':3

}


##-nPV
variables ['PV_npvs']={
    'name' : 'PV_npvs',
    'range' : (80,0,80),
    'xaxis' : 'PV_npvs',
    'fold':0
}


print "len(variables)=",len(variables)
for v in variables:
    print variables[v]['name'] 

