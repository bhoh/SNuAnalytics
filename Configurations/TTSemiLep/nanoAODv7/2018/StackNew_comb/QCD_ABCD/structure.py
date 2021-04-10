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



structure['nonTT'] = {
              'isSignal' : 0,
              'isData'   : 0
            }
structure['QCD'] = {
              'isSignal' : 0,
              'isData'   : 0
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
for mass in ['080']:
    sample_name = 'CHToCB_M{0}'.format(mass) 
    structure[sample_name] = {
                  'isSignal' : 1,
                  'isData'   : 0
                }


