StartTime=$(date +%s)

ARR_DIR=($(ls -d rootFile_2016_*/))

for dir in ${ARR_DIR[@]};do
    echo "--"
    echo ${dir}
    pushd ${dir}
    myhadd &> hadd.log&
    popd
done
EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
echo -e "JOBDIR:${PWD}
args=$@
runtime=$(($EndTime - $StartTime))
ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch
