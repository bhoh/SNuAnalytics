# /xrootd//store/user/jhchoi/Latino/HWWNano/
# Sites_cfg: /xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/
# changed to /xrd/store/user/jhchoi/Latino/HWWNano/
# L1Loose

SAMPLES=(
CHToCB_M050
CHToCB_M060
CHToCB_M070
CHToCB_M075
CHToCB_M080
CHToCB_M085
CHToCB_M090
CHToCB_M100
CHToCB_M110
CHToCB_M120
CHToCB_M130
CHToCB_M140
CHToCB_M150
)

EXCLUDE=()

#--Run--#
SAMPLE_LIST=''
EXCLUDE_LIST=''
for s in ${SAMPLES[@]};do SAMPLE_LIST=${s}','${SAMPLE_LIST};done
for e in ${EXCLUDE[@]};do EXCLUDE_LIST=${e}','${EXCLUDE_LIST};done
echo ${SAMPLE_LIST}
#echo ${EXCLUDE_LIST}

######################
# Option: -R(redo)
######################

sitescfg='--sitescfg SNuAnalytics/PostProcess/ChargedHiggsToCB/Sites_cfg.py'
modcfg='--modcfg SNuAnalytics/NanoGardenerFrameworks/Steps_cfg.py'
#modcfg='--modcfg SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200406_HMSemilepSKIMv6_10/Steps_cfg.py'
datacfg='--datacfg SNuAnalytics/PostProcess/ChargedHiggsToCB/Productions_cfg.py'

#--l1Prod--#
#mkPostProc.py ${sitescfg} ${modcfg} ${datacfg} -p Fall2017_102X_nAODv5_Full2017v6 -i Prod -s MCl1loose2017v6 -b -T ${SAMPLE_LIST}
mkPostProc.py ${sitescfg} ${modcfg} ${datacfg} -p Fall2017_102X_nAODv5_Full2017v6 -i Prod -s MCl1loose2017v6 -b -T CHToCB_M160
#mkPostProc.py ${sitescfg} ${datacfg} -p Fall2017_102X_nAODv5_Full2017v6 -i Prod -s MCl1loose2017v6 -b -T CHToCB_M140
#--Corr--#
#mkPostProc.py ${sitescfg} ${modcfg} ${datacfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6 -s MCCorr2017v6 -b -T ${SAMPLE_LIST} 
#mkPostProc.py ${sitescfg} ${datacfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6 -s MCCorr2017v6 -b -T CHToCB_M140
#--HM--#
#mkPostProc.py ${sitescfg} ${modcfg} ${datacfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6 -s HMSemilepSKIMv6_10 -b -T ${SAMPLE_LIST}
#mkPostProc.py ${sitescfg} ${modcfg} ${datacfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6 -s HMSemilepSKIMv6_10 -b -T CHToCB_M140


#mkPostProc.py ${sitescfg} ${modcfg} ${datacfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v5__MCCorr2017v5 -s Semilep2017 -b -T ${SAMPLE_LIST}
