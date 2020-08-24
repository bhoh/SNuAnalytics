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


##




#Run_mkDatacards_cuts_Resolved_VBF_TOP_ele_M1000
#ListProc=(VBF) # VBF GGF)
#ListRegion=(TOP) # TOP SB SR)
#ListFlavor=(ele) # ele mu)

ListProc=(VBF GGF) # VBF GGF)
ListRegion=(SR SB TOP) # TOP SB SR)
ListFlavor=(ele mu) # ele mu)
ARR_MASS=(1000)



TOTAL_MX=""
for MX in ${ARR_MASS[@]};do
    TOTAL_MX="$TOTAL_MX,${MX}"
done




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
		    break
                    NJOB=`jobs|wc -l`
                    if [ $NJOB -lt ${NSPLIT} ];then
                        echo "NJOB < ${NSPLIT}"
                        break
                    fi
                    sleep 5
                done



	    done
	done
    done
done
EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"


