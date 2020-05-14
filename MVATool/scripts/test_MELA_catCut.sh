
# To make the tree for MELA cut study
#python test_MELA_catCut.py
#python test_MELA_catCut.py | tee log.txt

# Copy MELA cut tree which is the output of TMVA cuts
#scp -r kistiUi20:Latino/CMSSW10215pch2/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/nAODv5v6_MVA/Out_Roots .
#scp -r kistiUi20:Latino/CMSSW10215pch2/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/nAODv5v6_MVA/Logs .

#datevalue=$(date +%F)
#echo $datevalue
#mv TMVAClassification TMVAClassification_$datevalue
#mkdir -p TMVAClassification/plots

root -l 'mvaeffscxxMod.C("","Out_Roots/out_train_2017_Bst_Pggfh1500_GgfM1000vsEW0p1.root",50,0.01)'
