##Just set below things##


tag='2017_SKIM7_QCD_ABCD'

variablesFile='variables.py' ##what variables to draw
cutsFile='cuts.py' ## event selection##region selection
plotFile='plot.py' ##color code and some format-related things

samplesFile = 'samples_2017.py'

lumi=41.53

#outputDirPlots='plots_'+tag+'Blined'
outputDirPlots='plots_'+tag
outputDir =           'rootFile_'+tag
treeName='Events'
aliasesFile='aliases.py'
#nuisancesFile = 'nuisances_stat_only.py'
#nuisancesFile = 'nuisances_weight_based.py'
nuisancesFile = 'nuisances_abcd.py'

structureFile = 'structure.py'


#outputDirDatacard='DataCards'

maxLogCratio=10000
