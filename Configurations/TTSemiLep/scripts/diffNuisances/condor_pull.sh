#!/bin/sh
ulimit -s unlimited
set -e
cd /cms/ldap_home/bhoh/HiggsCombTool/CMSSW_10_6_4/src
export SCRAM_ARCH=slc7_amd64_gcc820
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
mkdir -p /cms_scratch/bhoh/toys
cd /cms_scratch/bhoh/toys

WORK_SPACE_DIR_75=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_DNN_mass/M075Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_80=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_DNN_mass/M080Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_85=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_DNN_mass/M085Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_90=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_DNN_mass/M090Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_100=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_DNN_mass/M100Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_110=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_DNN_mass/M110Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_120=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_DNN_mass/M120Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_130=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_DNN_mass/M130Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_140=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_DNN_mass/M140Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_150=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_DNN_mass/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_160=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_DNN_mass/M160Y2016noHIPMY2017Y2016HIPMY2018.txt.root


#--robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 
if [ $1 -eq 0 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_75 -m 75 -n pull_75 --setParameters BR=0 -t -1 --robustHesse 1 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1
fi
if [ $1 -eq 1 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_80 -m 80 -n pull_80 --setParameters BR=0 -t -1 --robustHesse 1 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1
fi
if [ $1 -eq 2 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_85 -m 85 -n pull_85 --setParameters BR=0 -t -1 --robustHesse 1 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1
fi
if [ $1 -eq 3 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_90 -m 90 -n pull_90 --setParameters BR=0 -t -1 --robustHesse 1 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1
fi
if [ $1 -eq 4 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_100 -m 100 -n pull_100 --setParameters BR=0 -t -1 --robustHesse 1 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1
fi
if [ $1 -eq 5 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_110 -m 110 -n pull_110 --setParameters BR=0 -t -1 --robustHesse 1 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1
fi
if [ $1 -eq 6 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_120 -m 120 -n pull_120 --setParameters BR=0 -t -1 --robustHesse 1 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1
fi
if [ $1 -eq 7 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_130 -m 130 -n pull_130 --setParameters BR=0 -t -1 --robustHesse 1 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1
fi
if [ $1 -eq 8 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_140 -m 140 -n pull_140 --setParameters BR=0 -t -1 --robustHesse 1 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1
fi
if [ $1 -eq 9 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_150 -m 150 -n pull_150 --setParameters BR=0 -t -1 --robustHesse 1 --robustFit 1 --setRobustFitTolerance 1 --stepSize 0.1 --rMin -1
fi
if [ $1 -eq 10 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_160 -m 160 -n pull_160 --setParameters BR=0 -t -1 --robustHesse 1 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1
fi

