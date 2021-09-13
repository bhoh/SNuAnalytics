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


#cuts['sng_4j_eleORmuCH_>=2b'] = {
#  'expr' : '(nLooseLep == 1) && (nCleanJet20_2p5_PU_M >=4) && (nCleanJet_custum == nCleanJet20_2p5_PU_M) && (nBJets_WP_M >= 2) && (eleCH || muCH)',
#}

cuts['sng_4j_eleORmuCH'] = {
  'expr' : '(nLooseLep == 1) && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=4) && (eleCH || muCH)',
  'categories' : {
    '2b' : '(nBJets_WP_M) == 2',
    '3b' : '(nBJets_WP_M) >= 3',
  },
}

#cuts['sng_4j_>=2b'] = {
#  'expr' : '(nLooseLep == 1) && (nCleanJet20_2p5_PU_M >=4) && (nCleanJet_custum == nCleanJet20_2p5_PU_M) && (nBJets_WP_M >= 2) && (eleCH || muCH)',
#  'categories' : {
#    'eleCH' : 'eleCH',
#    'muCH'  : 'muCH',
#  },
#}

cuts['sng_4j'] = {
  'expr' : '(nLooseLep == 1) && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=4) && (eleCH || muCH)',
  'categories' : {
    'eleCH_2b' : 'eleCH && ((nBJets_WP_M) == 2)',
    'muCH_2b'  : 'muCH  && ((nBJets_WP_M) == 2)',
    'eleCH_3b' : 'eleCH && ((nBJets_WP_M) >= 3)',
    'muCH_3b'  : 'muCH  && ((nBJets_WP_M) >= 3)',
  },
}



#cuts['isVBF']='isVBF'
print "Ncuts=",len(cuts)

