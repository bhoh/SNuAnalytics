#samplesFile='samples_2017.py'
#handle=open(samplesFile,'r')
#exec(handle)
#handle.close()



xrootdPath = 'root://cms-xrdr.private.lo:2094'
treeBaseDir = "/xrootd/store/user/jhchoi/Latino/HWWNano/"


CAMPAIGN='Summer16_102X_nAODv5_Full2016v6'
STEP="MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_nom"



directory=treeBaseDir+CAMPAIGN+'/'+STEP


from GetXsecInNtuple import GetXsecInNtuple
from LatinoAnalysis.Tools.commonTools import *

kfactor={
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
BR='0.1086*3*0.6741'
for MX in List_MX:
    this_xsec=HiggsXS.GetHiggsProdXS('YR4','13TeV','ggH',int(MX),'bsm')
    kfactor['ggHWWlnuqq_M'+str(MX)]={
        'samplename':'GluGluHToWWToLNuQQ_M'+str(MX),
        'target_xsec':str(this_xsec)+'*'+BR,
        'kfactor':'1',
    }
for MX in List_MX_VBF:
    this_xsec=HiggsXS.GetHiggsProdXS('YR4','13TeV','vbfH',int(MX),'bsm')
    kfactor['vbfHWWlnuqq_M'+str(MX)]={
        'samplename':'VBFHToWWToLNuQQ_M'+str(MX),
        'target_xsec':str(this_xsec)+'*'+BR,
        'kfactor':'1',
    }

#getSampleFiles(directory,'WJetsToLNu-0J',False,'nanoLatino_')
for s in sorted(kfactor):
    path=getSampleFiles(directory,kfactor[s]['samplename'],False,'nanoLatino_')[0].replace("###","")
    kfactor[s]['kfactor']=str(format(eval(kfactor[s]['target_xsec']+'/'+str(GetXsecInNtuple(path))),'5g'))
    print s,kfactor[s]['kfactor']


##--export
import os

os.system('mkdir -p kfactor/')
f=open('kfactor/kfactor.py','w')
f.write('kfactor={}\n')
for s in kfactor:
    f.write('kfactor["'+s+'"]="'+str(kfactor[s]['kfactor'])+'"'+'\n')
f.close()




