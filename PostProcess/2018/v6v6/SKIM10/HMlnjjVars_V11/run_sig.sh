source TurnOnDryRun.sh

SAMPLES=(
GluGluHToWWToLNuQQ_M115
GluGluHToWWToLNuQQ_M120
GluGluHToWWToLNuQQ_M124
GluGluHToWWToLNuQQ_M125
GluGluHToWWToLNuQQ_M126
GluGluHToWWToLNuQQ_M130
GluGluHToWWToLNuQQ_M135
GluGluHToWWToLNuQQ_M140
GluGluHToWWToLNuQQ_M145
GluGluHToWWToLNuQQ_M150
GluGluHToWWToLNuQQ_M155
GluGluHToWWToLNuQQ_M160
GluGluHToWWToLNuQQ_M165
GluGluHToWWToLNuQQ_M170
GluGluHToWWToLNuQQ_M175
GluGluHToWWToLNuQQ_M180
GluGluHToWWToLNuQQ_M190
GluGluHToWWToLNuQQ_M200
GluGluHToWWToLNuQQ_M210
GluGluHToWWToLNuQQ_M230
GluGluHToWWToLNuQQ_M250
GluGluHToWWToLNuQQ_M270
GluGluHToWWToLNuQQ_M300
GluGluHToWWToLNuQQ_M350
GluGluHToWWToLNuQQ_M400
GluGluHToWWToLNuQQ_M450
GluGluHToWWToLNuQQ_M500
GluGluHToWWToLNuQQ_M550
GluGluHToWWToLNuQQ_M600
GluGluHToWWToLNuQQ_M650
GluGluHToWWToLNuQQ_M700
GluGluHToWWToLNuQQ_M750
GluGluHToWWToLNuQQ_M800
GluGluHToWWToLNuQQ_M900
GluGluHToWWToLNuQQ_M1000
GluGluHToWWToLNuQQ_M1500
GluGluHToWWToLNuQQ_M2000
GluGluHToWWToLNuQQ_M2500
GluGluHToWWToLNuQQ_M3000
GluGluHToWWToLNuQQ_M4000
GluGluHToWWToLNuQQ_M5000
VBFHToWWToLNuQQ_M115
VBFHToWWToLNuQQ_M120
VBFHToWWToLNuQQ_M124
VBFHToWWToLNuQQ_M125
VBFHToWWToLNuQQ_M126
VBFHToWWToLNuQQ_M130
VBFHToWWToLNuQQ_M135
VBFHToWWToLNuQQ_M140
VBFHToWWToLNuQQ_M145
VBFHToWWToLNuQQ_M150
VBFHToWWToLNuQQ_M155
VBFHToWWToLNuQQ_M160
VBFHToWWToLNuQQ_M165
VBFHToWWToLNuQQ_M170
VBFHToWWToLNuQQ_M175
VBFHToWWToLNuQQ_M180
VBFHToWWToLNuQQ_M190
VBFHToWWToLNuQQ_M200
VBFHToWWToLNuQQ_M210
VBFHToWWToLNuQQ_M230
VBFHToWWToLNuQQ_M250
VBFHToWWToLNuQQ_M270
VBFHToWWToLNuQQ_M300
VBFHToWWToLNuQQ_M350
VBFHToWWToLNuQQ_M400
VBFHToWWToLNuQQ_M450
VBFHToWWToLNuQQ_M500
VBFHToWWToLNuQQ_M550
VBFHToWWToLNuQQ_M600
VBFHToWWToLNuQQ_M650
VBFHToWWToLNuQQ_M700
VBFHToWWToLNuQQ_M750
VBFHToWWToLNuQQ_M800
VBFHToWWToLNuQQ_M900
VBFHToWWToLNuQQ_M1000
VBFHToWWToLNuQQ_M1500
VBFHToWWToLNuQQ_M2000
VBFHToWWToLNuQQ_M2500
VBFHToWWToLNuQQ_M3000
VBFHToWWToLNuQQ_M4000
VBFHToWWToLNuQQ_M5000
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
#mkPostProc.py -p Autumn18_102X_nAODv6_Full2018v6 -i Prod -s MCl1loose2018v6 -b -T ${SAMPLE_LIST} 
#mkPostProc.py -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6 -s MCCorr2018v6 -b -T ${SAMPLE_LIST} 
#mkPostProc.py -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6 -s HMSemilepSkimJHv6_HMvar7 -b -T ${SAMPLE_LIST}
modcfg="--modcfg SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200406_HMSemilepSKIMv6_10/Steps_cfg.py"
 
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6 -s HMSemilepSKIMv6_10 -b -T ${SAMPLE_LIST} 

modcfg="--modcfg SNuAnalytics/NanoGardenerModules/HMlnjjVars_Dev_jhchoi/Steps_cfg_HMlnjjVars_V11.py"
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_V11_nom -b -T ${SAMPLE_LIST}

#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s BWReweight -b -T ${SAMPLE_LIST}
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__HMFull_V11_nom -s BWReweight -b -T ${SAMPLE_LIST}
mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__BWReweight -s HMFull_V11_nom -b -T ${SAMPLE_LIST}



#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_V11_jetsysdown_uncorrelate -b -T ${SAMPLE_LIST}
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_V11_jetsysup_uncorrelate -b -T ${SAMPLE_LIST}

#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_V11_jetsysdown_correlate -b -T ${SAMPLE_LIST}
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_V11_jetsysup_correlate -b -T ${SAMPLE_LIST}

#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_V11_fatjetsys -b -T ${SAMPLE_LIST}

#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__BWReweight -s HMFull_V11_jetsysdown_uncorrelate -b -T ${SAMPLE_LIST}
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__BWReweight -s HMFull_V11_jetsysup_uncorrelate -b -T ${SAMPLE_LIST}

#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__BWReweight -s HMFull_V11_jetsysdown_correlate -b -T ${SAMPLE_LIST}
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__BWReweight -s HMFull_V11_jetsysup_correlate -b -T ${SAMPLE_LIST}

#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__BWReweight -s HMFull_V11_fatjetsys -b -T ${SAMPLE_LIST}



#SAMPLE_LIST=ZZZ;echo "!!!!TEST JOB!!!!"

SYSLIST=()
ANA=HMFull_V11_nom

SYSLIST+=(${ANA}_ElepTup)
SYSLIST+=(${ANA}_ElepTdo)
SYSLIST+=(${ANA}_MupTup)
SYSLIST+=(${ANA}_MupTdo)
SYSLIST+=(${ANA}_METup)
SYSLIST+=(${ANA}_METdo)

for sys in ${SYSLIST[@]};do
    continue
    echo "---$sys---"
    #mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s ${sys} -b -T ${SAMPLE_LIST}
    mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__BWReweight -s ${sys} -b -T ${SAMPLE_LIST}
done

unset -f condor_submit
