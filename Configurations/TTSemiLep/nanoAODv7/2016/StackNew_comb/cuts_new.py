#-----Variable Deinition-----#
import sys
try:
  from WPandCut2016 import *
except ImportError:
  import os
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv7/2016/StackNew_comb"
  sys.path.append(BASE_PATH)
  from WPandCut2016 import *

#cuts={}

scriptname=opt.cutsFile

supercut = '((nLooseLep == 1) && (nCleanJet_2p4 >=4) && (nBJets_WP_M >= 2) && (MET_CHToCB_pt_nom > 20.))\
           || ((nLooseLep == 2) && (nCleanJet_2p4 >=2) && (nBJets_WP_M >= 2) && (MET_CHToCB_pt_nom > 40.))'



cuts['sng_4j_eleORmuCH'] = {
  'expr' : '(nLooseLep == 1) && (nCleanJet_2p4 >=4) && (nTightElWithCut + nTightMuWithCut == 1)',
  'categories' : {
    '2b' : 'nBJets_WP_M == 2',
    '3b' : 'nBJets_WP_M >= 3',
  },
}

cuts['sng_4j'] = {
  'expr' : '(nLooseLep == 1) && (nCleanJet_2p4 >=4) && (nTightElWithCut + nTightMuWithCut == 1)',
  'categories' : {
    'eleCH_2b' : '(nTightElWithCut == 1) && (nBJets_WP_M == 2) && HLT_Ele27_WPTight_Gsf',
    'muCH_2b'  : '(nTightMuWithCut == 1) && (nBJets_WP_M == 2) && Trigger_sngMu',
    'eleCH_3b' : '(nTightElWithCut == 1) && (nBJets_WP_M >= 3) && HLT_Ele27_WPTight_Gsf',
    'muCH_3b'  : '(nTightMuWithCut == 1) && (nBJets_WP_M >= 3) && Trigger_sngMu',
  },
}

#cuts['dbl_2j_eeORmmORemORme'] = {
#  'expr' : '(nLooseLep == 2) && (nCleanJet_2p4 >=2) && (eeCH || mmCH || emCH || meCH)',
#  'categories' : {
#    '2b' : 'nBJets_WP_M == 2',
#    '3b' : 'nBJets_WP_M >= 3',
#  },
#}
#
#cuts['dbl_2j'] = {
#  'expr' : '(nLooseLep == 2) && (nCleanJet_2p4 >=2) && (eeCH || mmCH || emCH || meCH)',
#  'categories' : {
#    'ee_2b' : 'eeCH && (nBJets_WP_M == 2)',
#    'mm_2b' : 'mmCH && (nBJets_WP_M == 2)',
#    'em_2b' : 'emCH && (nBJets_WP_M == 2)',
#    'me_2b' : 'meCH && (nBJets_WP_M == 2)',
#    'ee_3b' : 'eeCH && (nBJets_WP_M >= 3)',
#    'mm_3b' : 'mmCH && (nBJets_WP_M >= 3)',
#    'em_3b' : 'emCH && (nBJets_WP_M >= 3)',
#    'me_3b' : 'meCH && (nBJets_WP_M >= 3)',
#  },
#}



#cuts['isVBF']='isVBF'
print "Ncuts=",len(cuts)

