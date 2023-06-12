#!/bin/sh
ulimit -s unlimited
set -e
cd /cms/ldap_home/bhoh/HiggsCombTool/CMSSW_10_6_4/src
export SCRAM_ARCH=slc7_amd64_gcc820
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd /cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/impact/210312_t-1

if [ $1 -eq 0 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_HEMIssue --algo impact --redefineSignalPOIs BR -P CMS_HEMIssue --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 1 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_LHEPdfAlphaS --algo impact --redefineSignalPOIs BR -P CMS_LHEPdfAlphaS --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 2 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_LHEPdfWeight --algo impact --redefineSignalPOIs BR -P CMS_LHEPdfWeight --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 3 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_PS_alphaS_fsr --algo impact --redefineSignalPOIs BR -P CMS_PS_alphaS_fsr --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 4 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_PS_alphaS_fsr_sig --algo impact --redefineSignalPOIs BR -P CMS_PS_alphaS_fsr_sig --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 5 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_PS_alphaS_sig_isr --algo impact --redefineSignalPOIs BR -P CMS_PS_alphaS_sig_isr --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 6 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_PS_alphaS_st_isr --algo impact --redefineSignalPOIs BR -P CMS_PS_alphaS_st_isr --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 7 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_PS_alphaS_ttbb_isr --algo impact --redefineSignalPOIs BR -P CMS_PS_alphaS_ttbb_isr --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 8 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_PS_alphaS_ttcc_isr --algo impact --redefineSignalPOIs BR -P CMS_PS_alphaS_ttcc_isr --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 9 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_PS_alphaS_ttjj_isr --algo impact --redefineSignalPOIs BR -P CMS_PS_alphaS_ttjj_isr --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 10 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_PU --algo impact --redefineSignalPOIs BR -P CMS_PU --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 11 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_QCDscale_tt --algo impact --redefineSignalPOIs BR -P CMS_QCDscale_tt --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 12 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_Top_pTreweight --algo impact --redefineSignalPOIs BR -P CMS_Top_pTreweight --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 13 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_TuneCP5 --algo impact --redefineSignalPOIs BR -P CMS_TuneCP5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 14 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_bRegCorr_2016 --algo impact --redefineSignalPOIs BR -P CMS_bRegCorr_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 15 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_bRegCorr_2017 --algo impact --redefineSignalPOIs BR -P CMS_bRegCorr_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 16 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_bRegCorr_2018 --algo impact --redefineSignalPOIs BR -P CMS_bRegCorr_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 17 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_btag_cferr1 --algo impact --redefineSignalPOIs BR -P CMS_btag_cferr1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 18 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_btag_cferr2 --algo impact --redefineSignalPOIs BR -P CMS_btag_cferr2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 19 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_btag_hf --algo impact --redefineSignalPOIs BR -P CMS_btag_hf --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 20 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_btag_hfstats1_2016a --algo impact --redefineSignalPOIs BR -P CMS_btag_hfstats1_2016a --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 21 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_btag_hfstats1_2016b --algo impact --redefineSignalPOIs BR -P CMS_btag_hfstats1_2016b --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 22 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_btag_hfstats1_2017 --algo impact --redefineSignalPOIs BR -P CMS_btag_hfstats1_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 23 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_btag_hfstats1_2018 --algo impact --redefineSignalPOIs BR -P CMS_btag_hfstats1_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 24 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_btag_hfstats2_2016a --algo impact --redefineSignalPOIs BR -P CMS_btag_hfstats2_2016a --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 25 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_btag_hfstats2_2016b --algo impact --redefineSignalPOIs BR -P CMS_btag_hfstats2_2016b --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 26 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_btag_hfstats2_2017 --algo impact --redefineSignalPOIs BR -P CMS_btag_hfstats2_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 27 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_btag_hfstats2_2018 --algo impact --redefineSignalPOIs BR -P CMS_btag_hfstats2_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 28 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_btag_lf --algo impact --redefineSignalPOIs BR -P CMS_btag_lf --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 29 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_btag_lfstats1_2016a --algo impact --redefineSignalPOIs BR -P CMS_btag_lfstats1_2016a --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 30 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_btag_lfstats1_2016b --algo impact --redefineSignalPOIs BR -P CMS_btag_lfstats1_2016b --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 31 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_btag_lfstats1_2017 --algo impact --redefineSignalPOIs BR -P CMS_btag_lfstats1_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 32 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_btag_lfstats1_2018 --algo impact --redefineSignalPOIs BR -P CMS_btag_lfstats1_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 33 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_btag_lfstats2_2016a --algo impact --redefineSignalPOIs BR -P CMS_btag_lfstats2_2016a --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 34 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_btag_lfstats2_2016b --algo impact --redefineSignalPOIs BR -P CMS_btag_lfstats2_2016b --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 35 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_btag_lfstats2_2017 --algo impact --redefineSignalPOIs BR -P CMS_btag_lfstats2_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 36 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_btag_lfstats2_2018 --algo impact --redefineSignalPOIs BR -P CMS_btag_lfstats2_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 37 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_cRegCorr_2016 --algo impact --redefineSignalPOIs BR -P CMS_cRegCorr_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 38 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_cRegCorr_2017 --algo impact --redefineSignalPOIs BR -P CMS_cRegCorr_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 39 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_cRegCorr_2018 --algo impact --redefineSignalPOIs BR -P CMS_cRegCorr_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 40 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_ele --algo impact --redefineSignalPOIs BR -P CMS_eff_ele --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 41 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_muon --algo impact --redefineSignalPOIs BR -P CMS_eff_muon --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 42 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_prefiring_2016 --algo impact --redefineSignalPOIs BR -P CMS_eff_prefiring_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 43 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_prefiring_2017 --algo impact --redefineSignalPOIs BR -P CMS_eff_prefiring_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 44 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_prefiring_2018 --algo impact --redefineSignalPOIs BR -P CMS_eff_prefiring_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 45 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_puid_2016a --algo impact --redefineSignalPOIs BR -P CMS_eff_puid_2016a --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 46 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_puid_2016b --algo impact --redefineSignalPOIs BR -P CMS_eff_puid_2016b --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 47 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_puid_2017 --algo impact --redefineSignalPOIs BR -P CMS_eff_puid_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 48 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_eff_puid_2018 --algo impact --redefineSignalPOIs BR -P CMS_eff_puid_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 49 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_hdamp --algo impact --redefineSignalPOIs BR -P CMS_hdamp --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 50 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_jer_2016 --algo impact --redefineSignalPOIs BR -P CMS_jer_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 51 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_jer_2017 --algo impact --redefineSignalPOIs BR -P CMS_jer_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 52 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_jer_2018 --algo impact --redefineSignalPOIs BR -P CMS_jer_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 53 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_jesFlavorQCD --algo impact --redefineSignalPOIs BR -P CMS_jesFlavorQCD --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 54 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_jesTotalNoFlavor --algo impact --redefineSignalPOIs BR -P CMS_jesTotalNoFlavor --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 55 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_mtop --algo impact --redefineSignalPOIs BR -P CMS_mtop --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 56 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_unclustEn_2016 --algo impact --redefineSignalPOIs BR -P CMS_unclustEn_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 57 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_unclustEn_2017 --algo impact --redefineSignalPOIs BR -P CMS_unclustEn_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 58 ]; then
  combine -M MultiDimFit -n _paramFit_Test_CMS_unclustEn_2018 --algo impact --redefineSignalPOIs BR -P CMS_unclustEn_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 59 ]; then
  combine -M MultiDimFit -n _paramFit_Test_DYNorm --algo impact --redefineSignalPOIs BR -P DYNorm --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 60 ]; then
  combine -M MultiDimFit -n _paramFit_Test_STNorm --algo impact --redefineSignalPOIs BR -P STNorm --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 61 ]; then
  combine -M MultiDimFit -n _paramFit_Test_TTVNorm --algo impact --redefineSignalPOIs BR -P TTVNorm --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 62 ]; then
  combine -M MultiDimFit -n _paramFit_Test_VVNorm --algo impact --redefineSignalPOIs BR -P VVNorm --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 63 ]; then
  combine -M MultiDimFit -n _paramFit_Test_WjNorm --algo impact --redefineSignalPOIs BR -P WjNorm --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 64 ]; then
  combine -M MultiDimFit -n _paramFit_Test_lumi_corr --algo impact --redefineSignalPOIs BR -P lumi_corr --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 65 ]; then
  combine -M MultiDimFit -n _paramFit_Test_lumi_corr_17_18 --algo impact --redefineSignalPOIs BR -P lumi_corr_17_18 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 66 ]; then
  combine -M MultiDimFit -n _paramFit_Test_lumi_uncorr_2016 --algo impact --redefineSignalPOIs BR -P lumi_uncorr_2016 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 67 ]; then
  combine -M MultiDimFit -n _paramFit_Test_lumi_uncorr_2017 --algo impact --redefineSignalPOIs BR -P lumi_uncorr_2017 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 68 ]; then
  combine -M MultiDimFit -n _paramFit_Test_lumi_uncorr_2018 --algo impact --redefineSignalPOIs BR -P lumi_uncorr_2018 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 69 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_ee_bin0 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_ee_bin0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 70 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_ee_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_ee_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 71 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_ee_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_ee_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 72 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_ee_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_ee_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 73 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_ee_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_ee_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 74 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_ee_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_ee_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 75 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_ee_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_ee_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 76 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_ee_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_ee_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 77 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_ee_bin6_Others --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_ee_bin6_Others --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 78 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_ee_bin6_ST --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_ee_bin6_ST --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 79 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_ee_bin6_TT+bb --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_ee_bin6_TT+bb --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 80 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_ee_bin6_TT+cc --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_ee_bin6_TT+cc --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 81 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_ee_bin6_TT+jj --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_ee_bin6_TT+jj --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 82 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_ee_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_ee_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 83 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_em_bin0 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_em_bin0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 84 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_em_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_em_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 85 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_em_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_em_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 86 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_em_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_em_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 87 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_em_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_em_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 88 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_em_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_em_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 89 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_em_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_em_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 90 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_em_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_em_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 91 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_em_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_em_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 92 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_em_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_em_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 93 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_me_bin0 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_me_bin0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 94 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_me_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_me_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 95 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_me_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_me_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 96 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_me_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_me_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 97 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_me_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_me_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 98 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_me_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_me_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 99 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_me_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_me_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 100 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_me_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_me_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 101 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_me_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_me_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 102 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_me_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_me_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 103 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_mm_bin0 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_mm_bin0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 104 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_mm_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_mm_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 105 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_mm_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_mm_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 106 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_mm_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_mm_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 107 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_mm_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_mm_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 108 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_mm_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_mm_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 109 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_mm_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_mm_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 110 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_mm_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_mm_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 111 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_mm_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_mm_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 112 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__dbl_4j_mm_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__dbl_4j_mm_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 113 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_2b_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_2b_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 114 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_2b_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_2b_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 115 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_2b_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_2b_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 116 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_2b_bin12 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_2b_bin12 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 117 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_2b_bin13 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_2b_bin13 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 118 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_2b_bin14 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_2b_bin14 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 119 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_2b_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_2b_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 120 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_2b_bin16 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_2b_bin16 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 121 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_2b_bin17 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_2b_bin17 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 122 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_2b_bin18 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_2b_bin18 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 123 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_2b_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_2b_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 124 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_2b_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_2b_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 125 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_2b_bin4 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_2b_bin4 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 126 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_2b_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_2b_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 127 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_2b_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_2b_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 128 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_2b_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_2b_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 129 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_2b_bin8 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_2b_bin8 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 130 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_2b_bin9 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_2b_bin9 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 131 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_3b_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_3b_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 132 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_3b_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_3b_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 133 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_3b_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_3b_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 134 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_3b_bin12 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_3b_bin12 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 135 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_3b_bin13 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_3b_bin13 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 136 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_3b_bin14 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_3b_bin14 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 137 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_3b_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_3b_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 138 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_3b_bin16 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_3b_bin16 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 139 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_3b_bin17 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_3b_bin17 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 140 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_3b_bin18 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_3b_bin18 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 141 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_3b_bin19 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_3b_bin19 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 142 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_3b_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_3b_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 143 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_3b_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_3b_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 144 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_3b_bin4 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_3b_bin4 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 145 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_3b_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_3b_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 146 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_3b_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_3b_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 147 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_3b_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_3b_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 148 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_3b_bin8 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_3b_bin8 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 149 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_eleCH_3b_bin9 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_eleCH_3b_bin9 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 150 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_2b_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_2b_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 151 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_2b_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_2b_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 152 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_2b_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_2b_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 153 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_2b_bin12 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_2b_bin12 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 154 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_2b_bin13 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_2b_bin13 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 155 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_2b_bin14 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_2b_bin14 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 156 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_2b_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_2b_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 157 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_2b_bin16 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_2b_bin16 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 158 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_2b_bin17 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_2b_bin17 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 159 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_2b_bin18 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_2b_bin18 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 160 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_2b_bin19_TT+bb --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_2b_bin19_TT+bb --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 161 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_2b_bin19_TT+cc --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_2b_bin19_TT+cc --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 162 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_2b_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_2b_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 163 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_2b_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_2b_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 164 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_2b_bin4 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_2b_bin4 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 165 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_2b_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_2b_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 166 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_2b_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_2b_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 167 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_2b_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_2b_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 168 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_2b_bin8 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_2b_bin8 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 169 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_2b_bin9 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_2b_bin9 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 170 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_3b_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_3b_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 171 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_3b_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_3b_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 172 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_3b_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_3b_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 173 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_3b_bin12 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_3b_bin12 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 174 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_3b_bin13 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_3b_bin13 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 175 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_3b_bin14 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_3b_bin14 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 176 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_3b_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_3b_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 177 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_3b_bin16 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_3b_bin16 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 178 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_3b_bin17 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_3b_bin17 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 179 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_3b_bin18 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_3b_bin18 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 180 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_3b_bin19 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_3b_bin19 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 181 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_3b_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_3b_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 182 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_3b_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_3b_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 183 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_3b_bin4 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_3b_bin4 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 184 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_3b_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_3b_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 185 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_3b_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_3b_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 186 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_3b_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_3b_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 187 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_3b_bin8 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_3b_bin8 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 188 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016HIPM__sng_4j_muCH_3b_bin9 --algo impact --redefineSignalPOIs BR -P prop_binY2016HIPM__sng_4j_muCH_3b_bin9 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 189 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_ee_bin0 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_ee_bin0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 190 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_ee_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_ee_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 191 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_ee_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_ee_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 192 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_ee_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_ee_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 193 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_ee_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_ee_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 194 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_ee_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_ee_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 195 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_ee_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_ee_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 196 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_ee_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_ee_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 197 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_ee_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_ee_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 198 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_ee_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_ee_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 199 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_em_bin0 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_em_bin0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 200 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_em_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_em_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 201 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_em_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_em_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 202 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_em_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_em_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 203 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_em_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_em_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 204 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_em_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_em_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 205 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_em_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_em_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 206 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_em_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_em_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 207 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_em_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_em_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 208 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_em_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_em_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 209 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_me_bin0 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_me_bin0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 210 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_me_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_me_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 211 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_me_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_me_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 212 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_me_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_me_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 213 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_me_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_me_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 214 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_me_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_me_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 215 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_me_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_me_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 216 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_me_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_me_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 217 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_me_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_me_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 218 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_me_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_me_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 219 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_mm_bin0 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_mm_bin0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 220 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_mm_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_mm_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 221 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_mm_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_mm_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 222 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_mm_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_mm_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 223 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_mm_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_mm_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 224 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_mm_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_mm_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 225 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_mm_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_mm_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 226 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_mm_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_mm_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 227 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_mm_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_mm_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 228 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__dbl_4j_mm_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__dbl_4j_mm_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 229 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_2b_bin0_Others --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_2b_bin0_Others --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 230 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_2b_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_2b_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 231 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_2b_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_2b_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 232 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_2b_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_2b_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 233 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_2b_bin12 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_2b_bin12 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 234 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_2b_bin13 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_2b_bin13 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 235 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_2b_bin14 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_2b_bin14 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 236 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_2b_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_2b_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 237 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_2b_bin16 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_2b_bin16 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 238 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_2b_bin17 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_2b_bin17 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 239 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_2b_bin18 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_2b_bin18 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 240 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_2b_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_2b_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 241 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_2b_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_2b_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 242 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_2b_bin4 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_2b_bin4 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 243 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_2b_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_2b_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 244 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_2b_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_2b_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 245 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_2b_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_2b_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 246 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_2b_bin8 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_2b_bin8 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 247 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_2b_bin9 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_2b_bin9 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 248 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 249 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 250 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 251 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin12 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin12 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 252 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin13 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin13 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 253 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin14 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin14 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 254 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 255 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin16 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin16 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 256 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin17 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin17 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 257 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin18 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin18 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 258 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin19_CHToCB_M150 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin19_CHToCB_M150 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 259 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin19_Others --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin19_Others --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 260 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin19_TT+bb --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin19_TT+bb --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 261 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 262 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 263 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin4 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin4 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 264 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 265 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 266 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 267 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin8 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin8 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 268 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_eleCH_3b_bin9 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_eleCH_3b_bin9 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 269 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_2b_bin0_TT+jj --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_2b_bin0_TT+jj --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 270 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_2b_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_2b_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 271 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_2b_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_2b_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 272 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_2b_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_2b_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 273 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_2b_bin12 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_2b_bin12 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 274 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_2b_bin13 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_2b_bin13 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 275 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_2b_bin14 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_2b_bin14 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 276 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_2b_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_2b_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 277 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_2b_bin16 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_2b_bin16 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 278 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_2b_bin17 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_2b_bin17 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 279 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_2b_bin18 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_2b_bin18 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 280 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_2b_bin19_Others --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_2b_bin19_Others --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 281 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_2b_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_2b_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 282 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_2b_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_2b_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 283 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_2b_bin4 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_2b_bin4 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 284 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_2b_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_2b_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 285 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_2b_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_2b_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 286 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_2b_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_2b_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 287 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_2b_bin8 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_2b_bin8 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 288 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_2b_bin9 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_2b_bin9 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 289 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_3b_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_3b_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 290 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_3b_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_3b_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 291 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_3b_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_3b_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 292 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_3b_bin12 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_3b_bin12 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 293 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_3b_bin13 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_3b_bin13 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 294 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_3b_bin14 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_3b_bin14 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 295 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_3b_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_3b_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 296 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_3b_bin16 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_3b_bin16 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 297 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_3b_bin17 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_3b_bin17 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 298 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_3b_bin18 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_3b_bin18 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 299 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_3b_bin19 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_3b_bin19 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 300 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_3b_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_3b_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 301 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_3b_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_3b_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 302 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_3b_bin4 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_3b_bin4 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 303 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_3b_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_3b_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 304 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_3b_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_3b_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 305 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_3b_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_3b_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 306 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_3b_bin8 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_3b_bin8 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 307 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2016noHIPM__sng_4j_muCH_3b_bin9 --algo impact --redefineSignalPOIs BR -P prop_binY2016noHIPM__sng_4j_muCH_3b_bin9 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 308 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_ee_bin0 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_ee_bin0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 309 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_ee_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_ee_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 310 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_ee_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_ee_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 311 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_ee_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_ee_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 312 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_ee_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_ee_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 313 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_ee_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_ee_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 314 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_ee_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_ee_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 315 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_ee_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_ee_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 316 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_ee_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_ee_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 317 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_ee_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_ee_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 318 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_em_bin0 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_em_bin0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 319 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_em_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_em_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 320 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_em_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_em_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 321 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_em_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_em_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 322 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_em_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_em_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 323 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_em_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_em_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 324 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_em_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_em_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 325 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_em_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_em_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 326 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_em_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_em_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 327 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_em_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_em_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 328 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_me_bin0 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_me_bin0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 329 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_me_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_me_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 330 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_me_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_me_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 331 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_me_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_me_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 332 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_me_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_me_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 333 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_me_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_me_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 334 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_me_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_me_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 335 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_me_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_me_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 336 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_me_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_me_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 337 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_me_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_me_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 338 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_mm_bin0 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_mm_bin0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 339 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_mm_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_mm_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 340 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_mm_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_mm_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 341 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_mm_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_mm_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 342 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_mm_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_mm_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 343 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_mm_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_mm_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 344 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_mm_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_mm_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 345 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_mm_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_mm_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 346 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_mm_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_mm_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 347 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__dbl_4j_mm_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2017__dbl_4j_mm_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 348 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_2b_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_2b_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 349 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_2b_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_2b_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 350 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_2b_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_2b_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 351 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_2b_bin12 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_2b_bin12 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 352 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_2b_bin13 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_2b_bin13 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 353 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_2b_bin14 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_2b_bin14 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 354 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_2b_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_2b_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 355 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_2b_bin16 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_2b_bin16 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 356 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_2b_bin17 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_2b_bin17 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 357 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_2b_bin18 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_2b_bin18 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 358 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_2b_bin19_TT+bb --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_2b_bin19_TT+bb --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 359 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_2b_bin19_TT+jj --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_2b_bin19_TT+jj --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 360 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_2b_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_2b_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 361 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_2b_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_2b_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 362 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_2b_bin4 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_2b_bin4 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 363 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_2b_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_2b_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 364 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_2b_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_2b_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 365 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_2b_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_2b_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 366 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_2b_bin8 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_2b_bin8 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 367 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_2b_bin9 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_2b_bin9 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 368 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_3b_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_3b_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 369 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_3b_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_3b_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 370 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_3b_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_3b_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 371 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_3b_bin12 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_3b_bin12 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 372 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_3b_bin13 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_3b_bin13 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 373 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_3b_bin14 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_3b_bin14 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 374 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_3b_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_3b_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 375 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_3b_bin16 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_3b_bin16 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 376 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_3b_bin17 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_3b_bin17 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 377 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_3b_bin18 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_3b_bin18 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 378 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_3b_bin19 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_3b_bin19 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 379 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_3b_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_3b_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 380 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_3b_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_3b_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 381 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_3b_bin4 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_3b_bin4 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 382 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_3b_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_3b_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 383 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_3b_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_3b_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 384 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_3b_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_3b_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 385 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_3b_bin8 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_3b_bin8 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 386 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_eleCH_3b_bin9 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_eleCH_3b_bin9 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 387 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_2b_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_2b_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 388 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_2b_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_2b_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 389 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_2b_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_2b_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 390 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_2b_bin12 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_2b_bin12 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 391 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_2b_bin13 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_2b_bin13 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 392 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_2b_bin14 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_2b_bin14 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 393 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_2b_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_2b_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 394 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_2b_bin16 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_2b_bin16 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 395 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_2b_bin17 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_2b_bin17 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 396 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_2b_bin18 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_2b_bin18 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 397 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_2b_bin19_Others --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_2b_bin19_Others --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 398 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_2b_bin19_TT+bb --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_2b_bin19_TT+bb --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 399 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_2b_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_2b_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 400 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_2b_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_2b_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 401 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_2b_bin4 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_2b_bin4 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 402 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_2b_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_2b_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 403 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_2b_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_2b_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 404 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_2b_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_2b_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 405 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_2b_bin8 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_2b_bin8 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 406 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_2b_bin9 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_2b_bin9 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 407 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_3b_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_3b_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 408 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_3b_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_3b_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 409 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_3b_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_3b_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 410 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_3b_bin12 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_3b_bin12 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 411 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_3b_bin13 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_3b_bin13 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 412 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_3b_bin14 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_3b_bin14 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 413 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_3b_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_3b_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 414 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_3b_bin16 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_3b_bin16 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 415 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_3b_bin17 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_3b_bin17 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 416 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_3b_bin18 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_3b_bin18 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 417 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_3b_bin19 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_3b_bin19 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 418 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_3b_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_3b_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 419 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_3b_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_3b_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 420 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_3b_bin4 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_3b_bin4 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 421 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_3b_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_3b_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 422 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_3b_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_3b_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 423 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_3b_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_3b_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 424 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_3b_bin8 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_3b_bin8 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 425 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2017__sng_4j_muCH_3b_bin9 --algo impact --redefineSignalPOIs BR -P prop_binY2017__sng_4j_muCH_3b_bin9 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 426 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_ee_bin0 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_ee_bin0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 427 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_ee_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_ee_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 428 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_ee_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_ee_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 429 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_ee_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_ee_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 430 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_ee_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_ee_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 431 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_ee_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_ee_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 432 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_ee_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_ee_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 433 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_ee_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_ee_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 434 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_ee_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_ee_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 435 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_ee_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_ee_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 436 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_em_bin0 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_em_bin0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 437 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_em_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_em_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 438 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_em_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_em_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 439 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_em_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_em_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 440 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_em_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_em_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 441 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_em_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_em_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 442 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_em_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_em_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 443 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_em_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_em_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 444 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_em_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_em_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 445 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_em_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_em_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 446 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_me_bin0 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_me_bin0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 447 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_me_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_me_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 448 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_me_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_me_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 449 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_me_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_me_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 450 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_me_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_me_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 451 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_me_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_me_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 452 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_me_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_me_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 453 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_me_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_me_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 454 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_me_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_me_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 455 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_me_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_me_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 456 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_mm_bin0 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_mm_bin0 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 457 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_mm_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_mm_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 458 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_mm_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_mm_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 459 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_mm_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_mm_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 460 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_mm_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_mm_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 461 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_mm_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_mm_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 462 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_mm_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_mm_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 463 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_mm_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_mm_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 464 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_mm_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_mm_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 465 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__dbl_4j_mm_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2018__dbl_4j_mm_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 466 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 467 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 468 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 469 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin12 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin12 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 470 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin13 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin13 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 471 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin14 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin14 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 472 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 473 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin16 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin16 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 474 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin17 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin17 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 475 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin18_CHToCB_M150 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin18_CHToCB_M150 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 476 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin18_Others --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin18_Others --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 477 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin18_QCD --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin18_QCD --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 478 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin18_ST --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin18_ST --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 479 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin18_TT+bb --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin18_TT+bb --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 480 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin18_TT+cc --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin18_TT+cc --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 481 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin18_TT+jj --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin18_TT+jj --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 482 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin19_TT+bb --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin19_TT+bb --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 483 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 484 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 485 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin4 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin4 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 486 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 487 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 488 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 489 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin8 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin8 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 490 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_2b_bin9 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_2b_bin9 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 491 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_3b_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_3b_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 492 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_3b_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_3b_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 493 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_3b_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_3b_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 494 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_3b_bin12 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_3b_bin12 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 495 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_3b_bin13 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_3b_bin13 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 496 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_3b_bin14 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_3b_bin14 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 497 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_3b_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_3b_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 498 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_3b_bin16 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_3b_bin16 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 499 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_3b_bin17 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_3b_bin17 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 500 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_3b_bin18 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_3b_bin18 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 501 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_3b_bin19 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_3b_bin19 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 502 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_3b_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_3b_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 503 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_3b_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_3b_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 504 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_3b_bin4 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_3b_bin4 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 505 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_3b_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_3b_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 506 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_3b_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_3b_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 507 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_3b_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_3b_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 508 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_3b_bin8 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_3b_bin8 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 509 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_eleCH_3b_bin9 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_eleCH_3b_bin9 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 510 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_2b_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_2b_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 511 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_2b_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_2b_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 512 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_2b_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_2b_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 513 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_2b_bin12 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_2b_bin12 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 514 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_2b_bin13 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_2b_bin13 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 515 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_2b_bin14 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_2b_bin14 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 516 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_2b_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_2b_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 517 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_2b_bin16 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_2b_bin16 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 518 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_2b_bin17 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_2b_bin17 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 519 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_2b_bin18 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_2b_bin18 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 520 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_2b_bin19_TT+jj --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_2b_bin19_TT+jj --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 521 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_2b_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_2b_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 522 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_2b_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_2b_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 523 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_2b_bin4 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_2b_bin4 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 524 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_2b_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_2b_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 525 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_2b_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_2b_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 526 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_2b_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_2b_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 527 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_2b_bin8 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_2b_bin8 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 528 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_2b_bin9 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_2b_bin9 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 529 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_3b_bin1 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_3b_bin1 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 530 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_3b_bin10 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_3b_bin10 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 531 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_3b_bin11 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_3b_bin11 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 532 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_3b_bin12 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_3b_bin12 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 533 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_3b_bin13 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_3b_bin13 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 534 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_3b_bin14 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_3b_bin14 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 535 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_3b_bin15 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_3b_bin15 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 536 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_3b_bin16 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_3b_bin16 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 537 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_3b_bin17 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_3b_bin17 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 538 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_3b_bin18 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_3b_bin18 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 539 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_3b_bin19 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_3b_bin19 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 540 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_3b_bin2 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_3b_bin2 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 541 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_3b_bin3 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_3b_bin3 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 542 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_3b_bin4 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_3b_bin4 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 543 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_3b_bin5 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_3b_bin5 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 544 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_3b_bin6 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_3b_bin6 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 545 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_3b_bin7 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_3b_bin7 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 546 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_3b_bin8 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_3b_bin8 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 547 ]; then
  combine -M MultiDimFit -n _paramFit_Test_prop_binY2018__sng_4j_muCH_3b_bin9 --algo impact --redefineSignalPOIs BR -P prop_binY2018__sng_4j_muCH_3b_bin9 --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 548 ]; then
  combine -M MultiDimFit -n _paramFit_Test_qcd_norm --algo impact --redefineSignalPOIs BR -P qcd_norm --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 549 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ttXsec --algo impact --redefineSignalPOIs BR -P ttXsec --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 550 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ttbbXsec --algo impact --redefineSignalPOIs BR -P ttbbXsec --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi
if [ $1 -eq 551 ]; then
  combine -M MultiDimFit -n _paramFit_Test_ttccXsec --algo impact --redefineSignalPOIs BR -P ttccXsec --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --rMin -1 -t -1 -m 150 -d ../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2
fi