SAMPLES=(
DYJetsToLL_M-4to50_HT-200to400
DYJetsToLL_M-4to50_HT-400to600
DYJetsToLL_M-4to50_HT-600toInf
#DYJetsToLL_M-10to50-LO_ext1
DYJetsToLL_M-10to50-LO
DYJetsToLL_M-50-LO
DYJetsToLL_M-50_HT-70to100
DYJetsToLL_M-50_HT-100to200
DYJetsToLL_M-50_HT-200to400
DYJetsToLL_M-50_HT-400to600
DYJetsToLL_M-50_HT-600to800
DYJetsToLL_M-50_HT-800to1200
DYJetsToLL_M-50_HT-1200to2500
DYJetsToLL_M-50_HT-2500toInf
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
