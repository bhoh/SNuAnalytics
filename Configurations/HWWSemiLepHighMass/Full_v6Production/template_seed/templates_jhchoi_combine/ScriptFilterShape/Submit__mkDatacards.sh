CURDIR=$PWD
StartTime=$(date +%s)

#python TurnOnCombinedSamples.py WPandCut2016.py CombineMultiV
#python TurnOnCombinedSamples.py WPandCut2016.py CombineH125
#python TurnOnCombinedSamples.py WPandCut2016.py CombineWjets
#python TurnOnCombinedSamples.py WPandCut2016.py Combine_ggWW
#python TurnOnCombinedSamples.py WPandCut2016.py Combine_qqWWqq
#python TurnOnCombinedSamples.py WPandCut2016.py CombineSBI

#pushd MassPoints
pushd StructureFiles
python MakeSampleStructurePythons.py
popd
YEAR=2016
NSPLIT=15
mkdir -p Datacards_${YEAR}
#cp nuisances.py nuisances_Boosted.py
#cp nuisances.py nuisances_Resolved.py


DefineList=`python MassPoints/List_MX_common.py`
#echo ARR_MASS=$DefineList                                                                                                                     
ARR_MASS=$DefineList


#ARR_MASS=(900)



#inputBoost=`ls rootFile*Boost*/hadd.root`
#inputResol=`ls rootFile*Resol*/hadd.root`

#ARR_MASS=(1000)
TOTAL_MX=""
for MX in ${ARR_MASS[@]};do
    TOTAL_MX="$TOTAL_MX,${MX}"
done




ListFlavor=(mu ele)

ListRegion=(SR TOP SB)

ListBoost=(Boosted Resolved)
    
for flv in ${ListFlavor[@]};do

    for rg in ${ListRegion[@]};do

	for MX in ${ARR_MASS[@]};do
	    for bst in ${ListBoost[@]};do


		input=`ls rootFile*${bst}*${rg}*/hadd.root`
		#samples_limit_M270_ele.py
		command="cd ${CURDIR};mkDatacards.py --pycfg=configuration_${bst}_${rg}.py --structureFile=StructureFiles/structure_M${MX}_${flv}.py --cutsFile=cuts_${bst}_${rg}_${flv}.py --inputFile=$input --outputDirDatacard=Datacards_${YEAR}/Datacard_M${MX} --samplesFile=StructureFiles/samples_limit_M${MX}_${flv}.py --variablesFile=variables_${bst}_${rg}.py"
		python python_tool/ExportShellCondorSetup.py -c "$command" -d "WORKDIR__Run_mkDatacards/${bst}_M${MX}_${flv}_${rg}/" -n "Run_mkDatacards_M${MX}_${flv}_${rg}_${bst}" -s
	    
	    done

	done

	
    done
done

EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"


