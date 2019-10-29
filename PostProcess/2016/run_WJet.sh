# /xrootd//store/user/jhchoi/Latino/HWWNano/
# Sites_cfg: /xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/
# changed to /xrd/store/user/jhchoi/Latino/HWWNano/
# L1Loose


SAMPLES=(
WJetsToLNu_HT70_100
WJetsToLNu_HT100_200
WJetsToLNu_HT100_200_ext1
WJetsToLNu_HT100_200_ext2
WJetsToLNu_HT200_400
WJetsToLNu_HT200_400_ext1
WJetsToLNu_HT200_400_ext2
WJetsToLNu_HT400_600
WJetsToLNu_HT400_600_ext1
WJetsToLNu_HT600_800
WJetsToLNu_HT600_800_ext1
WJetsToLNu_HT800_1200
WJetsToLNu_HT800_1200_ext1
WJetsToLNu_HT1200_2500
WJetsToLNu_HT1200_2500_ext1
WJetsToLNu_HT2500_inf
WJetsToLNu_HT2500_inf_ext1
WJetsToLNu
WJetsToLNu_ext2
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
