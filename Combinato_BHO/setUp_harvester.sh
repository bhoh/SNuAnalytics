
pushd .
cd /cms/ldap_home/bhoh/HiggsCombTool
cd CMSSW_10_6_4/src
cmsenv
#git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
## IMPORTANT: Checkout the recommended tag on the link above
#git clone https://github.com/cms-analysis/CombineHarvester.git CombineHarvester
scram b

popd
