#FilesPerJob=30
#FilesPerJobMainBKG=2
#FilesPerJobDATA=100


import os
import math
import sys
sys.path.append(os.getcwd())

#-----Variable Deinition-----#
from WPandCut2018 import *
#from GetXsecInNtuple import GetXsecInNtuple
#------End of Variable Definition-----#


import glob
import copy
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *



samples={}

SITE=os.uname()[1]
mcCommonWeight='XSWeight*SFweight*METFilter_MC'
directory=treeBaseDir+CAMPAIGN+'/'+STEP


samples['DY'] = {    'name'   :   getSampleFiles(directory,'DYJetsToLL_M-50-LO',False,'nanoLatino_')
                     + getSampleFiles(directory,'DYJetsToLL_M-10to50-LO',False,'nanoLatino_'),
                     'weight' : mcCommonWeight,
                     'FilesPerJob' : FilesPerJobMainBKG,
                          'suppressNegative' :['all'],
                          'suppressNegativeNuisances' :['all'],

}

samples['Wjets0j'] = {    'name'   :
                          getSampleFiles(directory,'WJetsToLNu-0J',False,'nanoLatino_'),
                          'weight' : mcCommonWeight,
                          'FilesPerJob' : FilesPerJobMainBKG,
                          'suppressNegative' :['all'],
                          'suppressNegativeNuisances' :['all'],

}
samples['Wjets1j'] = {    'name'   :
                          getSampleFiles(directory,'WJetsToLNu-1J',False,'nanoLatino_'),
                          'weight' : mcCommonWeight,
                          'FilesPerJob' : FilesPerJobMainBKG,
                          'suppressNegative' :['all'],
                          'suppressNegativeNuisances' :['all'],

}
samples['Wjets2j'] = {    'name'   :
                          getSampleFiles(directory,'WJetsToLNu-2J',False,'nanoLatino_'),
                          'weight' : mcCommonWeight,
                          'FilesPerJob' : FilesPerJobMainBKG,
                          'suppressNegative' :['all'],
                          'suppressNegativeNuisances' :['all'],

}
