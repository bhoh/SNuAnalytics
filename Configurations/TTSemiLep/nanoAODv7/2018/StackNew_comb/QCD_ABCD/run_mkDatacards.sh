#InputFile='rootFile_2018_SKIM7_QCD_ABCD/hadd.root'
InputFile='hadd_rebinned.root'

python mkDatacards_CHToCB.py --pycfg=configuration.py --inputFile=$InputFile --outputDirDatacard=Datacards --structureFile=structure.py
