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



#WORK_SPACE_DIR_Event_150=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_Event/M160Y2016noHIPMY2017Y2016HIPMY2018.txt.root
#WORK_SPACE_DIR_dijet_150=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_fitted_dijet_M_high/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root
#WORK_SPACE_DIR_initial_dijet_150=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/workspace/Asym_initial_dijet_M/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root

# no SR
PARMS='mask_Y2016HIPM__sng_4j_eleCH_3b=1,mask_Y2016HIPM__sng_4j_muCH_3b=1,mask_Y2016noHIPM__sng_4j_eleCH_3b=1,mask_Y2016noHIPM__sng_4j_muCH_3b=1,mask_Y2017__sng_4j_eleCH_3b=1,mask_Y2017__sng_4j_muCH_3b=1,mask_Y2018__sng_4j_eleCH_3b=1,mask_Y2018__sng_4j_muCH_3b=1,mask_Y2016HIPM__dbl_4j_ee=0,mask_Y2016HIPM__dbl_4j_mm=0,mask_Y2016noHIPM__dbl_4j_ee=0,mask_Y2016noHIPM__dbl_4j_mm=0,mask_Y2017__dbl_4j_ee=0,mask_Y2017__dbl_4j_mm=0,mask_Y2018__dbl_4j_ee=0,mask_Y2018__dbl_4j_mm=0,mask_Y2016HIPM__dbl_4j_em=0,mask_Y2016noHIPM__dbl_4j_em=0,mask_Y2017__dbl_4j_em=0,mask_Y2018__dbl_4j_em=0,mask_Y2018__dbl_4j_me=0,mask_Y2017__dbl_4j_me=0,mask_Y2016HIPM__dbl_4j_me=0,mask_Y2016HIPM__sng_4j_eleCH_2b=0,mask_Y2016HIPM__sng_4j_muCH_2b=0,mask_Y2016noHIPM__dbl_4j_me=0,mask_Y2016noHIPM__sng_4j_eleCH_2b=0,mask_Y2016noHIPM__sng_4j_muCH_2b=0,mask_Y2017__sng_4j_eleCH_2b=0,mask_Y2017__sng_4j_muCH_2b=0,mask_Y2018__sng_4j_eleCH_2b=0,mask_Y2018__sng_4j_muCH_2b=0'
UNMASK_SR='mask_Y2016HIPM__sng_4j_eleCH_3b=0,mask_Y2016HIPM__sng_4j_muCH_3b=0,mask_Y2016noHIPM__sng_4j_eleCH_3b=0,mask_Y2016noHIPM__sng_4j_muCH_3b=0,mask_Y2017__sng_4j_eleCH_3b=0,mask_Y2017__sng_4j_muCH_3b=0,mask_Y2018__sng_4j_eleCH_3b=0,mask_Y2018__sng_4j_muCH_3b=0'

PARMS3='BR=0,ttbbXsec=1.36'
PARMS_noDL='BR=0,ttbbXsec=1.36,mask_Y2016HIPM__dbl_4j_ee=1,mask_Y2016HIPM__dbl_4j_mm=1,mask_Y2016noHIPM__dbl_4j_ee=1,mask_Y2016noHIPM__dbl_4j_mm=1,mask_Y2017__dbl_4j_ee=1,mask_Y2017__dbl_4j_mm=1,mask_Y2018__dbl_4j_ee=1,mask_Y2018__dbl_4j_mm=1,mask_Y2016HIPM__dbl_4j_em=1,mask_Y2016noHIPM__dbl_4j_em=1,mask_Y2017__dbl_4j_em=1,mask_Y2018__dbl_4j_em=1,mask_Y2018__dbl_4j_me=1,mask_Y2017__dbl_4j_me=1,mask_Y2016HIPM__dbl_4j_me=1,mask_Y2016noHIPM__dbl_4j_me=1'

if [ $1 -eq 0 ]; then
  mkdir -p impact_morphed_mH75
  cd impact_morphed_mH75
  combine -M MultiDimFit -n _initialFit_Test --algo singles -m 75 -d $WORK_SPACE_DIR_75 --saveWorkspace --robustFit 1 --robustHesse 1 --setParameters $PARMS --verbose 3 --keepFailures --cminApproxPreFitTolerance=10 --rMin -1
  combineTool.py -M Impacts -d higgsCombine_initialFit_Test.MultiDimFit.mH75.root -m 75 -w w --snapshotName "MultiDimFit" --robustFit 1  --doFits --job-mode condor --setRobustFitTolerance 0.1 --stepSize 0.1 --keepFailures --cminApproxPreFitTolerance=10 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH75_t-1' -t -1 --rMin -1 --setParameters $UNMASK_SR,BR=0 --dry-run

