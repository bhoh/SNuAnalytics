##http://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/nonstandard/

combineTool.py -M Impacts -d datacard.root -m 1000 --doInitialFit --robustFit 1


combineTool.py -M Impacts -d datacard.root -m 1000 --robustFit 1 --doFits


combineTool.py -M Impacts -d datacard.root -m 1000 -o impacts.json


plotImpacts.py -i impacts.json -o impacts --blind
