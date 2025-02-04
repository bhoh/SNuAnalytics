#mydir=`ls -d rootFile*Boosted*`
#python python_tool/latino/SetupHaddInBatch.py -n 30 -a $mydir -t $mydir
#mydir=`ls -d rootFile*Resolved*`
#python python_tool/latino/SetupHaddInBatch.py -n 30 -a $mydir -t $mydir

###Instruction
#Add your rootfiledir into ARR_DIR


ARR_DIR=(
rootFile_2017_SKIM10_Boosted_HMFull_V11_cprime1.0BRnew0.0_DeepAK8WP2p5_dMchi2Resolution_SB
#rootFile_2017_SKIM10_Boosted_HMFull_V11_cprime1.0BRnew0.0_DeepAK8WP2p5_dMchi2Resolution_SR
#rootFile_2017_SKIM10_Boosted_HMFull_V11_cprime1.0BRnew0.0_DeepAK8WP2p5_dMchi2Resolution_TOP
#rootFile_2017_SKIM10_Resolved_HMFull_V11_cprime1.0BRnew0.0_DeepAK8WP2p5_dMchi2Resolution_SB
#rootFile_2017_SKIM10_Resolved_HMFull_V11_cprime1.0BRnew0.0_DeepAK8WP2p5_dMchi2Resolution_SR
#rootFile_2017_SKIM10_Resolved_HMFull_V11_cprime1.0BRnew0.0_DeepAK8WP2p5_dMchi2Resolution_TOP
)

##default is dryrun
for d in ${ARR_DIR[@]};do
    python python_tool/latino/SetupHaddInBatch.py -n 30 -a $d -t $d

    
    #continue
    pushd workdirhadd_${d}
    condor_submit runhadd.jds > runhadd.jid
    popd
done


