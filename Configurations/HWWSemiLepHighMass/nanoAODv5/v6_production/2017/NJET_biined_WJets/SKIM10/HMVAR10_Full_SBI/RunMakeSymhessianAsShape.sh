StartTime=$(date +%s)

ARR_REGION=(TOP SB SR)
ARR_PROC=(GGF VBF)

for rg in ${ARR_REGION[@]};do
    for proc in ${ARR_PROC[@]};do
        #python MakeEnvelopShape.py -c configuration_Boosted_${proc}_${rg}.py  -f hadd.root -n QCDscale &> RunMakeEnvelopShape_configuration_Boosted_${proc}_${rg}.log&
        #python MakeEnvelopShape.py -c configuration_Resolved_${proc}_${rg}.py -f hadd.root -n QCDscale &> RunMakeEnvelopShape_configuration_Resolved_${proc}_${rg}.log&
	echo "(python MakeSymhessianAsShape.py -c configuration_Boosted_${proc}_${rg}.py -f hadd.root -n PDF4LHC15_nnlo_30_pdfas;python MakeSymhessianAsShape.py -c configuration_Boosted_${proc}_${rg}.py -f hadd.root -n NNPDF31_nnlo_hessian_pdfas)" > RunMakeSymhessianAsShape_configuration_Boosted_${proc}_${rg}.log
	(python MakeSymhessianAsShape.py -c configuration_Boosted_${proc}_${rg}.py -f hadd.root -n PDF4LHC15_nnlo_30_pdfas;python MakeSymhessianAsShape.py -c configuration_Boosted_${proc}_${rg}.py -f hadd.root -n NNPDF31_nnlo_hessian_pdfas) &> RunMakeSymhessianAsShape_configuration_Boosted_${proc}_${rg}.log&


	echo "(python MakeSymhessianAsShape.py -c configuration_Resolved_${proc}_${rg}.py -f hadd.root -n PDF4LHC15_nnlo_30_pdfas;python MakeSymhessianAsShape.py -c configuration_Resolved_${proc}_${rg}.py -f hadd.root -n NNPDF31_nnlo_hessian_pdfas)" > RunMakeSymhessianAsShape_configuration_Resolved_${proc}_${rg}.log
	(python MakeSymhessianAsShape.py -c configuration_Resolved_${proc}_${rg}.py -f hadd.root -n PDF4LHC15_nnlo_30_pdfas;python MakeSymhessianAsShape.py -c configuration_Resolved_${proc}_${rg}.py -f hadd.root -n NNPDF31_nnlo_hessian_pdfas) &> RunMakeSymhessianAsShape_configuration_Resolved_${proc}_${rg}.log&
	
    done
done



EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
