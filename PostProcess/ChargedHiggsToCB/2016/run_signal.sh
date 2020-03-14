# /xrootd//store/user/jhchoi/Latino/HWWNano/
# Sites_cfg: /xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/
# changed to /xrd/store/user/jhchoi/Latino/HWWNano/
# L1Loose

#CHToCB_M050 is under production
SAMPLES=(
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
#echo ${SAMPLE_LIST}
#echo ${EXCLUDE_LIST}

######################
# Option: -R(redo)
######################

sitescfg='--sitescfg SNuAnalytics/PostProcess/ChargedHiggsToCB/Sites_cfg.py'
modcfg='--modcfg SNuAnalytics/PostProcess/ChargedHiggsToCB/Steps_cfg.py'
datacfg='--datacfg SNuAnalytics/PostProcess/ChargedHiggsToCB/Productions_cfg.py'

#--l1Prod--#
mkPostProc.py ${sitescfg} ${modcfg} ${datacfg} -p Summer16_102X_nAODv5_Full2016v6 -i Prod -s MCl1loose2016v6 -b -T ${SAMPLE_LIST}
#--Corr--#
#mkPostProc.py ${sitescfg} ${modcfg} ${datacfg} -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v5 -s MCCorr2016v5 -b -T ${SAMPLE_LIST} 


#mkPostProc.py ${sitescfg} ${modcfg} ${datacfg} -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v5__MCCorr2016v5 -s Semilep2016 -b -T ${SAMPLE_LIST}
