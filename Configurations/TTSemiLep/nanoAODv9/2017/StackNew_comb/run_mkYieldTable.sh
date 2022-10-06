#InputFile='rootFile_2017_SKIM5/hadd.root'
#InputFile='rootFile_2017_SKIM5/PDF/results_suppressZeros.root'
#InputFile='rootFile_2017_SKIM9_final/PDF/results_unc.root'
InputFile='QCD_ABCD/hadd_data_driven.root'
#InputFile='rootFile_2017_SKIM9_comb/PDF/results_unc.root'
#InputFile_ele='rootFile_2017_SKIM5_ele/PDF/results_suppressZeros.root'
#InputFile_mu='rootFile_2017_SKIM5_mu/PDF/results_suppressZeros.root'

python mkYieldTable_CHToCB.py --pycfg=configuration_comb.py --inputFile=$InputFile --outputDirYieldTable=YieldTable --structureFile=structure.py
