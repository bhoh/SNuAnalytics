##Just set below things##


tag='2016_SKIM7_QCD_ABCD_SF'

#variablesFile='variables_SF.py' ##what variables to draw
variablesFile='variables_SF.py' ##what variables to draw
cutsFile='cuts_SF.py' ## event selection##region selection
plotFile='plot_new.py' ##color code and some format-related things

samplesFile = 'samples_2016_SF.py'

lumi=36.33

#outputDirPlots='plots_'+tag+'Blined'
outputDirPlots='plots_'+tag
outputDir =           'rootFile_'+tag
treeName='Events'
aliasesFile='aliases_SF.py'
#nuisancesFile = 'nuisances_stat_only.py'
#nuisancesFile = 'nuisances_weight_based.py'
nuisancesFile = 'nuisances_abcd_SF.py'

#structureFile = 'structure.py'


#outputDirDatacard='DataCards'

maxLogCratio=10000
