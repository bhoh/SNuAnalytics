#RunCheckEntriesInSR_per_process.py
#parser.add_argument("-c", dest='cutname')
#parser.add_argument("-f", dest='histofile')
#parser.add_argument("-v", dest='variablename')
python TurnOffCombinedSamples.py WPandCut2017.py CombineH125
python TurnOffCombinedSamples.py WPandCut2017.py CombineMultiV
python TurnOffCombinedSamples.py WPandCut2017.py Combine_qqWWqq
python TurnOffCombinedSamples.py WPandCut2017.py Combine_ggWW
python TurnOffCombinedSamples.py WPandCut2017.py CombineSBI



##Boosted
echo "------Boosted--------"
#ARR_CUT=(eleCH__BoostedGGF__SR__METOver40__PtOverM04___ muCH__BoostedGGF__SR__METOver40__PtOverM04___)
#cutname=eleCH__BoostedGGF__SR__METOver40__PtOverM04___
#cutname=muCH__BoostedGGF__SR__METOver40__PtOverM04___
cutname=___BoostedGGF__SR__METOver40__PtOverM04___
variablename=Event
minN=5000


DefineList=`python MassPoints/List_MX.py` ## ggfhww mass points 
#echo ARR_MASS=$DefineList                                                                                                                                                                                  
ARR_MASS=$DefineList


#python_tool/ExportShellCondorSetup.py
#   parser.add_option("-c","--command",   dest="command", help="command to run")
#   parser.add_option("-d","--workdir",   dest="workdir", help="workarea")
#   parser.add_option("-n","--jobname",   dest="jobname", help="jobname")
#   parser.add_option("-s","--submit",   dest="submit",action="store_true", help="submit",default=False)

CURDIR=$PWD
for MX in ${ARR_MASS[@]};do
    #continue
    processname=ggHWWlnuqq_M${MX}_B
    #input=`ls rootFile*Boost*/hadd.root`
    directorypath=`ls -d rootFile*Boosted*/`
    #echo ${input}
    #for cutname in ${ARR_CUT[@]};do
    command="cd ${CURDIR};python CheckEntriesInSR_per_process.py -c ${cutname} -v ${variablename} -d ${directorypath} -n ${minN} -p ${processname}"
    python python_tool/ExportShellCondorSetup.py -c "$command" -d "RunCheckEntriesInSR_per_process_Boosted/${processname}" -n "RunCheckEntriesInSR_per_process_Boosted_${processname}" -s    
    #done
    echo "run M${MX}"
done
echo "------END Boosted--------"



echo "-----Resolved----"
#___ResolvedGGF__SR__METOver30__PtOverM035__WlepMtOver50__WWMtOver60__Score0To30___
cutname=___ResolvedGGF__SR__METOver30__PtOverM035__WlepMtOver50__WWMtOver60__Score0To30___
#input=`ls rootFile*Resol*/hadd.root`
#python CheckEntriesInSR.py -c ${cutname} -v ${variablename} -f ${input} -n ${minN}
for MX in ${ARR_MASS[@]};do
    processname=ggHWWlnuqq_M${MX}_B
    #input=`ls rootFile*Boost*/hadd.root`
    directorypath=`ls -d rootFile*Resolved*/`
    #echo ${input}
    #for cutname in ${ARR_CUT[@]};do
    command="cd ${CURDIR};python CheckEntriesInSR_per_process.py -c ${cutname} -v ${variablename} -d ${directorypath} -n ${minN} -p ${processname}"
    python python_tool/ExportShellCondorSetup.py -c "$command" -d "RunCheckEntriesInSR_per_process_Resolved/${processname}" -n "RunCheckEntriesInSR_per_process_Resolved_${processname}" -s
    #done
    echo "run M${MX}"
done


echo "-----END Resolved----"
