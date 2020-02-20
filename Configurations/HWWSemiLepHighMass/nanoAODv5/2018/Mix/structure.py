structure['DY']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['Wjets']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['top'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['WW']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }
structure['QCD_MU'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['QCD_EM'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

#QCD_bcToE
structure['QCD_bcToE'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }


List_MX=[125,200,210,250,300,350,400,500,550,600,650,700,750,800,900,1500,2000,2500,3000,4000,5000]

for MX in List_MX:

    structure['ggHWWlnuqq_M'+str(MX)] = {
        'isSignal' : 1,
        'isData'   : 0
    }
'''
List_MX_VBF=[200,210,250,270,300,350,400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000,5000]

for MX in List_MX_VBF:
    structure['VBFHToWWToLNuQQ_M'+str(MX)] = {
        'isSignal' : 1,
        'isData'   : 0,
    }

'''
structure['DATA']  = {
                  'isSignal' : 0,
                  'isData'   : 1
              }
