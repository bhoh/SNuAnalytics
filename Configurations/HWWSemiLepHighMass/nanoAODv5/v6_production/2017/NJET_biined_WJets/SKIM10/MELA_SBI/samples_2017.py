TESTRUN=False
import sys
sys.path.append(os.getcwd())

#-----Variable Deinition-----#
from WPandCut2017 import *
from GetXsecInNtuple import GetXsecInNtuple
#------End of Variable Definition-----#


import os
import glob
import copy
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *



#samples={}


xrootdPath = 'root://cms-xrdr.private.lo:2094'
treeBaseDir = "/xrootd/store/user/jhchoi/Latino/HWWNano/"


##--Set Campaign and Step--##
CAMPAIGN='Fall2017_102X_nAODv5_Full2017v6'
STEP="MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__BWReweight__HMFull_jhchoi10_nom__HMLHEAna"
CAMPAIGN_DATA='Run2017_102X_nAODv5_Full2017v6'
STEP_DATA="DATAl1loose2017v6__HMSemilepSKIMv6_10_data__HMFull_jhchoi10_data"


directory=treeBaseDir+CAMPAIGN+'/'+STEP

################################################                                                                                             
############ DATA DECLARATION ##################                                                                                             
################################################ 
DataRun = [
    ['B','Run2017B-Nano1June2019-v1'],
    ['C','Run2017C-Nano1June2019-v1'],
    ['D','Run2017D-Nano1June2019-v1'],
    ['E','Run2017E-Nano1June2019-v1'],
    ['F','Run2017F-Nano1June2019-v1']
]


DataSets = ['SingleMuon',\
'SingleElectron'
]

DataTrig = {
            'SingleMuon'     : 'Trigger_sngMu' ,
            'SingleElectron' : '!Trigger_sngMu && Trigger_sngEl' ,
           }


import sys
sys.path.insert(0, "MassPoints")
from List_MX import *
from List_MX_VBF import *

model="cprime1.0BRnew0.0"
from FilterMelaReweights import GetMinMaxCuts

for MX in List_MX:
  print MX
  MELA_cuts=GetMinMaxCuts(getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),model)
  cut=MELA_cuts['cut']
  print cut
  samples['ggHWWlnuqq_M'+str(MX)+'_S'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                                 'weight' : 'XSWeight*SFweight*METFilter_MC*'+model+'*'+cut,
                                                 'FilesPerJob' : 10,
                                               }
  samples['ggHWWlnuqq_M'+str(MX)+'_B'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                                 'weight' : 'XSWeight*SFweight*METFilter_MC*'+model+'_B'+'*'+cut,
                                                 'FilesPerJob' : 10,
                                               }
  samples['ggHWWlnuqq_M'+str(MX)+'_I'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                                 'weight' : 'XSWeight*SFweight*METFilter_MC*'+model+'_I'+'*'+cut,
                                                 'FilesPerJob' : 10,
                                               }
    
for MX in List_MX_VBF:

  samples['vbfHWWlnuqq_M'+str(MX)+'_S'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                                 'weight' : 'XSWeight*SFweight*METFilter_MC*'+model+'*'+cut,
                                                 'FilesPerJob' : 10,
                                               }

  samples['vbfHWWlnuqq_M'+str(MX)+'_B'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                                 'weight' : 'XSWeight*SFweight*METFilter_MC*'+model+'_B'+'*'+cut,
                                                 'FilesPerJob' : 10,
                                               }

  samples['vbfHWWlnuqq_M'+str(MX)+'_I'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                                 'weight' : 'XSWeight*SFweight*METFilter_MC*'+model+'_I'+'*'+cut,
                                                 'FilesPerJob' : 10,
                                               }



