# /xrootd//store/user/jhchoi/Latino/HWWNano/
# Sites_cfg: /xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/
# changed to /xrd/store/user/jhchoi/Latino/HWWNano/
# L1Loose


SAMPLES=(
DYJetsToLL_M-5to50-LO
DYJetsToLL_M-10to50-LO
DYJetsToLL_M-10to50-LO_ext1
DYJetsToLL_M-50-LO
DYJetsToLL_M-50-LO_ext1
DYJetsToLL_M-50
DYJetsToLL_M-4to50_HT-100to200
DYJetsToLL_M-4to50_HT-100to200_ext1
DYJetsToLL_M-4to50_HT-200to400
DYJetsToLL_M-4to50_HT-200to400_ext1
DYJetsToLL_M-4to50_HT-400to600
DYJetsToLL_M-4to50_HT-400to600_ext1
DYJetsToLL_M-4to50_HT-600toInf
DYJetsToLL_M-4to50_HT-600toInf_ext1
DYJetsToLL_M-50_HT-100to200
DYJetsToLL_M-50_HT-200to400
DYJetsToLL_M-50_HT-200to400_ext1
DYJetsToLL_M-50_HT-400to600_ext1
DYJetsToLL_M-50_HT-600to800
DYJetsToLL_M-50_HT-800to1200
DYJetsToLL_M-50_HT-1200to2500
DYJetsToLL_M-50_HT-2500toInf
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
#mkPostProc.py -p Fall2017_102X_nAODv4_Full2017v4 -i Prod -s MCl1loose2017v2 -b -T ${SAMPLE_LIST}
#mkPostProc.py -p Fall2017_102X_nAODv4_Full2017v4 -i Prod -s MCl1loose2017v2 -b
#--Corr--#
#mkPostProc.py -p Fall2017_102X_nAODv4_Full2017v4 -i MCl1loose2017v2 -s MCCorr2017_SemiLep -b -T ${SAMPLE_LIST} -E ${EXCLUDE_LIST}
#mkPostProc.py -p Fall2017_102X_nAODv4_Full2017v5 -i MCl1loose2017v5 -s MCCorr2017v5 -b -T ${SAMPLE_LIST}

#--semilep--#
#mkPostProc.py -p Fall2017_102X_nAODv4_Full2017v5 -i MCl1loose2017v5__MCCorr2017v5 -s Semilep2017 -b -T ${SAMPLE_LIST}

#mkPostProc.py -p Fall2017_102X_nAODv4_Full2017v5 -i MCl1loose2017v5__MCCorr2017v5__Semilep2017 -s HMlnjjSel2017 -T ${SAMPLE_LIST} -b
#mkPostProc.py -p Fall2017_102X_nAODv4_Full2017v5 -i MCl1loose2017v5__MCCorr2017v5__Semilep2017 -s HMlnjjSel2017 -T ${SAMPLE_LIST} -b
mkPostProc.py -p Fall2017_102X_nAODv4_Full2017v5 -i MCl1loose2017v5__MCCorr2017v5__Semilep2017 -s HMlnjjSel_New -T ${SAMPLE_LIST} -b




SAMPLES=()
EXCLUDE=()
