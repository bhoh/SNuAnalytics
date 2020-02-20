StartTime=$(date +%s)
##central##
#mkPlot.py --pycfg=configuration.py --inputFile=rootFile_2018/plots_2018.root

#--scaleToPlot=4
#mkPlot.py   --pycfg=configuration_jetonly.py   --inputFile=rootFile_2018_jetonly/plots_2018_jetonly.root




#return

DefineList=`python MassPoints/List_MX_common.py`
ARR_MASS=$DefineList

##--For each mass signal--##
for MASS in ${ARR_MASS[@]};do
    echo "M=${MASS}"
    #mkPlot.py --pycfg=configuration_limit.py --inputFile=rootFile_2018/plots_2018.root --plotFile=MassPoints/plot_M${MASS}.py --outputDirPlots=plot_M${MASS}_2018

    ##--SR
    #mkPlot.py --pycfg=configuration_SR.py --inputFile=rootFile_2018_SR/plots_2018_SR.root --plotFile=MassPoints/plot_M${MASS}_SR.py --outputDirPlots=plots_M${MASS}_2018_SR
    mkPlot.py --pycfg=configuration_SR.py --inputFile=rootFile_2018_SR_backup/plot.root --plotFile=MassPoints/plot_M${MASS}_SR.py --outputDirPlots=plots_M${MASS}_2018_SR

    #break

done
tar cf plots_2018SR.tar plots*




##--CR
mkPlot.py --pycfg=configuration_CR.py --inputFile=rootFile_2018_CR/plots_2018_CR.root --plotFile=plot_CR.py --outputDirPlots=plot_2018_CR
EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
echo -e "JOBDIR:${PWD}
args=$@
runtime=$(($EndTime - $StartTime))
ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch
