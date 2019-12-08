
#for histo factory
mkShapesMulti.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#mkShapesMulti.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --doHadd=True --treeName Events


#test
#mkShapesMulti.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --treeName Events

#mkShapes.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --treeName Events



#for hadd

#mkShapes.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --doHadd=True --treeName Events
#mkShapes.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --doHadd=True --batchSplit=AsMuchAsPossible --treeName Events
#mkShapes.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --doHadd=True --treeName Events


#Jet only

#mkShapes.py --pycfg=configuration_jetonly.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#mkShapes.py --pycfg=configuration_jetonly.py --batchSplit=AsMuchAsPossible --doHadd=True --treeName Events


#no 170to300

#mkShapes.py --pycfg=configuration_no170to300.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#mkShapes.py --pycfg=configuration_no170to300.py --batchSplit=AsMuchAsPossible --doHadd=True --treeName Events
