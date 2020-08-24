# /xrootd//store/user/jhchoi/Latino/HWWNano/
# Sites_cfg: /xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/
# changed to /xrd/store/user/jhchoi/Latino/HWWNano/
# L1Loose

source TurnOnDryRun.sh

SAMPLES=()
source Add_VHtautauWWJJ.sh

#SAMPLES=(WJetsToLNu)

EXCLUDE=()

#--Run--#
SAMPLE_LIST=''
EXCLUDE_LIST=''
for s in ${SAMPLES[@]};do SAMPLE_LIST=${s}','${SAMPLE_LIST};done
for e in ${EXCLUDE[@]};do EXCLUDE_LIST=${e}','${EXCLUDE_LIST};done

#----Central
#mkPostProc.py -p Summer16_102X_nAODv5_Full2016v6 -i Prod -s MCl1loose2016v6 -T ${SAMPLE_LIST} -b
#mkPostProc.py -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6 -s MCCorr2016v6 -T ${SAMPLE_LIST} -b
#mkPostProc.py -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6 -s HMSemilepSkimJHv6_7 -T ${SAMPLE_LIST} -b
#mkPostProc.py -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6__HMSemilepSkimJHv6_7 -s HMlnjjVars_Dev_jhchoi7 -T ${SAMPLE_LIST} -b


#mkPostProc.py -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6__HMSemilepSkimJH2016v6_5 -s HMlnjjVars_Dev_jhchoi -T ${SAMPLE_LIST} -b
#mkPostProc.py -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6__HMSemilepSkimJH2016v6_5 -s HMlnjjVars_Dev_jhchoi2 -T ${SAMPLE_LIST} -b
modcfg="--modcfg SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200406_HMSemilepSKIMv6_10/Steps_cfg.py"
mkPostProc.py ${modcfg} -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6 -s HMSemilepSKIMv6_10 -T ${SAMPLE_LIST} -b
modcfg="--modcfg SNuAnalytics/NanoGardenerModules/HMlnjjVars_Dev_jhchoi/Steps_cfg.py"
mkPostProc.py ${modcfg} -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_nom -T ${SAMPLE_LIST} -b
#mkPostProc.py ${modcfg} -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10 -s BWReweight -T ${SAMPLE_LIST} -b






##jetsys


mkPostProc.py ${modcfg} -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_jetsysdown_uncorrelate -T ${SAMPLE_LIST} -b
mkPostProc.py ${modcfg} -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_jetsysup_uncorrelate -T ${SAMPLE_LIST} -b

mkPostProc.py ${modcfg} -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_jetsysdown_correlate -T ${SAMPLE_LIST} -b
mkPostProc.py ${modcfg} -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_jetsysup_correlate -T ${SAMPLE_LIST} -b

mkPostProc.py ${modcfg} -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_fatjetsys -T ${SAMPLE_LIST} -b




#SAMPLE_LIST=ZZZ
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
    mkPostProc.py ${modcfg} -p Summer16_102X_nAODv5_Full2016v6 -i  MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10 -s ${sys} -b -T ${SAMPLE_LIST}
done




SAMPLES=()
EXCLUDE=()


unset -f condor_submit
