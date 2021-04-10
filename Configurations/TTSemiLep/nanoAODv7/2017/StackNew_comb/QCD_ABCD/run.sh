#mkShapesMulti.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#mkShapesMulti.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events --dry-run
mkShapesMulti.py --pycfg=configuration_SF.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events --outputDir=../../../../../../../../../../../../../cms_scratch/bhoh/rootFile_2017_SKIM7_QCD_ABCD_SF
#mkShapesMulti.py --pycfg=configuration_SF.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events --dry-run
#
#
#
#
#
InputFile='rootFile_2018_SKIM7_QCD_ABCD/hadd.root'
#InputFile='rootFile_2018_SKIM7/PDF/results_unc.root'
#InputFile='rootFile_2018_SKIM7_mva/PDF/results_unc.root'
#InputFile='rootFile_2018_SKIM7_comb/PDF/results_unc.root'
#InputFile='rootFile_2018_SKIM7_mva/hadd.root'
#InputFile_ele='rootFile_2018_SKIM5_ele/PDF/results_unc.root'
#InputFile_mu='rootFile_2018_SKIM5_mu/PDF/results_unc.root'
#mkPlot.py --pycfg=configuration_test.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_mva.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_comb.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_stat_only.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_withSig.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_withSig_ele.py --inputFile=$InputFile_ele --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_withSig_mu.py --inputFile=$InputFile_mu --onlyPlot=cratio --scaleToPlot=1.7
#
#
#
#mkPlot.py --pycfg=configuration_withSig_mu.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7 --fileFormats=png,pdf
#mkPlot.py --pycfg=configuration_withSig_ele.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7 --fileFormats=png,pdf
#mkPlot.py --pycfg=configuration_withSig.py --inputFile=$InputFile --onlyPlot=cratio --scaleToPlot=1.7 --fileFormats=png,pdf
#mkPlot.py --pycfg=configuration.py --inputFile=rootFile_2018_SKIM5/hadd.root --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_bkg_plus_sig_M090.py --inputFile=rootFile_2018_SKIM5/hadd.root --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_bkg_plus_sig_M120.py --inputFile=rootFile_2018_SKIM5/hadd.root --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_bkg_plus_sig_M150.py --inputFile=rootFile_2018_SKIM5/hadd.root --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_pull_bkg.py --inputFile=rootFile_2018_SKIM5/hadd.root --onlyPlot=c --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_pull_sig.py --inputFile=rootFile_2018_SKIM5/hadd.root --onlyPlot=c --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_gen_pull_bkg.py --inputFile=rootFile_2018_SKIM5_gen/hadd.root --onlyPlot=c --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_gen_pull_sig.py --inputFile=rootFile_2018_SKIM5_gen/hadd.root --onlyPlot=c --scaleToPlot=1.7
#
#
#
#
#
#python mkPDFShape.py --pycfg=configuration.py --inputFile=rootFile_2018_SKIM5/hadd.root --outputDirPDF rootFile_2018_SKIM5/PDF/
#python mkPDFShape.py --pycfg=configuration_ele.py --inputFile=rootFile_2018_SKIM5_ele/hadd.root --outputDirPDF rootFile_2018_SKIM5_ele/PDF/
#python mkPDFShape.py --pycfg=configuration_mu.py --inputFile=rootFile_2018_SKIM5_mu/hadd.root --outputDirPDF rootFile_2018_SKIM5_mu/PDF/
#
#
#
#python mkSuppressZeros.py --pycfg=configuration.py --inputFile=rootFile_2018_SKIM5/PDF/results_unc.root --outputDirShape=rootFile_2018_SKIM5/PDF/
#
