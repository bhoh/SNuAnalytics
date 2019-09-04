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

    pushd plots_${tag}/
    getidx
    popd
    tar -cf plots_${tag}.tar plots_${tag}/
    
    
done


scp plots*.tar ${USER}@lxplus.cern.ch:/eos/user/j/jhchoi/www/HWW/
