##Just set below things##


tag='2016HIPM_SKIM9_TopPtReweight'

variablesFile='variables_test.py' ##what variables to draw
cutsFile='cuts.py' ## event selection##region selection
plotFile='plot_test.py' ##color code and some format-related things

samplesFile = 'samples.py'

lumi=19.52 # 16.802739097 + 1.063261220 + 1.655228036 = 19.521228353

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
