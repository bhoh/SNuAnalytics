

#python doCombi.py -Year='2017'
#python doCombi.py -Year='2017' -Cuts 3b
#python doCombi.py -Year='2017' -Ch Mu
#python doCombi.py -Year='2017' -Ch Mu -Cuts 2b
#python doCombi.py -Year='2017' -Cuts 2b
#python doCombi.py -Year='2017'
#./mkCombiPlot.py

#python doCombi.py -Year='All' -combineCards -text2workspace
# --rAbsAcc arg (=0.00050000000000000001)
# --rRelAcc arg (=0.0050000000000000001)
#python doCombi.py -Year='All' -options='--run blind --rAbsAcc 0.1 --rRelAcc 0.005000000000000001'
#python doCombi.py -Year='All' -options='-t -1 --rAbsAcc 0.1 --rRelAcc 0.005000000000000001'
#python doCombi.py -Year='All' -M='FitDiagnostics' -options='--plots --saveShapes --saveWithUncertainties --saveOverallShapes --cminPreScan --cminPreFit 1' -combineCards -text2workspace
#python doCombi.py -Year='All' -M='FitDiagnostics' -options='--plots --saveShapes --saveWithUncertainties --saveOverallShapes --cminPreScan --cminPreFit 1' -text2workspace
#python doCombi.py -Year='All' -M='FitDiagnostics' -options='--plots --saveShapes --saveWithUncertainties --saveOverallShapes --cminPreScan --cminPreFit 1'
#
# -- making snapshot
#
#python doCombi.py -Year='All' -M='MultiDimFit' -options='--saveWorkspace --algo fixed --fixedPointPOIs BR=0 --cminPreScan --verbose 9'
#python doCombi.py -Year='All' -options='--rAbsAcc 0 --rRelAcc 0.005000000000000001 --cminPreScan --cminPreFit 1 --verbose 9'
#python doCombi.py -Year='All' -options='--rRelAcc 0.005000000000000001 --cminPreScan --cminPreFit 100 -t 3' 
#python doCombi.py -Year='All' -options='--rAbsAcc 0 --rRelAcc 0.005000000000000001 --cminPreScan --cminPreFit 1 --verbose 9 --minosAlgo minos'
#python doCombi.py -Year='All' -options='-t -1 --rAbsAcc 0 --rRelAcc 0.005000000000000001 --cminPreScan --cminPreFit 1 ' -snapshot
#
# -- pre-fit expectation and significance
#
#python doCombi.py -Year='All' -options='-t -1 --rAbsAcc 0 --rRelAcc 0.005000000000000001 --cminPreScan --cminPreFit 2 --minosAlgo bisection --verbose 4 '
#python doCombi.py -Year='All' -options='-t -1 --rAbsAcc 0 --rRelAcc 0.005000000000000001 --cminPreScan --cminPreFit 1 --setParameters BR10ToMinus7=0.01'
#python doCombi.py -Year='All' -options='-t -1 --cminPreScan  --freezeNuisanceGroups theory,experimental,autoMCStats --minosAlgo new'
#python doCombi.py -Year='All' -Ch='sngCH' -options='--cminPreScan --rAbsAcc 0 --rRelAcc 0.005000000000000001 --minosAlgo bisection' -combineCards -text2workspace
#python doCombi.py -Year='All' -Ch='All' -options='--cminPreScan --rAbsAcc 0 --rRelAcc 0.005000000000000001 --minosAlgo bisection' -combineCards -text2workspace
#python doCombi.py -Year='All' -Ch='All' -options='--cminPreScan --rAbsAcc 0 --rRelAcc 0.005000000000000001 --minosAlgo bisection' -text2workspace
python doCombi.py -Year='All' -options='--cminPreScan --rAbsAcc 0 --rRelAcc 0.005000000000000001 --minosAlgo bisection'  -combineCards
#python doCombi.py -Year='All' -options='--cminPreScan --rAbsAcc 0 --rRelAcc 0.005000000000000001 --minosAlgo bisection' -combineCards -text2workspace
#python doCombi.py -Year='All' -options='-t -1 --cminPreScan --rAbsAcc 0 --rRelAcc 0.005000000000000001 --minosAlgo bisection'
#
# -- likilhood scan
#
#python doCombi.py -Year='All' -M='MultiDimFit' -options='--algo grid --autoRange 0.05 --points 100 --setParameterRanges BR=0,0.1  --alignEdges 1 --robustFit=1 --stepSize 0.5 --cminPreScan  --verbose 9 --saveNLL' 
#python doCombi.py -Year='All' -M='HybridNew' -options='--LHCmode LHC-limits  --singlePoint 0.005 --saveToys --saveHybridResult --searchAlgo logSecant --cminPreScan --cminPreFit 1 --X-rtd MINIMIZER_MaxCalls=1000000 --cminDefaultMinimizerTolerance 0.1 --cminDefaultMinimizerType GSLMultiMin --cminDefaultMinimizerAlgo BFGS2 --cminFallbackAlgo Minuit2,Simplex,1:0.1 --rMin 0 --verbose 4  '
#python doCombi.py -Year='All' -options='--cminPreScan --cminPreFit 2 --cminDefaultMinimizerTolerance 1.0  --cminFallbackAlgo Minuit2,1:1.0  --X-rtd MINIMIZER_MaxCalls=9999999 --verbose 2 --freezeNuisanceGroups theory,experimental  --minosAlgo bisection --rAbsAcc 0 --rRelAcc 0.005000000000000001 '
#python doCombi.py -Year='All' -M='GenerateOnly' -options='--saveWorkspace --algo fixed --fixedPointPOIs BR=0 --cminPreScan --verbose 9'

