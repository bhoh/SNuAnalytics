##Just set below things##


tag='2017_SKIM9_val'

variablesFile='variables.py' ##what variables to draw
cutsFile='cuts.py' ## event selection##region selection
plotFile='plot.py' ##color code and some format-related things

samplesFile = 'samples.py'

lumi=41.48

#outputDirPlots='plots_'+tag+'Blined'
outputDirPlots='plots_'+tag
outputDir =           'rootFile_'+tag
treeName='Events'
aliasesFile='aliases.py'
#nuisancesFile = 'nuisances_stat_only.py'
#nuisancesFile = 'nuisances_weight_based.py'
nuisancesFile = 'nuisances_all.py'

structureFile = 'structure.py'


#outputDirDatacard='DataCards'

maxLogCratio=10000
