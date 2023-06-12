
#WORK_SPACE_DIR=../../workspace/Asym_fitted_dijet_M_high_DNN_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR=../../workspace/Asym_fitted_dijet_M_high/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR=../../workspace/Asym_Event/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR=../../workspace/Asym_fitted_dijet_M_high_Event/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR=../../workspace/Asym_DNN_mass_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root
#WORK_SPACE_DIR=../../workspace/Asym_fitted_dijet_M_high_noPassKF/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root
#WORK_SPACE_DIR=../../workspace/Asym_fitted_dijet_M_high/M080_yieldY2018.txt.root
SNAPSHOT_DIR=higgsCombine_initialFit_Test.MultiDimFit.mH150.root

# options used before 
# --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2 -t -1
# --setParameters mask_Y2016HIPM__sng_4j_eleCH_3b=1,mask_Y2016HIPM__sng_4j_muCH_3b=1,mask_Y2017__sng_4j_eleCH_3b=1,mask_Y2017__sng_4j_muCH_3b=1,mask_Y2018__sng_4j_eleCH_3b=1,mask_Y2018__sng_4j_muCH_3b=1 
#--freezeNuisanceGroups autoMCStats
# initial fit.  search NLL crossing
#--expectSignal 0.1 -t -1 

#muon only
#MASK1='mask_Y2016HIPM__sng_4j_eleCH_3b=1,mask_Y2016HIPM__sng_4j_muCH_3b=0,mask_Y2017__sng_4j_eleCH_3b=1,mask_Y2017__sng_4j_muCH_3b=0,mask_Y2018__sng_4j_eleCH_3b=1,mask_Y2018__sng_4j_muCH_3b=0,mask_Y2016HIPM__dbl_4j_ee=1,mask_Y2016HIPM__dbl_4j_mm=0,mask_Y2017__dbl_4j_ee=1,mask_Y2017__dbl_4j_mm=0,mask_Y2018__dbl_4j_ee=1,mask_Y2018__dbl_4j_mm=0,mask_Y2016HIPM__dbl_4j_em=1,mask_Y2017__dbl_4j_em=1,mask_Y2018__dbl_4j_em=1,mask_Y2018__dbl_4j_me=1,mask_Y2017__dbl_4j_me=1,mask_Y2016HIPM__dbl_4j_me=1,mask_Y2016HIPM__sng_4j_eleCH_2b=1,mask_Y2016HIPM__sng_4j_muCH_2b=0,mask_Y2017__sng_4j_eleCH_2b=1,mask_Y2017__sng_4j_muCH_2b=0,mask_Y2018__sng_4j_eleCH_2b=1,mask_Y2018__sng_4j_muCH_2b=0'
#electron only
#MASK1='mask_Y2016HIPM__sng_4j_eleCH_3b=0,mask_Y2016HIPM__sng_4j_muCH_3b=1,mask_Y2017__sng_4j_eleCH_3b=0,mask_Y2017__sng_4j_muCH_3b=1,mask_Y2018__sng_4j_eleCH_3b=0,mask_Y2018__sng_4j_muCH_3b=1,mask_Y2016HIPM__dbl_4j_ee=0,mask_Y2016HIPM__dbl_4j_mm=1,mask_Y2017__dbl_4j_ee=0,mask_Y2017__dbl_4j_mm=1,mask_Y2018__dbl_4j_ee=0,mask_Y2018__dbl_4j_mm=1,mask_Y2016HIPM__dbl_4j_em=1,mask_Y2017__dbl_4j_em=1,mask_Y2018__dbl_4j_em=1,mask_Y2018__dbl_4j_me=1,mask_Y2017__dbl_4j_me=1,mask_Y2016HIPM__dbl_4j_me=1,mask_Y2016HIPM__sng_4j_eleCH_2b=0,mask_Y2016HIPM__sng_4j_muCH_2b=1,mask_Y2017__sng_4j_eleCH_2b=0,mask_Y2017__sng_4j_muCH_2b=1,mask_Y2018__sng_4j_eleCH_2b=0,mask_Y2018__sng_4j_muCH_2b=1'
# muon and electron (em me not included. eff_ele and eff_mu are not merged into eff_lepton)
PARMS='BR=0.001,ttbbXsec=1.2,ttccXsec=1.2'
PARMS1='BR=0.01,ttbbXsec=1.2,ttccXsec=1.2,mask_Y2016HIPM__sng_4j_eleCH_3b=0,mask_Y2016HIPM__sng_4j_muCH_3b=0,mask_Y2017__sng_4j_eleCH_3b=0,mask_Y2017__sng_4j_muCH_3b=0,mask_Y2018__sng_4j_eleCH_3b=0,mask_Y2018__sng_4j_muCH_3b=0,mask_Y2016HIPM__dbl_4j_ee=0,mask_Y2016HIPM__dbl_4j_mm=0,mask_Y2017__dbl_4j_ee=0,mask_Y2017__dbl_4j_mm=0,mask_Y2018__dbl_4j_ee=0,mask_Y2018__dbl_4j_mm=0,mask_Y2016HIPM__dbl_4j_em=0,mask_Y2017__dbl_4j_em=0,mask_Y2018__dbl_4j_em=0,mask_Y2018__dbl_4j_me=0,mask_Y2017__dbl_4j_me=0,mask_Y2016HIPM__dbl_4j_me=0,mask_Y2016HIPM__sng_4j_eleCH_2b=0,mask_Y2016HIPM__sng_4j_muCH_2b=0,mask_Y2017__sng_4j_eleCH_2b=0,mask_Y2017__sng_4j_muCH_2b=0,mask_Y2018__sng_4j_eleCH_2b=0,mask_Y2018__sng_4j_muCH_2b=0'
# no SR
PARMS2='BR=0.01,ttbbXsec=1.2,ttccXsec=1.2,mask_Y2016HIPM__sng_4j_eleCH_3b=1,mask_Y2016HIPM__sng_4j_muCH_3b=1,mask_Y2016noHIPM__sng_4j_eleCH_3b=1,mask_Y2016noHIPM__sng_4j_muCH_3b=1,mask_Y2017__sng_4j_eleCH_3b=1,mask_Y2017__sng_4j_muCH_3b=1,mask_Y2018__sng_4j_eleCH_3b=1,mask_Y2018__sng_4j_muCH_3b=1,mask_Y2016HIPM__dbl_4j_ee=0,mask_Y2016HIPM__dbl_4j_mm=0,mask_Y2016noHIPM__dbl_4j_ee=0,mask_Y2016noHIPM__dbl_4j_mm=0,mask_Y2017__dbl_4j_ee=0,mask_Y2017__dbl_4j_mm=0,mask_Y2018__dbl_4j_ee=0,mask_Y2018__dbl_4j_mm=0,mask_Y2016HIPM__dbl_4j_em=0,mask_Y2016noHIPM__dbl_4j_em=0,mask_Y2017__dbl_4j_em=0,mask_Y2018__dbl_4j_em=0,mask_Y2018__dbl_4j_me=0,mask_Y2017__dbl_4j_me=0,mask_Y2016HIPM__dbl_4j_me=0,mask_Y2016HIPM__sng_4j_eleCH_2b=0,mask_Y2016HIPM__sng_4j_muCH_2b=0,mask_Y2016noHIPM__dbl_4j_me=0,mask_Y2016noHIPM__sng_4j_eleCH_2b=0,mask_Y2016noHIPM__sng_4j_muCH_2b=0,mask_Y2017__sng_4j_eleCH_2b=0,mask_Y2017__sng_4j_muCH_2b=0,mask_Y2018__sng_4j_eleCH_2b=0,mask_Y2018__sng_4j_muCH_2b=0'
# no SR CR2
PARMS3='BR=0.01,ttbbXsec=1.2,ttccXsec=1.2,mask_Y2016HIPM__sng_4j_eleCH_3b=1,mask_Y2016HIPM__sng_4j_muCH_3b=1,mask_Y2016noHIPM__sng_4j_eleCH_3b=1,mask_Y2016noHIPM__sng_4j_muCH_3b=1,mask_Y2017__sng_4j_eleCH_3b=1,mask_Y2017__sng_4j_muCH_3b=1,mask_Y2018__sng_4j_eleCH_3b=1,mask_Y2018__sng_4j_muCH_3b=1,mask_Y2016HIPM__dbl_4j_ee=1,mask_Y2016HIPM__dbl_4j_mm=1,mask_Y2016noHIPM__dbl_4j_ee=1,mask_Y2016noHIPM__dbl_4j_mm=1,mask_Y2017__dbl_4j_ee=1,mask_Y2017__dbl_4j_mm=1,mask_Y2018__dbl_4j_ee=1,mask_Y2018__dbl_4j_mm=1,mask_Y2016HIPM__dbl_4j_em=1,mask_Y2016noHIPM__dbl_4j_em=1,mask_Y2017__dbl_4j_em=1,mask_Y2018__dbl_4j_em=1,mask_Y2018__dbl_4j_me=1,mask_Y2017__dbl_4j_me=1,mask_Y2016HIPM__dbl_4j_me=1,mask_Y2016HIPM__sng_4j_eleCH_2b=0,mask_Y2016HIPM__sng_4j_muCH_2b=0,mask_Y2016noHIPM__dbl_4j_me=1,mask_Y2016noHIPM__sng_4j_eleCH_2b=0,mask_Y2016noHIPM__sng_4j_muCH_2b=0,mask_Y2017__sng_4j_eleCH_2b=0,mask_Y2017__sng_4j_muCH_2b=0,mask_Y2018__sng_4j_eleCH_2b=0,mask_Y2018__sng_4j_muCH_2b=0'
# no CR2
PARMS4='BR=0.001,ttbbXsec=1.2,ttccXsec=1.2,mask_Y2016HIPM__sng_4j_eleCH_3b=0,mask_Y2016HIPM__sng_4j_muCH_3b=0,mask_Y2016noHIPM__sng_4j_eleCH_3b=0,mask_Y2016noHIPM__sng_4j_muCH_3b=0,mask_Y2017__sng_4j_eleCH_3b=0,mask_Y2017__sng_4j_muCH_3b=0,mask_Y2018__sng_4j_eleCH_3b=0,mask_Y2018__sng_4j_muCH_3b=0,mask_Y2016HIPM__dbl_4j_ee=1,mask_Y2016HIPM__dbl_4j_mm=1,mask_Y2016noHIPM__dbl_4j_ee=1,mask_Y2016noHIPM__dbl_4j_mm=1,mask_Y2017__dbl_4j_ee=1,mask_Y2017__dbl_4j_mm=1,mask_Y2018__dbl_4j_ee=1,mask_Y2018__dbl_4j_mm=1,mask_Y2016HIPM__dbl_4j_em=1,mask_Y2016noHIPM__dbl_4j_em=1,mask_Y2017__dbl_4j_em=1,mask_Y2018__dbl_4j_em=1,mask_Y2018__dbl_4j_me=1,mask_Y2017__dbl_4j_me=1,mask_Y2016HIPM__dbl_4j_me=1,mask_Y2016HIPM__sng_4j_eleCH_2b=0,mask_Y2016HIPM__sng_4j_muCH_2b=0,mask_Y2016noHIPM__dbl_4j_me=1,mask_Y2016noHIPM__sng_4j_eleCH_2b=0,mask_Y2016noHIPM__sng_4j_muCH_2b=0,mask_Y2017__sng_4j_eleCH_2b=0,mask_Y2017__sng_4j_muCH_2b=0,mask_Y2018__sng_4j_eleCH_2b=0,mask_Y2018__sng_4j_muCH_2b=0'


