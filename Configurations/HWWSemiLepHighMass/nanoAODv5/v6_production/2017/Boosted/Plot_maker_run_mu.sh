StartTime=$(date +%s)


mkPlot.py --pycfg=configuration.py --inputFile=rootFile_2017_Boosted/hadd.root --plotFile=plot_mu.py --outputDirPlots=plots_2017_Boosted_mu



EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
echo -e "JOBDIR:${PWD}
args=$@
runtime=$(($EndTime - $StartTime))
ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch



