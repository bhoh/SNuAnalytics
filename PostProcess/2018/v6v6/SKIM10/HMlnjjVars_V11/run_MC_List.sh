#source TurnOnDryRun.sh

SAMPLES=()
source Add_VHtautauWWJJ.sh

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
 
mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6 -s HMSemilepSKIMv6_10 -b -T ${SAMPLE_LIST} 

modcfg="--modcfg SNuAnalytics/NanoGardenerModules/HMlnjjVars_Dev_jhchoi/Steps_cfg.py"
mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_nom -b -T ${SAMPLE_LIST}

#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s BWReweight -b -T ${SAMPLE_LIST}



mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_jetsysdown_uncorrelate -b -T ${SAMPLE_LIST}
mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_jetsysup_uncorrelate -b -T ${SAMPLE_LIST}

mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_jetsysdown_correlate -b -T ${SAMPLE_LIST}
mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_jetsysup_correlate -b -T ${SAMPLE_LIST}

mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_fatjetsys -b -T ${SAMPLE_LIST}



#SAMPLE_LIST=ZZZ;echo "!!!!TEST JOB!!!!"

SYSLIST=()
ANA=HMFull_jhchoi10_nom

SYSLIST+=(${ANA}_ElepTup)
SYSLIST+=(${ANA}_ElepTdo)
SYSLIST+=(${ANA}_MupTup)
SYSLIST+=(${ANA}_MupTdo)
SYSLIST+=(${ANA}_METup)
SYSLIST+=(${ANA}_METdo)

for sys in ${SYSLIST[@]};do
    #continue
    echo "---$sys---"
    mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s ${sys} -b -T ${SAMPLE_LIST}
done

unset -f condor_submit
