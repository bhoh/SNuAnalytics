#!/bin/sh
ulimit -s unlimited
set -e
cd /cms/ldap_home/bhoh/HiggsCombTool/CMSSW_10_6_4/src
export SCRAM_ARCH=slc7_amd64_gcc820
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
mkdir -p /cms_scratch/bhoh/toys
cd /cms_scratch/bhoh/toys

WORK_SPACE_DIR_75=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics75.root
WORK_SPACE_DIR_80=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics80.root
WORK_SPACE_DIR_85=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics85.root
WORK_SPACE_DIR_90=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics90.root
WORK_SPACE_DIR_100=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics100.root
WORK_SPACE_DIR_110=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics110.root
WORK_SPACE_DIR_120=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics120.root
WORK_SPACE_DIR_130=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics130.root
WORK_SPACE_DIR_140=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics140.root
WORK_SPACE_DIR_150=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics150.root
WORK_SPACE_DIR_160=/cms_scratch/bhoh/toys/morphedWorkspace_fitDiagnostics160.root


# no SR
PARMS2='mask_Y2016HIPM__sng_4j_eleCH_3b=1,mask_Y2016HIPM__sng_4j_muCH_3b=1,mask_Y2016noHIPM__sng_4j_eleCH_3b=1,mask_Y2016noHIPM__sng_4j_muCH_3b=1,mask_Y2017__sng_4j_eleCH_3b=1,mask_Y2017__sng_4j_muCH_3b=1,mask_Y2018__sng_4j_eleCH_3b=1,mask_Y2018__sng_4j_muCH_3b=1,mask_Y2016HIPM__dbl_4j_ee=0,mask_Y2016HIPM__dbl_4j_mm=0,mask_Y2016noHIPM__dbl_4j_ee=0,mask_Y2016noHIPM__dbl_4j_mm=0,mask_Y2017__dbl_4j_ee=0,mask_Y2017__dbl_4j_mm=0,mask_Y2018__dbl_4j_ee=0,mask_Y2018__dbl_4j_mm=0,mask_Y2016HIPM__dbl_4j_em=0,mask_Y2016noHIPM__dbl_4j_em=0,mask_Y2017__dbl_4j_em=0,mask_Y2018__dbl_4j_em=0,mask_Y2018__dbl_4j_me=0,mask_Y2017__dbl_4j_me=0,mask_Y2016HIPM__dbl_4j_me=0,mask_Y2016HIPM__sng_4j_eleCH_2b=0,mask_Y2016HIPM__sng_4j_muCH_2b=0,mask_Y2016noHIPM__dbl_4j_me=0,mask_Y2016noHIPM__sng_4j_eleCH_2b=0,mask_Y2016noHIPM__sng_4j_muCH_2b=0,mask_Y2017__sng_4j_eleCH_2b=0,mask_Y2017__sng_4j_muCH_2b=0,mask_Y2018__sng_4j_eleCH_2b=0,mask_Y2018__sng_4j_muCH_2b=0'
# with SR
PARMS3='mask_Y2016HIPM__sng_4j_eleCH_3b=0,mask_Y2016HIPM__sng_4j_muCH_3b=0,mask_Y2016noHIPM__sng_4j_eleCH_3b=0,mask_Y2016noHIPM__sng_4j_muCH_3b=0,mask_Y2017__sng_4j_eleCH_3b=0,mask_Y2017__sng_4j_muCH_3b=0,mask_Y2018__sng_4j_eleCH_3b=0,mask_Y2018__sng_4j_muCH_3b=0,mask_Y2016HIPM__dbl_4j_ee=0,mask_Y2016HIPM__dbl_4j_mm=0,mask_Y2016noHIPM__dbl_4j_ee=0,mask_Y2016noHIPM__dbl_4j_mm=0,mask_Y2017__dbl_4j_ee=0,mask_Y2017__dbl_4j_mm=0,mask_Y2018__dbl_4j_ee=0,mask_Y2018__dbl_4j_mm=0,mask_Y2016HIPM__dbl_4j_em=0,mask_Y2016noHIPM__dbl_4j_em=0,mask_Y2017__dbl_4j_em=0,mask_Y2018__dbl_4j_em=0,mask_Y2018__dbl_4j_me=0,mask_Y2017__dbl_4j_me=0,mask_Y2016HIPM__dbl_4j_me=0,mask_Y2016HIPM__sng_4j_eleCH_2b=0,mask_Y2016HIPM__sng_4j_muCH_2b=0,mask_Y2016noHIPM__dbl_4j_me=0,mask_Y2016noHIPM__sng_4j_eleCH_2b=0,mask_Y2016noHIPM__sng_4j_muCH_2b=0,mask_Y2017__sng_4j_eleCH_2b=0,mask_Y2017__sng_4j_muCH_2b=0,mask_Y2018__sng_4j_eleCH_2b=0,mask_Y2018__sng_4j_muCH_2b=0'
#
# --robustHesse 1 --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.01 

