#-----Variable Deinition-----#
import sys
try:
  from WPandCut2018 import *
except ImportError:
  import os
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv7/2018/StackNew_comb"
  sys.path.append(BASE_PATH)
  from WPandCut2018 import *

#cuts={}

scriptname=opt.cutsFile

supercut = '((nLooseLep == 1) && (nCleanJet30_2p5 >=3) && (nBJets_WP_M >= 2) && (MET_CHToCB_pt_nom > 20.))\
           || ((nLooseLep == 2) && (nCleanJet30_2p5 >=2) && (nBJets_WP_M >= 2) && (MET_CHToCB_pt_nom > 40.))'


cuts['sng_4j_eleORmuCH_bincl'] = {
  'expr' : '(nLooseLep == 1) && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=4) && (eleCH || muCH)',
}

cuts['sng_4j_eleORmuCH'] = {
  'expr' : '(nLooseLep == 1) && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=4) && (eleCH || muCH)',
  'categories' : {
    '2b' : '(nBJets_WP_M + nBJets_WP_M_20to30) == 2',
    '3b' : '(nBJets_WP_M + nBJets_WP_M_20to30) >= 3',
  },
}

cuts['sng_4j_bincl'] = {
  'expr' : '(nLooseLep == 1) && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=4) && (eleCH || muCH)',
  'categories' : {
    'eleCH' : 'eleCH',
    'muCH'  : 'muCH',
  },
}

cuts['sng_4j'] = {
  'expr' : '(nLooseLep == 1) && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=4) && (eleCH || muCH)',
  'categories' : {
    'eleCH_2b' : 'eleCH && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
    'muCH_2b'  : 'muCH  && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
    'eleCH_3b' : 'eleCH && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)',
    'muCH_3b'  : 'muCH  && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)',
  },
}

cuts['sng_jbin'] = {
  'expr' : '(nLooseLep == 1) && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=4) && (eleCH || muCH)',
  'categories' : {
    'eleCH_4j_2b' : 'eleCH  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==4) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
    'eleCH_5j_2b' : 'eleCH  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==5) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
    'eleCH_6j_2b' : 'eleCH  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=6) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
    'muCH_4j_2b'  : 'muCH   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==4) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
    'muCH_5j_2b'  : 'muCH   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==5) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
    'muCH_6j_2b'  : 'muCH   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=6) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
    'eleCH_4j_3b' : 'eleCH  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==4) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 3)',
    'eleCH_5j_3b' : 'eleCH  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==5) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 3)',
    'eleCH_6j_3b' : 'eleCH  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=6) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 3)',
    'eleCH_4b'    : 'eleCH  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=4) && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 4)',
    'muCH_4j_3b'  : 'muCH   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==4) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 3)',
    'muCH_5j_3b'  : 'muCH   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==5) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 3)',
    'muCH_6j_3b'  : 'muCH   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=6) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 3)',
    'muCH_4b'     : 'muCH   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=4) && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 4)',
  },
}
cuts['sng_jbin_bincl'] = {
  'expr' : '(nLooseLep == 1) && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=4) && (eleCH || muCH)',
  'categories' : {
    'eleCH_4j_2b' : 'eleCH  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==4)',
    'eleCH_5j_2b' : 'eleCH  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==5)',
    'eleCH_6j_2b' : 'eleCH  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=6)',
    'muCH_4j_2b'  : 'muCH   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==4)',
    'muCH_5j_2b'  : 'muCH   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==5)',
    'muCH_6j_2b'  : 'muCH   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=6)',
  },
}
#cuts['dbl_2j_eeORmmORemORme_>=2b'] = {
#  'expr' : '(nLooseLep == 2) && (nCleanJet20_2p5_PU_M >=2) && (nBJets_WP_M >= 2) && (eeCH || mmCH || emCH || meCH)',
#}

cuts['dbl_2j_eeORmmORemORme'] = {
  'expr' : '(nLooseLep == 2) && (nCleanJet30_2p5>=2) && (nBJets_WP_M >= 2) && (eeCH || mmCH || emCH || meCH) && (mll > 12)',
  'categories' : {
    '2b' : 'isOSpair && (nBJets_WP_M + nBJets_WP_M_20to30) == 2 && (emCH || meCH || abs(mll-91.18)>15)',
    '3b' : 'isOSpair && (nBJets_WP_M + nBJets_WP_M_20to30) >= 3 && (emCH || meCH || abs(mll-91.18)>15)',
    '2b_onZ' : 'isOSpair && (nBJets_WP_M + nBJets_WP_M_20to30) == 2 && (!emCH && !meCH && abs(mll-91.18)<=15)',
    '3b_onZ' : 'isOSpair && (nBJets_WP_M + nBJets_WP_M_20to30) >= 3 && (!emCH && !meCH && abs(mll-91.18)<=15)',
  },
}


#cuts['dbl_2j_>=2b'] = {
#  'expr' : '(nLooseLep == 2) && (nCleanJet20_2p5_PU_M >=2) && (nBJets_WP_M >= 2) && (eeCH || mmCH || emCH || meCH) && (mll > 12)',
#  'categories' : {
#    'ee' : 'eeCH',
#    'mm' : 'mmCH',
#    'em' : 'emCH',
#    'me' : 'meCH',
#    'ee' : 'eeCH',
#    'mm' : 'mmCH',
#    'em' : 'emCH',
#    'me' : 'meCH',
#  },
#}

cuts['dbl_2j'] = {
  'expr' : '(nLooseLep == 2) && (nCleanJet30_2p5>=2) && (nBJets_WP_M >= 2) && (eeCH || mmCH || emCH || meCH) && (mll > 12)',
  'categories' : {
    'ee_2b' : 'eeCH && isOSpair && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (abs(mll-91.18)>15)',
    'mm_2b' : 'mmCH && isOSpair && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (abs(mll-91.18)>15)',
    'em_2b' : 'emCH && isOSpair && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
    'me_2b' : 'meCH && isOSpair && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
    'ee_3b' : 'eeCH && isOSpair && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (abs(mll-91.18)>15)',
    'mm_3b' : 'mmCH && isOSpair && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (abs(mll-91.18)>15)',
    'em_3b' : 'emCH && isOSpair && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)',
    'me_3b' : 'meCH && isOSpair && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)',
    'ee_2b_onZ' : 'eeCH && isOSpair && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (abs(mll-91.18)<=15)',
    'mm_2b_onZ' : 'mmCH && isOSpair && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (abs(mll-91.18)<=15)',
    'ee_3b_onZ' : 'eeCH && isOSpair && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (abs(mll-91.18)<=15)',
    'mm_3b_onZ' : 'mmCH && isOSpair && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (abs(mll-91.18)<=15)',

  },
}

cuts['dbl_4j_eeORmmORemORme'] = {
  'expr' : '(nLooseLep == 2) && (nCleanJet30_2p5>=2) && (nCleanJet20_2p5>=4) && (nBJets_WP_M >= 2) && (eeCH || mmCH || emCH || meCH) && (mll > 12)',
  'categories' : {
    'offZ' : 'isOSpair && (emCH || meCH || abs(mll-91.18)>15)',
    'onZ' : 'isOSpair && (!emCH && !meCH && abs(mll-91.18)<=15)',
  },
}

cuts['dbl_4j'] = {
  'expr' : '(nLooseLep == 2) && (nCleanJet30_2p5>=2) && (nCleanJet20_2p5>=4) && (nBJets_WP_M >= 2) && (eeCH || mmCH || emCH || meCH) && (mll > 12)',
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

