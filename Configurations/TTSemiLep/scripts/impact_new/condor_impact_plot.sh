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
WORK_SPACE_DIR_75=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_DNN/M075Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_80=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_DNN/M080Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_85=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_DNN/M085Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_90=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_DNN/M090Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_100=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_DNN/M100Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_110=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_DNN/M110Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_120=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_DNN/M120Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_130=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_DNN/M130Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_140=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_high_DNN/M140Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_150=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_high_DNN/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_160=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_high_DNN/M160Y2016noHIPMY2017Y2016HIPMY2018.txt.root


WORK_SPACE_DIR_Event_150=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_Event/M160Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_dijet_150=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_high/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_initial_dijet_150=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_initial_dijet_M/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root

# no SR
PARMS2='mask_Y2016HIPM__sng_4j_eleCH_3b=1,mask_Y2016HIPM__sng_4j_muCH_3b=1,mask_Y2016noHIPM__sng_4j_eleCH_3b=1,mask_Y2016noHIPM__sng_4j_muCH_3b=1,mask_Y2017__sng_4j_eleCH_3b=1,mask_Y2017__sng_4j_muCH_3b=1,mask_Y2018__sng_4j_eleCH_3b=1,mask_Y2018__sng_4j_muCH_3b=1,mask_Y2016HIPM__dbl_4j_ee=0,mask_Y2016HIPM__dbl_4j_mm=0,mask_Y2016noHIPM__dbl_4j_ee=0,mask_Y2016noHIPM__dbl_4j_mm=0,mask_Y2017__dbl_4j_ee=0,mask_Y2017__dbl_4j_mm=0,mask_Y2018__dbl_4j_ee=0,mask_Y2018__dbl_4j_mm=0,mask_Y2016HIPM__dbl_4j_em=0,mask_Y2016noHIPM__dbl_4j_em=0,mask_Y2017__dbl_4j_em=0,mask_Y2018__dbl_4j_em=0,mask_Y2018__dbl_4j_me=0,mask_Y2017__dbl_4j_me=0,mask_Y2016HIPM__dbl_4j_me=0,mask_Y2016HIPM__sng_4j_eleCH_2b=0,mask_Y2016HIPM__sng_4j_muCH_2b=0,mask_Y2016noHIPM__dbl_4j_me=0,mask_Y2016noHIPM__sng_4j_eleCH_2b=0,mask_Y2016noHIPM__sng_4j_muCH_2b=0,mask_Y2017__sng_4j_eleCH_2b=0,mask_Y2017__sng_4j_muCH_2b=0,mask_Y2018__sng_4j_eleCH_2b=0,mask_Y2018__sng_4j_muCH_2b=0'

PARMS='BR=1.001,ttbbXsec=1.36'
PARMS_noDL='BR=0.001,ttbbXsec=1.36,mask_Y2016HIPM__dbl_4j_ee=1,mask_Y2016HIPM__dbl_4j_mm=1,mask_Y2016noHIPM__dbl_4j_ee=1,mask_Y2016noHIPM__dbl_4j_mm=1,mask_Y2017__dbl_4j_ee=1,mask_Y2017__dbl_4j_mm=1,mask_Y2018__dbl_4j_ee=1,mask_Y2018__dbl_4j_mm=1,mask_Y2016HIPM__dbl_4j_em=1,mask_Y2016noHIPM__dbl_4j_em=1,mask_Y2017__dbl_4j_em=1,mask_Y2018__dbl_4j_em=1,mask_Y2018__dbl_4j_me=1,mask_Y2017__dbl_4j_me=1,mask_Y2016HIPM__dbl_4j_me=1,mask_Y2016noHIPM__dbl_4j_me=1'


if [ $1 -eq 0 ]; then
  mkdir -p impact_mH75
  cd impact_mH75
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_75  -m 75 -o impacts.json
  plotImpacts.py -i impacts.json -o impacts_mH75
fi
if [ $1 -eq 1 ]; then
  mkdir -p impact_mH80
  cd impact_mH80
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_80  -m 80 -o impacts.json
  plotImpacts.py -i impacts.json -o impacts_mH80
fi
if [ $1 -eq 2 ]; then
  mkdir -p impact_mH85
  cd impact_mH85
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_85  -m 85 -o impacts.json
  plotImpacts.py -i impacts.json -o impacts_mH85
fi
if [ $1 -eq 3 ]; then
  mkdir -p impact_mH90
  cd impact_mH90
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_90  -m 90 -o impacts.json
  plotImpacts.py -i impacts.json -o impacts_mH90
fi
if [ $1 -eq 4 ]; then
  mkdir -p impact_mH100
  cd impact_mH100
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_100  -m 100 -o impacts.json
  plotImpacts.py -i impacts.json -o impacts_mH100
fi
if [ $1 -eq 5 ]; then
  mkdir -p impact_mH110
  cd impact_mH110
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_110  -m 110 -o impacts.json
  plotImpacts.py -i impacts.json -o impacts_mH110
fi
if [ $1 -eq 6 ]; then
  mkdir -p impact_mH120
  cd impact_mH120
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_120  -m 120 -o impacts.json
  plotImpacts.py -i impacts.json -o impacts_mH120
fi
if [ $1 -eq 7 ]; then
  mkdir -p impact_mH130
  cd impact_mH130
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_130  -m 130 -o impacts.json
  plotImpacts.py -i impacts.json -o impacts_mH130
fi
if [ $1 -eq 8 ]; then
  mkdir -p impact_mH140
  cd impact_mH140
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_140  -m 140 -o impacts.json
  plotImpacts.py -i impacts.json -o impacts_mH140
fi
if [ $1 -eq 9 ]; then
  mkdir -p impact_mH150
  cd impact_mH150
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_150  -m 150 -o impacts.json
  plotImpacts.py -i impacts.json -o impacts_mH150
fi
if [ $1 -eq 10 ]; then
  mkdir -p impact_mH160
  cd impact_mH160
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_160  -m 160 -o impacts.json
  plotImpacts.py -i impacts.json -o impacts_mH160
fi
if [ $1 -eq 11 ]; then
  mkdir -p impact_mH150_noDL
  cd impact_mH150_noDL
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_150  -m 150 -o impacts.json
  plotImpacts.py -i impacts.json -o impacts_mH150_noDL
fi

