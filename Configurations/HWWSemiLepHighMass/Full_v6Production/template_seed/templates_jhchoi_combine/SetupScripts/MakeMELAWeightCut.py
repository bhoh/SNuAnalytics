from LatinoAnalysis.Tools.commonTools import *
import sys
import sys
sys.path.insert(0, "MassPoints")
sys.path.append(os.getcwd())
from WPandCut2016 import *

#xrootdPath = 'root://cms-xrdr.private.lo:2094'
#treeBaseDir = "/xrootd/store/user/jhchoi/Latino/HWWNano/"


##--Set Campaign and Step--##

directory=treeBaseDir+CAMPAIGN+'/'+STEP




from List_MX import *
from List_MX_VBF import *

#model="cprime1.0BRnew0.0"
#model='RelW0.02'
from FilterMelaReweights import GetMinMaxCuts

##--MakeDirectoryForMelaweight
import os
os.system('mkdir -p MELACUT/')

f=open('MELACUT/'+model+'.py','w')
f.write('melaggf={}\n')
f.write('melavbf={}\n')
print "--ggh--"
print List_MX 
for MX in List_MX:
    print MX
    MELA_cuts=GetMinMaxCuts(getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),model)
    weightSum=MELA_cuts['wSum']
    print "weightSum/MELA_cuts['Npass']=",weightSum/MELA_cuts['Npass']
    cut=MELA_cuts['cut']
    eff=MELA_cuts['Npass']/(MELA_cuts['Npass']+MELA_cuts['Nveto'])
    cut+='*'+str(1/eff)
    if 'RelW' in model :cut+='*'+str(MELA_cuts['Npass']/weightSum)
    print cut
    f.write('melaggf['+str(MX)+']="'+cut+'"\n')
print "--vbf--"
print List_MX_VBF
for MX in List_MX_VBF:
    print MX
    MELA_cuts=GetMinMaxCuts(getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),model)
    weightSum=MELA_cuts['wSum']
    print "weightSum/MELA_cuts['Npass']=",weightSum/MELA_cuts['Npass']
    cut=MELA_cuts['cut']
    eff=MELA_cuts['Npass']/(MELA_cuts['Npass']+MELA_cuts['Nveto'])
    cut+='*'+str(1/eff)
    if 'RelW' in model :cut+='*'+str(MELA_cuts['Npass']/weightSum)
    print cut
    f.write('melavbf['+str(MX)+']="'+cut+'"\n')
