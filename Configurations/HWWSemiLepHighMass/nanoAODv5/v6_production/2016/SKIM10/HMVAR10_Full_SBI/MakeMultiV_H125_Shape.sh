

#ARR_BOOST=(Boosted Resolved)
#ARR_PROC=(GGF VBF)
#ARR_REGION=(TOP SB SR)
#for bst in ${ARR_BOOST[@]};do
#    for proc in ${ARR_PROC[@]};do
#	for rg in ${ARR_REGION[@]};do
#	    input=`ls rootFile*${bst}*${proc}*${rg}/hadd.root`
#	    python python_tool/latino/CombineMultiV.py -c configuration_${bst}_${proc}_${rg}.py -f ${input} -s WW,WWW,WWZ,WZ,WZZ,ZZZ,ZZ &> MakeMultiVShape_${bst}_${proc}_${rg}.log &
	    
#	done
 #   done
#done
##Turn off combined shape
python TurnOffCombinedSamples.py nuisances.py CombineMultiV
python TurnOffCombinedSamples.py nuisances.py CombineH125
python TurnOffCombinedSamples.py samples_2016.py CombineMultiV
python TurnOffCombinedSamples.py samples_2016.py CombineH125



cp nuisances.py nuisances_Boosted.py
cp nuisances.py nuisances_Resolved.py

ARR_BOOST=(Boosted Resolved)
for bst in ${ARR_BOOST[@]};do
	    input=`ls rootFile*${bst}*/hadd.root`
	    (python python_tool/latino/CombineShapes.py -c configuration_${bst}.py -f ${input} -s WW,WWJJ,WWW,WWZ,WZ,WZZ,ZZZ,ZZ -n MultiV &> MakeMultiVShape_${bst}.log;python python_tool/latino/CombineShapes.py -c configuration_${bst}.py -f ${input} -s ggHWWlnuqq_M125,vbfHWWlnuqq_M125,ZHWWlnuqq_M125,WpHWWlnuqq_M125,WmHWWlnuqq_M125,ggHtautaulnuqq_M125,vbfHtautaulnuqq_M125,WmHtautaulnuqq_M125,WpHtautaulnuqq_M125,ZHtautaulnuqq_M125 -n h125 &> MakeH125Shape_${bst}.log) &
done