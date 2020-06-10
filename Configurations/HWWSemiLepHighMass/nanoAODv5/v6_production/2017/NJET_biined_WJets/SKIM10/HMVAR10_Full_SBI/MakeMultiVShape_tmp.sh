#MakeMultiVShape_Boosted_VBF_SB.log

ARR_BOOST=(Boosted)  #(Boosted Resolved)
ARR_PROC=(VBF)  #(GGF VBF)
ARR_REGION=(SB) #(TOP SB SR)
for bst in ${ARR_BOOST[@]};do
    for proc in ${ARR_PROC[@]};do
	for rg in ${ARR_REGION[@]};do
	    input=`ls rootFile*${bst}*${proc}*${rg}/hadd.root`
	    echo $input
	    python python_tool/latino/CombineMultiV.py -c configuration_${bst}_${proc}_${rg}.py -f ${input} -s WW,WWW,WWZ,WZ,WZZ,ZZZ,ZZ &> MakeMultiVShape_${bst}_${proc}_${rg}.log &
	    
	done
    done
done


