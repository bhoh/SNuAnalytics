UsePseudoData=False
print "UsePseudoData=",UsePseudoData
print "CombineWjets=",CombineWjets
import sys
sys.path.append(os.getcwd())
#-----Variable Deinition-----#
from WPandCut2016 import *
import sys
from collections import OrderedDict
plot=OrderedDict()

TOPS = [skey for skey in samples if ('TT' in skey or 'ST' in skey or 'top' in skey)]



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

###--DY
groupPlot['Others']  = {
    'nameHR' : 'Others',
    'isSignal' : 0,
    'color': dict_TColor['yellow'], 
    'isData'   : 0,
    #'samples' : ['DY']
}


plot['DY']  = {
                  'nameHR' : 'DY',
                  'isSignal' : 0,
                  'color': dict_TColor['yellow'], 
                  'isData'   : 0,
              }

if CombineHTT:
    groupPlot['Others']['samples']=['DY','HTT']
else:
    groupPlot['Others']['samples']=['DY']+HTT
    for htt in HTT:
        plot[htt]  = {
                  'nameHR' : htt,
                  'isSignal' : 0,
                  'color': dict_TColor['yellow'],
                  'isData'   : 0,
              }

###--QCD
groupPlot['QCD']  = {
    'nameHR' : 'QCD',
    'isSignal' : 0,
    'color': dict_TColor['gray'],
    'isData'   : 0,
    'samples'  : []
}



if DIVIDEQCD:
    groupPlot['QCD']['samples']=QCD_EM+QCD_MU+QCD_bcToE
    for s in QCD_EM+QCD_MU+QCD_bcToE:
        plot[s]  = {
            'nameHR' : s,
            'isSignal' : 0,
            'color': dict_TColor['gray'],
            'isData'   : 0,
        }
else:
    groupPlot['QCD']['samples']=['QCD']
    plot['QCD']  = {
        'nameHR' : 'QCD',
        'isSignal' : 0,
        'color': dict_TColor['gray'],
        'isData'   : 0,
    }


##--MultiV
groupPlot['MultiV']={
    'nameHR' : 'Multi V',
    'isSignal' : 0,
    'color': dict_TColor['azure'],
    'isData'   : 0,
    'samples'  : MultiV+ggWW+qqWWqq
    
}
if CombineMultiV:
    groupPlot['MultiV']['samples']=['MultiV']
    plot['MultiV']={
        'nameHR' : s,
        'isSignal' : 0,
        'color': dict_TColor['cyan']+idx,
        'isData'   : 0,
        
    }
else:
    total=len(MultiV)
    idx=-1*int(total/2)
    for s in MultiV+ggWW+qqWWqq:
        plot[s]={
            'nameHR' : s,
            'isSignal' : 0,
            'color': dict_TColor['cyan']+idx,
            'isData'   : 0,

        }
        idx+=1


##---H125
groupPlot['h125']={
    'nameHR' : 'h125',
    'isSignal' : 0,
    'color': dict_TColor['magenta'],
    'isData'   : 0,
    'samples'  : H125

}
if CombineH125:
    groupPlot['h125']['samples']=['h125']
    plot['h125']  = {
        'nameHR' : 'h125',
        'isSignal' : 0,
        'color': dict_TColor['pink'],
        'isData'   : 0,
    }

else:
    total=len(H125)
    idx=-1*int(total/2)
    for s in H125:
        plot[s]={
            'nameHR' : s,
            'isSignal' : 0,
            'color': dict_TColor['pink']+idx,
            'isData'   : 0,
        }
        idx+=1

##--Wjets
groupPlot['Wjets']={
                  'nameHR' : 'W+jets',
                  'isSignal' : 0,
                  'color': dict_TColor['green'],
                  'isData'   : 0,

}
if CombineWjets :
    groupPlot['Wjets']['samples']=['Wjets']
    plot['Wjets']  = {
        'nameHR' : 'Wjets',
        'isSignal' : 0,
        'color': dict_TColor['green'],
        'isData'   : 0,
    }



