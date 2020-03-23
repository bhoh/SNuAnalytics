# /xrootd//store/user/jhchoi/Latino/HWWNano/
# Sites_cfg: /xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/
# changed to /xrd/store/user/jhchoi/Latino/HWWNano/
# L1Loose

SAMPLES=(
CHToCB_M120
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
modcfg='--modcfg SNuAnalytics/NanoGardenerFrameworks/Steps_cfg.py'
datacfg='--datacfg SNuAnalytics/PostProcess/ChargedHiggsToCB/Productions_cfg.py'

#--l1Prod--#
#mkPostProc.py ${sitescfg} ${modcfg} ${datacfg} -p Autumn18_102X_nAODv6_Full2018v6 -i Prod -s MCl1loose2018v6 -b -T ${SAMPLE_LIST}
#--Corr--#
mkPostProc.py ${sitescfg} ${modcfg} ${datacfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6 -s BinByBinFatJetMCJER -b -T ${SAMPLE_LIST} -R
#mkPostProc.py ${sitescfg} ${modcfg} ${datacfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6 -s CorrJetMC -b -T ${SAMPLE_LIST}
#mkPostProc.py ${sitescfg} ${modcfg} ${datacfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__CorrJetMC -s BinByBinJetMCJER -b -T ${SAMPLE_LIST} -R


#mkPostProc.py ${sitescfg} ${modcfg} ${datacfg} -p Autumn18_102X_nAODv5_Full2018v5 -i MCl1loose2018v5__MCCorr2018v5 -s Semilep2018 -b -T ${SAMPLE_LIST}
