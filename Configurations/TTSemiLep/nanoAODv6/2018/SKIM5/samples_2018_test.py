#------End of Variable Definition-----#


import os, sys
import glob
import copy
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *

#-----Variable Deinition-----#
try:
  from WPandCut2018 import *
except ImportError:
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv6/2018/SKIM5"
  sys.path.append(BASE_PATH)
  from WPandCut2018 import *

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
#STEP='MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__4j2b_CHToCB_2018__kinFitTTSemiLep'
STEP='MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__prune_CHToCB_2018'
#STEP='MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10'

CAMPAIGN_DATA='Run2018_102X_nAODv6_Full2018v6'
#STEP_DATA='DATAl1loose2018v6__HMSemilepSKIMv6_10_data__4j2b_CHToCB_2018__kinFitTTSemiLep'
STEP_DATA='DATAl1loose2018v6__HMSemilepSKIMv6_10_data__kinFitTTSemiLep'
#STEP_DATA='DATAl1loose2018v6__HMSemilepSKIMv6_10_data'

#directory=treeBaseDir+CAMPAIGN+'/'+STEP
directory=xrootdPath+'//xrd/store/user/jhchoi/Latino/HWWNano/'+CAMPAIGN+'/'+STEP






LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'

#eleWPweight='((Lepton_isTightElectron_'+eleWP+'[0]>0.5)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]'+'))'
eleWPweight='((abs(Lepton_pdgId[0])==11)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]'+'))'
#eleWPweight+='*(TriggerEffWeight_1l)'
eleWPweight+='*(HLT_Ele32_WPTight_Gsf==1)'

#muWPweight='((Lepton_isTightMuon_'+muWP+'[0]>0.5)*(Lepton_tightMuon_'+muWP+'_TotSF'+'[0]'+'))'
muWPweight='((abs(Lepton_pdgId[0])==13)*(Lepton_tightMuon_'+muWP+'_TotSF'+'[0]'+'))'
muWPweight+='*(TriggerEffWeight_1l)'


LepWPweight='(%s + %s)'%(eleWPweight,muWPweight)
XSWeight      = 'XSWeight'

SFweight = 'puWeight*\
EMTFbug_veto\
'
SFweight=SFweight+'*'+LepWPCut+'*'+LepWPweight

GenLepMatch = 'Lepton_genmatched[0]'
#GenLepMatch = 'Lepton_promptgenmatched[0]*Alt$(!Lepton_promptgenmatched[1], 1)'

#SFweight=SFweight+'*HEMweight'

################################################
############### B-Tag  WP ######################
################################################

#pfCombinedInclusiveSecondaryVertexV2BJetTags (CSV) algorithm [26] loose working point.
#SFweight=SFweight+'*btagSF*HEMweight'
SFweight=SFweight+'*btagSF'


################################################
###############  PU ID SF  ######################
################################################

SFweight+="*Jet_PUID_SF_L"

################################################
############### TT specific SF  ################
################################################
#XXX
#TTSFweight = 'btagSFNorm_top'
TTSFweight = '1'
TTbj        = '(genTtbarId%100==51 && genTtbarId%100==52)'
TTbb       = '(genTtbarId%100>=53 && genTtbarId%100<=55)*(2.9/2.3)'
TTcc       = '(genTtbarId%100>=41 && genTtbarId%100<=45)'
TTjj       = '(!%s && !%s && !%s)'%(TTbj,TTbb,TTcc)

################################################                                                                                             
############   MET  FILTERS  ###################                                                                                             
################################################                                                                                             

METFilter_MC   = 'METFilter_MC'

METFilter_DATA = 'METFilter_DATA'

################################################                                                                                             
############ DATA DECLARATION ##################                                                                                             
################################################ 
DataRun = [
    ['A','Run2018A-Nano25Oct2019-v1'] ,
    ['B','Run2018B-Nano25Oct2019-v1'] ,
    ['C','Run2018C-Nano25Oct2019-v1'] ,
    ['D','Run2018D-Nano25Oct2019_ver2-v1'] ,

]

DataSets = ['SingleMuon',\
'EGamma'
]

DataTrig = {
            'SingleMuon'     : 'Trigger_sngMu',
            'EGamma' : '!Trigger_sngMu && Trigger_sngEl',
           }





#import sys
#sys.path.insert(0, "MassPoints")
#from List_MX import *
#from List_MX_VBF import *
#
#
#for MX in List_MX:
#
#  samples['ggHWWlnuqq_M'+str(MX)] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
#                                                 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                                                 'FilesPerJob' : 10,
#                                               }
#    
#for MX in List_MX_VBF:
#
#  samples['vbfHWWlnuqq_M'+str(MX)] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
#                                                 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                                                 'FilesPerJob' : 10,
#                                               }




###########################################                                                                                                  
#############  BACKGROUNDS  ###############                                                                                                  
###########################################                                                                                                  
#samples['TTLJ'] = {    'name'   :   getSampleFiles(directory,'TTToSemiLeptonic_ext3',False,'nanoLatino_'),
#                      'weight' : XSWeight+'*'+SFweight+'*'+TTSFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                      #'FilesPerJob' : 4,
#                      'FilesPerJob' : 2,
#
#
#
#                    }

samples['TTLJ+jj'] = {    'name'   :   getSampleFiles(directory,'TTToSemiLeptonic_ext3',False,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+TTSFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+TTjj,
                      #'FilesPerJob' : 4,
                      'FilesPerJob' : 2,



                    }


samples['TTLJ+cc'] = {    'name'   :   getSampleFiles(directory,'TTToSemiLeptonic_ext3',False,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+TTSFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+TTcc,
                      #'FilesPerJob' : 4,
                      'FilesPerJob' : 2,
                    }


samples['TTLJ+bj'] = {    'name'   :   getSampleFiles(directory,'TTToSemiLeptonic_ext3',False,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+TTSFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+TTbj,
                      #'FilesPerJob' : 4,
                      'FilesPerJob' : 2,



                    }


samples['TTLJ+bb'] = {    'name'   :   getSampleFiles(directory,'TTToSemiLeptonic_ext3',False,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+TTSFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+TTbb,
                      #'FilesPerJob' : 4,
                      'FilesPerJob' : 2,



                    }


