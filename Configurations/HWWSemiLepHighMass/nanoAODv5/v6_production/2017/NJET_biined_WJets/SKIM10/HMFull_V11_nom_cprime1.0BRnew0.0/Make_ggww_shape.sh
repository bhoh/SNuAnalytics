python TurnOffCombinedSamples.py WPandCut2017.py CombineMultiV
python TurnOffCombinedSamples.py WPandCut2017.py CombineH125
python TurnOffCombinedSamples.py WPandCut2017.py CombineWjets
python TurnOffCombinedSamples.py WPandCut2017.py Combine_ggWW
python TurnOffCombinedSamples.py WPandCut2017.py Combine_qqWWqq
python TurnOffCombinedSamples.py WPandCut2017.py CombineSBI



#ARR_BOOST=(Boosted Resolved)
#for bst in ${ARR_BOOST[@]};do
#	    input=`ls rootFile*${bst}*/hadd.root`
#	    python python_tool/latino/CombineShapes.py -c configuration_${bst}.py -f ${input} -s WW,WWW,WWZ,WZ,WZZ,ZZZ,ZZ -n MultiV &> MakeMultiVShape_${bst}.log &
#done


#---Boosted--

#ggHWWlnuqq_M450_B
#ggHWWlnuqq_M500_B
#ggHWWlnuqq_M550_B
#ggHWWlnuqq_M600_B
#ggHWWlnuqq_M650_B
#ggHWWlnuqq_M700_B
#ggHWWlnuqq_M750_B
#ggHWWlnuqq_M800_B
#listB="ggHWWlnuqq_M450_B,ggHWWlnuqq_M500_B,ggHWWlnuqq_M550_B,ggHWWlnuqq_M600_B,ggHWWlnuqq_M650_B,ggHWWlnuqq_M700_B,ggHWWlnuqq_M750_B,ggHWWlnuqq_M800_B"
listB=(ggHWWlnuqq_M450_B
    ggHWWlnuqq_M500_B
    ggHWWlnuqq_M550_B
    ggHWWlnuqq_M600_B
    ggHWWlnuqq_M650_B
    ggHWWlnuqq_M700_B
    ggHWWlnuqq_M750_B
    ggHWWlnuqq_M800_B
    #ggHWWlnuqq_M125
)
rootfiledir=`ls -d rootFile*Boosted*/`
echo ${rootfiledir}
##hadd above process files
haddlist=""
for p in ${listB[@]};do
    #echo "ls rootFile*Boost*/hadddir_${p}/hadd_${p}.root"
    thisfile=`ls ${rootfiledir}/hadddir_${p}/hadd_${p}.root`
    echo $thisfile
    haddlist=$haddlist" $thisfile"
done
echo $haddlist
mkdir -p ${rootfiledir}/ggWWnoH/
ggWWfile=${rootfiledir}/ggWWnoH/plots_ggWWnoH.root
echo $ggWWfile
echo "hadd -f ${ggWWfile} ${haddlist}"
hadd -f ${ggWWfile} ${haddlist}

PROCINPUT=""
for PROC in ${listB[@]};do
    PROCINPUT="${PROCINPUT},${PROC}"
