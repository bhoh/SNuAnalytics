removeFromCuts=[
  'sng_4j_eleORmuCH_2b','sng_4j_eleORmuCH_3b',
  'dbl_2j_eeORmmORemORme_2b','dbl_2j_eeORmmORemORme_3b','dbl_2j_eeORmmORemORme_2b_onZ','dbl_2j_eeORmmORemORme_3b_onZ',
  'dbl_2j_ee_2b','dbl_2j_em_2b','dbl_2j_me_2b','dbl_2j_mm_2b','dbl_2j_ee_2b_onZ','dbl_2j_mm_2b_onZ',
  'dbl_2j_ee_3b','dbl_2j_em_3b','dbl_2j_me_3b','dbl_2j_mm_3b','dbl_2j_ee_3b_onZ','dbl_2j_mm_3b_onZ',
  'dbl_2j_ee_2b_onZ', 'dbl_2j_ee_3b_onZ', 'dbl_2j_mm_2b_onZ', 'dbl_2j_mm_3b_onZ', 'dbl_4j_ee_onZ', 'dbl_4j_eeORmmORemORme_onZ', 'dbl_4j_mm_onZ',
        ]

splitTTLL = False

if not splitTTLL:
  structure['TT+jj'] = {
                'removeFromCuts' : removeFromCuts,
                'isSignal' : 0,
                'isData'   : 0
              }
  structure['TT+bb'] = {
                'removeFromCuts' : removeFromCuts,
                'isSignal' : 0,
                'isData'   : 0
              }
  #structure['TT+bj'] = {
  #              'removeFromCuts' : removeFromCuts,
  #              'isSignal' : 0,
  #              'isData'   : 0
  #            }
  structure['TT+cc'] = {
                'removeFromCuts' : removeFromCuts,
                'isSignal' : 0,
                'isData'   : 0
              }
else:
  structure['TTLJ+jj'] = {
                'isSignal' : 0,
                'isData'   : 0
              }
  #structure['TTLJ+bj'] = {
  #              'isSignal' : 0,
  #              'isData'   : 0
  #            }
  structure['TTLJ+bb'] = {
                'isSignal' : 0,
                'isData'   : 0
              }
  structure['TTLJ+cc'] = {
                'isSignal' : 0,
                'isData'   : 0
              }

  structure['TTLL+jj'] = {
                'isSignal' : 0,
                'isData'   : 0
              }
  #structure['TTLL+bj'] = {
  #              'isSignal' : 0,
  #              'isData'   : 0
  #            }
  structure['TTLL+bb'] = {
                'isSignal' : 0,
                'isData'   : 0
              }
  structure['TTLL+cc'] = {
                'isSignal' : 0,
                'isData'   : 0
              }

structure['Others'] = {
              'removeFromCuts' : removeFromCuts,
              'isSignal' : 0,
              'isData'   : 0
            }
structure['ST'] = {
              'removeFromCuts' : removeFromCuts,
              'isSignal' : 0,
              'isData'   : 0
            }
structure['QCD'] = {
              'removeFromCuts' : removeFromCuts +['dbl_4j_ee','dbl_4j_ee_onZ','dbl_4j_em','dbl_4j_me'],
              'isSignal' : 0,
              'isData'   : 0,
               # exclue MC QCD from 1l 3b, 2l ee, em, me.
            }
#structure['ST'] = {
#              'isSignal' : 0,
#              'isData'   : 0
#            }
#structure['DY'] = {
#              'isSignal' : 0,
#              'isData'   : 0
#            }
#structure['Wjets'] = {
#              'isSignal' : 0,
#              'isData'   : 0
#            }
#structure['WW'] = {
#              'isSignal' : 0,
#              'isData'   : 0
#            }
#structure['WZ'] = {
#              'isSignal' : 0,
#              'isData'   : 0
#            }
#structure['ZZ'] = {
#              'isSignal' : 0,
#              'isData'   : 0
#            }
#structure['TTWjets'] = {
#              'isSignal' : 0,
#              'isData'   : 0
#            }
#structure['TTZjets'] = {
#              'isSignal' : 0,
#              'isData'   : 0
#            }
#structure['QCD_MU'] = {
#              'isSignal' : 0,
#              'isData'   : 0,
#              'removeFromCuts' : ['eleCH__Top4j2b__noHEMveto___','eleCH__Top4j3b__noHEMveto___'],
#            }
#structure['QCD_EM'] = {
#              'isSignal' : 0,
#              'isData'   : 0,
#              'removeFromCuts' : ['muCH__Top4j2b__noHEMveto___','muCH__Top4j3b__noHEMveto___'],
#            }
#structure['QCD_bcToE'] = {
#              'isSignal' : 0,
#              'isData'   : 0,
#              'removeFromCuts' : ['muCH__Top4j2b__noHEMveto___','muCH__Top4j3b__noHEMveto___'],
#            }
structure['DATA'] = {
              'removeFromCuts' : removeFromCuts,
              'isSignal' : 0,
              'isData'   : 1
            }


# CHToCB signal
# isSignal: all signals not grid(1), alternative(2), signal grids(3)
for mass in ['075','080','085','090','100','110','120','130','140','150', '160']:
    sample_name = 'CHToCB_M{0}'.format(mass) 
    structure[sample_name] = {
                  'removeFromCuts' : removeFromCuts,
                  'isSignal' : 2,
                  'isData'   : 0
                }

structure['CHToCB_M080_yield'] = {
              'removeFromCuts' : removeFromCuts,
              'rescaleTo': 'CHToCB_M080',
              'isSignal' : 2,
              'isData'   : 0
            }

