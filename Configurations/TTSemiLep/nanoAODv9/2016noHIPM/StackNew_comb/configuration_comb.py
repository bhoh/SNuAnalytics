##Just set below things##


tag='2016_SKIM9_comb'

variablesFile='variables_comb.py' ##what variables to draw
cutsFile='cuts_comb.py' ## event selection##region selection
plotFile='plot_comb.py' ##color code and some format-related things

samplesFile = 'samples.py'

lumi=16.81

#outputDirPlots='plots_'+tag+'Blined'
outputDirPlots='plots_'+tag
outputDir =           'rootFile_'+tag
treeName='Events'
aliasesFile='aliases.py'
#nuisancesFile = 'nuisances_stat_only.py'
#nuisancesFile = 'nuisances_weight_based.py'
nuisancesFile = 'nuisances_all.py'

#structureFile = 'structure.py'


#outputDirDatacard='DataCards'

maxLogCratio=10000