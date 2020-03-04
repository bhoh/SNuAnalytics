StartTime=$(date +%s)


mkPlot.py --pycfg=configuration.py --inputFile=rootFile_2017_Boosted/hadd.root --plotFile=plot.py --outputDirPlots=plots_2017_Boosted




EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
echo -e "JOBDIR:${PWD}
args=$@
runtime=$(($EndTime - $StartTime))
ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch



