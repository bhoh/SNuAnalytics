import sys
from collections import OrderedDict
plot=OrderedDict()


dict_TColor={
'green':416+3,##darker greeen
'cyan':432,##bright blue
'magenta':616,##violet
'yellow':400,
'blue':600,
'orange':800+7,##darker orange
'pink':900,
'black':1,
'red':632,
'azure':860,##blue
'gray':920,
}

scriptname=opt.plotFile


#groupPlot['QCD'] = {
#        'nameHR' : 'QCD',
#        'isSignal' : 0,
#        'color' :  dict_TColor['gray'],
#        'isData'   : 0,
#        'samples' : ['QCD_MU','QCD_EM','QCD_bcToE'],
#    }
groupPlot['TTV'] = {
        'nameHR' : 'TTV',
        'isSignal' : 0,
        'color' : dict_TColor['green'],
        'isData'   : 0,
        'samples' : ['TTWjets','TTZjets'],
    }
groupPlot['VV'] = {
        'nameHR' : 'VV',
        'isSignal' : 0,
        'color' : dict_TColor['cyan'],
        'isData'   : 0,
        'samples' : ['WW','WZ','ZZ'],
    }



groupPlot['V+jets'] = {
        'nameHR' : 'V+jets',
        'isSignal' : 0,
        'color' : dict_TColor['red'],
        'isData'   : 0,
        'samples' : ['DY','Wjets'],
    }

groupPlot['ST'] = {
        'nameHR' : 'ST',
        'isSignal' : 0,
        'color' : dict_TColor['pink'],
        'isData'   : 0,
        'samples' : ['ST'],
    }
groupPlot['TTLL'] = {
        'nameHR' : 'TTLL',
        'isSignal': 0,
        'color'   :  dict_TColor['magenta'],
        'isData'  : 0,
        'samples' : ['TTLL'],
    }

groupPlot['TTLJ+jj']  = {
                  'nameHR' : 'TTLJ+jj',
                  'isSignal' : 0,
                  'color': dict_TColor['orange'],
                  'isData'   : 0,                 
                  'samples'  : ['TTLJ+jj']
              }

groupPlot['TTLJ+cc']  = {
                  'nameHR' : 'TTLJ+cc',
                  'isSignal' : 0,
                  'color': dict_TColor['red']+4,
                  'isData'   : 0,                 
                  'samples'  : ['TTLJ+cc']
              }

groupPlot['TTLJ+bj']  = {
                  'nameHR' : 'TTLJ+bj',
                  'isSignal' : 0,
                  'color': dict_TColor['red']+1,
                  'isData'   : 0,                 
                  'samples'  : ['TTLJ+bj']
              }

groupPlot['TTLJ+bb']  = {
                  'nameHR' : 'TTLJ+bb',
                  'isSignal' : 0,
                  'color': dict_TColor['blue'],
                  'isData'   : 0,                 
                  'samples'  : ['TTLJ+bb']
              }



#if not 'ele' in scriptname:
#    plot['QCD_MU']  = {
#        'nameHR' : 'QCD_MU',
#        'isSignal' : 0,
#        'color': dict_TColor['gray'],
#        'isData'   : 0,
#        
#        'samples'  : ['QCD_MU']
#    }
#
#if not 'mu' in scriptname:
#    plot['QCD_EM']  = {
#        'nameHR' : 'QCD_EM',
#        'isSignal' : 0,
#        'color': dict_TColor['gray'],
#        'isData'   : 0,
#        'samples'  : ['QCD_EM']
#    }
#
#    plot['QCD_bcToE']  = {
#        'nameHR' : 'QCD_bcToE',
#        'isSignal' : 0,
#        'color': dict_TColor['gray']+1,
#        'isData'   : 0,
#        'samples'  : ['QCD_bcToE']
#    }
plot['WW']  = {
                  'nameHR' : 'WW',
                  'isSignal' : 0,
                  'color': dict_TColor['cyan'], 
                  'isData'   : 0,
                  'samples'  : ['WW']
              }

plot['WZ']  = {
                  'nameHR' : 'WZ',
                  'isSignal' : 0,
                  'color': dict_TColor['cyan'], 
                  'isData'   : 0,
                  'samples'  : ['WZ']
              }

plot['ZZ']  = {
                  'nameHR' : 'ZZ',
                  'isSignal' : 0,
                  'color': dict_TColor['cyan'], 
                  'isData'   : 0,
                  'samples'  : ['ZZ']
              }

plot['DY']  = {
                  'nameHR' : 'DY',
                  'isSignal' : 0,
                  'color': dict_TColor['red'], 
                  'isData'   : 0,
                  'samples'  : ['DY']
              }
plot['Wjets']  = {
                  'nameHR' : 'Wjets',
                  'isSignal' : 0,
                  'color': dict_TColor['red'], 
                  'isData'   : 0,
                  'samples'  : ['Wjets']
              }

plot['ST']  = {
                  'nameHR' : 'ST',
                  'isSignal' : 0,
                  'color': dict_TColor['pink'],
                  'isData'   : 0,                 
                  'samples'  : ['ST']
              }

plot['TTLL']  = {
                  'nameHR' : 'TTLL',
                  'isSignal' : 0,
                  'color': dict_TColor['magenta'],
                  'isData'   : 0,                 
                  'samples'  : ['TTLL']
              }

plot['TTLJ+jj']  = {
                  'nameHR' : 'TTLJ+jj',
                  'isSignal' : 0,
                  'color': dict_TColor['orange'],
                  'isData'   : 0,                 
                  'samples'  : ['TTLJ+jj']
              }

plot['TTLJ+cc']  = {
                  'nameHR' : 'TTLJ+cc',
                  'isSignal' : 0,
                  'color': dict_TColor['red']+4,
                  'isData'   : 0,                 
                  'samples'  : ['TTLJ+cc']
              }

plot['TTLJ+bj']  = {
                  'nameHR' : 'TTLJ+bj',
                  'isSignal' : 0,
                  'color': dict_TColor['red']+1,
                  'isData'   : 0,                 
                  'samples'  : ['TTLJ+bj']
              }

plot['TTLJ+bb']  = {
                  'nameHR' : 'TTLJ+bb',
                  'isSignal' : 0,
                  'color': dict_TColor['blue'],
                  'isData'   : 0,                 
                  'samples'  : ['TTLJ+bb']
              }

plot['TTWjets']  = {
                  'nameHR' : 'TTWjets',
                  'isSignal' : 0,
                  'color': dict_TColor['green'],
                  'isData'   : 0,                 
                  'samples'  : ['TTWjets']
              }
plot['TTZjets']  = {
                  'nameHR' : 'TTZjets',
                  'isSignal' : 0,
                  'color': dict_TColor['green'],
                  'isData'   : 0,                 
                  'samples'  : ['TTZjets']
              }

plot['DATA']  = {
                  'nameHR' : 'DATA',
                  'isSignal' : 0,
                  'color': 1, 
                  'isData'   : 1 ,
                  'isBlind'  : 0,
                  'samples'  : ['DATA']
              }


#import sys
#sys.path.insert(0, "MassPoints")
#from List_MX import *
#from List_MX_VBF import *
#
#
##for MX in List_MX:
#for MX in [900]:
#
#    plot['ggHWWlnuqq_M'+str(MX)]={
#        'nameHR':'ggHWWlnuqq_M'+str(MX),
#        #'scale' : 100,
#        'isData'   : 0,
#        'isSignal' : 1,
#        'color':dict_TColor['red'],
#        'samples' : ['ggHWWlnuqq_M'+str(MX)]
#    }
#    
##for MX in List_MX_VBF:
#for MX in [900]:
#    plot['vbfHWWlnuqq_M'+str(MX)]={
#        'nameHR':'vbfHWWlnuqq_M'+str(MX),
#        'isData'   : 0,
#        'isSignal' : 1,
#        #'scale' : 100,
#        'color':dict_TColor['blue'],
#        'samples' : ['ggHWWlnuqq_M'+str(MX)]
#    }

legend['lumi'] = 'L = 41.5/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
legend['extraText'] = 'work in progress'
