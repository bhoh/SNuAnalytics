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

##--sig

import sys

samples['DY'] = {    'name'   :   getSampleFiles(directory,'DYJetsToLL_M-50-LO_ext2',False,'nanoLatino_')
                     + getSampleFiles(directory,'DYJetsToLL_M-10to50-LO',False,'nanoLatino_'),
                     'weight' : mcCommonWeight,
                     'FilesPerJob' : FilesPerJobMainBKG,
                     'suppressNegative' :['all'],
                     'suppressNegativeNuisances' :['all'],

}
