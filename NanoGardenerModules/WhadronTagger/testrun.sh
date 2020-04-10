#HMSemilepSKIMv6_8
##DATARUN
#SNuAnalytics/NanoGardenerModules/WhadronTagger
modcfg="--modcfg SNuAnalytics/NanoGardenerModules/WhadronTagger/Steps_cfg.py"
#dobatch='-b'
dobatch=''

##For Wtagger Fat
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_9 -s WtaggerProducer -T GluGluHToWWToLNuQQ_M1000 ${dobatch} 
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_9 -s WhadronChain -T GluGluHToWWToLNuQQ_M1000
mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s WhadronChainFullJetSys -T GluGluHToWWToLNuQQ_M1000 -b

## Wjj resolved
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_9 -s WjjtaggerProducer -T GluGluHToWWToLNuQQ_M1000 ${dobatch} 
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_9 -s WjjtaggerProducer_nom -T GluGluHToWWToLNuQQ_M1000 ${dobatch} 



