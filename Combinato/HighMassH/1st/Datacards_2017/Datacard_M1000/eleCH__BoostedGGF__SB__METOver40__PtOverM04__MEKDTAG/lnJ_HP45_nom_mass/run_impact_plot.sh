##http://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/nonstandard/
##TODO
##-t -1  : make toy using expectation
##toy frequentist : fit to data
##-

###$1 -> workspace file
#robust="--robustFit 1"
robust=""

combineTool.py -M Impacts -d $1 -m 1000 --doInitialFit $robust


combineTool.py -M Impacts -d $1 -m 1000 $robust --doFits


combineTool.py -M Impacts -d $1 -m 1000 -o impacts.json


plotImpacts.py -i impacts.json -o impacts --blind