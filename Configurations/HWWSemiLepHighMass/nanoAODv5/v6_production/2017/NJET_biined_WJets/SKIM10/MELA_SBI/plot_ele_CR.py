UsePseudoData=True
print "UsePseudoData=",UsePseudoData
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

list_color=[]
for a in ['green','yellow','blue','red','gray','black']:
    print a
    list_color.append(dict_TColor[a])

scriptname=opt.plotFile

import sys
sys.path.insert(0, "MassPoints")
from List_MX import *
from List_MX_VBF import *

dict_scale={
140 : 6.41579864442 ,
200 : 4.41886412855 ,
400 : 5.5800917587 ,
700 : 5.44692468461 ,
900 : 5.74572106285 ,
2000 : 37.7288303073 ,    
}
#for MX in List_MX:
idx=0
for MX in [400,700,900,2000]:

    plot['ggHWWlnuqq_M'+str(MX)+'_B']={
        'nameHR':'ggHWWlnuqq_M'+str(MX),
        'scale' : dict_scale[MX],
        'isData'   : 0,
        'isSignal' : 1,
        'color': list_color[idx],
        'samples' : ['ggHWWlnuqq_M'+str(MX)+'_B']
    }
    idx+=1
    #for MX in List_MX_VBF:
for MX in [140,170,200,450,750,800,1000]:
    continue
    plot['vbfHWWlnuqq_M'+str(MX)+'_B']={
        'nameHR':'vbfHWWlnuqq_M'+str(MX),
        'isData'   : 0,
        'isSignal' : 1,
        #'scale' : 100,
        'color':dict_TColor['blue'],
        'samples' : ['vbfHWWlnuqq_M'+str(MX)+'_B']
    }

    

legend['lumi'] = 'L = 41.5/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
