from LatinoAnalysis.Tools.commonTools import *
from WPandCut2017 import *

#xrootdPath = 'root://cms-xrdr.private.lo:2094'
#treeBaseDir = "/xrootd/store/user/jhchoi/Latino/HWWNano/"


##--Set Campaign and Step--##                                                                                                                                 
#CAMPAIGN='Fall2017_102X_nAODv5_Full2017v6'
#STEP="MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_nom"

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


M='1500' ##model mass

branchname='meP'+M+'_Bst_ggf_S_'+WTAG+'_nom'

os.system('mkdir -p MEKD/')
f=open('MEKD/'+branchname+'.py','w')
f.write('melaggf={}\n')
f.write('melavbf={}\n')
print "--ggh--"
print List_MX 
for MX in List_MX:
    print MX
    #def GetMinMaxCuts(filelist,model,modes=['','_I','_B','_H','_I_HB'],nsigma=2): ##read 'model+modes' branch
    MELA_cuts=GetMinMaxCuts(getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),branchname,['']) ##'meP'+M+'_Bst_ggf_S_'+WTAG+'_nom'
    cut=MELA_cuts['cut']
    eff=MELA_cuts['Npass']/(MELA_cuts['Npass']+MELA_cuts['Nveto'])
    cut+='*'+str(1/eff)
    print cut
    f.write('melaggf['+str(MX)+']={}\n')
    f.write('melaggf['+str(MX)+']["Mean"]="'+str(MELA_cuts['']['Mean'])+'"\n')
    f.write('melaggf['+str(MX)+']["dev"]="'+str(MELA_cuts['']['dev'])+'"\n')
print "--vbf--"
print List_MX_VBF
for MX in List_MX_VBF:
    print MX
    MELA_cuts=GetMinMaxCuts(getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),branchname,[''])
    cut=MELA_cuts['cut']
    eff=MELA_cuts['Npass']/(MELA_cuts['Npass']+MELA_cuts['Nveto'])
    cut+='*'+str(1/eff)
    print cut
    f.write('melavbf['+str(MX)+']={}\n')
    f.write('melavbf['+str(MX)+']["Mean"]="'+str(MELA_cuts['']['Mean'])+'"\n')
    f.write('melavbf['+str(MX)+']["dev"]="'+str(MELA_cuts['']['dev'])+'"\n')

