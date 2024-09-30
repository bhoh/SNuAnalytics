cd /cms/ldap_home/bhoh/HiggsCombTool/CMSSW_10_6_4/src/
cmsenv
cd -

diffNuis=/cms/ldap_home/bhoh/HiggsCombTool/CMSSW_10_6_4/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py

python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_morphed_75.root -p BR -g plots_morphed_mH75.root
python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_morphed_80.root -p BR -g plots_morphed_mH80.root
python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_morphed_85.root -p BR -g plots_morphed_mH85.root
python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_morphed_90.root -p BR -g plots_morphed_mH90.root
python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_morphed_100.root -p BR -g plots_morphed_mH100.root
python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_morphed_110.root -p BR -g plots_morphed_mH110.root
python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_morphed_120.root -p BR -g plots_morphed_mH120.root
python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_morphed_130.root -p BR -g plots_morphed_mH130.root
python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_morphed_140.root -p BR -g plots_morphed_mH140.root
python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_morphed_150.root -p BR -g plots_morphed_mH150.root
python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnosticspull_morphed_160.root -p BR -g plots_morphed_mH160.root


#python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnostics75.root -p BR -g plots_morphed_mH75.root
#python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnostics80.root -p BR -g plots_morphed_mH80.root
#python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnostics85.root -p BR -g plots_morphed_mH85.root
#python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnostics90.root -p BR -g plots_morphed_mH90.root
#python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnostics100.root -p BR -g plots_morphed_mH100.root
#python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnostics110.root -p BR -g plots_morphed_mH110.root
#python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnostics120.root -p BR -g plots_morphed_mH120.root
#python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnostics130.root -p BR -g plots_morphed_mH130.root
#python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnostics140.root -p BR -g plots_morphed_mH140.root
#python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnostics150.root -p BR -g plots_morphed_mH150.root
#python diffNuisances.py /cms_scratch/bhoh/toys/fitDiagnostics160.root -p BR -g plots_morphed_mH160.root
