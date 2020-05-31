##Just set below things##


tag='2016_SKIM7_gen_pull_bkg'

variablesFile='variables_pull.py' ##what variables to draw
cutsFile='cuts.py' ## event selection##region selection
plotFile='plot_gen_pull_bkg.py' ##color code and some format-related things

samplesFile = 'samples_2016_GenKinFitter.py'

lumi=35.9

#outputDirPlots='plots_'+tag+'Blined'
outputDirPlots='plots_'+tag
outputDir =           'rootFile_'+tag
treeName='Events'
aliasesFile='aliases.py'
nuisancesFile = 'nuisances_NULL.py'

#structureFile = 'structure.py'


#outputDirDatacard='DataCards'

maxLogCratio=10000