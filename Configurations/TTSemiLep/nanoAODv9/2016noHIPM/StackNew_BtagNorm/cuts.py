#-----Variable Deinition-----#
import sys
try:
  from WPandCut2016 import *
except ImportError:
  import os
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv9/2016/StackNew_comb"
  sys.path.append(BASE_PATH)
  from WPandCut2016 import *

#cuts={}

scriptname=opt.cutsFile
include_bincl = True if not '_final' in opt.pycfg else False

supercut = '((nLooseLep == 1) && (nCleanJet25_2p4 >=4) && (MET_CHToCB_pt_nom > 20.))\
           || ((nLooseLep == 2) && (nCleanJet30_2p4 >=2) && (MET_CHToCB_pt_nom > 40.))'

# to speed up, add kinematic fitter status cut on super cut
kf_status_cut = True if '_final' in opt.pycfg else False
if kf_status_cut:
  supercut = '(' + supercut +') && (status_nom==0)'


cuts['sng_4j_eleORmuCH'] = {
  'expr' : '(nLooseLep == 1) && ((nCleanJet30_2p4+nCleanJet25to30_2p4)>=4) && (eleCH || muCH)',
}


cuts['sng_4j'] = {
  'expr' : '(nLooseLep == 1) && ((nCleanJet30_2p4+nCleanJet25to30_2p4)>=4) && (eleCH || muCH)',
  'categories' : {
    'eleCH' : 'eleCH',
    'muCH'  : 'muCH',
  },
}






cuts['dbl_4j_eeORmmORemORme'] = {
  'expr' : '(nLooseLep == 2) && (nCleanJet30_2p4>=2) && (nCleanJet25_2p4>=4) && (eeCH || mmCH || emCH || meCH) && (mll > 12)',
  'categories' : {
    'offZ' : 'isOSpair && (emCH || meCH || abs(mll-91.18)>15)',
    'onZ' : 'isOSpair && (!emCH && !meCH && abs(mll-91.18)<=15)',
  },
}

cuts['dbl_4j'] = {
  'expr' : '(nLooseLep == 2) && (nCleanJet30_2p4>=2) && (nCleanJet25_2p4>=4) && (eeCH || mmCH || emCH || meCH) && (mll > 12)',
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

