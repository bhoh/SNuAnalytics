TotalStartTime=$(date +%s)

#MakevbfHWWlnuqq_M120_SBIShape_Resolved.log:NameError: name 'JETCUTS' is not defined
#MakeggHWWlnuqq_M800_SBIShape_Resolved.log:NameError: name 'JETCUTS' is not defined
cp nuisances.py nuisances_Boosted.py
cp nuisances.py nuisances_Resolved.py

python TurnOffCombinedSamples.py WPandCut2017.py CombineMultiV
python TurnOffCombinedSamples.py WPandCut2017.py CombineH125
python TurnOffCombinedSamples.py WPandCut2017.py CombineWjets
python TurnOffCombinedSamples.py WPandCut2017.py CombineSBI

python TurnOnCombinedSamples.py WPandCut2017.py Combine_ggWW
python TurnOnCombinedSamples.py WPandCut2017.py Combine_qqWWqq

#DefineList=`python MassPoints/List_MX.py` ## ggfhww mass points
#echo ARR_MASS=$DefineList
#ARR_MASS=$DefineList
#CURDIR=$PWD
#for MX in ${ARR_MASS[@]};do

NCORE=10

DefineList=`python MassPoints/List_MX.py` ## ggfhww mass points

ARR_MASS=$DefineList
ARR_MASS=(800)
for MX in ${ARR_MASS[@]};do

    COMBINED_PROC=ggHWWlnuqq_M${MX}_SBI
    PROCLIST=(ggHWWlnuqq_M${MX}_S ggHWWlnuqq_M${MX}_I ggWW)
    #ARR_BOOST=(Boosted Resolved)
    ARR_BOOST=(Resolved)
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
	echo "PROCINPUT=${PROCINPUT}"
	(mkdir -p $rootfiledir/hadddir_${COMBINED_PROC}/temp/;StartTime=$(date +%s);python python_tool/latino/CombineShapes.py -c configuration_${bst}.py -f $rootfiledir/hadddir_${COMBINED_PROC}/plots_${COMBINED_PROC}.root -s ${PROCINPUT} -n ${COMBINED_PROC} -o;cp $rootfiledir/hadddir_${COMBINED_PROC}/plots_${COMBINED_PROC}.root_${COMBINED_PROC} $rootfiledir/plot_${COMBINED_PROC}.root;EndTime=$(date +%s);echo "runtime : $(($EndTime - $StartTime)) sec";)&>logs/Make${COMBINED_PROC}Shape_${bst}.log&
    done
done


#vbfHWWlnuqq_
DefineList=`python MassPoints/List_MX_VBF.py` ## ggfhww mass points
ARR_MASS=$DefineList
ARR_MASS=(120)
#MakevbfHWWlnuqq_M120_SBIShape_Resolved.log:NameError: name 'JETCUTS' is not defined
for MX in ${ARR_MASS[@]};do
    COMBINED_PROC=vbfHWWlnuqq_M${MX}_SBI
    PROCLIST=(vbfHWWlnuqq_M${MX}_S vbfHWWlnuqq_M${MX}_I qqWWqq)
    #ARR_BOOST=(Boosted Resolved)
    ARR_BOOST=(Resolved)
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
	echo "PROCINPUT=${PROCINPUT}"
	(mkdir -p $rootfiledir/hadddir_${COMBINED_PROC}/temp/;StartTime=$(date +%s);python python_tool/latino/CombineShapes.py -c configuration_${bst}.py -f $rootfiledir/hadddir_${COMBINED_PROC}/plots_${COMBINED_PROC}.root -s ${PROCINPUT} -n ${COMBINED_PROC} -o;cp $rootfiledir/hadddir_${COMBINED_PROC}/plots_${COMBINED_PROC}.root_${COMBINED_PROC} $rootfiledir/plot_${COMBINED_PROC}.root;EndTime=$(date +%s);echo "runtime : $(($EndTime - $StartTime)) sec";)&>logs/Make${COMBINED_PROC}Shape_${bst}.log&
    done
done
TotalEndTime=$(date +%s)
echo "runtime : $(($TotalEndTime - $TotalStartTime)) sec"
