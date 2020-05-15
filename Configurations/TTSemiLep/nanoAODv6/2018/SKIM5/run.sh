#mkShapesMulti.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#
#mkShapesMulti.py --pycfg=configuration_gen.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#
#mkShapesMulti.py --pycfg=configuration_test.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#
#
#mkPlot.py --pycfg=configuration_withSig.py --inputFile=rootFile_2018_SKIM5/hadd.root --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration.py --inputFile=rootFile_2018_SKIM5/hadd.root --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_bkg_plus_sig_M090.py --inputFile=rootFile_2018_SKIM5/hadd.root --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_bkg_plus_sig_M120.py --inputFile=rootFile_2018_SKIM5/hadd.root --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_bkg_plus_sig_M150.py --inputFile=rootFile_2018_SKIM5/hadd.root --onlyPlot=cratio --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_pull_bkg.py --inputFile=rootFile_2018_SKIM5/hadd.root --onlyPlot=c --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_pull_sig.py --inputFile=rootFile_2018_SKIM5/hadd.root --onlyPlot=c --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_gen_pull_bkg.py --inputFile=rootFile_2018_SKIM5_gen/hadd.root --onlyPlot=c --scaleToPlot=1.7
#mkPlot.py --pycfg=configuration_gen_pull_sig.py --inputFile=rootFile_2018_SKIM5_gen/hadd.root --onlyPlot=c --scaleToPlot=1.7

python mkPDFShape.py --pycfg=configuration.py --inputFile=rootFile_2018_SKIM5/hadd.root --outputDirPDF rootFile_2018_SKIM5/PDF/
