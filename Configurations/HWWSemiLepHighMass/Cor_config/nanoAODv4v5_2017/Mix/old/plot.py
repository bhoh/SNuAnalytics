
plot['Wjets']  = {
                  'nameHR' : 'Wjets',
                  'isSignal' : 0,
                  'color': 921,
                  'isData'   : 0,
                  'samples'  : ['Wjets'],
                  'scale'    : 0.915, 
              }

plot['top']  = {
                  'nameHR' : 'Top',
                  'isSignal' : 0,
                  'color': 400,   # kYellow
                  'isData'   : 0,                 
                  'samples'  : ['top']
              }



plot['QCD_MU']  = {
                  'nameHR' : 'QCD_MU',
                  'isSignal' : 0,
                  'color': 851,
                  'isData'   : 0,
   
                  'samples'  : ['QCD_MU']
              }

#QCD_MU_170to300
'''
plot['QCD_MU_170to300']  = {
                  'nameHR' : 'QCD_MU_170to300',
                  'isSignal' : 0,
                  'color': 951,
                  'isData'   : 0,
    'scale':0.0598,
                  'samples'  : ['QCD_MU_170to300']
              }
'''
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



plot['DY']  = {
                  'nameHR' : 'DY',
                  'isSignal' : 0,
                  'color': 418, 
                  'isData'   : 0,
                  'samples'  : ['DY']
              }





#plot['ggHWWlnuqq_M700']  = {
#                  'nameHR' : 'ggHWWlnuqq_M700',
#                  'isSignal' : 1,
#                  'isData'   : 0,
#                  'color': 632,   
#                  'samples'  : ['ggHWWlnuqq_M700'],
#                  'scale'    : 30
#}
#
'''
plot['ggHWWlnuqq_M900']  = {
                  'nameHR' : 'ggHWWlnuqq_M900',
                  'isSignal' : 1,
                  'isData'   : 0,
                  'color': 632,   
                  'samples'  : ['ggHWWlnuqq_M900'],
                  'scale'    : 120
}
'''
'''
plot['ggHWWlnuqq_M2500']  = {
                  'nameHR' : 'ggHWWlnuqq_M2500',
                  'isSignal' : 1,
                  'isData'   : 0,
                  'color': 600,   
                  'samples'  : ['ggHWWlnuqq_M2500'],
                  'scale'    : 3000
}

plot['ggHWWlnuqq_M5000']  = {
                  'nameHR' : 'ggHWWlnuqq_M5000',
                  'isSignal' : 1,
                  'isData'   : 0,
                  'color': 616,   
                  'samples'  : ['ggHWWlnuqq_M5000'],
                  'scale'    : 3000
}
'''


plot['DATA']  = {
                  'nameHR' : 'DATA',
                  'isSignal' : 0,
                  'color': 1, 
                  'isData'   : 1 ,
		  'isBlind'  : 0,
                  'samples'  : ['DATA']
              }

legend['lumi'] = 'L = 41.5/fb'
#legend['lumi'] = 'Simulation'
legend['sqrt'] = '#sqrt{s} = 13 TeV'
