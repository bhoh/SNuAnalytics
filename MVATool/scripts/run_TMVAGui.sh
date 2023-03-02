#out_train_CHToCB_High_BDT_High_year_comb.root
#out_train_CHToCB_High_DNN_High_year_comb_Batch1000.root
#out_train_CHToCB_High_DNN_High_year_comb_Batch2000.root
#out_train_CHToCB_High_DNN_High_year_comb_Batch4000.root
#out_train_CHToCB_High_DNN_High_year_comb_Batch500.root
#out_train_CHToCB_Low_BDT_Low_year_comb.root
#out_train_CHToCB_Low_DNN_Low_year_comb_Batch1000.root
#out_train_CHToCB_Low_DNN_Low_year_comb_Batch2000.root
#out_train_CHToCB_Low_DNN_Low_year_comb_Batch4000.root
#out_train_CHToCB_Low_DNN_Low_year_comb_Batch500.root


mkdir -p TMVAClassification/plots
if [ $1 -eq 0 ]
then
    root -l -e 'TMVA::TMVAGui("out_train_CHToCB_High_DNN_High_year_comb_Batch1000.root")' | tee TMVAClassification/plots/log_$1.txt
    mv TMVAClassification/plots TMVAClassification_$1/plots
fi
if [ $1 -eq 1 ]
then
    root -l -e 'TMVA::TMVAGui("out_train_CHToCB_High_DNN_High_year_comb_Batch2000.root")' | tee TMVAClassification/plots/log_$1.txt
    mv TMVAClassification/plots TMVAClassification_$1/plots
fi
if [ $1 -eq 2 ]
then
    root -l -e 'TMVA::TMVAGui("out_train_CHToCB_High_DNN_High_year_comb_Batch4000.root")' | tee TMVAClassification/plots/log_$1.txt
    mv TMVAClassification/plots TMVAClassification_$1/plots
fi
if [ $1 -eq 3 ]
then
    root -l -e 'TMVA::TMVAGui("out_train_CHToCB_High_DNN_High_year_comb_Batch500.root")' | tee TMVAClassification/plots/log_$1.txt
    mv TMVAClassification/plots TMVAClassification_$1/plots
fi
if [ $1 -eq 4 ]
then
    root -l -e 'TMVA::TMVAGui("out_train_CHToCB_Low_DNN_Low_year_comb_Batch1000.root")' | tee TMVAClassification/plots/log_$1.txt
    mv TMVAClassification/plots TMVAClassification_$1/plots
fi
if [ $1 -eq 5 ]
then
    root -l -e 'TMVA::TMVAGui("out_train_CHToCB_Low_DNN_Low_year_comb_Batch2000.root")' | tee TMVAClassification/plots/log_$1.txt
    mv TMVAClassification/plots TMVAClassification_$1/plots
fi
if [ $1 -eq 6 ]
then
    root -l -e 'TMVA::TMVAGui("out_train_CHToCB_Low_DNN_Low_year_comb_Batch4000.root")' | tee TMVAClassification/plots/log_$1.txt
    mv TMVAClassification/plots TMVAClassification_$1/plots
fi
if [ $1 -eq 7 ]
then
    root -l -e 'TMVA::TMVAGui("out_train_CHToCB_Low_DNN_Low_year_comb_Batch500.root")' | tee TMVAClassification/plots/log_$1.txt
    mv TMVAClassification/plots TMVAClassification_$1/plots
fi


# out dated code
#if [ $1 -eq 1 ]
#then
#    mkdir -p TMVAClassification/plots
#    root -l -e 'TMVA::TMVAGui("out_root_CHToCB_2016HIPM/out_train_CHToCB_2016HIPM.root")' | tee TMVAClassification/plots/log.txt
#    mv TMVAClassification/plots TMVAClassification_CHToCB_2016HIPM/plots
#fi
#if [ $1 -eq 2 ]
#then
#    mkdir -p TMVAClassification/plots
#    root -l -e 'TMVA::TMVAGui("out_root_CHToCB_2016noHIPM/out_train_CHToCB_2016noHIPM.root")' | tee TMVAClassification/plots/log.txt
#    mv TMVAClassification/plots TMVAClassification_CHToCB_2016noHIPM/plots
#fi
#if [ $1 -eq 3 ]
#then
#    mkdir -p TMVAClassification/plots
#    root -l -e 'TMVA::TMVAGui("out_root_CHToCB_2017/out_train_CHToCB_2017.root")' | tee TMVAClassification/plots/log.txt
#    mv TMVAClassification/plots TMVAClassification_CHToCB_2017/plots
#fi
#if [ $1 -eq 4 ]
#then
#    mkdir -p TMVAClassification/plots
#    root -l -e 'TMVA::TMVAGui("out_root_CHToCB_2018/out_train_CHToCB_2018.root")' | tee TMVAClassification/plots/log.txt
#    mv TMVAClassification/plots TMVAClassification_CHToCB_2018/plots
#fi
#if [ $1 -eq 5 ]
#then
#    mkdir -p TMVAClassification/plots
#    root -l -e 'TMVA::TMVAGui("out_root_CHToCB_year_comb/out_train_CHToCB_year_comb.root")' | tee TMVAClassification/plots/log.txt
#    mv TMVAClassification/plots TMVAClassification_CHToCB_year_comb/plots
#fi
