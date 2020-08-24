
import os

import sys
sys.path.append(os.getcwd())


#-----Variable Deinition-----#                                                                                                                 
from WPandCut2017 import *

##Just set below things##

tag=Year+'_Boosted_SKIM10_HMFull_V11_nom_'+model+'_'+WTAG+'_'+ALGO


variablesFile='variables_Boosted.py' ##what variables to draw
cutsFile='cuts_Boosted.py' ## event selection##region selection


samplesFile = 'samples_'+Year+'.py'

lumi=1.
if Year=='2016':
    lumi=35.9
if Year=='2017':
    lumi=41.5
if Year=='2018':
    lumi=59.7

#outputDirPlots='plots_'+tag+'Blined'
outputDirPlots='plots_'+tag
outputDir =           'rootFile_'+tag
treeName='Events'
aliasesFile='aliases.py'
nuisancesFile = 'nuisances_Boosted.py'
#nuisancesFile = 'nuisances_dummy.py'

#structureFile = 'structure.py'


#outputDirDatacard='DataCards'

maxLogCratio=100000
maxLogC=100000
