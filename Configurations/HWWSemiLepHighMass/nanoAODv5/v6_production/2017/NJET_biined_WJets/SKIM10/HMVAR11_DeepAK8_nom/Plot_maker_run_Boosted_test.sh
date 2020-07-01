StartTime=$(date +%s)







#test
#mkPlot.py --pycfg=configuration_Boosted.py --inputFile=${input} --plotFile=plot.py --cutsFile=cuts_Boosted.py --outputDirPlots=plots_2017_Boosted
cp nuisances.py nuisances_Boosted.py
python SpanPlotCut.py Boosted

ListFlavor=(ele)
ListRegion=(TOP)
ListProc=(GGF)
for flv in ${ListFlavor[@]};do
    #continue
    for rg in ${ListRegion[@]};do
	for proc in ${ListProc[@]};do
	    echo "${flv} , ${rg} ,${proc}"
	    #rootFile_2017_Boosted_SKIM10_HMVar10_Fullvar_GGF_SB
	    #configuration_Boosted_GGF_SB.py
	    #            os.system('cp cuts_'+boosted+'.py '+'cuts_'+boosted+'_'+proc+'_'+rg+'_'+flv+'.py')
	    #input=`ls rootFile*Boost*${proc}*${rg}/hadd.root`
	    for i in `seq 1 81`;do
		input=`ls rootFile*Boost*${proc}*${rg}/plots_2017_Boosted_SKIM10_HMVar10_Fullvar_GGF_TOP_ALL_top.${i}.root`
		echo ${input}
		#kill %${i}
		(mkPlot.py --pycfg=configuration_Boosted_${proc}_${rg}.py --inputFile=${input} --nuisancesFile=nuisances_test.py --plotFile=plot_test.py --cutsFile=cuts_Boosted_${proc}_${rg}_${flv}.py --outputDirPlots=plots_2017_Boosted_${proc}_${rg}_${flv}_test_${i} --onlyVariable=Event --nuisancesFile=nuisances_Boosted_test.py &> Plot_maker_run_Boosted_${proc}_${rg}_${flv}_test.log;echo "DONE" >> Plot_maker_run_Boosted_${proc}_${rg}_${flv}_test.log)&
	    done
	done
    done
done

#rootFile_2017_Boosted_SKIM7_HMVar5
#mkPlot.py --pycfg=configuration_Boosted.py --inputFile=rootFile_2017_Boosted_SKIM7_HMVar5/hadd.root --plotFile=plot.py --outputDirPlots=plots_2017_Boosted ##CR
#mkPlot.py --pycfg=configuration_Boosted.py --inputFile=rootFile_2017_Boosted_SKIM7_HMVar5/hadd.root --plotFile=plot_blind.py --cutsFile=cuts_Boosted_blind.py --outputDirPlots=plots_2017_Boosted ##SR

#mkPlot.py --pycfg=configuration_Boosted.py --inputFile=rootFile_2017_Boosted_SKIM7_HMVar5/hadd.root --plotFile=plot_ele.py --cutsFile=cuts_Boosted_ele.py --outputDirPlots=plots_2017_Boosted_ele ## CR
#mkPlot.py --pycfg=configuration_Boosted.py --inputFile=rootFile_2017_Boosted_SKIM7_HMVar5/hadd.root --plotFile=plot_ele_blind.py --cutsFile=cuts_Boosted_ele_blind.py --outputDirPlots=plots_2017_Boosted_ele ##SR

#mkPlot.py --pycfg=configuration_Boosted.py --inputFile=rootFile_2017_Boosted_SKIM7_HMVar5/hadd.root --plotFile=plot_mu.py --cutsFile=cuts_Boosted_mu.py --outputDirPlots=plots_2017_Boosted_mu ##CR
#mkPlot.py --pycfg=configuration_Boosted.py --inputFile=rootFile_2017_Boosted_SKIM7_HMVar5/hadd.root --plotFile=plot_mu_blind.py --cutsFile=cuts_Boosted_mu_blind.py --outputDirPlots=plots_2017_Boosted_mu ##SR
#mkPlot.py --pycfg=configuration_Resolved.py --inputFile=rootFile_2017_Resolved_SKIM5/hadd.root --plotFile=plot.py --outputDirPlots=plots_2017_Resolved

##rm
#rm plot_mu.py plot_ele.py cuts_Boosted_mu.py cuts_Boosted_ele.py plot_blind.py plot_mu_blind.py plot_ele_blind.py cuts_Boosted_blind.py cuts_Boosted_mu_blind.py cuts_Boosted_ele_blind.py


EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
echo -e "JOBDIR:${PWD}
args=$@
runtime=$(($EndTime - $StartTime))
ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch



