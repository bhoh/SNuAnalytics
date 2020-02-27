from collections import OrderedDict
plot=OrderedDict()




plot['DY']  = {
                  'nameHR' : 'DY',
                  'isSignal' : 0,
                  'color': 418, 
                  'isData'   : 0,
                  'samples'  : ['DY']
              }


plot['WW']  = {
                  'nameHR' : 'WW',
                  'isSignal' : 0,
                  'color': 618, 
                  'isData'   : 0,
                  'samples'  : ['WW']
              }


plot['QCD_MU']  = {
                  'nameHR' : 'QCD_MU',
                  'isSignal' : 0,
                  'color': 851,
                  'isData'   : 0,
   
                  'samples'  : ['QCD_MU']
              }


plot['QCD_EM']  = {
                  'nameHR' : 'QCD_EM',
                  'isSignal' : 0,
                  'color': 861,
                  'isData'   : 0,
    
                  'samples'  : ['QCD_EM']
              }

plot['QCD_bcToE']  = {
                  'nameHR' : 'QCD_bcToE',
                  'isSignal' : 0,
                  'color': 871,
                  'isData'   : 0,
   
                  'samples'  : ['QCD_bcToE']
              }


plot['top']  = {
                  'nameHR' : 'Top',
                  'isSignal' : 0,
                  'color': 400,   # kYellow
                  'isData'   : 0,                 
                  'samples'  : ['top']
              }





plot['Wjets']  = {
                  'nameHR' : 'Wjets',
                  'isSignal' : 0,
                  'color': 921,
                  'isData'   : 0,
                  'samples'  : ['Wjets'],
                  
              }



plot['DATA']  = {
                  'nameHR' : 'DATA',
                  'isSignal' : 0,
                  'color': 1, 
                  'isData'   : 1 ,
		  'isBlind'  : 0,
                  'samples'  : ['DATA']
              }

legend['lumi'] = 'L = 41.5/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