#--robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.01 
if [ $1 -eq 0 ]; then
  #combine -M MultiDimFit --saveWorkspace -n pull_75 -d $WORK_SPACE_DIR_75 --freezeParameters BR -m 75 --setParameters $PARMS2 --robustFit 1 --rMax 0.01 --rMin -1
  #combine -M FitDiagnostics -d higgsCombinepull_75.MultiDimFit.mH75.root -w w --snapshotName "MultiDimFit" -n pull_morphed_75 -t -1 --setParameters $PARMS3,BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_75 -m 75 -n pull_morphed_75 -t -1 --setParameters BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
fi
if [ $1 -eq 1 ]; then
  #combine -M MultiDimFit --saveWorkspace -n pull_80 -d $WORK_SPACE_DIR_80 --freezeParameters BR -m 80 --setParameters $PARMS2 --robustFit 1 --rMax 0.01 --rMin -1
  #combine -M FitDiagnostics -d higgsCombinepull_80.MultiDimFit.mH80.root -w w --snapshotName "MultiDimFit" -n pull_morphed_80 -t -1 --setParameters $PARMS3,BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_80 -m 80 -n pull_morphed_80 -t -1 --setParameters BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
fi
if [ $1 -eq 2 ]; then
  #combine -M MultiDimFit --saveWorkspace -n pull_85 -d $WORK_SPACE_DIR_85 --freezeParameters BR -m 85 --setParameters $PARMS2 --robustFit 1 --rMax 0.01 --rMin -1
  #combine -M FitDiagnostics -d higgsCombinepull_85.MultiDimFit.mH85.root -w w --snapshotName "MultiDimFit" -n pull_morphed_85 -t -1 --setParameters $PARMS3,BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_85 -m 85 -n pull_morphed_85 -t -1 --setParameters BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
fi
if [ $1 -eq 3 ]; then
  #combine -M MultiDimFit --saveWorkspace -n pull_90 -d $WORK_SPACE_DIR_90 --freezeParameters BR -m 90 --setParameters $PARMS2 --robustFit 1 --rMax 0.01 --rMin -1
  #combine -M FitDiagnostics -d higgsCombinepull_90.MultiDimFit.mH90.root -w w --snapshotName "MultiDimFit" -n pull_morphed_90 -t -1 --setParameters $PARMS3,BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_90 -m 90 -n pull_morphed_90 -t -1 --setParameters BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
fi
if [ $1 -eq 4 ]; then
  #combine -M MultiDimFit --saveWorkspace -n pull_100 -d $WORK_SPACE_DIR_100 --freezeParameters BR -m 100 --setParameters $PARMS2 --robustFit 1 --rMax 0.01 --rMin -1
  #combine -M FitDiagnostics -d higgsCombinepull_100.MultiDimFit.mH100.root -w w --snapshotName "MultiDimFit" -n pull_morphed_100 -t -1 --setParameters $PARMS3,BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_100 -m 100 -n pull_morphed_100 -t -1 --setParameters BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
