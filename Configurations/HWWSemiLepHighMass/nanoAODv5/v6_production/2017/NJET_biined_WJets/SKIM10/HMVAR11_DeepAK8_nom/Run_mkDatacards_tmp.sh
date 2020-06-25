StartTime=$(date +%s)

python TurnOnCombinedSamples.py nuisances.py CombineMultiV
python TurnOnCombinedSamples.py nuisances.py CombineH125
python TurnOnCombinedSamples.py nuisances.py CombineWjets
python TurnOnCombinedSamples.py samples_2017.py CombineMultiV
python TurnOnCombinedSamples.py samples_2017.py CombineH125
python TurnOnCombinedSamples.py samples_2017.py CombineWjets


YEAR=2017
NSPLIT=15
mkdir -p Datacards_${YEAR}
cp nuisances.py nuisances_Boosted.py
cp nuisances.py nuisances_Resolved.py


DefineList=`python MassPoints/List_MX_common.py`
#echo ARR_MASS=$DefineList                                                                                                                     
ARR_MASS=$DefineList






#inputBoost=`ls rootFile*Boost*/hadd.root`
#inputResol=`ls rootFile*Resol*/hadd.root`

ARR_MASS=(1000)
TOTAL_MX=""
for MX in ${ARR_MASS[@]};do
    TOTAL_MX="$TOTAL_MX,${MX}"
done



##

ListFlavor=(mu ele)
#ListRegion=(TOP SB SR)
ListRegion=(SR CR)
#ListProc=(VBF GGF)
for MX in ${ARR_MASS[@]};do
    
    for flv in ${ListFlavor[@]};do
	#input=`ls rootFile*Boost*/backup2/hadd.root`
	
	#echo ${input}
	for rg in ${ListRegion[@]};do
	    input=`ls rootFile*Boost*/hadd.root`
	    cp cuts_Boosted.py cuts_Boosted_${flv}_${rg}.py
	    mkDatacards.py --pycfg=configuration_Boosted.py --structureFile=MassPoints/structure_M${MX}_${flv}_${rg}.py --cutsFile=cuts_Boosted_${flv}_${rg}.py --inputFile=$input --outputDirDatacard=Datacards_${YEAR}/Datacard_M${MX} --samplesFile=MassPoints/samples_${YEAR}limit_M${MX}_${flv}_${rg}.py --variablesFile=variables_Boosted_Final.py &> Run_mkDatacards_cuts_Boosted_${flv}_M${MX}_${rg}.log&	
	    input=`ls rootFile*Resol*/hadd.root`
	    #echo ${input}
	    cp cuts_Resolved.py cuts_Resolved_${flv}_${rg}.py
	    mkDatacards.py --pycfg=configuration_Resolved.py --structureFile=MassPoints/structure_M${MX}_${flv}_${rg}.py --cutsFile=cuts_Resolved_${flv}_${rg}.py --inputFile=$input --outputDirDatacard=Datacards_${YEAR}/Datacard_M${MX} --samplesFile=MassPoints/samples_${YEAR}limit_M${MX}_${flv}_${rg}.py --variablesFile=variables_Resolved_Final.py &> Run_mkDatacards_cuts_Resolved_${flv}_M${MX}_${rg}.log&
		
	
	    while [ 1 ];do
		NJOB=`jobs|wc -l`
		if [ $NJOB -lt ${NSPLIT} ];then
                    echo "NJOB < ${NSPLIT}"
                    break
		fi
		sleep 3
            done
	done

	
    done
done

EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"


