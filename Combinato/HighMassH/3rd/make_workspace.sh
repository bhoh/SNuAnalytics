##input = datacard.txt
#text2workspace.py $1 -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalarSemilepNoI:GGFONLY --mass 1000
#text2workspace.py $1 -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalarSemilep:GGFONLY --mass 1000
mkdir -p logs/
text2workspace.py $1 -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalarSemilep:FLOATINGFVBF --mass $2 -o M$2.root &> logs/make_workspace_M$2_flogting.log&
text2workspace.py $1 -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalarSemilep:GGFONLY --mass $2 -o M$2_GGFOnly.root &> logs/make_workspace_M${2}_GGFOnly.log&
text2workspace.py $1 -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalarSemilep:VBFONLY --mass $2 -o M$2_VBFOnly.root &> logs/make_workspace_M${2}_VBFOnly.log&

text2workspace.py $1 -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalarSemilep:FLOATINGFVBF_NoI --mass $2 -o M$2_NoI.root &> logs/make_workspace_M$2_flogting_NoI.log&
text2workspace.py $1 -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalarSemilep:GGFONLY_NoI --mass $2 -o M$2_GGFOnly_NoI.root &> logs/make_workspace_M${2}_GGFOnly_NoI.log&
text2workspace.py $1 -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalarSemilep:VBFONLY_NoI --mass $2 -o M$2_VBFOnly_NoI.root &> logs/make_workspace_M${2}_VBFOnly_NoI.log&

#text2workspace.py $1 -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalarSemilep:FLOATINGFVBF_NoI --mass 1000 --out="$1_NoI.root"
