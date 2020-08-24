#combine workspace.root --mass 1000 --name workspace -M FitDiagnostics --cminDefaultMinimizerStrategy 0
#combine_M1000_2017.root


##--default
combine $1 --mass 1000 --name default -M FitDiagnostics --saveShapes --plots --saveWithUncertainties &> run_fitdiagnosis_default.log&

##--robust
combine $1 --mass 1000 --name robust -M FitDiagnostics --saveShapes --plots --saveWithUncertainties --robustFit=1 &> run_fitdiagnosis_robust.log&
##--Minuit2,
combine $1 --mass 1000 --name Minuit2 -M FitDiagnostics --saveShapes --plots --saveWithUncertainties --cminFallbackAlgo Minuit2,1:0.1 &> run_fitdiagnosis_Minuit2.log&
##--GSLMultiMin,BFGS2,1
combine $1 --mass 1000 --name GSLMultiMin_BFGS2 -M FitDiagnostics --saveShapes --plots --saveWithUncertainties --cminFallbackAlgo GSLMultiMin,BFGS2,1:0.1 &> run_fitdiagnosis_GSLMultiMin_BFGS2.log&

##Minuit2,Simplex,1:0.1
combine $1 --mass 1000 --name GSLMultiMin_Minuit2_Simplex -M FitDiagnostics --saveShapes --plots --saveWithUncertainties --cminFallbackAlgo Minuit2,Simplex,1:0.1 &> run_fitdiagnosis_Minuit2_Simplex.log&
#####-->gives postfit shape
##TODO
#--saveOverallShapes


##--option for retring fit
##--cminFallbackAlgo Minuit2,1:0.1 
####here, 0.1 : tolerance
###1 : strategy.
#--cminFallbackAlgo GSLMultiMin,BFGS2,1:0.1
#----cminFallbackAlgo Minuit2,1:0.1
