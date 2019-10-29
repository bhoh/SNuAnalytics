# /xrootd//store/user/jhchoi/Latino/HWWNano/
# Sites_cfg: /xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/
# changed to /xrd/store/user/jhchoi/Latino/HWWNano/
# L1Loose


SAMPLES=(
TTToSemiLeptonic
ST_t-channel_top
ST_t-channel_antitop
ST_tW_antitop
ST_tW_top
ST_s-channel
TTWJetsToLNu
TTWJetsToQQ
TTZjets
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


#--l1Prod--#
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v5 -i Prod -s MCl1loose2016v5 -b -T ${SAMPLE_LIST}
#--Corr--#
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v5 -i MCl1loose2016v5 -s MCCorr2016v5 -b -T ${SAMPLE_LIST} 

#--semilep--#
mkPostProc.py -p Summer16_102X_nAODv4_Full2016v5 -i MCl1loose2016v5__MCCorr2016v5 -s Semilep2016 -b -T ${SAMPLE_LIST}
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v5 -i MCl1loose2016v5__MCCorr2016v5__Semilep2016 -s HMlnjjSel2017 -b -T ${SAMPLE_LIST}
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v5 -i MCl1loose2016v5__MCCorr2016v5__Semilep2016 -s HMlnjjSel_New -b -T ${SAMPLE_LIST}



SAMPLES=()
EXCLUDE=()
