#-----Variable Deinition-----#
import sys
try:
  from WPandCut2018 import *
except ImportError:
  import os
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv9/2018/StackNew_comb"
  sys.path.append(BASE_PATH)
  from WPandCut2018 import *
#cuts={}

scriptname=opt.cutsFile

supercut = '((nLooseLep == 1) && (nCleanJet_2p4 >=4) && (nBJets_WP_M >= 2) && (MET_CHToCB_pt_nom > 20.))\
           || ((nLooseLep == 2) && (nCleanJet_2p4 >=2) && (nBJets_WP_M >= 2) && (MET_CHToCB_pt_nom > 40.))'

cuts['sng_4j'] = {
  'expr' : '(nLooseLep == 1) && (nCleanJet_2p4 >=4) && (eleCH || muCH)',
  'categories' : {
    'eleCH_2b' : 'eleCH && (nBJets_WP_M == 2)',
    'muCH_2b'  : 'muCH  && (nBJets_WP_M == 2)',
    'eleCH_3b' : 'eleCH && (nBJets_WP_M >= 3)',
    'muCH_3b'  : 'muCH  && (nBJets_WP_M >= 3)',
  },
}

cuts['sng_4j_eleORmuCH'] = {
  'expr' : '(nLooseLep == 1) && ((nCleanJet30_2p4+nCleanJet25to30_2p4)>=4) && (eleCH || muCH)',
  'categories' : {
    '2b' : '(nBJets_WP_M+nBJets_WP_M_25to30) == 2',
    '3b' : '(nBJets_WP_M+nBJets_WP_M_25to30) >= 3',
  },
}


cuts['dbl_4j_eeORmmORemORme'] = {
  'expr' : '(nLooseLep == 2) && (nCleanJet30_2p4>=2) && (nCleanJet20_2p4>=4) && (nBJets_WP_M >= 2) && (eeCH || mmCH || emCH || meCH) && (mll > 10)',
  'categories' : {
    'offZ' : 'isOSpair && (emCH || meCH || abs(mll-91.18)>15)',
    'onZ' : 'isOSpair && (!emCH && !meCH && abs(mll-91.18)<=15)',
  },
}

cuts['dbl_4j'] = {
  'expr' : '(nLooseLep == 2) && (nCleanJet30_2p4>=2) && (nCleanJet20_2p4>=4) && (nBJets_WP_M >= 2) && (eeCH || mmCH || emCH || meCH) && (mll > 10)',
  'categories' : {
    'ee'      : 'eeCH && isOSpair && (abs(mll-91.18)>15)',
    'mm'      : 'mmCH && isOSpair && (abs(mll-91.18)>15)',
    'em'      : 'emCH && isOSpair',
    'me'      : 'meCH && isOSpair',
    'ee_onZ'  : 'eeCH && isOSpair && (abs(mll-91.18)<=15)',
    'mm_onZ'  : 'mmCH && isOSpair && (abs(mll-91.18)<=15)',

  },
}



#cuts['isVBF']='isVBF'
print "Ncuts=",len(cuts)

