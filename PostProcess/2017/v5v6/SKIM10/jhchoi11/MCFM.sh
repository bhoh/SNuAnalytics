#GluGluToWWToENMN
#GluGluToWWToENMN
SAMPLE_LIST=GluGluToWWToENMN,GluGluToWWToENEN
modcfg="--modcfg SNuAnalytics/NanoGardenerModules/HMlnjjVars_Dev_jhchoi/Steps_cfg.py"
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i Prod -s HMLHEAna -T ${SAMPLE_LIST} -b
mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i Prod -s HMLHEAna -T GluGluToWWToENMN -b
