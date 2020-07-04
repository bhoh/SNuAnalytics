#source RunAsymptotic.sh <worspace> -m <mass>
StartTime=$(date +%s)
workspacefile=$1
mass=$2
combine -M AsymptoticLimits $workspacefile -t -1 -m $2 &> AsymptoticLimits_$workspacefile.txt&
EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
