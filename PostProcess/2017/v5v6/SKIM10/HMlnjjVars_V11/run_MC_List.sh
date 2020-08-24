# /xrootd//store/user/jhchoi/Latino/HWWNano/
# Sites_cfg: /xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/
# changed to /xrd/store/user/jhchoi/Latino/HWWNano/
# L1Loose

source TurnOnDryRun.sh



SAMPLES=()
source Add_VHtautauWWJJ.sh
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
#mkPostProc.py -p Fall2017_102X_nAODv5_Full2017v6 -i Prod -s MCl1loose2017v6 -b -T ${SAMPLE_LIST}
mkPostProc.py -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6 -s MCCorr2017v6 -b -T ${SAMPLE_LIST}


##SKIM10
modcfg="--modcfg SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200406_HMSemilepSKIMv6_10/Steps_cfg.py"
mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6 -s HMSemilepSKIMv6_10 -b -T ${SAMPLE_LIST}


##Analyzer
modcfg="--modcfg SNuAnalytics/NanoGardenerModules/HMlnjjVars_Dev_jhchoi/Steps_cfg.py"
mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_nom -T ${SAMPLE_LIST} -b
##JetSys -> HMFull_jhchoi10_jetsysdown_uncorrelate
mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_jetsysdown_uncorrelate -T ${SAMPLE_LIST} -b
mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_jetsysup_uncorrelate -T ${SAMPLE_LIST} -b
mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_jetsysdown_correlate -T ${SAMPLE_LIST} -b
mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_jetsysup_correlate -T ${SAMPLE_LIST} -b
mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_fatjetsys -T ${SAMPLE_LIST} -b

#mkPostProc.py -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6 -s HMSemilepSkimJHv6_7 -T ZZZ


##--Systematics
SYSLIST=()
##--Lepton momentum Scale--##
ANA=HMFull_jhchoi10_nom
SYSLIST+=(${ANA}_ElepTup)
SYSLIST+=(${ANA}_ElepTdo)
SYSLIST+=(${ANA}_MupTup)
SYSLIST+=(${ANA}_MupTdo)
SYSLIST+=(${ANA}_METup)
SYSLIST+=(${ANA}_METdo)

for sys in ${SYSLIST[@]};do
    echo "---$sys---"
    mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s ${sys} -b -T ${SAMPLE_LIST}
    #mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s ${sys} -b -T ZZZ ##To Test
done


##--Test
#mkPostProc.py -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6__MCCorr2017v6 -s ElepTup_suffix -b -T WW-LO
#mkPostProc.py -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6__MCCorr2017v6 -s METup_suffix -b -T WW-LO
#mkPostProc.py -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6__MCCorr2017v6 -s FATJESup_suffix_total -b -T WW-LO
#mkPostProc.py -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6__MCCorr2017v6 -s JESup_suffix_total -b -T WW-LO


SAMPLES=()
EXCLUDE=()





#unset -f condor_submit


