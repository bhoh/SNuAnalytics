structure['TT+jj'] = {
              'isSignal' : 0,
              'isData'   : 0
            }
structure['TT+bb'] = {
              'isSignal' : 0,
              'isData'   : 0
            }
structure['TT+bj'] = {
              'isSignal' : 0,
              'isData'   : 0
            }
structure['TT+cc'] = {
              'isSignal' : 0,
              'isData'   : 0
            }

structure['Others'] = {
              'isSignal' : 0,
              'isData'   : 0
            }
structure['QCD'] = {
              'isSignal' : 0,
              'isData'   : 0,
               # exclue MC QCD from 1l 3b, 2l ee, em, me.
              #'removeFromCuts' : ['sng_4j_eleCH_3b','sng_4j_muCH_3b','dbl_4j_ee','dbl_4j_ee_onZ','dbl_4j_em','dbl_4j_me']
              'removeFromCuts' : ['dbl_4j_ee','dbl_4j_ee_onZ','dbl_4j_em','dbl_4j_me']
            }
#structure['TTLJ+jj'] = {
#              'isSignal' : 0,
#              'isData'   : 0
#            }
#structure['TTLJ+bj'] = {
#              'isSignal' : 0,
#              'isData'   : 0
#            }
#structure['TTLJ+bb'] = {
#              'isSignal' : 0,
#              'isData'   : 0
#            }
#structure['TTLJ+cc'] = {
#              'isSignal' : 0,
#              'isData'   : 0
#            }
#structure['TTLL'] = {
#              'isSignal' : 0,
#              'isData'   : 0
#            }
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
              'isSignal' : 0,
              'isData'   : 1
            }


# CHToCB signal
# isSignal: all signals not grid(1), alternative(2), signal grids(3)
for mass in ['075','080','085','090','100','110','120','130','140','150', '160']:
    sample_name = 'CHToCB_M{0}'.format(mass) 
    structure[sample_name] = {
                  'isSignal' : 2,
                  'isData'   : 0
                }


