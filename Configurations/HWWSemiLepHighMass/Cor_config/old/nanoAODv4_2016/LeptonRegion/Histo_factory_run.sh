
#for histo factory
#mkShapes.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events



#for hadd
mkShapes.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --doHadd=True --batchSplit=AsMuchAsPossible --treeName Events
#mkShapes.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --doHadd=True --treeName Events
