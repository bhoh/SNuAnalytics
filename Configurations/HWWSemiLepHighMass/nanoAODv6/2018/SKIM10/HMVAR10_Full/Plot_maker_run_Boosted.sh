StartTime=$(date +%s)







#test
#mkPlot.py --pycfg=configuration_Boosted.py --inputFile=${input} --plotFile=plot.py --cutsFile=cuts_Boosted.py --outputDirPlots=plots_2018_Boosted
cp nuisances.py nuisances_Boosted.py
python SpanPlotCut.py Boosted

ListFlavor=(mu ele)
ListRegion=(TOP SB SR)
ListProc=(VBF GGF)
#ListFlavor=(ele)
#ListRegion=(TOP)
#ListProc=(GGF)
for flv in ${ListFlavor[@]};do
    #continue
    for rg in ${ListRegion[@]};do
	for proc in ${ListProc[@]};do
	    echo "${flv} , ${rg} ,${proc}"
	    #rootFile_2018_Boosted_SKIM10_HMVar10_Fullvar_GGF_SB
	    #configuration_Boosted_GGF_SB.py
	    #            os.system('cp cuts_'+boosted+'.py '+'cuts_'+boosted+'_'+proc+'_'+rg+'_'+flv+'.py')
	    input=`ls rootFile*Boost*${proc}*${rg}/hadd.root`
	    echo ${input}
	    (mkPlot.py --pycfg=configuration_Boosted_${proc}_${rg}.py --inputFile=${input} --plotFile=plot_${flv}_${rg}.py --cutsFile=cuts_Boosted_${proc}_${rg}_${flv}.py --outputDirPlots=plots_2018_Boosted_${proc}_${rg}_${flv} &> Plot_maker_run_Boosted_${proc}_${rg}_${flv}.log;echo "DONE" >> Plot_maker_run_Boosted_${proc}_${rg}_${flv}.log)&
	done
    done
done

#rootFile_2018_Boosted_SKIM7_HMVar5
#mkPlot.py --pycfg=configuration_Boosted.py --inputFile=rootFile_2018_Boosted_SKIM7_HMVar5/hadd.root --plotFile=plot.py --outputDirPlots=plots_2018_Boosted ##CR
#mkPlot.py --pycfg=configuration_Boosted.py --inputFile=rootFile_2018_Boosted_SKIM7_HMVar5/hadd.root --plotFile=plot_blind.py --cutsFile=cuts_Boosted_blind.py --outputDirPlots=plots_2018_Boosted ##SR

#mkPlot.py --pycfg=configuration_Boosted.py --inputFile=rootFile_2018_Boosted_SKIM7_HMVar5/hadd.root --plotFile=plot_ele.py --cutsFile=cuts_Boosted_ele.py --outputDirPlots=plots_2018_Boosted_ele ## CR
#mkPlot.py --pycfg=configuration_Boosted.py --inputFile=rootFile_2018_Boosted_SKIM7_HMVar5/hadd.root --plotFile=plot_ele_blind.py --cutsFile=cuts_Boosted_ele_blind.py --outputDirPlots=plots_2018_Boosted_ele ##SR

#mkPlot.py --pycfg=configuration_Boosted.py --inputFile=rootFile_2018_Boosted_SKIM7_HMVar5/hadd.root --plotFile=plot_mu.py --cutsFile=cuts_Boosted_mu.py --outputDirPlots=plots_2018_Boosted_mu ##CR
#mkPlot.py --pycfg=configuration_Boosted.py --inputFile=rootFile_2018_Boosted_SKIM7_HMVar5/hadd.root --plotFile=plot_mu_blind.py --cutsFile=cuts_Boosted_mu_blind.py --outputDirPlots=plots_2018_Boosted_mu ##SR
#mkPlot.py --pycfg=configuration_Resolved.py --inputFile=rootFile_2018_Resolved_SKIM5/hadd.root --plotFile=plot.py --outputDirPlots=plots_2018_Resolved

##rm
#rm plot_mu.py plot_ele.py cuts_Boosted_mu.py cuts_Boosted_ele.py plot_blind.py plot_mu_blind.py plot_ele_blind.py cuts_Boosted_blind.py cuts_Boosted_mu_blind.py cuts_Boosted_ele_blind.py


EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
echo -e "JOBDIR:${PWD}
args=$@
runtime=$(($EndTime - $StartTime))
ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch



