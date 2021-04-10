#hadd.root:/sng_4j_A_muCH_2b/EleSCEta
#hadd.root:/sng_4j_A_muCH_2b/MuonEta
#hadd.root:/sng_4j_A_muCH_2b/Event
#hadd.root:/sng_4j_A_muCH_2b/fitted_dijet_M
#hadd.root:/sng_4j_A_muCH_2b/fitted_dijet_M_down_type_jet_b_tagged
#hadd.root:/sng_4j_A_muCH_2b/fitted_dijet_M_high
#hadd.root:/sng_4j_A_muCH_2b/fitted_dijet_M_high_down_type_jet_b_tagged
#hadd.root:/sng_4j_A_muCH_2b/fitted_dijet_M_high_had_top_pt_gt_120_down_type_jet_b_tagged
#hadd.root:/sng_4j_A_muCH_2b/fitted_dijet_M_high_had_top_pt_gt_80_down_type_jet_b_tagged
#QCD_MU, QCD_EM, QCD_bcToE
import ROOT
import numpy as np

fileName='rootFile_2016_SKIM7_QCD_ABCD/hadd.root'
f = ROOT.TFile(fileName,'READ') 

outFileName = 'ABCD_data_driven_SF.root'
outFile =  ROOT.TFile(outFileName,'RECREATE')

#histo_DATA
#histo_DY
#histo_ST
#histo_TTLJ_jj
#histo_TTLJ_cc
#histo_TTLJ_bj
#histo_TTLJ_bb
#histo_TTLL_jj
#histo_TTLL_cc
#histo_TTLL_bj
#histo_TTLL_bb
#histo_TTWjets
#histo_TTZjets
#histo_Wjets
#histo_WW
#histo_WZ
#histo_ZZ     

samples = [
  'histo_DATA',
  'histo_DY',
  'histo_ST',
  'histo_TTLJ_jj',
  'histo_TTLJ_cc',
  'histo_TTLJ_bj',
  'histo_TTLJ_bb',
  'histo_TTLL_jj',
  'histo_TTLL_cc',
  'histo_TTLL_bj',
  'histo_TTLL_bb',
  'histo_TTWjets',
  'histo_TTZjets',
  'histo_Wjets',
  'histo_WW',
  'histo_WZ',
  'histo_ZZ',
]


cuts_variables = {
  'sng_4j_eleCH_2b' : ['EleSCEta',],
  'sng_4j_eleCH_3b' : ['EleSCEta',],
  'sng_4j_muCH_2b'  : ['MuonEta',],
  'sng_4j_muCH_3b'  : ['MuonEta',],
  #'dbl_2j_eeORmmORemORme_2b' : ['EleSCEta_2l','MuonEta_2l'],
  #'dbl_2j_eeORmmORemORme_3b' : ['EleSCEta_2l','MuonEta_2l'],
  #'dbl_2j_ee_2b' : ['mll'],
  #'dbl_2j_em_2b' : ['mll'],
  #'dbl_2j_me_2b' : ['mll'],
  #'dbl_2j_mm_2b' : ['mll'],
  #'dbl_2j_ee_3b' : ['mll'],
  #'dbl_2j_em_3b' : ['mll'],
  #'dbl_2j_me_3b' : ['mll'],
  #'dbl_2j_mm_3b' : ['mll'],
}

chennels = {}

for cut in cuts_variables:
  chennels[cut] = {}
  chennels[cut]['A'] = {}
  chennels[cut]['B'] = {}
  chennels[cut]['C'] = {}
  for var in cuts_variables[cut]:
    chennels[cut]['A'][var] = []
    chennels[cut]['B'][var] = []
    chennels[cut]['C'][var] = []
    for sample in samples:
      if 'sng_4j' in cut or ('dbl_2j' in cut and 'eeORmmORemORme' not in cut):
        histo_path_A = cut[:7] + 'A_' + cut[7:] + '/' + var + '/' + sample
        histo_path_B = cut[:7] + 'B_' + cut[7:] + '/' + var + '/' + sample
        histo_path_C = cut[:7] + 'C_' + cut[7:] + '/' + var + '/' + sample
        # just for a test
        #histo_path_C = cut[:7] + 'isoDown_C_' + cut[7:] + '/' + var + '/' + sample
      if 'dbl_2j_eeORmmORemORme' in cut:
        histo_path_A = cut[:22] + 'A_' + cut[22:] + '/' + var + '/' + sample
        histo_path_B = cut[:22] + 'B_' + cut[22:] + '/' + var + '/' + sample
        histo_path_C = cut[:22] + 'C_' + cut[22:] + '/' + var + '/' + sample
      chennels[cut]['A'][var].append(histo_path_A)
      chennels[cut]['B'][var].append(histo_path_B)
      chennels[cut]['C'][var].append(histo_path_C)



