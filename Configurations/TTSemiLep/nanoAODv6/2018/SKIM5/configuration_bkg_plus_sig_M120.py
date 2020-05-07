##Just set below things##


tag='2018_SKIM5_bkg_plus_sig_M120'

variablesFile='variables.py' ##what variables to draw
cutsFile='cuts.py' ## event selection##region selection
plotFile='plot_bkg_plus_sig_M120.py' ##color code and some format-related things

samplesFile = 'samples_2018_ttbarCat.py'

lumi=58.826

#outputDirPlots='plots_'+tag+'Blined'
outputDirPlots='plots_'+tag
outputDir =           'rootFile_'+tag
treeName='Events'
aliasesFile='aliases.py'
nuisancesFile = 'nuisances_stat_only.py'

#structureFile = 'structure.py'


#outputDirDatacard='DataCards'

maxLogCratio=10000
