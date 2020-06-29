##http://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/nonstandard/
##TODO
##-t -1  : make toy using expectation
##toy frequentist : fit to data
##-

###$1 -> workspace file
robust="--robustFit 1"
#robust=""
#opt="--cminFallbackAlgo Minuit2,Simplex,1:10" 
#opt="--cminFallbackAlgo Minuit2,Simplex,0:100"
#opt="--cminFallbackAlgo Minuit2,Migrad,0:1.0"
asimov="-t -1"
combineTool.py -M Impacts -d $1 -m 1000 --doInitialFit $robust $opt $asimov


combineTool.py -M Impacts -d $1 -m 1000 $robust --doFits $opt $asimov


combineTool.py -M Impacts -d $1 -m 1000 -o impacts.json


plotImpacts.py -i impacts.json -o impacts --blind
