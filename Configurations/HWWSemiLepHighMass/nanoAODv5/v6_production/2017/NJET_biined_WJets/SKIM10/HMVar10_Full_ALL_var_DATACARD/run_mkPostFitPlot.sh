##eleCH__BoostedGGF__SR__METOver40__PtOverM04__MEKDTAG
path_fitdiagonostics=/cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Combinato/HighMassH/example/lnJ_HP45_nom_mass/fitDiagnosticsworkspace.root
InputFile=rootFile_2017_Boosted_SKIM10_HMVar10_Fullvar_GGF_SR/hadd.root
OutputFile=postfit_test.root
structureFile=MassPoints/structure_M1000_ele.py
common_opt_b=" --pycfg=configuration_Boosted_GGF_SR.py --inputFileCombine=${path_fitdiagonostics} --outputFile="$OutputFile"  --inputFile="$InputFile"  --structureFile=$structureFile  --cutNameInOriginal=""  --kind=b  --getSignalFromPrefit=1"

mkPostFitPlot.py $common_opt_b --cut=eleCH__BoostedGGF__SR__METOver40__PtOverM04__MEKDTAG  --variable=lnJ_HP45_nom_mass
