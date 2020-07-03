UsePseudoData=False
print "UsePseudoData=",UsePseudoData

CombineMultiV=True ##Turn off when making shapes and combing multiv/ Turn on when mkRuncards, plotting
MultiV=['WW','WWJJ','WZ','ZZ','WWW','WWZ','WZZ','ZZZ',]
CombineWjets=True
Wjets=['Wjets0j','Wjets1j','Wjets2j']
CombineH125=True
H125=['ggHWWlnuqq_M125','vbfHWWlnuqq_M125','ZHWWlnuqq_M125','WpHWWlnuqq_M125','WmHWWlnuqq_M125',
       'ggHtautaulnuqq_M125','vbfHtautaulnuqq_M125','Wmhtautaulnuqq_M125','WpHtautaulnuqq_M125','ZHtautaulnuqq_M125']



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


groupPlot['DY']  = {
    'nameHR' : 'DY',
    'isSignal' : 0,
    'color': dict_TColor['yellow'], 
    'isData'   : 0,
    'samples' : ['DY']
}

groupPlot['QCD']  = {
    'nameHR' : 'QCD',
    'isSignal' : 0,
    'color': dict_TColor['gray'],
    'isData'   : 0,
    'samples'  : []
}


QCD_MU=['QCD_Pt-15to20_MuEnrichedPt5',
        'QCD_Pt-20to30_MuEnrichedPt5',
        'QCD_Pt-30to50_MuEnrichedPt5',
        'QCD_Pt-50to80_MuEnrichedPt5',
        'QCD_Pt-80to120_MuEnrichedPt5',
        'QCD_Pt-120to170_MuEnrichedPt5',
        'QCD_Pt-170to300_MuEnrichedPt5',
        'QCD_Pt-300to470_MuEnrichedPt5',
        'QCD_Pt-470to600_MuEnrichedPt5',
        'QCD_Pt-600to800_MuEnrichedPt5',
        'QCD_Pt-800to1000_MuEnrichedPt5',
        'QCD_Pt-1000toInf_MuEnrichedPt5',
]
QCD_EM=[
  'QCD_Pt-20to30_EMEnriched',
  'QCD_Pt-30to50_EMEnriched',
  'QCD_Pt-50to80_EMEnriched',
  'QCD_Pt-80to120_EMEnriched',
  'QCD_Pt-120to170_EMEnriched',
  'QCD_Pt-170to300_EMEnriched',
  'QCD_Pt-300toInf_EMEnriched'
]
QCD_bcToE=[
  'QCD_Pt_20to30_bcToE',
  'QCD_Pt_30to80_bcToE',
  'QCD_Pt_80to170_bcToE',
  'QCD_Pt_170to250_bcToE',
  'QCD_Pt_250toInf_bcToE',
]




if 'mu' in scriptname:

    groupPlot['QCD']['samples']=['QCD_MU']
if 'ele' in scriptname:

    groupPlot['QCD']['samples']=['QCD_EM','QCD_bcToE']



for s in ['QCD_EM','QCD_MU','QCD_bcToE']:
    plot[s]  = {
        'nameHR' : s,
        'isSignal' : 0,
        'color': dict_TColor['gray'],
        'isData'   : 0,
    }

groupPlot['MultiV']={
    'nameHR' : 'Multi V',
    'isSignal' : 0,
    'color': dict_TColor['azure'],
    'isData'   : 0,
    'samples'  : MultiV
    
}
if CombineMultiV:
    groupPlot['MultiV']['samples']=['MultiV']


groupPlot['Wjets']={
                  'nameHR' : 'W+jets',
                  'isSignal' : 0,
                  'color': dict_TColor['green'],
                  'isData'   : 0,
                  'samples'  : Wjets
}
if CombineWjets:
    groupPlot['Wjets']['samples']=['Wjets']

groupPlot['h125']={
    'nameHR' : 'W+jets',
    'isSignal' : 0,
    'color': dict_TColor['pink'],
    'isData'   : 0,
    'samples'  : H125

}

if CombineH125:
    groupPlot['h125']['samples']=['h125']

groupPlot['top']={
    'nameHR' : 'Top',
    'isSignal' : 0,
'color': dict_TColor['orange'],
                  'isData'   : 0,
                  'samples'  : ['top']
}

plot['DY']  = {
                  'nameHR' : 'DY',
                  'isSignal' : 0,
                  'color': dict_TColor['yellow'], 
                  'isData'   : 0,
              }
if CombineMultiV:
    plot['MultiV']  = {
        'nameHR' : 'MultiV',
        'isSignal' : 0,
        'color': dict_TColor['cyan'], 
        'isData'   : 0,
    }
