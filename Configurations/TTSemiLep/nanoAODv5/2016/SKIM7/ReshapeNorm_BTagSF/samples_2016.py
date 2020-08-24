#------End of Variable Definition-----#


import os, sys
import glob
import copy
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *

#-----Variable Deinition-----#
try:
  from WPandCut2016 import *
except ImportError:
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv5/2016/SKIM7"
  sys.path.append(BASE_PATH)
  from WPandCut2016 import *

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


CAMPAIGN='Summer16_102X_nAODv5_Full2016v6'
STEP="MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10"



CAMPAIGN_DATA='Run2016_102X_nAODv5_Full2016v6'
STEP_DATA="DATAl1loose2016v6__HMSemilepSKIMv6_10_data"


#directory=treeBaseDir+CAMPAIGN+'/'+STEP
directory=xrootdPath+'//xrd/store/user/jhchoi/Latino/HWWNano/'+CAMPAIGN+'/'+STEP






LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'

LepWPweight='(((Lepton_isTightElectron_'+eleWP+'[0]>0.5)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]'+')) + ((Lepton_isTightMuon_'+muWP+'[0]>0.5)*(Lepton_tightMuon_'+muWP+'_TotSF'+'[0]'+')))'
XSWeight      = 'XSWeight'

SFweight = 'puWeight*\
PrefireWeight*\
TriggerEffWeight_1l*\
EMTFbug_veto\
'
SFweight=SFweight+'*'+LepWPweight+'*'+LepWPCut

GenLepMatch = 'Lepton_genmatched[0]'

#SFweight=SFweight+'*HEMweight'

################################################
############### B-Tag  WP ######################
################################################
btagSF = "((CleanJet_pt>20 && abs(CleanJet_eta)<2.4)*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(CleanJet_pt<=20 || abs(CleanJet_eta)>=2.4))"

#pfCombinedInclusiveSecondaryVertexV2BJetTags (CSV) algorithm [26] loose working point.
SFweight=SFweight+'*'+btagSF


################################################                                                                                             
############   MET  FILTERS  ###################                                                                                             
################################################                                                                                             
METFilter_MC   = 'METFilter_MC'

###########################################                                                                                                  
#############  BACKGROUNDS  ###############                                                                                                  
###########################################                                                                                                  



samples['top'] = {    'name'   :   getSampleFiles(directory,'TTToSemiLeptonic',False,'nanoLatino_')
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
