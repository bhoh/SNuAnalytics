from LatinoAnalysis.Tools.commonTools import *
from WPandCut2018 import *

xrootdPath = 'root://cms-xrdr.private.lo:2094'
treeBaseDir = "/xrootd/store/user/jhchoi/Latino/HWWNano/"


##--Set Campaign and Step--##                                                                                                                                 

CAMPAIGN='Autumn18_102X_nAODv6_Full2018v6'
STEP="MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_nom"



directory=treeBaseDir+CAMPAIGN+'/'+STEP



import sys
sys.path.insert(0, "MassPoints")
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
    cut=MELA_cuts['cut']
    print cut
    f.write('melaggf['+str(MX)+']="'+cut+'"\n')
print "--vbf--"
print List_MX_VBF
for MX in List_MX_VBF:
    print MX
    MELA_cuts=GetMinMaxCuts(getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),model)
    cut=MELA_cuts['cut']
    print cut
    f.write('melavbf['+str(MX)+']="'+cut+'"\n')
