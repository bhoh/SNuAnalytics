##Just set below things##


tag='2016_SKIM9_Top_pTrw_M2T4'

variablesFile='variables_Top_pTrw.py' ##what variables to draw
cutsFile='cuts.py' ## event selection##region selection
plotFile='plot_Top_pTrw_M2T4.py' ##color code and some format-related things

samplesFile = 'samples_Top_pTrw_M2T4.py'

lumi=35.92

#outputDirPlots='plots_'+tag+'Blined'
outputDirPlots='plots_'+tag
outputDir =           'rootFile_'+tag
treeName='Events'
aliasesFile='aliases.py'
nuisancesFile = 'nuisances_stat_only.py'
#nuisancesFile = 'nuisances_weight_based.py'
#nuisancesFile = 'nuisances_all.py'

#structureFile = 'structure.py'


#outputDirDatacard='DataCards'

maxLogCratio=10000
