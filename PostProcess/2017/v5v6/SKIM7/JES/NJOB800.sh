NJOB=`python GetNJOB.py`

echo ${NJOB}

if [ $NJOB -lt 800 ];then
    echo "NJOB<800"
else
    echo "NJOB>800"
fi
