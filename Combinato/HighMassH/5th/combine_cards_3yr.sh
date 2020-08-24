#eleCH__BoostedGGF__SB__METOver40__PtOverM04__MEKDTAG
#eleCH__BoostedVBF__SB__METOver40__PtOverM04



ARR_YEAR=(2016 2017 2018)
#ARR_MASS=(1000)
ARR_MASS=(115 120 125 126 130 140 145 150 155 160 165 170 180 200 210 230 250 270 300 350 400 450 500 550 600 650 700 750 800 900 1000 1500 2000 2500 3000 4000 5000)
ARR_FLAVOR=(ele mu)
ARR_BOOST=(Boosted Resolved)
ARR_PROC=(GGF VBF)
#ARR_REGION=(TOP SB SR)
ARR_REGION=(SR)
#FINALVAR_B=lnJ_HP45_nom_mass
FINALVAR_B=lnJ_DeepAK8WP5_nom_mass
FINALVAR_R=lnjj_dMchi2Resolution_nom_mass

for MX in ${ARR_MASS[@]};do
    echo "Datacard_M${MX}"
    
    ARGUMENT=""
    for flv in ${ARR_FLAVOR[@]};do
	for boost in ${ARR_BOOST[@]};do
	    for proc in ${ARR_PROC[@]};do
		for rg in ${ARR_REGION[@]};do
		    echo "-"
		    cutname=""
		    FINALVAR=""
		    if [ $boost = Boosted ];then
			cutname="METOver40__PtOverM04"
			FINALVAR=${FINALVAR_B}
		    elif [ $boost = Resolved ];then
			cutname="METOver30__PtOverM035__WlepMtOver50__WWMtOver60__Score0To30"
			FINALVAR=${FINALVAR_R}
		    fi
		    if [ $rg != "SR" ];then
			FINALVAR="Event"
		    fi
		    for YEAR in ${ARR_YEAR[@]};do
			if [ $proc = GGF ];then
			    #ele_Boosted_GGF_SB_2017
			    ARGUMENT="${ARGUMENT} ${flv}_${boost}_${proc}0_${rg}_${YEAR}=Datacards_${YEAR}/Datacard_M${MX}/${flv}CH__${boost}${proc}__${rg}__${cutname}__MEKDTAG/${FINALVAR}/datacard.txt"
			    ARGUMENT="${ARGUMENT} ${flv}_${boost}_${proc}1_${rg}_${YEAR}=Datacards_${YEAR}/Datacard_M${MX}/${flv}CH__${boost}${proc}__${rg}__${cutname}__UNTAGGED/${FINALVAR}/datacard.txt"
			else
			    ARGUMENT="${ARGUMENT} ${flv}_${boost}_${proc}_${rg}_${YEAR}=Datacards_${YEAR}/Datacard_M${MX}/${flv}CH__${boost}${proc}__${rg}__${cutname}/${FINALVAR}/datacard.txt"
			fi
		    done
		done
	    done
	done
    done
    echo ${ARGUMENT}
    combineCards.py -S ${ARGUMENT} > combine_M${MX}_3yrs.txt
    
done


