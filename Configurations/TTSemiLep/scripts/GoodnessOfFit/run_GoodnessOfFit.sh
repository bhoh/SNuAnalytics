
#WORK_SPACE_DIR=../../workspace/Asym_fitted_dijet_M_high_DNN_High/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root
WORK_SPACE_DIR=../../workspace/Asym_fitted_dijet_M_high/M150Y2016noHIPMY2017Y2016HIPMY2018.txt.root
#WORK_SPACE_DIR=../../workspace/Asym_fitted_dijet_M_high/M080_yieldY2018.txt.root
SNAPSHOT_DIR=higgsCombine_initialFit_Test.MultiDimFit.mH150.root

# options used before 
# --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2 -t -1
# --setParameters mask_Y2016__sng_4j_eleCH_3b=1,mask_Y2016__sng_4j_muCH_3b=1,mask_Y2017__sng_4j_eleCH_3b=1,mask_Y2017__sng_4j_muCH_3b=1,mask_Y2018__sng_4j_eleCH_3b=1,mask_Y2018__sng_4j_muCH_3b=1 
#--freezeNuisanceGroups autoMCStats
# initial fit.  search NLL crossing
#--expectSignal 0.1 -t -1 

#muon only
#MASK1='mask_Y2016__sng_4j_eleCH_3b=1,mask_Y2016__sng_4j_muCH_3b=0,mask_Y2017__sng_4j_eleCH_3b=1,mask_Y2017__sng_4j_muCH_3b=0,mask_Y2018__sng_4j_eleCH_3b=1,mask_Y2018__sng_4j_muCH_3b=0,mask_Y2016__dbl_4j_ee=1,mask_Y2016__dbl_4j_mm=0,mask_Y2017__dbl_4j_ee=1,mask_Y2017__dbl_4j_mm=0,mask_Y2018__dbl_4j_ee=1,mask_Y2018__dbl_4j_mm=0,mask_Y2016__dbl_4j_em=1,mask_Y2017__dbl_4j_em=1,mask_Y2018__dbl_4j_em=1,mask_Y2018__dbl_4j_me=1,mask_Y2017__dbl_4j_me=1,mask_Y2016__dbl_4j_me=1,mask_Y2016__sng_4j_eleCH_2b=1,mask_Y2016__sng_4j_muCH_2b=0,mask_Y2017__sng_4j_eleCH_2b=1,mask_Y2017__sng_4j_muCH_2b=0,mask_Y2018__sng_4j_eleCH_2b=1,mask_Y2018__sng_4j_muCH_2b=0'
#electron only
#MASK1='mask_Y2016__sng_4j_eleCH_3b=0,mask_Y2016__sng_4j_muCH_3b=1,mask_Y2017__sng_4j_eleCH_3b=0,mask_Y2017__sng_4j_muCH_3b=1,mask_Y2018__sng_4j_eleCH_3b=0,mask_Y2018__sng_4j_muCH_3b=1,mask_Y2016__dbl_4j_ee=0,mask_Y2016__dbl_4j_mm=1,mask_Y2017__dbl_4j_ee=0,mask_Y2017__dbl_4j_mm=1,mask_Y2018__dbl_4j_ee=0,mask_Y2018__dbl_4j_mm=1,mask_Y2016__dbl_4j_em=1,mask_Y2017__dbl_4j_em=1,mask_Y2018__dbl_4j_em=1,mask_Y2018__dbl_4j_me=1,mask_Y2017__dbl_4j_me=1,mask_Y2016__dbl_4j_me=1,mask_Y2016__sng_4j_eleCH_2b=0,mask_Y2016__sng_4j_muCH_2b=1,mask_Y2017__sng_4j_eleCH_2b=0,mask_Y2017__sng_4j_muCH_2b=1,mask_Y2018__sng_4j_eleCH_2b=0,mask_Y2018__sng_4j_muCH_2b=1'
# muon and electron (em me not included. eff_ele and eff_mu are not merged into eff_lepton)
MASK1='mask_Y2016__sng_4j_eleCH_3b=0,mask_Y2016__sng_4j_muCH_3b=0,mask_Y2017__sng_4j_eleCH_3b=0,mask_Y2017__sng_4j_muCH_3b=0,mask_Y2018__sng_4j_eleCH_3b=0,mask_Y2018__sng_4j_muCH_3b=0,mask_Y2016__dbl_4j_ee=0,mask_Y2016__dbl_4j_mm=0,mask_Y2017__dbl_4j_ee=0,mask_Y2017__dbl_4j_mm=0,mask_Y2018__dbl_4j_ee=0,mask_Y2018__dbl_4j_mm=0,mask_Y2016__dbl_4j_em=0,mask_Y2017__dbl_4j_em=0,mask_Y2018__dbl_4j_em=0,mask_Y2018__dbl_4j_me=0,mask_Y2017__dbl_4j_me=0,mask_Y2016__dbl_4j_me=0,mask_Y2016__sng_4j_eleCH_2b=0,mask_Y2016__sng_4j_muCH_2b=0,mask_Y2017__sng_4j_eleCH_2b=0,mask_Y2017__sng_4j_muCH_2b=0,mask_Y2018__sng_4j_eleCH_2b=0,mask_Y2018__sng_4j_muCH_2b=0'
# no SR
MASK2='mask_Y2016__sng_4j_eleCH_3b=1,mask_Y2016__sng_4j_muCH_3b=1,mask_Y2017__sng_4j_eleCH_3b=1,mask_Y2017__sng_4j_muCH_3b=1,mask_Y2018__sng_4j_eleCH_3b=1,mask_Y2018__sng_4j_muCH_3b=1,mask_Y2016__dbl_4j_ee=0,mask_Y2016__dbl_4j_mm=0,mask_Y2017__dbl_4j_ee=0,mask_Y2017__dbl_4j_mm=0,mask_Y2018__dbl_4j_ee=0,mask_Y2018__dbl_4j_mm=0,mask_Y2016__dbl_4j_em=0,mask_Y2017__dbl_4j_em=0,mask_Y2018__dbl_4j_em=0,mask_Y2018__dbl_4j_me=0,mask_Y2017__dbl_4j_me=0,mask_Y2016__dbl_4j_me=0,mask_Y2016__sng_4j_eleCH_2b=0,mask_Y2016__sng_4j_muCH_2b=0,mask_Y2017__sng_4j_eleCH_2b=0,mask_Y2017__sng_4j_muCH_2b=0,mask_Y2018__sng_4j_eleCH_2b=0,mask_Y2018__sng_4j_muCH_2b=0'