#chennels = {
#  'sng_4j_eleCH_2b' : {
#        'B' : [
#                'sng_4j_B_eleCH_2b/EleSCEta/histo_DATA',
#                'sng_4j_B_eleCH_2b/EleSCEta/histo_DY',
#                'sng_4j_B_eleCH_2b/EleSCEta/histo_ST',
#                'sng_4j_B_eleCH_2b/EleSCEta/histo_TTLJ_jj',
#                'sng_4j_B_eleCH_2b/EleSCEta/histo_TTLJ_cc',
#                'sng_4j_B_eleCH_2b/EleSCEta/histo_TTLJ_bj',
#                'sng_4j_B_eleCH_2b/EleSCEta/histo_TTLJ_bb',
#                'sng_4j_B_eleCH_2b/EleSCEta/histo_TTLL_jj',
#                'sng_4j_B_eleCH_2b/EleSCEta/histo_TTLL_cc',
#                'sng_4j_B_eleCH_2b/EleSCEta/histo_TTLL_bj',
#                'sng_4j_B_eleCH_2b/EleSCEta/histo_TTLL_bb',
#                'sng_4j_B_eleCH_2b/EleSCEta/histo_TTWjets',
#                'sng_4j_B_eleCH_2b/EleSCEta/histo_TTZjets',
#                'sng_4j_B_eleCH_2b/EleSCEta/histo_Wjets',
#                'sng_4j_B_eleCH_2b/EleSCEta/histo_WW',
#                'sng_4j_B_eleCH_2b/EleSCEta/histo_WZ',
#                'sng_4j_B_eleCH_2b/EleSCEta/histo_ZZ',
#            ],
#        'C' : [
#                'sng_4j_C_eleCH_2b/EleSCEta/histo_DATA',
#                'sng_4j_C_eleCH_2b/EleSCEta/histo_DY',
#                'sng_4j_C_eleCH_2b/EleSCEta/histo_ST',
#                'sng_4j_C_eleCH_2b/EleSCEta/histo_TTLJ_jj',
#                'sng_4j_C_eleCH_2b/EleSCEta/histo_TTLJ_cc',
#                'sng_4j_C_eleCH_2b/EleSCEta/histo_TTLJ_bj',
#                'sng_4j_C_eleCH_2b/EleSCEta/histo_TTLJ_bb',
#                'sng_4j_C_eleCH_2b/EleSCEta/histo_TTLL_jj',
#                'sng_4j_C_eleCH_2b/EleSCEta/histo_TTLL_cc',
#                'sng_4j_C_eleCH_2b/EleSCEta/histo_TTLL_bj',
#                'sng_4j_C_eleCH_2b/EleSCEta/histo_TTLL_bb',
#                'sng_4j_C_eleCH_2b/EleSCEta/histo_TTWjets',
#                'sng_4j_C_eleCH_2b/EleSCEta/histo_TTZjets',
#                'sng_4j_C_eleCH_2b/EleSCEta/histo_Wjets',
#                'sng_4j_C_eleCH_2b/EleSCEta/histo_WW',
#                'sng_4j_C_eleCH_2b/EleSCEta/histo_WZ',
#                'sng_4j_C_eleCH_2b/EleSCEta/histo_ZZ',
#
#            ],
#      },
#  'sng_4j_eleCH_3b' : {
#        'B' : [
#                'sng_4j_B_eleCH_3b/EleSCEta/histo_DATA',
#                'sng_4j_B_eleCH_3b/EleSCEta/histo_DY',
#                'sng_4j_B_eleCH_3b/EleSCEta/histo_ST',
#                'sng_4j_B_eleCH_3b/EleSCEta/histo_TTLJ_jj',
#                'sng_4j_B_eleCH_3b/EleSCEta/histo_TTLJ_cc',
#                'sng_4j_B_eleCH_3b/EleSCEta/histo_TTLJ_bj',
#                'sng_4j_B_eleCH_3b/EleSCEta/histo_TTLJ_bb',
#                'sng_4j_B_eleCH_3b/EleSCEta/histo_TTLL_jj',
#                'sng_4j_B_eleCH_3b/EleSCEta/histo_TTLL_cc',
#                'sng_4j_B_eleCH_3b/EleSCEta/histo_TTLL_bj',
#                'sng_4j_B_eleCH_3b/EleSCEta/histo_TTLL_bb',
#                'sng_4j_B_eleCH_3b/EleSCEta/histo_TTWjets',
#                'sng_4j_B_eleCH_3b/EleSCEta/histo_TTZjets',
#                'sng_4j_B_eleCH_3b/EleSCEta/histo_Wjets',
#                'sng_4j_B_eleCH_3b/EleSCEta/histo_WW',
#                'sng_4j_B_eleCH_3b/EleSCEta/histo_WZ',
#                'sng_4j_B_eleCH_3b/EleSCEta/histo_ZZ',
#            ],
#        'C' : [
#                'sng_4j_C_eleCH_3b/EleSCEta/histo_DATA',
#                'sng_4j_C_eleCH_3b/EleSCEta/histo_DY',
#                'sng_4j_C_eleCH_3b/EleSCEta/histo_ST',
#                'sng_4j_C_eleCH_3b/EleSCEta/histo_TTLJ_jj',
#                'sng_4j_C_eleCH_3b/EleSCEta/histo_TTLJ_cc',
#                'sng_4j_C_eleCH_3b/EleSCEta/histo_TTLJ_bj',
#                'sng_4j_C_eleCH_3b/EleSCEta/histo_TTLJ_bb',
#                'sng_4j_C_eleCH_3b/EleSCEta/histo_TTLL_jj',
#                'sng_4j_C_eleCH_3b/EleSCEta/histo_TTLL_cc',
#                'sng_4j_C_eleCH_3b/EleSCEta/histo_TTLL_bj',
#                'sng_4j_C_eleCH_3b/EleSCEta/histo_TTLL_bb',
#                'sng_4j_C_eleCH_3b/EleSCEta/histo_TTWjets',
#                'sng_4j_C_eleCH_3b/EleSCEta/histo_TTZjets',
#                'sng_4j_C_eleCH_3b/EleSCEta/histo_Wjets',
#                'sng_4j_C_eleCH_3b/EleSCEta/histo_WW',
#                'sng_4j_C_eleCH_3b/EleSCEta/histo_WZ',
#                'sng_4j_C_eleCH_3b/EleSCEta/histo_ZZ',
#
#            ],
#      },
#  'sng_4j_muCH_2b'  : {
#        'B' : [
#                'sng_4j_B_muCH_2b/MuonEta/histo_DATA',
#                'sng_4j_B_muCH_2b/MuonEta/histo_DY',
#                'sng_4j_B_muCH_2b/MuonEta/histo_ST',
#                'sng_4j_B_muCH_2b/MuonEta/histo_TTLJ_jj',
#                'sng_4j_B_muCH_2b/MuonEta/histo_TTLJ_cc',
#                'sng_4j_B_muCH_2b/MuonEta/histo_TTLJ_bj',
#                'sng_4j_B_muCH_2b/MuonEta/histo_TTLJ_bb',
#                'sng_4j_B_muCH_2b/MuonEta/histo_TTLL_jj',
#                'sng_4j_B_muCH_2b/MuonEta/histo_TTLL_cc',
#                'sng_4j_B_muCH_2b/MuonEta/histo_TTLL_bj',
#                'sng_4j_B_muCH_2b/MuonEta/histo_TTLL_bb',
#                'sng_4j_B_muCH_2b/MuonEta/histo_TTWjets',
#                'sng_4j_B_muCH_2b/MuonEta/histo_TTZjets',
#                'sng_4j_B_muCH_2b/MuonEta/histo_Wjets',
#                'sng_4j_B_muCH_2b/MuonEta/histo_WW',
#                'sng_4j_B_muCH_2b/MuonEta/histo_WZ',
#                'sng_4j_B_muCH_2b/MuonEta/histo_ZZ',
#            ],
#        'C' : [
#                'sng_4j_C_muCH_2b/MuonEta/histo_DATA',
#                'sng_4j_C_muCH_2b/MuonEta/histo_DY',
#                'sng_4j_C_muCH_2b/MuonEta/histo_ST',
#                'sng_4j_C_muCH_2b/MuonEta/histo_TTLJ_jj',
#                'sng_4j_C_muCH_2b/MuonEta/histo_TTLJ_cc',
#                'sng_4j_C_muCH_2b/MuonEta/histo_TTLJ_bj',
#                'sng_4j_C_muCH_2b/MuonEta/histo_TTLJ_bb',
#                'sng_4j_C_muCH_2b/MuonEta/histo_TTLL_jj',
#                'sng_4j_C_muCH_2b/MuonEta/histo_TTLL_cc',
#                'sng_4j_C_muCH_2b/MuonEta/histo_TTLL_bj',
#                'sng_4j_C_muCH_2b/MuonEta/histo_TTLL_bb',
#                'sng_4j_C_muCH_2b/MuonEta/histo_TTWjets',
#                'sng_4j_C_muCH_2b/MuonEta/histo_TTZjets',
#                'sng_4j_C_muCH_2b/MuonEta/histo_Wjets',
#                'sng_4j_C_muCH_2b/MuonEta/histo_WW',
#                'sng_4j_C_muCH_2b/MuonEta/histo_WZ',
#                'sng_4j_C_muCH_2b/MuonEta/histo_ZZ',
#            ],
#      },
#  'sng_4j_muCH_3b'  : {
#        'B' : [
#                'sng_4j_B_muCH_3b/MuonEta/histo_DATA',
#                'sng_4j_B_muCH_3b/MuonEta/histo_DY',
#                'sng_4j_B_muCH_3b/MuonEta/histo_ST',
#                'sng_4j_B_muCH_3b/MuonEta/histo_TTLJ_jj',
#                'sng_4j_B_muCH_3b/MuonEta/histo_TTLJ_cc',
#                'sng_4j_B_muCH_3b/MuonEta/histo_TTLJ_bj',
#                'sng_4j_B_muCH_3b/MuonEta/histo_TTLJ_bb',
#                'sng_4j_B_muCH_3b/MuonEta/histo_TTLL_jj',
#                'sng_4j_B_muCH_3b/MuonEta/histo_TTLL_cc',
#                'sng_4j_B_muCH_3b/MuonEta/histo_TTLL_bj',
#                'sng_4j_B_muCH_3b/MuonEta/histo_TTLL_bb',
#                'sng_4j_B_muCH_3b/MuonEta/histo_TTWjets',
#                'sng_4j_B_muCH_3b/MuonEta/histo_TTZjets',
#                'sng_4j_B_muCH_3b/MuonEta/histo_Wjets',
#                'sng_4j_B_muCH_3b/MuonEta/histo_WW',
#                'sng_4j_B_muCH_3b/MuonEta/histo_WZ',
#                'sng_4j_B_muCH_3b/MuonEta/histo_ZZ',
#            ],
#        'C' : [
#                'sng_4j_C_muCH_3b/MuonEta/histo_DATA',
#                'sng_4j_C_muCH_3b/MuonEta/histo_DY',
#                'sng_4j_C_muCH_3b/MuonEta/histo_ST',
#                'sng_4j_C_muCH_3b/MuonEta/histo_TTLJ_jj',
#                'sng_4j_C_muCH_3b/MuonEta/histo_TTLJ_cc',
#                'sng_4j_C_muCH_3b/MuonEta/histo_TTLJ_bj',
#                'sng_4j_C_muCH_3b/MuonEta/histo_TTLJ_bb',
#                'sng_4j_C_muCH_3b/MuonEta/histo_TTLL_jj',
#                'sng_4j_C_muCH_3b/MuonEta/histo_TTLL_cc',
#                'sng_4j_C_muCH_3b/MuonEta/histo_TTLL_bj',
#                'sng_4j_C_muCH_3b/MuonEta/histo_TTLL_bb',
#                'sng_4j_C_muCH_3b/MuonEta/histo_TTWjets',
#                'sng_4j_C_muCH_3b/MuonEta/histo_TTZjets',
#                'sng_4j_C_muCH_3b/MuonEta/histo_Wjets',
#                'sng_4j_C_muCH_3b/MuonEta/histo_WW',
#                'sng_4j_C_muCH_3b/MuonEta/histo_WZ',
#                'sng_4j_C_muCH_3b/MuonEta/histo_ZZ',
#            ],
#
#      },
#
#  'dbl_2j_ee_2b' : {
#      'A' : [
#              'dbl_2j_A_ee_2b/EleSCEta/histo_DATA',
#              'dbl_2j_A_ee_2b/EleSCEta/histo_DY',
#              'dbl_2j_A_ee_2b/EleSCEta/histo_ST',
#              'dbl_2j_A_ee_2b/EleSCEta/histo_TTLJ_jj',
#              'dbl_2j_A_ee_2b/EleSCEta/histo_TTLJ_cc',
#              'dbl_2j_A_ee_2b/EleSCEta/histo_TTLJ_bj',
#              'dbl_2j_A_ee_2b/EleSCEta/histo_TTLJ_bb',
#              'dbl_2j_A_ee_2b/EleSCEta/histo_TTLL_jj',
#              'dbl_2j_A_ee_2b/EleSCEta/histo_TTLL_cc',
#              'dbl_2j_A_ee_2b/EleSCEta/histo_TTLL_bj',
#              'dbl_2j_A_ee_2b/EleSCEta/histo_TTLL_bb',
#              'dbl_2j_A_ee_2b/EleSCEta/histo_TTWjets',
#              'dbl_2j_A_ee_2b/EleSCEta/histo_TTZjets',
#              'dbl_2j_A_ee_2b/EleSCEta/histo_Wjets',
#              'dbl_2j_A_ee_2b/EleSCEta/histo_WW',
#              'dbl_2j_A_ee_2b/EleSCEta/histo_WZ',
#              'dbl_2j_A_ee_2b/EleSCEta/histo_ZZ',
#          ],
#      'B' : [
#              'dbl_2j_B_ee_2b/EleSCEta/histo_DATA',
#              'dbl_2j_B_ee_2b/EleSCEta/histo_DY',
#              'dbl_2j_B_ee_2b/EleSCEta/histo_ST',
#              'dbl_2j_B_ee_2b/EleSCEta/histo_TTLJ_jj',
#              'dbl_2j_B_ee_2b/EleSCEta/histo_TTLJ_cc',
#              'dbl_2j_B_ee_2b/EleSCEta/histo_TTLJ_bj',
#              'dbl_2j_B_ee_2b/EleSCEta/histo_TTLJ_bb',
#              'dbl_2j_B_ee_2b/EleSCEta/histo_TTLL_jj',
#              'dbl_2j_B_ee_2b/EleSCEta/histo_TTLL_cc',
#              'dbl_2j_B_ee_2b/EleSCEta/histo_TTLL_bj',
#              'dbl_2j_B_ee_2b/EleSCEta/histo_TTLL_bb',
#              'dbl_2j_B_ee_2b/EleSCEta/histo_TTWjets',
#              'dbl_2j_B_ee_2b/EleSCEta/histo_TTZjets',
#              'dbl_2j_B_ee_2b/EleSCEta/histo_Wjets',
#              'dbl_2j_B_ee_2b/EleSCEta/histo_WW',
#              'dbl_2j_B_ee_2b/EleSCEta/histo_WZ',
#              'dbl_2j_B_ee_2b/EleSCEta/histo_ZZ',
#          ],
#      'C' : [
#              'dbl_2j_C_ee_2b/EleSCEta/histo_DATA',
#              'dbl_2j_C_ee_2b/EleSCEta/histo_DY',
#              'dbl_2j_C_ee_2b/EleSCEta/histo_ST',
#              'dbl_2j_C_ee_2b/EleSCEta/histo_TTLJ_jj',
#              'dbl_2j_C_ee_2b/EleSCEta/histo_TTLJ_cc',
#              'dbl_2j_C_ee_2b/EleSCEta/histo_TTLJ_bj',
#              'dbl_2j_C_ee_2b/EleSCEta/histo_TTLJ_bb',
#              'dbl_2j_C_ee_2b/EleSCEta/histo_TTLL_jj',
#              'dbl_2j_C_ee_2b/EleSCEta/histo_TTLL_cc',
#              'dbl_2j_C_ee_2b/EleSCEta/histo_TTLL_bj',
#              'dbl_2j_C_ee_2b/EleSCEta/histo_TTLL_bb',
#              'dbl_2j_C_ee_2b/EleSCEta/histo_TTWjets',
#              'dbl_2j_C_ee_2b/EleSCEta/histo_TTZjets',
#              'dbl_2j_C_ee_2b/EleSCEta/histo_Wjets',
#              'dbl_2j_C_ee_2b/EleSCEta/histo_WW',
#              'dbl_2j_C_ee_2b/EleSCEta/histo_WZ',
#              'dbl_2j_C_ee_2b/EleSCEta/histo_ZZ',
#          ],
#      'D' : [
#              'dbl_2j_D_ee_2b/EleSCEta/histo_DATA',
#              'dbl_2j_D_ee_2b/EleSCEta/histo_DY',
#              'dbl_2j_D_ee_2b/EleSCEta/histo_ST',
#              'dbl_2j_D_ee_2b/EleSCEta/histo_TTLJ_jj',
#              'dbl_2j_D_ee_2b/EleSCEta/histo_TTLJ_cc',
#              'dbl_2j_D_ee_2b/EleSCEta/histo_TTLJ_bj',
#              'dbl_2j_D_ee_2b/EleSCEta/histo_TTLJ_bb',
#              'dbl_2j_D_ee_2b/EleSCEta/histo_TTLL_jj',
#              'dbl_2j_D_ee_2b/EleSCEta/histo_TTLL_cc',
#              'dbl_2j_D_ee_2b/EleSCEta/histo_TTLL_bj',
#              'dbl_2j_D_ee_2b/EleSCEta/histo_TTLL_bb',
#              'dbl_2j_D_ee_2b/EleSCEta/histo_TTWjets',
#              'dbl_2j_D_ee_2b/EleSCEta/histo_TTZjets',
#              'dbl_2j_D_ee_2b/EleSCEta/histo_Wjets',
#              'dbl_2j_D_ee_2b/EleSCEta/histo_WW',
#              'dbl_2j_D_ee_2b/EleSCEta/histo_WZ',
#              'dbl_2j_D_ee_2b/EleSCEta/histo_ZZ',
#          ],
#  },
#  'dbl_2j_ee_3b' : {
#      'A' : [
#              'dbl_2j_A_ee_3b/EleSCEta/histo_DATA',
#              'dbl_2j_A_ee_3b/EleSCEta/histo_DY',
#              'dbl_2j_A_ee_3b/EleSCEta/histo_ST',
#              'dbl_2j_A_ee_3b/EleSCEta/histo_TTLJ_jj',
#              'dbl_2j_A_ee_3b/EleSCEta/histo_TTLJ_cc',
#              'dbl_2j_A_ee_3b/EleSCEta/histo_TTLJ_bj',
#              'dbl_2j_A_ee_3b/EleSCEta/histo_TTLJ_bb',
#              'dbl_2j_A_ee_3b/EleSCEta/histo_TTLL_jj',
#              'dbl_2j_A_ee_3b/EleSCEta/histo_TTLL_cc',
#              'dbl_2j_A_ee_3b/EleSCEta/histo_TTLL_bj',
#              'dbl_2j_A_ee_3b/EleSCEta/histo_TTLL_bb',
#              'dbl_2j_A_ee_3b/EleSCEta/histo_TTWjets',
#              'dbl_2j_A_ee_3b/EleSCEta/histo_TTZjets',
#              'dbl_2j_A_ee_3b/EleSCEta/histo_Wjets',
#              'dbl_2j_A_ee_3b/EleSCEta/histo_WW',
#              'dbl_2j_A_ee_3b/EleSCEta/histo_WZ',
#              'dbl_2j_A_ee_3b/EleSCEta/histo_ZZ',
#          ],
#      'B' : [
#              'dbl_2j_B_ee_3b/EleSCEta/histo_DATA',
#              'dbl_2j_B_ee_3b/EleSCEta/histo_DY',
#              'dbl_2j_B_ee_3b/EleSCEta/histo_ST',
#              'dbl_2j_B_ee_3b/EleSCEta/histo_TTLJ_jj',
#              'dbl_2j_B_ee_3b/EleSCEta/histo_TTLJ_cc',
#              'dbl_2j_B_ee_3b/EleSCEta/histo_TTLJ_bj',
#              'dbl_2j_B_ee_3b/EleSCEta/histo_TTLJ_bb',
#              'dbl_2j_B_ee_3b/EleSCEta/histo_TTLL_jj',
#              'dbl_2j_B_ee_3b/EleSCEta/histo_TTLL_cc',
#              'dbl_2j_B_ee_3b/EleSCEta/histo_TTLL_bj',
#              'dbl_2j_B_ee_3b/EleSCEta/histo_TTLL_bb',
#              'dbl_2j_B_ee_3b/EleSCEta/histo_TTWjets',
#              'dbl_2j_B_ee_3b/EleSCEta/histo_TTZjets',
#              'dbl_2j_B_ee_3b/EleSCEta/histo_Wjets',
#              'dbl_2j_B_ee_3b/EleSCEta/histo_WW',
#              'dbl_2j_B_ee_3b/EleSCEta/histo_WZ',
#              'dbl_2j_B_ee_3b/EleSCEta/histo_ZZ',
#          ],
#      'C' : [
#              'dbl_2j_C_ee_3b/EleSCEta/histo_DATA',
#              'dbl_2j_C_ee_3b/EleSCEta/histo_DY',
#              'dbl_2j_C_ee_3b/EleSCEta/histo_ST',
#              'dbl_2j_C_ee_3b/EleSCEta/histo_TTLJ_jj',
#              'dbl_2j_C_ee_3b/EleSCEta/histo_TTLJ_cc',
#              'dbl_2j_C_ee_3b/EleSCEta/histo_TTLJ_bj',
#              'dbl_2j_C_ee_3b/EleSCEta/histo_TTLJ_bb',
#              'dbl_2j_C_ee_3b/EleSCEta/histo_TTLL_jj',
#              'dbl_2j_C_ee_3b/EleSCEta/histo_TTLL_cc',
#              'dbl_2j_C_ee_3b/EleSCEta/histo_TTLL_bj',
#              'dbl_2j_C_ee_3b/EleSCEta/histo_TTLL_bb',
#              'dbl_2j_C_ee_3b/EleSCEta/histo_TTWjets',
#              'dbl_2j_C_ee_3b/EleSCEta/histo_TTZjets',
#              'dbl_2j_C_ee_3b/EleSCEta/histo_Wjets',
#              'dbl_2j_C_ee_3b/EleSCEta/histo_WW',
#              'dbl_2j_C_ee_3b/EleSCEta/histo_WZ',
#              'dbl_2j_C_ee_3b/EleSCEta/histo_ZZ',
#          ],
#      'D' : [
#              'dbl_2j_D_ee_3b/EleSCEta/histo_DATA',
#              'dbl_2j_D_ee_3b/EleSCEta/histo_DY',
#              'dbl_2j_D_ee_3b/EleSCEta/histo_ST',
#              'dbl_2j_D_ee_3b/EleSCEta/histo_TTLJ_jj',
#              'dbl_2j_D_ee_3b/EleSCEta/histo_TTLJ_cc',
#              'dbl_2j_D_ee_3b/EleSCEta/histo_TTLJ_bj',
#              'dbl_2j_D_ee_3b/EleSCEta/histo_TTLJ_bb',
#              'dbl_2j_D_ee_3b/EleSCEta/histo_TTLL_jj',
#              'dbl_2j_D_ee_3b/EleSCEta/histo_TTLL_cc',
#              'dbl_2j_D_ee_3b/EleSCEta/histo_TTLL_bj',
#              'dbl_2j_D_ee_3b/EleSCEta/histo_TTLL_bb',
#              'dbl_2j_D_ee_3b/EleSCEta/histo_TTWjets',
#              'dbl_2j_D_ee_3b/EleSCEta/histo_TTZjets',
#              'dbl_2j_D_ee_3b/EleSCEta/histo_Wjets',
#              'dbl_2j_D_ee_3b/EleSCEta/histo_WW',
#              'dbl_2j_D_ee_3b/EleSCEta/histo_WZ',
#              'dbl_2j_D_ee_3b/EleSCEta/histo_ZZ',
#          ],
#  },
#  'dbl_2j_mm_2b' : {
#      'A' : [
#              'dbl_2j_A_mm_2b/MuonEta/histo_DATA',
#              'dbl_2j_A_mm_2b/MuonEta/histo_DY',
#              'dbl_2j_A_mm_2b/MuonEta/histo_ST',
#              'dbl_2j_A_mm_2b/MuonEta/histo_TTLJ_jj',
#              'dbl_2j_A_mm_2b/MuonEta/histo_TTLJ_cc',
#              'dbl_2j_A_mm_2b/MuonEta/histo_TTLJ_bj',
#              'dbl_2j_A_mm_2b/MuonEta/histo_TTLJ_bb',
#              'dbl_2j_A_mm_2b/MuonEta/histo_TTLL_jj',
#              'dbl_2j_A_mm_2b/MuonEta/histo_TTLL_cc',
#              'dbl_2j_A_mm_2b/MuonEta/histo_TTLL_bj',
#              'dbl_2j_A_mm_2b/MuonEta/histo_TTLL_bb',
#              'dbl_2j_A_mm_2b/MuonEta/histo_TTWjets',
#              'dbl_2j_A_mm_2b/MuonEta/histo_TTZjets',
#              'dbl_2j_A_mm_2b/MuonEta/histo_Wjets',
#              'dbl_2j_A_mm_2b/MuonEta/histo_WW',
#              'dbl_2j_A_mm_2b/MuonEta/histo_WZ',
#              'dbl_2j_A_mm_2b/MuonEta/histo_ZZ',
#          ],
#      'B' : [
#              'dbl_2j_B_mm_2b/MuonEta/histo_DATA',
#              'dbl_2j_B_mm_2b/MuonEta/histo_DY',
#              'dbl_2j_B_mm_2b/MuonEta/histo_ST',
#              'dbl_2j_B_mm_2b/MuonEta/histo_TTLJ_jj',
#              'dbl_2j_B_mm_2b/MuonEta/histo_TTLJ_cc',
#              'dbl_2j_B_mm_2b/MuonEta/histo_TTLJ_bj',
#              'dbl_2j_B_mm_2b/MuonEta/histo_TTLJ_bb',
#              'dbl_2j_B_mm_2b/MuonEta/histo_TTLL_jj',
#              'dbl_2j_B_mm_2b/MuonEta/histo_TTLL_cc',
#              'dbl_2j_B_mm_2b/MuonEta/histo_TTLL_bj',
#              'dbl_2j_B_mm_2b/MuonEta/histo_TTLL_bb',
#              'dbl_2j_B_mm_2b/MuonEta/histo_TTWjets',
#              'dbl_2j_B_mm_2b/MuonEta/histo_TTZjets',
#              'dbl_2j_B_mm_2b/MuonEta/histo_Wjets',
#              'dbl_2j_B_mm_2b/MuonEta/histo_WW',
#              'dbl_2j_B_mm_2b/MuonEta/histo_WZ',
#              'dbl_2j_B_mm_2b/MuonEta/histo_ZZ',
#          ],
#      'C' : [
#              'dbl_2j_C_mm_2b/MuonEta/histo_DATA',
#              'dbl_2j_C_mm_2b/MuonEta/histo_DY',
#              'dbl_2j_C_mm_2b/MuonEta/histo_ST',
#              'dbl_2j_C_mm_2b/MuonEta/histo_TTLJ_jj',
#              'dbl_2j_C_mm_2b/MuonEta/histo_TTLJ_cc',
#              'dbl_2j_C_mm_2b/MuonEta/histo_TTLJ_bj',
#              'dbl_2j_C_mm_2b/MuonEta/histo_TTLJ_bb',
#              'dbl_2j_C_mm_2b/MuonEta/histo_TTLL_jj',
#              'dbl_2j_C_mm_2b/MuonEta/histo_TTLL_cc',
#              'dbl_2j_C_mm_2b/MuonEta/histo_TTLL_bj',
#              'dbl_2j_C_mm_2b/MuonEta/histo_TTLL_bb',
#              'dbl_2j_C_mm_2b/MuonEta/histo_TTWjets',
#              'dbl_2j_C_mm_2b/MuonEta/histo_TTZjets',
#              'dbl_2j_C_mm_2b/MuonEta/histo_Wjets',
#              'dbl_2j_C_mm_2b/MuonEta/histo_WW',
#              'dbl_2j_C_mm_2b/MuonEta/histo_WZ',
#              'dbl_2j_C_mm_2b/MuonEta/histo_ZZ',
#          ],
#      'D' : [
#              'dbl_2j_D_mm_2b/MuonEta/histo_DATA',
#              'dbl_2j_D_mm_2b/MuonEta/histo_DY',
#              'dbl_2j_D_mm_2b/MuonEta/histo_ST',
#              'dbl_2j_D_mm_2b/MuonEta/histo_TTLJ_jj',
#              'dbl_2j_D_mm_2b/MuonEta/histo_TTLJ_cc',
#              'dbl_2j_D_mm_2b/MuonEta/histo_TTLJ_bj',
#              'dbl_2j_D_mm_2b/MuonEta/histo_TTLJ_bb',
#              'dbl_2j_D_mm_2b/MuonEta/histo_TTLL_jj',
#              'dbl_2j_D_mm_2b/MuonEta/histo_TTLL_cc',
#              'dbl_2j_D_mm_2b/MuonEta/histo_TTLL_bj',
#              'dbl_2j_D_mm_2b/MuonEta/histo_TTLL_bb',
#              'dbl_2j_D_mm_2b/MuonEta/histo_TTWjets',
#              'dbl_2j_D_mm_2b/MuonEta/histo_TTZjets',
#              'dbl_2j_D_mm_2b/MuonEta/histo_Wjets',
#              'dbl_2j_D_mm_2b/MuonEta/histo_WW',
#              'dbl_2j_D_mm_2b/MuonEta/histo_WZ',
#              'dbl_2j_D_mm_2b/MuonEta/histo_ZZ',
#          ],
#  },
#  'dbl_2j_mm_3b' : {
#      'A' : [
#              'dbl_2j_A_mm_3b/MuonEta/histo_DATA',
#              'dbl_2j_A_mm_3b/MuonEta/histo_DY',
#              'dbl_2j_A_mm_3b/MuonEta/histo_ST',
#              'dbl_2j_A_mm_3b/MuonEta/histo_TTLJ_jj',
#              'dbl_2j_A_mm_3b/MuonEta/histo_TTLJ_cc',
#              'dbl_2j_A_mm_3b/MuonEta/histo_TTLJ_bj',
#              'dbl_2j_A_mm_3b/MuonEta/histo_TTLJ_bb',
#              'dbl_2j_A_mm_3b/MuonEta/histo_TTLL_jj',
#              'dbl_2j_A_mm_3b/MuonEta/histo_TTLL_cc',
#              'dbl_2j_A_mm_3b/MuonEta/histo_TTLL_bj',
#              'dbl_2j_A_mm_3b/MuonEta/histo_TTLL_bb',
#              'dbl_2j_A_mm_3b/MuonEta/histo_TTWjets',
#              'dbl_2j_A_mm_3b/MuonEta/histo_TTZjets',
#              'dbl_2j_A_mm_3b/MuonEta/histo_Wjets',
#              'dbl_2j_A_mm_3b/MuonEta/histo_WW',
#              'dbl_2j_A_mm_3b/MuonEta/histo_WZ',
#              'dbl_2j_A_mm_3b/MuonEta/histo_ZZ',
#          ],
#      'B' : [
#              'dbl_2j_B_mm_3b/MuonEta/histo_DATA',
#              'dbl_2j_B_mm_3b/MuonEta/histo_DY',
#              'dbl_2j_B_mm_3b/MuonEta/histo_ST',
#              'dbl_2j_B_mm_3b/MuonEta/histo_TTLJ_jj',
#              'dbl_2j_B_mm_3b/MuonEta/histo_TTLJ_cc',
#              'dbl_2j_B_mm_3b/MuonEta/histo_TTLJ_bj',
#              'dbl_2j_B_mm_3b/MuonEta/histo_TTLJ_bb',
#              'dbl_2j_B_mm_3b/MuonEta/histo_TTLL_jj',
#              'dbl_2j_B_mm_3b/MuonEta/histo_TTLL_cc',
#              'dbl_2j_B_mm_3b/MuonEta/histo_TTLL_bj',
#              'dbl_2j_B_mm_3b/MuonEta/histo_TTLL_bb',
#              'dbl_2j_B_mm_3b/MuonEta/histo_TTWjets',
#              'dbl_2j_B_mm_3b/MuonEta/histo_TTZjets',
#              'dbl_2j_B_mm_3b/MuonEta/histo_Wjets',
#              'dbl_2j_B_mm_3b/MuonEta/histo_WW',
#              'dbl_2j_B_mm_3b/MuonEta/histo_WZ',
#              'dbl_2j_B_mm_3b/MuonEta/histo_ZZ',
#          ],
#      'C' : [
#              'dbl_2j_C_mm_3b/MuonEta/histo_DATA',
#              'dbl_2j_C_mm_3b/MuonEta/histo_DY',
#              'dbl_2j_C_mm_3b/MuonEta/histo_ST',
#              'dbl_2j_C_mm_3b/MuonEta/histo_TTLJ_jj',
#              'dbl_2j_C_mm_3b/MuonEta/histo_TTLJ_cc',
#              'dbl_2j_C_mm_3b/MuonEta/histo_TTLJ_bj',
#              'dbl_2j_C_mm_3b/MuonEta/histo_TTLJ_bb',
#              'dbl_2j_C_mm_3b/MuonEta/histo_TTLL_jj',
#              'dbl_2j_C_mm_3b/MuonEta/histo_TTLL_cc',
#              'dbl_2j_C_mm_3b/MuonEta/histo_TTLL_bj',
#              'dbl_2j_C_mm_3b/MuonEta/histo_TTLL_bb',
#              'dbl_2j_C_mm_3b/MuonEta/histo_TTWjets',
#              'dbl_2j_C_mm_3b/MuonEta/histo_TTZjets',
#              'dbl_2j_C_mm_3b/MuonEta/histo_Wjets',
#              'dbl_2j_C_mm_3b/MuonEta/histo_WW',
#              'dbl_2j_C_mm_3b/MuonEta/histo_WZ',
#              'dbl_2j_C_mm_3b/MuonEta/histo_ZZ',
#          ],
#      'D' : [
#              'dbl_2j_D_mm_3b/MuonEta/histo_DATA',
#              'dbl_2j_D_mm_3b/MuonEta/histo_DY',
#              'dbl_2j_D_mm_3b/MuonEta/histo_ST',
#              'dbl_2j_D_mm_3b/MuonEta/histo_TTLJ_jj',
#              'dbl_2j_D_mm_3b/MuonEta/histo_TTLJ_cc',
#              'dbl_2j_D_mm_3b/MuonEta/histo_TTLJ_bj',
#              'dbl_2j_D_mm_3b/MuonEta/histo_TTLJ_bb',
#              'dbl_2j_D_mm_3b/MuonEta/histo_TTLL_jj',
#              'dbl_2j_D_mm_3b/MuonEta/histo_TTLL_cc',
#              'dbl_2j_D_mm_3b/MuonEta/histo_TTLL_bj',
#              'dbl_2j_D_mm_3b/MuonEta/histo_TTLL_bb',
#              'dbl_2j_D_mm_3b/MuonEta/histo_TTWjets',
#              'dbl_2j_D_mm_3b/MuonEta/histo_TTZjets',
#              'dbl_2j_D_mm_3b/MuonEta/histo_Wjets',
#              'dbl_2j_D_mm_3b/MuonEta/histo_WW',
#              'dbl_2j_D_mm_3b/MuonEta/histo_WZ',
#              'dbl_2j_D_mm_3b/MuonEta/histo_ZZ',
#          ],
#  },
#  'dbl_2j_me_2b' : {
#      'A' : [
#              'dbl_2j_A_me_2b/MuonEta/histo_DATA',
#              'dbl_2j_A_me_2b/MuonEta/histo_DY',
#              'dbl_2j_A_me_2b/MuonEta/histo_ST',
#              'dbl_2j_A_me_2b/MuonEta/histo_TTLJ_jj',
#              'dbl_2j_A_me_2b/MuonEta/histo_TTLJ_cc',
#              'dbl_2j_A_me_2b/MuonEta/histo_TTLJ_bj',
#              'dbl_2j_A_me_2b/MuonEta/histo_TTLJ_bb',
#              'dbl_2j_A_me_2b/MuonEta/histo_TTLL_jj',
#              'dbl_2j_A_me_2b/MuonEta/histo_TTLL_cc',
#              'dbl_2j_A_me_2b/MuonEta/histo_TTLL_bj',
#              'dbl_2j_A_me_2b/MuonEta/histo_TTLL_bb',
#              'dbl_2j_A_me_2b/MuonEta/histo_TTWjets',
#              'dbl_2j_A_me_2b/MuonEta/histo_TTZjets',
#              'dbl_2j_A_me_2b/MuonEta/histo_Wjets',
#              'dbl_2j_A_me_2b/MuonEta/histo_WW',
#              'dbl_2j_A_me_2b/MuonEta/histo_WZ',
#              'dbl_2j_A_me_2b/MuonEta/histo_ZZ',
#          ],
#      'B' : [
#              'dbl_2j_B_me_2b/MuonEta/histo_DATA',
#              'dbl_2j_B_me_2b/MuonEta/histo_DY',
#              'dbl_2j_B_me_2b/MuonEta/histo_ST',
#              'dbl_2j_B_me_2b/MuonEta/histo_TTLJ_jj',
#              'dbl_2j_B_me_2b/MuonEta/histo_TTLJ_cc',
#              'dbl_2j_B_me_2b/MuonEta/histo_TTLJ_bj',
#              'dbl_2j_B_me_2b/MuonEta/histo_TTLJ_bb',
#              'dbl_2j_B_me_2b/MuonEta/histo_TTLL_jj',
#              'dbl_2j_B_me_2b/MuonEta/histo_TTLL_cc',
#              'dbl_2j_B_me_2b/MuonEta/histo_TTLL_bj',
#              'dbl_2j_B_me_2b/MuonEta/histo_TTLL_bb',
#              'dbl_2j_B_me_2b/MuonEta/histo_TTWjets',
#              'dbl_2j_B_me_2b/MuonEta/histo_TTZjets',
#              'dbl_2j_B_me_2b/MuonEta/histo_Wjets',
#              'dbl_2j_B_me_2b/MuonEta/histo_WW',
#              'dbl_2j_B_me_2b/MuonEta/histo_WZ',
#              'dbl_2j_B_me_2b/MuonEta/histo_ZZ',
#          ],
#      'C' : [
#              'dbl_2j_C_me_2b/MuonEta/histo_DATA',
#              'dbl_2j_C_me_2b/MuonEta/histo_DY',
#              'dbl_2j_C_me_2b/MuonEta/histo_ST',
#              'dbl_2j_C_me_2b/MuonEta/histo_TTLJ_jj',
#              'dbl_2j_C_me_2b/MuonEta/histo_TTLJ_cc',
#              'dbl_2j_C_me_2b/MuonEta/histo_TTLJ_bj',
#              'dbl_2j_C_me_2b/MuonEta/histo_TTLJ_bb',
#              'dbl_2j_C_me_2b/MuonEta/histo_TTLL_jj',
#              'dbl_2j_C_me_2b/MuonEta/histo_TTLL_cc',
#              'dbl_2j_C_me_2b/MuonEta/histo_TTLL_bj',
#              'dbl_2j_C_me_2b/MuonEta/histo_TTLL_bb',
#              'dbl_2j_C_me_2b/MuonEta/histo_TTWjets',
#              'dbl_2j_C_me_2b/MuonEta/histo_TTZjets',
#              'dbl_2j_C_me_2b/MuonEta/histo_Wjets',
#              'dbl_2j_C_me_2b/MuonEta/histo_WW',
#              'dbl_2j_C_me_2b/MuonEta/histo_WZ',
#              'dbl_2j_C_me_2b/MuonEta/histo_ZZ',
#          ],
#      'D' : [
#              'dbl_2j_D_me_2b/MuonEta/histo_DATA',
#              'dbl_2j_D_me_2b/MuonEta/histo_DY',
#              'dbl_2j_D_me_2b/MuonEta/histo_ST',
#              'dbl_2j_D_me_2b/MuonEta/histo_TTLJ_jj',
#              'dbl_2j_D_me_2b/MuonEta/histo_TTLJ_cc',
#              'dbl_2j_D_me_2b/MuonEta/histo_TTLJ_bj',
#              'dbl_2j_D_me_2b/MuonEta/histo_TTLJ_bb',
#              'dbl_2j_D_me_2b/MuonEta/histo_TTLL_jj',
#              'dbl_2j_D_me_2b/MuonEta/histo_TTLL_cc',
#              'dbl_2j_D_me_2b/MuonEta/histo_TTLL_bj',
#              'dbl_2j_D_me_2b/MuonEta/histo_TTLL_bb',
#              'dbl_2j_D_me_2b/MuonEta/histo_TTWjets',
#              'dbl_2j_D_me_2b/MuonEta/histo_TTZjets',
#              'dbl_2j_D_me_2b/MuonEta/histo_Wjets',
#              'dbl_2j_D_me_2b/MuonEta/histo_WW',
#              'dbl_2j_D_me_2b/MuonEta/histo_WZ',
#              'dbl_2j_D_me_2b/MuonEta/histo_ZZ',
#          ],
#  },
#  'dbl_2j_me_3b' : {
#      'A' : [
#              'dbl_2j_A_me_3b/MuonEta/histo_DATA',
#              'dbl_2j_A_me_3b/MuonEta/histo_DY',
#              'dbl_2j_A_me_3b/MuonEta/histo_ST',
#              'dbl_2j_A_me_3b/MuonEta/histo_TTLJ_jj',
#              'dbl_2j_A_me_3b/MuonEta/histo_TTLJ_cc',
#              'dbl_2j_A_me_3b/MuonEta/histo_TTLJ_bj',
#              'dbl_2j_A_me_3b/MuonEta/histo_TTLJ_bb',
#              'dbl_2j_A_me_3b/MuonEta/histo_TTLL_jj',
#              'dbl_2j_A_me_3b/MuonEta/histo_TTLL_cc',
#              'dbl_2j_A_me_3b/MuonEta/histo_TTLL_bj',
#              'dbl_2j_A_me_3b/MuonEta/histo_TTLL_bb',
#              'dbl_2j_A_me_3b/MuonEta/histo_TTWjets',
#              'dbl_2j_A_me_3b/MuonEta/histo_TTZjets',
#              'dbl_2j_A_me_3b/MuonEta/histo_Wjets',
#              'dbl_2j_A_me_3b/MuonEta/histo_WW',
#              'dbl_2j_A_me_3b/MuonEta/histo_WZ',
#              'dbl_2j_A_me_3b/MuonEta/histo_ZZ',
#          ],
#      'B' : [
#              'dbl_2j_B_me_3b/MuonEta/histo_DATA',
#              'dbl_2j_B_me_3b/MuonEta/histo_DY',
#              'dbl_2j_B_me_3b/MuonEta/histo_ST',
#              'dbl_2j_B_me_3b/MuonEta/histo_TTLJ_jj',
#              'dbl_2j_B_me_3b/MuonEta/histo_TTLJ_cc',
#              'dbl_2j_B_me_3b/MuonEta/histo_TTLJ_bj',
#              'dbl_2j_B_me_3b/MuonEta/histo_TTLJ_bb',
#              'dbl_2j_B_me_3b/MuonEta/histo_TTLL_jj',
#              'dbl_2j_B_me_3b/MuonEta/histo_TTLL_cc',
#              'dbl_2j_B_me_3b/MuonEta/histo_TTLL_bj',
#              'dbl_2j_B_me_3b/MuonEta/histo_TTLL_bb',
#              'dbl_2j_B_me_3b/MuonEta/histo_TTWjets',
#              'dbl_2j_B_me_3b/MuonEta/histo_TTZjets',
#              'dbl_2j_B_me_3b/MuonEta/histo_Wjets',
#              'dbl_2j_B_me_3b/MuonEta/histo_WW',
#              'dbl_2j_B_me_3b/MuonEta/histo_WZ',
#              'dbl_2j_B_me_3b/MuonEta/histo_ZZ',
#          ],
#      'C' : [
#              'dbl_2j_C_me_3b/MuonEta/histo_DATA',
#              'dbl_2j_C_me_3b/MuonEta/histo_DY',
#              'dbl_2j_C_me_3b/MuonEta/histo_ST',
#              'dbl_2j_C_me_3b/MuonEta/histo_TTLJ_jj',
#              'dbl_2j_C_me_3b/MuonEta/histo_TTLJ_cc',
#              'dbl_2j_C_me_3b/MuonEta/histo_TTLJ_bj',
#              'dbl_2j_C_me_3b/MuonEta/histo_TTLJ_bb',
#              'dbl_2j_C_me_3b/MuonEta/histo_TTLL_jj',
#              'dbl_2j_C_me_3b/MuonEta/histo_TTLL_cc',
#              'dbl_2j_C_me_3b/MuonEta/histo_TTLL_bj',
#              'dbl_2j_C_me_3b/MuonEta/histo_TTLL_bb',
#              'dbl_2j_C_me_3b/MuonEta/histo_TTWjets',
#              'dbl_2j_C_me_3b/MuonEta/histo_TTZjets',
#              'dbl_2j_C_me_3b/MuonEta/histo_Wjets',
#              'dbl_2j_C_me_3b/MuonEta/histo_WW',
#              'dbl_2j_C_me_3b/MuonEta/histo_WZ',
#              'dbl_2j_C_me_3b/MuonEta/histo_ZZ',
#          ],
#      'D' : [
#              'dbl_2j_D_me_3b/MuonEta/histo_DATA',
#              'dbl_2j_D_me_3b/MuonEta/histo_DY',
#              'dbl_2j_D_me_3b/MuonEta/histo_ST',
#              'dbl_2j_D_me_3b/MuonEta/histo_TTLJ_jj',
#              'dbl_2j_D_me_3b/MuonEta/histo_TTLJ_cc',
#              'dbl_2j_D_me_3b/MuonEta/histo_TTLJ_bj',
#              'dbl_2j_D_me_3b/MuonEta/histo_TTLJ_bb',
#              'dbl_2j_D_me_3b/MuonEta/histo_TTLL_jj',
#              'dbl_2j_D_me_3b/MuonEta/histo_TTLL_cc',
#              'dbl_2j_D_me_3b/MuonEta/histo_TTLL_bj',
#              'dbl_2j_D_me_3b/MuonEta/histo_TTLL_bb',
#              'dbl_2j_D_me_3b/MuonEta/histo_TTWjets',
#              'dbl_2j_D_me_3b/MuonEta/histo_TTZjets',
#              'dbl_2j_D_me_3b/MuonEta/histo_Wjets',
#              'dbl_2j_D_me_3b/MuonEta/histo_WW',
#              'dbl_2j_D_me_3b/MuonEta/histo_WZ',
#              'dbl_2j_D_me_3b/MuonEta/histo_ZZ',
#          ],
#  },
#  'dbl_2j_em_2b' : {
#      'A' : [
#              'dbl_2j_A_em_2b/EleSCEta/histo_DATA',
#              'dbl_2j_A_em_2b/EleSCEta/histo_DY',
#              'dbl_2j_A_em_2b/EleSCEta/histo_ST',
#              'dbl_2j_A_em_2b/EleSCEta/histo_TTLJ_jj',
#              'dbl_2j_A_em_2b/EleSCEta/histo_TTLJ_cc',
#              'dbl_2j_A_em_2b/EleSCEta/histo_TTLJ_bj',
#              'dbl_2j_A_em_2b/EleSCEta/histo_TTLJ_bb',
#              'dbl_2j_A_em_2b/EleSCEta/histo_TTLL_jj',
#              'dbl_2j_A_em_2b/EleSCEta/histo_TTLL_cc',
#              'dbl_2j_A_em_2b/EleSCEta/histo_TTLL_bj',
#              'dbl_2j_A_em_2b/EleSCEta/histo_TTLL_bb',
#              'dbl_2j_A_em_2b/EleSCEta/histo_TTWjets',
#              'dbl_2j_A_em_2b/EleSCEta/histo_TTZjets',
#              'dbl_2j_A_em_2b/EleSCEta/histo_Wjets',
#              'dbl_2j_A_em_2b/EleSCEta/histo_WW',
#              'dbl_2j_A_em_2b/EleSCEta/histo_WZ',
#              'dbl_2j_A_em_2b/EleSCEta/histo_ZZ',
#          ],
#      'B' : [
#              'dbl_2j_B_em_2b/EleSCEta/histo_DATA',
#              'dbl_2j_B_em_2b/EleSCEta/histo_DY',
#              'dbl_2j_B_em_2b/EleSCEta/histo_ST',
#              'dbl_2j_B_em_2b/EleSCEta/histo_TTLJ_jj',
#              'dbl_2j_B_em_2b/EleSCEta/histo_TTLJ_cc',
#              'dbl_2j_B_em_2b/EleSCEta/histo_TTLJ_bj',
#              'dbl_2j_B_em_2b/EleSCEta/histo_TTLJ_bb',
#              'dbl_2j_B_em_2b/EleSCEta/histo_TTLL_jj',
#              'dbl_2j_B_em_2b/EleSCEta/histo_TTLL_cc',
#              'dbl_2j_B_em_2b/EleSCEta/histo_TTLL_bj',
#              'dbl_2j_B_em_2b/EleSCEta/histo_TTLL_bb',
#              'dbl_2j_B_em_2b/EleSCEta/histo_TTWjets',
#              'dbl_2j_B_em_2b/EleSCEta/histo_TTZjets',
#              'dbl_2j_B_em_2b/EleSCEta/histo_Wjets',
#              'dbl_2j_B_em_2b/EleSCEta/histo_WW',
#              'dbl_2j_B_em_2b/EleSCEta/histo_WZ',
#              'dbl_2j_B_em_2b/EleSCEta/histo_ZZ',
#          ],
#      'C' : [
#              'dbl_2j_C_em_2b/EleSCEta/histo_DATA',
#              'dbl_2j_C_em_2b/EleSCEta/histo_DY',
#              'dbl_2j_C_em_2b/EleSCEta/histo_ST',
#              'dbl_2j_C_em_2b/EleSCEta/histo_TTLJ_jj',
#              'dbl_2j_C_em_2b/EleSCEta/histo_TTLJ_cc',
#              'dbl_2j_C_em_2b/EleSCEta/histo_TTLJ_bj',
#              'dbl_2j_C_em_2b/EleSCEta/histo_TTLJ_bb',
#              'dbl_2j_C_em_2b/EleSCEta/histo_TTLL_jj',
#              'dbl_2j_C_em_2b/EleSCEta/histo_TTLL_cc',
#              'dbl_2j_C_em_2b/EleSCEta/histo_TTLL_bj',
#              'dbl_2j_C_em_2b/EleSCEta/histo_TTLL_bb',
#              'dbl_2j_C_em_2b/EleSCEta/histo_TTWjets',
#              'dbl_2j_C_em_2b/EleSCEta/histo_TTZjets',
#              'dbl_2j_C_em_2b/EleSCEta/histo_Wjets',
#              'dbl_2j_C_em_2b/EleSCEta/histo_WW',
#              'dbl_2j_C_em_2b/EleSCEta/histo_WZ',
#              'dbl_2j_C_em_2b/EleSCEta/histo_ZZ',
#          ],
#      'D' : [
#              'dbl_2j_D_em_2b/EleSCEta/histo_DATA',
#              'dbl_2j_D_em_2b/EleSCEta/histo_DY',
#              'dbl_2j_D_em_2b/EleSCEta/histo_ST',
#              'dbl_2j_D_em_2b/EleSCEta/histo_TTLJ_jj',
#              'dbl_2j_D_em_2b/EleSCEta/histo_TTLJ_cc',
#              'dbl_2j_D_em_2b/EleSCEta/histo_TTLJ_bj',
#              'dbl_2j_D_em_2b/EleSCEta/histo_TTLJ_bb',
#              'dbl_2j_D_em_2b/EleSCEta/histo_TTLL_jj',
#              'dbl_2j_D_em_2b/EleSCEta/histo_TTLL_cc',
#              'dbl_2j_D_em_2b/EleSCEta/histo_TTLL_bj',
#              'dbl_2j_D_em_2b/EleSCEta/histo_TTLL_bb',
#              'dbl_2j_D_em_2b/EleSCEta/histo_TTWjets',
#              'dbl_2j_D_em_2b/EleSCEta/histo_TTZjets',
#              'dbl_2j_D_em_2b/EleSCEta/histo_Wjets',
#              'dbl_2j_D_em_2b/EleSCEta/histo_WW',
#              'dbl_2j_D_em_2b/EleSCEta/histo_WZ',
#              'dbl_2j_D_em_2b/EleSCEta/histo_ZZ',
#          ],
#  },
#  'dbl_2j_em_3b' : {
#      'A' : [
#              'dbl_2j_A_em_3b/EleSCEta/histo_DATA',
#              'dbl_2j_A_em_3b/EleSCEta/histo_DY',
#              'dbl_2j_A_em_3b/EleSCEta/histo_ST',
#              'dbl_2j_A_em_3b/EleSCEta/histo_TTLJ_jj',
#              'dbl_2j_A_em_3b/EleSCEta/histo_TTLJ_cc',
#              'dbl_2j_A_em_3b/EleSCEta/histo_TTLJ_bj',
#              'dbl_2j_A_em_3b/EleSCEta/histo_TTLJ_bb',
#              'dbl_2j_A_em_3b/EleSCEta/histo_TTLL_jj',
#              'dbl_2j_A_em_3b/EleSCEta/histo_TTLL_cc',
#              'dbl_2j_A_em_3b/EleSCEta/histo_TTLL_bj',
#              'dbl_2j_A_em_3b/EleSCEta/histo_TTLL_bb',
#              'dbl_2j_A_em_3b/EleSCEta/histo_TTWjets',
#              'dbl_2j_A_em_3b/EleSCEta/histo_TTZjets',
#              'dbl_2j_A_em_3b/EleSCEta/histo_Wjets',
#              'dbl_2j_A_em_3b/EleSCEta/histo_WW',
#              'dbl_2j_A_em_3b/EleSCEta/histo_WZ',
#              'dbl_2j_A_em_3b/EleSCEta/histo_ZZ',
#          ],
#      'B' : [
#              'dbl_2j_B_em_3b/EleSCEta/histo_DATA',
#              'dbl_2j_B_em_3b/EleSCEta/histo_DY',
#              'dbl_2j_B_em_3b/EleSCEta/histo_ST',
#              'dbl_2j_B_em_3b/EleSCEta/histo_TTLJ_jj',
#              'dbl_2j_B_em_3b/EleSCEta/histo_TTLJ_cc',
#              'dbl_2j_B_em_3b/EleSCEta/histo_TTLJ_bj',
#              'dbl_2j_B_em_3b/EleSCEta/histo_TTLJ_bb',
#              'dbl_2j_B_em_3b/EleSCEta/histo_TTLL_jj',
#              'dbl_2j_B_em_3b/EleSCEta/histo_TTLL_cc',
#              'dbl_2j_B_em_3b/EleSCEta/histo_TTLL_bj',
#              'dbl_2j_B_em_3b/EleSCEta/histo_TTLL_bb',
#              'dbl_2j_B_em_3b/EleSCEta/histo_TTWjets',
#              'dbl_2j_B_em_3b/EleSCEta/histo_TTZjets',
#              'dbl_2j_B_em_3b/EleSCEta/histo_Wjets',
#              'dbl_2j_B_em_3b/EleSCEta/histo_WW',
#              'dbl_2j_B_em_3b/EleSCEta/histo_WZ',
#              'dbl_2j_B_em_3b/EleSCEta/histo_ZZ',
#          ],
#      'C' : [
#              'dbl_2j_C_em_3b/EleSCEta/histo_DATA',
#              'dbl_2j_C_em_3b/EleSCEta/histo_DY',
#              'dbl_2j_C_em_3b/EleSCEta/histo_ST',
#              'dbl_2j_C_em_3b/EleSCEta/histo_TTLJ_jj',
#              'dbl_2j_C_em_3b/EleSCEta/histo_TTLJ_cc',
#              'dbl_2j_C_em_3b/EleSCEta/histo_TTLJ_bj',
#              'dbl_2j_C_em_3b/EleSCEta/histo_TTLJ_bb',
#              'dbl_2j_C_em_3b/EleSCEta/histo_TTLL_jj',
#              'dbl_2j_C_em_3b/EleSCEta/histo_TTLL_cc',
#              'dbl_2j_C_em_3b/EleSCEta/histo_TTLL_bj',
#              'dbl_2j_C_em_3b/EleSCEta/histo_TTLL_bb',
#              'dbl_2j_C_em_3b/EleSCEta/histo_TTWjets',
#              'dbl_2j_C_em_3b/EleSCEta/histo_TTZjets',
#              'dbl_2j_C_em_3b/EleSCEta/histo_Wjets',
#              'dbl_2j_C_em_3b/EleSCEta/histo_WW',
#              'dbl_2j_C_em_3b/EleSCEta/histo_WZ',
#              'dbl_2j_C_em_3b/EleSCEta/histo_ZZ',
#          ],
#      'D' : [
#              'dbl_2j_D_em_3b/EleSCEta/histo_DATA',
#              'dbl_2j_D_em_3b/EleSCEta/histo_DY',
#              'dbl_2j_D_em_3b/EleSCEta/histo_ST',
#              'dbl_2j_D_em_3b/EleSCEta/histo_TTLJ_jj',
#              'dbl_2j_D_em_3b/EleSCEta/histo_TTLJ_cc',
#              'dbl_2j_D_em_3b/EleSCEta/histo_TTLJ_bj',
#              'dbl_2j_D_em_3b/EleSCEta/histo_TTLJ_bb',
#              'dbl_2j_D_em_3b/EleSCEta/histo_TTLL_jj',
#              'dbl_2j_D_em_3b/EleSCEta/histo_TTLL_cc',
#              'dbl_2j_D_em_3b/EleSCEta/histo_TTLL_bj',
#              'dbl_2j_D_em_3b/EleSCEta/histo_TTLL_bb',
#              'dbl_2j_D_em_3b/EleSCEta/histo_TTWjets',
#              'dbl_2j_D_em_3b/EleSCEta/histo_TTZjets',
#              'dbl_2j_D_em_3b/EleSCEta/histo_Wjets',
#              'dbl_2j_D_em_3b/EleSCEta/histo_WW',
#              'dbl_2j_D_em_3b/EleSCEta/histo_WZ',
#              'dbl_2j_D_em_3b/EleSCEta/histo_ZZ',
#          ],
#  },
#}

#from pprint import pprint
#pprint(chennels)
#raise Exception()

import copy
input_dict = {}
input_dict[''] = copy.deepcopy(chennels)

nuisances = [
        'btag_lfUp',
        'btag_lfDown',
        'btag_hfUp',
        'btag_hfDown',
        'btag_hfstats1_2016Up',
        'btag_hfstats1_2016Down',
        'btag_hfstats2_2016Up',
        'btag_hfstats2_2016Down',
        'btag_lfstats1_2016Up',
        'btag_lfstats1_2016Down',
        'btag_lfstats2_2016Up',
        'btag_lfstats2_2016Down',
        'btag_cferr1Up',
        'btag_cferr1Down',
        'btag_cferr2Up',
        'btag_cferr2Down',
        'ttbbUp',
        'ttbbDown',
        'ttccUp',
        'ttccDown',
        'ttXsecUp',
        'ttXsecDown',
        'isoVar',
        'binningVar',
        ]

exclude_envelop = [
        'ttXsecUp',
        'ttXsecDown',
        'isoVar',
        'binningVar',
        ]

for nuisance in nuisances:
  input_dict[nuisance] = copy.deepcopy(input_dict[''])
  for ch in input_dict[nuisance]:
    for region in input_dict[nuisance][ch]:
      for var in input_dict[nuisance][ch][region]:
        for i, histo_name in enumerate(input_dict[nuisance][ch][region][var]):
          if 'histo_DATA' in histo_name:
              histo_name_nuis = histo_name[:] #[:] to deepcopy
          elif 'isoVar' in nuisance or 'binningVar' in nuisance:
            histo_name_nuis = histo_name[:] #[:] to deepcopy
          else:
            histo_name_nuis = histo_name + '_' + nuisance
          # special treatment for isoVar syst.
          if 'isoVar' in nuisance:
            if 'sng_' in histo_name_nuis and '_C_' in histo_name_nuis:
              histo_name_nuis = histo_name_nuis.replace('_C_','_isoDown_C_')
            #print(nuisance, ch, region, var, i, histo_name_nuis)

          input_dict[nuisance][ch][region][var][i] = histo_name_nuis


bins = {
   #'sng_4j_eleCH_2b' : np.array([-2.5, -1.48, 0, 1.48, 2.5]),
   'sng_4j_eleCH_2b' : np.array([-2.5, -2.1, -1.48, -0.5, 0, 0.5, 1.48, 2.1, 2.5]),
   'sng_4j_eleCH_3b' : np.array([-2.5, -1.48, 0, 1.48, 2.5]),
   'sng_4j_muCH_2b'  : np.array([-2.4, -1.2, -0.9, 0, 0.9, 1.2, 2.4]),
   'sng_4j_muCH_3b'  : np.array([-2.4, -1.2, -0.9, 0, 0.9, 1.2, 2.4]),
   #'dbl_2j_ee_2b'    : np.array([0.,10.,30.,50.,60.,70,90,100,110.,130,150.,175,200.]),
   #'dbl_2j_ee_3b'    : np.array([0.,10.,30.,50.,60.,70,90,100,110.,130,150.,175,200.]),
   #'dbl_2j_mm_2b'    : np.array([0.,10.,30.,50.,60.,70,90,100,110.,130,150.,175,200.]),
   #'dbl_2j_mm_3b'    : np.array([0.,10.,30.,50.,60.,70,90,100,110.,130,150.,175,200.]),
   #'dbl_2j_em_2b'    : np.array([0.,10.,30.,50.,60.,70,90,100,110.,130,150.,175,200.]),
   #'dbl_2j_em_3b'    : np.array([0.,10.,30.,50.,60.,70,90,100,110.,130,150.,175,200.]),
   #'dbl_2j_me_2b'    : np.array([0.,10.,30.,50.,60.,70,90,100,110.,130,150.,175,200.]),
   #'dbl_2j_me_3b'    : np.array([0.,10.,30.,50.,60.,70,90,100,110.,130,150.,175,200.]),

   #'dbl_2j_eeORmmORemORme_2b' : np.array([-2.4, -1.7, -0.9, 0, 0.9, 1.7, 2.4]),
   #'dbl_2j_eeORmmORemORme_3b' : np.array([-2.4, -1.7, -0.9, 0, 0.9, 1.7, 2.4]),

   #'dbl_2j_ee_2b'    : np.array([0.,2.]),
   #'dbl_2j_ee_3b'    : np.array([0.,2.]),
   #'dbl_2j_mm_2b'    : np.array([0.,2.]),
   #'dbl_2j_mm_3b'    : np.array([0.,2.]),
   #'dbl_2j_em_2b'    : np.array([0.,2.]),
   #'dbl_2j_em_3b'    : np.array([0.,2.]),
   #'dbl_2j_me_2b'    : np.array([0.,2.]),
   #'dbl_2j_me_3b'    : np.array([0.,2.]),
}

