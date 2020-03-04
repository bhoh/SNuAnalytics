YEAR=2017
mkdir -p Datacards_${YEAR}


DefineList=`python MassPoints/List_MX_common.py`
#echo ARR_MASS=$DefineList                                                                                                                     
ARR_MASS=$DefineList


for MX in ${ARR_MASS[@]};do
    #continue
    #mkDatacards.py --pycfg=configuration_limit.py --structureFile=MassPoints/structure_M${MX}.py --inputFile=rootFile_${YEAR}/plots_${YEAR}.root --outputDirDatacard=Datacards_${YEAR}/Datacard_M${MX} --samplesFile=MassPoints/samples_${YEAR}limit_M${MX}.py
    mkDatacards.py --pycfg=configuration_SR.py --structureFile=MassPoints/structure_M${MX}.py --inputFile=rootFile_${YEAR}_SR_backup/plot.root --outputDirDatacard=Datacards_${YEAR}/Datacard_M${MX} --samplesFile=MassPoints/samples_${YEAR}limit_M${MX}.py
done

#mkDatacards.py --pycfg=configuration_SR.py --structureFile=structure.py --inputFile=rootFile_${YEAR}_SR/plots_${YEAR}_SR.root --outputDirDatacard=Datacards_${YEAR}
