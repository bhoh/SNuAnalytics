##Just set below things##


tag='2018_SKIM5_PostFit_M130to150_b'

variablesFile='variables.py' ##what variables to draw
cutsFile='cuts.py' ## event selection##region selection
plotFile='plot_noSig.py' ##color code and some format-related things

samplesFile = 'samples.py'

lumi=59.83

#outputDirPlots='plots_'+tag+'Blined'
outputDirPlots='plots_'+tag
outputDir ='rootFile_'+tag
treeName='Events'
aliasesFile='aliases.py'
nuisancesFile = 'nuisances_stat_only.py'
#nuisancesFile = 'nuisances_weight_based.py'
#nuisancesFile = 'nuisances_all.py'

#structureFile = 'structure.py'


#outputDirDatacard='DataCards'

maxLogCratio=10000
