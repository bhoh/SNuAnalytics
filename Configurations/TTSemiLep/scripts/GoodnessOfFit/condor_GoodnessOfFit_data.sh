#!/bin/sh
#ulimit -s unlimited
#set -e
cd /cms/ldap_home/bhoh/HiggsCombTool/CMSSW_10_6_4/src
#export SCRAM_ARCH=slc7_amd64_gcc820
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
mkdir -p /cms_scratch/bhoh/toys
cd /cms_scratch/bhoh/toys

IMPORTPARS=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/GenerateOnly/importPars.py

WORK_SPACE_DIR_75=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_DNN_Low/M075Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_80=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_DNN_Low/M080Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_85=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_DNN_Low/M085Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_90=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_DNN_Low/M090Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_100=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_DNN_Low/M100Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_110=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_DNN_Low/M110Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_120=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_DNN_Low/M120Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_130=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_DNN_High/M130Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_140=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_high_DNN_High/M140Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_150=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_high_DNN_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR_160=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_high_DNN_High/M160Y2016noHIPMY2017Y2016HIPMY2018.txt.root

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


#WORK_SPACE_DIR_75=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics75.root
#WORK_SPACE_DIR_80=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics80.root
#WORK_SPACE_DIR_85=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics85.root
#WORK_SPACE_DIR_90=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics90.root
#WORK_SPACE_DIR_100=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics100.root
#WORK_SPACE_DIR_110=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics110.root
#WORK_SPACE_DIR_120=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics120.root
#WORK_SPACE_DIR_130=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics130.root
#WORK_SPACE_DIR_140=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics140.root
#WORK_SPACE_DIR_150=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics150.root
#WORK_SPACE_DIR_160=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics160.root






# no SR
PARMS2='mask_Y2016HIPM__sng_4j_eleCH_3b=1,mask_Y2016HIPM__sng_4j_muCH_3b=1,mask_Y2016noHIPM__sng_4j_eleCH_3b=1,mask_Y2016noHIPM__sng_4j_muCH_3b=1,mask_Y2017__sng_4j_eleCH_3b=1,mask_Y2017__sng_4j_muCH_3b=1,mask_Y2018__sng_4j_eleCH_3b=1,mask_Y2018__sng_4j_muCH_3b=1,mask_Y2016HIPM__dbl_4j_ee=0,mask_Y2016HIPM__dbl_4j_mm=0,mask_Y2016noHIPM__dbl_4j_ee=0,mask_Y2016noHIPM__dbl_4j_mm=0,mask_Y2017__dbl_4j_ee=0,mask_Y2017__dbl_4j_mm=0,mask_Y2018__dbl_4j_ee=0,mask_Y2018__dbl_4j_mm=0,mask_Y2016HIPM__dbl_4j_em=0,mask_Y2016noHIPM__dbl_4j_em=0,mask_Y2017__dbl_4j_em=0,mask_Y2018__dbl_4j_em=0,mask_Y2018__dbl_4j_me=0,mask_Y2017__dbl_4j_me=0,mask_Y2016HIPM__dbl_4j_me=0,mask_Y2016HIPM__sng_4j_eleCH_2b=0,mask_Y2016HIPM__sng_4j_muCH_2b=0,mask_Y2016noHIPM__dbl_4j_me=0,mask_Y2016noHIPM__sng_4j_eleCH_2b=0,mask_Y2016noHIPM__sng_4j_muCH_2b=0,mask_Y2017__sng_4j_eleCH_2b=0,mask_Y2017__sng_4j_muCH_2b=0,mask_Y2018__sng_4j_eleCH_2b=0,mask_Y2018__sng_4j_muCH_2b=0'

