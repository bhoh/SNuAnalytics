
plot['Wjets']  = {
                  'nameHR' : 'Wjets',
                  'isSignal' : 0,
                  'color': 921,
                  'isData'   : 0,
                  'samples'  : ['Wjets'],
                  
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
plot['QCD_pt170to300']  = {
                  'nameHR' : 'QCD_pt170to300',
                  'isSignal' : 0,
                  'color': 951,
                  'isData'   : 0,
'scale':0.1,
                  'samples'  : ['QCD_pt170to300']
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


'''
plot['DY']  = {
                  'nameHR' : 'DY',
                  'isSignal' : 0,
                  'color': 418, 
                  'isData'   : 0,
                  'samples'  : ['DY']
              }

'''
plot['WW']  = {
                  'nameHR' : 'WW',
                  'isSignal' : 0,
                  'color': 618, 
                  'isData'   : 0,
                  'samples'  : ['DY']
              }




plot['DATA']  = {
                  'nameHR' : 'DATA',
                  'isSignal' : 0,
                  'color': 1, 
                  'isData'   : 1 ,
		  'isBlind'  : 1,
                  'samples'  : ['DATA']
              }

legend['lumi'] = 'L = 41.5/fb'
#legend['lumi'] = 'Simulation'
legend['sqrt'] = '#sqrt{s} = 13 TeV'

#List_MX=[200,210,250,300,350,400,500,550,600,650,700,750,800,900,1500,2000,2500,3000,4000,5000]
plot['ggHWWlnuqq_M__THIS_MASS__']  = {
    'nameHR' : 'ggHWWlnuqq_M__THIS_MASS__',
    'isSignal' : 1,
    'isData'   : 0,
    'color': 632,
    'samples'  : ['ggHWWlnuqq_M__THIS_MASS__'],
    'scale'    : __THIS_SCALE__
}    

