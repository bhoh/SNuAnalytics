StartTime=$(date +%s)

YEAR=2017
NSPLIT=15
mkdir -p Datacards_${YEAR}
cp nuisances.py nuisances_Boosted.py
cp nuisances.py nuisances_Resolved.py


DefineList=`python MassPoints/List_MX_common.py`
#echo ARR_MASS=$DefineList                                                                                                                     
ARR_MASS=$DefineList






inputBoost=`ls rootFile*Boost*/hadd.root`
inputResol=`ls rootFile*Resol*/hadd.root`

#ARR_MASS=(1000)
TOTAL_MX=""
for MX in ${ARR_MASS[@]};do
    TOTAL_MX="$TOTAL_MX,${MX}"
done



##

ListFlavor=(mu ele)
ListRegion=(TOP SB SR)
ListProc=(VBF GGF)
for MX in ${ARR_MASS[@]};do
    echo "${MX} in ${TOTAL_MX}"
    for flv in ${ListFlavor[@]};do
	#continue
	for rg in ${ListRegion[@]};do
            for proc in ${ListProc[@]};do
		#echo "${MX}, ${flv} , ${rg} ,${proc}"
		#rootFile_2017_Boosted_SKIM10_HMVar10_Fullvar_GGF_SB
		#configuration_Boosted_GGF_SB.py
		#            os.system('cp cuts_'+boosted+'.py '+'cuts_'+boosted+'_'+proc+'_'+rg+'_'+flv+'.py')
		input=`ls rootFile*Boost*${proc}*${rg}/hadd.root`
		#echo ${input}
		mkDatacards.py --pycfg=configuration_Boosted_${proc}_${rg}.py --structureFile=MassPoints/structure_M${MX}_${flv}.py --cutsFile=cuts_Boosted_${proc}_${rg}_${flv}.py --inputFile=$input --outputDirDatacard=Datacards_${YEAR}/Datacard_M${MX} --samplesFile=MassPoints/samples_${YEAR}limit_M${MX}_${flv}.py --variablesFile=variables_Boosted_Final.py &> Run_mkDatacards_cuts_Boosted_${proc}_${rg}_${flv}_M${MX}.log&

		input=`ls rootFile*Resol*${proc}*${rg}/hadd.root`
		#echo ${input}
		mkDatacards.py --pycfg=configuration_Resolved_${proc}_${rg}.py --structureFile=MassPoints/structure_M${MX}_${flv}.py --cutsFile=cuts_Resolved_${proc}_${rg}_${flv}.py --inputFile=$input --outputDirDatacard=Datacards_${YEAR}/Datacard_M${MX} --samplesFile=MassPoints/samples_${YEAR}limit_M${MX}_${flv}.py --variablesFile=variables_Resolved_Final.py &> Run_mkDatacards_cuts_Resolved_${proc}_${rg}_${flv}_M${MX}.log&
		
			
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
done
EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"


