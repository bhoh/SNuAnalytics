# /xrootd//store/user/jhchoi/Latino/HWWNano/
# Sites_cfg: /xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/
# changed to /xrd/store/user/jhchoi/Latino/HWWNano/
# L1Loose

##--DATACorr2016--##
SAMPLES=()
SAMPLES=(\
SingleElectron_Run2016B-Nano14Dec2018_ver2-v1 \
SingleElectron_Run2016C-Nano14Dec2018-v1 \
SingleElectron_Run2016D-Nano14Dec2018-v1 \
SingleElectron_Run2016E-Nano14Dec2018-v1 \
SingleElectron_Run2016F-Nano14Dec2018-v1 \
SingleElectron_Run2016G-Nano14Dec2018-v1 \
SingleElectron_Run2016H-Nano14Dec2018-v1 \
SingleMuon_Run2016B-Nano14Dec2018_ver2-v1 \
SingleMuon_Run2016C-Nano14Dec2018-v1 \
SingleMuon_Run2016D-Nano14Dec2018-v1 \
SingleMuon_Run2016E-Nano14Dec2018-v1 \
SingleMuon_Run2016F-Nano14Dec2018-v1 \
SingleMuon_Run2016G-Nano14Dec2018-v1 \
SingleMuon_Run2016H-Nano14Dec2018-v1 \
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
#mkPostProc.py -p Run2016_102X_nAODv4_Full2016v5 -i Prod -s DATAl1loose2016v5 -b -T ${SAMPLE_LIST}
#--Cor--#

mkPostProc.py -p Run2016_102X_nAODv4_Full2016v5 -i DATAl1loose2016v5 -s Semilep2016 -b -T ${SAMPLE_LIST}
#mkPostProc.py -p Run2016_102X_nAODv4_Full2016v5 -i DATAl1loose2016v5__Semilep2016 -s HMlnjjSel2017 -b -T ${SAMPLE_LIST}
#mkPostProc.py -p Run2016_102X_nAODv4_Full2016v5 -i DATAl1loose2016v5__Semilep2016 -s HMlnjjSel_New -b -T ${SAMPLE_LIST}





SAMPLES=()
EXCLUDE=()
