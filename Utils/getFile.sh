fileName="nanoLatino_GluGluHToWWToLNuQQ_M900__part1__HMlnjjSel2017.root"
#fileName="nanoLatino_WJetsToLNu_HT1200_2500__part10__HMlnjjSel2017_test.root"
#fileName="nanoLatino_GluGluHToWWToLNuQQ_M900__part1_Skim.root"
#fileName="nanoLatino_GluGluHToWWToLNuQQ_M2500__part0_Skim.root"
#fileName="nanoLatino_GluGluHToWWToLNuQQ_M4000__part6_Skim.root"
#scp  -P 4280 ui20.sdfarm.kr:Latino/workdir/jobs/NanoGardening__Fall2017_102X_nAODv4_Full2017v5/${fileName} .
scp  -P 4280 ui20.sdfarm.kr:Latino/workdir/jobs/${fileName} .
