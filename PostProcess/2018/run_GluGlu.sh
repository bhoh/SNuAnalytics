SAMPLES=(
GluGluHToWWToLNuQQ_M115
GluGluHToWWToLNuQQ_M120
GluGluHToWWToLNuQQ_M125
GluGluHToWWToLNuQQ_M130
GluGluHToWWToLNuQQ_M140
GluGluHToWWToLNuQQ_M145
GluGluHToWWToLNuQQ_M160
GluGluHToWWToLNuQQ_M170
GluGluHToWWToLNuQQ_M180
GluGluHToWWToLNuQQ_M200
GluGluHToWWToLNuQQ_M210
GluGluHToWWToLNuQQ_M250
GluGluHToWWToLNuQQ_M270
GluGluHToWWToLNuQQ_M300
GluGluHToWWToLNuQQ_M350
GluGluHToWWToLNuQQ_M400
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
#mkPostProc.py -p Autumn18_102X_nAODv5_Full2018v5 -i MCl1loose2018v5__MCCorr2018v5 -s Semilep2018 -b -T ${SAMPLE_LIST}
#mkPostProc.py -p Autumn18_102X_nAODv5_Full2018v5 -i MCl1loose2018v5__MCCorr2018v5__Semilep2018 -s HMlnjjSel2017 -b -T ${SAMPLE_LIST}
mkPostProc.py -p Autumn18_102X_nAODv5_Full2018v5 -i MCl1loose2018v5__MCCorr2018v5__Semilep2018 -s HMlnjjSel_New -b -T ${SAMPLE_LIST}
