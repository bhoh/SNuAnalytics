MX=${1}
YEAR=2017
mkdir -p Datacards_${YEAR}
cp nuisances.py nuisances_Boosted.py
cp nuisances.py nuisances_Resolved.py


DefineList=`python MassPoints/List_MX_common.py`
#echo ARR_MASS=$DefineList                                                                                                                     
ARR_MASS=$DefineList



ARR_REGION=(SR SB TOP)
ARR_PROC=(GGF VBF)


inputBoost=`ls rootFile*Boost*/hadd.root`
inputResol=`ls rootFile*Resol*/hadd.root`

#ARR_MASS=(1000)





##

ListFlavor=(mu ele)
ListRegion=(TOP SB SR)
ListProc=(VBF GGF)

for flv in ${ListFlavor[@]};do
    #continue
    for rg in ${ListRegion[@]};do
        for proc in ${ListProc[@]};do
	    echo "${flv} , ${rg} ,${proc}"
	    #rootFile_2017_Boosted_SKIM10_HMVar10_Fullvar_GGF_SB
	    #configuration_Boosted_GGF_SB.py
	    #            os.system('cp cuts_'+boosted+'.py '+'cuts_'+boosted+'_'+proc+'_'+rg+'_'+flv+'.py')
	    input=`ls rootFile*Boost*${proc}*${rg}/hadd.root`
	    echo ${input}
	    mkDatacards.py --pycfg=configuration_Boosted_${proc}_${rg}.py --structureFile=MassPoints/structure_M${MX}_${flv}.py --cutsFile=cuts_Boosted_${proc}_${rg}_${flv}.py --inputFile=$input --outputDirDatacard=Datacards_${YEAR}/Datacard_M${MX} --samplesFile=MassPoints/samples_${YEAR}limit_M${MX}_${flv}.py --variablesFile=variables_Boosted_Final.py
	    
	    input=`ls rootFile*Resol*${proc}*${rg}/hadd.root`
	    echo ${input}
	    mkDatacards.py --pycfg=configuration_Resolved_${proc}_${rg}.py --structureFile=MassPoints/structure_M${MX}_${flv}.py --cutsFile=cuts_Resolved_${proc}_${rg}_${flv}.py --inputFile=$input --outputDirDatacard=Datacards_${YEAR}/Datacard_M${MX} --samplesFile=MassPoints/samples_${YEAR}limit_M${MX}_${flv}.py --variablesFile=variables_Resolved_Final.py
	    
	    
	    
	done
    done
done

