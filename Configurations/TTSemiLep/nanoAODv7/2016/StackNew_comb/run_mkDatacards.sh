#InputFile='rootFile_2016_SKIM7/hadd.root'
InputFile='rootFile_2016_SKIM7_final/PDF/results_unc.root'
#InputFile='QCD_ABCD/hadd_data_driven.root'
#InputFile_ele='rootFile_2016_SKIM7_ele/PDF/results_suppressZeros.root'
#InputFile_ele='rootFile_2016_SKIM7_ele/PDF/results_suppressZeros.root'
#InputFile_mu='rootFile_2016_SKIM7_mu/PDF/results_suppressZeros.root'

python mkDatacards_CHToCB.py --pycfg=configuration_comb.py --inputFile=$InputFile --outputDirDatacard=Datacards --structureFile=structure.py
