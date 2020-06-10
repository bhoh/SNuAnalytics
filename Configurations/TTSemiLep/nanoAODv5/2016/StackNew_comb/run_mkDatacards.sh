#InputFile='rootFile_2016_SKIM7/hadd.root'
InputFile='rootFile_2016_SKIM7/PDF/results_unc.root'
#InputFile_ele='rootFile_2016_SKIM7_ele/PDF/results_suppressZeros.root'
#InputFile_mu='rootFile_2016_SKIM7_mu/PDF/results_suppressZeros.root'

#mkDatacards.py --pycfg=configuration.py --inputFile=$InputFile --outputDirDatacard=Datacards --structureFile=structure.py
python mkDatacards_CHToCB.py --pycfg=configuration_comb_ele.py --inputFile=$InputFile --outputDirDatacard=Datacards --structureFile=structure.py
python mkDatacards_CHToCB.py --pycfg=configuration_comb_mu.py --inputFile=$InputFile --outputDirDatacard=Datacards --structureFile=structure.py
