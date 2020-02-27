StartTime=$(date +%s)


#mkPlot.py --pycfg=configuration.py --inputFile=rootFile_2017_l1CR/plots.root --plotFile=plot.py --outputDirPlots=plots_2017_l1CR
mkPlot.py --pycfg=configuration.py --inputFile=rootFile_2017_l1CR/plots.root --plotFile=plot_ele.py --outputDirPlots=plots_2017_l1CR_ele
#mkPlot.py --pycfg=configuration.py --inputFile=rootFile_2017_l1CR/plots.root --plotFile=plot_mu.py --outputDirPlots=plots_2017_l1CR_mu



EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
echo -e "JOBDIR:${PWD}
args=$@
runtime=$(($EndTime - $StartTime))
ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch



