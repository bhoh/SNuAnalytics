python TurnOffCombinedSamples.py WPandCut2017.py CombineMultiV
python TurnOffCombinedSamples.py WPandCut2017.py CombineH125
python TurnOffCombinedSamples.py WPandCut2017.py CombineWjets
python TurnOffCombinedSamples.py WPandCut2017.py Combine_ggWW
python TurnOffCombinedSamples.py WPandCut2017.py Combine_qqWWqq
python TurnOffCombinedSamples.py WPandCut2017.py CombineSBI


DefineList=`python MassPoints/List_MX.py` ## ggfhww mass points
#echo ARR_MASS=$DefineList
ARR_MASS=$DefineList
#CURDIR=$PWD
for MX in ${ARR_MASS[@]};do
    continue
    ###--- GGF
    COMBINED_PROC=ggHWWlnuqq_M${MX}_SBI
    PROCLIST=(ggHWWlnuqq_M${MX}_S ggHWWlnuqq_M${MX}_I ggWW)
    
    ARR_BOOST=(Boosted Resolved)
    CURDIR=${PWD}
    for bst in ${ARR_BOOST[@]};do
	#input=`ls rootFile*${bst}*/hadd.root`
	rootfiledir=`ls -d rootFile*${bst}*/`
	echo "rootfiledir=${rootfiledir}"
	mkdir -p $rootfiledir/hadddir_${COMBINED_PROC}/
	haddfiles=()
	for PROC in ${PROCLIST[@]};do
            haddfiles+=($(ls $rootfiledir/plot*${PROC}.*root))
	done
	haddlist=""
	for f in ${haddfiles[@]};do
            haddlist=$haddlist" "$f
	done
	#echo "haddlist=$haddlist"
	#hadd -f $rootfiledir/hadddir_${COMBINED_PROC}/plots_${COMBINED_PROC}.root ${haddlist}
	
	
	
	PROCINPUT=""
	for PROC in ${PROCLIST[@]};do
            PROCINPUT="${PROCINPUT},${PROC}"
	done
	PROCINPUT=${PROCINPUT#,}    
	
	python python_tool/ExportShellCondorSetup.py -c "cd ${CURDIR};mkdir -p $rootfiledir/hadddir_${COMBINED_PROC}/temp/;hadd -f $rootfiledir/hadddir_${COMBINED_PROC}/plots_${COMBINED_PROC}.root ${haddlist};" -d $rootfiledir/hadddir_${COMBINED_PROC}/ -n "Make${COMBINED_PROC}Shape${bst}" -m 1 -s
    done
done

DefineList=`python MassPoints/List_MX_VBF.py` ## vbfhww mass points
ARR_MASS=$DefineList
for MX in ${ARR_MASS[@]};do
    ###--VBF
    COMBINED_PROC=vbfHWWlnuqq_M${MX}_SBI
    PROCLIST=(vbfHWWlnuqq_M${MX}_S vbfHWWlnuqq_M${MX}_I qqWWqq)
    
    ARR_BOOST=(Boosted Resolved)
    CURDIR=${PWD}
    for bst in ${ARR_BOOST[@]};do
	#input=`ls rootFile*${bst}*/hadd.root`
	rootfiledir=`ls -d rootFile*${bst}*/`
	echo "rootfiledir=${rootfiledir}"
	mkdir -p $rootfiledir/hadddir_${COMBINED_PROC}/
	haddfiles=()
	for PROC in ${PROCLIST[@]};do
            haddfiles+=($(ls $rootfiledir/plot*${PROC}.*root))
	done
	haddlist=""
	for f in ${haddfiles[@]};do
            haddlist=$haddlist" "$f
	done
	echo "haddlist=$haddlist"
	#hadd -f $rootfiledir/hadddir_${COMBINED_PROC}/plots_${COMBINED_PROC}.root ${haddlist}
	
	
	
	PROCINPUT=""
	for PROC in ${PROCLIST[@]};do
            PROCINPUT="${PROCINPUT},${PROC}"
	done
	PROCINPUT=${PROCINPUT#,}    

	python python_tool/ExportShellCondorSetup.py -c "cd ${CURDIR};mkdir -p $rootfiledir/hadddir_${COMBINED_PROC}/temp/;hadd -f $rootfiledir/hadddir_${COMBINED_PROC}/plots_${COMBINED_PROC}.root ${haddlist};" -d $rootfiledir/hadddir_${COMBINED_PROC}/ -n "Make${COMBINED_PROC}Shape${bst}" -m 1 -s
    done
    

    
    
done



