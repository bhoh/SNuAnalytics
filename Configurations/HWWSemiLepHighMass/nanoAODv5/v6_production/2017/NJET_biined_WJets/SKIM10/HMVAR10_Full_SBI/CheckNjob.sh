

NJOB=`jobs|wc -l`
if [ $NJOB -lt 10 ];then
    echo "NJOB < 10"
fi
