##Just set below things##


tag='2016_SKIM7_bkg_plus_sig_M090'

variablesFile='variables.py' ##what variables to draw
cutsFile='cuts.py' ## event selection##region selection
plotFile='plot_bkg_plus_sig_M090.py' ##color code and some format-related things

samplesFile = 'samples_2016_ttbarCat.py'

lumi=35.9

#outputDirPlots='plots_'+tag+'Blined'
outputDirPlots='plots_'+tag
outputDir =           'rootFile_'+tag
treeName='Events'
aliasesFile='aliases.py'
nuisancesFile = 'nuisances_stat_only.py'

#structureFile = 'structure.py'


#outputDirDatacard='DataCards'

maxLogCratio=10000
