#-----Variable Deinition-----#                                                                                                                                                                                                                               \
                                                                                                                                                                                                                                                              




eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'

METtype='Puppi'

if METtype=='' or METtype=='PF':
    MET_pt='MET_pt'
    MET_phi='MET_phi'
    Wlep_px='Wlep_px_PF'
    Wlep_py='Wlep_py_PF'
    Wlep_pz='Wlep_pz_PF'
    Wlep_E='Wlep_E_PF'
    Wlep_pt='Wlep_pt_PF'
    Wlep_eta='Wlep_eta_PF'
    Wlep_phi='Wlep_phi_PF'
    Wlep_mass='Wlep_mass_PF'


else:
    MET_pt=METtype+'MET_pt'
    MET_phi=METtype+'MET_phi'
    Wlep_px='Wlep_px_'+METtype
    Wlep_py='Wlep_py_'+METtype
    Wlep_pz='Wlep_pz_'+METtype
    Wlep_E='Wlep_E_'+METtype
    Wlep_pt='Wlep_pt_'+METtype
    Wlep_eta='Wlep_eta_'+METtype
    Wlep_phi='Wlep_phi_'+METtype
    Wlep_mass='Wlep_mass_'+METtype


LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'

bAlgo='DeepB'
bWP='0.2219'

isbjet='(CleanJet_jetIdx[CleanJetNotFat_jetIdx]>0 && CleanJet_pt[CleanJetNotFat_jetIdx]>20 && fabs(CleanJet_eta[CleanJetNotFat_jetIdx]) < 2.4 && Jet_btag'+bAlgo+'[CleanJet_jetIdx[CleanJetNotFat_jetIdx]] > '+bWP+'  )'
nbjet='(Sum$'+isbjet+')'
btagSF_each='( '+isbjet+'*Alt$(Jet_btagSF_shape, 1) + !'+isbjet+'*1 )'
logbtagSF='(Sum$(  TMath::Log('+btagSF_each+')))'
btagSF='(TMath::Exp( '+logbtagSF+' ))'


ww_px_pow2=' pow(     Whad_pt*cos(Whad_phi)+'+Wlep_px+', 2    )'
ww_px='(     Whad_pt*cos(Whad_phi)+'+Wlep_px+')'
ww_py_pow2=' pow(     Whad_pt*cos(Whad_phi)+'+Wlep_py+', 2    )'
ww_py='(     Whad_pt*cos(Whad_phi)+'+Wlep_py+')'
ww_pz_pow2=' pow(     Whad_pt*cos(Whad_phi)+'+Wlep_pz+', 2    )'
ww_pz='(     Whad_pt*cos(Whad_phi)+'+Wlep_pz+')'
ww_E_pow2=' pow(     Whad_pt*cos(Whad_phi)+'+Wlep_E+', 2    )'
ww_E='(     Whad_pt*cos(Whad_phi)+'+Wlep_E+')'

mww = '( sqrt( '+ww_E_pow2+' - '+ww_px_pow2+' - '+ww_py_pow2+' -'+ww_pz_pow2+'    )     )'
ww_pt='( sqrt( '+ww_px_pow2+' + '+ww_py_pow2+'  )  )'
ww_phi = '(atan('+ww_py+'/'+ww_px+' ) )'
ww_eta=' ( asinh('+ww_pz+'/'+ww_pt+') )'

wlep_mt='(sqrt(pow('+Wlep_E+',2) - pow('+Wlep_pz+',2)  ))'
lvqq_mt='(sqrt('+ww_E_pow2+'-'+ww_pz_pow2+'))'

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
STEP="MCl1loose2017v5__MCCorr2017v5__Semilep2017"



CAMPAIGN_DATA='Run2017_102X_nAODv4_Full2017v5'
STEP_DATA="DATAl1loose2017v5__Semilep2017"


directory=treeBaseDir+CAMPAIGN+'/'+STEP




eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'



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
SFweight=SFweight+'*'+LepWPweight+'*'+LepWPCut

#GenLepMatch   = 'GenLepMatch'+Nlep+'l'
GenLepMatch = 'Lepton_genmatched[0]'

################################################
############### B-Tag  WP ######################
################################################


SFweight=SFweight+'*'+btagSF

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
            'SingleElectron' : 'Trigger_sngEl' ,
           }

###########################################
############### SIGNAL ####################
###########################################

List_MX=[125,200,210,230,250,300,350,400,500,550,600,650,700,750,800,900,1500,2000,2500,3000,4000,5000]
for MX in List_MX:

  samples['ggHWWlnuqq_M'+str(MX)] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                                 #'weight' : XSWeight,
                                 'FilesPerJob' : 5,
                               }




###########################################                                                                                                  
#############  BACKGROUNDS  ###############                                                                                                  
###########################################                                                                                                  

samples['Wjets'] = {    'name'   :   getSampleFiles(directory,'WJetsToLNu_HT100_200',False,'nanoLatino_')
                        + getSampleFiles(directory,'WJetsToLNu_HT200_400',False,'nanoLatino_')
                        + getSampleFiles(directory,'WJetsToLNu_HT400_600',False,'nanoLatino_')
                        + getSampleFiles(directory,'WJetsToLNu_HT600_800',False,'nanoLatino_')
                        + getSampleFiles(directory,'WJetsToLNu_HT800_1200',False,'nanoLatino_')
                        + getSampleFiles(directory,'WJetsToLNu_HT1200_2500',False,'nanoLatino_')
                        + getSampleFiles(directory,'WJetsToLNu_HT2500_inf',False,'nanoLatino_')
                        ,
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                        'FilesPerJob' : 5,
                 }


############ DY ############                                                                                                   
ptllDYW_NLO = '((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'


samples['DY'] = {    'name'   :   getSampleFiles(directory,'DYJetsToLL_M-50',False,'nanoLatino_')
                     + getSampleFiles(directory,'DYJetsToLL_M-10to50-LO',False,'nanoLatino_'),
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                     'FilesPerJob' : 5,
}
addSampleWeight(samples,'DY','DYJetsToLL_M-50',ptllDYW_NLO)
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)

                 

samples['top'] = {    'name'   :   getSampleFiles(directory,'TTToSemiLeptonic',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_t-channel_top',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_t-channel_antitop',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_tW_antitop',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_tW_top',False,'nanoLatino_') 
                      ,
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                      'FilesPerJob' : 5,
                    }

samples['VV'] = {    'name'   :   getSampleFiles(directory,'WZ',False,'nanoLatino_')
                      + getSampleFiles(directory,'ZZ',False,'nanoLatino_')
                     ,
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                     'FilesPerJob' : 5,
                    }

'''
samples['QCD'] = {    'name'   :   getSampleFiles(directory,'QCD_Pt-15to20_MuEnrichedPt5',False,'nanoLatino_')
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
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                     'FilesPerJob' : 5,
                    }
'''




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
                        
