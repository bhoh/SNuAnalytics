##Just set below things##


tag='2018_SKIM5'

variablesFile='variables_comb.py' ##what variables to draw
cutsFile='cuts.py' ## event selection##region selection
plotFile='plot_comb.py' ##color code and some format-related things

samplesFile = 'samples_2018.py'

lumi=41.5

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
