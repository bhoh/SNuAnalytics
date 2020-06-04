##http://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/

CURDIR=`pwd`
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_2_13
cd CMSSW_10_2_13/src
cmsenv
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
cd HiggsAnalysis/CombinedLimit

cd $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit
git fetch origin
git checkout v8.0.1
scramv1 b clean; scramv1 b # always make a clean build

git clone git@github.com:soarnsoar/ToolsForHiggsCombine.git
git clone git@github.com:soarnsoar/HiggsCombinePhysicsModel.git python//HiggsCombinePhysicsModel 
wget https://raw.githubusercontent.com/cms-analysis/HiggsAnalysis-CombinedLimit/81x-root606/test/diffNuisances.py                                                 

cd $CMSSW_BASE/src/
##http://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/nonstandard/
bash <(curl -s https://raw.githubusercontent.com/cms-analysis/CombineHarvester/master/CombineTools/scripts/sparse-checkout-ssh.sh)


cd $CURDIR
