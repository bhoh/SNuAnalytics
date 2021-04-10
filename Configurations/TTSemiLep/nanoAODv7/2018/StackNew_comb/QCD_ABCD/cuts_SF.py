#-----Variable Deinition-----#
import sys
try:
  from WPandCut2018 import *
except ImportError:
  import os
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv7/2018/top_pt_reweight"
  sys.path.append(BASE_PATH)
  from WPandCut2018 import *

#cuts={}

#MET
#          #
#          #
#    A     #     D
#          #
# # # # # # # # # # # #
#          #
#    B     #     C
#          #
########## # ######### id


scriptname=opt.cutsFile

supercut = '((nLooseLep == 1) && (nCleanJet30_2p5 >=3) && (nBJets_WP_M >= 2))\
           || ((nLooseLep == 2) && (nCleanJet30_2p5 >=2) && (nBJets_WP_M >= 2))'

cuts['sng_4j_eleORmuCH'] = {
  'expr' : '(nLooseLep == 1) && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=4)',
  'categories' : {
    #'B_2b' : '(eleCH || muCH) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom<=20)',
    #'B_3b' : '(eleCH || muCH) && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom<=20)',
    #'C_2b' : '(eleCH_noTight || muCH_noTight) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom<=20)',
    #'C_3b' : '(eleCH_noTight || muCH_noTight) && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom<=20)',
    #'A_2b' : '(eleCH || muCH) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    #'A_3b' : '(eleCH || muCH) && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom>20)',
    'D_2b' : '(eleCH_noTight || muCH_noTight) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    'D_3b' : '(eleCH_noTight || muCH_noTight) && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom>20)',

  },
}
cuts['sng_4j_eleORmuCH_isoDown'] = {
  'expr' : '(nLooseLep == 1) && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=4)',
  'categories' : {
    #'C_2b' : '(eleCH_noTight_isoDown || muCH_noTight_isoDown) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom<=20)',
    #'C_3b' : '(eleCH_noTight_isoDown || muCH_noTight_isoDown) && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom<=20)',
    'D_2b' : '(eleCH_noTight_isoDown || muCH_noTight_isoDown) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    'D_3b' : '(eleCH_noTight_isoDown || muCH_noTight_isoDown) && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom>20)',

  },
}
cuts['sng_4j'] = {
  'expr' : '(nLooseLep == 1) && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=4)',
  'categories' : {
    #'B_eleCH_2b' : 'eleCH && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom<=20)',
    #'B_muCH_2b'  : 'muCH  && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom<=20)',
    #'B_eleCH_3b' : 'eleCH && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom<=20)',
    #'B_muCH_3b'  : 'muCH  && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom<=20)',
    #'C_eleCH_2b' : 'eleCH_noTight && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom<=20)',
    #'C_muCH_2b'  : 'muCH_noTight  && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom<=20)',
    #'C_eleCH_3b' : 'eleCH_noTight && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom<=20)',
    #'C_muCH_3b'  : 'muCH_noTight  && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom<=20)',   
    #'A_eleCH_2b' : 'eleCH && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    #'A_muCH_2b'  : 'muCH  && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    #'A_eleCH_3b' : 'eleCH && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom>20)',
    #'A_muCH_3b'  : 'muCH  && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom>20)',
    'D_eleCH_2b' : 'eleCH_noTight && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    'D_muCH_2b'  : 'muCH_noTight  && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    'D_eleCH_3b' : 'eleCH_noTight && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom>20)',
    'D_muCH_3b'  : 'muCH_noTight  && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom>20)',

  },
}
cuts['sng_4j_isoDown'] = {
  'expr' : '(nLooseLep == 1) && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=4)',
  'categories' : {
    #'C_eleCH_2b' : 'eleCH_noTight_isoDown && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom<=20)',
    #'C_muCH_2b'  : 'muCH_noTight_isoDown  && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom<=20)',
    #'C_eleCH_3b' : 'eleCH_noTight_isoDown && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom<=20)',
    #'C_muCH_3b'  : 'muCH_noTight_isoDown  && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom<=20)',   
    'D_eleCH_2b' : 'eleCH_noTight_isoDown && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    'D_muCH_2b'  : 'muCH_noTight_isoDown  && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    'D_eleCH_3b' : 'eleCH_noTight_isoDown && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom>20)',
    'D_muCH_3b'  : 'muCH_noTight_isoDown  && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom>20)',

  },
}
cuts['sng_jbin'] = {
  'expr' : '(nLooseLep == 1) && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=4)',
  'categories' : {
    'D_eleCH_4j_2b' : 'eleCH_noTight  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==4) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    'D_eleCH_5j_2b' : 'eleCH_noTight  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==5) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    'D_eleCH_6j_2b' : 'eleCH_noTight  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=6) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    'D_muCH_4j_2b'  : 'muCH_noTight   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==4) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    'D_muCH_5j_2b'  : 'muCH_noTight   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==5) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    'D_muCH_6j_2b'  : 'muCH_noTight   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=6) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    'D_eleCH_4j_3b' : 'eleCH_noTight  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==4) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 3) && (MET_CHToCB_pt_nom>20)',
    'D_eleCH_5j_3b' : 'eleCH_noTight  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==5) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 3) && (MET_CHToCB_pt_nom>20)',
    'D_eleCH_6j_3b' : 'eleCH_noTight  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=6) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 3) && (MET_CHToCB_pt_nom>20)',
    'D_eleCH_4b'    : 'eleCH_noTight  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=4) && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 4) && (MET_CHToCB_pt_nom>20)',
    'D_muCH_4j_3b'  : 'muCH_noTight   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==4) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 3) && (MET_CHToCB_pt_nom>20)',
    'D_muCH_5j_3b'  : 'muCH_noTight   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==5) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 3) && (MET_CHToCB_pt_nom>20)',
    'D_muCH_6j_3b'  : 'muCH_noTight   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=6) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 3) && (MET_CHToCB_pt_nom>20)',
    'D_muCH_4b'     : 'muCH_noTight   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=4) && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 4) && (MET_CHToCB_pt_nom>20)',
  },
}
cuts['sng_jbin_isoDown'] = {
  'expr' : '(nLooseLep == 1) && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=4)',
  'categories' : {
    'D_eleCH_4j_2b' : 'eleCH_noTight_isoDown  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==4) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    'D_eleCH_5j_2b' : 'eleCH_noTight_isoDown  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==5) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    'D_eleCH_6j_2b' : 'eleCH_noTight_isoDown  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=6) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    'D_muCH_4j_2b'  : 'muCH_noTight_isoDown   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==4) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    'D_muCH_5j_2b'  : 'muCH_noTight_isoDown   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==5) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    'D_muCH_6j_2b'  : 'muCH_noTight_isoDown   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=6) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2) && (MET_CHToCB_pt_nom>20)',
    'D_eleCH_4j_3b' : 'eleCH_noTight_isoDown  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==4) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 3) && (MET_CHToCB_pt_nom>20)',
    'D_eleCH_5j_3b' : 'eleCH_noTight_isoDown  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==5) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 3) && (MET_CHToCB_pt_nom>20)',
    'D_eleCH_6j_3b' : 'eleCH_noTight_isoDown  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=6) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 3) && (MET_CHToCB_pt_nom>20)',
    'D_eleCH_4b'    : 'eleCH_noTight_isoDown  && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=4) && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 4) && (MET_CHToCB_pt_nom>20)',
    'D_muCH_4j_3b'  : 'muCH_noTight_isoDown   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==4) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 3) && (MET_CHToCB_pt_nom>20)',
    'D_muCH_5j_3b'  : 'muCH_noTight_isoDown   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)==5) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 3) && (MET_CHToCB_pt_nom>20)',
    'D_muCH_6j_3b'  : 'muCH_noTight_isoDown   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=6) && ((nBJets_WP_M + nBJets_WP_M_20to30) == 3) && (MET_CHToCB_pt_nom>20)',
    'D_muCH_4b'     : 'muCH_noTight_isoDown   && ((nCleanJet30_2p5+nCleanJet20to30_2p5_PU_M)>=4) && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 4) && (MET_CHToCB_pt_nom>20)',
  },
}
#MET
#          #
#          #
#    A     #     D
#          #
# # # # # # # # # # # #
#          #
#    B     #     C
#          #
########## # ######### OS/SS


