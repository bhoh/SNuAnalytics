YEAR=2016
mkdir -p Datacards_${YEAR}


DefineList=`python MassPoints/List_MX_common.py`
#echo ARR_MASS=$DefineList
ARR_MASS=$DefineList


#ARR_MX=(200)
for MX in ${ARR_MASS[@]};do
    echo $MX
    #mkDatacards.py --pycfg=configuration_limit.py --structureFile=MassPoints/structure_M${MX}.py --inputFile=rootFile_${YEAR}/plots_${YEAR}.root --outputDirDatacard=Datacards_${YEAR}/Datacard_M${MX} --samplesFile=MassPoints/samples_${YEAR}limit_M${MX}.py

    #rootFile_2016_SR/plots_2016_SR.root
    #MassPoints/samples_2016limit_M1500
    mkDatacards.py --pycfg=configuration_SR.py --structureFile=MassPoints/structure_M${MX}.py --inputFile=rootFile_${YEAR}_SR_backup/plot.root --outputDirDatacard=Datacards_${YEAR}/Datacard_M${MX} --samplesFile=MassPoints/samples_${YEAR}limit_M${MX}.py

done

