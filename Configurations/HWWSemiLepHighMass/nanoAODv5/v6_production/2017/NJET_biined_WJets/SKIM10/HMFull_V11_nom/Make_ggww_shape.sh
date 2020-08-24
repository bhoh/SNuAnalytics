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
    ggHWWlnuqq_M125
)
rootfiledir=`ls -d rootFile*Boost*/`
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
mkdir -p ${rootfiledir}/ggWW/
ggWWfile=${rootfiledir}/ggWW/plots_ggWW.root
echo $ggWWfile
echo "hadd -f ${ggWWfile} ${haddlist}"
hadd -f ${ggWWfile} ${haddlist}

PROCINPUT=""
for PROC in ${listB[@]};do
    PROCINPUT="${PROCINPUT},${PROC}"
done
PROCINPUT=${PROCINPUT#,}
(python python_tool/latino/CombineShapesToAvg.py -c configuration_Boosted.py -f ${ggWWfile} -s ${PROCINPUT} -n ggWW -o;cp ${ggWWfile}_ggWW ${rootfiledir}/plot_ggWW.root)&> logs/Make_ggww_shape_Boosted.log&


#--Resolved
listR=(
ggHWWlnuqq_M300_B
ggHWWlnuqq_M350_B
ggHWWlnuqq_M400_B
ggHWWlnuqq_M450_B
ggHWWlnuqq_M500_B
ggHWWlnuqq_M550_B
ggHWWlnuqq_M600_B
ggHWWlnuqq_M125
)
rootfiledir=`ls -d rootFile*Resol*/`
echo ${rootfiledir}
##hadd_above process files
haddlist=""
for p in ${listR[@]};do
    thisfile=`ls ${rootfiledir}/hadddir_${p}/hadd_${p}.root`
    echo $thisfile
    haddlist=$haddlist" $thisfile"
done
echo $haddlist
mkdir -p ${rootfiledir}/ggWW/
ggWWfile=${rootfiledir}/ggWW/plots_ggWW.root
echo $ggWWfile
echo "hadd -f ${ggWWfile} ${haddlist}"
hadd -f ${ggWWfile} ${haddlist}

PROCINPUT=""
for PROC in ${listR[@]};do
    PROCINPUT="${PROCINPUT},${PROC}"
done
PROCINPUT=${PROCINPUT#,}

(python python_tool/latino/CombineShapesToAvg.py -c configuration_Resolved.py -f ${ggWWfile} -s ${PROCINPUT} -n ggWW -o;cp ${ggWWfile}_ggWW ${rootfiledir}/plot_ggWW.root)&> logs/Make_ggww_shape_Resolved.log&


