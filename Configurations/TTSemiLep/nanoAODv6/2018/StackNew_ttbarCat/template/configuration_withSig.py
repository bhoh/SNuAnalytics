##Just set below things##


tag='2018_SKIM5<CH>'

variablesFile='variables<CH>.py' ##what variables to draw
cutsFile='cuts<CH>.py' ## event selection##region selection
plotFile='plot<CH>.py' ##color code and some format-related things

samplesFile = 'samples_2018_ttbarCat<CH>.py'

lumi=58.826

#outputDirPlots='plots_'+tag+'Blined'
outputDirPlots='plots_'+tag
outputDir ='rootFile_'+tag
treeName='Events'
aliasesFile='aliases.py'
#nuisancesFile = 'nuisances_stat_only.py'
#nuisancesFile = 'nuisances_weight_based.py'
nuisancesFile = 'nuisances_all<CH>.py'

#structureFile = 'structure.py'


#outputDirDatacard='DataCards'

maxLogCratio=10000
