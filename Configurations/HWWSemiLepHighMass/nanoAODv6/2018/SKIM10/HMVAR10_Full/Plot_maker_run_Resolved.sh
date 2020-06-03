StartTime=$(date +%s)







#test
#mkPlot.py --pycfg=configuration_Resolved.py --inputFile=${input} --plotFile=plot.py --cutsFile=cuts_Resolved.py --outputDirPlots=plots_2018_Resolved
cp nuisances.py nuisances_Resolved.py
python SpanPlotCut.py Resolved

#ListFlavor=(mu ele)
#ListRegion=(TOP SB SR)
#ListProc=(VBF GGF)

ListFlavor=(mu)
ListRegion=(SB)
ListProc=(GGF)
for flv in ${ListFlavor[@]};do
    #continue
    for rg in ${ListRegion[@]};do
	for proc in ${ListProc[@]};do
	    echo "${flv} , ${rg} ,${proc}"
	    #rootFile_2018_Resolved_SKIM10_HMVar10_Fullvar_GGF_SB
	    #configuration_Resolved_GGF_SB.py
	    #            os.system('cp cuts_'+boosted+'.py '+'cuts_'+boosted+'_'+proc+'_'+rg+'_'+flv+'.py')
	    input=`ls rootFile*Resol*${proc}*${rg}/hadd.root`
	    echo ${input}
	    (mkPlot.py --pycfg=configuration_Resolved_${proc}_${rg}.py --inputFile=${input} --plotFile=plot_${flv}_${rg}.py --cutsFile=cuts_Resolved_${proc}_${rg}_${flv}.py --outputDirPlots=plots_2018_Resolved_${proc}_${rg}_${flv} &> Plot_maker_run_Resolved_${proc}_${rg}_${flv}.log;echo "DONE" >> Plot_maker_run_Resolved_${proc}_${rg}_${flv}.log)&
	done
    done
done



EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
echo -e "JOBDIR:${PWD}
args=$@
runtime=$(($EndTime - $StartTime))
ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch



