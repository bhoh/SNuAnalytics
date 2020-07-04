python TurnOffCombinedSamples.py WPandCut2017.py CombineMultiV
python TurnOffCombinedSamples.py WPandCut2017.py CombineH125
python TurnOffCombinedSamples.py WPandCut2017.py CombineWjets
python TurnOffCombinedSamples.py WPandCut2017.py Combine_ggWW
python TurnOffCombinedSamples.py WPandCut2017.py Combine_qqWWqq
python TurnOffCombinedSamples.py WPandCut2017.py CombineSBI


COMBINED_PROC=MultiV
PROCLIST=(WW WWW WWZ WZ WZZ ZZZ ZZ)

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
    (mkdir -p $rootfiledir/hadddir_${COMBINED_PROC}/temp/;StartTime=$(date +%s);python python_tool/latino/CombineShapes.py -c configuration_${bst}.py -f $rootfiledir/hadddir_${COMBINED_PROC}/plots_${COMBINED_PROC}.root -s ${PROCINPUT} -n ${COMBINED_PROC} -o;cp $rootfiledir/hadddir_${COMBINED_PROC}/plots_${COMBINED_PROC}.root_${COMBINED_PROC} $rootfiledir/plot_${COMBINED_PROC}.root;EndTime=$(date +%s);echo "runtime : $(($EndTime - $StartTime)) sec";)&>logs/Make${COMBINED_PROC}Shape_${bst}.log&
    

done
