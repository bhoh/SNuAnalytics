
#InputFile='rootFile_2017_SKIM7/hadd.root'
#InputFile='rootFile_2017_SKIM7/PDF/results_unc.root'
InputFile='rootFile_2017_SKIM7_final/PDF/results_unc.root'
#InputFile='QCD_ABCD/hadd_data_driven.root'


mkPlot.py --pycfg=configuration_final.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7

#mkPlot.py --pycfg=configuration_norm_High.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7 --plotNormalizedDistributions
#mkPlot.py --pycfg=configuration_norm_Low.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7 --plotNormalizedDistributions
