##Just set below things##

#tag='FatJetPreselCleaningWlep_semilep'
tag='simple2017'
#tag='Boosted2017'
#tag='semilep_tight80XWP'


variablesFile='variables.py' ##what variables to draw
cutsFile='cuts.py' ## event selection##region selection
plotFile='plot.py' ##color code and some format-related things
samplesFile = 'samples_'+tag+'.py'

lumi=41.5

#outputDirPlots='plots_'+tag+'Blined'
outputDirPlots='plots_'+tag
outputDir =           'rootFile_'+tag
treeName='Events'
aliasesFile='aliases.py'
#nuisancesFile = 'nuisances.py'


