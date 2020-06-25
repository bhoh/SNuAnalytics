TotalStartTime=$(date +%s)
python TurnOffCombinedSamples.py nuisances.py CombineMultiV
python TurnOffCombinedSamples.py nuisances.py CombineH125
python TurnOffCombinedSamples.py nuisances.py CombineWjets
python TurnOffCombinedSamples.py samples_2017.py CombineMultiV
python TurnOffCombinedSamples.py samples_2017.py CombineH125
python TurnOffCombinedSamples.py samples_2017.py CombineWjets

#DefineList=`python MassPoints/List_MX.py` ## ggfhww mass points
#echo ARR_MASS=$DefineList
#ARR_MASS=$DefineList
#CURDIR=$PWD
#for MX in ${ARR_MASS[@]};do

NCORE=10

DefineList=`python MassPoints/List_MX.py` ## ggfhww mass points
ARR_MASS=$DefineList
for MX in ${ARR_MASS[@]};do
    continue
    COMBINED_PROC=ggHWWlnuqq_M${MX}_SBI
    PROCLIST=(ggHWWlnuqq_M${MX}_S ggHWWlnuqq_M${MX}_I ggWW)
    ARR_BOOST=(Boosted Resolved)
    CURDIR=${PWD}
    for bst in ${ARR_BOOST[@]};do
	echo "MX=${MX},$bst"
	rootfiledir=`ls -d rootFile*${bst}*/`
	echo "rootfiledir=${rootfiledir}"
	mkdir -p $rootfiledir/hadddir_${COMBINED_PROC}/
	
	PROCINPUT=""
	for PROC in ${PROCLIST[@]};do
            PROCINPUT="${PROCINPUT},${PROC}"
	done
	PROCINPUT=${PROCINPUT#,}    
	##--interactive
	
	while [ 1 ];do
	    NJOB=`jobs|wc -l`
	    echo "NJOB=$NJOB"
	    if [ ${NJOB} -lt ${NCORE} ];then
		echo "NJOB < ${NCORE}"
		break
	    fi
	    sleep 15
	done

	
	echo "MASS=${MX},${bst}"
	(mkdir -p $rootfiledir/hadddir_${COMBINED_PROC}/temp/;StartTime=$(date +%s);python python_tool/latino/CombineShapes.py -c configuration_${bst}.py -f $rootfiledir/hadddir_${COMBINED_PROC}/plots_${COMBINED_PROC}.root -s ${PROCINPUT} -n ${COMBINED_PROC} -o;cp $rootfiledir/hadddir_${COMBINED_PROC}/plots_${COMBINED_PROC}.root_${COMBINED_PROC} $rootfiledir/plot_${COMBINED_PROC}.root;EndTime=$(date +%s);echo "runtime : $(($EndTime - $StartTime)) sec";)&>Make${COMBINED_PROC}Shape_${bst}.log&
    done
done


#vbfHWWlnuqq_
DefineList=`python MassPoints/List_MX_VBF.py` ## ggfhww mass points
ARR_MASS=$DefineList
for MX in ${ARR_MASS[@]};do
    COMBINED_PROC=vbfHWWlnuqq_M${MX}_SBI
    PROCLIST=(vbfHWWlnuqq_M${MX}_S vbfHWWlnuqq_M${MX}_I qqWWqq)
    ARR_BOOST=(Boosted Resolved)
    CURDIR=${PWD}
    for bst in ${ARR_BOOST[@]};do
	echo "MX=${MX},$bst"
	rootfiledir=`ls -d rootFile*${bst}*/`
	echo "rootfiledir=${rootfiledir}"
	mkdir -p $rootfiledir/hadddir_${COMBINED_PROC}/
	
	PROCINPUT=""
	for PROC in ${PROCLIST[@]};do
            PROCINPUT="${PROCINPUT},${PROC}"
	done
	PROCINPUT=${PROCINPUT#,}    
	##--interactive
	while [ 1 ];do
	    NJOB=`jobs|wc -l`
	    if [ $NJOB -lt ${NCORE} ];then
		echo "NJOB < ${NCORE}"
		break
	    fi
	    sleep 15
	done
	echo "MASS=${MX},${bst}"
	(mkdir -p $rootfiledir/hadddir_${COMBINED_PROC}/temp/;StartTime=$(date +%s);python python_tool/latino/CombineShapes.py -c configuration_${bst}.py -f $rootfiledir/hadddir_${COMBINED_PROC}/plots_${COMBINED_PROC}.root -s ${PROCINPUT} -n ${COMBINED_PROC} -o;cp $rootfiledir/hadddir_${COMBINED_PROC}/plots_${COMBINED_PROC}.root_${COMBINED_PROC} $rootfiledir/plot_${COMBINED_PROC}.root;EndTime=$(date +%s);echo "runtime : $(($EndTime - $StartTime)) sec";)&>Make${COMBINED_PROC}Shape_${bst}.log&
    done
done
TotalEndTime=$(date +%s)
echo "runtime : $(($TotalEndTime - $TotalStartTime)) sec"