# standalone test
#combineTool.py -M GoodnessOfFit -d $WORK_SPACE_DIR -m 150 --algorithm saturated --setParameters $MASK2 -t 10

# GOF test with generated toys with MR+SR
combine -M GoodnessOfFit -d $WORK_SPACE_DIR --toysFile higgsCombineTest.GenerateOnly.mH120.123456.root -m 150 --algorithm saturated --toysFrequentist -t 500

###  
#combineTool.py -M Impacts -d $WORK_SPACE_DIR -m 150  --robustFit 1  --doFits --verbose 3 --job-mode condor --prefix-file ../job_prefix.txt --setRobustFitTolerance 0.1 --stepSize 0.1 --setRobustFitStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --sub-opts='accounting_group=group_cms\nJobBatchName=mkCombine_impacts_t-1' --setParameters BR=0.001,ttbbXsec=1.2,ttccXsec=1.2 -t -1  --dry-run 
#
#combineTool.py -M Impacts -d $WORK_SPACE_DIR  -m 150 -o impacts.json
#combineTool.py -M Impacts -d $WORK_SPACE_DIR  -m 150 -o impacts.json --include rgx{jes}
#combineTool.py -M Impacts -d $WORK_SPACE_DIR  -m 150 -o impacts.json --exclude rgx{^prop_bin}
#plotImpacts.py -i impacts.json -o impacts
