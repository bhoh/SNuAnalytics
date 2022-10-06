#InputFile='rootFile_2018_SKIM5/hadd.root'
#InputFile='rootFile_2018_SKIM5/PDF/results_suppressZeros.root'
#InputFile='rootFile_2018_SKIM7_final/PDF/results_unc.root'
InputFile='rootFile_2018_SKIM9_stat_only/hadd.root'
#InputFile='rootFile_2018_SKIM7_comb/PDF/results_unc.root'
#InputFile_ele='rootFile_2018_SKIM5_ele/PDF/results_suppressZeros.root'
#InputFile_mu='rootFile_2018_SKIM5_mu/PDF/results_suppressZeros.root'

python mkYieldTable_CHToCB.py --pycfg=configuration_stat_only.py --inputFile=$InputFile --outputDirYieldTable=YieldTable --structureFile=structure.py
