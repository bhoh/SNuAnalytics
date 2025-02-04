import os
import sys
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/SignalXsec')


#-----Variable Deinition-----#
from WPandCut2016 import *


directory=treeBaseDir+CAMPAIGN+'/'+STEP


from GetXsecInNtuple import GetXsecInNtuple
from LatinoAnalysis.Tools.commonTools import *

from PowhegXsec import *

kfactor={}

if not Year=='2016':
    kfactor={
        'Wjets0j':{
            'samplename':'WJetsToLNu-0J',
            'target_xsec':'50131.98',
            'kfactor':'1',
        },
        'Wjets1j':{
            'samplename':'WJetsToLNu-1J',
            'target_xsec':'8426.09',
            'kfactor':'1',
        },
        'Wjets2j':{
            'samplename':'WJetsToLNu-2J',
            'target_xsec':'3172.96',
            'kfactor':'1',
        },
        
    }

    kfactor['QCD_Pt-20to30_MuEnrichedPt5']={
        'samplename':'QCD_Pt-20to30_MuEnrichedPt5',
        'target_xsec':'2.232e+06',
        'kfactor':'1'
    }
    kfactor['QCD_Pt-30to50_MuEnrichedPt5']={
        'samplename':'QCD_Pt-30to50_MuEnrichedPt5',
        'target_xsec':'1.389e+06',
        'kfactor':'1'
    }
    kfactor['QCD_Pt-50to80_MuEnrichedPt5']={
        'samplename':'QCD_Pt-50to80_MuEnrichedPt5',
        'target_xsec':'3.961e+05',
        'kfactor':'1'
    }
    kfactor['QCD_Pt-80to120_MuEnrichedPt5']={
        'samplename':'QCD_Pt-80to120_MuEnrichedPt5',
        'target_xsec':'8.779e+04',
        'kfactor':'1'
    }
    kfactor['QCD_Pt-120to170_MuEnrichedPt5']={
        'samplename':'QCD_Pt-120to170_MuEnrichedPt5',
        'target_xsec':'2.090e+04',
        'kfactor':'1'
    }
    kfactor['QCD_Pt-170to300_MuEnrichedPt5']={
        'samplename':'QCD_Pt-170to300_MuEnrichedPt5',
        'target_xsec':'7.075e+03',
        'kfactor':'1'
    }
    kfactor['QCD_Pt-300to470_MuEnrichedPt5']={
        'samplename':'QCD_Pt-300to470_MuEnrichedPt5',
        'target_xsec':'6.075e+02',
        'kfactor':'1'
    }
    kfactor['QCD_Pt-470to600_MuEnrichedPt5']={
        'samplename':'QCD_Pt-470to600_MuEnrichedPt5',
        'target_xsec':'5.865e+01',
        'kfactor':'1'
    }
    kfactor['QCD_Pt-600to800_MuEnrichedPt5']={
        'samplename':'QCD_Pt-600to800_MuEnrichedPt5',
        'target_xsec':'1.807e+01',
        'kfactor':'1'
    }
    kfactor['QCD_Pt-800to1000_MuEnrichedPt5']={
        'samplename':'QCD_Pt-800to1000_MuEnrichedPt5',
        'target_xsec':'3.301e+00',
        'kfactor':'1'
    }
    
    kfactor['QCD_Pt-1000toInf_MuEnrichedPt5']={
        'samplename':'QCD_Pt-1000toInf_MuEnrichedPt5',
        'target_xsec':'1.090e+00',
        'kfactor':'1'
    }



else:
    kfactor={
        'Wjets0j':{
            'samplename':'WJetsToLNu_0J',
            'target_xsec':'50131.98',
            'kfactor':'1',
        },
        'Wjets1j':{
            'samplename':'WJetsToLNu_1J',
            'target_xsec':'8426.09',
            'kfactor':'1',
        },
        'Wjets2j':{
            'samplename':'WJetsToLNu_2J',
            'target_xsec':'3172.96',
            'kfactor':'1',
        },

    }

    kfactor['QCD_Pt-20toInf_MuEnrichedPt15']={
        'samplename':'QCD_Pt-20toInf_MuEnrichedPt15',
        'target_xsec':'272600',
        'kfactor':'1'
    }

##--QCD Mu
kfactor['QCD_Pt-15to20_MuEnrichedPt5']={
    'samplename':'QCD_Pt-15to20_MuEnrichedPt5',
    'target_xsec':'2.819e+06',
    'kfactor':'1'
}

##--QCD EM
kfactor['QCD_Pt-20to30_EMEnriched']={
    'samplename':'QCD_Pt-20to30_EMEnriched',
    'target_xsec':'4.886e+06',
    'kfactor':'1'
}
kfactor['QCD_Pt-30to50_EMEnriched']={
    'samplename':'QCD_Pt-30to50_EMEnriched',
    'target_xsec':'6.298e+06',
    'kfactor':'1'
}
kfactor['QCD_Pt-50to80_EMEnriched']={
    'samplename':'QCD_Pt-50to80_EMEnriched',
    'target_xsec':'1.961e+06',
    'kfactor':'1'
}
kfactor['QCD_Pt-80to120_EMEnriched']={
    'samplename':'QCD_Pt-80to120_EMEnriched',
    'target_xsec':'3.656e+05',
    'kfactor':'1'
}
kfactor['QCD_Pt-120to170_EMEnriched']={
    'samplename':'QCD_Pt-120to170_EMEnriched',
    'target_xsec':'3.656e+05',
    'kfactor':'1'
}
kfactor['QCD_Pt-170to300_EMEnriched']={
    'samplename':'QCD_Pt-170to300_EMEnriched',
    'target_xsec':'20860.0',
    'kfactor':'1'
}
kfactor['QCD_Pt-300toInf_EMEnriched']={
    'samplename':'QCD_Pt-300toInf_EMEnriched',
    'target_xsec':'1350.',
    'kfactor':'1'
}


for s in kfactor:
    if not 'QCD' in s: continue

    r_mu="0.341"
    r_em="0.425"
    r_bctoe="1.741" 
    if 'EM' in s:
        kfactor[s]['target_xsec']=r_em+'*'+kfactor[s]['target_xsec']
    elif 'Mu' in s:
        kfactor[s]['target_xsec']=r_mu+'*'+kfactor[s]['target_xsec']
    elif 'bcToE' in s:
        kfactor[s]['target_xsec']=r_bctoe+'*'+kfactor[s]['target_xsec']



NormToPowheg={

}



from LatinoAnalysis.Tools.HiggsXSection  import *
HiggsXS = HiggsXSection()

import sys
sys.path.insert(0, "MassPoints")
from List_MX import *
from List_MX_VBF import *
BR='0.1086*2*0.6741*2' ##only mu,e decay for Wlep
HWW_XSEC={
'GGF':{},
'VBF':{},
}
HWWLNUQQ_XSEC={
'GGF':{},
'VBF':{},
}

##----Fill information of latest signal xsec
for MX in List_MX:
    this_xsec=HiggsXS.GetHiggsProdXS('YR4','13TeV','ggH',int(MX),'bsm')*HiggsXS.GetHiggsBR('YR4','H_WW',int(MX),'bsm')
    HWW_XSEC['GGF'][MX]=this_xsec
    HWWLNUQQ_XSEC['GGF'][MX]=this_xsec*float(eval(BR))
    kfactor['ggHWWlnuqq_M'+str(MX)]={
        'samplename':'GluGluHToWWToLNuQQ_M'+str(MX),
        'target_xsec':str(this_xsec)+'*'+BR,
        'kfactor':'1',
    }
    this_xsec=GGF[Year][int(MX)][0]
    NormToPowheg['ggHWWlnuqq_M'+str(MX)]={
        'samplename':'GluGluHToWWToLNuQQ_M'+str(MX),
        'target_xsec':str(this_xsec),
        'kfactor':1,
    }
for MX in List_MX_VBF:
    
    this_xsec=HiggsXS.GetHiggsProdXS('YR4','13TeV','vbfH',int(MX),'bsm')*HiggsXS.GetHiggsBR('YR4','H_WW',int(MX),'bsm')
    HWW_XSEC['VBF'][MX]=this_xsec
    HWWLNUQQ_XSEC['VBF'][MX]=this_xsec*float(eval(BR))
    kfactor['vbfHWWlnuqq_M'+str(MX)]={
        'samplename':'VBFHToWWToLNuQQ_M'+str(MX),
        'target_xsec':str(this_xsec)+'*'+BR,
        'kfactor':'1',
    }
    this_xsec=VBF[Year][int(MX)][0]
    NormToPowheg['vbfHWWlnuqq_M'+str(MX)]={
        'samplename':'VBFHToWWToLNuQQ_M'+str(MX),
        'target_xsec':str(this_xsec),
        'kfactor':1,
    }
##-----

##---Calc Kfactor---
for s in sorted(kfactor):
    path=getSampleFiles(directory,kfactor[s]['samplename'],False,'nanoLatino_')[0].replace("###","")
    kfactor[s]['kfactor']=str(format(eval(kfactor[s]['target_xsec']+'/'+str(GetXsecInNtuple(path))),'5g'))
    print s,kfactor[s]['kfactor']

for s in sorted(NormToPowheg):
    path=getSampleFiles(directory,kfactor[s]['samplename'],False,'nanoLatino_')[0].replace("###","")
    NormToPowheg[s]['kfactor']=str(format(eval(NormToPowheg[s]['target_xsec']+'/'+str(GetXsecInNtuple(path))),'5g'))

##--export
import os

os.system('mkdir -p kfactor/')
f=open('kfactor/kfactor.py','w')
f.write('kfactor={}\n')
for s in kfactor:
    f.write('kfactor["'+s+'"]="'+str(kfactor[s]['kfactor'])+'"'+'\n')
f.close()


f=open('kfactor/NormToPowheg.py','w')
f.write('NormToPowheg={}\n')
for s in NormToPowheg:
    f.write('NormToPowheg["'+s+'"]="'+str(NormToPowheg[s]['kfactor'])+'"'+'\n')
f.close()


os.system('mkdir -p xsec/')
f=open('xsec/XSEC.py','w')

f.write('HWW_XSEC='+str(HWW_XSEC)+'\n')
f.write('HWWLNUQQ_XSEC='+str(HWWLNUQQ_XSEC)+'\n')
f.close()




