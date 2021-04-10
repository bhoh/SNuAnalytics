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
import copy

fileName='rootFile_2016_SKIM7_QCD_ABCD_SF/hadd.root'

outFileName = 'ABCD_data_driven_shape.root'
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

input_dict = {
  '' : {
    'input'    : 'rootFile_2016_SKIM7_QCD_ABCD_SF/hadd.root',
    'chennels' : {
      'sng_4j_D_eleCH_2b' : {
            'Event' : copy.deepcopy(samples),
            'hadronic_top_pt' : copy.deepcopy(samples),
            '1st_leading_jet_pt' : copy.deepcopy(samples),
            '1st_leading_jet_eta' : copy.deepcopy(samples),
            'Lepton_pt[0]' : copy.deepcopy(samples),
            'Lepton_pt[1]' : copy.deepcopy(samples),
            'Lepton_eta[0]' : copy.deepcopy(samples),
            'Lepton_eta[1]' : copy.deepcopy(samples),
            'PuppiMet' : copy.deepcopy(samples),
            'PV_npvs' : copy.deepcopy(samples),
            'nCleanJet20_2p4' : copy.deepcopy(samples),
            'nCleanJet30_2p4' : copy.deepcopy(samples),
            'nCleanJet20to30_2p4_PU_M' : copy.deepcopy(samples),
            'nBJets_WP_M' : copy.deepcopy(samples),
            'nBJets_WP_M_20to30' : copy.deepcopy(samples),
            'fitted_dijet_M' : copy.deepcopy(samples),
            'fitted_dijet_M_high' : copy.deepcopy(samples),
            'fitted_dijet_M_down_type_jet_b_tagged' : copy.deepcopy(samples),
            'fitted_dijet_M_high_down_type_jet_b_tagged' : copy.deepcopy(samples),
          },
      'sng_4j_D_eleCH_3b' : {
            'Event' : copy.deepcopy(samples),
            'hadronic_top_pt' : copy.deepcopy(samples),
            '1st_leading_jet_pt' : copy.deepcopy(samples),
            '1st_leading_jet_eta' : copy.deepcopy(samples),
            'Lepton_pt[0]' : copy.deepcopy(samples),
            'Lepton_pt[1]' : copy.deepcopy(samples),
            'Lepton_eta[1]' : copy.deepcopy(samples),
            'PuppiMet' : copy.deepcopy(samples),
            'PV_npvs' : copy.deepcopy(samples),
            'nCleanJet20_2p4' : copy.deepcopy(samples),
            'nCleanJet30_2p4' : copy.deepcopy(samples),
            'nCleanJet20to30_2p4_PU_M' : copy.deepcopy(samples),
            'nBJets_WP_M' : copy.deepcopy(samples),
            'nBJets_WP_M_20to30' : copy.deepcopy(samples),
            'Lepton_eta[0]' : copy.deepcopy(samples),
            'fitted_dijet_M' : copy.deepcopy(samples),
            'fitted_dijet_M_high' : copy.deepcopy(samples),
            'fitted_dijet_M_down_type_jet_b_tagged' : copy.deepcopy(samples),
            'fitted_dijet_M_high_down_type_jet_b_tagged' : copy.deepcopy(samples),
          },
      'sng_4j_D_muCH_2b'  : {
            'Event' : copy.deepcopy(samples),
            'hadronic_top_pt' : copy.deepcopy(samples),
            '1st_leading_jet_pt' : copy.deepcopy(samples),
            '1st_leading_jet_eta' : copy.deepcopy(samples),
            'Lepton_pt[0]' : copy.deepcopy(samples),
            'Lepton_pt[1]' : copy.deepcopy(samples),
            'Lepton_eta[1]' : copy.deepcopy(samples),
            'PuppiMet' : copy.deepcopy(samples),
            'PV_npvs' : copy.deepcopy(samples),
            'nCleanJet20_2p4' : copy.deepcopy(samples),
            'nCleanJet30_2p4' : copy.deepcopy(samples),
            'nCleanJet20to30_2p4_PU_M' : copy.deepcopy(samples),
            'nBJets_WP_M' : copy.deepcopy(samples),
            'nBJets_WP_M_20to30' : copy.deepcopy(samples),
            'Lepton_eta[0]' : copy.deepcopy(samples),
            'fitted_dijet_M' : copy.deepcopy(samples),
            'fitted_dijet_M_high' : copy.deepcopy(samples),
            'fitted_dijet_M_down_type_jet_b_tagged' : copy.deepcopy(samples),
            'fitted_dijet_M_high_down_type_jet_b_tagged' : copy.deepcopy(samples),
          },
      'sng_4j_D_muCH_3b'  : {
            'Event' : copy.deepcopy(samples),
            'hadronic_top_pt' : copy.deepcopy(samples),
            '1st_leading_jet_pt' : copy.deepcopy(samples),
            '1st_leading_jet_eta' : copy.deepcopy(samples),
            'Lepton_pt[0]' : copy.deepcopy(samples),
            'Lepton_pt[1]' : copy.deepcopy(samples),
            'Lepton_eta[1]' : copy.deepcopy(samples),
            'PuppiMet' : copy.deepcopy(samples),
            'PV_npvs' : copy.deepcopy(samples),
            'nCleanJet20_2p4' : copy.deepcopy(samples),
            'nCleanJet30_2p4' : copy.deepcopy(samples),
            'nCleanJet20to30_2p4_PU_M' : copy.deepcopy(samples),
            'nBJets_WP_M' : copy.deepcopy(samples),
            'nBJets_WP_M_20to30' : copy.deepcopy(samples),
            'Lepton_eta[0]' : copy.deepcopy(samples),
            'fitted_dijet_M' : copy.deepcopy(samples),
            'fitted_dijet_M_high' : copy.deepcopy(samples),
            'fitted_dijet_M_down_type_jet_b_tagged' : copy.deepcopy(samples),
            'fitted_dijet_M_high_down_type_jet_b_tagged' : copy.deepcopy(samples),
          },
      'dbl_2j_D_ee_2b' : {
            'Bins' : copy.deepcopy(samples),
            'Event' : copy.deepcopy(samples),
            'hadronic_top_pt' : copy.deepcopy(samples),
            '1st_leading_jet_pt' : copy.deepcopy(samples),
            '1st_leading_jet_eta' : copy.deepcopy(samples),
            'Lepton_pt[0]' : copy.deepcopy(samples),
            'Lepton_pt[1]' : copy.deepcopy(samples),
            'Lepton_eta[1]' : copy.deepcopy(samples),
            'PuppiMet' : copy.deepcopy(samples),
            'PV_npvs' : copy.deepcopy(samples),
            'nCleanJet20_2p4' : copy.deepcopy(samples),
            'nCleanJet30_2p4' : copy.deepcopy(samples),
            'nCleanJet20to30_2p4_PU_M' : copy.deepcopy(samples),
            'nBJets_WP_M' : copy.deepcopy(samples),
            'nBJets_WP_M_20to30' : copy.deepcopy(samples),
            'Lepton_eta[0]' : copy.deepcopy(samples),
            'fitted_dijet_M' : copy.deepcopy(samples),
            'fitted_dijet_M_high' : copy.deepcopy(samples),
            'fitted_dijet_M_down_type_jet_b_tagged' : copy.deepcopy(samples),
            'fitted_dijet_M_high_down_type_jet_b_tagged' : copy.deepcopy(samples),
                      },
      'dbl_2j_D_em_2b' : {
            'Bins' : copy.deepcopy(samples),
            'Event' : copy.deepcopy(samples),
            'hadronic_top_pt' : copy.deepcopy(samples),
            '1st_leading_jet_pt' : copy.deepcopy(samples),
            '1st_leading_jet_eta' : copy.deepcopy(samples),
            'Lepton_pt[0]' : copy.deepcopy(samples),
            'Lepton_pt[1]' : copy.deepcopy(samples),
            'Lepton_eta[1]' : copy.deepcopy(samples),
            'PuppiMet' : copy.deepcopy(samples),
            'PV_npvs' : copy.deepcopy(samples),
            'nCleanJet20_2p4' : copy.deepcopy(samples),
            'nCleanJet30_2p4' : copy.deepcopy(samples),
            'nCleanJet20to30_2p4_PU_M' : copy.deepcopy(samples),
            'nBJets_WP_M' : copy.deepcopy(samples),
            'nBJets_WP_M_20to30' : copy.deepcopy(samples),
            'Lepton_eta[0]' : copy.deepcopy(samples),
            'fitted_dijet_M' : copy.deepcopy(samples),
            'fitted_dijet_M_high' : copy.deepcopy(samples),
            'fitted_dijet_M_down_type_jet_b_tagged' : copy.deepcopy(samples),
            'fitted_dijet_M_high_down_type_jet_b_tagged' : copy.deepcopy(samples),
          },
      'dbl_2j_D_me_2b' : {
            'Bins' : copy.deepcopy(samples),
            'Event' : copy.deepcopy(samples),
            'hadronic_top_pt' : copy.deepcopy(samples),
            '1st_leading_jet_pt' : copy.deepcopy(samples),
            '1st_leading_jet_eta' : copy.deepcopy(samples),
            'Lepton_pt[0]' : copy.deepcopy(samples),
            'Lepton_pt[1]' : copy.deepcopy(samples),
            'Lepton_eta[1]' : copy.deepcopy(samples),
            'PuppiMet' : copy.deepcopy(samples),
            'PV_npvs' : copy.deepcopy(samples),
            'nCleanJet20_2p4' : copy.deepcopy(samples),
            'nCleanJet30_2p4' : copy.deepcopy(samples),
            'nCleanJet20to30_2p4_PU_M' : copy.deepcopy(samples),
            'nBJets_WP_M' : copy.deepcopy(samples),
            'nBJets_WP_M_20to30' : copy.deepcopy(samples),
            'Lepton_eta[0]' : copy.deepcopy(samples),
            'fitted_dijet_M' : copy.deepcopy(samples),
            'fitted_dijet_M_high' : copy.deepcopy(samples),
            'fitted_dijet_M_down_type_jet_b_tagged' : copy.deepcopy(samples),
            'fitted_dijet_M_high_down_type_jet_b_tagged' : copy.deepcopy(samples),
            
          },
      'dbl_2j_D_mm_2b' : {
            'Bins' : copy.deepcopy(samples),
            'Event' : copy.deepcopy(samples),
            'hadronic_top_pt' : copy.deepcopy(samples),
            '1st_leading_jet_pt' : copy.deepcopy(samples),
            '1st_leading_jet_eta' : copy.deepcopy(samples),
            'Lepton_pt[0]' : copy.deepcopy(samples),
            'Lepton_pt[1]' : copy.deepcopy(samples),
            'Lepton_eta[1]' : copy.deepcopy(samples),
            'PuppiMet' : copy.deepcopy(samples),
            'PV_npvs' : copy.deepcopy(samples),
            'nCleanJet20_2p4' : copy.deepcopy(samples),
            'nCleanJet30_2p4' : copy.deepcopy(samples),
            'nCleanJet20to30_2p4_PU_M' : copy.deepcopy(samples),
            'nBJets_WP_M' : copy.deepcopy(samples),
            'nBJets_WP_M_20to30' : copy.deepcopy(samples),
            'Lepton_eta[0]' : copy.deepcopy(samples),
            'fitted_dijet_M' : copy.deepcopy(samples),
            'fitted_dijet_M_high' : copy.deepcopy(samples),
            'fitted_dijet_M_down_type_jet_b_tagged' : copy.deepcopy(samples),
            'fitted_dijet_M_high_down_type_jet_b_tagged' : copy.deepcopy(samples),
            
          },
      'dbl_2j_D_ee_3b' : {
            'Bins' : copy.deepcopy(samples),
             'Event' : copy.deepcopy(samples),
            'hadronic_top_pt' : copy.deepcopy(samples),
            '1st_leading_jet_pt' : copy.deepcopy(samples),
            '1st_leading_jet_eta' : copy.deepcopy(samples),
            'Lepton_pt[0]' : copy.deepcopy(samples),
            'Lepton_pt[1]' : copy.deepcopy(samples),
            'Lepton_eta[1]' : copy.deepcopy(samples),
            'PuppiMet' : copy.deepcopy(samples),
            'PV_npvs' : copy.deepcopy(samples),
            'nCleanJet20_2p4' : copy.deepcopy(samples),
            'nCleanJet30_2p4' : copy.deepcopy(samples),
            'nCleanJet20to30_2p4_PU_M' : copy.deepcopy(samples),
            'nBJets_WP_M' : copy.deepcopy(samples),
            'nBJets_WP_M_20to30' : copy.deepcopy(samples),
            'Lepton_eta[0]' : copy.deepcopy(samples),
            'fitted_dijet_M' : copy.deepcopy(samples),
            'fitted_dijet_M_high' : copy.deepcopy(samples),
            'fitted_dijet_M_down_type_jet_b_tagged' : copy.deepcopy(samples),
            'fitted_dijet_M_high_down_type_jet_b_tagged' : copy.deepcopy(samples),           
          },
      'dbl_2j_D_em_3b' : {
            'Bins' : copy.deepcopy(samples),
             'Event' : copy.deepcopy(samples),
            'hadronic_top_pt' : copy.deepcopy(samples),
            '1st_leading_jet_pt' : copy.deepcopy(samples),
            '1st_leading_jet_eta' : copy.deepcopy(samples),
            'Lepton_pt[0]' : copy.deepcopy(samples),
            'Lepton_pt[1]' : copy.deepcopy(samples),
            'Lepton_eta[1]' : copy.deepcopy(samples),
            'PuppiMet' : copy.deepcopy(samples),
            'PV_npvs' : copy.deepcopy(samples),
            'nCleanJet20_2p4' : copy.deepcopy(samples),
            'nCleanJet30_2p4' : copy.deepcopy(samples),
            'nCleanJet20to30_2p4_PU_M' : copy.deepcopy(samples),
            'nBJets_WP_M' : copy.deepcopy(samples),
            'nBJets_WP_M_20to30' : copy.deepcopy(samples),
            'Lepton_eta[0]' : copy.deepcopy(samples),
            'fitted_dijet_M' : copy.deepcopy(samples),
            'fitted_dijet_M_high' : copy.deepcopy(samples),
            'fitted_dijet_M_down_type_jet_b_tagged' : copy.deepcopy(samples),
            'fitted_dijet_M_high_down_type_jet_b_tagged' : copy.deepcopy(samples),           
          },
      'dbl_2j_D_me_3b' : {
            'Bins' : copy.deepcopy(samples),
            'Event' : copy.deepcopy(samples),
            'hadronic_top_pt' : copy.deepcopy(samples),
            '1st_leading_jet_pt' : copy.deepcopy(samples),
            '1st_leading_jet_eta' : copy.deepcopy(samples),
            'Lepton_pt[0]' : copy.deepcopy(samples),
            'Lepton_pt[1]' : copy.deepcopy(samples),
            'Lepton_eta[1]' : copy.deepcopy(samples),
            'PuppiMet' : copy.deepcopy(samples),
            'PV_npvs' : copy.deepcopy(samples),
            'nCleanJet20_2p4' : copy.deepcopy(samples),
            'nCleanJet30_2p4' : copy.deepcopy(samples),
            'nCleanJet20to30_2p4_PU_M' : copy.deepcopy(samples),
            'nBJets_WP_M' : copy.deepcopy(samples),
            'nBJets_WP_M_20to30' : copy.deepcopy(samples),
            'Lepton_eta[0]' : copy.deepcopy(samples),
            'fitted_dijet_M' : copy.deepcopy(samples),
            'fitted_dijet_M_high' : copy.deepcopy(samples),
            'fitted_dijet_M_down_type_jet_b_tagged' : copy.deepcopy(samples),
            'fitted_dijet_M_high_down_type_jet_b_tagged' : copy.deepcopy(samples),            
          },
      'dbl_2j_D_mm_3b' : {
            'Bins' : copy.deepcopy(samples),
            'Event' : copy.deepcopy(samples),
            'hadronic_top_pt' : copy.deepcopy(samples),
            '1st_leading_jet_pt' : copy.deepcopy(samples),
            '1st_leading_jet_eta' : copy.deepcopy(samples),
            'Lepton_pt[0]' : copy.deepcopy(samples),
            'Lepton_pt[1]' : copy.deepcopy(samples),
            'Lepton_eta[1]' : copy.deepcopy(samples),
            'PuppiMet' : copy.deepcopy(samples),
            'PV_npvs' : copy.deepcopy(samples),
            'nCleanJet20_2p4' : copy.deepcopy(samples),
            'nCleanJet30_2p4' : copy.deepcopy(samples),
            'nCleanJet20to30_2p4_PU_M' : copy.deepcopy(samples),
            'nBJets_WP_M' : copy.deepcopy(samples),
            'nBJets_WP_M_20to30' : copy.deepcopy(samples),
            'Lepton_eta[0]' : copy.deepcopy(samples),
            'fitted_dijet_M' : copy.deepcopy(samples),
            'fitted_dijet_M_high' : copy.deepcopy(samples),
            'fitted_dijet_M_down_type_jet_b_tagged' : copy.deepcopy(samples),
            'fitted_dijet_M_high_down_type_jet_b_tagged' : copy.deepcopy(samples),            
          },
      'sng_4j_eleORmuCH_D_2b' : {
            'Event' : copy.deepcopy(samples),
            'hadronic_top_pt' : copy.deepcopy(samples),
            '1st_leading_jet_pt' : copy.deepcopy(samples),
            '1st_leading_jet_eta' : copy.deepcopy(samples),
            'Lepton_pt[0]' : copy.deepcopy(samples),
            'Lepton_pt[1]' : copy.deepcopy(samples),
            'Lepton_eta[0]' : copy.deepcopy(samples),
            'Lepton_eta[1]' : copy.deepcopy(samples),
            'PuppiMet' : copy.deepcopy(samples),
            'PV_npvs' : copy.deepcopy(samples),
            'nCleanJet20_2p4' : copy.deepcopy(samples),
            'nCleanJet30_2p4' : copy.deepcopy(samples),
            'nCleanJet20to30_2p4_PU_M' : copy.deepcopy(samples),
            'nBJets_WP_M' : copy.deepcopy(samples),
            'nBJets_WP_M_20to30' : copy.deepcopy(samples),
            'fitted_dijet_M' : copy.deepcopy(samples),
            'fitted_dijet_M_high' : copy.deepcopy(samples),
            'fitted_dijet_M_down_type_jet_b_tagged' : copy.deepcopy(samples),
            'fitted_dijet_M_high_down_type_jet_b_tagged' : copy.deepcopy(samples),
          },
      'sng_4j_eleORmuCH_D_3b' : {
            'Event' : copy.deepcopy(samples),
            'hadronic_top_pt' : copy.deepcopy(samples),
            '1st_leading_jet_pt' : copy.deepcopy(samples),
            '1st_leading_jet_eta' : copy.deepcopy(samples),
            'Lepton_pt[0]' : copy.deepcopy(samples),
            'Lepton_pt[1]' : copy.deepcopy(samples),
            'Lepton_eta[0]' : copy.deepcopy(samples),
            'Lepton_eta[1]' : copy.deepcopy(samples),
            'PuppiMet' : copy.deepcopy(samples),
            'PV_npvs' : copy.deepcopy(samples),
            'nCleanJet20_2p4' : copy.deepcopy(samples),
            'nCleanJet30_2p4' : copy.deepcopy(samples),
            'nCleanJet20to30_2p4_PU_M' : copy.deepcopy(samples),
            'nBJets_WP_M' : copy.deepcopy(samples),
            'nBJets_WP_M_20to30' : copy.deepcopy(samples),
            'fitted_dijet_M' : copy.deepcopy(samples),
            'fitted_dijet_M_high' : copy.deepcopy(samples),
            'fitted_dijet_M_down_type_jet_b_tagged' : copy.deepcopy(samples),
            'fitted_dijet_M_high_down_type_jet_b_tagged' : copy.deepcopy(samples),
          },

      'dbl_2j_eeORmmORemORme_D_2b' : {
            'Bins' : copy.deepcopy(samples),
            'Event' : copy.deepcopy(samples),
            'hadronic_top_pt' : copy.deepcopy(samples),
            '1st_leading_jet_pt' : copy.deepcopy(samples),
            '1st_leading_jet_eta' : copy.deepcopy(samples),
            'Lepton_pt[0]' : copy.deepcopy(samples),
            'Lepton_pt[1]' : copy.deepcopy(samples),
            'Lepton_eta[1]' : copy.deepcopy(samples),
            'PuppiMet' : copy.deepcopy(samples),
            'PV_npvs' : copy.deepcopy(samples),
            'nCleanJet20_2p4' : copy.deepcopy(samples),
            'nCleanJet30_2p4' : copy.deepcopy(samples),
            'nCleanJet20to30_2p4_PU_M' : copy.deepcopy(samples),
            'nBJets_WP_M' : copy.deepcopy(samples),
            'nBJets_WP_M_20to30' : copy.deepcopy(samples),
            'Lepton_eta[0]' : copy.deepcopy(samples),
            'fitted_dijet_M' : copy.deepcopy(samples),
            'fitted_dijet_M_high' : copy.deepcopy(samples),
            'fitted_dijet_M_down_type_jet_b_tagged' : copy.deepcopy(samples),
            'fitted_dijet_M_high_down_type_jet_b_tagged' : copy.deepcopy(samples),            
          },
      'dbl_2j_eeORmmORemORme_D_3b' : {
            'Bins' : copy.deepcopy(samples),
            'Event' : copy.deepcopy(samples),
            'hadronic_top_pt' : copy.deepcopy(samples),
            '1st_leading_jet_pt' : copy.deepcopy(samples),
            '1st_leading_jet_eta' : copy.deepcopy(samples),
            'Lepton_pt[0]' : copy.deepcopy(samples),
            'Lepton_pt[1]' : copy.deepcopy(samples),
            'Lepton_eta[1]' : copy.deepcopy(samples),
            'PuppiMet' : copy.deepcopy(samples),
            'PV_npvs' : copy.deepcopy(samples),
            'nCleanJet20_2p4' : copy.deepcopy(samples),
            'nCleanJet30_2p4' : copy.deepcopy(samples),
            'nCleanJet20to30_2p4_PU_M' : copy.deepcopy(samples),
            'nBJets_WP_M' : copy.deepcopy(samples),
            'nBJets_WP_M_20to30' : copy.deepcopy(samples),
            'Lepton_eta[0]' : copy.deepcopy(samples),
            'fitted_dijet_M' : copy.deepcopy(samples),
            'fitted_dijet_M_high' : copy.deepcopy(samples),
            'fitted_dijet_M_down_type_jet_b_tagged' : copy.deepcopy(samples),
            'fitted_dijet_M_high_down_type_jet_b_tagged' : copy.deepcopy(samples),            
          },

    },
  },
}

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
        ]

for nuisance in nuisances:
  input_dict[nuisance] = copy.deepcopy(input_dict[''])
  for ch in input_dict[nuisance]['chennels']:
    for var in input_dict[nuisance]['chennels'][ch]:
      for i, histo_name in enumerate(input_dict[nuisance]['chennels'][ch][var]):
        histo_name_nuis = histo_name + '_' + nuisance
        input_dict[nuisance]['chennels'][ch][var][i] = histo_name_nuis

from pprint import pprint
pprint(input_dict)

#bins = {
#   'sng_4j_eleCH_2b' : np.array([-2.5, -1.479, 0, 1.479, 2.5]),
#   'sng_4j_eleCH_3b' : np.array([-2.5, 2.5]),
#   'sng_4j_muCH_2b'  : np.array([-2.4, -1.2, -0.9, 0, 0.9, 1.2, 2.4]),
#   'sng_4j_muCH_3b'  : np.array([-2.4, -0.9, 0, 0.9, 2.4]),
#}

def GetHisto(f_, ch, var, histoNameList, rebin):

  histo_rebinned = None
  for histoName in histoNameList:
    print('%s/%s/%s'%(ch,var,histoName))
    histo = f_.Get('%s/%s/%s'%(ch,var,histoName))

    if histo_rebinned == None:
      if 'histo_DATA' not in histoName:
        raise Exception('first entry should be histo_DATA')
      histo_rebinned = histo.Clone()
    else:
      if 'histo_DATA' in histoName:
        raise Exception('histo_DATA is entered for the negative summation')
      # scale ttbar samples
      if 'histo_TTLL_' in histoName or 'histo_TTLJ_' in histoName:
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

      histo_rebinned.Add(histo, -1)

  return histo_rebinned

def SuppressZeros(histo):
  nBinsX = histo.GetNbinsX()
  for i in range(nBinsX):
    content = histo.GetBinContent(i+1)
    error   = histo.GetBinError(i+1)
    if content < 0:
      if content+error < 0:
        histo.SetBinContent(i+1,0)
        histo.SetBinError(i+1,0)
      else:
        histo.SetBinContent(i+1,0)
        histo.SetBinError(i+1,content+error)

def AppendForEnvelop(histos_envelop, ch, var, histoD):
  if ch not in histos_envelop:
    histos_envelop[ch] = {}
  if var not in histos_envelop[ch]:
    histos_envelop[ch][var] = []
  histos_envelop[ch][var].append(histoD)

def WriteEnvelop(histos_envelop, ch, var):
  histo_list = histos_envelop[ch][var]
  nBinsX = histo_list[0].GetNbinsX()
  bins_cont_up, bins_err_up     = [0.]*nBinsX, [0.]*nBinsX
  bins_cont_down, bins_err_down = [999999999999999999999999999999]*nBinsX, [999999999999999999999999999999]*nBinsX

  for i_histo, histo in enumerate(histo_list):
    # if sum is below zero, skip this histo
    sum_binc = sum([histo.GetBinContent(i+1) for i in range(nBinsX)])
    if i_histo>0 and sum_binc <= 1e-7:
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
      
  histo_envelop_up   = histo_list[0].Clone('histo_QCD_data_driven_qcd_envelopUp')
  histo_envelop_down = histo_list[0].Clone('histo_QCD_data_driven_qcd_envelopDown')

  for i in range(nBinsX):
    histo_envelop_up.SetBinContent(i+1,bins_cont_up[i])
    histo_envelop_up.SetBinError(i+1,bins_err_up[i])
    histo_envelop_down.SetBinContent(i+1,bins_cont_down[i])
    histo_envelop_down.SetBinError(i+1,bins_err_down[i])

  outFile.cd(ch+'/'+var)
  histo_envelop_up.Write('histo_QCD_data_driven_qcd_envelopUp')
  histo_envelop_down.Write('histo_QCD_data_driven_qcd_envelopDown')


histos_envelop = {}

outFile.cd()
for tag_key, tag in input_dict.iteritems():
  f = ROOT.TFile(tag['input'],'READ')
  chennels = tag['chennels']
  for ch in chennels:
    outFile.mkdir(ch)
    outFile.cd(ch)
    for var in chennels[ch]:
      outFile.mkdir(ch+'/'+var)
      outFile.cd(ch+'/'+var)
  
      histoNameD = chennels[ch][var]
      rebin      = None
  
      print(histoNameD)
  
      histoD = GetHisto(f, ch, var, histoNameD, rebin)
      SuppressZeros(histoD)
      outHistName = 'histo_QCD_data_driven'
      if tag_key == '':
        pass
      else:
        if 'btag_' in tag_key:
          outHistName += '_CMS_' + tag_key
        else:
          outHistName += '_' + tag_key
      histoD.Write(outHistName)
      AppendForEnvelop(histos_envelop, ch, var, histoD)

for ch in input_dict['']['chennels']:
  for var in input_dict['']['chennels'][ch]:
    WriteEnvelop(histos_envelop, ch, var)

outFile.Close()