bins_syst = {
   #'sng_4j_eleCH_2b' : np.array([-2.5, -1.48, 0, 1.48, 2.5]),
   'sng_4j_eleCH_2b' : np.array([-2.5, -2.1, -1.7, -1.48, -0.9, -0.5, 0, 0.5, 0.9, 1.48, 1.7, 2.1, 2.5]),
   'sng_4j_eleCH_3b' : np.array([-2.5, -1.48, 0, 1.48, 2.5]),
   'sng_4j_muCH_2b'  : np.array([-2.4, -2.1, -1.2, -0.9, -0.3, 0, 0.3,0.9, 1.2, 2.1, 2.4]),
   'sng_4j_muCH_3b'  : np.array([-2.4, -1.2, -0.9, 0, 0.9, 1.2, 2.4]),
   #'dbl_2j_ee_2b'    : np.array([0.,10.,20.,30.,40.,50.,55.,60.,65.,70,90,95,100,105,110.,120,130,140,150.,160,180,200.]),
   #'dbl_2j_ee_3b'    : np.array([0.,10.,20.,30.,40.,50.,55.,60.,65.,70,90,95,100,105,110.,120,130,140,150.,160,180,200.]),
   #'dbl_2j_mm_2b'    : np.array([0.,10.,20.,30.,40.,50.,55.,60.,65.,70,90,95,100,105,110.,120,130,140,150.,160,180,200.]),
   #'dbl_2j_mm_3b'    : np.array([0.,10.,20.,30.,40.,50.,55.,60.,65.,70,90,95,100,105,110.,120,130,140,150.,160,180,200.]),
   #'dbl_2j_em_2b'    : np.array([0.,10.,20.,30.,40.,50.,55.,60.,65.,70,90,95,100,105,110.,120,130,140,150.,160,180,200.]),
   #'dbl_2j_em_3b'    : np.array([0.,10.,20.,30.,40.,50.,55.,60.,65.,70,90,95,100,105,110.,120,130,140,150.,160,180,200.]),
   #'dbl_2j_me_2b'    : np.array([0.,10.,20.,30.,40.,50.,55.,60.,65.,70,90,95,100,105,110.,120,130,140,150.,160,180,200.]),
   #'dbl_2j_me_3b'    : np.array([0.,10.,20.,30.,40.,50.,55.,60.,65.,70,90,95,100,105,110.,120,130,140,150.,160,180,200.]),

   #'dbl_2j_eeORmmORemORme_2b' : np.array([-2.4, -2.1, -1.7, -1.48, -0.9, -0.5, 0, 0.5, 0.9, 1.48, 1.7, 2.1, 2.4]),
   #'dbl_2j_eeORmmORemORme_3b' : np.array([-2.4, -2.1, -1.7, -1.48, -0.9, -0.5, 0, 0.5, 0.9, 1.48, 1.7, 2.1, 2.4]),

   #'dbl_2j_ee_2b'    : np.array([0.,2.]),
   #'dbl_2j_ee_3b'    : np.array([0.,2.]),
   #'dbl_2j_mm_2b'    : np.array([0.,2.]),
   #'dbl_2j_mm_3b'    : np.array([0.,2.]),
   #'dbl_2j_em_2b'    : np.array([0.,2.]),
   #'dbl_2j_em_3b'    : np.array([0.,2.]),
   #'dbl_2j_me_2b'    : np.array([0.,2.]),
   #'dbl_2j_me_3b'    : np.array([0.,2.]),
}

def GetHisto(histoNameList, rebin, tag_key, rescale):
  histo_rebinned = None
  norm_data = 1.
  norm_mc   = 1.
  ratio     = 1.
  for histoName in histoNameList:
    #print(histoName)
    if 'ttbb' in histoName or 'ttcc' in histoName or 'ttXsec' in histoName:
        histo_ = f.Get('_'.join(histoName.split('_')[:-1]))
    else:
      histo_ = f.Get(histoName)

    histo = histo_.Clone(histo_.GetName()+'_'+tag_key)

    if histo_rebinned == None:
      if 'histo_DATA' not in histoName:
        raise Exception('first entry should be histo_DATA')
      histo_rebinned = histo.Rebin(rebin.size-1, histo.GetName()+'_rebinned'+tag_key, rebin)
      norm_data = histo_rebinned.Integral()
    else:
      if 'histo_DATA' in histoName:
        raise Exception('histo_DATA is entered for the negative summation')
      # scale ttbar samples
      if 'histo_TTLL_' in histoName or 'histo_TTLJ_' in histoName:

        # ttbb ttcc scale
        if '_bb' in histoName or '_bj' in histoName:
          if '_ttbbUp' in histoName:
            scale = 1.5
          elif '_ttbbDown' in histoName:
            scale = 1.
          else:
            scale = 1.2
        elif '_cc' in histoName:
          if '_ttccUp' in histoName:
            scale = 1.2
          elif '_ttccDown' in histoName:
            scale = 1./1.2
          else:
            scale = 1.0
        elif '_jj' in histoName:
          if '_ttbbUp' in histoName:
            scale = 1.0
            #scale = 0.99247 #((364.35-1.3*(1.433+6.782)-1.0*28.21)/(327.93))
          elif '_ttbbDown' in histoName:
            scale = 1.0
            #scale = 1.0058  #((364.35-(1./1.3)*(1.433+6.782)-1.0*28.21)/(327.93))
          elif '_ttccUp' in histoName:
            scale = 1.0
            #scale = 0.97418 #((364.35-1.0*(1.433+6.782)-1.3*28.21)/(327.93))
          elif '_ttccDown' in histoName:
            scale = 1.0
            #scale = 1.0198  #((364.35-1.0*(1.433+6.782)-(1./1.3)*28.21)/(327.93))
          else:
            scale = 1.0 
        else:
          raise Exception('unsupported ttbar category')
        # ttXsec scale
        if '_ttXsecUp' in histoName:
          scale = 1.06114
        elif '_ttXsecDown' in histoName:
          scale = 1./1.06114
        #print("%s   :     %f"%(histoName, scale))
        histo.Scale(scale)
      histo.Scale(rescale)
      histo_rebinned.Add(histo.Rebin(rebin.size-1, histo.GetName()+'_rebinned'+tag_key, rebin), -1)
  norm_mc = norm_data - histo_rebinned.Integral()
  ratio = norm_data/norm_mc

  return histo_rebinned, ratio

def truncated_normal_mean(mu, sigma):
  # probability distribution truncating below zero
  pi = ROOT.TMath.Pi()
  if sigma <= 0:
    mean = mu
  else:
    mean = mu + (1/ROOT.TMath.Sqrt(2*pi))*ROOT.TMath.Exp(-1/2*(-mu/sigma)**2)/(1-1/2*(1+ROOT.TMath.Erf(-mu/(2**(1/2)*pi))))
  return mean


def SuppressZeros(histo):
  nBinsX = histo.GetNbinsX()
  for i in range(nBinsX):
    content = histo.GetBinContent(i+1)
    error   = histo.GetBinError(i+1)
    if content < 0 or content == 0:
      #if content+error > 0:
      #  histo.SetBinContent(i+1,content+error)
      #  histo.SetBinError(i+1,error)
      #else:
      #  histo.SetBinContent(i+1,1e-10)
      #  histo.SetBinError(i+1,1e-10)
      mean    = truncated_normal_mean(content,error)
      if mean < 0:
        histo.SetBinContent(i+1,1e-10)
        histo.SetBinError(i+1,0)
      else:
        print("mean",mean,"mu",content,"std",error)
        histo.SetBinContent(i+1,mean)
        histo.SetBinError(i+1,content+error-mean)

def AppendForEnvelop(histos_envelop, ch, var, histoD):
  if ch not in histos_envelop:
    histos_envelop[ch] = {}
  if var not in histos_envelop[ch]:
    histos_envelop[ch][var] = []
  histos_envelop[ch][var].append(histoD)

def WriteEnvelop(histos_envelop, ch, var, rebin_syst):
  histo_list = histos_envelop[ch][var]
  nBinsX     = rebin_syst.size - 1
  BinsX_cent = (rebin_syst[:-1] + np.roll(rebin_syst,-1)[:-1])/2 #bin center
  print('rebin_syst',rebin_syst)
  print('BinsX_cent',BinsX_cent)
  bins_cont_up, bins_err_up     = [0.]*nBinsX, [0.]*nBinsX
  bins_cont_down, bins_err_down = [999999999999999999999999999999]*nBinsX, [999999999999999999999999999999]*nBinsX

  for i_histo, histo in enumerate(histo_list):
    # if sum is below zero, skip this histo
    sum_binc = sum([histo.GetBinContent(i+1) for i in range(nBinsX)])
    if i_histo>0 and sum_binc <= 1e-8:
      continue
    #
    for i, i_cent in enumerate(BinsX_cent):
      bin_content = histo.GetBinContent(histo.FindBin(i_cent))
      bin_error = histo.GetBinError(histo.FindBin(i_cent))
      if bins_cont_up[i] < bin_content:
        bins_cont_up[i] = bin_content
        bins_err_up[i]  = bin_error
      if bins_cont_down[i] > bin_content:
        bins_cont_down[i] = bin_content
        bins_err_down[i]  = bin_error
      
  histo_envelop_up   = ROOT.TH1D('histo_TF_data_driven_envelopUp','histo_TF_data_driven_envelopUp',    nBinsX, rebin_syst)
  histo_envelop_down = ROOT.TH1D('histo_TF_data_driven_envelopDown','histo_TF_data_driven_envelopDown',nBinsX, rebin_syst)

  for i in range(nBinsX):
    histo_envelop_up.SetBinContent(i+1,bins_cont_up[i])
    histo_envelop_up.SetBinError(i+1,bins_err_up[i])
    histo_envelop_down.SetBinContent(i+1,bins_cont_down[i])
    histo_envelop_down.SetBinError(i+1,bins_err_down[i])

  outFile.cd(ch+'/'+var)
  histo_envelop_up.Write('histo_TF_data_driven_envelopUp')
  histo_envelop_down.Write('histo_TF_data_driven_envelopDown')


outFile.cd()

histos_envelop = {}
for tag_key in input_dict:
  chennels = input_dict[tag_key]
  for ch in chennels:
    outFile.mkdir(ch)
    outFile.cd(ch)
    for var in chennels[ch]['B']:
      outFile.mkdir(ch+'/'+var)
      outFile.cd(ch+'/'+var)
      histoNameA = chennels[ch]['A'][var]
      histoNameB = chennels[ch]['B'][var]
      histoNameC = chennels[ch]['C'][var]
      # rebin
      if not tag_key == 'binningVar':
        rebin      = bins[ch]
      else:
        rebin      = bins_syst[ch]
      if tag_key == "" or tag_key == "isoVar":
        print(tag_key)
        print(histoNameB)
        print(histoNameC)

      print(tag_key)
      _, ratio  = GetHisto(histoNameA, rebin, tag_key, 1.)
      if ratio < 1.: # if DATA norm < MC norm. rescale MC in region B and C
        rescale = ratio
        print('###############################################################')
        print('            %s\t\t\t%s'%(ch,tag_key))
        print('            rescale MC to : %f'%rescale)
        print('###############################################################')
      else:
        rescale = 1.

      histoB, _ = GetHisto(histoNameB, rebin, tag_key, rescale)
      histoC, _ = GetHisto(histoNameC, rebin, tag_key, rescale)

      histoB.Divide(histoC)  # transfer factor : looser ID region to tighter ID region
      histoB.SetName(ch+'__'+var)
      outHistName = 'histo_TF_data_driven'
      if tag_key == '':
        pass
      else:
        outHistName += '_' + tag_key

      SuppressZeros(histoB)
      histoB.Write(outHistName)
      #
      if tag_key not in exclude_envelop:
        AppendForEnvelop(histos_envelop, ch, var, histoB)

for ch in input_dict['']:
  for var in input_dict[''][ch]['B']:
    rebin_syst = bins[ch]
    WriteEnvelop(histos_envelop, ch, var, rebin_syst)

outFile.Close()
