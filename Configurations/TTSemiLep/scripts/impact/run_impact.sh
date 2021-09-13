
WORK_SPACE_DIR=../workspace/Asym_fitted_dijet_M_DNN_Low/M120Y2017Y2016Y2018.txt.root

# --setParameters BR=0.0001 -t -1
# --setParameters mask_Y2016__sng_4j_eleCH_3b=1,mask_Y2016__sng_4j_muCH_3b=1,mask_Y2017__sng_4j_eleCH_3b=1,mask_Y2017__sng_4j_muCH_3b=1,mask_Y2018__sng_4j_eleCH_3b=1,mask_Y2018__sng_4j_muCH_3b=1 
#--freezeNuisanceGroups autoMCStats
#combineTool.py -M Impacts -d $WORK_SPACE_DIR -m 120  --doInitialFit --robustFit 1 --verbose 3 --rMax 0.01 --points 5000 --cminDefaultMinimizerType Minuit2 --cminDefaultMinimizerAlgo Combined --cminFallbackAlgo Minuit2,1:1.0 --cminApproxPreFitTolerance 0 --setParameters BR=0.0001,mask_Y2016__sng_4j_eleCH_3b=1,mask_Y2016__sng_4j_muCH_3b=1,mask_Y2017__sng_4j_eleCH_3b=1,mask_Y2017__sng_4j_muCH_3b=1,mask_Y2018__sng_4j_eleCH_3b=1,mask_Y2018__sng_4j_muCH_3b=1 
#
#
#
#combineTool.py -M Impacts -d $WORK_SPACE_DIR -m 120  --robustFit 1  --doFits   --points 5000 --verbose 3 --rMax 0.01 --cminDefaultMinimizerType Minuit2 --cminDefaultMinimizerAlgo Combined --cminFallbackAlgo Minuit2,1:1.0 --cminApproxPreFitTolerance 0  --job-mode condor --prefix-file job_prefix.txt  --setParameters BR=0.0001,mask_Y2016__sng_4j_eleCH_3b=1,mask_Y2016__sng_4j_muCH_3b=1,mask_Y2017__sng_4j_eleCH_3b=1,mask_Y2017__sng_4j_muCH_3b=1,mask_Y2018__sng_4j_eleCH_3b=1,mask_Y2018__sng_4j_muCH_3b=1 --dry-run
#sed -i '/log                   = combine_task\.\$(ClusterId)\.log/a accounting_group=group_cms' condor_combine_task.sub
#sed -i '/accounting_group=group_cms/a JobBatchName=mkCombine_impacts' condor_combine_task.sub
#condor_submit condor_combine_task.sub
#
#
#
#combineTool.py -M Impacts -d $WORK_SPACE_DIR  -m 120 -o impacts.json
#combineTool.py -M Impacts -d $WORK_SPACE_DIR  -m 120 -o impacts.json --exclude rgx{^prop_bin}
plotImpacts.py -i impacts.json -o impacts
