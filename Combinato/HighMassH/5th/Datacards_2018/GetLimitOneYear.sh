#eleCH__BoostedGGF__SB__METOver40__PtOverM04__MEKDTAG
#eleCH__BoostedVBF__SB__METOver40__PtOverM04
NCORE=15
mkdir -p Limits/
option="--run blind"
YEAR=2018
#ARR_MASS=(1000)
ARR_MASS=(115 120 125 126 130 140 145 150 155 160 165 170 180 200 210 230 250 270 300 350 400 450 500 550 600 650 700 750 800 900 1000 1500 2000 2500 3000 4000 5000)

for MX in ${ARR_MASS[@]};do
    echo "MX="${MX}
    #combine_M180_2017
    #text2workspace.py combine_M${MX}_${YEAR}.txt -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalar:XWW${MX} -o M${MX}.root &> logs/make_workspace_M${MX}.log
    text2workspace.py combine_M${MX}_${YEAR}.txt -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalar:XWW${MX} -o NoI_M${MX}.root --PO KillInterference &> logs/make_workspace_M${MX}_NoI.log
    #workspacefile=M${MX}.root
    #combine -M AsymptoticLimits -d $workspacefile ${option} --trackParameters fvbf -t -1 -m ${MX} -s 1 &> Limits/AsymptoticLimits_$workspacefile.txt&
    #combine -M AsymptoticLimits -d $workspacefile ${option} --setParameters fvbf=0 --freezeParameters fvbf -t -1 -m ${MX} -s 2 &> Limits/AsymptoticLimits_${workspacefile}_GGFOnly.txt&
    #combine -M AsymptoticLimits -d $workspacefile ${option} --setParameters fvbf=1 --freezeParameters fvbf -t -1 -m ${MX} -s 3 &> Limits/AsymptoticLimits_${workspacefile}_VBFOnly.txt&
    #combine -M AsymptoticLimits -d $workspacefile ${option} --setParameters fvbf=0.5 --freezeParameters fvbf -t -1 -m ${MX} -s 4 &> Limits/AsymptoticLimits_${workspacefile}_fvbf0p5.txt&
    
    workspacefile=NoI_M${MX}.root
    combine -M AsymptoticLimits -d $workspacefile ${option} --trackParameters fvbf -t -1 -m ${MX} -s 5 &> Limits/AsymptoticLimits_$workspacefile.txt&
    combine -M AsymptoticLimits -d $workspacefile ${option} --setParameters fvbf=0 --freezeParameters fvbf -t -1 -m ${MX} -s 6 &> Limits/AsymptoticLimits_${workspacefile}_GGFOnly.txt&
    combine -M AsymptoticLimits -d $workspacefile ${option} --setParameters fvbf=1 --freezeParameters fvbf -t -1 -m ${MX} -s 7 &> Limits/AsymptoticLimits_${workspacefile}_VBFOnly.txt&
    combine -M AsymptoticLimits -d $workspacefile ${option} --setParameters fvbf=0.5 --freezeParameters fvbf -t -1 -m ${MX} -s 8 &> Limits/AsymptoticLimits_${workspacefile}_fvbf0p5.txt&


    while [ 1 ];do
        NJOB=`jobs|wc -l`
        echo "NJOB=$NJOB"
        if [ ${NJOB} -lt ${NCORE} ];then
            echo "NJOB < ${NCORE}"
            break
        fi
        sleep 3
    done
    
done


