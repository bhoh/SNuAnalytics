SAMPLES=()
SAMPLES=(
EGamma_Run2018A-Nano25Oct2019-v1
EGamma_Run2018B-Nano25Oct2019-v1
EGamma_Run2018C-Nano25Oct2019-v1
EGamma_Run2018D-Nano25Oct2019_ver2-v1
SingleMuon_Run2018A-Nano25Oct2019-v1
SingleMuon_Run2018B-Nano25Oct2019-v1
SingleMuon_Run2018C-Nano25Oct2019-v1
SingleMuon_Run2018D-Nano25Oct2019_ver2-v1
)
EXCLUDE=()

#--Run--#
SAMPLE_LIST=''
EXCLUDE_LIST=''
for s in ${SAMPLES[@]};do SAMPLE_LIST=${s}','${SAMPLE_LIST};done
for e in ${EXCLUDE[@]};do EXCLUDE_LIST=${e}','${EXCLUDE_LIST};done
#echo ${SAMPLE_LIST}
#echo ${EXCLUDE_LIST}

#mkPostProc.py -p Run2018_102X_nAODv6_Full2018v6 -i DATAl1loose2018v6__HMSemilepSkimJH2018v6_5_data -s HMlnjjVars_Dev_jhchoi -b -T ${SAMPLE_LIST}
#mkPostProc.py -p Run2018_102X_nAODv6_Full2018v6 -i DATAl1loose2018v6__HMSemilepSkimJH2018v6_5_data -s HMlnjjVars_Dev_jhchoi2 -b -T ${SAMPLE_LIST}
mkPostProc.py -p Run2018_102X_nAODv6_Full2018v6 -i DATAl1loose2018v6__HMSemilepSkimJH2018v6_5_data -s HEMweightData -b -T ${SAMPLE_LIST}
#mkPostProc.py -p Run2018_102X_nAODv6_Full2018v6 -i Prod -s DATAl1loose2018v6 -b -T ${SAMPLE_LIST}
#mkPostProc.py -p Run2018_102X_nAODv6_Full2018v6 -i DATAl1loose2018v6 -s HMSemilepSkimJH2018v6_5_data -b -T ${SAMPLE_LIST}







SAMPLES=()
EXCLUDE=()
