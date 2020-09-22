#FilesPerJob=30
#FilesPerJobMainBKG=2
#FilesPerJobDATA=100


import math
import os

import sys
sys.path.append(os.getcwd())


#-----Variable Deinition-----#
from WPandCut2017 import *
#from GetXsecInNtuple import GetXsecInNtuple
#------End of Variable Definition-----#

import glob
import copy
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *



samples={}



directory=treeBaseDir+CAMPAIGN+'/'+STEP
mcCommonWeight='XSWeight*SFweight*METFilter_MC'

samples['DY'] = {    'name'   :   getSampleFiles(directory,'DYJetsToLL_M-50',False,'nanoLatino_')
                     + getSampleFiles(directory,'DYJetsToLL_M-10to50-LO',False,'nanoLatino_'),
                     'weight' : mcCommonWeight,
                     #'FilesPerJob' : 10,
                     'FilesPerJob' : FilesPerJobMainBKG,
}


samples['Wjets0j'] = {    'name'   :
                          getSampleFiles(directory,'WJetsToLNu-0J',False,'nanoLatino_')
                          ,
                          'weight' : mcCommonWeight,
                          #'FilesPerJob' : 4,
                          'FilesPerJob' : FilesPerJobMainBKG,
                          'suppressNegative' :['all'],
                          'suppressNegativeNuisances' :['all'],

                        }
samples['Wjets1j'] = {    'name'   :
                          getSampleFiles(directory,'WJetsToLNu-1J',False,'nanoLatino_')
                          ,
                          'weight' : mcCommonWeight,
                        #'FilesPerJob' : 4,
                          'FilesPerJob' : FilesPerJobMainBKG,
                          'suppressNegative' :['all'],
                          'suppressNegativeNuisances' :['all'],

                        }
samples['Wjets2j'] = {    'name'   :
                          getSampleFiles(directory,'WJetsToLNu-2J',False,'nanoLatino_')
                          ,
                          'weight' : mcCommonWeight,
                          #'FilesPerJob' : 4,
                          'FilesPerJob' : FilesPerJobMainBKG,

                          'suppressNegative' :['all'],
                          'suppressNegativeNuisances' :['all'],
                        }
