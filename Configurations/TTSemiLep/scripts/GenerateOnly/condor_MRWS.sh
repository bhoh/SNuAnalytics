#!/bin/sh
ulimit -s unlimited
set -e
cd /cms/ldap_home/bhoh/HiggsCombTool/CMSSW_10_6_4/src
export SCRAM_ARCH=slc7_amd64_gcc820
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
mkdir -p /cms_scratch/bhoh/toys
cd /cms_scratch/bhoh/toys

IMPORTPARS=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/GenerateOnly/importPars.py

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

# no SR
PARMS2='mask_Y2016HIPM__sng_4j_eleCH_3b=1,mask_Y2016HIPM__sng_4j_muCH_3b=1,mask_Y2016noHIPM__sng_4j_eleCH_3b=1,mask_Y2016noHIPM__sng_4j_muCH_3b=1,mask_Y2017__sng_4j_eleCH_3b=1,mask_Y2017__sng_4j_muCH_3b=1,mask_Y2018__sng_4j_eleCH_3b=1,mask_Y2018__sng_4j_muCH_3b=1,mask_Y2016HIPM__dbl_4j_ee=0,mask_Y2016HIPM__dbl_4j_mm=0,mask_Y2016noHIPM__dbl_4j_ee=0,mask_Y2016noHIPM__dbl_4j_mm=0,mask_Y2017__dbl_4j_ee=0,mask_Y2017__dbl_4j_mm=0,mask_Y2018__dbl_4j_ee=0,mask_Y2018__dbl_4j_mm=0,mask_Y2016HIPM__dbl_4j_em=0,mask_Y2016noHIPM__dbl_4j_em=0,mask_Y2017__dbl_4j_em=0,mask_Y2018__dbl_4j_em=0,mask_Y2018__dbl_4j_me=0,mask_Y2017__dbl_4j_me=0,mask_Y2016HIPM__dbl_4j_me=0,mask_Y2016HIPM__sng_4j_eleCH_2b=0,mask_Y2016HIPM__sng_4j_muCH_2b=0,mask_Y2016noHIPM__dbl_4j_me=0,mask_Y2016noHIPM__sng_4j_eleCH_2b=0,mask_Y2016noHIPM__sng_4j_muCH_2b=0,mask_Y2017__sng_4j_eleCH_2b=0,mask_Y2017__sng_4j_muCH_2b=0,mask_Y2018__sng_4j_eleCH_2b=0,mask_Y2018__sng_4j_muCH_2b=0'


if [ $1 -eq 0 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_75 -m 75 --setParameters $PARMS2 -n 75 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --cminDefaultMinimizerStrategy 0
  python $IMPORTPARS $WORK_SPACE_DIR_75 fitDiagnostics75.root
fi
if [ $1 -eq 1 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_80 -m 80 --setParameters $PARMS2 -n 80 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --cminDefaultMinimizerStrategy 0
  python $IMPORTPARS $WORK_SPACE_DIR_80 fitDiagnostics80.root
fi
if [ $1 -eq 2 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_85 -m 85 --setParameters $PARMS2 -n 85 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --cminDefaultMinimizerStrategy 0
  python $IMPORTPARS $WORK_SPACE_DIR_85 fitDiagnostics85.root
fi
if [ $1 -eq 3 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_90 -m 90 --setParameters $PARMS2 -n 90 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --cminDefaultMinimizerStrategy 0
  python $IMPORTPARS $WORK_SPACE_DIR_90 fitDiagnostics90.root
fi
if [ $1 -eq 4 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_100 -m 100 --setParameters $PARMS2 -n 100 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --cminDefaultMinimizerStrategy 0
  python $IMPORTPARS $WORK_SPACE_DIR_100 fitDiagnostics100.root
fi
if [ $1 -eq 5 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_110 -m 110 --setParameters $PARMS2 -n 110 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --cminDefaultMinimizerStrategy 0
  python $IMPORTPARS $WORK_SPACE_DIR_110 fitDiagnostics110.root
fi
if [ $1 -eq 6 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_120 -m 120 --setParameters $PARMS2 -n 120 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --cminDefaultMinimizerStrategy 0
  python $IMPORTPARS $WORK_SPACE_DIR_120 fitDiagnostics120.root
fi
if [ $1 -eq 7 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_130 -m 130 --setParameters $PARMS2 -n 130 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --cminDefaultMinimizerStrategy 0
  python $IMPORTPARS $WORK_SPACE_DIR_130 fitDiagnostics130.root
fi
if [ $1 -eq 8 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_140 -m 140 --setParameters $PARMS2 -n 140 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --cminDefaultMinimizerStrategy 0
  python $IMPORTPARS $WORK_SPACE_DIR_140 fitDiagnostics140.root
fi
if [ $1 -eq 9 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_150 -m 150 --setParameters $PARMS2 -n 150 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --cminDefaultMinimizerStrategy 0
  python $IMPORTPARS $WORK_SPACE_DIR_150 fitDiagnostics150.root
fi
if [ $1 -eq 10 ]; then
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_160 -m 160 --setParameters $PARMS2 -n 160 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --cminDefaultMinimizerStrategy 0
  python $IMPORTPARS $WORK_SPACE_DIR_160 fitDiagnostics160.root
fi
