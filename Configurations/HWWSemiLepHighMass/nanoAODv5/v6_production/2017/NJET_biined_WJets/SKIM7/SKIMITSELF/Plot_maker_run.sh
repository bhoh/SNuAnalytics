StartTime=$(date +%s)
cp plot.py plot_mu.py
cp plot.py plot_ele.py
cp cuts.py cuts_mu.py
cp cuts.py cuts_ele.py

#rootFile_2017_SKIM7_ITSELF
mkPlot.py --pycfg=configuration.py --inputFile=rootFile_2017_SKIM7_ITSELF/hadd.root --plotFile=plot.py --outputDirPlots=plots_2017
mkPlot.py --pycfg=configuration.py --inputFile=rootFile_2017_SKIM7_ITSELF/hadd.root --plotFile=plot_ele.py --cutsFile=cuts_ele.py --outputDirPlots=plots_ele
mkPlot.py --pycfg=configuration.py --inputFile=rootFile_2017_SKIM7_ITSELF/hadd.root --plotFile=plot_mu.py --cutsFile=cuts_mu.py --outputDirPlots=plots_mu
#mkPlot.py --pycfg=configuration_Resolved.py --inputFile=rootFile_2017_Resolved_SKIM5/hadd.root --plotFile=plot.py --outputDirPlots=plots_2017_Resolved




EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
echo -e "JOBDIR:${PWD}
args=$@
runtime=$(($EndTime - $StartTime))
ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch



