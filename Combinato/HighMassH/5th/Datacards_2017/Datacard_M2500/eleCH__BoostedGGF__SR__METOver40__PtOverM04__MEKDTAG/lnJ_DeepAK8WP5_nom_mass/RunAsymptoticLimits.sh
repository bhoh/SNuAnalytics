StartTime=$(date +%s)
workspacefile=$1
mass=$2
option="--run blind"
#option="-- bypassFrequentistFit --run blind"
combine -M AsymptoticLimits -d $workspacefile ${option} --trackParameters fvbf -t -1 -m $2 -s 1 &> AsymptoticLimits_$workspacefile.txt&
combine -M AsymptoticLimits -d $workspacefile ${option} --setParameters fvbf=0 --freezeParameters fvbf -t -1 -m $2 -s 2 &> AsymptoticLimits_${workspacefile}_GGFOnly.txt&
combine -M AsymptoticLimits -d $workspacefile ${option} --setParameters fvbf=1 --freezeParameters fvbf -t -1 -m $2 -s 3 &> AsymptoticLimits_${workspacefile}_VBFOnly.txt&
combine -M AsymptoticLimits -d $workspacefile ${option} --setParameters fvbf=0.5 --freezeParameters fvbf -t -1 -m $2 -s 4 &> AsymptoticLimits_${workspacefile}_fvbf0p5.txt&


EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
