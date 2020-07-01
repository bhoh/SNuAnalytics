python TurnOffCombinedSamples.py nuisances.py CombineMultiV
python TurnOffCombinedSamples.py nuisances.py CombineH125
python TurnOffCombinedSamples.py nuisances.py CombineWjets
python TurnOffCombinedSamples.py samples_2017.py CombineMultiV
python TurnOffCombinedSamples.py samples_2017.py CombineH125
python TurnOffCombinedSamples.py samples_2017.py CombineWjets

COMBINED_PROC=h125
#PROCLIST=(ggHWWlnuqq_M125 vbfHWWlnuqq_M125 ZHWWlnuqq_M125 WpHWWlnuqq_M125 WmHWWlnuqq_M125 ggHtautaulnuqq_M125 vbfHtautaulnuqq_M125 WmHtautaulnuqq_M125 WpHtautaulnuqq_M125 ZHtautaulnuqq_M125)
PROCLIST=(ZHWWlnuqq_M125 WpHWWlnuqq_M125 WmHWWlnuqq_M125 ggHtautaulnuqq_M125 vbfHtautaulnuqq_M125 WmHtautaulnuqq_M125 WpHtautaulnuqq_M125 ZHtautaulnuqq_M125)

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
    (mkdir -p $rootfiledir/hadddir_${COMBINED_PROC}/temp/;StartTime=$(date +%s);python python_tool/latino/CombineShapes.py -c configuration_${bst}.py -f $rootfiledir/hadddir_${COMBINED_PROC}/plots_${COMBINED_PROC}.root -s ${PROCINPUT} -n ${COMBINED_PROC} -o;cp $rootfiledir/hadddir_${COMBINED_PROC}/plots_${COMBINED_PROC}.root_${COMBINED_PROC} $rootfiledir/plot_${COMBINED_PROC}.root;EndTime=$(date +%s);echo "runtime : $(($EndTime - $StartTime)) sec";)&>Make${COMBINED_PROC}Shape_${bst}.log&

    

done
