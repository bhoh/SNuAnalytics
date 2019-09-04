# /xrootd//store/user/jhchoi/Latino/HWWNano/
# Sites_cfg: /xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/
# changed to /xrd/store/user/jhchoi/Latino/HWWNano/
# L1Loose

##--DATACorr2017--##
SAMPLES=()
SAMPLES=(\
SingleElectron_Run2017B-Nano14Dec2018-v1 \
SingleElectron_Run2017C-Nano14Dec2018-v1 \
SingleElectron_Run2017D-Nano14Dec2018-v1 \
SingleElectron_Run2017E-Nano14Dec2018-v1 \
SingleElectron_Run2017F-Nano14Dec2018-v1 \
SingleMuon_Run2017B-Nano14Dec2018-v1 \
SingleMuon_Run2017C-Nano14Dec2018-v1 \
SingleMuon_Run2017D-Nano14Dec2018-v1 \
SingleMuon_Run2017E-Nano14Dec2018-v1 \
SingleMuon_Run2017F-Nano14Dec2018-v1 \
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
#mkPostProc.py -p Run2017_102X_nAODv4_Full2017v4 -i Prod -s DATAl1loose2017v2 -b -T ${SAMPLE_LIST}
#--Cor--#
#mkPostProc.py -p Run2017_102X_nAODv4_Full2017v4 -i DATAl1loose2017v2 -s DATACorr2017 -b -T ${SAMPLE_LIST}
mkPostProc.py -p Run2017_102X_nAODv4_Full2017v5 -i DATAl1loose2017v5 -s Semilep2017 -b -T ${SAMPLE_LIST}





SAMPLES=()
EXCLUDE=()
