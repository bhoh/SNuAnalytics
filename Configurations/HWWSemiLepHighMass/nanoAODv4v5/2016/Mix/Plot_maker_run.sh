StartTime=$(date +%s)

##central
#mkPlot.py --pycfg=configuration.py --inputFile=rootFile_2016/plots_2016.root


#mkPlot.py --pycfg=configuration_limit.py --inputFile=rootFile_2016/plots_2016.root
#mkPlot.py --pycfg=configuration_no170to300.py --inputFile=rootFile_no170to300_2016/plots_no170to300_2016.root
#mkPlot.py --pycfg=configuration_jetonly.py --inputFile=rootFile_2016_jetonly/plots_2016_jetonly.root

#--scaleToPlot=4
#mkPlot.py   --pycfg=configuration.py   --inputFile=rootFile_Boosted2016/plots_Boosted2016.root

#200,210,250,300,350,400,500,600,700,800,900,1500,2000,2500,3000,4000,5000
#ARR_MASS=(200 210 250 300 350 400 500 600 700 800 900 1500 2000 2500 3000 4000 5000)

DefineList=`python MassPoints/List_MX_common.py`
#echo ARR_MASS=$DefineList
ARR_MASS=$DefineList

echo $ARR_MASS
for MASS in ${ARR_MASS[@]};do
    echo "M=${MASS}"
    #mkPlot.py --pycfg=configuration_limit.py --inputFile=rootFile_2016/plots_2016.root --plotFile=MassPoints/plot_M${MASS}.py --outputDirPlots=plot_M${MASS}_2016

    ##--SR
    #mkPlot.py --pycfg=configuration_SR.py --inputFile=rootFile_2016_SR/plots_2016_SR.root --plotFile=MassPoints/plot_M${MASS}_SR.py --outputDirPlots=plots_M${MASS}_2016_SR
    #--simple hadd
    mkPlot.py --pycfg=configuration_SR.py --inputFile=rootFile_2016_SR_backup/plot.root --plotFile=MassPoints/plot_M${MASS}_SR.py --outputDirPlots=plots_M${MASS}_2016_SR
    

done
tar cf plots_2016SR.tar plots*

##--CR
#mkPlot.py --pycfg=configuration_CR.py --inputFile=rootFile_2016_CR/plots_2016_CR.root --plotFile=plot_CR.py --outputDirPlots=plots_2016_CR
EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
echo -e "JOBDIR:${PWD}
args=$@
runtime=$(($EndTime - $StartTime))
ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch
