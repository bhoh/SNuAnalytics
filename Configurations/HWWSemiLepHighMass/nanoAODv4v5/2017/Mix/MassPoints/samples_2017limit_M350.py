#-----Variable Deinition-----#

                                                                                                                                                              

supercut = 'nLepton>0'


eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'

LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'

bAlgo='DeepB'
bWP='0.1522'

#isbjet='(CleanJet_jetIdx[CleanJetNotFat_jetIdx]>0 && CleanJet_pt[CleanJetNotFat_jetIdx]>20 && fabs(CleanJet_eta[CleanJetNotFat_jetIdx]) < 2.4 && Jet_btag'+bAlgo+'[CleanJet_jetIdx[CleanJetNotFat_jetIdx]] > '+bWP+'  )'
'''
isbjet='(Jet_btag'+bAlgo+'[CleanJet_jetIdx] > '+bWP +'&&'+'(Jet_pt[CleanJet_jetIdx]>20)  )'
nbjet='(Sum$'+isbjet+')'
btagSF_each='( '+isbjet+'*Alt$(Jet_btagSF, 1) + !'+isbjet+'*1 )'
logbtagSF='(Sum$(  TMath::Log('+btagSF_each+')))'
btagSF='(TMath::Exp( '+logbtagSF+' ))'
'''
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


CAMPAIGN='Fall2017_102X_nAODv4_Full2017v5'
#STEP="MCl1loose2017v5__MCCorr2017v5__Semilep2017__HMlnjjSel2017"
#STEP="MCl1loose2017v5__MCCorr2017v5__Semilep2017_whad30__CorrFatJetMass__HMlnjjSel"
STEP="MCl1loose2017v5__MCCorr2017v5__Semilep2017_whad30__CorrFatJetMass__HMlnjjSelBWR"



CAMPAIGN_DATA='Run2017_102X_nAODv4_Full2017v5'
STEP_DATA="DATAl1loose2017v5__Semilep2017_whad30__HMlnjjSel"


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
  ['B','Run2017B-Nano14Dec2018-v1'] ,
  ['C','Run2017C-Nano14Dec2018-v1'],
  ['D','Run2017D-Nano14Dec2018-v1'],
  ['E','Run2017E-Nano14Dec2018-v1'],
  ['F','Run2017F-Nano14Dec2018-v1']
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




samples['ggHWWlnuqq_M350_S_B_I'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M350',False,'nanoLatino_'),
                                             'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*(MSSModel+MSSModel_I+MSSModel_B+MSSModel_H+MSSModel_I_HB)',
                                             'FilesPerJob' : 50,
                                           }

samples['ggHWWlnuqq_M350_S'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M350',False,'nanoLatino_'),
                                         'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*MSSModel',
                                         'FilesPerJob' : 50,
                                       }

samples['ggWW_MELA'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M350',False,'nanoLatino_'),
                                         'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*(MSSModel_B+MSSModel_H+MSSModel_I_HB)',
                                        'FilesPerJob' : 50,
                                         
                                         
                                      }


samples['VBFHToWWToLNuQQ_M350_S_B_I'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M350',False,'nanoLatino_'),
                                             'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*(MSSModel+MSSModel_I+MSSModel_B+MSSModel_H+MSSModel_I_HB)',
                                             'FilesPerJob' : 50,
                                           }

samples['VBFHToWWToLNuQQ_M350_S'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M350',False,'nanoLatino_'),
                                         'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*MSSModel',
                                         'FilesPerJob' : 50,
                                       }

samples['qqWW_MELA'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M350',False,'nanoLatino_'),
                                         'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*(MSSModel_B+MSSModel_H+MSSModel_I_HB)',
                                        'FilesPerJob' : 50,
                                         
                                         
                                      }






#samples['VBFHToWWToLNuQQ_M'+str(MX)] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
#                                           'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                                           #'weight' : XSWeight,
#                                           'FilesPerJob' : 40,
#                                         }

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
                        'FilesPerJob' : 2,
                 }

#addSampleWeight(samples, 'Wjets', 'WJetsToLNu-0J', '0.0022')
#addSampleWeight(samples, 'Wjets', 'WJetsToLNu-0J', '0.0022')
#addSampleWeight(samples, 'Wjets', 'WJetsToLNu-0J', '0.0022')



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
                      'FilesPerJob' : 2,
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

'''

samples['QCD_pt170to300']={'name':
                           getSampleFiles(directory,'QCD_Pt_170to300',False,'nanoLatino_')
                           +getSampleFiles(directory,'QCD_Pt_170to300_ext1',False,'nanoLatino_')
                           ,
                           'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*0.5',
                           'FilesPerJob' : 20,
}
'''

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




#samples['WW'] = {    'name'   :   getSampleFiles(directory,'WW-LO',False,'nanoLatino_') ,
#                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+LepWPweight ,
#                 }

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
                        

