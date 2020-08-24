FilesPerJob=2

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

directory=treeBaseDir+CAMPAIGN+'/'+STEP



################################################                                                                                             
############ DATA DECLARATION ##################                                                                                             
################################################ 
samples['Wjets0j'] = {    'name'   :
                          getSampleFiles(directory,'WJetsToLNu-0J',False,'nanoLatino_'),
                          'weight' : '1',
                          'FilesPerJob' : FilesPerJob,

}
samples['Wjets1j'] = {    'name'   :
                          getSampleFiles(directory,'WJetsToLNu-1J',False,'nanoLatino_'),
                          'weight' : '1',
                          'FilesPerJob' : FilesPerJob,
}
samples['Wjets2j'] = {    'name'   :
                          getSampleFiles(directory,'WJetsToLNu-2J',False,'nanoLatino_'),
                          'weight' : '1',
                          'FilesPerJob' : FilesPerJob,
}




