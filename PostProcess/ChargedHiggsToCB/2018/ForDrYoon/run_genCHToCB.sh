# /xrootd//store/user/jhchoi/Latino/HWWNano/
# Sites_cfg: /xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/
# changed to /xrd/store/user/jhchoi/Latino/HWWNano/
# L1Loose

SAMPLES=(
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
modcfg='--modcfg SNuAnalytics/NanoGardenerFrameworks/Steps_cfg.py'
#modcfg='--modcfg SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200406_HMSemilepSKIMv6_10/Steps_cfg.py'
datacfg='--datacfg SNuAnalytics/PostProcess/ChargedHiggsToCB/Productions_cfg.py'


#for CHToCB samples
#for single signal samples, interactive
mkPostProc.py ${sitescfg} ${modcfg} ${datacfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__genCHToCB_2018 -s GenKinFitTTSemiLep_2018 -T CHToCB_M120 -R

#for single signal samples, batch
#mkPostProc.py ${sitescfg} ${modcfg} ${datacfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__genCHToCB_2018 -s GenKinFitTTSemiLep_2018 -b -T CHToCB_M120

#for single signal samples, batch, make submit script but not submit
#mkPostProc.py ${sitescfg} ${modcfg} ${datacfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__genCHToCB_2018 -s GenKinFitTTSemiLep_2018 -b -T CHToCB_M120 --dry-run

# for all signal samples
# it does not submit existing skim
#mkPostProc.py ${sitescfg} ${modcfg} ${datacfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__genCHToCB_2018 -s GenKinFitTTSemiLep_2018 -b -T ${SAMPLE_LIST}

# for all signal samples
#XXX override existing skim
#mkPostProc.py ${sitescfg} ${modcfg} ${datacfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__genCHToCB_2018 -s GenKinFitTTSemiLep_2018 -b -T ${SAMPLE_LIST} -R

#for SM ttbar
#mkPostProc.py ${sitescfg} ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__genCHToCB_2018 -s GenKinFitTTSemiLep_2018 -b -T TTToSemiLeptonic