# only 1l CR
PARMS3='mask_Y2016HIPM__sng_4j_eleCH_3b=1,mask_Y2016HIPM__sng_4j_muCH_3b=1,mask_Y2016noHIPM__sng_4j_eleCH_3b=1,mask_Y2016noHIPM__sng_4j_muCH_3b=1,mask_Y2017__sng_4j_eleCH_3b=1,mask_Y2017__sng_4j_muCH_3b=1,mask_Y2018__sng_4j_eleCH_3b=1,mask_Y2018__sng_4j_muCH_3b=1,mask_Y2016HIPM__dbl_4j_ee=1,mask_Y2016HIPM__dbl_4j_mm=1,mask_Y2016noHIPM__dbl_4j_ee=1,mask_Y2016noHIPM__dbl_4j_mm=1,mask_Y2017__dbl_4j_ee=1,mask_Y2017__dbl_4j_mm=1,mask_Y2018__dbl_4j_ee=1,mask_Y2018__dbl_4j_mm=1,mask_Y2016HIPM__dbl_4j_em=1,mask_Y2016noHIPM__dbl_4j_em=1,mask_Y2017__dbl_4j_em=1,mask_Y2018__dbl_4j_em=1,mask_Y2018__dbl_4j_me=1,mask_Y2017__dbl_4j_me=1,mask_Y2016HIPM__dbl_4j_me=1,mask_Y2016HIPM__sng_4j_eleCH_2b=0,mask_Y2016HIPM__sng_4j_muCH_2b=0,mask_Y2016noHIPM__dbl_4j_me=1,mask_Y2016noHIPM__sng_4j_eleCH_2b=0,mask_Y2016noHIPM__sng_4j_muCH_2b=0,mask_Y2017__sng_4j_eleCH_2b=0,mask_Y2017__sng_4j_muCH_2b=0,mask_Y2018__sng_4j_eleCH_2b=0,mask_Y2018__sng_4j_muCH_2b=0'


# only dl
PARMS4='mask_Y2016HIPM__sng_4j_eleCH_3b=1,mask_Y2016HIPM__sng_4j_muCH_3b=1,mask_Y2016noHIPM__sng_4j_eleCH_3b=1,mask_Y2016noHIPM__sng_4j_muCH_3b=1,mask_Y2017__sng_4j_eleCH_3b=1,mask_Y2017__sng_4j_muCH_3b=1,mask_Y2018__sng_4j_eleCH_3b=1,mask_Y2018__sng_4j_muCH_3b=1,mask_Y2016HIPM__dbl_4j_ee=0,mask_Y2016HIPM__dbl_4j_mm=0,mask_Y2016noHIPM__dbl_4j_ee=0,mask_Y2016noHIPM__dbl_4j_mm=0,mask_Y2017__dbl_4j_ee=0,mask_Y2017__dbl_4j_mm=0,mask_Y2018__dbl_4j_ee=0,mask_Y2018__dbl_4j_mm=0,mask_Y2016HIPM__dbl_4j_em=0,mask_Y2016noHIPM__dbl_4j_em=0,mask_Y2017__dbl_4j_em=0,mask_Y2018__dbl_4j_em=0,mask_Y2018__dbl_4j_me=0,mask_Y2017__dbl_4j_me=0,mask_Y2016HIPM__dbl_4j_me=0,mask_Y2016HIPM__sng_4j_eleCH_2b=1,mask_Y2016HIPM__sng_4j_muCH_2b=1,mask_Y2016noHIPM__dbl_4j_me=0,mask_Y2016noHIPM__sng_4j_eleCH_2b=1,mask_Y2016noHIPM__sng_4j_muCH_2b=1,mask_Y2017__sng_4j_eleCH_2b=1,mask_Y2017__sng_4j_muCH_2b=1,mask_Y2018__sng_4j_eleCH_2b=1,mask_Y2018__sng_4j_muCH_2b=1'

#'mask_Y2016HIPM__sng_4j_eleCH_3b__failKF=1,mask_Y2016HIPM__sng_4j_muCH_3b__failKF=1,mask_Y2016noHIPM__sng_4j_eleCH_3b__failKF=1,mask_Y2016noHIPM__sng_4j_muCH_3b__failKF=1,mask_Y2017__sng_4j_eleCH_3b__failKF=1,mask_Y2017__sng_4j_muCH_3b__failKF=1,mask_Y2018__sng_4j_eleCH_3b__failKF=1,mask_Y2018__sng_4j_muCH_3b__failKF=1'