else:
    groupPlot['Wjets']['samples'] = Wjets                                                                                                                                        
    #del groupPlot['Wjets']
    total=len(Wjets)
    idx=-1*int(total/2)
    for wjet in Wjets:
        #groupPlot[wjet]={
        #    'nameHR' : wjet,
        #    'isSignal' : 0,
        #    'color': dict_TColor['green']+idx,
        #    'isData'   : 0,
        #    'samples':wjet
        #}
        plot[wjet]={
            'nameHR' : wjet,
            'isSignal' : 0,
            'color': dict_TColor['green']+idx,
            'isData'   : 0,

        }
        idx+=1


##--Tops
total=len(TOPS)
idx=-1*int(total/2)

for top in TOPS:
    groupPlot[top]={
        'nameHR' : top,
        'isSignal' : 0,
        'color': dict_TColor['orange']+idx,
        'isData'   : 0,
        'samples'  : [top]
    }
    plot[top]  = {
        'nameHR' : top,
        'isSignal' : 0,
        'color': dict_TColor['orange']+idx,
        'isData'   : 0,
    }
    idx+=1





    
if UsePseudoData:
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


#for MX in List_MX:
if 'SR' in scriptname:
    if not UsePseudoData : plot['DATA']['isBlind']=1
if "Boost" in scriptname:
    #MList=[3000]
    MList=[900]
    if Year=='2016':MList=[2500]
    scale=100
else:
    MList=[400]
    scale=100
        
for MX in MList:
    
    plot['ggHWWlnuqq_M'+str(MX)+'_S']={
        #'nameHR':'ggHWWlnuqq_M'+str(MX)+'x'+str(scale),
        #'nameHR':'ggHWWlnuqq_M'+str(MX),
        'nameHR':'GGF'+str(MX)+' x'+str(scale),
        'scale' : scale,
        'isData'   : 0,
        'isSignal' : 2,
        'color':dict_TColor['red'],
        'samples' : ['ggHWWlnuqq_M'+str(MX)+'_S']
    }
    groupPlot['ggHWWlnuqq_M'+str(MX)+'_S']={
        #'nameHR':'ggHWWlnuqq_M'+str(MX)+'x'+str(scale),
        'nameHR':'GGF'+str(MX)+' x'+str(scale),
        #'nameHR':'ggHWWlnuqq_M'+str(MX),
        'scale' : scale,
        'isData'   : 0,
        'isSignal' : 2,
        'color':dict_TColor['red'],
        'samples' : ['ggHWWlnuqq_M'+str(MX)+'_S']
    }

    #for MX in List_MX_VBF:
for MX in MList:
    #continue
    groupPlot['vbfHWWlnuqq_M'+str(MX)+'_S']={
        'nameHR':'VBF M'+str(MX)+' x'+str(scale),
        #'nameHR':'vbfHWWlnuqq_M'+str(MX),
        'isData'   : 0,
        'isSignal' : 2,
        'scale' : scale,
        'color':dict_TColor['blue'],
        'samples' : ['vbfHWWlnuqq_M'+str(MX)+'_S']
    }
    
    plot['vbfHWWlnuqq_M'+str(MX)+'_S']={
        'nameHR':'VBF'+str(MX)+' x'+str(scale),
        #'nameHR':'vbfHWWlnuqq_M'+str(MX)+'x'+str(scale),
        #'nameHR':'vbfHWWlnuqq_M'+str(MX),
        'isData'   : 0,
        'isSignal' : 2,
        'scale' : scale,
        'color':dict_TColor['blue'],
        'samples' : ['vbfHWWlnuqq_M'+str(MX)+'_S']
    }

    

if Year=='2016':
    lumi=35.9
if Year=='2017':
    lumi=41.5
if Year=='2018':
    lumi=59.7


legend['lumi'] = 'L = '+str(lumi)+'/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'


