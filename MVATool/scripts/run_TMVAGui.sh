
if [ $1 -eq 1 ]
then
    mkdir -p TMVAClassification/plots
    root -l -e 'TMVA::TMVAGui("out_root_CHToCB_Low_2016/out_train_CHToCB_Low_2016.root")' | tee TMVAClassification/plots/log.txt
    mv TMVAClassification/plots TMVAClassification_CHToCB_Low_2016/plots
fi
if [ $1 -eq 2 ]
then
    mkdir -p TMVAClassification/plots
    root -l -e 'TMVA::TMVAGui("out_root_CHToCB_High_2016/out_train_CHToCB_High_2016.root")' | tee TMVAClassification/plots/log.txt
    mv TMVAClassification/plots TMVAClassification_CHToCB_High_2016/plots
fi
if [ $1 -eq 3 ]
then
    mkdir -p TMVAClassification/plots
    root -l -e 'TMVA::TMVAGui("out_root_CHToCB_Low_2017/out_train_CHToCB_Low_2017.root")' | tee TMVAClassification/plots/log.txt
    mv TMVAClassification/plots TMVAClassification_CHToCB_Low_2017/plots
fi
if [ $1 -eq 4 ]
then
    mkdir -p TMVAClassification/plots
    root -l -e 'TMVA::TMVAGui("out_root_CHToCB_High_2017/out_train_CHToCB_High_2017.root")' | tee TMVAClassification/plots/log.txt
    mv TMVAClassification/plots TMVAClassification_CHToCB_High_2017/plots
fi
if [ $1 -eq 5 ]
then
    mkdir -p TMVAClassification/plots
    root -l -e 'TMVA::TMVAGui("out_root_CHToCB_Low_2018/out_train_CHToCB_Low_2018.root")' | tee TMVAClassification/plots/log.txt
    mv TMVAClassification/plots TMVAClassification_CHToCB_Low_2018/plots
fi
if [ $1 -eq 6 ]
then
    mkdir -p TMVAClassification/plots
    root -l -e 'TMVA::TMVAGui("out_root_CHToCB_High_2018/out_train_CHToCB_High_2018.root")' | tee TMVAClassification/plots/log.txt
    mv TMVAClassification/plots TMVAClassification_CHToCB_High_2018/plots
fi
