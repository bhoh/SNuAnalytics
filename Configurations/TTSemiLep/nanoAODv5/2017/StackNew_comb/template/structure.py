structure['TTLJ'] = {
              'isSignal' : 0,
              'isData'   : 0
            }
structure['TTLL'] = {
              'isSignal' : 0,
              'isData'   : 0
            }
structure['ST'] = {
              'isSignal' : 0,
              'isData'   : 0
            }
structure['Wjets'] = {
              'isSignal' : 0,
              'isData'   : 0
            }
structure['DY'] = {
              'isSignal' : 0,
              'isData'   : 0
            }
structure['QCD_MU'] = {
              'isSignal' : 0,
              'isData'   : 0,
              'removeFromCuts' : [ k for k in cuts if 'eleCH' in k],
            }
structure['QCD_EM'] = {
              'isSignal' : 0,
              'isData'   : 0,
              'removeFromCuts' : [ k for k in cuts if 'muCH' in k],
            }
structure['QCD_bcToE'] = {
              'isSignal' : 0,
              'isData'   : 0,
              'removeFromCuts' : [ k for k in cuts if 'muCH' in k],
            }
structure['WW'] = {
              'isSignal' : 0,
              'isData'   : 0
            }
structure['WZ'] = {
              'isSignal' : 0,
              'isData'   : 0
            }
structure['ZZ'] = {
              'isSignal' : 0,
              'isData'   : 0
            }
structure['TTZjets'] = {
              'isSignal' : 0,
              'isData'   : 0
            }
structure['TTWjets'] = {
              'isSignal' : 0,
              'isData'   : 0
            }
structure['DATA'] = {
              'isSignal' : 0,
              'isData'   : 1
            }


# CHToCB signal
# isSignal: all signals not grid(1), alternative(2), signal grids(3)
for mass in ['075','080','085','090','100','110','120','130','140','150']:
    sample_name = 'CHToCB_M{0}'.format(mass) 
    structure[sample_name] = {
                  'isSignal' : 2,
                  'isData'   : 0
                }

#structure['CHToCB_M<MASS>'] = {
#              'isSignal' : 1,
#              'isData'   : 0
#            }

