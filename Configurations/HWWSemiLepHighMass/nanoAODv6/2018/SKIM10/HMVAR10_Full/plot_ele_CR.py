UsePseudoData=False
print "UsePseudoData->",UsePseudoData
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

plot['DY']  = {
                  'nameHR' : 'DY',
                  'isSignal' : 0,
                  'color': dict_TColor['red'], 
                  'isData'   : 0,
                  'samples'  : ['DY']
              }

plot['WZZ']  = {
                  'nameHR' : 'WZZ',
                  'isSignal' : 0,
                  'color': dict_TColor['azure'], 
                  'isData'   : 0,
                  'samples'  : ['WZZ']
              }

plot['WWZ']  = {
                  'nameHR' : 'WWZ',
                  'isSignal' : 0,
                  'color': dict_TColor['azure']+1, 
                  'isData'   : 0,
                  'samples'  : ['WWZ']
              }
plot['ZZ']  = {
                  'nameHR' : 'ZZ',
                  'isSignal' : 0,
                  'color': dict_TColor['azure']+2,
                  'isData'   : 0,
                  'samples'  : ['ZZ']
              }

plot['WZ']  = {
                  'nameHR' : 'WZ',
                  'isSignal' : 0,
                  'color': dict_TColor['azure']+3, 
                  'isData'   : 0,
                  'samples'  : ['WZ']
              }
plot['WW']  = {
                  'nameHR' : 'WW',
                  'isSignal' : 0,
                  'color': dict_TColor['cyan'], 
                  'isData'   : 0,
                  'samples'  : ['WW']
              }



if not 'ele' in scriptname:
    plot['QCD_MU']  = {
        'nameHR' : 'QCD_MU',
        'isSignal' : 0,
        'color': dict_TColor['gray'],
        'isData'   : 0,
        
        'samples'  : ['QCD_MU']
    }

if not 'mu' in scriptname:
    plot['QCD_EM']  = {
        'nameHR' : 'QCD_EM',
        'isSignal' : 0,
        'color': dict_TColor['gray'],
        'isData'   : 0,
        'samples'  : ['QCD_EM']
    }

    plot['QCD_bcToE']  = {
        'nameHR' : 'QCD_bcToE',
        'isSignal' : 0,
        'color': dict_TColor['gray']+1,
        'isData'   : 0,
        'samples'  : ['QCD_bcToE']
    }


plot['top']  = {
                  'nameHR' : 'Top',
                  'isSignal' : 0,
                  'color': dict_TColor['orange'],
                  'isData'   : 0,                 
                  'samples'  : ['top']
              }





plot['Wjets0j']  = {
                  'nameHR' : 'Wjets0j',
                  'isSignal' : 0,
                  'color': dict_TColor['green'],
                  'isData'   : 0,
                  'samples'  : ['Wjets0j'],
                  
              }
plot['Wjets1j']  = {
                  'nameHR' : 'Wjets1j',
                  'isSignal' : 0,
                  'color': dict_TColor['green']-3,
                  'isData'   : 0,
                  'samples'  : ['Wjets1j'],
                  
              }
plot['Wjets2j']  = {
                  'nameHR' : 'Wjets2j',
                  'isSignal' : 0,
                  'color': dict_TColor['green']+1,
                  'isData'   : 0,
                  'samples'  : ['Wjets2j'],
                  
              }


if UsePseudoData==True:
    plot['PseudoData']  = {
        'nameHR' : 'PseudoData',
        'isSignal' : 0,
        'color': 1,
        'isData'   : 1 ,
        'isBlind'  : 0,
        'samples'  : ['PseudoData']
    }
else:

    plot['DATA']  = {
        'nameHR' : 'DATA',
        'isSignal' : 0,
        'color': 1, 
        'isData'   : 1 ,
        'isBlind'  : 0,
        'samples'  : ['DATA']
    }


import sys
sys.path.insert(0, "MassPoints")
from List_MX import *
from List_MX_VBF import *

if 'SR' in scriptname:
    if not UsePseudoData : plot['DATA']['isBlind']=1

    #for MX in List_MX:
    for MX in []:

        plot['ggHWWlnuqq_M'+str(MX)]={
            'nameHR':'ggHWWlnuqq_M'+str(MX),
            #'scale' : 100,
            'isData'   : 0,
            'isSignal' : 1,
            'color':dict_TColor['red'],
            'samples' : ['ggHWWlnuqq_M'+str(MX)]
        }

    #for MX in List_MX_VBF:
    for MX in []:
        plot['vbfHWWlnuqq_M'+str(MX)]={
            'nameHR':'vbfHWWlnuqq_M'+str(MX),
            'isData'   : 0,
            'isSignal' : 1,
            #'scale' : 100,
            'color':dict_TColor['blue'],
            'samples' : ['ggHWWlnuqq_M'+str(MX)]
        }

legend['lumi'] = 'L = 58.8/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
