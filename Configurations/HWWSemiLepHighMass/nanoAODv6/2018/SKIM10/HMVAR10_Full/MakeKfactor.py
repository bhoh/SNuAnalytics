#samplesFile='samples_2017.py'
#handle=open(samplesFile,'r')
#exec(handle)
#handle.close()



xrootdPath = 'root://cms-xrdr.private.lo:2094'
treeBaseDir = "/xrootd/store/user/jhchoi/Latino/HWWNano/"
CAMPAIGN='Fall2017_102X_nAODv5_Full2017v6'
STEP="MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_nom"


directory=treeBaseDir+CAMPAIGN+'/'+STEP


from GetXsecInNtuple import GetXsecInNtuple
from LatinoAnalysis.Tools.commonTools import *
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
#getSampleFiles(directory,'WJetsToLNu-0J',False,'nanoLatino_')
for s in kfactor:
    path=getSampleFiles(directory,kfactor[s]['samplename'],False,'nanoLatino_')[0].replace("###","")
    kfactor[s]['kfactor']=kfactor[s]['target_xsec']+'/'+str(GetXsecInNtuple(path))
    print s,kfactor[s]['kfactor']


##--export
import os

os.system('mkdir -p kfactor/')
f=open('kfactor/kfactor.py','w')
f.write('kfactor={}\n')
for s in kfactor:
    f.write('kfactor["'+s+'"]="'+str(kfactor[s]['kfactor'])+'"'+'\n')
f.close()
