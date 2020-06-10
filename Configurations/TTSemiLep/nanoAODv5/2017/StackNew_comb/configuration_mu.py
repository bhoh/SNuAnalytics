##Just set below things##


tag='2017_SKIM7_mu'

variablesFile='variables_mu.py' ##what variables to draw
cutsFile='cuts_mu.py' ## event selection##region selection
plotFile='plot_noSig_mu.py' ##color code and some format-related things

samplesFile = 'samples_2017_mu.py'

lumi=41.5

#outputDirPlots='plots_'+tag+'Blined'
outputDirPlots='plots_'+tag
outputDir =           'rootFile_'+tag
treeName='Events'
aliasesFile='aliases.py'
#nuisancesFile = 'nuisances_stat_only.py'
#nuisancesFile = 'nuisances_weight_based.py'
nuisancesFile = 'nuisances_all_mu.py'

structureFile = 'structure.py'


#outputDirDatacard='DataCards'

maxLogCratio=10000
