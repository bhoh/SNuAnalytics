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

PARMS='BR=0.001,ttbbXsec=1.36'
PARMS_noDL='BR=0.001,ttbbXsec=1.36,mask_Y2016HIPM__dbl_4j_ee=1,mask_Y2016HIPM__dbl_4j_mm=1,mask_Y2016noHIPM__dbl_4j_ee=1,mask_Y2016noHIPM__dbl_4j_mm=1,mask_Y2017__dbl_4j_ee=1,mask_Y2017__dbl_4j_mm=1,mask_Y2018__dbl_4j_ee=1,mask_Y2018__dbl_4j_mm=1,mask_Y2016HIPM__dbl_4j_em=1,mask_Y2016noHIPM__dbl_4j_em=1,mask_Y2017__dbl_4j_em=1,mask_Y2018__dbl_4j_em=1,mask_Y2018__dbl_4j_me=1,mask_Y2017__dbl_4j_me=1,mask_Y2016HIPM__dbl_4j_me=1,mask_Y2016noHIPM__dbl_4j_me=1'

if [ $1 -eq 0 ]; then
  mkdir -p impact_mH75
  cd impact_mH75
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_75 -m 75  --doInitialFit --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --cminDefaultMinimizerTolerance=0.1 --setParameters $PARMS --rMin -1 -t -1
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_75 -m 75  --robustFit 1  --doFits --verbose 3 --job-mode condor --setRobustFitTolerance 1.0 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH75_t-1' --setParameters $PARMS  --rMin -1 -t -1 --dry-run


fi
if [ $1 -eq 1 ]; then
  mkdir -p impact_mH80
  cd impact_mH80
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_80 -m 80  --doInitialFit --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --cminDefaultMinimizerTolerance=0.1 --setParameters $PARMS --rMin -1 -t -1
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_80 -m 80  --robustFit 1  --doFits --verbose 3 --job-mode condor --setRobustFitTolerance 1.0 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH80_t-1' --setParameters $PARMS  --rMin -1 -t -1 --dry-run
fi
if [ $1 -eq 2 ]; then
  mkdir -p impact_mH85
  cd impact_mH85
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_85 -m 85  --doInitialFit --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --cminDefaultMinimizerTolerance=0.1 --setParameters $PARMS --rMin -1 -t -1
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_85 -m 85  --robustFit 1  --doFits --verbose 3 --job-mode condor --setRobustFitTolerance 1.0 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH85_t-1' --setParameters $PARMS  --rMin -1 -t -1 --dry-run
fi
if [ $1 -eq 3 ]; then
  mkdir -p impact_mH90
  cd impact_mH90
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_90 -m 90  --doInitialFit --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --cminDefaultMinimizerTolerance=0.1 --setParameters $PARMS --rMin -1 -t -1
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_90 -m 90  --robustFit 1  --doFits --verbose 3 --job-mode condor --setRobustFitTolerance 1.0 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH90_t-1' --setParameters $PARMS  --rMin -1 -t -1 --dry-run
fi
if [ $1 -eq 4 ]; then
  mkdir -p impact_mH100
  cd impact_mH100
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_100 -m 100  --doInitialFit --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --cminDefaultMinimizerTolerance=0.1 --setParameters $PARMS --rMin -1 -t -1
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_100 -m 100  --robustFit 1  --doFits --verbose 3 --job-mode condor --setRobustFitTolerance 1.0 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH100_t-1' --setParameters $PARMS  --rMin -1 -t -1 --dry-run
fi
if [ $1 -eq 5 ]; then
  mkdir -p impact_mH110
  cd impact_mH110
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_110 -m 110  --doInitialFit --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --cminDefaultMinimizerTolerance=0.1 --setParameters $PARMS --rMin -1 -t -1
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_110 -m 110  --robustFit 1  --doFits --verbose 3 --job-mode condor --setRobustFitTolerance 1.0 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH110_t-1' --setParameters $PARMS  --rMin -1 -t -1 --dry-run
fi
if [ $1 -eq 6 ]; then
  mkdir -p impact_mH120
  cd impact_mH120
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_120 -m 120  --doInitialFit --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --cminDefaultMinimizerTolerance=0.1 --setParameters $PARMS --rMin -1 -t -1
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_120 -m 120  --robustFit 1  --doFits --verbose 3 --job-mode condor --setRobustFitTolerance 1.0 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH120_t-1' --setParameters $PARMS  --rMin -1 -t -1 --dry-run
fi
if [ $1 -eq 7 ]; then
  mkdir -p impact_mH130
  cd impact_mH130
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_130 -m 130  --doInitialFit --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --cminDefaultMinimizerTolerance=0.1 --setParameters $PARMS --rMin -1 -t -1
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_130 -m 130  --robustFit 1  --doFits --verbose 3 --job-mode condor --setRobustFitTolerance 1.0 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH130_t-1' --setParameters $PARMS  --rMin -1 -t -1 --dry-run
fi
if [ $1 -eq 8 ]; then
  mkdir -p impact_mH140
  cd impact_mH140
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_140 -m 140  --doInitialFit --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --cminDefaultMinimizerTolerance=0.1 --setParameters $PARMS --rMin -1 -t -1
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_140 -m 140  --robustFit 1  --doFits --verbose 3 --job-mode condor --setRobustFitTolerance 1.0 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH140_t-1' --setParameters $PARMS  --rMin -1 -t -1 --dry-run
fi
if [ $1 -eq 9 ]; then
  mkdir -p impact_mH150
  cd impact_mH150
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_150 -m 150  --doInitialFit --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --cminDefaultMinimizerTolerance=0.1 --setParameters $PARMS --rMin -1 -t -1
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_150 -m 150  --robustFit 1  --doFits --verbose 3 --job-mode condor --setRobustFitTolerance 1.0 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH150_t-1' --setParameters $PARMS  --rMin -1 -t -1 --dry-run
fi
if [ $1 -eq 10 ]; then
  mkdir -p impact_mH160
  cd impact_mH160
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_160 -m 160  --doInitialFit --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --cminDefaultMinimizerTolerance=0.1 --setParameters $PARMS --rMin -1 -t -1
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_160 -m 160  --robustFit 1  --doFits --verbose 3 --job-mode condor --setRobustFitTolerance 1.0 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH160_t-1' --setParameters $PARMS  --rMin -1 -t -1 --dry-run
fi

