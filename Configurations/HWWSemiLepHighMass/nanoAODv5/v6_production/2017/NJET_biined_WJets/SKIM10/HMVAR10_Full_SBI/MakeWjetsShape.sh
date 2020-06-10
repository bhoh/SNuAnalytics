

#ARR_BOOST=(Boosted Resolved)
#ARR_BOOST=(Resolved)
#ARR_PROC=(GGF VBF)
#ARR_REGION=(TOP SB SR)
#for bst in ${ARR_BOOST[@]};do
#    for proc in ${ARR_PROC[@]};do
#	for rg in ${ARR_REGION[@]};do
#	    input=`ls rootFile*${bst}*${proc}*${rg}/hadd.root`
#	    python python_tool/latino/CombineWjets.py -c configuration_${bst}_${proc}_${rg}.py -f ${input} -s Wjets0j,Wjets1j,Wjets2j &> MakeWjetsShape_${bst}_${proc}_${rg}.log &
#	    sleep 1
#	done
#    done
#done


ARR_BOOST=(Boosted Resolved)
for bst in ${ARR_BOOST[@]};do
            input=`ls rootFile*${bst}*/hadd.root`
            python python_tool/latino/CombineShapes.py -c configuration_${bst}.py -f ${input} -s Wjets0j,Wjets1j,Wjets2j -n Wjets &> MakeWjetsVShape_${bst}.log &
done
