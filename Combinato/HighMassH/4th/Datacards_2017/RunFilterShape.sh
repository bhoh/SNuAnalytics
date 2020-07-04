NSPLIT=15
ARR_F=($(ls Datacard_M*/*/*/*/*.root))
for f in ${ARR_F[@]};do
    echo $f
    python FilterShape.py -f $f &
    while [ 1 ];do
        NJOB=`jobs|wc -l`
        if [ $NJOB -lt ${NSPLIT} ];then
            echo "NJOB < ${NSPLIT}"
            break
        fi
        sleep 3
    done
    #break
done
