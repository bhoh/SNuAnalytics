#MakevbfHWWlnuqq_M124_SBIShape_Boosted.log:cp: cannot stat 'rootFile_2017_Boosted_SKIM10_HMVar10_Full_SBI//hadddir_vbfHWWlnuqq_M124_SBI/plots_vbfHWWlnuqq_M124_SBI.root_vbfHWWlnuqq_M124_SBI': No such file or directory
#MakevbfHWWlnuqq_M124_SBIShape_Resolved.log:cp: cannot stat 'rootFile_2017_Resolved_SKIM10_HMVar10_Full_SBI//hadddir_vbfHWWlnuqq_M124_SBI/plots_vbfHWWlnuqq_M124_SBI.root_vbfHWWlnuqq_M124_SBI': No such file or directory
#MakevbfHWWlnuqq_M190_SBIShape_Boosted.log:cp: cannot stat 'rootFile_2017_Boosted_SKIM10_HMVar10_Full_SBI//hadddir_vbfHWWlnuqq_M190_SBI/plots_vbfHWWlnuqq_M190_SBI.root_vbfHWWlnuqq_M190_SBI': No such file or directory
#MakevbfHWWlnuqq_M190_SBIShape_Resolved.log:cp: cannot stat 'rootFile_2017_Resolved_SKIM10_HMVar10_Full_SBI//hadddir_vbfHWWlnuqq_M190_SBI/plots_vbfHWWlnuqq_M190_SBI.root_vbfHWWlnuqq_M190_SBI': No such file or directory
#MakevbfHWWlnuqq_M700_SBIShape_Boosted.log:cp: cannot stat 'rootFile_2017_Boosted_SKIM10_HMVar10_Full_SBI//hadddir_vbfHWWlnuqq_M700_SBI/plots_vbfHWWlnuqq_M700_SBI.root_vbfHWWlnuqq_M700_SBI': No such file or directory


python TurnOffCombinedSamples.py nuisances.py CombineMultiV
python TurnOffCombinedSamples.py nuisances.py CombineH125
python TurnOffCombinedSamples.py nuisances.py CombineWjets
python TurnOffCombinedSamples.py samples_2017.py CombineMultiV
python TurnOffCombinedSamples.py samples_2017.py CombineH125
python TurnOffCombinedSamples.py samples_2017.py CombineWjets

DefineList=`python MassPoints/List_MX.py` ## ggfhww mass points
#echo ARR_MASS=$DefineList
ARR_MASS=$DefineList
#CURDIR=$PWD
ARR_MASS=(124)
for MX in ${ARR_MASS[@]};do
    ###--- GGF
    COMBINED_PROC=ggHWWlnuqq_M${MX}_SBI
    PROCLIST=(ggHWWlnuqq_M${MX}_S ggHWWlnuqq_M${MX}_I h125 ggWW)
    
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


DefineList=`python MassPoints/List_MX_VBF.py` ## vbfhww mass points
ARR_MASS=$DefineList
###--VBF
ARR_MASS=(190)
COMBINED_PROC=vbfHWWlnuqq_M${MX}_SBI
PROCLIST=(vbfHWWlnuqq_M${MX}_S vbfHWWlnuqq_M${MX}_I h125 ggWW)

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



