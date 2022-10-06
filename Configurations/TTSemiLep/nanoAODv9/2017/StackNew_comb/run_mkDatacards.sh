#InputFile='rootFile_2017_SKIM9/hadd.root'
InputFile='rootFile_2017_SKIM9_final/PDF/results_unc.root'
#InputFile='QCD_ABCD/rootFile_2017_SKIM9_QCD_ABCD_SF_final/hadd_data_driven.root'
#InputFile_ele='rootFile_2017_SKIM9_ele/PDF/results_suppressZeros.root'
#InputFile_mu='rootFile_2017_SKIM9_mu/PDF/results_suppressZeros.root'

python mkDatacards_CHToCB.py --pycfg=configuration_comb.py --inputFile=$InputFile --outputDirDatacard=Datacards --structureFile=structure.py
