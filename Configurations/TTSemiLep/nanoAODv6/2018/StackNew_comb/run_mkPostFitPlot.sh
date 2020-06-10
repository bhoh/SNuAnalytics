#InputFile='rootFile_2018_SKIM5/hadd.root'
InputFile='rootFile_2018_SKIM5/PDF/results_suppressZeros.root'
InputFile_ele='rootFile_2018_SKIM5_ele/PDF/results_suppressZeros.root'
InputFile_mu='rootFile_2018_SKIM5_mu/PDF/results_suppressZeros.root'

OutputFile='rootFile_2018_SKIM5/PDF/results_PostFit_b.root'
OutputFile_ele='rootFile_2018_SKIM5/PDF/results_PostFit_b.root'
OutputFile_mu='rootFile_2018_SKIM5/PDF/results_PostFit_b.root'

OutputFile_M130to150='rootFile_2018_SKIM5/PDF/results_PostFit_b_M130to150.root'
OutputFile_M130to150_ele='rootFile_2018_SKIM5/PDF/results_PostFit_b_M130to150.root'
OutputFile_M130to150_mu='rootFile_2018_SKIM5/PDF/results_PostFit_b_M130to150.root'

#/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv5/2017/StackNew_comb/scripts/combine
common_opt_b=' --pycfg=configuration.py --inputFileCombine=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv5/2017/StackNew_comb/scripts/combine/fitDiagnosticsM110Y2016muCH4j2b__4j3b__eleCH4j2b__4j3b__Y2017muCH4j2b__4j3b__eleCH4j2b__4j3b__Y2018muCH4j2b__HEMveto4j3b__HEMvetoeleCH4j2b__HEMveto4j3b__HEMveto.root --outputFile='$OutputFile'  --inputFile='$InputFile'  --structureFile=structure.py  --cutNameInOriginal=''  --kind=b  --getSignalFromPrefit=1'
common_opt_b_M130to150=' --pycfg=configuration.py --inputFileCombine=/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv5/2017/StackNew_comb/scripts/combine/fitDiagnosticsM130Y2016muCH4j2b__4j3b__eleCH4j2b__4j3b__Y2017muCH4j2b__4j3b__eleCH4j2b__4j3b__Y2018muCH4j2b__HEMveto4j3b__HEMvetoeleCH4j2b__HEMveto4j3b__HEMveto.root --outputFile='$OutputFile_M130to150'  --inputFile='$InputFile'  --structureFile=structure.py  --cutNameInOriginal=''  --kind=b  --getSignalFromPrefit=1'
#mkPostFitPlot.py $common_opt_b --cut=muCH__Top4j2b__noHEMveto  --variable=fitted_dijet_M
#mkPostFitPlot.py $common_opt_b --cut=eleCH__Top4j2b__noHEMveto  --variable=fitted_dijet_M
#mkPostFitPlot.py $common_opt_b --cut=muCH__Top4j3b__noHEMveto  --variable=fitted_dijet_M_down_type_jet_b_tagged
#mkPostFitPlot.py $common_opt_b --cut=eleCH__Top4j3b__noHEMveto  --variable=fitted_dijet_M_down_type_jet_b_tagged
#mkPostFitPlot.py $common_opt_b_M130to150 --cut=muCH__Top4j2b__noHEMveto  --variable=fitted_dijet_M
#mkPostFitPlot.py $common_opt_b_M130to150 --cut=eleCH__Top4j2b__noHEMveto  --variable=fitted_dijet_M
#mkPostFitPlot.py $common_opt_b_M130to150 --cut=muCH__Top4j3b__noHEMveto  --variable=fitted_dijet_M_high_down_type_jet_b_tagged
#mkPostFitPlot.py $common_opt_b_M130to150 --cut=eleCH__Top4j3b__noHEMveto  --variable=fitted_dijet_M_high_down_type_jet_b_tagged


#mkPlot.py --pycfg=configuration_PostFit_b.py --inputFile=$OutputFile --onlyPlot=cratio --scaleToPlot=1.7
mkPlot.py --pycfg=configuration_PostFit_M130to150_b.py --inputFile=$OutputFile_M130to150 --onlyPlot=cratio --scaleToPlot=1.7
