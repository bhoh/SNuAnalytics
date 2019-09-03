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

#MCl1loose2016__MCCorr2016__FatJetPreselCleaningWlep_semilep
CAMPAIGN='Summer16_102X_nAODv4_Full2016v4'
#STEP="MCl1loose2016__MCCorr2016__FatJetPreselCleaning_semilep_v2"
STEP="MCl1loose2016__MCCorr2016__FatJetPreselCleaning_semilep_v2__wlepMaker"
#STEP="MCl1loose2016__MCCorr2016"


CAMPAIGN_DATA='Run2016_102X_nAODv4_Full2016v4'
#STEP_DATA='DATAl1loose2016__FatJetPreselCleaning_semilep_v2'
STEP_DATA="DATAl1loose2016__FatJetPreselCleaning_semilep_v2__wlepMaker"
#STEP_DATA='DATAl1loose2016'

#STEP="MCl1loose2016__MCCorr2016__FatJetPreselCleaningWlep_semilep"
directory=treeBaseDir+CAMPAIGN+'/'+STEP

Nlep='1'

#eleWP='cut_WP_Tight80X'
eleWP='mva_90p_Iso2016'
muWP='cut_Tight80x'



LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'

LepWPweight='(((Lepton_isTightElectron_'+eleWP+'[0]>0.5)*(Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]'+')) || ((Lepton_isTightMuon_'+muWP+'[0]>0.5)*(Lepton_tightMuon_'+muWP+'_IdIsoSF'+'[0]'+')))'
XSWeight      = 'XSWeight'
#SFweight      = 'SFweight'+Nlep+'l*'+LepWPweight+'*'+LepWPCut
#SFweight = 'puWeight*\
#TriggerEffWeight_1l*\
#Lepton_RecoSF[0]*\
#EMTFbug_veto'

SFweight = 'puWeight*\
TriggerEffWeight_1l*\
Lepton_RecoSF[0]*\
EMTFbug_veto'

#GenLepMatch   = 'GenLepMatch'+Nlep+'l'
GenLepMatch = 'Lepton_genmatched[0]'


if Nlep == '2' :
  fakeW = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP
else:
  fakeW = 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l'

################################################
############### B-Tag  WP ######################
################################################
btagSF='btagWeight_CSVV2'


#btagSF="( TMath::Exp(Sum$( TMath::Log( (Jet_pt>20 && Jet_pt<30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || CleanJet_pt>30 || abs(CleanJet_eta)>2.5) ) ) ) )"

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
            ['B','Run2016B-Nano14Dec2018_ver2-v1'] ,
            ['C','Run2016C-Nano14Dec2018-v1'] ,
            ['D','Run2016D-Nano14Dec2018-v1'] ,
            ['E','Run2016E-Nano14Dec2018-v1'] ,
            ['F','Run2016F-Nano14Dec2018-v1'] ,
            ['G','Run2016G-Nano14Dec2018-v1'] ,
            ['H','Run2016H-Nano14Dec2018-v1'] ,
          ]

DataSets = ['SingleMuon',\
'SingleElectron'
]

DataTrig = {
            'SingleMuon'     : 'Trigger_sngMu' ,
            'SingleElectron' : 'Trigger_sngEl' ,
           }

###########################################
############### SIGNAL ####################
###########################################


samples['ggHWWlnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M125',False,'nanoLatino_'),
                               'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+LepWPweight,
                               #'weight' : XSWeight,
                               'FilesPerJob' : 5,
}


samples['ggHWWlnuqq_M700'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M700',False,'nanoLatino_'),
                               'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+LepWPweight,
                               #'weight' : XSWeight,                                                                                         
                               'FilesPerJob' : 5,
}
samples['ggHWWlnuqq_M4000'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M4000',False,'nanoLatino_'),
                               'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+LepWPweight,
                               #'weight' : XSWeight,                                                                                         
                               'FilesPerJob' : 5,
}
samples['ggHWWlnuqq_M5000'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M5000',False,'nanoLatino_'),
                               'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+LepWPweight,
                               #'weight' : XSWeight,                                                                                         
                               'FilesPerJob' : 5,
}


###########################################                                                                                                  
#############  BACKGROUNDS  ###############                                                                                                  
###########################################                                                                                                  

samples['Wjets'] = {    'name'   :   getSampleFiles(directory,'WJetsToLNu',False,'nanoLatino_')
          + getSampleFiles(directory,'WJetsToLNu_ext2',False,'nanoLatino_'),
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+LepWPweight ,
                        'FilesPerJob' : 5,
                 }

samples['DY'] = {    'name'   :   getSampleFiles(directory,'DYJetsToLL_M-10to50',False,'nanoLatino_')
                                + getSampleFiles(directory,'DYJetsToLL_M-50_ext2',False,'nanoLatino_'),
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+LepWPweight ,
                     'FilesPerJob' : 5,
                 }

samples['top'] = {    'name'   :   getSampleFiles(directory,'TTToSemiLeptonic',False,'nanoLatino_')
                                 + getSampleFiles(directory,'ST_s-channel',False,'nanoLatino_')
                                 + getSampleFiles(directory,'ST_t-channel_antitop',False,'nanoLatino_')
                                 + getSampleFiles(directory,'ST_t-channel_top',False,'nanoLatino_')
                                 + getSampleFiles(directory,'ST_tW_antitop',False,'nanoLatino_')
                                 + getSampleFiles(directory,'ST_tW_top',False,'nanoLatino_') ,
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+LepWPweight ,
                      'FilesPerJob' : 5,
                 }

samples['WWToLNuQQ'] = {    'name'   :   getSampleFiles(directory,'WWToLNuQQ',False,'nanoLatino_') ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+LepWPweight ,
                           # 'weight' : XSWeight,
                 }
#def getEventSumw(directory,sample,prefix):

Wjets_w1=str(getEventSumw(directory,'WJetsToLNu','nanoLatino_'))
Wjets_w2=str(getEventSumw(directory,'WJetsToLNu_ext2','nanoLatino_'))
Wjets_totalw=str(float(Wjets_w1)+float(Wjets_w2))
print "Wjets_w1="+Wjets_w1
print "Wjets_w2="+Wjets_w2
print "Wjets_totalw="+Wjets_totalw
addSampleWeight(samples,'Wjets','WJetsToLNu',Wjets_w1+"/"+Wjets_totalw)
addSampleWeight(samples,'Wjets','WJetsToLNu_ext2',Wjets_w2+"/"+Wjets_totalw)




###########################################                                                                                                  
################## DATA ###################                                                                                                  
###########################################                                                                                                  



samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut ,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 20,
                  }

print samples['DATA']
#print "[jhchoi]@@@samples['DATA']['weights'] bf appending="+str(samples['DATA']['weights'])


for Run in DataRun :
        directory = treeBaseDir+CAMPAIGN_DATA+'/'+STEP_DATA
        for DataSet in DataSets :
                FileTarget = getSampleFiles(directory,DataSet+'_'+Run[1],True,'nanoLatino_')
                for iFile in FileTarget:

                        #print(iFile)
                        
                        samples['DATA']['name'].append(iFile)
                        samples['DATA']['weights'].append(DataTrig[DataSet])
                        
