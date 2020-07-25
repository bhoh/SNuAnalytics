python TurnOffCombinedSamples.py nuisances.py CombineMultiV
python TurnOffCombinedSamples.py nuisances.py CombineH125
python TurnOffCombinedSamples.py nuisances.py CombineWjets
python TurnOffCombinedSamples.py samples_2017.py CombineMultiV
python TurnOffCombinedSamples.py samples_2017.py CombineH125
python TurnOffCombinedSamples.py samples_2017.py CombineWjets

COMBINED_PROC=qqWWqq
PROCLIST=(WWJJ vbfHWWlnuqq_M125)

ARR_BOOST=(Boosted Resolved)
CURDIR=${PWD}
for bst in ${ARR_BOOST[@]};do
    #input=`ls rootFile*${bst}*/hadd.root`
    rootfiledir=`ls -d rootFile*${bst}*/`
    echo "rootfiledir=${rootfiledir}"
    mkdir -p $rootfiledir/hadddir_${COMBINED_PROC}/
    PROCINPUT=""
    for PROC in ${PROCLIST[@]};do
        PROCINPUT="${PROCINPUT},${PROC}"
    done
    PROCINPUT=${PROCINPUT#,}    
    ##--interactive
    (mkdir -p $rootfiledir/hadddir_${COMBINED_PROC}/temp/;StartTime=$(date +%s);python python_tool/latino/CombineShapes.py -c configuration_${bst}.py -f $rootfiledir/hadddir_${COMBINED_PROC}/hadd_${COMBINED_PROC}.root -s ${PROCINPUT} -n ${COMBINED_PROC} -o;cp $rootfiledir/hadddir_${COMBINED_PROC}/hadd_${COMBINED_PROC}.root_${COMBINED_PROC} $rootfiledir/plot_${COMBINED_PROC}.root;EndTime=$(date +%s);echo "runtime : $(($EndTime - $StartTime)) sec";)&>logs/Make${COMBINED_PROC}Shape_${bst}.log&
    

done
echo "Make_qqwwqq_shape.sh" >>mylog.txt
