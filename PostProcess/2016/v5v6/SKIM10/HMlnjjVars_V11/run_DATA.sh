source TurnOnDryRun.sh
SAMPLES=()
SAMPLES=(\
SingleElectron_Run2016B-Nano1June2019_ver2-v1
SingleElectron_Run2016C-Nano1June2019-v1
SingleElectron_Run2016D-Nano1June2019-v1
SingleElectron_Run2016E-Nano1June2019-v1
SingleElectron_Run2016F-Nano1June2019-v1
SingleElectron_Run2016G-Nano1June2019-v1
SingleElectron_Run2016H-Nano1June2019-v1
SingleMuon_Run2016B-Nano1June2019_ver2-v1
SingleMuon_Run2016C-Nano1June2019-v1
SingleMuon_Run2016D-Nano1June2019-v1
SingleMuon_Run2016E-Nano1June2019-v1
SingleMuon_Run2016F-Nano1June2019-v1
SingleMuon_Run2016G-Nano1June2019-v1
SingleMuon_Run2016H-Nano1June2019-v1
)
EXCLUDE=()

#--Run--#
SAMPLE_LIST=''
EXCLUDE_LIST=''
for s in ${SAMPLES[@]};do SAMPLE_LIST=${s}','${SAMPLE_LIST};done
for e in ${EXCLUDE[@]};do EXCLUDE_LIST=${e}','${EXCLUDE_LIST};done
#echo ${SAMPLE_LIST}
#echo ${EXCLUDE_LIST}

#mkPostProc.py -p Run2016_102X_nAODv5_Full2016v6 -i DATAl1loose2016v6 -s HMSemilepSkimJHv6_7_data -b -T SingleMuon_Run2016E-Nano1June2019-v1


#mkPostProc.py -p Run2016_102X_nAODv5_Full2016v6 -i Prod -s DATAl1loose2016v6 -b -T ${SAMPLE_LIST}
#mkPostProc.py -p Run2016_102X_nAODv5_Full2016v6 -i DATAl1loose2016v6 -s HMSemilepSkimJHv6_7_data -b -T ${SAMPLE_LIST}


modcfg="--modcfg SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200406_HMSemilepSKIMv6_10/Steps_cfg.py"
#mkPostProc.py ${modcfg} -p Run2016_102X_nAODv5_Full2016v6 -i DATAl1loose2016v6 -b -s HMSemilepSKIMv6_10_data -T ${SAMPLE_LIST}
modcfg="--modcfg SNuAnalytics/NanoGardenerModules/HMlnjjVars_Dev_jhchoi/Steps_cfg_HMlnjjVars_V11.py"
mkPostProc.py ${modcfg} -p Run2016_102X_nAODv5_Full2016v6 -i DATAl1loose2016v6__HMSemilepSKIMv6_10_data -s HMFull_V11_data -T ${SAMPLE_LIST} -b





SAMPLES=()
EXCLUDE=()
unset -f condor_submit
