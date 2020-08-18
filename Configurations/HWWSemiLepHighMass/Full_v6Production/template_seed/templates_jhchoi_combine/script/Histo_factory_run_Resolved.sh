mkdir -p logs/
StartTime=$(date +%s)


#Resolved
mkShapesMulti.py --pycfg=configuration_Resolved_SB.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
mkShapesMulti.py --pycfg=configuration_Resolved_TOP.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
mkShapesMulti.py --pycfg=configuration_Resolved_SR.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#Boosted
