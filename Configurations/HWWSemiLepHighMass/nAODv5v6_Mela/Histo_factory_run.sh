#pushd MassPoints
#python MakeSampleStructurePythons.py
#python MakePlotPythons.py
#popd
StartTime=$(date +%s)

#for histo factory
#mkShapesMulti.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#mkShapesMulti.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --treeName Events
#mkShapesMulti.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --doHadd=True --treeName Events


#test
#mkShapesMulti.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --treeName Events

#mkShapes.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --treeName Events



#for hadd

#mkShapes.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --doHadd=True --treeName Events
#mkShapes.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --doHadd=True --batchSplit=AsMuchAsPossible --treeName Events
#mkShapes.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --doHadd=True --treeName Events


#Jet only

#mkShapes.py --pycfg=configuration_jetonly.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#mkShapes.py --pycfg=configuration_jetonly.py --batchSplit=AsMuchAsPossible --doHadd=True --treeName Events


#no 170to300

#mkShapes.py --pycfg=configuration_no170to300.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#mkShapes.py --pycfg=configuration_no170to300.py --batchSplit=AsMuchAsPossible --doHadd=True --treeName Events


##Limit
#mkShapesMulti.py --pycfg=configuration_limit.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#cp -r rootFile_2017 rootFile_2017_backup
#mkShapesMulti.py --pycfg=configuration_limit.py --batchSplit=AsMuchAsPossible --doHadd=True --treeName Events

##--SR
#mkShapesMulti.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#cp -r rootFile_2017_SR rootFile_2017_SR_backup
#pushd rootFile_2017_SR_backup
#hadd plot.root *.root &> hadd.log&
#popd
mkShapesMulti.py --pycfg=configuration.py --batchSplit=AsMuchAsPossible --doHadd --treeName Events


##--CR
#mkShapesMulti.py --pycfg=configuration_CR.py --batchSplit=AsMuchAsPossible --doBatch --treeName Events
#cp -r rootFile_2017_CR rootFile_2017_CR_backup
#mkShapesMulti.py --pycfg=configuration_CR.py --batchSplit=AsMuchAsPossible --doHadd --treeName Events


EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
#echo -e "JOBDIR:${PWD}
#args=$@
#runtime=$(($EndTime - $StartTime))
#ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch
