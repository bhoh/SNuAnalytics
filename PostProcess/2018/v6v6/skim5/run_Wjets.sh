#source TurnOnDryRun.sh

SAMPLES=(
WJetsToLNu_Pt50to100
WJetsToLNu_Pt100to250
WJetsToLNu_Pt250to400
WJetsToLNu_Pt400to600
WJetsToLNu_Pt600toInf
)

#--Run--#

SAMPLE_LIST=''
EXCLUDE_LIST=''
for s in ${SAMPLES[@]};do SAMPLE_LIST=${s}','${SAMPLE_LIST};done
for e in ${EXCLUDE[@]};do EXCLUDE_LIST=${e}','${EXCLUDE_LIST};done


######################
# Option: -R(redo)
######################
#--l1Prod--#
mkPostProc.py -p Autumn18_102X_nAODv6_Full2018v6 -i Prod -s MCl1loose2018v6 -b -T ${SAMPLE_LIST} 
mkPostProc.py -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6 -s MCCorr2018v6 -b -T ${SAMPLE_LIST} 
mkPostProc.py -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6 -s HMSemilepSkimJH2018v6_5 -b -T ${SAMPLE_LIST} 
#mkPostProc.py -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSkimJH2018v6_5 -s HMlnjjVars_Dev_jhchoi -b -T ${SAMPLE_LIST} 
mkPostProc.py -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSkimJH2018v6_5 -s HMlnjjVars_Dev_jhchoi2 -b -T ${SAMPLE_LIST} 


SYSLIST=()
SYSLIST+=(ElepTup_suffix ElepTdo_suffix)
SYSLIST+=(MupTup_suffix MupTdo_suffix)
SYSLIST+=(METup_suffix METdo_suffix)
for sys in ${SYSLIST[@]};do
    continue
    echo "---$sys---"
    mkPostProc.py -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSkimJH2018v6_5 -s ${sys} -b -T ${SAMPLE_LIST}
done

#unset -f condor_submit
