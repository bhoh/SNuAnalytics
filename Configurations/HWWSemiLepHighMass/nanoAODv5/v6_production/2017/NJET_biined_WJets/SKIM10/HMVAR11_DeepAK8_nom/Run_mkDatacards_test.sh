StartTime=$(date +%s)

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

ARR_MASS=(1000)





##
##Run_mkDatacards_cuts_Boosted_GGF_SR_mu.log
ListFlavor=(mu ele)
ListRegion=(TOP SB SR)
ListProc=(VBF GGF)
for MX in ${ARR_MASS[@]};do
    for flv in ${ListFlavor[@]};do
	#continue
	for rg in ${ListRegion[@]};do
            for proc in ${ListProc[@]};do
		echo "aaaa"
	    done
	done
    done
done
EndTime=$(date +%s)
echo $EndTime