fi

if [ $1 -eq 1 ]; then
  mkdir -p impact_morphed_mH80
  cd impact_morphed_mH80
  combine -M MultiDimFit -n _initialFit_Test --algo singles -m 80 -d $WORK_SPACE_DIR_80 --saveWorkspace --robustFit 1 --robustHesse 1 --setParameters $PARMS --verbose 3 --keepFailures --cminApproxPreFitTolerance=10  --rMin -1
  combineTool.py -M Impacts -d higgsCombine_initialFit_Test.MultiDimFit.mH80.root -m 80 -w w --snapshotName "MultiDimFit" --robustFit 1  --doFits --job-mode condor --setRobustFitTolerance 0.1 --stepSize 0.1 --keepFailures --cminApproxPreFitTolerance=10 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH80_t-1' -t -1 --rMin -1 --setParameters $UNMASK_SR,BR=0 --dry-run

fi


if [ $1 -eq 2 ]; then
  mkdir -p "impact_morphed_mH85"
  cd "impact_morphed_mH85"
  combine -M MultiDimFit -n _initialFit_Test --algo singles -m 85 -d $WORK_SPACE_DIR_85 --saveWorkspace --robustFit 1 --robustHesse 1 --setParameters $PARMS --verbose 3 --keepFailures --cminApproxPreFitTolerance=10 --rMin -1
  combineTool.py -M Impacts -d "higgsCombine_initialFit_Test.MultiDimFit.mH85.root" -m 85 -w w --snapshotName "MultiDimFit" --robustFit 1 --doFits --job-mode condor --setRobustFitTolerance 0.1 --stepSize 0.1 --keepFailures --cminApproxPreFitTolerance=10 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH85_t-1' -t -1 --rMin -1 --setParameters $UNMASK_SR,BR=0 --dry-run
fi

if [ $1 -eq 3 ]; then
  mkdir -p "impact_morphed_mH90"
  cd "impact_morphed_mH90"
  combine -M MultiDimFit -n _initialFit_Test --algo singles -m 90 -d $WORK_SPACE_DIR_90 --saveWorkspace --robustFit 1 --robustHesse 1 --setParameters $PARMS --verbose 3 --keepFailures --cminApproxPreFitTolerance=10 --rMin -1
  combineTool.py -M Impacts -d "higgsCombine_initialFit_Test.MultiDimFit.mH90.root" -m 90 -w w --snapshotName "MultiDimFit" --robustFit 1 --doFits --job-mode condor --setRobustFitTolerance 0.1 --stepSize 0.1 --keepFailures --cminApproxPreFitTolerance=10 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH90_t-1' -t -1 --rMin -1 --setParameters $UNMASK_SR,BR=0 --dry-run
fi

if [ $1 -eq 4 ]; then
  mkdir -p "impact_morphed_mH100"
  cd "impact_morphed_mH100"
  combine -M MultiDimFit -n _initialFit_Test --algo singles -m 100 -d $WORK_SPACE_DIR_100 --saveWorkspace --robustFit 1 --robustHesse 1 --setParameters $PARMS --verbose 3 --keepFailures --cminApproxPreFitTolerance=10 --rMin -1
  combineTool.py -M Impacts -d "higgsCombine_initialFit_Test.MultiDimFit.mH100.root" -m 100 -w w --snapshotName "MultiDimFit" --robustFit 1 --doFits --job-mode condor --setRobustFitTolerance 0.1 --stepSize 0.1 --keepFailures --cminApproxPreFitTolerance=10 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH100_t-1' -t -1 --rMin -1 --setParameters $UNMASK_SR,BR=0 --dry-run
fi

if [ $1 -eq 5 ]; then
  mkdir -p "impact_morphed_mH110"
  cd "impact_morphed_mH110"
  combine -M MultiDimFit -n _initialFit_Test --algo singles -m 110 -d $WORK_SPACE_DIR_110 --saveWorkspace --robustFit 1 --robustHesse 1 --setParameters $PARMS --verbose 3 --keepFailures --cminApproxPreFitTolerance=10 --rMin -1
  combineTool.py -M Impacts -d "higgsCombine_initialFit_Test.MultiDimFit.mH110.root" -m 110 -w w --snapshotName "MultiDimFit" --robustFit 1 --doFits --job-mode condor --setRobustFitTolerance 0.1 --stepSize 0.1 --keepFailures --cminApproxPreFitTolerance=10 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH110_t-1' -t -1 --rMin -1 --setParameters $UNMASK_SR,BR=0 --dry-run
fi

