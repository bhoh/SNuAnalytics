# /xrootd//store/user/jhchoi/Latino/HWWNano/
# Sites_cfg: /xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/
# changed to /xrd/store/user/jhchoi/Latino/HWWNano/
# L1Loose
#mkPostProc.py -p Fall2017_102X_nAODv4_Full2017v4 -i Prod -s MCl1loose2017v2 -b
#mkPostProc.py -p Fall2017_102X_nAODv4_Full2017v4 -i MCl1loose2017v2 -s MCCorr2017_SemiLep -b -n -E DYJetsToLL_M-10to50-LO,GluGluHToWWTo2L2NuPowheg_M125,QCD_Pt-170to300_MuEnrichedPt5,ttHToNonbb_M125,TTTo2L2Nu_PSWeights_CP5Down,TTTo2L2Nu_PSWeights,VBFHToWWTo2L2Nu_M124,VBFHToWWToLNuQQ_M550,VBFHToWWToLNuQQ_M600,VBFHToWWToLNuQQ_M700,VBFHToWWToLNuQQ_M750,VBFHToWWToLNuQQ_M800,VBFHToWWToLNuQQ_M900,Wg_AMCNLOFXFX,Wg_MADGRAPHMLM,WJetsToLNu_HT100_200,WJetsToLNu_HT600_800,WLLJJToLNu_M-4To50_QCD_2Jet,WLLJJToLNu_M-50_QCD_0Jet,WLLJJToLNu_M-50_QCD_1Jet,WLLJJToLNu_M-50_QCD_2Jet,WLLJJToLNu_M-50_QCD_3Jet,WLLJJToLNu_M-60_EWK_4F,WpWmJJ_EWK,WpWmJJ_EWK_QCD_noTop_noHiggs,WpWpJJ_EWK,WWG,ZGToLLG,ZZTo2L2Nu,ZZTo2L2Q,ZZTo4L-ext1,ZZTo4L
#mkPostProc.py -p Fall2017_102X_nAODv4_Full2017v4 -i MCl1loose2017v2 -s MCCorr2017_SemiLep -b -T DYJetsToLL_M-50 -R
mkPostProc.py -p Fall2017_102X_nAODv4_Full2017v4 -i MCl1loose2017v2 -s MCCorr2017_SemiLep -b -T ttHToNonbb_M125 -R 
