StartTime=$(date +%s)

python TurnOnCombinedSamples.py nuisances.py CombineMultiV
python TurnOnCombinedSamples.py nuisances.py CombineH125
python TurnOnCombinedSamples.py nuisances.py CombineWjets

python TurnOnCombinedSamples.py plot.py CombineMultiV
python TurnOnCombinedSamples.py plot.py CombineH125
python TurnOnCombinedSamples.py plot.py CombineWjets






#test
#mkPlot.py --pycfg=configuration_Resolved.py --inputFile=${input} --plotFile=plot.py --cutsFile=cuts_Resolved.py --outputDirPlots=plots_2018_Resolved
cp nuisances.py nuisances_Resolved.py

#python SpanPlotCut.py Resolved

#ListFlavor=(mu ele muele)
#ListRegion=(TOP SB SR)
#ListProc=(VBF GGF)
##ListFlavor=(ele)
##ListRegion=(TOP)
##ListProc=(GGF)
#for flv in ${ListFlavor[@]};do
    #continue
#    for rg in ${ListRegion[@]};do
#	for proc in ${ListProc[@]};do
#	    echo "${flv} , ${rg} ,${proc}"
	    #rootFile_2018_Resolved_SKIM10_HMVar10_Fullvar_GGF_SB
	    #configuration_Resolved_GGF_SB.py
	    #            os.system('cp cuts_'+boosted+'.py '+'cuts_'+boosted+'_'+proc+'_'+rg+'_'+flv+'.py')
	    #input=`ls rootFile*Resol*${proc}*${rg}/hadd.root`
#	    input=`ls rootFile*Resol*/hadd.root`
#	    echo ${input}
#	    (mkPlot.py --pycfg=configuration_Resolved_${proc}_${rg}.py --inputFile=${input} --plotFile=plot_Resolved_${flv}_${rg}.py --cutsFile=cuts_Resolved_${proc}_${rg}_${flv}.py --outputDirPlots=plots_2018_Resolved_${proc}_${rg}_${flv} &> Plot_maker_run_Resolved_${proc}_${rg}_${flv}.log;echo "DONE" >> Plot_maker_run_Resolved_${proc}_${rg}_${flv}.log)&
#	done
#    done
#done

#rootFile_2018_Resolved_SKIM7_HMVar5
#mkPlot.py --pycfg=configuration_Resolved.py --inputFile=rootFile_2018_Resolved_SKIM7_HMVar5/hadd.root --plotFile=plot.py --outputDirPlots=plots_2018_Resolved ##CR
#mkPlot.py --pycfg=configuration_Resolved.py --inputFile=rootFile_2018_Resolved_SKIM7_HMVar5/hadd.root --plotFile=plot_blind.py --cutsFile=cuts_Resolved_blind.py --outputDirPlots=plots_2018_Resolved ##SR

#mkPlot.py --pycfg=configuration_Resolved.py --inputFile=rootFile_2018_Resolved_SKIM7_HMVar5/hadd.root --plotFile=plot_ele.py --cutsFile=cuts_Resolved_ele.py --outputDirPlots=plots_2018_Resolved_ele ## CR
#mkPlot.py --pycfg=configuration_Resolved.py --inputFile=rootFile_2018_Resolved_SKIM7_HMVar5/hadd.root --plotFile=plot_ele_blind.py --cutsFile=cuts_Resolved_ele_blind.py --outputDirPlots=plots_2018_Resolved_ele ##SR

#mkPlot.py --pycfg=configuration_Resolved.py --inputFile=rootFile_2018_Resolved_SKIM7_HMVar5/hadd.root --plotFile=plot_mu.py --cutsFile=cuts_Resolved_mu.py --outputDirPlots=plots_2018_Resolved_mu ##CR
#mkPlot.py --pycfg=configuration_Resolved.py --inputFile=rootFile_2018_Resolved_SKIM7_HMVar5/hadd.root --plotFile=plot_mu_blind.py --cutsFile=cuts_Resolved_mu_blind.py --outputDirPlots=plots_2018_Resolved_mu ##SR
#mkPlot.py --pycfg=configuration_Resolved.py --inputFile=rootFile_2018_Resolved_SKIM5/hadd.root --plotFile=plot.py --outputDirPlots=plots_2018_Resolved

##rm
#rm plot_mu.py plot_ele.py cuts_Resolved_mu.py cuts_Resolved_ele.py plot_blind.py plot_mu_blind.py plot_ele_blind.py cuts_Resolved_blind.py cuts_Resolved_mu_blind.py cuts_Resolved_ele_blind.py



input=`ls rootFile*Resol*/hadd.root`
FLV=(ele mu)
for flv in ${FLV[@]};do
    cp plot.py plot_${flv}.py
    cp cuts_Resolved.py cuts_Resolved_${flv}.py 
    (mkPlot.py --pycfg=configuration_Resolved.py --inputFile=${input} --plotFile=plot_${flv}.py --cutsFile=cuts_Resolved_${flv}.py --outputDirPlots=plots_2018_Resolved_${flv} &> Plot_maker_run_Resolved_${flv}.log;echo "DONE" >> Plot_maker_run_Resolved_${flv}.log)&
done
EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
echo -e "JOBDIR:${PWD}
args=$@
runtime=$(($EndTime - $StartTime))
ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch



