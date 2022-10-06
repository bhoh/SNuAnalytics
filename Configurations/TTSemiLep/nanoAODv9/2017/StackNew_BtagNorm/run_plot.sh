#InputFile='rootFile_2016_SKIM9/hadd.root'
#InputFile='rootFile_2016_SKIM9_final/PDF/results_unc.root'
#InputFile='QCD_ABCD/hadd_data_driven.root'
#InputFile='QCD_ABCD/rootFile_2016_SKIM9_QCD_ABCD_SF_final/hadd_data_driven.root'
#InputFile='QCD_ABCD/rootFile_2016_SKIM9_QCD_ABCD_SF/hadd_data_driven.root'
#InputFile='rootFile_2017_SKIM9_stat_only/hadd.root'
#InputFile='rootFile_2017_SKIM9_noBtagSF/hadd.root'
#mkPlot.py --pycfg=configuration_noBtagSF.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#sleep 30m;
InputFile='rootFile_2017_SKIM9_BtagSF/hadd.root'
mkPlot.py --pycfg=configuration_BtagSF.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_val.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#
#

#mkPlot.py --pycfg=configuration_Top_pTrw.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7 --fileFormats=png,pdf
#mkPlot.py --pycfg=configuration_Top_pTrw_M2T4.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7 --fileFormats=png,pdf
#
#
#mkPlot.py --pycfg=configuration_norm_High.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7 --plotNormalizedDistributions
#mkPlot.py --pycfg=configuration_norm_Low.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7 --plotNormalizedDistributions

