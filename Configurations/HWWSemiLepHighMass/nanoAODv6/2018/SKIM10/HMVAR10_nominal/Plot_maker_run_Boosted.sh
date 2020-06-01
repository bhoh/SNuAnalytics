StartTime=$(date +%s)





input="rootFile_2018_Boosted_SKIM10_HMVar10/hadd.root"

#test
#mkPlot.py --pycfg=configuration_Boosted.py --inputFile=${input} --plotFile=plot.py --cutsFile=cuts_Boosted.py --outputDirPlots=plots_2018_Boosted

python SpanPlotCut.py Boosted

ListFlavor=(mu ele)
ListRegion=(CR SR)
for flv in ${ListFlavor[@]};do
    #continue
    for rg in ${ListRegion[@]};do
	echo "${flv} , ${rg}"
	echo "mkPlot.py --pycfg=configuration_Boosted.py --inputFile=${input} --plotFile=plot_${flv}_${rg}.py --cutsFile=cuts_Boosted_${flv}_${rg}.py --outputDirPlots=plots_2018_Boosted_${flv}_${rg}"
	(mkPlot.py --pycfg=configuration_Boosted.py --inputFile=${input} --plotFile=plot_${flv}_${rg}.py --cutsFile=cuts_Boosted_${flv}_${rg}.py --outputDirPlots=plots_2018_Boosted_${flv}_${rg} &> Plot_maker_run_Boosted_${flv}_${rg}.log;echo "DONE" >> Plot_maker_run_Boosted_${flv}_${rg}.log)&
    done
done



EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
echo -e "JOBDIR:${PWD}
args=$@
runtime=$(($EndTime - $StartTime))
ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch



