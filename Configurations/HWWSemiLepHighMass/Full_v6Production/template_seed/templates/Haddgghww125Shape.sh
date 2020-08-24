COMBINED_PROC=ggHWWlnuqq_M125
PROCLIST=(ggHWWlnuqq_M125)
ARR_BOOST=(Boosted Resolved)
CURDIR=${PWD}
for bst in ${ARR_BOOST[@]};do
    #input=`ls rootFile*${bst}*/hadd.root`
    rootfiledir=`ls -d rootFile*${bst}*/`
    echo "rootfiledir=${rootfiledir}"
    mkdir -p $rootfiledir/hadddir_${COMBINED_PROC}/
    haddfiles=()
    for PROC in ${PROCLIST[@]};do
	#haddfiles=($(ls ${rootfiledir}/plot*ggHWWlnuqq_M125.*root))
	#haddfiles+=($(ls $rootfiledir/plot*vbfHWWlnuqq_M125.*root))
	#haddfiles+=($(ls $rootfiledir/plot*ZHWWlnuqq_M125.*root))
	haddfiles+=($(ls $rootfiledir/plot*${PROC}.*root))
    done
    haddlist=""
    for f in ${haddfiles[@]};do
    #	echo "-"
    #   echo ${f}
	haddlist=$haddlist" "$f
    done
    echo "haddlist=$haddlist"
    ##--interactive
    #(mkdir -p $rootfiledir/hadddir_Wjets/temp/;StartTime=$(date +%s);hadd -j 10 -d $rootfiledir/hadddir_Wjets/temp/ -f $rootfiledir/hadddir_Wjets/plots_Wjets.root ${haddlist};python python_tool/latino/CombineShapes.py -c configuration_${bst}.py -f ${input} -s Wjets0j,Wjets1j,Wjets2j -n Wjets -o;echo "runtime : $(($EndTime - $StartTime)) sec";)>MakeWjetsShape_${bst}.log&
    ##--batch
    PROCINPUT=""
    for PROC in ${PROCLIST[@]};do
	PROCINPUT="${PROCINPUT},${PROC}"
    done
    PROCINPUT=${PROCINPUT#,}
    #python python_tool/ExportShellCondorSetup.py -c "cd ${CURDIR};mkdir -p $rootfiledir/hadddir_${COMBINED_PROC}/temp/;hadd -j 10 -d $rootfiledir/hadddir_${COMBINED_PROC}/temp/ -f $rootfiledir/hadddir_${COMBINED_PROC}/plots_${COMBINED_PROC}.root ${haddlist};python python_tool/latino/CombineShapes.py -c configuration_${bst}.py -f ${input} -s ${PROCINPUT} -n ${COMBINED_PROC} -o;" -d $rootfiledir/hadddir_${COMBINED_PROC}/ -n "Make${COMBINED_PROC}Shape${bst}" -m 10 -s
    python python_tool/ExportShellCondorSetup.py -c "cd ${CURDIR};mkdir -p $rootfiledir/hadddir_${COMBINED_PROC}/temp/;hadd -j 10 -d $rootfiledir/hadddir_${COMBINED_PROC}/temp/ -f $rootfiledir/hadddir_${COMBINED_PROC}/hadd_${COMBINED_PROC}.root ${haddlist};" -d $rootfiledir/hadddir_${COMBINED_PROC}/ -n "Make${COMBINED_PROC}Shape${bst}" -m 10 -s

done

echo "Haddgghww125Shape.sh" >> mylog.txt
