

plot['DY']  = {
                  'nameHR' : 'DY',
                  'isSignal' : 0,
                  'color': 418, 
                  'isData'   : 0,
                  'samples'  : ['DY']
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
                  
                  'samples'  : ['Wjets']
              }

plot['QCD_MU']  = {
                  'nameHR' : 'QCD_MU',
                  'isSignal' : 0,
                  'color': 857,
                  'isData'   : 0,
                  'samples'  : ['QCD_MU']
              }

plot['QCD_EM']  = {
                  'nameHR' : 'QCD_EM',
                  'isSignal' : 0,
                  'color': 957,
                  'isData'   : 0,
                  'samples'  : ['QCD_EM']
              }


plot['ggHWWlnuqq_M__THIS_MASS__']  = {
                  'nameHR' : 'ggHWWlnuqq_M__THIS_MASS__ x __THIS_SCALE__',
                  'isSignal' : 1,
                  'isData'   : 0,
                  'color': 632,   
                  'samples'  : ['ggHWWlnuqq_M__THIS_MASS__'],
                  'scale'    : __THIS_SCALE__
}

plot['DATA']  = {
                  'nameHR' : 'DATA',
                  'isSignal' : 0,
                  'color': 1, 
                  'isData'   : 1 ,
		  'isBlind'  : 1,
                  'samples'  : ['DATA']
              }
legend['lumi'] = 'L = 59.7/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
