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


chennels = {
  'sng_4j_eleCH_2b' : {
        'B' : [
                'sng_4j_B_eleCH_2b/EleSCEta/histo_DATA',
                'sng_4j_B_eleCH_2b/EleSCEta/histo_DY',
                'sng_4j_B_eleCH_2b/EleSCEta/histo_ST',
                'sng_4j_B_eleCH_2b/EleSCEta/histo_TTLJ_jj',
                'sng_4j_B_eleCH_2b/EleSCEta/histo_TTLJ_cc',
                'sng_4j_B_eleCH_2b/EleSCEta/histo_TTLJ_bj',
                'sng_4j_B_eleCH_2b/EleSCEta/histo_TTLJ_bb',
                'sng_4j_B_eleCH_2b/EleSCEta/histo_TTLL_jj',
                'sng_4j_B_eleCH_2b/EleSCEta/histo_TTLL_cc',
                'sng_4j_B_eleCH_2b/EleSCEta/histo_TTLL_bj',
                'sng_4j_B_eleCH_2b/EleSCEta/histo_TTLL_bb',
                'sng_4j_B_eleCH_2b/EleSCEta/histo_TTWjets',
                'sng_4j_B_eleCH_2b/EleSCEta/histo_TTZjets',
                'sng_4j_B_eleCH_2b/EleSCEta/histo_Wjets',
                'sng_4j_B_eleCH_2b/EleSCEta/histo_WW',
                'sng_4j_B_eleCH_2b/EleSCEta/histo_WZ',
                'sng_4j_B_eleCH_2b/EleSCEta/histo_ZZ',
            ],
        'C' : [
                'sng_4j_C_eleCH_2b/EleSCEta/histo_DATA',
                'sng_4j_C_eleCH_2b/EleSCEta/histo_DY',
                'sng_4j_C_eleCH_2b/EleSCEta/histo_ST',
                'sng_4j_C_eleCH_2b/EleSCEta/histo_TTLJ_jj',
                'sng_4j_C_eleCH_2b/EleSCEta/histo_TTLJ_cc',
                'sng_4j_C_eleCH_2b/EleSCEta/histo_TTLJ_bj',
                'sng_4j_C_eleCH_2b/EleSCEta/histo_TTLJ_bb',
                'sng_4j_C_eleCH_2b/EleSCEta/histo_TTLL_jj',
                'sng_4j_C_eleCH_2b/EleSCEta/histo_TTLL_cc',
                'sng_4j_C_eleCH_2b/EleSCEta/histo_TTLL_bj',
                'sng_4j_C_eleCH_2b/EleSCEta/histo_TTLL_bb',
                'sng_4j_C_eleCH_2b/EleSCEta/histo_TTWjets',
                'sng_4j_C_eleCH_2b/EleSCEta/histo_TTZjets',
                'sng_4j_C_eleCH_2b/EleSCEta/histo_Wjets',
                'sng_4j_C_eleCH_2b/EleSCEta/histo_WW',
                'sng_4j_C_eleCH_2b/EleSCEta/histo_WZ',
                'sng_4j_C_eleCH_2b/EleSCEta/histo_ZZ',

            ],
      },
  'sng_4j_eleCH_3b' : {
        'B' : [
                'sng_4j_B_eleCH_3b/EleSCEta/histo_DATA',
                'sng_4j_B_eleCH_3b/EleSCEta/histo_DY',
                'sng_4j_B_eleCH_3b/EleSCEta/histo_ST',
                'sng_4j_B_eleCH_3b/EleSCEta/histo_TTLJ_jj',
                'sng_4j_B_eleCH_3b/EleSCEta/histo_TTLJ_cc',
                'sng_4j_B_eleCH_3b/EleSCEta/histo_TTLJ_bj',
                'sng_4j_B_eleCH_3b/EleSCEta/histo_TTLJ_bb',
                'sng_4j_B_eleCH_3b/EleSCEta/histo_TTLL_jj',
                'sng_4j_B_eleCH_3b/EleSCEta/histo_TTLL_cc',
                'sng_4j_B_eleCH_3b/EleSCEta/histo_TTLL_bj',
                'sng_4j_B_eleCH_3b/EleSCEta/histo_TTLL_bb',
                'sng_4j_B_eleCH_3b/EleSCEta/histo_TTWjets',
                'sng_4j_B_eleCH_3b/EleSCEta/histo_TTZjets',
                'sng_4j_B_eleCH_3b/EleSCEta/histo_Wjets',
                'sng_4j_B_eleCH_3b/EleSCEta/histo_WW',
                'sng_4j_B_eleCH_3b/EleSCEta/histo_WZ',
                'sng_4j_B_eleCH_3b/EleSCEta/histo_ZZ',
            ],
        'C' : [
                'sng_4j_C_eleCH_3b/EleSCEta/histo_DATA',
                'sng_4j_C_eleCH_3b/EleSCEta/histo_DY',
                'sng_4j_C_eleCH_3b/EleSCEta/histo_ST',
                'sng_4j_C_eleCH_3b/EleSCEta/histo_TTLJ_jj',
                'sng_4j_C_eleCH_3b/EleSCEta/histo_TTLJ_cc',
                'sng_4j_C_eleCH_3b/EleSCEta/histo_TTLJ_bj',
                'sng_4j_C_eleCH_3b/EleSCEta/histo_TTLJ_bb',
                'sng_4j_C_eleCH_3b/EleSCEta/histo_TTLL_jj',
                'sng_4j_C_eleCH_3b/EleSCEta/histo_TTLL_cc',
                'sng_4j_C_eleCH_3b/EleSCEta/histo_TTLL_bj',
                'sng_4j_C_eleCH_3b/EleSCEta/histo_TTLL_bb',
                'sng_4j_C_eleCH_3b/EleSCEta/histo_TTWjets',
                'sng_4j_C_eleCH_3b/EleSCEta/histo_TTZjets',
                'sng_4j_C_eleCH_3b/EleSCEta/histo_Wjets',
                'sng_4j_C_eleCH_3b/EleSCEta/histo_WW',
                'sng_4j_C_eleCH_3b/EleSCEta/histo_WZ',
                'sng_4j_C_eleCH_3b/EleSCEta/histo_ZZ',

            ],
      },
  'sng_4j_muCH_2b'  : {
        'B' : [
                'sng_4j_B_muCH_2b/MuonEta/histo_DATA',
                'sng_4j_B_muCH_2b/MuonEta/histo_DY',
                'sng_4j_B_muCH_2b/MuonEta/histo_ST',
                'sng_4j_B_muCH_2b/MuonEta/histo_TTLJ_jj',
                'sng_4j_B_muCH_2b/MuonEta/histo_TTLJ_cc',
                'sng_4j_B_muCH_2b/MuonEta/histo_TTLJ_bj',
                'sng_4j_B_muCH_2b/MuonEta/histo_TTLJ_bb',
                'sng_4j_B_muCH_2b/MuonEta/histo_TTLL_jj',
                'sng_4j_B_muCH_2b/MuonEta/histo_TTLL_cc',
                'sng_4j_B_muCH_2b/MuonEta/histo_TTLL_bj',
                'sng_4j_B_muCH_2b/MuonEta/histo_TTLL_bb',
                'sng_4j_B_muCH_2b/MuonEta/histo_TTWjets',
                'sng_4j_B_muCH_2b/MuonEta/histo_TTZjets',
                'sng_4j_B_muCH_2b/MuonEta/histo_Wjets',
                'sng_4j_B_muCH_2b/MuonEta/histo_WW',
                'sng_4j_B_muCH_2b/MuonEta/histo_WZ',
                'sng_4j_B_muCH_2b/MuonEta/histo_ZZ',
            ],
        'C' : [
                'sng_4j_C_muCH_2b/MuonEta/histo_DATA',
                'sng_4j_C_muCH_2b/MuonEta/histo_DY',
                'sng_4j_C_muCH_2b/MuonEta/histo_ST',
                'sng_4j_C_muCH_2b/MuonEta/histo_TTLJ_jj',
                'sng_4j_C_muCH_2b/MuonEta/histo_TTLJ_cc',
                'sng_4j_C_muCH_2b/MuonEta/histo_TTLJ_bj',
                'sng_4j_C_muCH_2b/MuonEta/histo_TTLJ_bb',
                'sng_4j_C_muCH_2b/MuonEta/histo_TTLL_jj',
                'sng_4j_C_muCH_2b/MuonEta/histo_TTLL_cc',
                'sng_4j_C_muCH_2b/MuonEta/histo_TTLL_bj',
                'sng_4j_C_muCH_2b/MuonEta/histo_TTLL_bb',
                'sng_4j_C_muCH_2b/MuonEta/histo_TTWjets',
                'sng_4j_C_muCH_2b/MuonEta/histo_TTZjets',
                'sng_4j_C_muCH_2b/MuonEta/histo_Wjets',
                'sng_4j_C_muCH_2b/MuonEta/histo_WW',
                'sng_4j_C_muCH_2b/MuonEta/histo_WZ',
                'sng_4j_C_muCH_2b/MuonEta/histo_ZZ',
            ],
      },
  'sng_4j_muCH_3b'  : {
        'B' : [
                'sng_4j_B_muCH_3b/MuonEta/histo_DATA',
                'sng_4j_B_muCH_3b/MuonEta/histo_DY',
                'sng_4j_B_muCH_3b/MuonEta/histo_ST',
                'sng_4j_B_muCH_3b/MuonEta/histo_TTLJ_jj',
                'sng_4j_B_muCH_3b/MuonEta/histo_TTLJ_cc',
                'sng_4j_B_muCH_3b/MuonEta/histo_TTLJ_bj',
                'sng_4j_B_muCH_3b/MuonEta/histo_TTLJ_bb',
                'sng_4j_B_muCH_3b/MuonEta/histo_TTLL_jj',
                'sng_4j_B_muCH_3b/MuonEta/histo_TTLL_cc',
                'sng_4j_B_muCH_3b/MuonEta/histo_TTLL_bj',
                'sng_4j_B_muCH_3b/MuonEta/histo_TTLL_bb',
                'sng_4j_B_muCH_3b/MuonEta/histo_TTWjets',
                'sng_4j_B_muCH_3b/MuonEta/histo_TTZjets',
                'sng_4j_B_muCH_3b/MuonEta/histo_Wjets',
                'sng_4j_B_muCH_3b/MuonEta/histo_WW',
                'sng_4j_B_muCH_3b/MuonEta/histo_WZ',
                'sng_4j_B_muCH_3b/MuonEta/histo_ZZ',
            ],
        'C' : [
                'sng_4j_C_muCH_3b/MuonEta/histo_DATA',
                'sng_4j_C_muCH_3b/MuonEta/histo_DY',
                'sng_4j_C_muCH_3b/MuonEta/histo_ST',
                'sng_4j_C_muCH_3b/MuonEta/histo_TTLJ_jj',
                'sng_4j_C_muCH_3b/MuonEta/histo_TTLJ_cc',
                'sng_4j_C_muCH_3b/MuonEta/histo_TTLJ_bj',
                'sng_4j_C_muCH_3b/MuonEta/histo_TTLJ_bb',
                'sng_4j_C_muCH_3b/MuonEta/histo_TTLL_jj',
                'sng_4j_C_muCH_3b/MuonEta/histo_TTLL_cc',
                'sng_4j_C_muCH_3b/MuonEta/histo_TTLL_bj',
                'sng_4j_C_muCH_3b/MuonEta/histo_TTLL_bb',
                'sng_4j_C_muCH_3b/MuonEta/histo_TTWjets',
                'sng_4j_C_muCH_3b/MuonEta/histo_TTZjets',
                'sng_4j_C_muCH_3b/MuonEta/histo_Wjets',
                'sng_4j_C_muCH_3b/MuonEta/histo_WW',
                'sng_4j_C_muCH_3b/MuonEta/histo_WZ',
                'sng_4j_C_muCH_3b/MuonEta/histo_ZZ',
            ],

      },

  'dbl_2j_ee_2b' : {
      'A' : [
              'dbl_2j_A_ee_2b/Event/histo_DATA',
              'dbl_2j_A_ee_2b/Event/histo_DY',
              'dbl_2j_A_ee_2b/Event/histo_ST',
              'dbl_2j_A_ee_2b/Event/histo_TTLJ_jj',
              'dbl_2j_A_ee_2b/Event/histo_TTLJ_cc',
              'dbl_2j_A_ee_2b/Event/histo_TTLJ_bj',
              'dbl_2j_A_ee_2b/Event/histo_TTLJ_bb',
              'dbl_2j_A_ee_2b/Event/histo_TTLL_jj',
              'dbl_2j_A_ee_2b/Event/histo_TTLL_cc',
              'dbl_2j_A_ee_2b/Event/histo_TTLL_bj',
              'dbl_2j_A_ee_2b/Event/histo_TTLL_bb',
              'dbl_2j_A_ee_2b/Event/histo_TTWjets',
              'dbl_2j_A_ee_2b/Event/histo_TTZjets',
              'dbl_2j_A_ee_2b/Event/histo_Wjets',
              'dbl_2j_A_ee_2b/Event/histo_WW',
              'dbl_2j_A_ee_2b/Event/histo_WZ',
              'dbl_2j_A_ee_2b/Event/histo_ZZ',
          ],
      'B' : [
              'dbl_2j_B_ee_2b/Event/histo_DATA',
              'dbl_2j_B_ee_2b/Event/histo_DY',
              'dbl_2j_B_ee_2b/Event/histo_ST',
              'dbl_2j_B_ee_2b/Event/histo_TTLJ_jj',
              'dbl_2j_B_ee_2b/Event/histo_TTLJ_cc',
              'dbl_2j_B_ee_2b/Event/histo_TTLJ_bj',
              'dbl_2j_B_ee_2b/Event/histo_TTLJ_bb',
              'dbl_2j_B_ee_2b/Event/histo_TTLL_jj',
              'dbl_2j_B_ee_2b/Event/histo_TTLL_cc',
              'dbl_2j_B_ee_2b/Event/histo_TTLL_bj',
              'dbl_2j_B_ee_2b/Event/histo_TTLL_bb',
              'dbl_2j_B_ee_2b/Event/histo_TTWjets',
              'dbl_2j_B_ee_2b/Event/histo_TTZjets',
              'dbl_2j_B_ee_2b/Event/histo_Wjets',
              'dbl_2j_B_ee_2b/Event/histo_WW',
              'dbl_2j_B_ee_2b/Event/histo_WZ',
              'dbl_2j_B_ee_2b/Event/histo_ZZ',
          ],
      'C' : [
              'dbl_2j_C_ee_2b/Event/histo_DATA',
              'dbl_2j_C_ee_2b/Event/histo_DY',
              'dbl_2j_C_ee_2b/Event/histo_ST',
              'dbl_2j_C_ee_2b/Event/histo_TTLJ_jj',
              'dbl_2j_C_ee_2b/Event/histo_TTLJ_cc',
              'dbl_2j_C_ee_2b/Event/histo_TTLJ_bj',
              'dbl_2j_C_ee_2b/Event/histo_TTLJ_bb',
              'dbl_2j_C_ee_2b/Event/histo_TTLL_jj',
              'dbl_2j_C_ee_2b/Event/histo_TTLL_cc',
              'dbl_2j_C_ee_2b/Event/histo_TTLL_bj',
              'dbl_2j_C_ee_2b/Event/histo_TTLL_bb',
              'dbl_2j_C_ee_2b/Event/histo_TTWjets',
              'dbl_2j_C_ee_2b/Event/histo_TTZjets',
              'dbl_2j_C_ee_2b/Event/histo_Wjets',
              'dbl_2j_C_ee_2b/Event/histo_WW',
              'dbl_2j_C_ee_2b/Event/histo_WZ',
              'dbl_2j_C_ee_2b/Event/histo_ZZ',
          ],
      'D' : [
              'dbl_2j_D_ee_2b/Event/histo_DATA',
              'dbl_2j_D_ee_2b/Event/histo_DY',
              'dbl_2j_D_ee_2b/Event/histo_ST',
              'dbl_2j_D_ee_2b/Event/histo_TTLJ_jj',
              'dbl_2j_D_ee_2b/Event/histo_TTLJ_cc',
              'dbl_2j_D_ee_2b/Event/histo_TTLJ_bj',
              'dbl_2j_D_ee_2b/Event/histo_TTLJ_bb',
              'dbl_2j_D_ee_2b/Event/histo_TTLL_jj',
              'dbl_2j_D_ee_2b/Event/histo_TTLL_cc',
              'dbl_2j_D_ee_2b/Event/histo_TTLL_bj',
              'dbl_2j_D_ee_2b/Event/histo_TTLL_bb',
              'dbl_2j_D_ee_2b/Event/histo_TTWjets',
              'dbl_2j_D_ee_2b/Event/histo_TTZjets',
              'dbl_2j_D_ee_2b/Event/histo_Wjets',
              'dbl_2j_D_ee_2b/Event/histo_WW',
              'dbl_2j_D_ee_2b/Event/histo_WZ',
              'dbl_2j_D_ee_2b/Event/histo_ZZ',
          ],
  },
  'dbl_2j_ee_3b' : {
      'A' : [
              'dbl_2j_A_ee_3b/Event/histo_DATA',
              'dbl_2j_A_ee_3b/Event/histo_DY',
              'dbl_2j_A_ee_3b/Event/histo_ST',
              'dbl_2j_A_ee_3b/Event/histo_TTLJ_jj',
              'dbl_2j_A_ee_3b/Event/histo_TTLJ_cc',
              'dbl_2j_A_ee_3b/Event/histo_TTLJ_bj',
              'dbl_2j_A_ee_3b/Event/histo_TTLJ_bb',
              'dbl_2j_A_ee_3b/Event/histo_TTLL_jj',
              'dbl_2j_A_ee_3b/Event/histo_TTLL_cc',
              'dbl_2j_A_ee_3b/Event/histo_TTLL_bj',
              'dbl_2j_A_ee_3b/Event/histo_TTLL_bb',
              'dbl_2j_A_ee_3b/Event/histo_TTWjets',
              'dbl_2j_A_ee_3b/Event/histo_TTZjets',
              'dbl_2j_A_ee_3b/Event/histo_Wjets',
              'dbl_2j_A_ee_3b/Event/histo_WW',
              'dbl_2j_A_ee_3b/Event/histo_WZ',
              'dbl_2j_A_ee_3b/Event/histo_ZZ',
          ],
      'B' : [
              'dbl_2j_B_ee_3b/Event/histo_DATA',
              'dbl_2j_B_ee_3b/Event/histo_DY',
              'dbl_2j_B_ee_3b/Event/histo_ST',
              'dbl_2j_B_ee_3b/Event/histo_TTLJ_jj',
              'dbl_2j_B_ee_3b/Event/histo_TTLJ_cc',
              'dbl_2j_B_ee_3b/Event/histo_TTLJ_bj',
              'dbl_2j_B_ee_3b/Event/histo_TTLJ_bb',
              'dbl_2j_B_ee_3b/Event/histo_TTLL_jj',
              'dbl_2j_B_ee_3b/Event/histo_TTLL_cc',
              'dbl_2j_B_ee_3b/Event/histo_TTLL_bj',
              'dbl_2j_B_ee_3b/Event/histo_TTLL_bb',
              'dbl_2j_B_ee_3b/Event/histo_TTWjets',
              'dbl_2j_B_ee_3b/Event/histo_TTZjets',
              'dbl_2j_B_ee_3b/Event/histo_Wjets',
              'dbl_2j_B_ee_3b/Event/histo_WW',
              'dbl_2j_B_ee_3b/Event/histo_WZ',
              'dbl_2j_B_ee_3b/Event/histo_ZZ',
          ],
      'C' : [
              'dbl_2j_C_ee_3b/Event/histo_DATA',
              'dbl_2j_C_ee_3b/Event/histo_DY',
              'dbl_2j_C_ee_3b/Event/histo_ST',
              'dbl_2j_C_ee_3b/Event/histo_TTLJ_jj',
              'dbl_2j_C_ee_3b/Event/histo_TTLJ_cc',
              'dbl_2j_C_ee_3b/Event/histo_TTLJ_bj',
              'dbl_2j_C_ee_3b/Event/histo_TTLJ_bb',
              'dbl_2j_C_ee_3b/Event/histo_TTLL_jj',
              'dbl_2j_C_ee_3b/Event/histo_TTLL_cc',
              'dbl_2j_C_ee_3b/Event/histo_TTLL_bj',
              'dbl_2j_C_ee_3b/Event/histo_TTLL_bb',
              'dbl_2j_C_ee_3b/Event/histo_TTWjets',
              'dbl_2j_C_ee_3b/Event/histo_TTZjets',
              'dbl_2j_C_ee_3b/Event/histo_Wjets',
              'dbl_2j_C_ee_3b/Event/histo_WW',
              'dbl_2j_C_ee_3b/Event/histo_WZ',
              'dbl_2j_C_ee_3b/Event/histo_ZZ',
          ],
      'D' : [
              'dbl_2j_D_ee_3b/Event/histo_DATA',
              'dbl_2j_D_ee_3b/Event/histo_DY',
              'dbl_2j_D_ee_3b/Event/histo_ST',
              'dbl_2j_D_ee_3b/Event/histo_TTLJ_jj',
              'dbl_2j_D_ee_3b/Event/histo_TTLJ_cc',
              'dbl_2j_D_ee_3b/Event/histo_TTLJ_bj',
              'dbl_2j_D_ee_3b/Event/histo_TTLJ_bb',
              'dbl_2j_D_ee_3b/Event/histo_TTLL_jj',
              'dbl_2j_D_ee_3b/Event/histo_TTLL_cc',
              'dbl_2j_D_ee_3b/Event/histo_TTLL_bj',
              'dbl_2j_D_ee_3b/Event/histo_TTLL_bb',
              'dbl_2j_D_ee_3b/Event/histo_TTWjets',
              'dbl_2j_D_ee_3b/Event/histo_TTZjets',
              'dbl_2j_D_ee_3b/Event/histo_Wjets',
              'dbl_2j_D_ee_3b/Event/histo_WW',
              'dbl_2j_D_ee_3b/Event/histo_WZ',
              'dbl_2j_D_ee_3b/Event/histo_ZZ',
          ],
  },
  'dbl_2j_mm_2b' : {
      'A' : [
              'dbl_2j_A_mm_2b/Event/histo_DATA',
              'dbl_2j_A_mm_2b/Event/histo_DY',
              'dbl_2j_A_mm_2b/Event/histo_ST',
              'dbl_2j_A_mm_2b/Event/histo_TTLJ_jj',
              'dbl_2j_A_mm_2b/Event/histo_TTLJ_cc',
              'dbl_2j_A_mm_2b/Event/histo_TTLJ_bj',
              'dbl_2j_A_mm_2b/Event/histo_TTLJ_bb',
              'dbl_2j_A_mm_2b/Event/histo_TTLL_jj',
              'dbl_2j_A_mm_2b/Event/histo_TTLL_cc',
              'dbl_2j_A_mm_2b/Event/histo_TTLL_bj',
              'dbl_2j_A_mm_2b/Event/histo_TTLL_bb',
              'dbl_2j_A_mm_2b/Event/histo_TTWjets',
              'dbl_2j_A_mm_2b/Event/histo_TTZjets',
              'dbl_2j_A_mm_2b/Event/histo_Wjets',
              'dbl_2j_A_mm_2b/Event/histo_WW',
              'dbl_2j_A_mm_2b/Event/histo_WZ',
              'dbl_2j_A_mm_2b/Event/histo_ZZ',
          ],
      'B' : [
              'dbl_2j_B_mm_2b/Event/histo_DATA',
              'dbl_2j_B_mm_2b/Event/histo_DY',
              'dbl_2j_B_mm_2b/Event/histo_ST',
              'dbl_2j_B_mm_2b/Event/histo_TTLJ_jj',
              'dbl_2j_B_mm_2b/Event/histo_TTLJ_cc',
              'dbl_2j_B_mm_2b/Event/histo_TTLJ_bj',
              'dbl_2j_B_mm_2b/Event/histo_TTLJ_bb',
              'dbl_2j_B_mm_2b/Event/histo_TTLL_jj',
              'dbl_2j_B_mm_2b/Event/histo_TTLL_cc',
              'dbl_2j_B_mm_2b/Event/histo_TTLL_bj',
              'dbl_2j_B_mm_2b/Event/histo_TTLL_bb',
              'dbl_2j_B_mm_2b/Event/histo_TTWjets',
              'dbl_2j_B_mm_2b/Event/histo_TTZjets',
              'dbl_2j_B_mm_2b/Event/histo_Wjets',
              'dbl_2j_B_mm_2b/Event/histo_WW',
              'dbl_2j_B_mm_2b/Event/histo_WZ',
              'dbl_2j_B_mm_2b/Event/histo_ZZ',
          ],
      'C' : [
              'dbl_2j_C_mm_2b/Event/histo_DATA',
              'dbl_2j_C_mm_2b/Event/histo_DY',
              'dbl_2j_C_mm_2b/Event/histo_ST',
              'dbl_2j_C_mm_2b/Event/histo_TTLJ_jj',
              'dbl_2j_C_mm_2b/Event/histo_TTLJ_cc',
              'dbl_2j_C_mm_2b/Event/histo_TTLJ_bj',
              'dbl_2j_C_mm_2b/Event/histo_TTLJ_bb',
              'dbl_2j_C_mm_2b/Event/histo_TTLL_jj',
              'dbl_2j_C_mm_2b/Event/histo_TTLL_cc',
              'dbl_2j_C_mm_2b/Event/histo_TTLL_bj',
              'dbl_2j_C_mm_2b/Event/histo_TTLL_bb',
              'dbl_2j_C_mm_2b/Event/histo_TTWjets',
              'dbl_2j_C_mm_2b/Event/histo_TTZjets',
              'dbl_2j_C_mm_2b/Event/histo_Wjets',
              'dbl_2j_C_mm_2b/Event/histo_WW',
              'dbl_2j_C_mm_2b/Event/histo_WZ',
              'dbl_2j_C_mm_2b/Event/histo_ZZ',
          ],
      'D' : [
              'dbl_2j_D_mm_2b/Event/histo_DATA',
              'dbl_2j_D_mm_2b/Event/histo_DY',
              'dbl_2j_D_mm_2b/Event/histo_ST',
              'dbl_2j_D_mm_2b/Event/histo_TTLJ_jj',
              'dbl_2j_D_mm_2b/Event/histo_TTLJ_cc',
              'dbl_2j_D_mm_2b/Event/histo_TTLJ_bj',
              'dbl_2j_D_mm_2b/Event/histo_TTLJ_bb',
              'dbl_2j_D_mm_2b/Event/histo_TTLL_jj',
              'dbl_2j_D_mm_2b/Event/histo_TTLL_cc',
              'dbl_2j_D_mm_2b/Event/histo_TTLL_bj',
              'dbl_2j_D_mm_2b/Event/histo_TTLL_bb',
              'dbl_2j_D_mm_2b/Event/histo_TTWjets',
              'dbl_2j_D_mm_2b/Event/histo_TTZjets',
              'dbl_2j_D_mm_2b/Event/histo_Wjets',
              'dbl_2j_D_mm_2b/Event/histo_WW',
              'dbl_2j_D_mm_2b/Event/histo_WZ',
              'dbl_2j_D_mm_2b/Event/histo_ZZ',
          ],
  },
  'dbl_2j_mm_3b' : {
      'A' : [
              'dbl_2j_A_mm_3b/Event/histo_DATA',
              'dbl_2j_A_mm_3b/Event/histo_DY',
              'dbl_2j_A_mm_3b/Event/histo_ST',
              'dbl_2j_A_mm_3b/Event/histo_TTLJ_jj',
              'dbl_2j_A_mm_3b/Event/histo_TTLJ_cc',
              'dbl_2j_A_mm_3b/Event/histo_TTLJ_bj',
              'dbl_2j_A_mm_3b/Event/histo_TTLJ_bb',
              'dbl_2j_A_mm_3b/Event/histo_TTLL_jj',
              'dbl_2j_A_mm_3b/Event/histo_TTLL_cc',
              'dbl_2j_A_mm_3b/Event/histo_TTLL_bj',
              'dbl_2j_A_mm_3b/Event/histo_TTLL_bb',
              'dbl_2j_A_mm_3b/Event/histo_TTWjets',
              'dbl_2j_A_mm_3b/Event/histo_TTZjets',
              'dbl_2j_A_mm_3b/Event/histo_Wjets',
              'dbl_2j_A_mm_3b/Event/histo_WW',
              'dbl_2j_A_mm_3b/Event/histo_WZ',
              'dbl_2j_A_mm_3b/Event/histo_ZZ',
          ],
      'B' : [
              'dbl_2j_B_mm_3b/Event/histo_DATA',
              'dbl_2j_B_mm_3b/Event/histo_DY',
              'dbl_2j_B_mm_3b/Event/histo_ST',
              'dbl_2j_B_mm_3b/Event/histo_TTLJ_jj',
              'dbl_2j_B_mm_3b/Event/histo_TTLJ_cc',
              'dbl_2j_B_mm_3b/Event/histo_TTLJ_bj',
              'dbl_2j_B_mm_3b/Event/histo_TTLJ_bb',
              'dbl_2j_B_mm_3b/Event/histo_TTLL_jj',
              'dbl_2j_B_mm_3b/Event/histo_TTLL_cc',
              'dbl_2j_B_mm_3b/Event/histo_TTLL_bj',
              'dbl_2j_B_mm_3b/Event/histo_TTLL_bb',
              'dbl_2j_B_mm_3b/Event/histo_TTWjets',
              'dbl_2j_B_mm_3b/Event/histo_TTZjets',
              'dbl_2j_B_mm_3b/Event/histo_Wjets',
              'dbl_2j_B_mm_3b/Event/histo_WW',
              'dbl_2j_B_mm_3b/Event/histo_WZ',
              'dbl_2j_B_mm_3b/Event/histo_ZZ',
          ],
      'C' : [
              'dbl_2j_C_mm_3b/Event/histo_DATA',
              'dbl_2j_C_mm_3b/Event/histo_DY',
              'dbl_2j_C_mm_3b/Event/histo_ST',
              'dbl_2j_C_mm_3b/Event/histo_TTLJ_jj',
              'dbl_2j_C_mm_3b/Event/histo_TTLJ_cc',
              'dbl_2j_C_mm_3b/Event/histo_TTLJ_bj',
              'dbl_2j_C_mm_3b/Event/histo_TTLJ_bb',
              'dbl_2j_C_mm_3b/Event/histo_TTLL_jj',
              'dbl_2j_C_mm_3b/Event/histo_TTLL_cc',
              'dbl_2j_C_mm_3b/Event/histo_TTLL_bj',
              'dbl_2j_C_mm_3b/Event/histo_TTLL_bb',
              'dbl_2j_C_mm_3b/Event/histo_TTWjets',
              'dbl_2j_C_mm_3b/Event/histo_TTZjets',
              'dbl_2j_C_mm_3b/Event/histo_Wjets',
              'dbl_2j_C_mm_3b/Event/histo_WW',
              'dbl_2j_C_mm_3b/Event/histo_WZ',
              'dbl_2j_C_mm_3b/Event/histo_ZZ',
          ],
      'D' : [
              'dbl_2j_D_mm_3b/Event/histo_DATA',
              'dbl_2j_D_mm_3b/Event/histo_DY',
              'dbl_2j_D_mm_3b/Event/histo_ST',
              'dbl_2j_D_mm_3b/Event/histo_TTLJ_jj',
              'dbl_2j_D_mm_3b/Event/histo_TTLJ_cc',
              'dbl_2j_D_mm_3b/Event/histo_TTLJ_bj',
              'dbl_2j_D_mm_3b/Event/histo_TTLJ_bb',
              'dbl_2j_D_mm_3b/Event/histo_TTLL_jj',
              'dbl_2j_D_mm_3b/Event/histo_TTLL_cc',
              'dbl_2j_D_mm_3b/Event/histo_TTLL_bj',
              'dbl_2j_D_mm_3b/Event/histo_TTLL_bb',
              'dbl_2j_D_mm_3b/Event/histo_TTWjets',
              'dbl_2j_D_mm_3b/Event/histo_TTZjets',
              'dbl_2j_D_mm_3b/Event/histo_Wjets',
              'dbl_2j_D_mm_3b/Event/histo_WW',
              'dbl_2j_D_mm_3b/Event/histo_WZ',
              'dbl_2j_D_mm_3b/Event/histo_ZZ',
          ],
  },
  'dbl_2j_me_2b' : {
      'A' : [
              'dbl_2j_A_me_2b/Event/histo_DATA',
              'dbl_2j_A_me_2b/Event/histo_DY',
              'dbl_2j_A_me_2b/Event/histo_ST',
              'dbl_2j_A_me_2b/Event/histo_TTLJ_jj',
              'dbl_2j_A_me_2b/Event/histo_TTLJ_cc',
              'dbl_2j_A_me_2b/Event/histo_TTLJ_bj',
              'dbl_2j_A_me_2b/Event/histo_TTLJ_bb',
              'dbl_2j_A_me_2b/Event/histo_TTLL_jj',
              'dbl_2j_A_me_2b/Event/histo_TTLL_cc',
              'dbl_2j_A_me_2b/Event/histo_TTLL_bj',
              'dbl_2j_A_me_2b/Event/histo_TTLL_bb',
              'dbl_2j_A_me_2b/Event/histo_TTWjets',
              'dbl_2j_A_me_2b/Event/histo_TTZjets',
              'dbl_2j_A_me_2b/Event/histo_Wjets',
              'dbl_2j_A_me_2b/Event/histo_WW',
              'dbl_2j_A_me_2b/Event/histo_WZ',
              'dbl_2j_A_me_2b/Event/histo_ZZ',
          ],
      'B' : [
              'dbl_2j_B_me_2b/Event/histo_DATA',
              'dbl_2j_B_me_2b/Event/histo_DY',
              'dbl_2j_B_me_2b/Event/histo_ST',
              'dbl_2j_B_me_2b/Event/histo_TTLJ_jj',
              'dbl_2j_B_me_2b/Event/histo_TTLJ_cc',
              'dbl_2j_B_me_2b/Event/histo_TTLJ_bj',
              'dbl_2j_B_me_2b/Event/histo_TTLJ_bb',
              'dbl_2j_B_me_2b/Event/histo_TTLL_jj',
              'dbl_2j_B_me_2b/Event/histo_TTLL_cc',
              'dbl_2j_B_me_2b/Event/histo_TTLL_bj',
              'dbl_2j_B_me_2b/Event/histo_TTLL_bb',
              'dbl_2j_B_me_2b/Event/histo_TTWjets',
              'dbl_2j_B_me_2b/Event/histo_TTZjets',
              'dbl_2j_B_me_2b/Event/histo_Wjets',
              'dbl_2j_B_me_2b/Event/histo_WW',
              'dbl_2j_B_me_2b/Event/histo_WZ',
              'dbl_2j_B_me_2b/Event/histo_ZZ',
          ],
      'C' : [
              'dbl_2j_C_me_2b/Event/histo_DATA',
              'dbl_2j_C_me_2b/Event/histo_DY',
              'dbl_2j_C_me_2b/Event/histo_ST',
              'dbl_2j_C_me_2b/Event/histo_TTLJ_jj',
              'dbl_2j_C_me_2b/Event/histo_TTLJ_cc',
              'dbl_2j_C_me_2b/Event/histo_TTLJ_bj',
              'dbl_2j_C_me_2b/Event/histo_TTLJ_bb',
              'dbl_2j_C_me_2b/Event/histo_TTLL_jj',
              'dbl_2j_C_me_2b/Event/histo_TTLL_cc',
              'dbl_2j_C_me_2b/Event/histo_TTLL_bj',
              'dbl_2j_C_me_2b/Event/histo_TTLL_bb',
              'dbl_2j_C_me_2b/Event/histo_TTWjets',
              'dbl_2j_C_me_2b/Event/histo_TTZjets',
              'dbl_2j_C_me_2b/Event/histo_Wjets',
              'dbl_2j_C_me_2b/Event/histo_WW',
              'dbl_2j_C_me_2b/Event/histo_WZ',
              'dbl_2j_C_me_2b/Event/histo_ZZ',
          ],
      'D' : [
              'dbl_2j_D_me_2b/Event/histo_DATA',
              'dbl_2j_D_me_2b/Event/histo_DY',
              'dbl_2j_D_me_2b/Event/histo_ST',
              'dbl_2j_D_me_2b/Event/histo_TTLJ_jj',
              'dbl_2j_D_me_2b/Event/histo_TTLJ_cc',
              'dbl_2j_D_me_2b/Event/histo_TTLJ_bj',
              'dbl_2j_D_me_2b/Event/histo_TTLJ_bb',
              'dbl_2j_D_me_2b/Event/histo_TTLL_jj',
              'dbl_2j_D_me_2b/Event/histo_TTLL_cc',
              'dbl_2j_D_me_2b/Event/histo_TTLL_bj',
              'dbl_2j_D_me_2b/Event/histo_TTLL_bb',
              'dbl_2j_D_me_2b/Event/histo_TTWjets',
              'dbl_2j_D_me_2b/Event/histo_TTZjets',
              'dbl_2j_D_me_2b/Event/histo_Wjets',
              'dbl_2j_D_me_2b/Event/histo_WW',
              'dbl_2j_D_me_2b/Event/histo_WZ',
              'dbl_2j_D_me_2b/Event/histo_ZZ',
          ],
  },
  'dbl_2j_me_3b' : {
      'A' : [
              'dbl_2j_A_me_3b/Event/histo_DATA',
              'dbl_2j_A_me_3b/Event/histo_DY',
              'dbl_2j_A_me_3b/Event/histo_ST',
              'dbl_2j_A_me_3b/Event/histo_TTLJ_jj',
              'dbl_2j_A_me_3b/Event/histo_TTLJ_cc',
              'dbl_2j_A_me_3b/Event/histo_TTLJ_bj',
              'dbl_2j_A_me_3b/Event/histo_TTLJ_bb',
              'dbl_2j_A_me_3b/Event/histo_TTLL_jj',
              'dbl_2j_A_me_3b/Event/histo_TTLL_cc',
              'dbl_2j_A_me_3b/Event/histo_TTLL_bj',
              'dbl_2j_A_me_3b/Event/histo_TTLL_bb',
              'dbl_2j_A_me_3b/Event/histo_TTWjets',
              'dbl_2j_A_me_3b/Event/histo_TTZjets',
              'dbl_2j_A_me_3b/Event/histo_Wjets',
              'dbl_2j_A_me_3b/Event/histo_WW',
              'dbl_2j_A_me_3b/Event/histo_WZ',
              'dbl_2j_A_me_3b/Event/histo_ZZ',
          ],
      'B' : [
              'dbl_2j_B_me_3b/Event/histo_DATA',
              'dbl_2j_B_me_3b/Event/histo_DY',
              'dbl_2j_B_me_3b/Event/histo_ST',
              'dbl_2j_B_me_3b/Event/histo_TTLJ_jj',
              'dbl_2j_B_me_3b/Event/histo_TTLJ_cc',
              'dbl_2j_B_me_3b/Event/histo_TTLJ_bj',
              'dbl_2j_B_me_3b/Event/histo_TTLJ_bb',
              'dbl_2j_B_me_3b/Event/histo_TTLL_jj',
              'dbl_2j_B_me_3b/Event/histo_TTLL_cc',
              'dbl_2j_B_me_3b/Event/histo_TTLL_bj',
              'dbl_2j_B_me_3b/Event/histo_TTLL_bb',
              'dbl_2j_B_me_3b/Event/histo_TTWjets',
              'dbl_2j_B_me_3b/Event/histo_TTZjets',
              'dbl_2j_B_me_3b/Event/histo_Wjets',
              'dbl_2j_B_me_3b/Event/histo_WW',
              'dbl_2j_B_me_3b/Event/histo_WZ',
              'dbl_2j_B_me_3b/Event/histo_ZZ',
          ],
      'C' : [
              'dbl_2j_C_me_3b/Event/histo_DATA',
              'dbl_2j_C_me_3b/Event/histo_DY',
              'dbl_2j_C_me_3b/Event/histo_ST',
              'dbl_2j_C_me_3b/Event/histo_TTLJ_jj',
              'dbl_2j_C_me_3b/Event/histo_TTLJ_cc',
              'dbl_2j_C_me_3b/Event/histo_TTLJ_bj',
              'dbl_2j_C_me_3b/Event/histo_TTLJ_bb',
              'dbl_2j_C_me_3b/Event/histo_TTLL_jj',
              'dbl_2j_C_me_3b/Event/histo_TTLL_cc',
              'dbl_2j_C_me_3b/Event/histo_TTLL_bj',
              'dbl_2j_C_me_3b/Event/histo_TTLL_bb',
              'dbl_2j_C_me_3b/Event/histo_TTWjets',
              'dbl_2j_C_me_3b/Event/histo_TTZjets',
              'dbl_2j_C_me_3b/Event/histo_Wjets',
              'dbl_2j_C_me_3b/Event/histo_WW',
              'dbl_2j_C_me_3b/Event/histo_WZ',
              'dbl_2j_C_me_3b/Event/histo_ZZ',
          ],
      'D' : [
              'dbl_2j_D_me_3b/Event/histo_DATA',
              'dbl_2j_D_me_3b/Event/histo_DY',
              'dbl_2j_D_me_3b/Event/histo_ST',
              'dbl_2j_D_me_3b/Event/histo_TTLJ_jj',
              'dbl_2j_D_me_3b/Event/histo_TTLJ_cc',
              'dbl_2j_D_me_3b/Event/histo_TTLJ_bj',
              'dbl_2j_D_me_3b/Event/histo_TTLJ_bb',
              'dbl_2j_D_me_3b/Event/histo_TTLL_jj',
              'dbl_2j_D_me_3b/Event/histo_TTLL_cc',
              'dbl_2j_D_me_3b/Event/histo_TTLL_bj',
              'dbl_2j_D_me_3b/Event/histo_TTLL_bb',
              'dbl_2j_D_me_3b/Event/histo_TTWjets',
              'dbl_2j_D_me_3b/Event/histo_TTZjets',
              'dbl_2j_D_me_3b/Event/histo_Wjets',
              'dbl_2j_D_me_3b/Event/histo_WW',
              'dbl_2j_D_me_3b/Event/histo_WZ',
              'dbl_2j_D_me_3b/Event/histo_ZZ',
          ],
  },
  'dbl_2j_em_2b' : {
      'A' : [
              'dbl_2j_A_em_2b/Event/histo_DATA',
              'dbl_2j_A_em_2b/Event/histo_DY',
              'dbl_2j_A_em_2b/Event/histo_ST',
              'dbl_2j_A_em_2b/Event/histo_TTLJ_jj',
              'dbl_2j_A_em_2b/Event/histo_TTLJ_cc',
              'dbl_2j_A_em_2b/Event/histo_TTLJ_bj',
              'dbl_2j_A_em_2b/Event/histo_TTLJ_bb',
              'dbl_2j_A_em_2b/Event/histo_TTLL_jj',
              'dbl_2j_A_em_2b/Event/histo_TTLL_cc',
              'dbl_2j_A_em_2b/Event/histo_TTLL_bj',
              'dbl_2j_A_em_2b/Event/histo_TTLL_bb',
              'dbl_2j_A_em_2b/Event/histo_TTWjets',
              'dbl_2j_A_em_2b/Event/histo_TTZjets',
              'dbl_2j_A_em_2b/Event/histo_Wjets',
              'dbl_2j_A_em_2b/Event/histo_WW',
              'dbl_2j_A_em_2b/Event/histo_WZ',
              'dbl_2j_A_em_2b/Event/histo_ZZ',
          ],
      'B' : [
              'dbl_2j_B_em_2b/Event/histo_DATA',
              'dbl_2j_B_em_2b/Event/histo_DY',
              'dbl_2j_B_em_2b/Event/histo_ST',
              'dbl_2j_B_em_2b/Event/histo_TTLJ_jj',
              'dbl_2j_B_em_2b/Event/histo_TTLJ_cc',
              'dbl_2j_B_em_2b/Event/histo_TTLJ_bj',
              'dbl_2j_B_em_2b/Event/histo_TTLJ_bb',
              'dbl_2j_B_em_2b/Event/histo_TTLL_jj',
              'dbl_2j_B_em_2b/Event/histo_TTLL_cc',
              'dbl_2j_B_em_2b/Event/histo_TTLL_bj',
              'dbl_2j_B_em_2b/Event/histo_TTLL_bb',
              'dbl_2j_B_em_2b/Event/histo_TTWjets',
              'dbl_2j_B_em_2b/Event/histo_TTZjets',
              'dbl_2j_B_em_2b/Event/histo_Wjets',
              'dbl_2j_B_em_2b/Event/histo_WW',
              'dbl_2j_B_em_2b/Event/histo_WZ',
              'dbl_2j_B_em_2b/Event/histo_ZZ',
          ],
      'C' : [
              'dbl_2j_C_em_2b/Event/histo_DATA',
              'dbl_2j_C_em_2b/Event/histo_DY',
              'dbl_2j_C_em_2b/Event/histo_ST',
              'dbl_2j_C_em_2b/Event/histo_TTLJ_jj',
              'dbl_2j_C_em_2b/Event/histo_TTLJ_cc',
              'dbl_2j_C_em_2b/Event/histo_TTLJ_bj',
              'dbl_2j_C_em_2b/Event/histo_TTLJ_bb',
              'dbl_2j_C_em_2b/Event/histo_TTLL_jj',
              'dbl_2j_C_em_2b/Event/histo_TTLL_cc',
              'dbl_2j_C_em_2b/Event/histo_TTLL_bj',
              'dbl_2j_C_em_2b/Event/histo_TTLL_bb',
              'dbl_2j_C_em_2b/Event/histo_TTWjets',
              'dbl_2j_C_em_2b/Event/histo_TTZjets',
              'dbl_2j_C_em_2b/Event/histo_Wjets',
              'dbl_2j_C_em_2b/Event/histo_WW',
              'dbl_2j_C_em_2b/Event/histo_WZ',
              'dbl_2j_C_em_2b/Event/histo_ZZ',
          ],
      'D' : [
              'dbl_2j_D_em_2b/Event/histo_DATA',
              'dbl_2j_D_em_2b/Event/histo_DY',
              'dbl_2j_D_em_2b/Event/histo_ST',
              'dbl_2j_D_em_2b/Event/histo_TTLJ_jj',
              'dbl_2j_D_em_2b/Event/histo_TTLJ_cc',
              'dbl_2j_D_em_2b/Event/histo_TTLJ_bj',
              'dbl_2j_D_em_2b/Event/histo_TTLJ_bb',
              'dbl_2j_D_em_2b/Event/histo_TTLL_jj',
              'dbl_2j_D_em_2b/Event/histo_TTLL_cc',
              'dbl_2j_D_em_2b/Event/histo_TTLL_bj',
              'dbl_2j_D_em_2b/Event/histo_TTLL_bb',
              'dbl_2j_D_em_2b/Event/histo_TTWjets',
              'dbl_2j_D_em_2b/Event/histo_TTZjets',
              'dbl_2j_D_em_2b/Event/histo_Wjets',
              'dbl_2j_D_em_2b/Event/histo_WW',
              'dbl_2j_D_em_2b/Event/histo_WZ',
              'dbl_2j_D_em_2b/Event/histo_ZZ',
          ],
  },
  'dbl_2j_em_3b' : {
      'A' : [
              'dbl_2j_A_em_3b/Event/histo_DATA',
              'dbl_2j_A_em_3b/Event/histo_DY',
              'dbl_2j_A_em_3b/Event/histo_ST',
              'dbl_2j_A_em_3b/Event/histo_TTLJ_jj',
              'dbl_2j_A_em_3b/Event/histo_TTLJ_cc',
              'dbl_2j_A_em_3b/Event/histo_TTLJ_bj',
              'dbl_2j_A_em_3b/Event/histo_TTLJ_bb',
              'dbl_2j_A_em_3b/Event/histo_TTLL_jj',
              'dbl_2j_A_em_3b/Event/histo_TTLL_cc',
              'dbl_2j_A_em_3b/Event/histo_TTLL_bj',
              'dbl_2j_A_em_3b/Event/histo_TTLL_bb',
              'dbl_2j_A_em_3b/Event/histo_TTWjets',
              'dbl_2j_A_em_3b/Event/histo_TTZjets',
              'dbl_2j_A_em_3b/Event/histo_Wjets',
              'dbl_2j_A_em_3b/Event/histo_WW',
              'dbl_2j_A_em_3b/Event/histo_WZ',
              'dbl_2j_A_em_3b/Event/histo_ZZ',
          ],
      'B' : [
              'dbl_2j_B_em_3b/Event/histo_DATA',
              'dbl_2j_B_em_3b/Event/histo_DY',
              'dbl_2j_B_em_3b/Event/histo_ST',
              'dbl_2j_B_em_3b/Event/histo_TTLJ_jj',
              'dbl_2j_B_em_3b/Event/histo_TTLJ_cc',
              'dbl_2j_B_em_3b/Event/histo_TTLJ_bj',
              'dbl_2j_B_em_3b/Event/histo_TTLJ_bb',
              'dbl_2j_B_em_3b/Event/histo_TTLL_jj',
              'dbl_2j_B_em_3b/Event/histo_TTLL_cc',
              'dbl_2j_B_em_3b/Event/histo_TTLL_bj',
              'dbl_2j_B_em_3b/Event/histo_TTLL_bb',
              'dbl_2j_B_em_3b/Event/histo_TTWjets',
              'dbl_2j_B_em_3b/Event/histo_TTZjets',
              'dbl_2j_B_em_3b/Event/histo_Wjets',
              'dbl_2j_B_em_3b/Event/histo_WW',
              'dbl_2j_B_em_3b/Event/histo_WZ',
              'dbl_2j_B_em_3b/Event/histo_ZZ',
          ],
      'C' : [
              'dbl_2j_C_em_3b/Event/histo_DATA',
              'dbl_2j_C_em_3b/Event/histo_DY',
              'dbl_2j_C_em_3b/Event/histo_ST',
              'dbl_2j_C_em_3b/Event/histo_TTLJ_jj',
              'dbl_2j_C_em_3b/Event/histo_TTLJ_cc',
              'dbl_2j_C_em_3b/Event/histo_TTLJ_bj',
              'dbl_2j_C_em_3b/Event/histo_TTLJ_bb',
              'dbl_2j_C_em_3b/Event/histo_TTLL_jj',
              'dbl_2j_C_em_3b/Event/histo_TTLL_cc',
              'dbl_2j_C_em_3b/Event/histo_TTLL_bj',
              'dbl_2j_C_em_3b/Event/histo_TTLL_bb',
              'dbl_2j_C_em_3b/Event/histo_TTWjets',
              'dbl_2j_C_em_3b/Event/histo_TTZjets',
              'dbl_2j_C_em_3b/Event/histo_Wjets',
              'dbl_2j_C_em_3b/Event/histo_WW',
              'dbl_2j_C_em_3b/Event/histo_WZ',
              'dbl_2j_C_em_3b/Event/histo_ZZ',
          ],
      'D' : [
              'dbl_2j_D_em_3b/Event/histo_DATA',
              'dbl_2j_D_em_3b/Event/histo_DY',
              'dbl_2j_D_em_3b/Event/histo_ST',
              'dbl_2j_D_em_3b/Event/histo_TTLJ_jj',
              'dbl_2j_D_em_3b/Event/histo_TTLJ_cc',
              'dbl_2j_D_em_3b/Event/histo_TTLJ_bj',
              'dbl_2j_D_em_3b/Event/histo_TTLJ_bb',
              'dbl_2j_D_em_3b/Event/histo_TTLL_jj',
              'dbl_2j_D_em_3b/Event/histo_TTLL_cc',
              'dbl_2j_D_em_3b/Event/histo_TTLL_bj',
              'dbl_2j_D_em_3b/Event/histo_TTLL_bb',
              'dbl_2j_D_em_3b/Event/histo_TTWjets',
              'dbl_2j_D_em_3b/Event/histo_TTZjets',
              'dbl_2j_D_em_3b/Event/histo_Wjets',
              'dbl_2j_D_em_3b/Event/histo_WW',
              'dbl_2j_D_em_3b/Event/histo_WZ',
              'dbl_2j_D_em_3b/Event/histo_ZZ',
          ],
  },
}


import copy
input_dict = {}
input_dict[''] = copy.deepcopy(chennels)

nuisances = [
        'CMS_btag_lfUp',
        'CMS_btag_lfDown',
        'CMS_btag_hfUp',
        'CMS_btag_hfDown',
        'CMS_btag_hfstats1_2016Up',
        'CMS_btag_hfstats1_2016Down',
        'CMS_btag_hfstats2_2016Up',
        'CMS_btag_hfstats2_2016Down',
        'CMS_btag_lfstats1_2016Up',
        'CMS_btag_lfstats1_2016Down',
        'CMS_btag_lfstats2_2016Up',
        'CMS_btag_lfstats2_2016Down',
        'CMS_btag_cferr1Up',
        'CMS_btag_cferr1Down',
        'CMS_btag_cferr2Up',
        'CMS_btag_cferr2Down',
        'ttbbUp',
        'ttbbDown',
        'ttccUp',
        'ttccDown',
        'ttXsecUp',
        'ttXsecDown',
        ]

for nuisance in nuisances:
  input_dict[nuisance] = copy.deepcopy(input_dict[''])
  for ch in input_dict[nuisance]:
    for region in input_dict[nuisance][ch]:
      for i, histo_name in enumerate(input_dict[nuisance][ch][region]):
        if 'histo_DATA' not in histo_name:
          histo_name_nuis = histo_name + '_' + nuisance
        else:
          histo_name_nuis = histo_name
        input_dict[nuisance][ch][region][i] = histo_name_nuis


bins = {
   'sng_4j_eleCH_2b' : np.array([-2.5, -1.479, 0, 1.479, 2.5]),
   'sng_4j_eleCH_3b' : np.array([-2.5, 0, 2.5]),
   'sng_4j_muCH_2b'  : np.array([-2.4, -1.2, -0.9, 0, 0.9, 1.2, 2.4]),
   'sng_4j_muCH_3b'  : np.array([-2.4, -0.9, 0, 0.9, 2.4]),
   'dbl_2j_ee_2b'    : np.array([0.,2.]),
   'dbl_2j_ee_3b'    : np.array([0.,2.]),
   'dbl_2j_mm_2b'    : np.array([0.,2.]),
   'dbl_2j_mm_3b'    : np.array([0.,2.]),
   'dbl_2j_em_2b'    : np.array([0.,2.]),
   'dbl_2j_em_3b'    : np.array([0.,2.]),
   'dbl_2j_me_2b'    : np.array([0.,2.]),
   'dbl_2j_me_3b'    : np.array([0.,2.]),
}

def GetHisto(histoNameList, rebin):
  histo_rebinned = None
  for histoName in histoNameList:
    print(histoName)
    if 'ttbb' in histoName or 'ttcc' in histoName or 'ttXsec' in histoName:
        histo = f.Get('_'.join(histoName.split('_')[:-1]))
    else:
      histo = f.Get(histoName)

    if histo_rebinned == None:
      if 'histo_DATA' not in histoName:
        raise Exception('first entry should be histo_DATA')
      histo_rebinned = histo.Rebin(rebin.size-1, histo.GetName()+'_rebinned', rebin)
    else:
      if 'histo_DATA' in histoName:
        raise Exception('histo_DATA is entered for the negative summation')
      # scale ttbar samples
      if 'histo_TTLL_' in histoName or 'histo_TTLJ_' in histoName:

        # ttbb ttcc scale
        if '_bb' in histoName or '_bj' in histoName:
          if '_ttbbUp' in histoName:
            scale = 1.3
          elif '_ttbbDown' in histoName:
            scale = 1./1.3
          else:
            scale = 1.0
        elif '_cc' in histoName:
          if '_ttccUp' in histoName:
            scale = 1.3
          elif '_ttccDown' in histoName:
            scale = 1./1.3
          else:
            scale = 1.0
        elif '_jj' in histoName:
          if '_ttbbUp' in histoName:
            scale = 0.99247 #((364.35-1.3*(1.433+6.782)-1.0*28.21)/(327.93))
          elif '_ttbbDown' in histoName:
            scale = 1.0058  #((364.35-(1./1.3)*(1.433+6.782)-1.0*28.21)/(327.93))
          elif '_ttccUp' in histoName:
            scale = 0.97418 #((364.35-1.0*(1.433+6.782)-1.3*28.21)/(327.93))
          elif '_ttccDown' in histoName:
            scale = 1.0198  #((364.35-1.0*(1.433+6.782)-(1./1.3)*28.21)/(327.93))
          else:
            scale = 1.0 
        else:
          raise Exception('unsupported ttbar category')
        # ttXsec scale
        if '_ttXsecUp' in histoName:
          scale = 1.06114
        elif '_ttXsecDown' in histoName:
          scale = 1./1.06114
        histo.Scale(scale)
      histo_rebinned.Add(histo.Rebin(rebin.size-1, histo.GetName()+'_rebinned', rebin), -1)

  return histo_rebinned

def truncated_normal_mean(mu, sigma):
  # probability distribution truncating below zero
  pi = ROOT.TMath.Pi()
  mean = mu + (1/ROOT.TMath.Sqrt(2*pi))*ROOT.TMath.Exp(-1/2*(-mu/sigma)**2)/(1-1/2*(1+ROOT.TMath.Erf(-mu/(2**(1/2)*pi))))
  return mean

def SuppressZeros(histo):
  nBinsX = histo.GetNbinsX()
  for i in range(nBinsX):
    content = histo.GetBinContent(i+1)
    error   = histo.GetBinError(i+1)
    if content < 0 or content == 0:
      mean    = truncated_normal_mean(content,error)
      if mean < 0:
        histo.SetBinContent(i+1,1e-10)
        histo.SetBinError(i+1,1e-10)
      else:
        print("mean",mean,"mu",content,"std",error)
        histo.SetBinContent(i+1,mean)
        histo.SetBinError(i+1,content+error-mean)


def AppendForEnvelop(histos_envelop, ch, histoD):
  if ch not in histos_envelop:
    histos_envelop[ch] = []
  histos_envelop[ch].append(histoD)

def WriteEnvelop(histos_envelop, ch):
  histo_list = histos_envelop[ch]
  nBinsX = histo_list[0].GetNbinsX()
  bins_cont_up, bins_err_up     = [0.]*nBinsX, [0.]*nBinsX
  bins_cont_down, bins_err_down = [999999999999999999999999999999]*nBinsX, [999999999999999999999999999999]*nBinsX

  for i_histo, histo in enumerate(histo_list):
    # if sum is below zero, skip this histo
    sum_binc = sum([histo.GetBinContent(i+1) for i in range(nBinsX)])
    if i_histo>0 and sum_binc <= 1e-8:
      continue
    #
    for i in range(nBinsX):
      bin_content = histo.GetBinContent(i+1)
      bin_error = histo.GetBinError(i+1)
      if bins_cont_up[i] < bin_content:
        bins_cont_up[i] = bin_content
        bins_err_up[i]  = bin_error
      if bins_cont_down[i] > bin_content:
        bins_cont_down[i] = bin_content
        bins_err_down[i]  = bin_error
      
  histo_envelop_up   = histo_list[0].Clone('histo_TF_data_driven_envelopUp')
  histo_envelop_down = histo_list[0].Clone('histo_TF_data_driven_envelopDown')

  for i in range(nBinsX):
    histo_envelop_up.SetBinContent(i+1,bins_cont_up[i])
    histo_envelop_up.SetBinError(i+1,bins_err_up[i])
    histo_envelop_down.SetBinContent(i+1,bins_cont_down[i])
    histo_envelop_down.SetBinError(i+1,bins_err_down[i])

  outFile.cd(ch)
  histo_envelop_up.Write('histo_TF_data_driven_envelopUp')
  histo_envelop_down.Write('histo_TF_data_driven_envelopDown')


outFile.cd()

histos_envelop = {}
for tag_key in input_dict:
  chennels = input_dict[tag_key]
  for ch in chennels:
    outFile.mkdir(ch)
    outFile.cd(ch)
    histoNameB = chennels[ch]['B']
    histoNameC = chennels[ch]['C']
    rebin      = bins[ch]
  
    print(histoNameB)
    print(histoNameC)
  
    histoB = GetHisto(histoNameB, rebin)
    histoC = GetHisto(histoNameC, rebin)
  
    histoB.Divide(histoC)  # transfer factor : looser ID region to tighter ID region
    histoB.SetName(ch)
    outHistName = 'histo_TF_data_driven'
    if tag_key == '':
      pass
    else:
      outHistName += '_' + tag_key.replace('CMS_','')

    SuppressZeros(histoB)
    histoB.Write(outHistName)
    AppendForEnvelop(histos_envelop, ch, histoB)

for ch in input_dict['']:
  WriteEnvelop(histos_envelop, ch)

outFile.Close()
