StartTime=$(date +%s)

mkPlot.py --pycfg=configuration.py --inputFile=rootFile_2017_Resolved/plots_2017.root --plotFile=plot_ele.py --outputDirPlots=plots_2017_Resolved_ele




EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
echo -e "JOBDIR:${PWD}
args=$@
runtime=$(($EndTime - $StartTime))
ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch



