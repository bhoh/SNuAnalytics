structure['TT'] = {
              'isSignal' : 0,
              'isData'   : 0
            }
structure['nonTT'] = {
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

