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


for mass, color in [('090','green'),('120','red'),('150','blue')]:
    sample_name = 'CHToCB_M{0}'.format(mass) 
    groupPlot[sample_name]={
        'nameHR':'M{0}(BR=0.01)'.format(mass),
        'scale' : 2*(0.01)*(1-0.01),
        'isData'   : 0,
        'isSignal' : 2,
        'color':dict_TColor[color],
        'samples' : [sample_name]
    }

groupPlot['CHToCB_M130'] = {
        'nameHR' : '',
        'isSignal' : 0,
        'color' : 0,
        'isData'   : 0,
        'samples' : ['CHToCB_M130'],
    }


for mass, color in [('090','green'),('120','red'),('150','blue')]:
    sample_name = 'CHToCB_M{0}'.format(mass) 
    plot[sample_name]={
        'nameHR':'M{0}(BR=0.01)'.format(mass),
        'scale' : 2*(0.01)*(1-0.01),
        'isData'   : 0,
        'isSignal' : 2,
        'color':dict_TColor[color],
        'samples' : [sample_name]
    }


plot['CHToCB_M130'] = {
        'nameHR' : '',
        'isSignal' : 0,
        'scale' : 2*(0.01)*(1-0.01)*1.4,
        'color' : 0,
        'isData'   : 0,
        'samples' : ['CHToCB_M130'],
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
#        'isSignal' : 2,
#        'color':dict_TColor['red'],
#        'samples' : ['ggHWWlnuqq_M'+str(MX)]
#    }
#    
##for MX in List_MX_VBF:
#for MX in [900]:
#    plot['vbfHWWlnuqq_M'+str(MX)]={
#        'nameHR':'vbfHWWlnuqq_M'+str(MX),
#        'isData'   : 0,
#        'isSignal' : 2,
#        #'scale' : 100,
#        'color':dict_TColor['blue'],
#        'samples' : ['ggHWWlnuqq_M'+str(MX)]
#    }

legend['lumi'] = 'L = 41.5/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
legend['extraText'] = 'Simulation  '
