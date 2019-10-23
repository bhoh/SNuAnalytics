# /xrootd//store/user/jhchoi/Latino/HWWNano/
# Sites_cfg: /xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/
# changed to /xrd/store/user/jhchoi/Latino/HWWNano/
# L1Loose

##--DATACorr2017--##
SAMPLES=()
SAMPLES=(\
SingleMuon_Run2018A-Nano1June2019-v1 \
SingleMuon_Run2018B-Nano1June2019-v1 \
SingleMuon_Run2018C-Nano1June2019-v1 \
SingleMuon_Run2018D-Nano1June2019_ver2-v1 \
EGamma_Run2018A-Nano1June2019-v1 \
EGamma_Run2018B-Nano1June2019-v1 \
EGamma_Run2018C-Nano1June2019-v1 \
EGamma_Run2018D-Nano1June2019_ver2-v1 \
)
EXCLUDE=()

#--Run--#
SAMPLE_LIST=''
EXCLUDE_LIST=''
for s in ${SAMPLES[@]};do SAMPLE_LIST=${s}','${SAMPLE_LIST};done
for e in ${EXCLUDE[@]};do EXCLUDE_LIST=${e}','${EXCLUDE_LIST};done
#echo ${SAMPLE_LIST}
#echo ${EXCLUDE_LIST}

#--l1Prod--#

#--Cor--#
#mkPostProc.py -p Run2018_102X_nAODv5_Full2018v5 -i DATAl1loose2018v5 -s Semilep2018 -b -T ${SAMPLE_LIST}

##--HMlnjjSel2017--##
#mkPostProc.py -p Run2018_102X_nAODv5_Full2018v5 -i DATAl1loose2018v5__Semilep2018 -s HMlnjjSel2017 -b -T ${SAMPLE_LIST}
mkPostProc.py -p Run2018_102X_nAODv5_Full2018v5 -i DATAl1loose2018v5__Semilep2018 -s HMlnjjSel_New -b -T ${SAMPLE_LIST}


SAMPLES=()
EXCLUDE=()
