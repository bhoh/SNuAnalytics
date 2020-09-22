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
variables['Lepton_pt[0]']={
    'name' : 'Lepton_pt[0]',
    'range':(200,0,200),
    'xaxis':'P_{T}(Lepton) [GeV]',
    'fold':3

}
variables['Lepton_eta[0]']={
    'name' : 'Lepton_eta[0]',
    'range':(100,-2.5,2.5),
    'xaxis':'#eta(Lepton)',
    'fold':3
}

variables['Lepton_pt[1]']={
    'name' : 'Lepton_pt[1]',
    'range':(200,0,200),
    'xaxis':'P_{T}(subLepton) [GeV]',
    'fold':3

}
variables['Lepton_eta[1]']={
    'name' : 'Lepton_eta[1]',
    'range':(100,-2.5,2.5),
    'xaxis':'#eta(subLepton)',
    'fold':3
}

variables['eleTrigMatch0']={
    'name' : 'eleTrigMatch0',
    'range':(2,0,2),
    'xaxis':'eleTrigMatch0',
    'fold':3
}


variables['eleTrigMatch1']={
    'name' : 'eleTrigMatch1',
    'range':(2,0,2),
    'xaxis':'eleTrigMatch1',
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