# without DL control
if [ $1 -eq 11 ]; then
  mkdir -p impact_mH150_noDL
  cd impact_mH150_noDL
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_150 -m 150  --doInitialFit --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --cminDefaultMinimizerTolerance=0.1 --setParameters $PARMS_noDL --rMin -1 -t -1
  combineTool.py -M Impacts -d $WORK_SPACE_DIR_150 -m 150  --robustFit 1  --doFits --verbose 3 --job-mode condor --setRobustFitTolerance 1.0 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH150_noDL_t-1' --setParameters $PARMS_noDL  --rMin -1 -t -1 --dry-run
fi
#if [ $1 -eq 3 ]; then
#  mkdir -p impact_Event_mH150
#  cd impact_Event_mH150
#  combineTool.py -M Impacts -d $WORK_SPACE_DIR_Event_150 -m 150  --doInitialFit --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --cminDefaultMinimizerTolerance=0.1 --setParameters $PARMS --rMin -1 -t -1
#  combineTool.py -M Impacts -d $WORK_SPACE_DIR_Event_150 -m 150  --robustFit 1  --doFits --verbose 3 --job-mode condor --setRobustFitTolerance 1.0 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --sub-opts='accounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH150_t-1' --setParameters $PARMS  --rMin -1 -t -1 --dry-run
#
#fi
#if [ $1 -eq 4 ]; then
#  mkdir -p impact_dijet_mH150
#  cd impact_dijet_mH150
#  combineTool.py -M Impacts -d $WORK_SPACE_DIR_dijet_150 -m 150  --doInitialFit --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --cminDefaultMinimizerTolerance=0.1 --setParameters $PARMS --rMin -1 -t -1
#  combineTool.py -M Impacts -d $WORK_SPACE_DIR_dijet_150 -m 150  --robustFit 1  --doFits --verbose 3 --job-mode condor --setRobustFitTolerance 1.0 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --sub-opts='accounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH150_t-1' --setParameters $PARMS  --rMin -1 -t -1 --dry-run
#
#fi
#if [ $1 -eq 5 ]; then
#  mkdir -p impact_initial_dijet_mH150
#  cd impact_initial_dijet_mH150
#  combineTool.py -M Impacts -d $WORK_SPACE_DIR_initial_dijet_150 -m 150  --doInitialFit --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --cminDefaultMinimizerTolerance=0.1 --setParameters $PARMS --rMin -1 -t -1
#  combineTool.py -M Impacts -d $WORK_SPACE_DIR_initial_dijet_150 -m 150  --robustFit 1  --doFits --verbose 3 --job-mode condor --setRobustFitTolerance 1.0 --stepSize 0.1 --setRobustFitStrategy 0 --keepFailures --cminApproxPreFitTolerance=10 --X-rtd MINIMIZER_MaxCalls=9999999 --sub-opts='accounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH150_t-1' --setParameters $PARMS  --rMin -1 -t -1 --dry-run
#
#fi

