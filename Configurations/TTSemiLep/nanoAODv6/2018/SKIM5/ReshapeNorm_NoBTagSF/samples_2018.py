#-----Variable Deinition-----#
from WPandCut2018 import *

#------End of Variable Definition-----#


import os
import glob
import copy
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *



samples={}

SITE=os.uname()[1]
xrootdPath=''
if    'iihe' in SITE :
  xrootdPath  = 'dcap://maite.iihe.ac.be/'
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/'
elif  'cern' in SITE :
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'

elif  'sdfarm' in SITE:
  xrootdPath = 'root://cms-xrdr.private.lo:2094'
  treeBaseDir = "/xrootd/store/user/jhchoi/Latino/HWWNano/"


CAMPAIGN='Autumn18_102X_nAODv6_Full2018v6'
STEP="MCl1loose2018v6__MCCorr2018v6__HMSemilepSkimJH2018v6_5__HEMweightMC"



CAMPAIGN_DATA='Run2018_102X_nAODv6_Full2018v6'
STEP_DATA="DATAl1loose2018v6__HMSemilepSkimJH2018v6_5_data__HEMweightData"


#directory=treeBaseDir+CAMPAIGN+'/'+STEP
directory=xrootdPath+'//xrd/store/user/jhchoi/Latino/HWWNano/'+CAMPAIGN+'/'+STEP






LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'

LepWPweight='(((Lepton_isTightElectron_'+eleWP+'[0]>0.5)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]'+')) + ((Lepton_isTightMuon_'+muWP+'[0]>0.5)*(Lepton_tightMuon_'+muWP+'_TotSF'+'[0]'+')))'
XSWeight      = 'XSWeight'

SFweight = 'puWeight*\
TriggerEffWeight_1l*\
EMTFbug_veto\
'
SFweight=SFweight+'*'+LepWPweight+'*'+LepWPCut

GenLepMatch = 'Lepton_genmatched[0]'

SFweight=SFweight+'*HEMweight'

################################################                                                                                             
############   MET  FILTERS  ###################                                                                                             
################################################                                                                                             
METFilter_MC   = 'METFilter_MC'

###########################################                                                                                                  
#############  BACKGROUNDS  ###############                                                                                                  
###########################################                                                                                                  



samples['top'] = {    'name'   :   getSampleFiles(directory,'TTToSemiLeptonic_ext3',False,'nanoLatino_')
                      #+ getSampleFiles(directory,'ST_t-channel_top',False,'nanoLatino_')
                      #+ getSampleFiles(directory,'ST_t-channel_antitop',False,'nanoLatino_')
                      #+ getSampleFiles(directory,'ST_s-channel_ext1',False,'nanoLatino_')
                      #+ getSampleFiles(directory,'ST_tW_antitop_ext1',False,'nanoLatino_')
                      #+ getSampleFiles(directory,'ST_tW_top_ext1',False,'nanoLatino_')
                      #+ getSampleFiles(directory,'TTTo2L2Nu',False,'nanoLatino_') 
                      ,
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                      'FilesPerJob' : 4,
                      #'FilesPerJob' : 40,
                    }
