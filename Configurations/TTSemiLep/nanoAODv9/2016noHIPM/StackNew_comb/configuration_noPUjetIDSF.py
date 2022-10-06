##Just set below things##


tag='2016noHIPM_SKIM9_noPUjetIDSF'

variablesFile='variables_test.py' ##what variables to draw
cutsFile='cuts.py' ## event selection##region selection
plotFile='plot_test.py' ##color code and some format-related things

samplesFile = 'samples.py'

lumi=16.81 # 0.418771191 + 7.653261227 +7.866107374 +0.8740119304

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