else:

    total=len(MultiV)
    idx=-1*int(total/2)
    for s in MultiV:
        plot[s]={
            'nameHR' : s,
            'isSignal' : 0,
            'color': dict_TColor['cyan']+idx,
            'isData'   : 0,

        }
        idx+=1
        '''
    plot['WZZ']  = {
        'nameHR' : 'WZZ',
        'isSignal' : 0,
        'color': dict_TColor['azure'], 
        'isData'   : 0,
    }
    
    plot['WWZ']  = {
        'nameHR' : 'WWZ',
        'isSignal' : 0,
        'color': dict_TColor['azure']+1, 
        'isData'   : 0,
    }
    plot['WWW']  = {
        'nameHR' : 'WWW',
        'isSignal' : 0,
        'color': dict_TColor['azure']+1, 
        'isData'   : 0,
    }
    plot['ZZZ']  = {
        'nameHR' : 'ZZZ',
        'isSignal' : 0,
        'color': dict_TColor['azure']+1, 
        'isData'   : 0,
    }
    
    plot['ZZ']  = {
        'nameHR' : 'ZZ',
        'isSignal' : 0,
        'color': dict_TColor['azure']+2,
        'isData'   : 0,
    }
    
    plot['WZ']  = {
        'nameHR' : 'WZ',
        'isSignal' : 0,
        'color': dict_TColor['azure']+3, 
        'isData'   : 0,
    }
    plot['WW']  = {
        'nameHR' : 'WW',
        'isSignal' : 0,
        'color': dict_TColor['cyan'], 
        'isData'   : 0,
    }
        '''

#plot['WpWmJJ_EWK_QCD_noHiggs']  = {
#                  'nameHR' : 'WpWmJJ_EWK_QCD_noHiggs',
#                  'isSignal' : 0,
#                  'color': dict_TColor['cyan']+2, 
#                  'isData'   : 0,
#              }


plot['top']  = {
                  'nameHR' : 'Top',
                  'isSignal' : 0,
                  'color': dict_TColor['orange'],
                  'isData'   : 0,                 
              }




if CombineWjets:
    plot['Wjets']  = {
        'nameHR' : 'Wjets',
        'isSignal' : 0,
        'color': dict_TColor['green'],
        'isData'   : 0,
    }
else:
    total=len(Wjets)
    idx=-1*int(total/2)
    for s in Wjets:
        plot[s]={
            'nameHR' : s,
            'isSignal' : 0,
            'color': dict_TColor['green']+idx,
            'isData'   : 0,

        }
        idx+=1
        '''
    plot['Wjets0j']  = {
        'nameHR' : 'Wjets0j',
        'isSignal' : 0,
        'color': dict_TColor['green'],
        'isData'   : 0,
    }
    plot['Wjets1j']  = {
        'nameHR' : 'Wjets1j',
        'isSignal' : 0,
        'color': dict_TColor['green']-3,
        'isData'   : 0,
    }
    plot['Wjets2j']  = {
        'nameHR' : 'Wjets2j',
        'isSignal' : 0,
        'color': dict_TColor['green']+1,
        'isData'   : 0,
    }
        '''

if CombineH125:
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


#for MX in List_MX:
if 'SR' in scriptname:
    if not UsePseudoData : plot['DATA']['isBlind']=1
    if "Boost" in scriptname:
        MList=[900]
        scale=100
    else:
        MList=[400]
        scale=10
        
    for MX in MList:

        plot['ggHWWlnuqq_M'+str(MX)+'_S']={
            'nameHR':'ggHWWlnuqq_M'+str(MX),
            'scale' : scale,
            'isData'   : 0,
            'isSignal' : 3,
            'color':dict_TColor['red'],
            'samples' : ['ggHWWlnuqq_M'+str(MX)+'_S']
        }
        groupPlot['ggHWWlnuqq_M'+str(MX)+'_S']={
            'nameHR':'ggHWWlnuqq_M'+str(MX),
            'scale' : scale,
            'isData'   : 0,
            'isSignal' : 3,
            'color':dict_TColor['red'],
            'samples' : ['ggHWWlnuqq_M'+str(MX)+'_S']
        }

        #for MX in List_MX_VBF:
    for MX in MList:
        #continue
        groupPlot['vbfHWWlnuqq_M'+str(MX)+'_S']={
            'nameHR':'vbfHWWlnuqq_M'+str(MX),
            'isData'   : 0,
            'isSignal' : 3,
            'scale' : scale,
            'color':dict_TColor['blue'],
            'samples' : ['ggHWWlnuqq_M'+str(MX)+'_S']
        }

        plot['vbfHWWlnuqq_M'+str(MX)+'_S']={
            'nameHR':'vbfHWWlnuqq_M'+str(MX),
            'isData'   : 0,
            'isSignal' : 3,
            'scale' : scale,
            'color':dict_TColor['blue'],
            'samples' : ['ggHWWlnuqq_M'+str(MX)+'_S']
        }

    

legend['lumi'] = 'L = 41.5/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
