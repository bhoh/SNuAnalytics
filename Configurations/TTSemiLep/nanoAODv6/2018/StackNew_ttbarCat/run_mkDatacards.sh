#InputFile='rootFile_2018_SKIM5/hadd.root'
InputFile='rootFile_2018_SKIM5/PDF/results_unc.root'
InputFile_ele='rootFile_2018_SKIM5_ele/PDF/results_unc.root'
InputFile_mu='rootFile_2018_SKIM5_mu/PDF/results_unc.root'

mkDatacards.py --pycfg=configuration.py --inputFile=$InputFile --outputDirDatacard=Datacards --structureFile=structure.py
