#HMSemilepSKIMv6_8
##DATARUN
#SNuAnalytics/NanoGardenerModules/WhadronTagger
modcfg="--modcfg SNuAnalytics/NanoGardenerModules/W_Taggers/Steps_cfg.py"
#dobatch='-b'
dobatch=''

##For Wtagger Fat
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_9 -s WtaggerProducer -T GluGluHToWWToLNuQQ_M1000 ${dobatch} 
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_9 -s WhadronChain -T GluGluHToWWToLNuQQ_M1000



#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s WhadronChainFullJetSys -T GluGluHToWWToLNuQQ_M1000 -b
#mkPostProc.py ${modcfg} -p Run2018_102X_nAODv6_Full2018v6 -i DATAl1loose2018v6__HMSemilepSKIMv6_10_data -s WhadronChainFullJetSys_data -T SingleMuon_Run2018C-Nano25Oct2019_ver2-v1 -b

#mkPostProc.py ${modcfg} -p Run2018_102X_nAODv6_Full2018v6 -i DATAl1loose2018v6__HMSemilepSKIMv6_10_data -s WhadronChainFullJetSys_data_test -T SingleMuon_Run2018D-Nano25Oct2019_ver2-v1 -b

## Wjj resolved
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_9 -s WjjtaggerProducer -T GluGluHToWWToLNuQQ_M1000 ${dobatch} 
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_9 -s WjjtaggerProducer_nom -T GluGluHToWWToLNuQQ_M1000 ${dobatch} 





#mkPostProc.py ${modcfg} -p Run2018_102X_nAODv6_Full2018v6 -i DATAl1loose2018v6__HMSemilepSKIMv6_10_data -s WtaggerProducer_data -T SingleMuon_Run2018D-Nano25Oct2019_ver2-v1
#mkPostProc.py ${modcfg} -p Run2018_102X_nAODv6_Full2018v6 -i DATAl1loose2018v6__HMSemilepSKIMv6_10_data -s WhadronChain_data -T SingleMuon_Run2018D-Nano25Oct2019_ver2-v1 -b


#WtaggerProducer
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s WtaggerProducer -T GluGluHToWWToLNuQQ_M1000

##wlepmaker
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s WlepMaker_test -T GluGluHToWWToLNuQQ_M1000

#WmakerChain test
mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s WtaggerProducer -T GluGluHToWWToLNuQQ_M1000
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s WmakerChain_nom_test -T GluGluHToWWToLNuQQ_M1000 -b
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s WmakerChain_sys_test -T GluGluHToWWToLNuQQ_M1000 -b
#mkPostProc.py ${modcfg} -p Run2018_102X_nAODv6_Full2018v6 -i DATAl1loose2018v6__HMSemilepSKIMv6_10_data -s WmakerChain_data_test -T SingleMuon_Run2018D-Nano25Oct2019_ver2-v1 -b
