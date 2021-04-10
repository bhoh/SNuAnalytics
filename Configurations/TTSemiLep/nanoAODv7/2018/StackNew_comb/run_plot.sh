#InputFile='rootFile_2018_SKIM7/hadd.root'
#InputFile='rootFile_2018_SKIM7/PDF/results_unc.root'
InputFile='rootFile_2018_SKIM7_final/PDF/results_unc.root'
#InputFile='rootFile_2018_SKIM7_mva/PDF/results_unc.root'
#InputFile='QCD_ABCD/hadd_data_driven.root'
#InputFile='rootFile_2018_SKIM7_mva/hadd.root'
#InputFile_ele='rootFile_2018_SKIM5_ele/PDF/results_unc.root'
#InputFile_mu='rootFile_2018_SKIM5_mu/PDF/results_unc.root'

mkPlot.py --pycfg=configuration_final.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_norm_High.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7 --plotNormalizedDistributions
#mkPlot.py --pycfg=configuration_norm_Low.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7 --plotNormalizedDistributions