# --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --cminDefaultMinimizerStrategy 0
# --cminPreFit 1000 --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --cminFallbackAlgo Minuit2,Simplex,1:0.1  --verbose 3 --setParameterRanges CMS_Top_pTreweight=-1,0[:STNorm=-2,2:TTVNorm=-2,2]
#  --freezeParameters CMS_Top_pTreweight
if [ $1 -eq 0 ]; then
  combine -M GoodnessOfFit --algorithm saturated -d $WORK_SPACE_DIR_75  -m 75 --setParameters $PARMS2,BR=0 --freezeParameters BR -n data  --cminFallbackAlgo Minuit2,Simplex,1:0.1  --verbose 3
fi
if [ $1 -eq 1 ]; then
  combine -M GoodnessOfFit --algorithm saturated -d $WORK_SPACE_DIR_80  -m 80 --setParameters $PARMS2,BR=0 --freezeParameters BR -n data  --cminFallbackAlgo Minuit2,Simplex,1:0.1  --verbose 3
fi
if [ $1 -eq 2 ]; then
  combine -M GoodnessOfFit --algorithm saturated -d $WORK_SPACE_DIR_85  -m 85 --setParameters $PARMS2,BR=0 --freezeParameters BR -n data  --cminFallbackAlgo Minuit2,Simplex,1:0.1  --verbose 3
fi
if [ $1 -eq 3 ]; then
  combine -M GoodnessOfFit --algorithm saturated -d $WORK_SPACE_DIR_90  -m 90 --setParameters $PARMS2,BR=0 --freezeParameters BR -n data  --cminFallbackAlgo Minuit2,Simplex,1:0.1  --verbose 3
fi
if [ $1 -eq 4 ]; then
  combine -M GoodnessOfFit --algorithm saturated -d $WORK_SPACE_DIR_100  -m 100 --setParameters $PARMS2,BR=0 --freezeParameters BR -n data  --cminFallbackAlgo Minuit2,Simplex,1:0.1  --verbose 3  
fi
if [ $1 -eq 5 ]; then
  combine -M GoodnessOfFit --algorithm saturated -d $WORK_SPACE_DIR_110  -m 110 --setParameters $PARMS2,BR=0 --freezeParameters BR -n data  --cminFallbackAlgo Minuit2,Simplex,1:0.1  --verbose 3 
fi
if [ $1 -eq 6 ]; then
  combine -M GoodnessOfFit --algorithm saturated -d $WORK_SPACE_DIR_120  -m 120 --setParameters $PARMS2,BR=0 --freezeParameters BR -n data  --cminFallbackAlgo Minuit2,Simplex,1:0.1  --verbose 3  
fi
if [ $1 -eq 7 ]; then
  combine -M GoodnessOfFit --algorithm saturated -d $WORK_SPACE_DIR_130  -m 130 --setParameters $PARMS2,BR=0 --freezeParameters BR -n data  --cminFallbackAlgo Minuit2,Simplex,1:0.1  --verbose 3  
fi
if [ $1 -eq 8 ]; then
  combine -M GoodnessOfFit --algorithm saturated -d $WORK_SPACE_DIR_140  -m 140 --setParameters $PARMS2,BR=0 --freezeParameters BR -n data  --cminFallbackAlgo Minuit2,Simplex,1:0.1  --verbose 3  
fi
if [ $1 -eq 9 ]; then
  combine -M GoodnessOfFit --algorithm saturated -d $WORK_SPACE_DIR_150  -m 150 --setParameters $PARMS2,BR=0 --freezeParameters BR -n data  --cminFallbackAlgo Minuit2,Simplex,1:0.1  --verbose 3  
fi
if [ $1 -eq 10 ]; then
  combine -M GoodnessOfFit --algorithm saturated -d $WORK_SPACE_DIR_160  -m 160 --setParameters $PARMS2,BR=0 --freezeParameters BR -n data  --cminFallbackAlgo Minuit2,Simplex,1:0.1  --verbose 3  
fi


cd /cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/GoodnessOfFit