# no CR1
PARMS4='BR=0.001,ttbbXsec=1.2,ttccXsec=1.2,mask_Y2016HIPM__sng_4j_eleCH_3b=0,mask_Y2016HIPM__sng_4j_muCH_3b=0,mask_Y2016noHIPM__sng_4j_eleCH_3b=0,mask_Y2016noHIPM__sng_4j_muCH_3b=0,mask_Y2017__sng_4j_eleCH_3b=0,mask_Y2017__sng_4j_muCH_3b=0,mask_Y2018__sng_4j_eleCH_3b=0,mask_Y2018__sng_4j_muCH_3b=0,mask_Y2016HIPM__dbl_4j_ee=0,mask_Y2016HIPM__dbl_4j_mm=0,mask_Y2016noHIPM__dbl_4j_ee=0,mask_Y2016noHIPM__dbl_4j_mm=0,mask_Y2017__dbl_4j_ee=0,mask_Y2017__dbl_4j_mm=0,mask_Y2018__dbl_4j_ee=0,mask_Y2018__dbl_4j_mm=0,mask_Y2016HIPM__dbl_4j_em=0,mask_Y2016noHIPM__dbl_4j_em=0,mask_Y2017__dbl_4j_em=0,mask_Y2018__dbl_4j_em=0,mask_Y2018__dbl_4j_me=0,mask_Y2017__dbl_4j_me=0,mask_Y2016HIPM__dbl_4j_me=0,mask_Y2016HIPM__sng_4j_eleCH_2b=1,mask_Y2016HIPM__sng_4j_muCH_2b=1,mask_Y2016noHIPM__dbl_4j_me=0,mask_Y2016noHIPM__sng_4j_eleCH_2b=1,mask_Y2016noHIPM__sng_4j_muCH_2b=1,mask_Y2017__sng_4j_eleCH_2b=1,mask_Y2017__sng_4j_muCH_2b=1,mask_Y2018__sng_4j_eleCH_2b=1,mask_Y2018__sng_4j_muCH_2b=1'
# no SR DATA
PARMS5='mask_Y2016HIPM__sng_4j_eleCH_3b=1,mask_Y2016HIPM__sng_4j_muCH_3b=1,mask_Y2016noHIPM__sng_4j_eleCH_3b=1,mask_Y2016noHIPM__sng_4j_muCH_3b=1,mask_Y2017__sng_4j_eleCH_3b=1,mask_Y2017__sng_4j_muCH_3b=1,mask_Y2018__sng_4j_eleCH_3b=1,mask_Y2018__sng_4j_muCH_3b=1,mask_Y2016HIPM__dbl_4j_ee=0,mask_Y2016HIPM__dbl_4j_mm=0,mask_Y2016noHIPM__dbl_4j_ee=0,mask_Y2016noHIPM__dbl_4j_mm=0,mask_Y2017__dbl_4j_ee=0,mask_Y2017__dbl_4j_mm=0,mask_Y2018__dbl_4j_ee=0,mask_Y2018__dbl_4j_mm=0,mask_Y2016HIPM__dbl_4j_em=0,mask_Y2016noHIPM__dbl_4j_em=0,mask_Y2017__dbl_4j_em=0,mask_Y2018__dbl_4j_em=0,mask_Y2018__dbl_4j_me=0,mask_Y2017__dbl_4j_me=0,mask_Y2016HIPM__dbl_4j_me=0,mask_Y2016HIPM__sng_4j_eleCH_2b=0,mask_Y2016HIPM__sng_4j_muCH_2b=0,mask_Y2016noHIPM__dbl_4j_me=0,mask_Y2016noHIPM__sng_4j_eleCH_2b=0,mask_Y2016noHIPM__sng_4j_muCH_2b=0,mask_Y2017__sng_4j_eleCH_2b=0,mask_Y2017__sng_4j_muCH_2b=0,mask_Y2018__sng_4j_eleCH_2b=0,mask_Y2018__sng_4j_muCH_2b=0'

# step 1
#combineTool.py -M Impacts -d $WORK_SPACE_DIR -m 150  --doInitialFit --robustFit 1 --verbose 3 --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --cminDefaultMinimizerTolerance=0.01 --setParameters $PARMS --rMin -1 -t -1

# step 2
#combineTool.py -M Impacts -d $WORK_SPACE_DIR -m 150  --robustFit 1  --doFits --verbose 3 --job-mode condor --prefix-file ../job_prefix.txt --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --sub-opts='accounting_group=group_cms\nJobBatchName=mkCombine_impacts_t-1' --setParameters $PARMS  --rMin -1 -t -1


# step 3
combineTool.py -M Impacts -d $WORK_SPACE_DIR  -m 150 -o impacts.json
#combineTool.py -M Impacts -d $WORK_SPACE_DIR  -m 150 -o impacts.json --include rgx{jes}
#combineTool.py -M Impacts -d $WORK_SPACE_DIR  -m 150 -o impacts.json --exclude rgx{^prop_bin}
plotImpacts.py -i impacts.json -o impacts
