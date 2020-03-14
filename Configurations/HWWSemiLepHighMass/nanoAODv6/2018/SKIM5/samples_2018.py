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
STEP="MCl1loose2018v6__MCCorr2018v6__HMSemilepSkimJH2018v6_5__HMlnjjVars_Dev_jhchoi"



CAMPAIGN_DATA='Run2018_102X_nAODv6_Full2018v6'
STEP_DATA="DATAl1loose2018v6__HMSemilepSkimJH2018v6_5_data__HMlnjjVars_Dev_jhchoi"


directory=treeBaseDir+CAMPAIGN+'/'+STEP






LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'

LepWPweight='(((Lepton_isTightElectron_'+eleWP+'[0]>0.5)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]'+')) + ((Lepton_isTightMuon_'+muWP+'[0]>0.5)*(Lepton_tightMuon_'+muWP+'_TotSF'+'[0]'+')))'
XSWeight      = 'XSWeight'

SFweight = 'puWeight*\
TriggerEffWeight_1l*\
EMTFbug_veto\
'
SFweight=SFweight+'*'+LepWPweight+'*'+LepWPCut

GenLepMatch = 'Lepton_genmatched[0]'



################################################
############### B-Tag  WP ######################
################################################

#pfCombinedInclusiveSecondaryVertexV2BJetTags (CSV) algorithm [26] loose working point.
SFweight=SFweight+'*btagSF*tau21SF'


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
            'SingleMuon'     : 'Trigger_sngMu' ,
            'EGamma' : 'Trigger_sngEl && !Trigger_sngMu' ,
           }



'''
####-Test---####
samples['QCD_MU'] = {    'name'   :   
                         getSampleFiles(directory,'QCD_Pt-300to470_MuEnrichedPt5',False,'nanoLatino_')                      ,
                         'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC,
                         'FilesPerJob' : 20,
}

samples['WW'] = {    'name'   :   getSampleFiles(directory,'WW-LO',False,'nanoLatino_') ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+LepWPweight ,
                     'FilesPerJob' : 1,
}

'''



import sys
sys.path.insert(0, "MassPoints")
from List_MX import *
from List_MX_VBF import *


for MX in List_MX:

  samples['ggHWWlnuqq_M'+str(MX)] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                                 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                                                 'FilesPerJob' : 10,
                                               }
    
for MX in List_MX_VBF:

  samples['vbfHWWlnuqq_M'+str(MX)] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                                 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                                                 'FilesPerJob' : 10,
                                               }




###########################################                                                                                                  
#############  BACKGROUNDS  ###############                                                                                                  
###########################################                                                                                                  

samples['Wjets'] = {    'name'   :   
                        getSampleFiles(directory,'WJetsToLNu-0J',False,'nanoLatino_')
                        +getSampleFiles(directory,'WJetsToLNu-1J',False,'nanoLatino_')
                        +getSampleFiles(directory,'WJetsToLNu-2J',False,'nanoLatino_')
                        ,
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                        'FilesPerJob' : 5,
                 }

addSampleWeight(samples, 'Wjets', 'WJetsToLNu-0J', '0.915')
addSampleWeight(samples, 'Wjets', 'WJetsToLNu-1J', '0.915')
addSampleWeight(samples, 'Wjets', 'WJetsToLNu-2J', '0.915')



############ DY ############                                                                                                   
ptllDYW_NLO = '((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'


samples['DY'] = {    'name'   :   getSampleFiles(directory,'DYJetsToLL_M-50-LO',False,'nanoLatino_')
                     + getSampleFiles(directory,'DYJetsToLL_M-10to50-LO',False,'nanoLatino_'),
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+ptllDYW_LO,
                     'FilesPerJob' : 20,
}
#addSampleWeight(samples,'DY','DYJetsToLL_M-50',ptllDYW_NLO)
#addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)

                 

samples['top'] = {    'name'   :   getSampleFiles(directory,'TTToSemiLeptonic_ext3',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_t-channel_top',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_t-channel_antitop',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_s-channel_ext1',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_tW_antitop_ext1',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_tW_top_ext1',False,'nanoLatino_')
                      + getSampleFiles(directory,'TTTo2L2Nu',False,'nanoLatino_') 
                      ,
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                      'FilesPerJob' : 4,
                      #'FilesPerJob' : 40,
                    }

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
                     'FilesPerJob' : 20,
}


samples['QCD_EM'] = {'name'   :
                  getSampleFiles(directory,'QCD_Pt-15to20_EMEnriched',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt-20to30_EMEnriched',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt-30to50_EMEnriched',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt-50to80_EMEnriched',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt-80to120_EMEnriched',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt-120to170_EMEnriched',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt-170to300_EMEnriched',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt-300toInf_EMEnriched',False,'nanoLatino_')

                  ,
                  'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC,
                  'FilesPerJob' : 20,
}


samples['QCD_bcToE'] = {'name'   :
                  getSampleFiles(directory,'QCD_Pt_20to30_bcToE',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt_30to80_bcToE',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt_80to170_bcToE',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt_170to250_bcToE',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt_250toInf_bcToE',False,'nanoLatino_')
                  ,
                  'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC,
                  'FilesPerJob' : 20,
}
##--MultiBoson
samples['WW'] = {    'name'   :   getSampleFiles(directory,'WWToLNuQQ',False,'nanoLatino_') ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+LepWPweight ,
                     'FilesPerJob' : 2,                 
}
'''

samples['WZ'] = {    'name'   :   getSampleFiles(directory,'WZ',False,'nanoLatino_') ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+LepWPweight ,
                 }

samples['ZZ'] = {    'name'   :   getSampleFiles(directory,'ZZ',False,'nanoLatino_') ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+LepWPweight ,
                 }


samples['WWW'] = {    'name'   :   getSampleFiles(directory,'WWW',False,'nanoLatino_') ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+LepWPweight ,
                 }

samples['WZZ'] = {    'name'   :   getSampleFiles(directory,'WZZ',False,'nanoLatino_') ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+LepWPweight ,
                 }
samples['ZZZ'] = {    'name'   :   getSampleFiles(directory,'ZZZ',False,'nanoLatino_') ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+LepWPweight ,
                 }

samples['WWZ'] = {    'name'   :   getSampleFiles(directory,'WWZ',False,'nanoLatino_') ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+LepWPweight ,
                 }

'''
samples['ggHWWlnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M125',False,'nanoLatino_'),
                                    'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                                    'FilesPerJob' : 10,
                            }

samples['vbfHWWlnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M125',False,'nanoLatino_'),
                                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                                     'FilesPerJob' : 10,
                              }
samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut ,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 10,
                  }

#print samples['DATA']



for Run in DataRun :
        directory = treeBaseDir+CAMPAIGN_DATA+'/'+STEP_DATA
        for DataSet in DataSets :
                FileTarget = getSampleFiles(directory,DataSet+'_'+Run[1],True,'nanoLatino_')
                for iFile in FileTarget:

                        #print(iFile)
                        
                        samples['DATA']['name'].append(iFile)
                        samples['DATA']['weights'].append(DataTrig[DataSet])
                        


