StartTime=$(date +%s)

# --onlyPlot'       , dest='onlyPlot'       , help='draw only specified plot type (comma-separated c, cratio, and/or cdifference)', default=None

##central
#mkPlot.py --pycfg=configuration.py --inputFile=rootFile_2017/plots_2017.root


#mkPlot.py --pycfg=configuration_limit.py --inputFile=rootFile_2017/plots_2017.root
#mkPlot.py --pycfg=configuration_no170to300.py --inputFile=rootFile_no170to300_2017/plots_no170to300_2017.root
#mkPlot.py --pycfg=configuration_jetonly.py --inputFile=rootFile_2017_jetonly/plots_2017_jetonly.root

#--scaleToPlot=4
#mkPlot.py   --pycfg=configuration.py   --inputFile=rootFile_Boosted2017/plots_Boosted2017.root


#DefineList=`python MassPoints/List_melaKDmass.py`
#echo ARR_MASS=$DefineList                                                                                                                                                        
#ARR_MASS=$DefineList


#for MASS in ${ARR_MASS[@]};do
#    
#    #continue
#    echo "M=${MASS}"
#
#    mkPlot.py --pycfg=configuration.py --inputFile=rootFile_2017_SR/plots_2017_SR.root --plotFile=MassPoints/plot_M${MASS}_SR.py --outputDirPlots=plots_M${MASS}_2017_SR
#    #break
#
#
#done

#mkPlot.py --pycfg=configuration.py --inputFile=rootFile_melaKD_2017/plots_melaKD_2017.root  --outputDirPlots=plots_melaKD_2017_SR  --linearOnly --onlyPlot=c --scaleToPlot=1.7
mkPlot.py --pycfg=configuration.py --inputFile=rootFile_melaKD_2017_Test/plots_melaKD_2017_Test.root  --outputDirPlots=plots_melaKD_2017_SR_Test  --linearOnly --onlyPlot=c --scaleToPlot=1.7

##--CR
#mkPlot.py --pycfg=configuration_CR.py --inputFile=rootFile_2017_CR/plots_2017_CR.root --plotFile=plot_CR.py --outputDirPlots=plots_2017_CR


EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
#echo -e "JOBDIR:${PWD}
#args=$@
#runtime=$(($EndTime - $StartTime))
#ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch
