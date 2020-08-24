
import os

import sys
sys.path.append(os.getcwd())


#-----Variable Deinition-----#                                                                                                                 
from WPandCut2017 import *

##Just set below things##


#tag='simple2017'
tag='2017_Resolved_SKIM10_HMFull_V11_nom_'+model+'_'+WTAG+'_'+ALGO+'_dphicut'


variablesFile='variables_Resolved.py' ##what variables to draw
cutsFile='cuts_Resolved.py' ## event selection##region selection


samplesFile = 'samples_2017.py'

lumi=41.5

#outputDirPlots='plots_'+tag+'Blined'
outputDirPlots='plots_'+tag
outputDir =           'rootFile_'+tag
treeName='Events'
aliasesFile='aliases.py'
#nuisancesFile = 'nuisances_Resolved.py'
nuisancesFile = 'nuisances_dummy.py'

#structureFile = 'structure.py'


#outputDirDatacard='DataCards'

maxLogCratio=10000
