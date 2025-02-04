mkdir -p logs/
StartTime=$(date +%s)

python TurnOffCombinedSamples.py WPandCut2016.py CombineMultiV
python TurnOffCombinedSamples.py WPandCut2016.py CombineH125
python TurnOffCombinedSamples.py WPandCut2016.py CombineWjets
python TurnOffCombinedSamples.py WPandCut2016.py Combine_ggWW
python TurnOffCombinedSamples.py WPandCut2016.py Combine_qqWWqq
python TurnOffCombinedSamples.py WPandCut2016.py CombineSBI





cp nuisances.py nuisances_Boosted.py
cp nuisances.py nuisances_Resolved.py


#TEST
#mkShapesMulti.py --pycfg=configuration_Boosted.py --batchSplit=AsMuchAsPossible --treeName Events
#mkShapesMulti.py --pycfg=configuration_Resolved.py --batchSplit=AsMuchAsPossible --treeName Events

#mkShapesMulti.py --pycfg=configuration_Boosted_GGF_SB.py --batchSplit=AsMuchAsPossible --treeName Events

#Boosted
#mkShapesMulti.py --pycfg=configuration_Boosted_SB.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#mkShapesMulti.py --pycfg=configuration_Boosted_TOP.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
mkShapesMulti.py --pycfg=configuration_Boosted_SR.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events --samplesFile=samples_test.py

#Resolved
#mkShapesMulti.py --pycfg=configuration_Resolved_SB.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#mkShapesMulti.py --pycfg=configuration_Resolved_TOP.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
mkShapesMulti.py --pycfg=configuration_Resolved_SR.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events --samplesFile=samples_test.py
#Boosted
##--GGF
#mkShapesMulti.py --pycfg=configuration_Boosted_GGF_SB.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#mkShapesMulti.py --pycfg=configuration_Boosted_GGF_TOP.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#mkShapesMulti.py --pycfg=configuration_Boosted_GGF_SR.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events

##--VBF
#mkShapesMulti.py --pycfg=configuration_Boosted_VBF_SB.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#mkShapesMulti.py --pycfg=configuration_Boosted_VBF_TOP.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#mkShapesMulti.py --pycfg=configuration_Boosted_VBF_SR.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events

#Resolved
##--GGF
#mkShapesMulti.py --pycfg=configuration_Resolved_GGF_SB.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#mkShapesMulti.py --pycfg=configuration_Resolved_GGF_TOP.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#mkShapesMulti.py --pycfg=configuration_Resolved_GGF_SR.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events

##--VBF
#mkShapesMulti.py --pycfg=configuration_Resolved_VBF_SB.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#mkShapesMulti.py --pycfg=configuration_Resolved_VBF_TOP.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#mkShapesMulti.py --pycfg=configuration_Resolved_VBF_SR.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events



EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
echo -e "JOBDIR:${PWD}
args=$@
runtime=$(($EndTime - $StartTime))
ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch
