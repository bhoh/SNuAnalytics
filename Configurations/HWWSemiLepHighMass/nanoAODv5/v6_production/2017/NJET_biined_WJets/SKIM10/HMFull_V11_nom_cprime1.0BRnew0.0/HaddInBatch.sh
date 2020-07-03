mydir=`ls -d rootFile*Boosted*`
python python_tool/latino/SetupHaddInBatch.py -n 30 -a $mydir -t $mydir
mydir=`ls -d rootFile*Resolved*`
python python_tool/latino/SetupHaddInBatch.py -n 30 -a $mydir -t $mydir

