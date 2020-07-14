##input = datacard.txt
#text2workspace.py $1 -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalarSemilepNoI:GGFONLY --mass 1000
#text2workspace.py $1 -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalarSemilep:GGFONLY --mass 1000
mkdir -p logs/
##--overall
#text2workspace.py $1 -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalar:XWW$2 --mass $2 -o M$2.root &> logs/make_workspace_M$2.log&
text2workspace.py $1 -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalar:XWW$2 -o M$2.root &> logs/make_workspace_M$2.log&
text2workspace.py $1 -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalar:XWW$2 -o M${2}_NoI.root --PO KillInterference &> logs/make_workspace_M${2}_NoI.log&


#text2workspace.py $1 -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalarSemilep:FLOATINGFVBF_NoI --mass 1000 --out="$1_NoI.root"
