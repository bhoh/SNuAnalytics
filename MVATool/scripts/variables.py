
from collections import OrderedDict

class Variables():

  def __init__(self):
    self.isDeltaR = True
    self.isJetEtaPhi = False
    self.permute_leptonic_top_b = False
    self.include_gamma = False
    self.include_pt = True
    self.include_dijet_pt = False
    self.include_dijet_E = False
    self.include_leptonic_side = False

    self.include_ctagging = True
    self.include_btagging = True
    
    self.include_year_label = True
    self.include_mass_label = True
    self.include_dijet_M = True
  
  # do not add spectator, it should be add when using it after training. but TMVAfiller module don't support spectators
  #spectators['fitted_dijet_M_nom'] = {
  #    'definition' : 'fitted_dijet_M_nom',
  #  }
  #spectators['EventNum_mvaCHToCB'] = {
  #    'definition' : 'EventNum_mvaCHToCB',
  #    'type' : 'I'
  #  }
  
  #variables[''] = {
  #    'definition' : '',
  #    'type' : 'D'
  #  }
  
  def getVariables(self):
    variables = OrderedDict()
    #spectators = OrderedDict()
    if self.include_year_label:
      variables['year_label'] = {
              'definition' : 'year_label',
          'type' : 'F'
        }
    
    if self.include_mass_label:
      variables['mass_label'] = {
              'definition' : 'mass_label',
          'type' : 'F'
        }
    

    if self.include_ctagging:
      variables['CvB_jet0_mvaCHToCB_nom'] = {
          'definition' : 'CvB_jet0_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['CvB_jet1_mvaCHToCB_nom'] = {
          'definition' : 'CvB_jet1_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['CvB_jet2_mvaCHToCB_nom'] = {
          'definition' : 'CvB_jet2_mvaCHToCB_nom',
          'type' : 'F'
        }

      variables['CvL_jet0_mvaCHToCB_nom'] = {
          'definition' : 'CvL_jet0_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['CvL_jet1_mvaCHToCB_nom'] = {
          'definition' : 'CvL_jet1_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['CvL_jet2_mvaCHToCB_nom'] = {
          'definition' : 'CvL_jet2_mvaCHToCB_nom',
          'type' : 'F'
        }

    if self.include_btagging:
      variables['csv_jet0_mvaCHToCB_nom'] = {
          'definition' : 'csv_jet0_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['csv_jet1_mvaCHToCB_nom'] = {
          'definition' : 'csv_jet1_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['csv_jet2_mvaCHToCB_nom'] = {
          'definition' : 'csv_jet2_mvaCHToCB_nom',
          'type' : 'F'
        }

    if self.include_dijet_M:
      variables['fitted_dijet_M_nom'] = {
          'definition' : 'fitted_dijet_M_nom',
          'type' : 'F'
        }
      variables['fitted_dijet_M_high_nom'] = {
          'definition' : 'fitted_dijet_M_high_nom',
          'type' : 'F'
        }

    if self.include_leptonic_side:
      variables['csv_jet3_mvaCHToCB_nom'] = {
          'definition' : 'csv_jet3_mvaCHToCB_nom',
          'type' : 'F'
        }
    #variables['avg_csv_had_top'] = {
    #    'definition' : 'avg_csv_had_top := (csv_jet0_mvaCHToCB_nom+csv_jet1_mvaCHToCB_nom+csv_jet2_mvaCHToCB_nom)/3',
    #    'type' : 'F'
    #  }
    #variables['2nd_moment_csv_jet0_mvaCHToCB_nom'] = {
    #        'definition' : '2nd_moment_csv_jet0_mvaCHToCB_nom := (csv_jet0_mvaCHToCB_nom-(csv_jet0_mvaCHToCB_nom+csv_jet1_mvaCHToCB_nom+csv_jet2_mvaCHToCB_nom)/3)*(csv_jet0_mvaCHToCB_nom-(csv_jet0_mvaCHToCB_nom+csv_jet1_mvaCHToCB_nom+csv_jet2_mvaCHToCB_nom)/3)',
    #    'type' : 'F'
    #  }
    #variables['2nd_moment_csv_jet1_mvaCHToCB_nom'] = {
    #        'definition' : '2nd_moment_csv_jet1_mvaCHToCB_nom := (csv_jet1_mvaCHToCB_nom-(csv_jet0_mvaCHToCB_nom+csv_jet1_mvaCHToCB_nom+csv_jet2_mvaCHToCB_nom)/3)*(csv_jet1_mvaCHToCB_nom-(csv_jet0_mvaCHToCB_nom+csv_jet1_mvaCHToCB_nom+csv_jet2_mvaCHToCB_nom)/3)',
    #    'type' : 'F'
    #  }
    #variables['2nd_moment_csv_jet2_mvaCHToCB_nom'] = {
    #        'definition' : '2nd_moment_csv_jet2_mvaCHToCB_nom := (csv_jet2_mvaCHToCB_nom-(csv_jet0_mvaCHToCB_nom+csv_jet1_mvaCHToCB_nom+csv_jet2_mvaCHToCB_nom)/3)*(csv_jet2_mvaCHToCB_nom-(csv_jet0_mvaCHToCB_nom+csv_jet1_mvaCHToCB_nom+csv_jet2_mvaCHToCB_nom)/3)',
    #    'type' : 'F'
    #  }
    if self.include_pt:
      variables['jet_pt0_mvaCHToCB_nom'] = {
          'definition' : 'jet_pt0_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['jet_pt1_mvaCHToCB_nom'] = {
          'definition' : 'jet_pt1_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['jet_pt2_mvaCHToCB_nom'] = {
          'definition' : 'jet_pt2_mvaCHToCB_nom',
          'type' : 'F'
        }
      if self.include_leptonic_side:
        variables['jet_pt3_mvaCHToCB_nom'] = {
            'definition' : 'jet_pt3_mvaCHToCB_nom',
            'type' : 'F'
          }
    
    if self.include_dijet_pt:
      variables['dijet_pt0_mvaCHToCB_nom'] = {
          'definition' : 'dijet_pt0_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['dijet_pt1_mvaCHToCB_nom'] = {
          'definition' : 'dijet_pt1_mvaCHToCB_nom',
          'type' : 'F'
        }
    
    if self.include_dijet_E:
      variables['dijet_E0_mvaCHToCB_nom'] = {
          'definition' : 'dijet_E0_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['dijet_E1_mvaCHToCB_nom'] = {
          'definition' : 'dijet_E1_mvaCHToCB_nom',
          'type' : 'F'
        }
    
    if self.isDeltaR:
      variables['dijet_deltaR0_mvaCHToCB_nom'] = {
          'definition' : 'dijet_deltaR0_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['dijet_deltaR1_mvaCHToCB_nom'] = {
          'definition' : 'dijet_deltaR1_mvaCHToCB_nom',
          'type' : 'F'
        }
      if self.permute_leptonic_top_b:
        variables['dijet_deltaR2_mvaCHToCB_nom'] = {
            'definition' : 'dijet_deltaR2_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['dijet_deltaR3_mvaCHToCB_nom'] = {
            'definition' : 'dijet_deltaR3_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['dijet_deltaR4_mvaCHToCB_nom'] = {
            'definition' : 'dijet_deltaR4_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['dijet_deltaR5_mvaCHToCB_nom'] = {
            'definition' : 'dijet_deltaR5_mvaCHToCB_nom',
            'type' : 'F'
          }
      
      variables['Hplus_b_deltaR0_mvaCHToCB_nom'] = {
          'definition' : 'Hplus_b_deltaR0_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['Hplus_b_deltaR1_mvaCHToCB_nom'] = {
          'definition' : 'Hplus_b_deltaR1_mvaCHToCB_nom',
          'type' : 'F'
        }
    
      if self.permute_leptonic_top_b:
        variables['Hplus_b_deltaR2_mvaCHToCB_nom'] = {
            'definition' : 'Hplus_b_deltaR2_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['Hplus_b_deltaR3_mvaCHToCB_nom'] = {
            'definition' : 'Hplus_b_deltaR3_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['Hplus_b_deltaR4_mvaCHToCB_nom'] = {
            'definition' : 'Hplus_b_deltaR4_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['Hplus_b_deltaR5_mvaCHToCB_nom'] = {
            'definition' : 'Hplus_b_deltaR5_mvaCHToCB_nom',
            'type' : 'F'
          }
      #variables['dijet_ptD0_mvaCHToCB'] = {
      #    'definition' : 'dijet_ptD0_mvaCHToCB',
      #    'type' : 'F'
      #  }
      #variables['dijet_ptD1_mvaCHToCB'] = {
      #    'definition' : 'dijet_ptD1_mvaCHToCB',
      #    'type' : 'F'
      #  }
    
      if self.include_leptonic_side:
        variables['lj_deltaR0_mvaCHToCB_nom'] = {
            'definition' : 'lj_deltaR0_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['lj_deltaR1_mvaCHToCB_nom'] = {
            'definition' : 'lj_deltaR1_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['lj_deltaR2_mvaCHToCB_nom'] = {
            'definition' : 'lj_deltaR2_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['lj_deltaR3_mvaCHToCB_nom'] = {
            'definition' : 'lj_deltaR3_mvaCHToCB_nom',
            'type' : 'F'
          }
      
      
      variables['bb_deltaR0_mvaCHToCB_nom'] = {
          'definition' : 'bb_deltaR0_mvaCHToCB_nom',
          'type' : 'F'
        }
      if self.permute_leptonic_top_b:
        variables['bb_deltaR1_mvaCHToCB_nom'] = {
            'definition' : 'bb_deltaR1_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['bb_deltaR2_mvaCHToCB_nom'] = {
            'definition' : 'bb_deltaR2_mvaCHToCB_nom',
            'type' : 'F'
          }
    elif self.isJetEtaPhi:
      variables['jet_eta0_mvaCHToCB_nom'] = {
          'definition' : 'jet_eta0_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['jet_eta1_mvaCHToCB_nom'] = {
          'definition' : 'jet_eta1_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['jet_eta2_mvaCHToCB_nom'] = {
          'definition' : 'jet_eta2_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['jet_phi0_mvaCHToCB_nom'] = {
          'definition' : 'jet_phi0_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['jet_phi1_mvaCHToCB_nom'] = {
          'definition' : 'jet_phi1_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['jet_phi2_mvaCHToCB_nom'] = {
          'definition' : 'jet_phi2_mvaCHToCB_nom',
          'type' : 'F'
        }
    else:
      #delta eta
      variables['dijet_deltaEta0_mvaCHToCB_nom'] = {
          'definition' : 'dijet_deltaEta0_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['dijet_deltaEta1_mvaCHToCB_nom'] = {
          'definition' : 'dijet_deltaEta1_mvaCHToCB_nom',
          'type' : 'F'
        }
      if self.permute_leptonic_top_b:
        variables['dijet_deltaEta2_mvaCHToCB_nom'] = {
            'definition' : 'dijet_deltaEta2_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['dijet_deltaEta3_mvaCHToCB_nom'] = {
            'definition' : 'dijet_deltaEta3_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['dijet_deltaEta4_mvaCHToCB_nom'] = {
            'definition' : 'dijet_deltaEta4_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['dijet_deltaEta5_mvaCHToCB_nom'] = {
            'definition' : 'dijet_deltaEta5_mvaCHToCB_nom',
            'type' : 'F'
          }
      
      variables['Hplus_b_deltaEta0_mvaCHToCB_nom'] = {
          'definition' : 'Hplus_b_deltaEta0_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['Hplus_b_deltaEta1_mvaCHToCB_nom'] = {
          'definition' : 'Hplus_b_deltaEta1_mvaCHToCB_nom',
          'type' : 'F'
        }
    
      if self.permute_leptonic_top_b:
        variables['Hplus_b_deltaEta2_mvaCHToCB_nom'] = {
            'definition' : 'Hplus_b_deltaEta2_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['Hplus_b_deltaEta3_mvaCHToCB_nom'] = {
            'definition' : 'Hplus_b_deltaEta3_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['Hplus_b_deltaEta4_mvaCHToCB_nom'] = {
            'definition' : 'Hplus_b_deltaEta4_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['Hplus_b_deltaEta5_mvaCHToCB_nom'] = {
            'definition' : 'Hplus_b_deltaEta5_mvaCHToCB_nom',
            'type' : 'F'
          }
      #variables['dijet_ptD0_mvaCHToCB'] = {
      #    'definition' : 'dijet_ptD0_mvaCHToCB',
      #    'type' : 'F'
      #  }
      #variables['dijet_ptD1_mvaCHToCB'] = {
      #    'definition' : 'dijet_ptD1_mvaCHToCB',
      #    'type' : 'F'
      #  }
      variables['lj_deltaEta0_mvaCHToCB_nom'] = {
          'definition' : 'lj_deltaEta0_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['lj_deltaEta1_mvaCHToCB_nom'] = {
          'definition' : 'lj_deltaEta1_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['lj_deltaEta2_mvaCHToCB_nom'] = {
          'definition' : 'lj_deltaEta2_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['lj_deltaEta3_mvaCHToCB_nom'] = {
          'definition' : 'lj_deltaEta3_mvaCHToCB_nom',
          'type' : 'F'
        }
      
      
      variables['bb_deltaEta0_mvaCHToCB_nom'] = {
          'definition' : 'bb_deltaEta0_mvaCHToCB_nom',
          'type' : 'F'
        }
      if self.permute_leptonic_top_b:
        variables['bb_deltaEta1_mvaCHToCB_nom'] = {
            'definition' : 'bb_deltaEta1_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['bb_deltaEta2_mvaCHToCB_nom'] = {
            'definition' : 'bb_deltaEta2_mvaCHToCB_nom',
            'type' : 'F'
          }
      #delta phi
      variables['dijet_deltaPhi0_mvaCHToCB_nom'] = {
          'definition' : 'dijet_deltaPhi0_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['dijet_deltaPhi1_mvaCHToCB_nom'] = {
          'definition' : 'dijet_deltaPhi1_mvaCHToCB_nom',
          'type' : 'F'
        }
      if self.permute_leptonic_top_b:
        variables['dijet_deltaPhi2_mvaCHToCB_nom'] = {
            'definition' : 'dijet_deltaPhi2_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['dijet_deltaPhi3_mvaCHToCB_nom'] = {
            'definition' : 'dijet_deltaPhi3_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['dijet_deltaPhi4_mvaCHToCB_nom'] = {
            'definition' : 'dijet_deltaPhi4_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['dijet_deltaPhi5_mvaCHToCB_nom'] = {
            'definition' : 'dijet_deltaPhi5_mvaCHToCB_nom',
            'type' : 'F'
          }
      
      variables['Hplus_b_deltaPhi0_mvaCHToCB_nom'] = {
          'definition' : 'Hplus_b_deltaPhi0_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['Hplus_b_deltaPhi1_mvaCHToCB_nom'] = {
          'definition' : 'Hplus_b_deltaPhi1_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['Hplus_b_deltaPhi2_mvaCHToCB_nom'] = {
          'definition' : 'Hplus_b_deltaPhi2_mvaCHToCB_nom',
          'type' : 'F'
        }
      if self.permute_leptonic_top_b:
        variables['Hplus_b_deltaPhi3_mvaCHToCB_nom'] = {
            'definition' : 'Hplus_b_deltaPhi3_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['Hplus_b_deltaPhi4_mvaCHToCB_nom'] = {
            'definition' : 'Hplus_b_deltaPhi4_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['Hplus_b_deltaPhi5_mvaCHToCB_nom'] = {
            'definition' : 'Hplus_b_deltaPhi5_mvaCHToCB_nom',
            'type' : 'F'
          }
      #variables['dijet_ptD0_mvaCHToCB'] = {
      #    'definition' : 'dijet_ptD0_mvaCHToCB',
      #    'type' : 'F'
      #  }
      #variables['dijet_ptD1_mvaCHToCB'] = {
      #    'definition' : 'dijet_ptD1_mvaCHToCB',
      #    'type' : 'F'
      #  }
      variables['lj_deltaPhi0_mvaCHToCB_nom'] = {
          'definition' : 'lj_deltaPhi0_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['lj_deltaPhi1_mvaCHToCB_nom'] = {
          'definition' : 'lj_deltaPhi1_mvaCHToCB_nom',
          'type' : 'F'
        }
      if self.permute_leptonic_top_b:
        variables['lj_deltaPhi2_mvaCHToCB_nom'] = {
            'definition' : 'lj_deltaPhi2_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['lj_deltaPhi3_mvaCHToCB_nom'] = {
            'definition' : 'lj_deltaPhi3_mvaCHToCB_nom',
            'type' : 'F'
          }
      
      
      variables['bb_deltaPhi0_mvaCHToCB_nom'] = {
          'definition' : 'bb_deltaPhi0_mvaCHToCB_nom',
          'type' : 'F'
        }
      if self.permute_leptonic_top_b:
        variables['bb_deltaPhi1_mvaCHToCB_nom'] = {
            'definition' : 'bb_deltaPhi1_mvaCHToCB_nom',
            'type' : 'F'
          }
        variables['bb_deltaPhi2_mvaCHToCB_nom'] = {
            'definition' : 'bb_deltaPhi2_mvaCHToCB_nom',
            'type' : 'F'
          }
    variables['min_deltaR_bb_event_mvaCHToCB_nom'] = {
        'definition' : 'min_deltaR_bb_event_mvaCHToCB_nom',
        'type' : 'F'
      }
    #variables['min_deltaR_jj_event_mvaCHToCB'] = { #minor
    #    'definition' : 'min_deltaR_jj_event_mvaCHToCB',
    #    'type' : 'F'
    #  }
    #variables['had_top_pt_scalar_sum_mvaCHToCB'] = { #minor
    #    'definition' : 'had_top_pt_scalar_sum_mvaCHToCB',
    #    'type' : 'F'
    #  }
    
    #variables['HT_btagged_L'] = {
    #    'definition' : 'HT_btagged_L',
    #    'type' : 'F'
    #  }
    #variables['HT_not_btagged_L'] = {
    #    'definition' : 'HT_not_btagged_L',
    #    'type' : 'F'
    #  }
    #variables['HT_btagged_M_nom'] = {
    #    'definition' : 'HT_btagged_M_nom',
    #    'type' : 'F'
    #  }
    #variables['HT_not_btagged_M_nom'] = {
    #    'definition' : 'HT_not_btagged_M_nom',
    #    'type' : 'F'
    #  }
    
    if self.include_pt:
      if self.include_leptonic_side:
        variables['Lepton_pt'] = {
                'definition' : 'lepton_pt := Lepton_pt[0]',
            'type' : 'F'
          }
        variables['MET_pt'] = {
                'definition' : 'MET := PuppiMET_pt',
            'type' : 'F'
          }
    
    if self.include_gamma:
      #"TMath::Sqrt(hadronic_top_M_nom*hadronic_top_M_nom+hadronic_top_pt_nom*hadronic_top_pt_nom)/hadronic_top_M_nom"
      variables['hadronic_top_gamma_mvaCHToCB_nom'] = {
          'definition' : 'hadronic_top_gamma_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['dijet_gamma0_mvaCHToCB_nom'] = {
          'definition' : 'dijet_gamma0_mvaCHToCB_nom',
          'type' : 'F'
        }
      variables['dijet_gamma1_mvaCHToCB_nom'] = {
          'definition' : 'dijet_gamma1_mvaCHToCB_nom',
          'type' : 'F'
        }
    #variables['hadronic_top_M_nom'] = {
    #    'definition' : 'hadronic_top_mass_mvaCHToCB_nom',
    #    'type' : 'F'
    #  }
    #variables['leptonic_top_M_nom'] = {
    #    'definition' : 'leptonic_top_M_nom',
    #    'type' : 'F'
    #  }
    #variables['leptonic_W_M_nom'] = {
    #    'definition' : 'leptonic_W_M_nom',
    #    'type' : 'F'
    #  }
    
    #variables['leptonic_top_M_nom'] = {
    #        'definition' : 'leptonic_top_M_nom',
    #    'type' : 'F'
    #  }
    #variables['chi2_nom'] = {      # no gain
    #        'definition' : 'chi2_nom',
    #    'type' : 'F'
    #  }
    #variables['HT_btagged_T'] = {
    #    'definition' : 'HT_btagged_T',
    #    'type' : 'F'
    #  }
    #variables['HT_not_btagged_T'] = {
    #    'definition' : 'HT_not_btagged_T',
    #    'type' : 'F'
    #  }
    #variables['mbb_mvaCHToCB'] = {
    #    'definition' : 'mbb_mvaCHToCB',
    #    'type' : 'F'
    #  }
    #variables['mcb0_mvaCHToCB'] = {
    #    'definition' : 'mcb0_mvaCHToCB',
    #    'type' : 'F'
    #  }
    #variables['mcb1_mvaCHToCB'] = {
    #    'definition' : 'mcb1_mvaCHToCB',
    #    'type' : 'F'
    #  }
    #variables['hadronic_top_mass_mvaCHToCB'] = {
    #    'definition' : 'hadronic_top_mass_mvaCHToCB',
    #    'type' : 'F'
    #  }
  
    return variables
