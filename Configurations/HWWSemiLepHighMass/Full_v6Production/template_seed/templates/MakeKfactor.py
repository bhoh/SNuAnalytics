import os
import sys
sys.path.append(os.getcwd())


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

NormToPowheg={

}

#ggHWWlnuqq_M'+str(MX)
#GluGluHToWWToLNuQQ_M
#vbfHWWlnuqq_M
#VBFHToWWToLNuQQ_M


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

#getSampleFiles(directory,'WJetsToLNu-0J',False,'nanoLatino_')
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




