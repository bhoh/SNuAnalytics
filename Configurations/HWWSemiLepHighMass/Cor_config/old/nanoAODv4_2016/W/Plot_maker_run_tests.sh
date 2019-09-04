TAGS=()
TAGS+=(no_SFweight)

TAGS+=(only_puWeight)
TAGS+=(only_TriggerEffWeight_1l)
TAGS+=(only_Lepton_RecoSF)
TAGS+=(only_EMTFbug_veto)


TAGS+=(no_puWeight)
TAGS+=(no_TriggerEffWeight_1l)
TAGS+=(no_Lepton_RecoSF)
TAGS+=(no_EMTFbug_veto)





for tag in ${TAGS[@]};do

    mkPlot.py   --pycfg=configuration_${tag}.py   --inputFile=rootFile_${tag}/plots_${tag}.root    
    

done