done
PROCINPUT=${PROCINPUT#,}
#(python python_tool/latino/CombineShapesToAvg.py -c configuration_Boosted.py -f ${ggWWfile} -s ${PROCINPUT} -n ggWWnoH -o;cp ${ggWWfile}_ggWW ${rootfiledir}/plot_ggWW.root)&> logs/Make_ggww_shape_Boosted.log&
(python python_tool/latino/CombineShapesToAvg.py -c configuration_Boosted.py -f ${ggWWfile} -s ${PROCINPUT} -n ggWWnoH -o)&> logs/Make_ggww_shape_Boosted.log&
##ggWWnoH is created
##hadd ggWWnoH + ggHWWlnuqq_M125
(mkdir -p ${rootfiledir}/ggWW/;hadd -f ${rootfiledir}/ggWW/plot_ggWW.root ${rootfiledir}/ggWWnoH/plots_ggWWnoH.root_ggWWnoH ${rootfiledir}/hadddir_ggHWWlnuqq_M125/hadd_ggHWWlnuqq_M125.root;python python_tool/latino/CombineShapes.py -c configuration_Boosted.py -f ${rootfiledir}/ggWW/plot_ggWW.root -s ggWWnoH,ggHWWlnuqq_M125 -n ggWW -o;cp ${rootfiledir}/ggWW/plot_ggWW.root_ggWW ${rootfiledir}/plot_ggWW.root;)

#(mkdir -p $rootfiledir/hadddir_${COMBINED_PROC}/temp/;StartTime=$(date +%s);python python_tool/latino/CombineShapes.py -c configuration_${bst}.py -f $rootfiledir/hadddir_${COMBINED_PROC}/plots_${COMBINED_PROC}.root -s ${PROCINPUT} -n ${COMBINED_PROC} -o;cp $rootfiledir/hadddir_${COMBINED_PROC}/plots_${COMBINED_PROC}.root_${COMBINED_PROC} $rootfiledir/plot_${COMBINED_PROC}.root;EndTime=$(date +%s);echo "runtime : $(($EndTime - $StartTime)) sec";)&>logs/Make${COMBINED_PROC}Shape_${bst}.log&

#--Resolved
listR=(
ggHWWlnuqq_M300_B
ggHWWlnuqq_M350_B
ggHWWlnuqq_M400_B
ggHWWlnuqq_M450_B
ggHWWlnuqq_M500_B
ggHWWlnuqq_M550_B
ggHWWlnuqq_M600_B
#ggHWWlnuqq_M125
)
rootfiledir=`ls -d rootFile*Resolved*/`
echo ${rootfiledir}
##hadd_above process files
haddlist=""
for p in ${listR[@]};do
    thisfile=`ls ${rootfiledir}/hadddir_${p}/hadd_${p}.root`
    echo $thisfile
    haddlist=$haddlist" $thisfile"
done
echo $haddlist
mkdir -p ${rootfiledir}/ggWWnoH/
ggWWfile=${rootfiledir}/ggWWnoH/plots_ggWWnoH.root
echo $ggWWfile
echo "hadd -f ${ggWWfile} ${haddlist}"
hadd -f ${ggWWfile} ${haddlist}

PROCINPUT=""
for PROC in ${listR[@]};do
    PROCINPUT="${PROCINPUT},${PROC}"
done
PROCINPUT=${PROCINPUT#,}

#(python python_tool/latino/CombineShapesToAvg.py -c configuration_Resolved.py -f ${ggWWfile} -s ${PROCINPUT} -n ggWW -o;cp ${ggWWfile}_ggWW ${rootfiledir}/plot_ggWW.root)&> logs/Make_ggww_shape_Resolved.log&
(python python_tool/latino/CombineShapesToAvg.py -c configuration_Resolved.py -f ${ggWWfile} -s ${PROCINPUT} -n ggWWnoH -o)&> logs/Make_ggww_shape_Resolved.log&
(mkdir -p ${rootfiledir}/ggWW/;hadd -f ${rootfiledir}/ggWW/plot_ggWW.root ${rootfiledir}/ggWWnoH/plots_ggWWnoH.root_ggWWnoH ${rootfiledir}/hadddir_ggHWWlnuqq_M125/hadd_ggHWWlnuqq_M125.root;python python_tool/latino/CombineShapes.py -c configuration_Resolved.py -f ${rootfiledir}/ggWW/plot_ggWW.root -s ggWWnoH,ggHWWlnuqq_M125 -n ggWW -o;cp ${rootfiledir}/ggWW/plot_ggWW.root_ggWW ${rootfiledir}/plot_ggWW.root)
