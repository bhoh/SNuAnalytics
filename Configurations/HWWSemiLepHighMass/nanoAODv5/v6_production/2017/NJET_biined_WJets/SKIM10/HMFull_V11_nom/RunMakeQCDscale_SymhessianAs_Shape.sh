StartTime=$(date +%s)
python TurnOffCombinedSamples.py WPandCut2017.py CombineMultiV
python TurnOffCombinedSamples.py WPandCut2017.py CombineH125
python TurnOffCombinedSamples.py WPandCut2017.py CombineWjets
python TurnOffCombinedSamples.py WPandCut2017.py Combine_ggWW
python TurnOffCombinedSamples.py WPandCut2017.py Combine_qqWWqq
python TurnOffCombinedSamples.py WPandCut2017.py CombineSBI



##--Boosted
(python MakeEnvelopShape.py -c configuration_Boosted.py  -f hadd.root -n QCDscaleAccept;python MakeSymhessianAsShape.py -c configuration_Boosted.py -f hadd.root -n pdfAccept;) &> logs/RunMakeQCDscale_SymhessianAs_Shape_configuration_Boosted.log&
##--Resolved
(python MakeEnvelopShape.py -c configuration_Resolved.py  -f hadd.root -n QCDscaleAccept;python MakeSymhessianAsShape.py -c configuration_Resolved.py -f hadd.root -n pdfAccept;) &> logs/RunMakeQCDscale_SymhessianAs_Shape_configuration_Resolved.log&
EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
