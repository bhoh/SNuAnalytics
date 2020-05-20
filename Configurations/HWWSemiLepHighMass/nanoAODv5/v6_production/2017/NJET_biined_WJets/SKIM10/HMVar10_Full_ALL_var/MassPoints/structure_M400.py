#['WW', 'ggHWWlnuqq_M1500', 'DY', 'DATA', 'WZ', 'ggHWWlnuqq_M125', 'ZZZ', 'ggHWWlnuqq_M900', 'vbfHWWlnuqq_M500', 'Wjets1j', 'QCD_MU', 'WZZ', 'vbfHWWlnuqq_M900', 'QCD_bcToE', 'Wjets2j', 'QCD_EM', 'ggHWWlnuqq_M500', 'ZZ', 'WWW', 'vbfHWWlnuqq_M1500', 'vbfHWWlnuqq_M125', 'WWZ', 'Wjets0j', 'top']

QCD_MU=['QCD_Pt-15to20_MuEnrichedPt5',
        'QCD_Pt-20to30_MuEnrichedPt5',
        'QCD_Pt-30to50_MuEnrichedPt5',
        'QCD_Pt-50to80_MuEnrichedPt5',
        'QCD_Pt-80to120_MuEnrichedPt5',
        'QCD_Pt-120to170_MuEnrichedPt5',
        'QCD_Pt-170to300_MuEnrichedPt5',
        'QCD_Pt-300to470_MuEnrichedPt5',
        'QCD_Pt-470to600_MuEnrichedPt5',
        'QCD_Pt-600to800_MuEnrichedPt5',
        'QCD_Pt-800to1000_MuEnrichedPt5',
        'QCD_Pt-1000toInf_MuEnrichedPt5',
]
QCD_EM=[
  'QCD_Pt-20to30_EMEnriched',
  'QCD_Pt-30to50_EMEnriched',
  'QCD_Pt-50to80_EMEnriched',
  'QCD_Pt-80to120_EMEnriched',
  'QCD_Pt-120to170_EMEnriched',
  'QCD_Pt-170to300_EMEnriched',
  'QCD_Pt-300toInf_EMEnriched'
]
QCD_bcToE=[
  'QCD_Pt_20to30_bcToE',
  'QCD_Pt_30to80_bcToE',
  'QCD_Pt_80to170_bcToE',
  'QCD_Pt_170to250_bcToE',
  'QCD_Pt_250toInf_bcToE',
]

for name in [ 'DY', 'WZZ', 'WWZ','WWW','ZZZ', 'ZZ', 'WZ', 'WW', 'WpWmJJ_EWK_QCD_noHiggs', 'top', 'Wjets0j', 'Wjets1j', 'Wjets2j','vbfHWWlnuqq_M125','ggHWWlnuqq_M125'] + ['QCD_MU','QCD_EM','QCD_bcToE']:
    structure[name]  = {
        'isSignal' : 0,
        'isData'   : 0
    }

#ggHWWlnuqq_M400_S_B_I
structure['ggHWWlnuqq_M400'] = {
    'isSignal' : 1,
    'isData'   : 0
}


structure['vbfHWWlnuqq_M400'] = {
    'isSignal' : 1,
    'isData'   : 0
}


structure['PseudoData']  = {
                  'isSignal' : 0,
                  'isData'   : 1
              }
