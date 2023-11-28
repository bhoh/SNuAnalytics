##Just set below things##


tag='2017_SKIM9_postfit_b'

variablesFile='variables_comb.py' ##what variables to draw
cutsFile='cuts_comb.py' ## event selection##region selection
plotFile='plot_postfit_b.py' ##color code and some format-related things

samplesFile = 'samples_PostFitPlot.py'

lumi=41.48

#outputDirPlots='plots_'+tag+'Blined'
outputDirPlots='plots_'+tag
outputDir =           'rootFile_'+tag
treeName='Events'
aliasesFile='aliases.py'
nuisancesFile = 'nuisances_stat_only.py'
#nuisancesFile = 'nuisances_weight_based.py'
#nuisancesFile = 'nuisances_all.py'

structureFile = 'structure_PostFitPlot.py'


#outputDirDatacard='DataCards'

maxLogCratio=10000
