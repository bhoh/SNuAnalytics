pushd MassPoints
python MakeSampleStructurePythons.py
python MakePlotPythons.py
popd

StartTime=$(date +%s)

##--SR
#mkShapesMulti.py --pycfg=configuration_SR.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
cp -r rootFile_2016_SR rootFile_2016_SR_backup
pushd rootFile_2016_SR_backup
hadd plot.root *.root &> hadd.log&
popd
#mkShapesMulti.py --pycfg=configuration_SR.py --batchSplit=AsMuchAsPossible --doHadd=True --treeName Events


##--CR
#mkShapesMulti.py --pycfg=configuration_CR.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events 
#cp -r rootFile_2016_CR rootFile_2016_CR_backup
#mkShapesMulti.py --pycfg=configuration_CR.py --batchSplit=AsMuchAsPossible --doHadd=True --treeName Events 





EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
echo -e "JOBDIR:${PWD}
args=$@
runtime=$(($EndTime - $StartTime))
ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch
