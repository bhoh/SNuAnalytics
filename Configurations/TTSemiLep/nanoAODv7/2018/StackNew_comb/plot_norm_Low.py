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


groupQCD = []
if not 'ele' in scriptname:
  groupQCD.extend(['QCD_MU'])
if not 'mu' in scriptname:
  groupQCD.extend(['QCD_EM','QCD_bcToE'])


groupPlot['Bkgs'] = {
        'nameHR' : 'All Bkgs',
        'isSignal' : 0,
        'color' :  dict_TColor['black'],
        'isData'   : 0,
        'samples' : ['TTWjets','TTZjets','WW','WZ','ZZ','Wjets','ST','DY','QCD_MU','QCD_EM','QCD_bcToE','TTLJ_jj','TTLL_jj','TTLJ_cc','TTLL_cc','TTLJ_bb','TTLL_bb','TTLJ_bj','TTLL_bj'],
    }



#for mass in ['075','080','085','090','100','110','120','130','140','150', '160']:
for mass, color in [('075','green'),('090','red'),('120','blue')]:
    sample_name = 'CHToCB_M{0}'.format(mass) 
    groupPlot[sample_name]={
        'nameHR':'M{0}'.format(mass),
        'scale' : 2*(0.01)*(1-0.01)*364.35,
        'isData'   : 0,
        'isSignal' : 1,
        #'color':dict_TColor['red'],
        'color':dict_TColor[color],
        'samples' : [sample_name]
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

plot['TTLL_jj']  = {
                  'nameHR' : 'TTLL+jj',
                  'isSignal' : 0,
                  'color': dict_TColor['magenta'],
                  'isData'   : 0,                 
                  'samples'  : ['TTLL_jj']
              }

plot['TTLL_bb']  = {
                  'nameHR' : 'TTLL+bb',
                  'isSignal' : 0,
                  'color': dict_TColor['magenta'],
                  'isData'   : 0,                 
                  'samples'  : ['TTLL_bb']
              }

plot['TTLL_bj']  = {
                  'nameHR' : 'TTLL+bj',
                  'isSignal' : 0,
                  'color': dict_TColor['magenta'],
                  'isData'   : 0,                 
                  'samples'  : ['TTLL_bj']
              }

plot['TTLL_cc']  = {
                  'nameHR' : 'TTLL+cc',
                  'isSignal' : 0,
                  'color': dict_TColor['magenta'],
                  'isData'   : 0,                 
                  'samples'  : ['TTLL_cc']
              }
plot['TTLJ_jj']  = {
                  'nameHR' : 'TTLJ+jj',
                  'isSignal' : 0,
                  'color': dict_TColor['orange'],
                  'isData'   : 0,                 
                  'samples'  : ['TTLJ_jj']
              }

plot['TTLJ_cc']  = {
                  'nameHR' : 'TTLJ+cc',
                  'isSignal' : 0,
                  'color': dict_TColor['red']+4,
                  'isData'   : 0,                 
                  'samples'  : ['TTLJ_cc']
              }

plot['TTLJ_bj']  = {
                  'nameHR' : 'TTLJ+bj',
                  'isSignal' : 0,
                  'color': dict_TColor['red']+1,
                  'isData'   : 0,                 
                  'samples'  : ['TTLJ_bj']
              }

plot['TTLJ_bb']  = {
                  'nameHR' : 'TTLJ+bb',
                  'isSignal' : 0,
                  'color': dict_TColor['blue'],
                  'isData'   : 0,                 
                  'samples'  : ['TTLJ_bb']
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


#plot['DATA']  = {
#                  'nameHR' : 'DATA',
#                  'isSignal' : 0,
#                  'color': 1, 
#                  'isData'   : 1 ,
#		  'isBlind'  : 0,
#                  'samples'  : ['DATA']
#              }
for mass in ['075','080','085','090','100','110','120','130','140','150', '160']:
    sample_name = 'CHToCB_M{0}'.format(mass) 
    plot[sample_name]={
        'nameHR':'M{0}(BR=0.01)'.format(mass),
        'scale' : 2*(0.01)*(1-0.01)*364.35,
        'isData'   : 0,
        'isSignal' : 1,
        'color':dict_TColor['red'],
        'samples' : [sample_name]
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

legend['lumi'] = 'L = 59.74/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
legend['extraText'] = 'work in progress'
