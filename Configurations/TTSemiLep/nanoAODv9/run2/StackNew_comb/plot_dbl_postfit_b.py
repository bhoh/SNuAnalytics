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

splitTTLL = False

groupPlot['Others'] = {
        'nameHR' : 'Others',
        'isSignal' : 0,
        'color' :  dict_TColor['cyan'],
        'isData'   : 0,
        'samples' : ['Others'],
        #'samples' : ['TTWjets','TTZjets','WW','WZ','ZZ','Wjets','ST'],
    }

groupPlot['ST'] = {
        'nameHR' : 'ST',
        'isSignal' : 0,
        'color' :  dict_TColor['green']-1,
        'isData'   : 0,
        'samples' : ['ST'],
    }




if not splitTTLL:
  groupPlot['TT+jj']  = {
                    'nameHR' : 'TT+light',
                    'isSignal' : 0,
                    'color': dict_TColor['orange'],
                    'isData'   : 0,                 
                    'samples'  : ['TT+jj']
                }
  
  groupPlot['TT+cc']  = {
                    'nameHR' : 'TT+#geq1c',
                    'isSignal' : 0,
                    'color': dict_TColor['red']-5,
                    'isData'   : 0,                 
                    'samples'  : ['TT+cc']
                }
  
  # merge TT+bj to TT+bb : its xsec scale is highly correlated
  groupPlot['TT+bb']  = { 
                    'nameHR' : 'TT+#geq1b',
                    'isSignal' : 0,
                    'color': dict_TColor['blue'],
                    'isData'   : 0,                 
                    'samples'  : ['TT+bb']
                }
else:
  groupPlot['TTLJ+jj']  = {
                    'nameHR' : 'TTLJ+jj',
                    'isSignal' : 0,
                    'color': dict_TColor['orange'],
                    'isData'   : 0,                 
                    'samples'  : ['TTLJ_jj',]
                }
  
  groupPlot['TTLJ+cc']  = {
                    'nameHR' : 'TTLJ+cc',
                    'isSignal' : 0,
                    'color': dict_TColor['red']+4,
                    'isData'   : 0,                 
                    'samples'  : ['TTLJ_cc',]
                }
  
  # merge TT+bj to TT+bb : its xsec scale is highly correlated
  groupPlot['TTLJ+bb']  = { 
                    'nameHR' : 'TTLJ+bb',
                    'isSignal' : 0,
                    'color': dict_TColor['blue'],
                    'isData'   : 0,                 
                    'samples'  : ['TTLJ_bb','TTLJ_bj']
                }
  groupPlot['TTLL+jj']  = {
                    'nameHR' : 'TTLL+jj',
                    'isSignal' : 0,
                    'color': dict_TColor['orange'],
                    'isData'   : 0,                 
                    'samples'  : ['TTLL_jj',]
                }
  
  groupPlot['TTLL+cc']  = {
                    'nameHR' : 'TTLL+cc',
                    'isSignal' : 0,
                    'color': dict_TColor['red']+4,
                    'isData'   : 0,                 
                    'samples'  : ['TTLL_cc',]
                }
  
  # merge TT+bj to TT+bb : its xsec scale is highly correlated
  groupPlot['TTLL+bb']  = { 
                    'nameHR' : 'TTLL+bb',
                    'isSignal' : 0,
                    'color': dict_TColor['blue'],
                    'isData'   : 0,                 
                    'samples'  : ['TTLL_bb','TTLL_bj']
                }

#groupPlot['TT+bb']  = {
#                  'nameHR' : 'TT+bb',
#                  'isSignal' : 0,
#                  'color': dict_TColor['blue'],
#                  'isData'   : 0,                 
#                  'samples'  : ['TTLJ_bb','TTLL_bb']
#              }
#groupPlot['TT+bj']  = {
#                  'nameHR' : 'TT+bj',
#                  'isSignal' : 0,
#                  'color': dict_TColor['blue'],
#                  'isData'   : 0,                 
#                  'samples'  : ['TTLJ_bj','TTLL_bj']
#              }





plot['ST']  = {
                  'nameHR' : 'ST',
                  'isSignal' : 0,
                  'color': dict_TColor['green'],
                  'isData'   : 0,                 
                  'samples'  : ['ST']
              }

plot['TT+jj']  = {
                  'nameHR' : 'TT+light',
                  'isSignal' : 0,
                  'color': dict_TColor['magenta'],
                  'isData'   : 0,                 
                  'samples'  : ['TT+jj']
              }

plot['TT+bb']  = {
                  'nameHR' : 'TT+#geq1b',
                  'isSignal' : 0,
                  'color': dict_TColor['magenta'],
                  'isData'   : 0,                 
                  'samples'  : ['TT+bb']
              }

plot['TT+cc']  = {
                  'nameHR' : 'TT+#geq1c',
                  'isSignal' : 0,
                  'color': dict_TColor['magenta'],
                  'isData'   : 0,                 
                  'samples'  : ['TT+cc']
              }

plot['Others']  = {
                  'nameHR' : 'Others',
                  'isSignal' : 0,
                  'color': dict_TColor['cyan'],
                  'isData'   : 0,                 
                  'samples'  : ['Others']
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

if "2018"         in opt.pycfg:
  legend['lumi'] = 'L = 59.83/fb'
elif "2017"       in opt.pycfg:
  legend['lumi'] = 'L = 41.48/fb'
elif "2016noHIPM" in opt.pycfg:
  legend['lumi'] = 'L = 16.8/fb'
elif "2016HIPM"   in opt.pycfg:
  legend['lumi'] = 'L = 19.5/fb'
elif "run2"   in opt.pycfg:
  legend['lumi'] = 'L = 137.65/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
legend['extraText'] = 'work in progress'
