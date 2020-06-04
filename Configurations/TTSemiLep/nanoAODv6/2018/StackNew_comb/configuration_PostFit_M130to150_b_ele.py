##Just set below things##


tag='2018_SKIM5_PostFit_M130to150_b_ele'

variablesFile='variables_ele.py' ##what variables to draw
cutsFile='cuts_ele.py' ## event selection##region selection
plotFile='plot_noSig_ele.py' ##color code and some format-related things

samplesFile = 'samples_2018_ele.py'

lumi=58.826

#outputDirPlots='plots_'+tag+'Blined'
outputDirPlots='plots_'+tag
outputDir ='rootFile_'+tag
treeName='Events'
aliasesFile='aliases.py'
nuisancesFile = 'nuisances_stat_only.py'
#nuisancesFile = 'nuisances_weight_based.py'
#nuisancesFile = 'nuisances_all_ele.py'

#structureFile = 'structure.py'


#outputDirDatacard='DataCards'

maxLogCratio=10000
