#InputFile='rootFile_2018_SKIM7/hadd.root'
#InputFile='rootFile_2018_SKIM7/PDF/results_unc.root'
#InputFile='rootFile_2018_SKIM7_final/PDF/results_unc.root'
#InputFile='rootFile_2018_SKIM7_val/PDF/results_unc.root'
#InputFile='rootFile_2018_SKIM7_mva/PDF/results_unc.root'
#InputFile='QCD_ABCD/hadd_data_driven.root'
InputFile='QCD_ABCD/rootFile_2018_SKIM7_QCD_ABCD_SF_final/hadd_data_driven.root'
#InputFile='QCD_ABCD/rootFile_2018_SKIM7_QCD_ABCD_SF/hadd_data_driven.root'
mkPlot.py --pycfg=configuration_final.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_val.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_norm_High.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7 --plotNormalizedDistributions
#mkPlot.py --pycfg=configuration_norm_Low.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7 --plotNormalizedDistributions
