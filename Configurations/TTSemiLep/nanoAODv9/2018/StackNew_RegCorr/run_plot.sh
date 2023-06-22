#InputFile='rootFile_2018_SKIM7/hadd.root'
#InputFile='rootFile_2018_SKIM7/PDF/results_unc.root'
#InputFile='rootFile_2018_SKIM7_val/PDF/results_unc.root'
#InputFile='rootFile_2018_SKIM7_mva/PDF/results_unc.root'
#InputFile='QCD_ABCD/hadd_data_driven.root'
#InputFile='QCD_ABCD/rootFile_2018_SKIM7_QCD_ABCD_SF_final/hadd_data_driven.root'
#InputFile='QCD_ABCD/rootFile_2018_SKIM7_QCD_ABCD_SF/hadd_data_driven.root'

#InputFile='rootFile_2018_SKIM9_charge/hadd.root'
#mkPlot.py --pycfg=configuration_charge.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#InputFile='rootFile_2018_SKIM9_val/PDF/results_unc.root'
#InputFile='rootFile_2018_SKIM9_val/hadd.root'
#mkPlot.py --pycfg=configuration_val.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_norm_High.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_norm_High.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7 --plotNormalizedDistributions
#mkPlot.py --pycfg=configuration_norm_Low.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7 --plotNormalizedDistributions
#mkPlot.py --pycfg=configuration_val.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_norm_High.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7 --plotNormalizedDistributions
InputFile='rootFile_2018_SKIM9_RegCorr/hadd.root'
#InputFile='rootFile_2018_SKIM9_final/hadd.root'
mkPlot.py --pycfg=configuration_RegCorr.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#InputFile='rootFile_2018_SKIM9_stat_only/hadd.root'
#InputFile='rootFile_2018_SKIM9_puWeight/hadd.root'
#mkPlot.py --pycfg=configuration_stat_only.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7

#mkPlot.py --pycfg=configuration_puWeight.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_val.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_norm_High.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7 --plotNormalizedDistributions
#mkPlot.py --pycfg=configuration_norm_Low.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7 --plotNormalizedDistributions

#InputFile='rootFile_2018_SKIM9_noBtagNormSF/hadd.root'
#mkPlot.py --pycfg=configuration_noBtagNormSF.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#InputFile='rootFile_2018_SKIM9_noPUweightSF/hadd.root'
#mkPlot.py --pycfg=configuration_noPUweightSF.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#InputFile='rootFile_2018_SKIM9_stat_only/hadd.root'
#mkPlot.py --pycfg=configuration_stat_only.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#InputFile='rootFile_2018_SKIM9_noTopPtReweight/hadd.root'
#mkPlot.py --pycfg=configuration_noTopPtReweight.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7

#InputFile='rootFile_2018_SKIM9_HEM/hadd.root'
#mkPlot.py --pycfg=configuration_HEM.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7 --onlyCut='sng_4j_eleORmuCH_2b'
