cd /cms/ldap_home/bhoh/HiggsCombTool/CMSSW_10_6_4/src/
cmsenv
cd -

diffNuis=/cms/ldap_home/bhoh/HiggsCombTool/CMSSW_10_6_4/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py

python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_75.root -p BR -g plots_mH75.root
python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_80.root -p BR -g plots_mH80.root
python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_85.root -p BR -g plots_mH85.root
python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_90.root -p BR -g plots_mH90.root
python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_100.root -p BR -g plots_mH100.root
python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_110.root -p BR -g plots_mH110.root
python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_120.root -p BR -g plots_mH120.root
python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_130.root -p BR -g plots_mH130.root
python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_140.root -p BR -g plots_mH140.root
python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_150.root -p BR -g plots_mH150.root
python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_160.root -p BR -g plots_mH160.root
