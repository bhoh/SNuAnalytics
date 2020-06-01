#!/usr/bin/env python

file_names = {
  ('2017','TTLJ_powheg') :
  [
    '/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_TTToSemiLeptonic__part%s.root'%idx for idx in range(0,4)
  ],
  ('2017','TTLJ_powheg_Test') :
  [
    '/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_TTToSemiLeptonic__part%s.root'%idx for idx in range(4,8)
  ],
  ('2017','WJetsToLNu-0J') :
  [
    '/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_WJetsToLNu-0J__part%s.root'%idx for idx in range(0,9)
  ],
  ('2017','WJetsToLNu-0J_Test') :
  [
    '/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_WJetsToLNu-0J__part%s.root'%idx for idx in range(9,19)
  ],
  ('2017','WJetsToLNu-1J') :
  [
    '/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_WJetsToLNu-1J__part%s.root'%idx for idx in range(0,5)
  ],
  ('2017','WJetsToLNu-1J_Test') :
  [
    '/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_WJetsToLNu-1J__part%s.root'%idx for idx in range(5,10)
  ],
  ('2017','WJetsToLNu-2J') :
  [
    '/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_WJetsToLNu-1J__part%s.root'%idx for idx in range(0,6)
  ],
  ('2017','WJetsToLNu-2J_Test') :
  [
    '/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_WJetsToLNu-1J__part%s.root'%idx for idx in range(6,12)
  ],
  ('2017','HWW_GgfM200') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_GluGluHToWWToLNuQQ_M200__part0.root'],
  ('2017','HWW_VbfM200') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_VBFHToWWToLNuQQ_M200__part%s.root'%idx for idx in range(0,4)],
  ('2017','HWW_GgfM400') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_GluGluHToWWToLNuQQ_M400__part%s.root' % idx for idx in range(0,2)],
  ('2017','HWW_VbfM400') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_VBFHToWWToLNuQQ_M400__part0.root'],
  ('2017','HWW_GgfM800') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_GluGluHToWWToLNuQQ_M800__part0.root'],
  ('2017','HWW_VbfM800') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_VBFHToWWToLNuQQ_M800__part%s.root' % idx for idx in range(0,2)],
  ('2017','HWW_GgfM1000') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_GluGluHToWWToLNuQQ_M1000__part%s.root' % idx for idx in range(0,3)],
  ('2017','HWW_VbfM1000') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_VBFHToWWToLNuQQ_M1000__part%s.root' % idx for idx in range(0,2)],
  ('2017','HWW_GgfM1500') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_GluGluHToWWToLNuQQ_M1500__part0.root' ],
  ('2017','HWW_VbfM1500') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_VBFHToWWToLNuQQ_M1500__part0.root' ],
  ('2017','HWW_GgfM2000') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_GluGluHToWWToLNuQQ_M2000__part%s.root' % idx for idx in range(0,2) ],
  ('2017','HWW_VbfM2000') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_VBFHToWWToLNuQQ_M2000__part0.root' ],
  ('2017','HWW_GgfM3000') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_GluGluHToWWToLNuQQ_M3000__part0.root'],
  ('2017','HWW_VbfM3000') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_VBFHToWWToLNuQQ_M3000__part%s.root' % idx for idx in range(0,2)],
  ('2017','HWW_GgfM4000') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_GluGluHToWWToLNuQQ_M4000__part0.root'],
  ('2017','HWW_VbfM4000') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_VBFHToWWToLNuQQ_M4000__part0.root'],
  ('2017','HWW_GgfM5000') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_GluGluHToWWToLNuQQ_M5000__part0.root'],
  ('2017','HWW_VbfM5000') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11pre_nom/nanoLatino_VBFHToWWToLNuQQ_M5000__part0.root'],
}

