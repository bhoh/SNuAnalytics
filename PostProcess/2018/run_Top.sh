SAMPLES=(
ST_t-channel_top
ST_t-channel_antitop
ST_tW_top_ext1
ST_tW_antitop_ext1
ST_s-channel_ext1
TTToSemiLeptonic
TTZjets
TTWjets
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
#mkPostProc.py -p Autumn18_102X_nAODv5_Full2018v5 -i Prod -s MCl1loose2018v5 -b -T ${SAMPLE_LIST} 
#--Corr--#
#mkPostProc.py -p Autumn18_102X_nAODv5_Full2018v5 -i MCl1loose2018v5 -s MCCorr2018v5 -b -T ${SAMPLE_LIST}
#--Semilep--#
mkPostProc.py -p Autumn18_102X_nAODv5_Full2018v5 -i MCl1loose2018v5__MCCorr2018v5 -s Semilep2018 -b -T ${SAMPLE_LIST}
#mkPostProc.py -p Autumn18_102X_nAODv5_Full2018v5 -i MCl1loose2018v5__MCCorr2018v5__Semilep2018 -s HMlnjjSel2017 -b -T ${SAMPLE_LIST}
#mkPostProc.py -p Autumn18_102X_nAODv5_Full2018v5 -i MCl1loose2018v5__MCCorr2018v5__Semilep2018 -s HMlnjjSel_New -b -T ${SAMPLE_LIST}
