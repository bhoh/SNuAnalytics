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

outFileName = 'ABCD_SF.root'
outFile =  ROOT.TFile(outFileName,'RECREATE')


chennels = {
  'sng_4j_eleCH_2b' : {
        'B' : [
                'sng_4j_B_eleCH_2b/EleSCEta/histo_QCD_EM',
                'sng_4j_B_eleCH_2b/EleSCEta/histo_QCD_bcToE',
            ],
        'C' : [
                'sng_4j_C_eleCH_2b/EleSCEta/histo_QCD_EM',
                'sng_4j_C_eleCH_2b/EleSCEta/histo_QCD_bcToE',

            ],
      },
  'sng_4j_eleCH_3b' : {
        'B' : [
                'sng_4j_B_eleCH_3b/EleSCEta/histo_QCD_EM',
                'sng_4j_B_eleCH_3b/EleSCEta/histo_QCD_bcToE',
            ],
        'C' : [
                'sng_4j_C_eleCH_3b/EleSCEta/histo_QCD_EM',
                'sng_4j_C_eleCH_3b/EleSCEta/histo_QCD_bcToE',

            ],
      },
  'sng_4j_muCH_2b'  : {
        'B' : [
                'sng_4j_B_muCH_2b/MuonEta/histo_QCD_MU',
            ],
        'C' : [
                'sng_4j_C_muCH_2b/MuonEta/histo_QCD_MU',
            ],
      },
  'sng_4j_muCH_3b'  : {
        'B' : [
                'sng_4j_B_muCH_3b/MuonEta/histo_QCD_MU',
            ],
        'C' : [
                'sng_4j_C_muCH_3b/MuonEta/histo_QCD_MU',
            ],

      },
  #'dbl_2j_ee_2b' : {
  #      'B' : [
  #            'dbl_2j_B_ee_2b/Event/histo_QCD_EM',
  #            'dbl_2j_B_ee_2b/Event/histo_QCD_bcToE',
  #            'dbl_2j_B_ee_2b/Event/histo_QCD_MU',
  #          ],
  #      'C' : [
  #            'dbl_2j_C_ee_2b/Event/histo_QCD_EM',
  #            'dbl_2j_C_ee_2b/Event/histo_QCD_bcToE',
  #            'dbl_2j_C_ee_2b/Event/histo_QCD_MU',
  #          ],
  #    },
  #'dbl_2j_ee_3b' : {
  #      'B' : [
  #            'dbl_2j_B_ee_3b/Event/histo_QCD_EM',
  #            'dbl_2j_B_ee_3b/Event/histo_QCD_bcToE',
  #            'dbl_2j_B_ee_3b/Event/histo_QCD_MU',
  #          ],
  #      'C' : [
  #            'dbl_2j_C_ee_3b/Event/histo_QCD_EM',
  #            'dbl_2j_C_ee_3b/Event/histo_QCD_bcToE',
  #            'dbl_2j_C_ee_3b/Event/histo_QCD_MU',
  #          ],
  #    },
  #'dbl_2j_em_2b' : {
  #      'B' : [
  #            'dbl_2j_B_em_2b/Event/histo_QCD_EM',
  #            'dbl_2j_B_em_2b/Event/histo_QCD_bcToE',
  #            'dbl_2j_B_em_2b/Event/histo_QCD_MU',
  #          ],
  #      'C' : [
  #            'dbl_2j_C_em_2b/Event/histo_QCD_EM',
  #            'dbl_2j_C_em_2b/Event/histo_QCD_bcToE',
  #            'dbl_2j_C_em_2b/Event/histo_QCD_MU',
  #          ],
  #    },
  #'dbl_2j_em_3b' : {
  #      'B' : [
  #            'dbl_2j_B_em_3b/Event/histo_QCD_EM',
  #            'dbl_2j_B_em_3b/Event/histo_QCD_bcToE',
  #            'dbl_2j_B_em_3b/Event/histo_QCD_MU',
  #          ],
  #      'C' : [
  #            'dbl_2j_C_em_3b/Event/histo_QCD_EM',
  #            'dbl_2j_C_em_3b/Event/histo_QCD_bcToE',
  #            'dbl_2j_C_em_3b/Event/histo_QCD_MU',
  #          ],
  #    },
  #'dbl_2j_me_2b' : {
  #      'B' : [
  #            'dbl_2j_B_me_2b/Event/histo_QCD_EM',
  #            'dbl_2j_B_me_2b/Event/histo_QCD_bcToE',
  #            'dbl_2j_B_me_2b/Event/histo_QCD_MU',
  #          ],
  #      'C' : [
  #            'dbl_2j_C_me_2b/Event/histo_QCD_EM',
  #            'dbl_2j_C_me_2b/Event/histo_QCD_bcToE',
  #            'dbl_2j_C_me_2b/Event/histo_QCD_MU',
  #          ],
  #    },
  #'dbl_2j_me_3b' : {
  #      'B' : [
  #            'dbl_2j_B_me_3b/Event/histo_QCD_EM',
  #            'dbl_2j_B_me_3b/Event/histo_QCD_bcToE',
  #            'dbl_2j_B_me_3b/Event/histo_QCD_MU',
  #          ],
  #      'C' : [
  #            'dbl_2j_C_me_3b/Event/histo_QCD_EM',
  #            'dbl_2j_C_me_3b/Event/histo_QCD_bcToE',
  #            'dbl_2j_C_me_3b/Event/histo_QCD_MU',
  #          ],
  #    },
  #'dbl_2j_mm_2b' : {
  #      'B' : [
  #            'dbl_2j_B_mm_2b/Event/histo_QCD_EM',
  #            'dbl_2j_B_mm_2b/Event/histo_QCD_bcToE',
  #            'dbl_2j_B_mm_2b/Event/histo_QCD_MU',
  #          ],
  #      'C' : [
  #            'dbl_2j_C_mm_2b/Event/histo_QCD_EM',
  #            'dbl_2j_C_mm_2b/Event/histo_QCD_bcToE',
  #            'dbl_2j_C_mm_2b/Event/histo_QCD_MU',
  #          ],
  #    },
  #'dbl_2j_mm_3b' : {
  #      'B' : [
  #            'dbl_2j_B_mm_3b/Event/histo_QCD_EM',
  #            'dbl_2j_B_mm_3b/Event/histo_QCD_bcToE',
  #            'dbl_2j_B_mm_3b/Event/histo_QCD_MU',
  #          ],
  #      'C' : [
  #            'dbl_2j_C_mm_3b/Event/histo_QCD_EM',
  #            'dbl_2j_C_mm_3b/Event/histo_QCD_bcToE',
  #            'dbl_2j_C_mm_3b/Event/histo_QCD_MU',
  #          ],
  #    },
}

bins = {
   'sng_4j_eleCH_2b' : np.array([-2.5, 2.5]),
   'sng_4j_eleCH_3b' : np.array([-2.5, 2.5]),
   'sng_4j_muCH_2b'  : np.array([-2.4, 2.4]),
   'sng_4j_muCH_3b'  : np.array([-2.4, 2.4]),
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
    histo = f.Get(histoName)

    if histo_rebinned == None:
      histo_rebinned = histo.Rebin(rebin.size-1, histo.GetName()+'_rebinned', rebin)
    else:
      histo_rebinned.Add(histo.Rebin(rebin.size-1, histo.GetName()+'_rebinned', rebin))

  return histo_rebinned

outFile.cd()
for ch in chennels:
  histoNameB = chennels[ch]['B']
  histoNameC = chennels[ch]['C']
  rebin      = bins[ch]

  print(histoNameB)
  print(histoNameC)

  histoB = GetHisto(histoNameB, rebin)
  histoC = GetHisto(histoNameC, rebin)

  histoB.Divide(histoC)  # convertion factor : looser ID region to tighter ID region
  histoB.SetName(ch)
  histoB.Write()

outFile.Close()
