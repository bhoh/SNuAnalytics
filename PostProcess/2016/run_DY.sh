# /xrootd//store/user/jhchoi/Latino/HWWNano/
# Sites_cfg: /xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/
# changed to /xrd/store/user/jhchoi/Latino/HWWNano/
# L1Loose


SAMPLES=(
DYJetsToLL_M-10to50-LO
DYJetsToLL_M-50-LO_ext1
DYJetsToLL_M-50-LO_ext2
DYJetsToLL_M-10to50
DYJetsToLL_M-10to50_ext1
DYJetsToLL_M-50_ext2
DYJetsToLL_M-50-UEup
DYJetsToLL_M-50-UEdo
DYJetsToLL_M-50-PSup
DYJetsToLL_M-50-PSdo
DYJetsToLL_M-5to50_HT-70to100
DYJetsToLL_M-5to50_HT-100to200
DYJetsToLL_M-5to50_HT-100to200_ext1
DYJetsToLL_M-5to50_HT-200to400
DYJetsToLL_M-5to50_HT-200to400_ext1
DYJetsToLL_M-5to50_HT-400to600
DYJetsToLL_M-5to50_HT-400to600_ext1
DYJetsToLL_M-5to50_HT-600toinf
DYJetsToLL_M-50_HT-70to100
DYJetsToLL_M-50_HT-100to200
DYJetsToLL_M-50_HT-100to200_ext1
DYJetsToLL_M-50_HT-200to400
DYJetsToLL_M-50_HT-200to400_ext1
DYJetsToLL_M-50_HT-400to600
DYJetsToLL_M-50_HT-400to600_ext1
DYJetsToLL_M-50_HT-600to800
DYJetsToLL_M-50_HT-800to1200
DYJetsToLL_M-50_HT-1200to2500
DYJetsToLL_M-50_HT-2500toinf
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
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v5 -i MCl1loose2016v5__MCCorr2016v5 -s Semilep2016 -b -T ${SAMPLE_LIST}
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v5 -i MCl1loose2016v5__MCCorr2016v5__Semilep2016 -s HMlnjjSel2017 -b -T ${SAMPLE_LIST}
mkPostProc.py -p Summer16_102X_nAODv4_Full2016v5 -i MCl1loose2016v5__MCCorr2016v5__Semilep2016 -s HMlnjjSel_New -b -T ${SAMPLE_LIST}



SAMPLES=()
EXCLUDE=()
