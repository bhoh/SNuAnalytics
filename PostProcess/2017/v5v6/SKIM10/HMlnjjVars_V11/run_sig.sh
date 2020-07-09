# /xrootd//store/user/jhchoi/Latino/HWWNano/
# Sites_cfg: /xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/
# changed to /xrd/store/user/jhchoi/Latino/HWWNano/
# L1Loose

source TurnOnDryRun.sh



SAMPLES=(
GluGluHToWWToLNuQQ_M115
GluGluHToWWToLNuQQ_M120
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
VBFHToWWToLNuQQ_M140
VBFHToWWToLNuQQ_M145
VBFHToWWToLNuQQ_M150
VBFHToWWToLNuQQ_M155
VBFHToWWToLNuQQ_M160
VBFHToWWToLNuQQ_M165
VBFHToWWToLNuQQ_M170
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

EXCLUDE=()

#--Run--#
SAMPLE_LIST=''
EXCLUDE_LIST=''
for s in ${SAMPLES[@]};do SAMPLE_LIST=${s}','${SAMPLE_LIST};done
for e in ${EXCLUDE[@]};do EXCLUDE_LIST=${e}','${EXCLUDE_LIST};done
#echo ${SAMPLE_LIST}
#echo ${EXCLUDE_LIST}

######################
# Option: -R(redo)
######################

#modcfg='--modcfg SNuAnalytics/NanoGardenerFrameworks/Steps_cfg.py'

#--l1Prod--#
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i Prod -s MCl1loose2017v6 -b -T ${SAMPLE_LIST}
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6 -s MCCorr2017v6 -b -T ${SAMPLE_LIST}


##SKIM10
modcfg="--modcfg SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200406_HMSemilepSKIMv6_10/Steps_cfg.py"
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6 -s HMSemilepSKIMv6_10 -b -T ${SAMPLE_LIST}


##Analyzer
modcfg="--modcfg SNuAnalytics/NanoGardenerModules/HMlnjjVars_Dev_jhchoi/Steps_cfg_HMlnjjVars_V11.py"
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s HMFull_V11_nom -T ${SAMPLE_LIST} -b

##Test BWReweighter


#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__BWReweight -s HMFull_V11_nom -T ${SAMPLE_LIST} -b


mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__BWReweight -s HMFull_V11_nom -T ${SAMPLE_LIST} -b

#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__BWReweight -s HMFull_V11_nom -T GluGluHToWWToLNuQQ_M900 ##test

#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11_nom -s BWReweight -T ${SAMPLE_LIST} -b


#test
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__BWReweight__HMFull_V11_nom -s HMLHEAna -T GluGluHToWWToLNuQQ_M250
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__BWReweight__HMFull_V11_nom -s HMLHEAna -T ${SAMPLE_LIST} -b




##JetSys -> HMFull_V11_jetsysdown_uncorrelate
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s HMFull_V11_jetsysdown_uncorrelate -T ${SAMPLE_LIST} -b
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s HMFull_V11_jetsysup_uncorrelate -T ${SAMPLE_LIST} -b
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s HMFull_V11_jetsysdown_correlate -T ${SAMPLE_LIST} -b
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s HMFull_V11_jetsysup_correlate -T ${SAMPLE_LIST} -b
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s HMFull_V11_fatjetsys -T ${SAMPLE_LIST} -b


##--after BWR
mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__BWReweight -s HMFull_V11_jetsysdown_uncorrelate -T ${SAMPLE_LIST} -b
mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__BWReweight -s HMFull_V11_jetsysup_uncorrelate -T ${SAMPLE_LIST} -b
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__BWReweight -s HMFull_V11_jetsysdown_correlate -T ${SAMPLE_LIST} -b
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__BWReweight -s HMFull_V11_jetsysup_correlate -T ${SAMPLE_LIST} -b
mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__BWReweight -s HMFull_V11_fatjetsys -T ${SAMPLE_LIST} -b


##--Test--
#mkPostProc.py -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6 -s HMSemilepSkimJHv6_7 -T ZZZ


##--Systematics
SYSLIST=()
##--Lepton momentum Scale--##
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
    #mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s ${sys} -b -T ${SAMPLE_LIST}
    mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__BWReweight -s ${sys} -b -T ${SAMPLE_LIST}
    #mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s ${sys} -b -T ZZZ ##To Test
done


##--Test
#mkPostProc.py -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6__MCCorr2017v6 -s ElepTup_suffix -b -T WW-LO
#mkPostProc.py -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6__MCCorr2017v6 -s METup_suffix -b -T WW-LO
#mkPostProc.py -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6__MCCorr2017v6 -s FATJESup_suffix_total -b -T WW-LO
#mkPostProc.py -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6__MCCorr2017v6 -s JESup_suffix_total -b -T WW-LO


SAMPLES=()
EXCLUDE=()





unset -f condor_submit


