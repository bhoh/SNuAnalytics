#-----Variable Deinition-----#

supercut = 'nLepton>0'

eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'

LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'

bAlgo='DeepB'
bWP='0.1522'

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


CAMPAIGN='Fall2017_102X_nAODv5_Full2017v6'
STEP="MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMlnjjVars_Dev"


CAMPAIGN_DATA='Run2017_102X_nAODv5_Full2017v6'
STEP_DATA="DATAl1loose2017v6__HMSemilepSKIMv6_10_data__HMlnjjVars_Dev"
#STEP_DATA="DATAl1loose2017v6__HMSemilepSkimJHv6_7_data__HMlnjjVars_Dev"


directory=treeBaseDir+CAMPAIGN+'/'+STEP



LepWPweight='(((Lepton_isTightElectron_'+eleWP+'[0]>0.5)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]'+')) + ((Lepton_isTightMuon_'+muWP+'[0]>0.5)*(Lepton_tightMuon_'+muWP+'_TotSF'+'[0]'+')))'
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
PrefireWeight'
SFweight=SFweight+'*'+LepWPweight+'*'+LepWPCut

#GenLepMatch   = 'GenLepMatch'+Nlep+'l'
GenLepMatch = 'Lepton_genmatched[0]'

################################################
############### B-Tag  WP ######################
################################################


SFweight=SFweight+'*btagSF'


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
  ['B','Run2017B-Nano1June2019-v1'] ,
  ['C','Run2017C-Nano1June2019-v1'],
  ['D','Run2017D-Nano1June2019-v1'],
  ['E','Run2017E-Nano1June2019-v1'],
  ['F','Run2017F-Nano1June2019-v1']
]

DataSets = ['SingleMuon',\
'SingleElectron'
]

DataTrig = {
            'SingleMuon'     : 'Trigger_sngMu' ,
            'SingleElectron' : '!Trigger_sngMu && Trigger_sngEl' ,
           }

###########################################
############### SIGNAL ####################
###########################################

import sys
sys.path.insert(0, "MassPoints")

#from List_MX import *
#from List_MX_VBF import *
from List_melaKDmass import *

##--ggF X
#for MX in List_MX:
for MX in List_melaKDmass:

  samples['ggHWWlnuqq_M'+str(MX)] = {
      'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
      'FilesPerJob' : 50,
                               }

##--VBF X                                                                                                                                      

#for MX in List_MX_VBF:
for MX in List_melaKDmass:

  samples['VBFHToWWToLNuQQ_M'+str(MX)] = {
      'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
      'FilesPerJob' : 50,
                                            }
    

###########################################                                                                                                  
#############  BACKGROUNDS  ###############                                                                                                  
###########################################                                                                                                  

samples['Wjets'] = {    'name'   :   
                        getSampleFiles(directory,'WJetsToLNu-0J',False,'nanoLatino_')
                        +getSampleFiles(directory,'WJetsToLNu-1J',False,'nanoLatino_')
                        +getSampleFiles(directory,'WJetsToLNu-2J',False,'nanoLatino_')
                        #getSampleFiles(directory,'WJetsToLNu_HT100_200',False,'nanoLatino_')
                        #+ getSampleFiles(directory,'WJetsToLNu_HT200_400',False,'nanoLatino_')
                        #+ getSampleFiles(directory,'WJetsToLNu_HT400_600',False,'nanoLatino_')
                        #+ getSampleFiles(directory,'WJetsToLNu_HT600_800',False,'nanoLatino_')
                        #+ getSampleFiles(directory,'WJetsToLNu_HT800_1200',False,'nanoLatino_')
                        #+ getSampleFiles(directory,'WJetsToLNu_HT1200_2500',False,'nanoLatino_')
                        #+ getSampleFiles(directory,'WJetsToLNu_HT2500_inf',False,'nanoLatino_')
                        ,
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                        'FilesPerJob' : 10,
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
                     'FilesPerJob' : 40,
}
#addSampleWeight(samples,'DY','DYJetsToLL_M-50',ptllDYW_NLO)
#addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)

                 

samples['top'] = {    'name'   :   getSampleFiles(directory,'TTToSemiLeptonic',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_t-channel_top',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_t-channel_antitop',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_s-channel',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_tW_antitop',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_tW_top',False,'nanoLatino_') 
                      ,
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                      'FilesPerJob' : 5,
                      #'FilesPerJob' : 40,
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
                  #+getSampleFiles(directory,'QCD_Pt-170to300_EMEnriched',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt-300toInf_EMEnriched',False,'nanoLatino_')

                  ,
                  'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC,
                  'FilesPerJob' : 20,
}


'''
QCD_Pt_20to30_bcToE
QCD_Pt_30to80_bcToE
QCD_Pt_80to170_bcToE
QCD_Pt_170to250_bcToE
QCD_Pt_250toInf_bcToE

'''
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



#addSampleWeight(samples, 'QCD_bcToE', 'QCD_Pt_170to250_bcToE', '5')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-15to20_MuEnrichedPt5', '0.0022')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-20to30_MuEnrichedPt5', '0.0045')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-30to50_MuEnrichedPt5', '0.00974')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-50to80_MuEnrichedPt5', '0.0196')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-80to120_MuEnrichedPt5', '0.0322')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-120to170_MuEnrichedPt5', '0.04518')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-170to300_MuEnrichedPt5', '0.0598')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-300to470_MuEnrichedPt5', '0.08024013043')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-470to600_MuEnrichedPt5', '0.08775072499')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-600to800_MuEnrichedPt5', '0.13412')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-800to1000_MuEnrichedPt5', '0.14552')
addSampleWeight(samples, 'QCD_MU', 'QCD_Pt-1000toInf_MuEnrichedPt5', '0.15544')


addSampleWeight(samples, 'QCD_EM', 'QCD_Pt-15to20_EMEnriched', '0.001057282011')  #missing sample
addSampleWeight(samples, 'QCD_EM', 'QCD_Pt-20to30_EMEnriched', '0.0088')
addSampleWeight(samples, 'QCD_EM', 'QCD_Pt-30to50_EMEnriched', '0.0470')
addSampleWeight(samples, 'QCD_EM', 'QCD_Pt-50to80_EMEnriched', '0.100')
addSampleWeight(samples, 'QCD_EM', 'QCD_Pt-80to120_EMEnriched', '0.1359064286')
addSampleWeight(samples, 'QCD_EM', 'QCD_Pt-120to170_EMEnriched', '0.1396945073')
addSampleWeight(samples, 'QCD_EM', 'QCD_Pt-170to300_EMEnriched', '0.1829736842')
addSampleWeight(samples, 'QCD_EM', 'QCD_Pt-300toInf_EMEnriched', '0.15')




samples['WW'] = {    'name'   :   getSampleFiles(directory,'WW-LO',False,'nanoLatino_') ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+LepWPweight ,
                 }

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
#addSampleWeight(samples,'Wjets','WJetsToLNu',Wjets_w1+"/"+Wjets_totalw)
#addSampleWeight(samples,'Wjets','WJetsToLNu_ext2',Wjets_w2+"/"+Wjets_totalw)




###########################################                                                                                                  
################## DATA ###################                                                                                                  
###########################################                                                                                                  



samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut ,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 40,
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
                        