if [ $1 -eq 6 ]; then
  mkdir -p "impact_morphed_mH120"
  cd "impact_morphed_mH120"
  combine -M MultiDimFit -n _initialFit_Test --algo singles -m 120 -d $WORK_SPACE_DIR_120 --saveWorkspace --robustFit 1 --robustHesse 1 --setParameters $PARMS --verbose 3 --keepFailures --cminApproxPreFitTolerance=10 --rMin -1
  combineTool.py -M Impacts -d "higgsCombine_initialFit_Test.MultiDimFit.mH120.root" -m 120 -w w --snapshotName "MultiDimFit" --robustFit 1 --doFits --job-mode condor --setRobustFitTolerance 0.1 --stepSize 0.1 --keepFailures --cminApproxPreFitTolerance=10 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH120_t-1' -t -1 --rMin -1 --setParameters $UNMASK_SR,BR=0 --dry-run
fi

if [ $1 -eq 7 ]; then
  mkdir -p "impact_morphed_mH130"
  cd "impact_morphed_mH130"
  combine -M MultiDimFit -n _initialFit_Test --algo singles -m 130 -d $WORK_SPACE_DIR_130 --saveWorkspace --robustFit 1 --robustHesse 1 --setParameters $PARMS --verbose 3 --keepFailures --cminApproxPreFitTolerance=10 --rMin -1
  combineTool.py -M Impacts -d "higgsCombine_initialFit_Test.MultiDimFit.mH130.root" -m 130 -w w --snapshotName "MultiDimFit" --robustFit 1 --doFits --job-mode condor --setRobustFitTolerance 0.1 --stepSize 0.1 --keepFailures --cminApproxPreFitTolerance=10 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH130_t-1' -t -1 --rMin -1 --setParameters $UNMASK_SR,BR=0 --dry-run
fi

if [ $1 -eq 8 ]; then
  mkdir -p "impact_morphed_mH140"
  cd "impact_morphed_mH140"
  combine -M MultiDimFit -n _initialFit_Test --algo singles -m 140 -d $WORK_SPACE_DIR_140 --saveWorkspace --robustFit 1 --robustHesse 1 --setParameters $PARMS --verbose 3 --keepFailures --cminApproxPreFitTolerance=10 --rMin -1
  combineTool.py -M Impacts -d "higgsCombine_initialFit_Test.MultiDimFit.mH140.root" -m 140 -w w --snapshotName "MultiDimFit" --robustFit 1 --doFits --job-mode condor --setRobustFitTolerance 0.1 --stepSize 0.1 --keepFailures --cminApproxPreFitTolerance=10 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH140_t-1' -t -1 --rMin -1 --setParameters $UNMASK_SR,BR=0 --dry-run
fi

if [ $1 -eq 9 ]; then
  mkdir -p "impact_morphed_mH150"
  cd "impact_morphed_mH150"
  combine -M MultiDimFit -n _initialFit_Test --algo singles -m 150 -d $WORK_SPACE_DIR_150 --saveWorkspace --robustFit 1 --robustHesse 1 --setParameters $PARMS --verbose 3 --keepFailures --cminApproxPreFitTolerance=10 --rMin -1
  combineTool.py -M Impacts -d "higgsCombine_initialFit_Test.MultiDimFit.mH150.root" -m 150 -w w --snapshotName "MultiDimFit" --robustFit 1 --doFits --job-mode condor --setRobustFitTolerance 0.1 --stepSize 0.1 --keepFailures --cminApproxPreFitTolerance=10 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH150_t-1' -t -1 --rMin -1 --setParameters $UNMASK_SR,BR=0 --dry-run
fi

if [ $1 -eq 10 ]; then
  mkdir -p "impact_morphed_mH160"
  cd "impact_morphed_mH160"
  combine -M MultiDimFit -n _initialFit_Test --algo singles -m 160 -d $WORK_SPACE_DIR_160 --saveWorkspace --robustFit 1 --robustHesse 1 --setParameters $PARMS --verbose 3 --keepFailures --cminApproxPreFitTolerance=10 --rMin -1
  combineTool.py -M Impacts -d "higgsCombine_initialFit_Test.MultiDimFit.mH160.root" -m 160 -w w --snapshotName "MultiDimFit" --robustFit 1 --doFits --job-mode condor --setRobustFitTolerance 0.1 --stepSize 0.1 --keepFailures --cminApproxPreFitTolerance=10 --sub-opts='+singularityimage="/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el7:latest"\n+singularitybind="/cvmfs, /etc/condor, /cms, /cms_scratch, /var/lib/condor, /xrootd/store/user/bhoh"\naccounting_group=group_cms\nJobBatchName=mkCombine_impacts_mH160_t-1' -t -1 --rMin -1 --setParameters $UNMASK_SR,BR=0 --dry-run
fi
