#FilesPerJob=30
#FilesPerJobMainBKG=2
#FilesPerJobDATA=100

TESTRUN=False

import math
import os
import sys
sys.path.append(os.getcwd())

#-----Variable Deinition-----#
from WPandCut2016 import *

#------End of Variable Definition-----#



import glob
import copy
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *



samples={}





METFilter_MC   = 'METFilter_MC'

METFilter_DATA = 'METFilter_DATA'

mcCommonWeight='XSWeight*SFweight*METFilter_MC'

METFilter_DATA = 'METFilter_DATA'


samples['DY'] = {    'name'   :   getSampleFiles(directory,'DYJetsToLL_M-50-LO_ext2',False,'nanoLatino_')
                     + getSampleFiles(directory,'DYJetsToLL_M-10to50-LO',False,'nanoLatino_'),
                     'weight' : mcCommonWeight,
                     'FilesPerJob' : FilesPerJobMainBKG,
                     'suppressNegative' :['all'],
                     'suppressNegativeNuisances' :['all'],

}


################################################
############ DATA DECLARATION ##################
################################################
DataRun = [
    ['B','Run2016B-Nano1June2019_ver2-v1'],
    ['C','Run2016C-Nano1June2019-v1'],
    ['D','Run2016D-Nano1June2019-v1'],
    ['E','Run2016E-Nano1June2019-v1'],
    ['F','Run2016F-Nano1June2019-v1'],
    ['G','Run2016G-Nano1June2019-v1'],
    ['H','Run2016H-Nano1June2019-v1'],
]


DataSets = ['SingleElectron'
]

DataTrig = {
            'SingleElectron' : 'Trigger_sngEl' ,
           }



for Run in DataRun :

    samples['DATA'+Run[1]]  = {   'name': [ ] ,
                       'weight' : 'METFilter_DATA*LepWPCut' ,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : FilesPerJobDATA,
                     }

    directoryDATA = treeBaseDir+CAMPAIGN_DATA+'/'+STEP_DATA
    for DataSet in DataSets :
        FileTarget = getSampleFiles(directoryDATA,DataSet+'_'+Run[1],True,'nanoLatino_')
        for iFile in FileTarget:

            samples['DATA'+Run[1]]['name'].append(iFile)
            samples['DATA'+Run[1]]['weights'].append(DataTrig[DataSet])
