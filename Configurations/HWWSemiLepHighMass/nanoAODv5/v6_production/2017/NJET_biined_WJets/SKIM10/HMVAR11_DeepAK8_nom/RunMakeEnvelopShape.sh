StartTime=$(date +%s)



ARR_REGION=(TOP SB SR)
ARR_PROC=(GGF VBF)

for rg in ${ARR_REGION[@]};do
    for proc in ${ARR_PROC[@]};do
        #mkShapesMulti.py --pycfg=configuration_Boosted_${proc}_${rg}.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
        #mkShapesMulti.py --pycfg=configuration_Resolved_${proc}_${rg}.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
	echo "python MakeEnvelopShape.py -c configuration_Boosted_${proc}_${rg}.py  -f hadd.root -n QCDscaleAccept" > RunMakeEnvelopShape_configuration_Boosted_${proc}_${rg}.log
	python MakeEnvelopShape.py -c configuration_Boosted_${proc}_${rg}.py  -f hadd.root -n QCDscale &> RunMakeEnvelopShape_configuration_Boosted_${proc}_${rg}.log&
	echo "python MakeEnvelopShape.py -c configuration_Resolved_${proc}_${rg}.py -f hadd.root -n QCDscaleAccept" > RunMakeEnvelopShape_configuration_Resolved_${proc}_${rg}.log
	python MakeEnvelopShape.py -c configuration_Resolved_${proc}_${rg}.py -f hadd.root -n QCDscale &> RunMakeEnvelopShape_configuration_Resolved_${proc}_${rg}.log&
    done
done


EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
echo -e "JOBDIR:${PWD}                                                                                                                                                            
args=$@                                                                                                                                                                           
runtime=$(($EndTime - $StartTime))                                                                                                                                                
ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch

