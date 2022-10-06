#------End of Variable Definition-----#


import os, sys
import glob
import copy
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *

#-----Variable Deinition-----#
try:
  from WPandCut2017 import *
except ImportError:
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv5/2017/StackNew_comb"
  sys.path.append(BASE_PATH)
  from WPandCut2017 import *

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

CAMPAIGN='Fall2017_102X_nAODv5_Full2017v6'
STEP="MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__kinFitTTSemiLep_2017"



CAMPAIGN_DATA='Run2017_102X_nAODv5_Full2017v6'
STEP_DATA="DATAl1loose2017v6__HMSemilepSKIMv6_10_data__kinFitTTSemiLep_2017"


#directory=treeBaseDir+CAMPAIGN+'/'+STEP
directory=xrootdPath+'//xrd/store/user/jhchoi/Latino/HWWNano/'+CAMPAIGN+'/'+STEP


def makeMCDirectory(var=''):
   if var=='':
       return xrootdPath+'//xrd/store/user/jhchoi/Latino/HWWNano/'+CAMPAIGN+'/'+STEP
   else:
       return xrootdPath+'//xrd/store/user/jhchoi/Latino/HWWNano/'+CAMPAIGN+'/'+STEP + "{var}".format(var='__'+var)




LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'

#eleWPweight='((Lepton_isTightElectron_'+eleWP+'[0]>0.5)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]'+'))'
eleWPweight='((abs(Lepton_pdgId[0])==11)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]'+'))'
eleWPweight+='*(TriggerEffWeight_1l)'
#eleWPweight+='*(HLT_Ele35_WPTight_Gsf==1)'

#muWPweight='((Lepton_isTightMuon_'+muWP+'[0]>0.5)*(Lepton_tightMuon_'+muWP+'_TotSF'+'[0]'+'))'
muWPweight='((abs(Lepton_pdgId[0])==13)*(Lepton_tightMuon_'+muWP+'_TotSF'+'[0]'+'))'
muWPweight+='*(TriggerEffWeight_1l)'


LepWPweight='(%s + %s)'%(eleWPweight,muWPweight)
XSWeight      = 'XSWeight'

SFweight = 'puWeight*\
PrefireWeight*\
EMTFbug_veto\
'
SFweight=SFweight+'*'+LepWPCut+'*'+LepWPweight

#GenLepMatch = 'Lepton_genmatched[0]'
##GenLepMatch = 'Lepton_promptgenmatched[0]*Alt$(!Lepton_promptgenmatched[1], 1)'

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

SFweight+="*Jet_PUID_SF_L[0]"

################################################
############### TT specific SF  ################
################################################
#XXX
TTSFweight = 'btagSFNorm_top'
#TTSFweight = '1'
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
    ['B','Run2017B-Nano1June2019-v1'],
    ['C','Run2017C-Nano1June2019-v1'],
    ['D','Run2017D-Nano1June2019-v1'],
    ['E','Run2017E-Nano1June2019-v1'],
    ['F','Run2017F-Nano1June2019-v1']
]

DataSets = ['SingleMuon',\
'SingleElectron'
]

DataTrig = {
            'SingleMuon'     : 'Trigger_sngMu',
            'SingleElectron' : '!Trigger_sngMu && Trigger_sngEl',
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

samples['TTLJ+jj'] = {    'name'   :   getSampleFiles(directory,'TTToSemiLeptonic',False,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+TTSFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+TTjj,
                      #'FilesPerJob' : 4,
                      'FilesPerJob' : 9,



                    }


samples['TTLJ+cc'] = {    'name'   :   getSampleFiles(directory,'TTToSemiLeptonic',False,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+TTSFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+TTcc,
                      #'FilesPerJob' : 4,
                      'FilesPerJob' : 9,
                    }


samples['TTLJ+bj'] = {    'name'   :   getSampleFiles(directory,'TTToSemiLeptonic',False,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+TTSFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+TTbj,
                      #'FilesPerJob' : 4,
                      'FilesPerJob' : 9,



                    }


samples['TTLJ+bb'] = {    'name'   :   getSampleFiles(directory,'TTToSemiLeptonic',False,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+TTSFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+TTbb,
                      #'FilesPerJob' : 4,
                      'FilesPerJob' : 9,



                    }

name_TTLJ_TuneCP5Up = getSampleFiles(directory,'TTToSemiLeptonic_TuneCP5Up',False,'nanoLatino_')
name_TTLJ_TuneCP5Down = getSampleFiles(directory,'TTToSemiLeptonic_TuneCP5Down',False,'nanoLatino_')
name_TTLJ_hdampUp = getSampleFiles(directory,'TTToSemiLeptonic_hdampUp',False,'nanoLatino_')
name_TTLJ_hdampDown = getSampleFiles(directory,'TTToSemiLeptonic_hdampDown',False,'nanoLatino_')
name_TTLJ_mtopUp = getSampleFiles(directory,'TTToSemiLeptonic_mtopUp',False,'nanoLatino_')
name_TTLJ_mtopDown = getSampleFiles(directory,'TTToSemiLeptonic_mtopDown',False,'nanoLatino_')



samples['TTLL'] = {    'name'   :   getSampleFiles(directory,'TTTo2L2Nu_PSWeights',False,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                      'FilesPerJob' : 19,
                    }

name_TTLL_TuneCP5Up = getSampleFiles(directory,'TTTo2L2Nu_TuneCP5Up',False,'nanoLatino_')
name_TTLL_TuneCP5Down = getSampleFiles(directory,'TTTo2L2Nu_TuneCP5Down',False,'nanoLatino_')
name_TTLL_hdampUp = getSampleFiles(directory,'TTTo2L2Nu_hdampUp',False,'nanoLatino_')
name_TTLL_hdampDown = getSampleFiles(directory,'TTTo2L2Nu_hdampDown',False,'nanoLatino_')
name_TTLL_mtopUp = getSampleFiles(directory,'TTTo2L2Nu_mtopUp',False,'nanoLatino_')
name_TTLL_mtopDown = getSampleFiles(directory,'TTTo2L2Nu_mtopDown',False,'nanoLatino_')

samples['ST'] = {    'name'   :   getSampleFiles(directory,'ST_t-channel_top',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_t-channel_antitop',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_s-channel',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_tW_antitop',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_tW_top',False,'nanoLatino_')
                      ,
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                      'FilesPerJob' : 4,
                      #'FilesPerJob' : 40,
                    }


samples['Wjets'] = {    'name'   :   
                        getSampleFiles(directory,'WJetsToLNu-0J',False,'nanoLatino_')
                        +getSampleFiles(directory,'WJetsToLNu-1J',False,'nanoLatino_')
                        +getSampleFiles(directory,'WJetsToLNu-2J',False,'nanoLatino_')
                        ,
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                        'FilesPerJob' : 20,
                 }

addSampleWeight(samples, 'Wjets', 'WJetsToLNu-0J', '0.915')
addSampleWeight(samples, 'Wjets', 'WJetsToLNu-1J', '0.915')
addSampleWeight(samples, 'Wjets', 'WJetsToLNu-2J', '0.915')



############ DY ############                                                                                                   
ptllDYW_NLO = '((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'


samples['DY'] = {    'name'   :   getSampleFiles(directory,'DYJetsToLL_M-50-LO',False,'nanoLatino_')
                     + getSampleFiles(directory,'DYJetsToLL_M-10to50-LO',False,'nanoLatino_'),
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                     #'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+ptllDYW_LO,
                     'FilesPerJob' : 20,
}
#addSampleWeight(samples,'DY','DYJetsToLL_M-50',ptllDYW_NLO)
#addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)

                 

##--QCD
samples['QCD_MU'] = {    'name'   :   getSampleFiles(directory,'QCD_Pt-15to20_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-20to30_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-30to50_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-50to80_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-80to120_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-120to170_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-170to300_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-300to470_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-470to600_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-600to800_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-800to1000_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-1000toInf_MuEnrichedPt5',False,'nanoLatino_')

                      ,
                     'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC,
                     'FilesPerJob' : 100,
}


samples['QCD_EM'] = {'name'   :
                  #getSampleFiles(directory,'QCD_Pt-15to20_EMEnriched',False,'nanoLatino_')
                  getSampleFiles(directory,'QCD_Pt-20to30_EMEnriched',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt-30to50_EMEnriched',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt-50to80_EMEnriched',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt-80to120_EMEnriched',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt-120to170_EMEnriched',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt-170to300_EMEnriched',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt-300toInf_EMEnriched',False,'nanoLatino_')

                  ,
                  'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC,
                  'FilesPerJob' : 100,
}


samples['QCD_bcToE'] = {'name'   :
                  getSampleFiles(directory,'QCD_Pt_20to30_bcToE',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt_30to80_bcToE',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt_80to170_bcToE',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt_170to250_bcToE',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt_250toInf_bcToE',False,'nanoLatino_')
                  ,
                  'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC,
                  'FilesPerJob' : 100,
}
##--MultiBoson
samples['WW'] = {    'name'   :   getSampleFiles(directory,'WWToLNuQQ',False,'nanoLatino_') ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                     'FilesPerJob' : 100,                 
}

samples['WZ'] = {    'name'   :   getSampleFiles(directory,'WZ',False,'nanoLatino_') ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                     'FilesPerJob' : 100,                 
                 }

samples['ZZ'] = {    'name'   :   getSampleFiles(directory,'ZZ',False,'nanoLatino_') ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                     'FilesPerJob' : 100,                 
                 }

'''
samples['WWW'] = {    'name'   :   getSampleFiles(directory,'WWW',False,'nanoLatino_') ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                 }

samples['WZZ'] = {    'name'   :   getSampleFiles(directory,'WZZ',False,'nanoLatino_') ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                 }
samples['ZZZ'] = {    'name'   :   getSampleFiles(directory,'ZZZ',False,'nanoLatino_') ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                 }

samples['WWZ'] = {    'name'   :   getSampleFiles(directory,'WWZ',False,'nanoLatino_') ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                 }

'''

#TTX
samples['TTZjets'] = {    'name'   :   getSampleFiles(directory,'TTZjets',False,'nanoLatino_') ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                     'FilesPerJob' : 3,                 
                 }
samples['TTWjets'] = {    'name'   :   getSampleFiles(directory,'TTWjets',False,'nanoLatino_') ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                     'FilesPerJob' : 10,                 
                 }


# CHToCB signal
for mass in ['075','080','085','090','100','110','120','130','140','150']: #XXX 140 is under production
#for mass in ['075','080','085','090','100','110','120','130','150']:
    sample_name = 'CHToCB_M{0}'.format(mass) 
    samples[sample_name] = { 'name'    : getSampleFiles(directory,sample_name,False,'nanoLatino_'),
                                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                                     'FilesPerJob' : 1,
            }


samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut ,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 20,
                  }

#print samples['DATA']



for Run in DataRun :
        #directory = treeBaseDir+CAMPAIGN_DATA+'/'+STEP_DATA
        directory = xrootdPath+'//xrd/store/user/jhchoi/Latino/HWWNano/'+CAMPAIGN_DATA+'/'+STEP_DATA
        for DataSet in DataSets :
                FileTarget = getSampleFiles(directory,DataSet+'_'+Run[1],True,'nanoLatino_')
                for iFile in FileTarget:

                        #print(iFile)
                        
                        samples['DATA']['name'].append(iFile)
                        samples['DATA']['weights'].append(DataTrig[DataSet])
                        


