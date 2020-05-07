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


groupPlot['TTLJ']  = {
                  'nameHR' : 'TTLJ',
                  'isSignal' : 2,
                  'color': dict_TColor['orange'],
                  'isData'   : 0,                 
                  'samples'  : ['TTLJ+jj','TTLJ+cc','TTLJ+bb','TTLJ+bj']
              }

groupPlot['CHToCB_M130'] = {
        'nameHR' : '',
        'isSignal' : 0,
        'color' : 0,
        'isData'   : 0,
        'samples' : ['CHToCB_M130'],
    }

plot['TTLJ+jj']  = {
                  'nameHR' : 'TTLJ+jj',
                  'isSignal' : 2,
                  'color': dict_TColor['orange'],
                  'isData'   : 0,                 
                  'samples'  : ['TTLJ+jj']
              }

plot['TTLJ+cc']  = {
                  'nameHR' : 'TTLJ+cc',
                  'isSignal' : 2,
                  'color': dict_TColor['red']+4,
                  'isData'   : 0,                 
                  'samples'  : ['TTLJ+cc']
              }

plot['TTLJ+bj']  = {
                  'nameHR' : 'TTLJ+bj',
                  'isSignal' : 2,
                  'color': dict_TColor['red']+1,
                  'isData'   : 0,                 
                  'samples'  : ['TTLJ+bj']
              }

plot['TTLJ+bb']  = {
                  'nameHR' : 'TTLJ+bb',
                  'isSignal' : 2,
                  'color': dict_TColor['blue'],
                  'isData'   : 0,                 
                  'samples'  : ['TTLJ+bb']
              }

plot['CHToCB_M130'] = { #dummy
        'nameHR' : '',
        'isSignal' : 0,
        'color' : 0,
        'isData'   : 0,
        'samples' : ['CHToCB_M130'],
    }



legend['lumi'] = 'L = 35.9/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'
legend['extraText'] = 'Simulation  '