#cuts['dbl_2j_eeORmmORemORme'] = {
#  'expr' : '(nLooseLep == 2) && (nCleanJet30_2p5>=2) && (nBJets_WP_M >= 2) && (eeCH || mmCH || emCH || meCH) && (mll>10 && abs(mll-91.18)>15)',
#  'categories' : {
#    'A_2b' : 'isOSpair  && (MET_CHToCB_pt_nom>40)  && (nBJets_WP_M + nBJets_WP_M_20to30) == 2',
#    'B_2b' : 'isOSpair && (MET_CHToCB_pt_nom<=40) && (nBJets_WP_M + nBJets_WP_M_20to30) == 2',
#    'C_2b' : '!isOSpair && (MET_CHToCB_pt_nom<=40) && (nBJets_WP_M + nBJets_WP_M_20to30) == 2',
#    'D_2b' : '!isOSpair  && (MET_CHToCB_pt_nom>40)  && (nBJets_WP_M + nBJets_WP_M_20to30) == 2',
#    'A_3b' : 'isOSpair  && (MET_CHToCB_pt_nom>40)  && (nBJets_WP_M + nBJets_WP_M_20to30) >= 3',
#    'B_3b' : 'isOSpair && (MET_CHToCB_pt_nom<=40) && (nBJets_WP_M + nBJets_WP_M_20to30) >= 3',
#    'C_3b' : '!isOSpair && (MET_CHToCB_pt_nom<=40) && (nBJets_WP_M + nBJets_WP_M_20to30) >= 3',
#    'D_3b' : '!isOSpair  && (MET_CHToCB_pt_nom>40)  && (nBJets_WP_M + nBJets_WP_M_20to30) >= 3',
#  },
#}
#
##cuts['dbl_2j_>=2b'] = {
##  'expr' : '(nLooseLep == 2) && (nCleanJet20_2p5_PU_M >=2) && (nBJets_WP_M >= 2) && (eeCH || mmCH || emCH || meCH) && (mll>10 && abs(mll-91.18)>15)',
##  'categories' : {
##    'ee' : 'eeCH',
##    'mm' : 'mmCH',
##    'em' : 'emCH',
##    'me' : 'meCH',
##    'ee' : 'eeCH',
##    'mm' : 'mmCH',
##    'em' : 'emCH',
##    'me' : 'meCH',
##  },
##}
#
#cuts['dbl_2j'] = {
#  'expr' : '(nLooseLep == 2) && (nCleanJet30_2p5>=2) && (nBJets_WP_M >= 2) && (eeCH || mmCH || emCH || meCH) && (mll>10 && abs(mll-91.18)>15)',
#  'categories' : {
#    'A_ee_2b' : 'isOSpair  && (MET_CHToCB_pt_nom>40)  && eeCH && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
#    'B_ee_2b' : 'isOSpair && (MET_CHToCB_pt_nom<=40) && eeCH && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
#    'C_ee_2b' : '!isOSpair && (MET_CHToCB_pt_nom<=40) && eeCH && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
#    'D_ee_2b' : '!isOSpair  && (MET_CHToCB_pt_nom>40)  && eeCH && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
#    'A_mm_2b' : 'isOSpair  && (MET_CHToCB_pt_nom>40)  && mmCH && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
#    'B_mm_2b' : 'isOSpair && (MET_CHToCB_pt_nom<=40) && mmCH && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
#    'C_mm_2b' : '!isOSpair && (MET_CHToCB_pt_nom<=40) && mmCH && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
#    'D_mm_2b' : '!isOSpair  && (MET_CHToCB_pt_nom>40)  && mmCH && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
#    'A_em_2b' : 'isOSpair  && (MET_CHToCB_pt_nom>40)  && emCH && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
#    'B_em_2b' : 'isOSpair && (MET_CHToCB_pt_nom<=40) && emCH && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
#    'C_em_2b' : '!isOSpair && (MET_CHToCB_pt_nom<=40) && emCH && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
#    'D_em_2b' : '!isOSpair  && (MET_CHToCB_pt_nom>40)  && emCH && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
#    'A_me_2b' : 'isOSpair  && (MET_CHToCB_pt_nom>40)  && meCH && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
#    'B_me_2b' : 'isOSpair && (MET_CHToCB_pt_nom<=40) && meCH && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
#    'C_me_2b' : '!isOSpair && (MET_CHToCB_pt_nom<=40) && meCH && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
#    'D_me_2b' : '!isOSpair  && (MET_CHToCB_pt_nom>40)  && meCH && ((nBJets_WP_M + nBJets_WP_M_20to30) == 2)',
#    'A_ee_3b' : 'isOSpair  && (MET_CHToCB_pt_nom>40)  && eeCH && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)',
#    'B_ee_3b' : 'isOSpair && (MET_CHToCB_pt_nom<=40) && eeCH && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)',
#    'C_ee_3b' : '!isOSpair && (MET_CHToCB_pt_nom<=40) && eeCH && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)',
#    'D_ee_3b' : '!isOSpair  && (MET_CHToCB_pt_nom>40)  && eeCH && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)',
#    'A_mm_3b' : 'isOSpair  && (MET_CHToCB_pt_nom>40)  && mmCH && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)',
#    'B_mm_3b' : 'isOSpair && (MET_CHToCB_pt_nom<=40) && mmCH && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)',
#    'C_mm_3b' : '!isOSpair && (MET_CHToCB_pt_nom<=40) && mmCH && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)',
#    'D_mm_3b' : '!isOSpair  && (MET_CHToCB_pt_nom>40)  && mmCH && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)',
#    'A_em_3b' : 'isOSpair  && (MET_CHToCB_pt_nom>40)  && emCH && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)',
#    'B_em_3b' : 'isOSpair && (MET_CHToCB_pt_nom<=40) && emCH && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)',
#    'C_em_3b' : '!isOSpair && (MET_CHToCB_pt_nom<=40) && emCH && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)',
#    'D_em_3b' : '!isOSpair  && (MET_CHToCB_pt_nom>40)  && emCH && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)',
#    'A_me_3b' : 'isOSpair  && (MET_CHToCB_pt_nom>40)  && meCH && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)',
#    'B_me_3b' : 'isOSpair && (MET_CHToCB_pt_nom<=40) && meCH && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)',
#    'C_me_3b' : '!isOSpair && (MET_CHToCB_pt_nom<=40) && meCH && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)',
#    'D_me_3b' : '!isOSpair  && (MET_CHToCB_pt_nom>40)  && meCH && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)',
#  },
#}


#cuts['isVBF']='isVBF'
print "Ncuts=",len(cuts)