fi
if [ $1 -eq 5 ]; then
  #combine -M MultiDimFit --saveWorkspace -n pull_110 -d $WORK_SPACE_DIR_110 --freezeParameters BR -m 110 --setParameters $PARMS2 --robustFit 1 --rMax 0.01 --rMin -1
  #combine -M FitDiagnostics -d higgsCombinepull_110.MultiDimFit.mH110.root -w w --snapshotName "MultiDimFit" -n pull_morphed_110 -t -1 --setParameters $PARMS3,BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_110 -m 110 -n pull_morphed_110 -t -1 --setParameters BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
fi
if [ $1 -eq 6 ]; then
  #combine -M MultiDimFit --saveWorkspace -n pull_120 -d $WORK_SPACE_DIR_120 --freezeParameters BR -m 120 --setParameters $PARMS2 --robustFit 1 --rMax 0.01 --rMin -1
  #combine -M FitDiagnostics -d higgsCombinepull_120.MultiDimFit.mH120.root -w w --snapshotName "MultiDimFit" -n pull_morphed_120 -t -1 --setParameters $PARMS3,BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_120 -m 120 -n pull_morphed_120 -t -1 --setParameters BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
fi
if [ $1 -eq 7 ]; then
  #combine -M MultiDimFit --saveWorkspace -n pull_130 -d $WORK_SPACE_DIR_130 --freezeParameters BR -m 130 --setParameters $PARMS2 --robustFit 1 --rMax 0.01 --rMin -1
  #combine -M FitDiagnostics -d higgsCombinepull_130.MultiDimFit.mH130.root -w w --snapshotName "MultiDimFit" -n pull_morphed_130 -t -1 --setParameters $PARMS3,BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_130 -m 130 -n pull_morphed_130 -t -1 --setParameters BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
fi
if [ $1 -eq 8 ]; then
  #combine -M MultiDimFit --saveWorkspace -n pull_140 -d $WORK_SPACE_DIR_140 --freezeParameters BR -m 140 --setParameters $PARMS2 --robustFit 1 --rMax 0.01 --rMin -1
  #combine -M FitDiagnostics -d higgsCombinepull_140.MultiDimFit.mH140.root -w w --snapshotName "MultiDimFit" -n pull_morphed_140 -t -1 --setParameters $PARMS3,BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_140 -m 140 -n pull_morphed_140 -t -1 --setParameters BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
fi
if [ $1 -eq 9 ]; then
  #combine -M MultiDimFit --saveWorkspace -n pull_150 -d $WORK_SPACE_DIR_150 --freezeParameters BR -m 150 --setParameters $PARMS2 --robustFit 1 --rMax 0.01 --rMin -1
  #combine -M FitDiagnostics -d higgsCombinepull_150.MultiDimFit.mH150.root -w w --snapshotName "MultiDimFit" -n pull_morphed_150 -t -1 --setParameters $PARMS3,BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_150 -m 150 -n pull_morphed_150 -t -1 --setParameters BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
fi
if [ $1 -eq 10 ]; then
  #combine -M MultiDimFit --saveWorkspace -n pull_160 -d $WORK_SPACE_DIR_160 --freezeParameters BR -m 160 --setParameters $PARMS2 --robustFit 1 --rMax 0.01 --rMin -1
  #combine -M FitDiagnostics -d higgsCombinepull_160.MultiDimFit.mH160.root -w w --snapshotName "MultiDimFit" -n pull_morphed_160 -t -1 --setParameters $PARMS3,BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
  combine -M FitDiagnostics -d $WORK_SPACE_DIR_160 -m 160 -n pull_morphed_160 -t -1 --setParameters BR=0  --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1 --robustHesse 1 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999
fi

