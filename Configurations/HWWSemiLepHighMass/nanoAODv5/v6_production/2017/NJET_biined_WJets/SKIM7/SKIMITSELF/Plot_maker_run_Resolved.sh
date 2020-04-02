StartTime=$(date +%s)
cp plot.py plot_mu.py
cp plot.py plot_ele.py
cp cuts_Resolved.py cuts_Resolved_mu.py
cp cuts_Resolved.py cuts_Resolved_ele.py


#mkPlot.py --pycfg=configuration_Resolved.py --inputFile=rootFile_2017_Resolved_SKIM5/hadd.root --plotFile=plot.py --outputDirPlots=plots_2017_Resolved
mkPlot.py --pycfg=configuration_Resolved.py --inputFile=rootFile_2017_Resolved_SKIM5/hadd.root --plotFile=plot_ele.py --cutsFile=cuts_Resolved_ele.py --outputDirPlots=plots_2017_Resolved_ele
mkPlot.py --pycfg=configuration_Resolved.py --inputFile=rootFile_2017_Resolved_SKIM5/hadd.root --plotFile=plot_mu.py --cutsFile=cuts_Resolved_mu.py --outputDirPlots=plots_2017_Resolved_mu
#mkPlot.py --pycfg=configuration_Resolved.py --inputFile=rootFile_2017_Resolved_SKIM5/hadd.root --plotFile=plot.py --outputDirPlots=plots_2017_Resolved




EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
echo -e "JOBDIR:${PWD}
args=$@
runtime=$(($EndTime - $StartTime))
ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch



