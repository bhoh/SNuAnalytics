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

fileName='hadd_rebinned.root'
f = ROOT.TFile(fileName,'READ') 

outFileName = 'hadd_rebinned.root'
outFile =  ROOT.TFile(outFileName,'UPDATE')

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
                'sng_4j_B_eleCH_2b/EleSCEta/histo_QCD_EM',
                'sng_4j_B_eleCH_2b/EleSCEta/histo_QCD_bcToE',
                'sng_4j_B_eleCH_2b/EleSCEta/histo_QCD_MU',
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
                'sng_4j_C_eleCH_2b/EleSCEta/histo_QCD_EM',
                'sng_4j_C_eleCH_2b/EleSCEta/histo_QCD_bcToE',
                'sng_4j_C_eleCH_2b/EleSCEta/histo_QCD_MU',

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
                'sng_4j_B_eleCH_3b/EleSCEta/histo_QCD_EM',
                'sng_4j_B_eleCH_3b/EleSCEta/histo_QCD_bcToE',
                'sng_4j_B_eleCH_3b/EleSCEta/histo_QCD_MU',
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
                'sng_4j_C_eleCH_3b/EleSCEta/histo_QCD_EM',
                'sng_4j_C_eleCH_3b/EleSCEta/histo_QCD_bcToE',
                'sng_4j_C_eleCH_3b/EleSCEta/histo_QCD_MU',

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
                'sng_4j_B_muCH_2b/MuonEta/histo_QCD_EM',
                'sng_4j_B_muCH_2b/MuonEta/histo_QCD_bcToE',
                'sng_4j_B_muCH_2b/MuonEta/histo_QCD_MU',
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
                'sng_4j_C_muCH_2b/MuonEta/histo_QCD_EM',
                'sng_4j_C_muCH_2b/MuonEta/histo_QCD_bcToE',
                'sng_4j_C_muCH_2b/MuonEta/histo_QCD_MU',
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
                'sng_4j_B_muCH_3b/MuonEta/histo_QCD_EM',
                'sng_4j_B_muCH_3b/MuonEta/histo_QCD_bcToE',
                'sng_4j_B_muCH_3b/MuonEta/histo_QCD_MU',
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
                'sng_4j_C_muCH_3b/MuonEta/histo_QCD_EM',
                'sng_4j_C_muCH_3b/MuonEta/histo_QCD_bcToE',
                'sng_4j_C_muCH_3b/MuonEta/histo_QCD_MU',
            ],

      },

}


import copy
input_dict = {}
input_dict[''] = copy.deepcopy(chennels)

nuisances = [
        'btag_lfUp',
        'btag_lfDown',
        'btag_hfUp',
        'btag_lfDown',
        'btag_hfstats1_2018Up',
        'btag_hfstats1_2018Down',
        'btag_hfstats2_2018Up',
        'btag_hfstats2_2018Down',
        'btag_lfstats1_2018Up',
        'btag_lfstats1_2018Down',
        'btag_lfstats2_2018Up',
        'btag_lfstats2_2018Down',
        'btag_cferr1Up',
        'btag_cferr1Down',
        'btag_cferr2Up',
        'btag_cferr2Down',
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

def RebinHisto(histoNameList, rebin):
  for histoName in histoNameList:
    print(histoName)
    histo = f.Get(histoName)
    target_dir = '/'.join(histoName.split('/')[:-1])
    outFile.cd(target_dir)
    histo_rebinned = histo.Rebin(rebin.size-1, histo.GetName(), rebin)
    histo_rebinned.Write(histo.GetName(), ROOT.TObject.kOverwrite)

    


for tag_key in input_dict:
  chennels = input_dict[tag_key]
  for ch in chennels:
    histoNameB = chennels[ch]['B']
    histoNameC = chennels[ch]['C']
    rebin      = bins[ch]
  
    print(histoNameB)
    print(histoNameC)
  
    RebinHisto(histoNameB, rebin)
    RebinHisto(histoNameC, rebin)
  
  
outFile.Close()


