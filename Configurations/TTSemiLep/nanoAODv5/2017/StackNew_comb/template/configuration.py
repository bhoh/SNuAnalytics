##Just set below things##


tag='2017_SKIM7<CH>'

variablesFile='variables<CH>.py' ##what variables to draw
cutsFile='cuts<CH>.py' ## event selection##region selection
plotFile='plot_noSig<CH>.py' ##color code and some format-related things

samplesFile = 'samples_2017<CH>.py'

lumi=41.5

#outputDirPlots='plots_'+tag+'Blined'
outputDirPlots='plots_'+tag
outputDir =           'rootFile_'+tag
treeName='Events'
aliasesFile='aliases.py'
#nuisancesFile = 'nuisances_stat_only.py'
#nuisancesFile = 'nuisances_weight_based.py'
nuisancesFile = 'nuisances_all<CH>.py'

structureFile = 'structure.py'


#outputDirDatacard='DataCards'

maxLogCratio=10000
