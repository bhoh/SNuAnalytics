##############
# -n dry-run
#
#
#for histo factory
#mkShapes.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#mkShapes.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --treeName Events


mkShapesMulti.py --pycfg=configuration_Int.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events  -n
############
#for hadd ##
############
#mkShapesMulti.py --pycfg=configuration_Int.py --batchSplit=AsMuchAsPossible --doHadd=True --treeName Events
