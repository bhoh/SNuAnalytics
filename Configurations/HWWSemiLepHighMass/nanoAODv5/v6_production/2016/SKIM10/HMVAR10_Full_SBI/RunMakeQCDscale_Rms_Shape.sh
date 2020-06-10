StartTime=$(date +%s)
python TurnOffCombinedSamples.py nuisances.py CombineMultiV
python TurnOffCombinedSamples.py nuisances.py CombineH125
python TurnOffCombinedSamples.py samples_2016.py CombineMultiV
python TurnOffCombinedSamples.py samples_2016.py CombineH125

#ARR_REGION=(TOP SB SR)
#ARR_PROC=(GGF VBF)

#for rg in ${ARR_REGION[@]};do
#    for proc in ${ARR_PROC[@]};do
        #python MakeEnvelopShape.py -c configuration_Boosted_${proc}_${rg}.py  -f hadd.root -n QCDscale &> RunMakeEnvelopShape_configuration_Boosted_${proc}_${rg}.log&
        #python MakeEnvelopShape.py -c configuration_Resolved_${proc}_${rg}.py -f hadd.root -n QCDscale &> RunMakeEnvelopShape_configuration_Resolved_${proc}_${rg}.log&
	#echo "(python MakeEnvelopShape.py -c configuration_Boosted_${proc}_${rg}.py  -f hadd.root -n QCDscaleAccept;python MakeRmsShape.py -c configuration_Boosted_${proc}_${rg}.py -f hadd.root -n PDF4LHC15_nnlo_30_pdfas;python MakeRmsShape.py -c configuration_Boosted_${proc}_${rg}.py -f hadd.root -n NNPDF31_nnlo_hessian_pdfas)" > RunMakeQCDscale_Rms_Shape_configuration_Boosted_${proc}_${rg}.log
#	echo "(python MakeEnvelopShape.py -c configuration_Boosted_${proc}_${rg}.py  -f hadd.root -n QCDscaleAccept;python MakeRmsShape.py -c configuration_Boosted_${proc}_${rg}.py -f hadd.root -n pdfAccept;" > RunMakeQCDscale_Rms_Shape_configuration_Boosted_${proc}_${rg}.log
	#(python MakeEnvelopShape.py -c configuration_Boosted_${proc}_${rg}.py  -f hadd.root -n QCDscaleAccept;python MakeRmsShape.py -c configuration_Boosted_${proc}_${rg}.py -f hadd.root -n PDF4LHC15_nnlo_30_pdfas;python MakeRmsShape.py -c configuration_Boosted_${proc}_${rg}.py -f hadd.root -n NNPDF31_nnlo_hessian_pdfas) &> RunMakeQCDscale_Rms_Shape_configuration_Boosted_${proc}_${rg}.log&
#	(python MakeEnvelopShape.py -c configuration_Boosted_${proc}_${rg}.py  -f hadd.root -n QCDscaleAccept;python MakeRmsShape.py -c configuration_Boosted_${proc}_${rg}.py -f hadd.root -n pdfAccept;) &> RunMakeQCDscale_Rms_Shape_configuration_Boosted_${proc}_${rg}.log&


	#echo "(python MakeEnvelopShape.py -c configuration_Resolved_${proc}_${rg}.py -f hadd.root -n QCDscaleAccept;python MakeRmsShape.py -c configuration_Resolved_${proc}_${rg}.py -f hadd.root -n PDF4LHC15_nnlo_30_pdfas;python MakeRmsShape.py -c configuration_Resolved_${proc}_${rg}.py -f hadd.root -n NNPDF31_nnlo_hessian_pdfas)" > RunMakeQCDscale_Rms_Shape_configuration_Resolved_${proc}_${rg}.log
	#(python MakeEnvelopShape.py -c configuration_Resolved_${proc}_${rg}.py -f hadd.root -n QCDscaleAccept;python MakeRmsShape.py -c configuration_Resolved_${proc}_${rg}.py -f hadd.root -n PDF4LHC15_nnlo_30_pdfas;python MakeRmsShape.py -c configuration_Resolved_${proc}_${rg}.py -f hadd.root -n NNPDF31_nnlo_hessian_pdfas) &> RunMakeQCDscale_Rms_Shape_configuration_Resolved_${proc}_${rg}.log&
#	echo "(python MakeEnvelopShape.py -c configuration_Resolved_${proc}_${rg}.py  -f hadd.root -n QCDscaleAccept;python MakeRmsShape.py -c configuration_Resolved_${proc}_${rg}.py -f hadd.root -n pdfAccept;" > RunMakeQCDscale_Rms_Shape_configuration_Resolved_${proc}_${rg}.log
#	(python MakeEnvelopShape.py -c configuration_Resolved_${proc}_${rg}.py  -f hadd.root -n QCDscaleAccept;python MakeRmsShape.py -c configuration_Resolved_${proc}_${rg}.py -f hadd.root -n pdfAccept;) &> RunMakeQCDscale_Rms_Shape_configuration_Resolved_${proc}_${rg}.log&
#    done
#done

(python MakeEnvelopShape.py -c configuration_Boosted.py  -f hadd.root -n QCDscaleAccept;python MakeRmsShape.py -c configuration_Boosted.py -f hadd.root -n pdfAccept;) &> RunMakeQCDscale_Rms_Shape_configuration_Boosted.log&
(python MakeEnvelopShape.py -c configuration_Resolved.py  -f hadd.root -n QCDscaleAccept;python MakeRmsShape.py -c configuration_Resolved.py -f hadd.root -n pdfAccept;) &> RunMakeQCDscale_Rms_Shape_configuration_Resolved.log&

EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
