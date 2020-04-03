#HMSemilepSKIMv6_8
##DATARUN
modcfg="--modcfg SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200403_HMSemilepSKIMv6_8/Steps_cfg.py"
#mkPostProc.py ${modcfg} -p Run2017_102X_nAODv5_Full2017v6 -i DATAl1loose2017v6 -s HMSemilepSKIMv6_8_data -b -T SingleElectron_Run2017E-Nano1June2019-v1
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6 -s HMSemilepSKIMv6_8 -b -T GluGluHToWWToLNuQQ_M400

mkPostProc.py ${modcfg} -p Run2018_102X_nAODv6_Full2018v6 -i DATAl1loose2018v6 -s HMSemilepSKIMv6_8_data -b -T SingleMuon_Run2018C-Nano25Oct2019-v1
mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6 -s HMSemilepSKIMv6_8 -b -T GluGluHToWWToLNuQQ_M400

##MCRUN
