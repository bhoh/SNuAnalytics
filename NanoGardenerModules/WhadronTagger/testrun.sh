#HMSemilepSKIMv6_8
##DATARUN
#SNuAnalytics/NanoGardenerModules/WhadronTagger
modcfg="--modcfg SNuAnalytics/NanoGardenerModules/WhadronTagger/Steps_cfg.py"
#dobatch='-b'
#dobatch=''
mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_9 -s WtaggerProducer2018 -T GluGluHToWWToLNuQQ_M400 ${dobatch} 

