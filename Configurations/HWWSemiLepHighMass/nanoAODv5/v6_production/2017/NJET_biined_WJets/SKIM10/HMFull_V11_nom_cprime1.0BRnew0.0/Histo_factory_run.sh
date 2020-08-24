mkdir -p logs/
StartTime=$(date +%s)

python TurnOffCombinedSamples.py WPandCut2017.py CombineMultiV
python TurnOffCombinedSamples.py WPandCut2017.py CombineH125
python TurnOffCombinedSamples.py WPandCut2017.py CombineWjets
python TurnOffCombinedSamples.py WPandCut2017.py Combine_ggWW
python TurnOffCombinedSamples.py WPandCut2017.py Combine_qqWWqq
python TurnOffCombinedSamples.py WPandCut2017.py CombineSBI





cp nuisances.py nuisances_Boosted.py
cp nuisances.py nuisances_Resolved.py


#TEST
#mkShapesMulti.py --pycfg=configuration_Boosted.py --batchSplit=AsMuchAsPossible --treeName Events
#mkShapesMulti.py --pycfg=configuration_Resolved.py --batchSplit=AsMuchAsPossible --treeName Events

##ALL

#python SpanConfigCut.py Boosted
#python SpanConfigCut.py Resolved
#ARR_REGION=(SR SB TOP)
#ARR_REGION=(SR)
#ARR_PROC=(GGF VBF)

#for rg in ${ARR_REGION[@]};do
    #for proc in ${ARR_PROC[@]};do
	#echo "${rg}"
mkShapesMulti.py --pycfg=configuration_Boosted.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
mkShapesMulti.py --pycfg=configuration_Resolved.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
    #done
#done

#ONLY FINAL Variable

#mkShapesMulti.py --pycfg=configuration_Boosted_Final.py --batchSplit=AsMuchAsPossible --variablesFile=variables_Boosted_Final.py --doBatch --treeName Events 
#mkShapesMulti.py --pycfg=configuration_Resolved_Final.py --batchSplit=AsMuchAsPossible --variablesFile=variables_Resolved_Final.py --doBatch --treeName Events


EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
echo -e "JOBDIR:${PWD}
args=$@
runtime=$(($EndTime - $StartTime))
ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch
