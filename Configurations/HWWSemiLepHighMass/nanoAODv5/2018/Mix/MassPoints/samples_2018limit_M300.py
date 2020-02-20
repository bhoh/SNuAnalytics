

#-----Variable Deinition-----#

                                                                                                                                                              

supercut = 'nLepton>0'


eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'


LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'


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


CAMPAIGN='Autumn18_102X_nAODv5_Full2018v5'
STEP="MCl1loose2018v5__MCCorr2018v5__Semilep2018_whad30__CorrFatJetMass__HMlnjjSelBWR"



CAMPAIGN_DATA='Run2018_102X_nAODv5_Full2018v5'
STEP_DATA="DATAl1loose2018v5__Semilep2018_whad30__HMlnjjSel"


directory=treeBaseDir+CAMPAIGN+'/'+STEP






LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'

LepWPweight='(((Lepton_isTightElectron_'+eleWP+'[0]>0.5)*(Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]'+')) + ((Lepton_isTightMuon_'+muWP+'[0]>0.5)*(Lepton_tightMuon_'+muWP+'_IdIsoSF'+'[0]'+')))'
XSWeight      = 'XSWeight'
#SFweight      = 'SFweight'+Nlep+'l*'+LepWPweight+'*'+LepWPCut
#SFweight = 'puWeight*\
#TriggerEffWeight_1l*\
#Lepton_RecoSF[0]*\
#EMTFbug_veto'

SFweight = 'puWeight*\
TriggerEffWeight_1l*\
Lepton_RecoSF[0]*\
EMTFbug_veto*\
PUJetIdSF*\
tau21SF\
'
SFweight=SFweight+'*'+LepWPweight+'*'+LepWPCut

#GenLepMatch   = 'GenLepMatch'+Nlep+'l'
GenLepMatch = 'Lepton_genmatched[0]'

################################################
############### B-Tag  WP ######################
################################################


SFweight=SFweight+'*'+'btagSF'

################################################
############### B-Tag  WP ######################
################################################

#pfCombinedInclusiveSecondaryVertexV2BJetTags (CSV) algorithm [26] loose working point.


################################################                                                                                             
############   MET  FILTERS  ###################                                                                                             
################################################                                                                                             

METFilter_MC   = 'METFilter_MC'

METFilter_DATA = 'METFilter_DATA'

################################################                                                                                             
############ DATA DECLARATION ##################                                                                                             
################################################ 
DataRun = [
    ['A','Run2018A-Nano1June2019-v1'] ,
    ['B','Run2018B-Nano1June2019-v1'] ,
    ['C','Run2018C-Nano1June2019-v1'] ,
    ['D','Run2018D-Nano1June2019_ver2-v1'] ,
    
]

DataSets = ['SingleMuon',\
'EGamma'
]

DataTrig = {
            'SingleMuon'     : 'Trigger_sngMu' ,
            'EGamma' : 'Trigger_sngEl && !Trigger_sngMu' ,
           }

###########################################
############### SIGNAL ####################
###########################################

'''
samples['ggHWWlnuqq_M300'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M300',False,'nanoLatino_'),
                                    'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                                    #'weight' : XSWeight,
                                    'FilesPerJob' : 5,
                                  }
'''


samples['ggHWWlnuqq_M300_S_B_I'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M300',False,'nanoLatino_'),
                                               'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*(MSSModel+MSSModel_I+MSSModel_B+MSSModel_H+MSSModel_I_HB)',
                                             'FilesPerJob' : 50,
                                           }

samples['ggHWWlnuqq_M300_S'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M300',False,'nanoLatino_'),
                                         'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*MSSModel',
                                         'FilesPerJob' : 50,
                                      }

samples['ggWW_MELA'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M300',False,'nanoLatino_'),
                                        'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*(MSSModel_B+MSSModel_H+MSSModel_I_HB)',
                                         'FilesPerJob' : 50,
                                       }


samples['VBFHToWWToLNuQQ_M300_S_B_I'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M300',False,'nanoLatino_'),
                                             'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*(MSSModel+MSSModel_I+MSSModel_B+MSSModel_H+MSSModel_I_HB)',
                                             'FilesPerJob' : 50,
                                           }

samples['VBFHToWWToLNuQQ_M300_S'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M300',False,'nanoLatino_'),
                                         'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*MSSModel',
                                         'FilesPerJob' : 50,
                                       }

samples['qqWW_MELA'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M300',False,'nanoLatino_'),
                                         'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*(MSSModel_B+MSSModel_H+MSSModel_I_HB)',
                                        'FilesPerJob' : 50,


                                      }


###########################################                                                                                                  
#############  BACKGROUNDS  ###############                                                                                                  
###########################################                                                                                                  

samples['Wjets'] = {    'name'   :   getSampleFiles(directory,'WJetsToLNu-0J',False,'nanoLatino_')
                        +getSampleFiles(directory,'WJetsToLNu-1J',False,'nanoLatino_')
                        +getSampleFiles(directory,'WJetsToLNu-2J',False,'nanoLatino_')
                        ,
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                        'FilesPerJob' : 20,
                 }


############ DY ############                                                                                                   
ptllDYW_NLO = '((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'


samples['DY'] = {    'name'   :   #getSampleFiles(directory,'DYJetsToLL_M-50',False,'nanoLatino_')
                     getSampleFiles(directory,'DYJetsToLL_M-50-LO',False,'nanoLatino_')
                     + getSampleFiles(directory,'DYJetsToLL_M-10to50-LO',False,'nanoLatino_'),
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                     'FilesPerJob' : 20,
}
#addSampleWeight(samples,'DY','DYJetsToLL_M-50',ptllDYW_NLO)
addSampleWeight(samples,'DY','DYJetsToLL_M-50-LO',ptllDYW_LO)
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)

                 

samples['top'] = {    'name'   :   getSampleFiles(directory,'TTToSemiLeptonic',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_t-channel_top',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_t-channel_antitop',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_s-channel_ext1',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_tW_antitop_ext1',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_tW_top_ext1',False,'nanoLatino_') 
                      ,
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                      'FilesPerJob' : 5,
                    }

#samples['VV'] = {    'name'   :   getSampleFiles(directory,'WZ',False,'nanoLatino_')
#                      + getSampleFiles(directory,'ZZ',False,'nanoLatino_')
#                     ,
#                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                     'FilesPerJob' : 5,
#                    }


samples['QCD_MU'] = {    'name'   :   getSampleFiles(directory,'QCD_Pt-15to20_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-20to30_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-30to50_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-50to80_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-80to120_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-80to120_MuEnrichedPt5_ext1',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-120to170_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-120to170_MuEnrichedPt5_ext1',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-170to300_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-300to470_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-300to470_MuEnrichedPt5_ext3',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-470to600_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-470to600_MuEnrichedPt5_ext1',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-600to800_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-800to1000_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-1000toInf_MuEnrichedPt5',False,'nanoLatino_')
                      

                      ,
                     'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC,
                     'FilesPerJob' : 20,
                    }
samples['QCD_EM'] = {    'name'   :   getSampleFiles(directory,'QCD_Pt-15to20_EMEnriched',False,'nanoLatino_')
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

addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-15to20_MuEnrichedPt5', '0.0022')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-20to30_MuEnrichedPt5', '0.0045')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-30to50_MuEnrichedPt5', '0.00974')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-50to80_MuEnrichedPt5', '0.0196')

addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-80to120_MuEnrichedPt5', '0.0322')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-80to120_MuEnrichedPt5_ext1', '0.0322')
###EXT
w1=str(getEventSumw(directory,'QCD_Pt-80to120_MuEnrichedPt5','nanoLatino_'))
w2=str(getEventSumw(directory,'QCD_Pt-80to120_MuEnrichedPt5_ext1','nanoLatino_'))
totalw=str(float(w1)+float(w2))
######

addSampleWeight(samples,'QCD_MU','QCD_Pt-80to120_MuEnrichedPt5',w1+"/"+totalw)
addSampleWeight(samples,'QCD_MU','QCD_Pt-80to120_MuEnrichedPt5_ext1',w2+"/"+totalw)

addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-120to170_MuEnrichedPt5', '0.04518')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-120to170_MuEnrichedPt5_ext1', '0.04518')
###EXT
w1=str(getEventSumw(directory,'QCD_Pt-120to170_MuEnrichedPt5','nanoLatino_'))
w2=str(getEventSumw(directory,'QCD_Pt-120to170_MuEnrichedPt5_ext1','nanoLatino_'))
totalw=str(float(w1)+float(w2))
addSampleWeight(samples,'QCD_MU','QCD_Pt-120to170_MuEnrichedPt5',w1+"/"+totalw)
addSampleWeight(samples,'QCD_MU','QCD_Pt-120to170_MuEnrichedPt5_ext1',w2+"/"+totalw)
######

addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-170to300_MuEnrichedPt5', '0.0598')

addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-300to470_MuEnrichedPt5', '0.10196')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-300to470_MuEnrichedPt5_ext3', '0.10196')
###EXT
w1=str(getEventSumw(directory,'QCD_Pt-300to470_MuEnrichedPt5','nanoLatino_'))
w2=str(getEventSumw(directory,'QCD_Pt-300to470_MuEnrichedPt5_ext3','nanoLatino_'))
totalw=str(float(w1)+float(w2))
addSampleWeight(samples,'QCD_MU','QCD_Pt-300to470_MuEnrichedPt5',w1+"/"+totalw)
addSampleWeight(samples,'QCD_MU','QCD_Pt-300to470_MuEnrichedPt5_ext3',w2+"/"+totalw)
###

addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-470to600_MuEnrichedPt5', '0.08722')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-470to600_MuEnrichedPt5_ext1', '0.08722')
###EXT
w1=str(getEventSumw(directory,'QCD_Pt-470to600_MuEnrichedPt5','nanoLatino_'))
w2=str(getEventSumw(directory,'QCD_Pt-470to600_MuEnrichedPt5_ext1','nanoLatino_'))
totalw=str(float(w1)+float(w2))
addSampleWeight(samples,'QCD_MU','QCD_Pt-470to600_MuEnrichedPt5',w1+"/"+totalw)
addSampleWeight(samples,'QCD_MU','QCD_Pt-470to600_MuEnrichedPt5_ext1',w2+"/"+totalw)
###

addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-600to800_MuEnrichedPt5', '0.13412')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-800to1000_MuEnrichedPt5', '0.14552')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-1000toInf_MuEnrichedPt5', '0.15544')



addSampleWeight(samples, 'QCD_EM', 'QCD_Pt-15to20_EMEnriched', '0.0096*0.1101') 
addSampleWeight(samples, 'QCD_EM', 'QCD_Pt-15to20_EMEnriched_ext1', '0.0096*0.1101') 
###EXT
#w1=str(getEventSumw(directory,'QCD_Pt-15to20_EMEnriched','nanoLatino_'))
#w2=str(getEventSumw(directory,'QCD_Pt-15to20_EMEnriched_ext1','nanoLatino_'))
#totalw=str(float(w1)+float(w2))
#addSampleWeight(samples,'QCD_EM','QCD_Pt-15to20_EMEnriched',w1+"/"+totalw)
#addSampleWeight(samples,'QCD_EM','QCD_Pt-15to20_EMEnriched_ext1',w2+"/"+totalw)
###


addSampleWeight(samples, 'QCD_EM', 'QCD_Pt-20to30_EMEnriched', '0.008875251076')
addSampleWeight(samples, 'QCD_EM', 'QCD_Pt-30to50_EMEnriched', '0.0470')
addSampleWeight(samples, 'QCD_EM', 'QCD_Pt-50to80_EMEnriched', '0.100')
addSampleWeight(samples, 'QCD_EM', 'QCD_Pt-50to80_EMEnriched_ext1', '0.100')
##EXT
#w1=str(getEventSumw(directory,'QCD_Pt-50to80_EMEnriched','nanoLatino_'))
#w2=str(getEventSumw(directory,'QCD_Pt-50to80_EMEnriched_ext1','nanoLatino_'))
#totalw=str(float(w1)+float(w2))
#addSampleWeight(samples,'QCD_EM','QCD_Pt-50to80_EMEnriched',w1+"/"+totalw)
#addSampleWeight(samples,'QCD_EM','QCD_Pt-50to80_EMEnriched_ext1',w2+"/"+totalw)
###

addSampleWeight(samples, 'QCD_EM', 'QCD_Pt-80to120_EMEnriched', '0.1359064286')
addSampleWeight(samples, 'QCD_EM', 'QCD_Pt-120to170_EMEnriched', '0.1396945073')
addSampleWeight(samples, 'QCD_EM', 'QCD_Pt-170to300_EMEnriched', '0.1829736842')
addSampleWeight(samples, 'QCD_EM', 'QCD_Pt-300toInf_EMEnriched', '0.15')


samples['QCD_bcToE'] = {    'name'   :   #getSampleFiles(directory,'QCD_Pt_20to30_bcToE',False,'nanoLatino_')
                            getSampleFiles(directory,'QCD_Pt_30to80_bcToE',False,'nanoLatino_')
                            #+getSampleFiles(directory,'QCD_Pt_80to170_bcToE',False,'nanoLatino_')
                            #+getSampleFiles(directory,'QCD_Pt_170to250_bcToE',False,'nanoLatino_')
                            #+getSampleFiles(directory,'QCD_Pt_250toInf_bcToE',False,'nanoLatino_')
                            ,
                         'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC,
                         'FilesPerJob' : 20,
                       }


#samples['WW'] = {    'name'   :   getSampleFiles(directory,'WW-LO',False,'nanoLatino_')
#                     ,
#                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                     'FilesPerJob' : 5,
#                    }


#samples['WWToLNuQQ'] = {    'name'   :   getSampleFiles(directory,'WWToLNuQQ',False,'nanoLatino_') ,
#                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+LepWPweight ,
#                 }
#def getEventSumw(directory,sample,prefix):

#Wjets_w1=str(getEventSumw(directory,'WJetsToLNu','nanoLatino_'))
#Wjets_w2=str(getEventSumw(directory,'WJetsToLNu_ext2','nanoLatino_'))
#Wjets_totalw=str(float(Wjets_w1)+float(Wjets_w2))
#print "Wjets_w1="+Wjets_w1
#print "Wjets_w2="+Wjets_w2
#print "Wjets_totalw="+Wjets_totalw





###########################################                                                                                                  
################## DATA ###################                                                                                                  
###########################################                                                                                                  



samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut ,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 20,
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
                        
