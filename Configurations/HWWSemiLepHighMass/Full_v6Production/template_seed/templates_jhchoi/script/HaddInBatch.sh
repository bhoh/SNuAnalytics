#mydir=`ls -d rootFile*Boosted*`
#python python_tool/latino/SetupHaddInBatch.py -n 30 -a $mydir -t $mydir
#mydir=`ls -d rootFile*Resolved*`
#python python_tool/latino/SetupHaddInBatch.py -n 30 -a $mydir -t $mydir

###Instruction
#Add your rootfiledir into ARR_DIR


ARR_DIR=(
)
ARR_DIR=`ls -d rootFile*/`
##default is dryrun
for d in ${ARR_DIR[@]};do
    python python_tool/latino/SetupHaddInBatch.py -n 5 -a $d -t $d

    
    #continue
    pushd workdirhadd_${d}
    condor_submit runhadd.jds > runhadd.jid
    popd
done


