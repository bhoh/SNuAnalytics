StartTime=$(date +%s)
python TurnOffCombinedSamples.py WPandCut2017.py CombineMultiV
python TurnOffCombinedSamples.py WPandCut2017.py CombineH125
python TurnOffCombinedSamples.py WPandCut2017.py CombineWjets
python TurnOffCombinedSamples.py WPandCut2017.py Combine_ggWW
python TurnOffCombinedSamples.py WPandCut2017.py Combine_qqWWqq
python TurnOffCombinedSamples.py WPandCut2017.py CombineSBI


_MYDIR=${PWD}



##This Script will make batch jobs to make PDF/QCDscale Acc up/down shapes for each shape file

_configuration=configuration_Boosted_TOP.py
python MakeEnvelopShape.py -c ${_configuration} -n QCDscaleAccept;python MakeSymhessianAsShape.py -c ${_configuration} -n pdfAccept





#command="cd ${_MYDIR};python MakeEnvelopShape.py -c ${_configuration} -n QCDscaleAccept;python MakeSymhessianAsShape.py -c ${_configuration} -n pdfAccept"
#python python_tool/ExportShellCondorSetup.py -c "${command}" -d workdir/workdir_${_configuration}_QCDScale_PDFAccept -n "QCD_PDF_ACC_${_configuration}" -m 1


##--Boosted
#(python MakeEnvelopShape.py -c configuration_Boosted.py -n QCDscaleAccept;python MakeSymhessianAsShape.py -c configuration_Boosted.py -n pdfAccept;) &> logs/RunMakeQCDscale_SymhessianAs_Shape_configuration_Boosted.log&
##--Resolved
#(python MakeEnvelopShape.py -c configuration_Resolved.py -n QCDscaleAccept;python MakeSymhessianAsShape.py -c configuration_Resolved.py -n pdfAccept;) &> logs/RunMakeQCDscale_SymhessianAs_Shape_configuration_Resolved.log&
EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
