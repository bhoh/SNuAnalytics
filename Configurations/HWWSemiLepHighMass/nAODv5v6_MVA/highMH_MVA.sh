
# To make the tree for MELA cut study
python highMH_MVA.py

# dont use this because the logs are saved at dedicated files in Logs dir
#python highMH_MVA.py | tee log.txt

# Copy MELA cut tree which is the output of TMVA cuts
#scp -r kistiUi20:Latino/CMSSW10215pch2/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/nAODv5v6_MVA/Out_Roots_Allp400p1500 .
#scp -r kistiUi20:Latino/CMSSW10215pch2/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/nAODv5v6_MVA/Out_Roots_kd .
#scp -r kistiUi20:Latino/CMSSW10215pch2/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/nAODv5v6_MVA/Logs .

#datevalue=$(date +%F)
#echo $datevalue
#mv TMVAClassification TMVAClassification_$datevalue
#mkdir -p TMVAClassification/plots


# for one file
#root -l 'mvaeffscxxMod.C("","Out_Roots/out_train_2017_Bst_Pggfh1500_GgfM1000vsEW0p1.root",50,0.01)'
#root -l 'mvaeffscxxMod.C("","Out_Roots/out_train_2017_Bst_Pggfh1500_GgfM1000vsVbfM1000.root",50,0.01)'

## for many files
###python mvaeffscxxMod.py

