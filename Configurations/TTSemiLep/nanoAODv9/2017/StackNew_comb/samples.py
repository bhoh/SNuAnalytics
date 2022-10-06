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
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv9/2017/StackNew_comb"
  sys.path.append(BASE_PATH)
  from WPandCut2017 import *

samples={}

scriptname=opt.samplesFile

SITE=os.uname()[1]
xrootdPath=''
if    'iihe' in SITE :
  xrootdPath  = 'dcap://maite.iihe.ac.be/'
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/'
elif  'cern' in SITE :
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'

elif  'sdfarm' in SITE:
  xrootdPath = 'root://cms-xrdr.private.lo:2094'
  treeBaseDir = "/xrootd/store/user/bhoh/Latino/HWWNano/"

include_mva = False

CAMPAIGN='Summer20UL17_106x_nAODv9_Full2017v9'
#STEP="MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr__kinFitTTSemiLep_2017"
#STEP="CHToCBLepton2017v7__CHToCBJetMETCorr2017v7"
if include_mva:
  STEP="CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017__mvaCHToCB_2017"
else:
  STEP="CHToCBLepton2017v9__CHToCBJetMETCorr2017v9__kinFitTTSemiLepV5"


CAMPAIGN_DATA='Run2017_UL2017_nAODv9_Full2017v9'
#STEP_DATA="DATAl1loose2017v7__CHToCBJetMETCorr_data__kinFitTTSemiLep_2017"
#STEP_DATA="DATACHToCBLepton2017v7__CHToCBJetMETCorr_data"

if include_mva:
  STEP_DATA="DATACHToCBLepton2017v7__CHToCBJetMETCorr_data__kinFitTTSemiLepV4_2017__mvaCHToCB_2017"
else:
  STEP_DATA="DATACHToCBLepton2017v9__CHToCBJetMETCorr_data__kinFitTTSemiLepV5"

#directory=treeBaseDir+CAMPAIGN+'/'+STEP
directory=xrootdPath+'//xrd/store/user/bhoh/Latino/HWWNano/'+CAMPAIGN+'/'+STEP


def makeMCDirectory(var=''):
   if var=='':
       return xrootdPath+'//xrd/store/user/bhoh/Latino/HWWNano/'+CAMPAIGN+'/'+STEP
   else:
       return xrootdPath+'//xrd/store/user/bhoh/Latino/HWWNano/'+CAMPAIGN+'/'+STEP + "{var}".format(var=var)

def makeMCDirectory_mva(var):
  campaign_dir = xrootdPath+'//xrd/store/user/bhoh/Latino/HWWNano/'+CAMPAIGN
  split_STEPs = STEP.split('__')
  STEP_new = '__'.join(split_STEPs[:-1])
  print(STEP_new)
  return campaign_dir+'/'+STEP_new + "{var}".format(var=var)




LepWPCut="((Sum$(Lepton_isTightElectron_{ELE_WP} && Lepton_triggmatched )>0.5 && {SNG_ELE_TRIG}>0.5) || (Sum$(Lepton_isTightMuon_{MU_WP} && Lepton_triggmatched )>0.5 && {SNG_MU_TRIG}>0.5))".format(ELE_WP=eleWP, MU_WP=muWP, SNG_ELE_TRIG='HLT_Ele35_WPTight_Gsf', SNG_MU_TRIG='HLT_IsoMu27')


#eleWPweight='((Lepton_isTightElectron_'+eleWP+'[0]>0.5)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]'+'))'
eleWPweight='((abs(Lepton_pdgId[0])==11)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]'+'))'
#eleWPweight='((abs(Lepton_pdgId[0])==11)*(Lepton_RecoSF'+'[0]'+'))'
#eleWPweight+='*(OTF_EleID_POGTight_SF)'
#eleWPweight+='*(TriggerEffWeight_1l)'

#muWPweight='((Lepton_isTightMuon_'+muWP+'[0]>0.5)*(Lepton_tightMuon_'+muWP+'_TotSF'+'[0]'+'))'
muWPweight='((abs(Lepton_pdgId[0])==13)*(Lepton_tightMuon_'+muWP+'_TotSF'+'[0]'+'))'
#muWPweight='((abs(Lepton_pdgId[0])==13)*(OTF_MuID_POGTight_SF*OTF_MuISO_SF))' 
#muWPweight+='*(TriggerEffWeight_1l)'

#LepWPweight='(%s + %s)'%(eleWPweight,muWPweight)
LepSFweight='((nLooseLep==1)*(%s + %s)+(nLooseLep==2)*Lepton_RecoSF[0]*Alt$(Lepton_RecoSF[1],0)*LepSF2l__ele_%s__mu_%s)'%(eleWPweight,muWPweight,eleWP,muWP)
LepTrigSFweight='Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)'

XSWeight = 'XSWeight'
SFweight = 'puWeight*\
L1PreFiringWeight_Nom\
'
SFweight=SFweight+'*'+LepWPCut+'*'+LepSFweight+'*'+LepTrigSFweight


#GenLepMatch = 'Lepton_genmatched[0]'
GenLepMatch = '1'
##GenLepMatch = 'Lepton_promptgenmatched[0]*Alt$(!Lepton_promptgenmatched[1], 1)'

#SFweight=SFweight+'*HEMweight'

################################################
############### B-Tag  WP ######################
################################################

#pfCombinedInclusiveSecondaryVertexV2BJetTags (CSV) algorithm [26] loose working point.
#SFweight=SFweight+'*btagSF*HEMweight'
SFweight=SFweight+'*btagSF'
SFweight=SFweight+'*btagSFNorm_top'

################################################
###############  PU ID SF  ######################
################################################

SFweight+="*Jet_PUID_SF_L[0]"

################################################
###############  N-1 SF  ######################
################################################
if '_noLeptonSF' in opt.pycfg:
  SFweight=SFweight+'/'+LepSFweight
elif '_noTrigSF' in opt.pycfg:
  SFweight=SFweight+'/'+LepTrigSFweight
elif '_noPreFireSF' in opt.pycfg:
  SFweight=SFweight+'/L1PreFiringWeight_Nom'
elif '_noPUweightSF' in opt.pycfg:
  SFweight=SFweight+'/puWeight'
elif '_noBtagSF' in opt.pycfg:
  SFweight=SFweight+'/btagSF/btagSFNorm_top'
elif '_noBtagNormSF' in opt.pycfg:
  SFweight=SFweight+'/btagSFNorm_top'
elif '_noPUjetIDSF' in opt.pycfg:
  SFweight=SFweight+'/Jet_PUID_SF_L[0]'
elif '_TopPtReweight' in opt.pycfg:
  Top_pTrw = ''
  SFweight=SFweight+'*'+Top_pTrw



################################################
############### TT specific SF  ################
################################################
#XXX
TTSFweight = '1.'
#TTSFweight = '1'
TTbj        = '(genTtbarId%100==51 || genTtbarId%100==52)'
TTbb       = '(genTtbarId%100>=53 && genTtbarId%100<=55)'
TTcc       = '(genTtbarId%100>=41 && genTtbarId%100<=45)'
TTjj       = '(!%s && !%s && !%s)'%(TTbj,TTbb,TTcc)
ttch       = '(1/364.35)'

################################################                                                                                             
############   MET  FILTERS  ###################                                                                                             
################################################                                                                                             

METFilter_MC   = 'METFilter_MC'

METFilter_DATA = 'METFilter_DATA'

################################################                                                                                             
############ DATA DECLARATION ##################                                                                                             
################################################ 
DataRun = [
    ['B','Run2017B-UL2017-v1'],
    ['C','Run2017C-UL2017-v1'],
    ['D','Run2017D-UL2017-v1'],
    ['E','Run2017E-UL2017-v1'],
    ['F','Run2017F-UL2017-v1']
]

DataSets = ['SingleMuon',\
'SingleElectron'
]
#DataSets = ['MuonEG','SingleMuon','SingleElectron','DoubleMuon', 'DoubleEG']

DataTrig = {
            'SingleMuon'     : 'HLT_IsoMu27',
            'SingleElectron' : '!HLT_IsoMu27 && HLT_Ele35_WPTight_Gsf',
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

samples['TTLJ'] = {    'name'   :   getSampleFiles(directory,'TTToSemiLeptonic',False,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+TTSFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                      #'FilesPerJob' : 4,
                      'FilesPerJob' : 1,
                      'subsamples': {
                          'jj' : TTjj,
                          'bb' : TTbb,
                          'bj' : TTbj,
                          'cc' : TTcc,
                      }
                    }


#name_TTLJ_TuneCP5Up = getSampleFiles(directory+'__splitTTSysts','TTToSemiLeptonic_TuneCP5Up',False,'nanoLatino_')
#name_TTLJ_TuneCP5Down = getSampleFiles(directory+'__splitTTSysts','TTToSemiLeptonic_TuneCP5Down',False,'nanoLatino_')
#name_TTLJ_hdampUp = getSampleFiles(directory+'__splitTTSysts','TTToSemiLeptonic_hdampUp',False,'nanoLatino_')
#name_TTLJ_hdampDown = getSampleFiles(directory+'__splitTTSysts','TTToSemiLeptonic_hdampDown',False,'nanoLatino_')
#name_TTLJ_mtopUp = getSampleFiles(directory+'__splitTTSysts','TTToSemiLeptonic_mtopUp',False,'nanoLatino_')
#name_TTLJ_mtopDown = getSampleFiles(directory+'__splitTTSysts','TTToSemiLeptonic_mtopDown',False,'nanoLatino_')



samples['TTLL'] = {    'name'   :   getSampleFiles(directory,'TTTo2L2Nu',False,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                      'FilesPerJob' : 1,
                      'subsamples': {
                          'jj' : TTjj,
                          'bb' : TTbb,
                          'bj' : TTbj,
                          'cc' : TTcc,
                      }
                    }

#name_TTLL_TuneCP5Up = getSampleFiles(directory+'__splitTTSysts','TTTo2L2Nu_TuneCP5Up',False,'nanoLatino_')
#name_TTLL_TuneCP5Down = getSampleFiles(directory+'__splitTTSysts','TTTo2L2Nu_TuneCP5Down',False,'nanoLatino_')
#name_TTLL_hdampUp = getSampleFiles(directory+'__splitTTSysts','TTTo2L2Nu_hdampUp',False,'nanoLatino_')
#name_TTLL_hdampDown = getSampleFiles(directory+'__splitTTSysts','TTTo2L2Nu_hdampDown',False,'nanoLatino_')
#name_TTLL_mtopUp = getSampleFiles(directory+'__splitTTSysts','TTTo2L2Nu_mtopUp',False,'nanoLatino_')
#name_TTLL_mtopDown = getSampleFiles(directory+'__splitTTSysts','TTTo2L2Nu_mtopDown',False,'nanoLatino_')

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
                        getSampleFiles(directory,'WJetsToLNu_LO',False,'nanoLatino_')
                        ,
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                        'FilesPerJob' : 10,
                 }


############ DY ############                                                                                                   
ptllDYW_NLO = '((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'


samples['DY'] = {    'name'   :   getSampleFiles(directory,'DYJetsToLL_M-50_LO',False,'nanoLatino_'),
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                     #'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+ptllDYW_LO,
                     'FilesPerJob' : 10,
}

##--QCD
samples['QCD'] = {   'name'   :   getSampleFiles(directory,'QCD_bEnriched_HT100to200',False,'nanoLatino_')
                      + getSampleFiles(directory,'QCD_bEnriched_HT200to300',False,'nanoLatino_')
                      + getSampleFiles(directory,'QCD_bEnriched_HT300to500',False,'nanoLatino_')
                      + getSampleFiles(directory,'QCD_bEnriched_HT500to700',False,'nanoLatino_')
                      + getSampleFiles(directory,'QCD_bEnriched_HT700to1000',False,'nanoLatino_')
                      + getSampleFiles(directory,'QCD_bEnriched_HT1000to1500',False,'nanoLatino_')
                      + getSampleFiles(directory,'QCD_bEnriched_HT1500to2000',False,'nanoLatino_')
                      + getSampleFiles(directory,'QCD_bEnriched_HT2000toInf',False,'nanoLatino_')
                      ,
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                     #'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+ptllDYW_LO,
                     'FilesPerJob' : 100,
}
##--MultiBoson
samples['WW'] = {    'name'   :   getSampleFiles(directory,'WW',False,'nanoLatino_') ,
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
samples['TTZjets'] = {    'name'   :   getSampleFiles(directory,'TTZToLLNuNu_M-10',False,'nanoLatino_')
                                       +getSampleFiles(directory,'TTZToQQ',False,'nanoLatino_')
                                       ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                     'FilesPerJob' : 1,                 
                 }
samples['TTWjets'] = {    'name'   :   getSampleFiles(directory,'TTWJetsToQQ',False,'nanoLatino_') 
                                       +getSampleFiles(directory,'TTWJetsToLNu',False,'nanoLatino_')
                                       ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                     'FilesPerJob' : 1,                 
                 }

samples['ttH'] = {'name'   :
                  getSampleFiles(directory,'ttHToNonbb_M125',False,'nanoLatino_')
                  +getSampleFiles(directory,'ttHTobb_M125',False,'nanoLatino_')
                  ,
                  'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                  'FilesPerJob' : 1,
}

# CHToCB signal
for mass in ['075','080','085','090','100','110','120','130','140','150', '160']:
#for mass in ['075','080','085','090','100','110','120','130','150']:
    sample_name = 'CHToCB_M{0}'.format(mass) 
    samples[sample_name] = { 'name'    : getSampleFiles(directory,sample_name,False,'nanoLatino_'),
                                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+ttch,
                                     'FilesPerJob' : 50,
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
        directory = xrootdPath+'//xrd/store/user/bhoh/Latino/HWWNano/'+CAMPAIGN_DATA+'/'+STEP_DATA
        for DataSet in DataSets :
                FileTarget = getSampleFiles(directory,DataSet+'_'+Run[1],True,'nanoLatino_')
                for iFile in FileTarget:

                        #print(iFile)
                        
                        samples['DATA']['name'].append(iFile)
                        samples['DATA']['weights'].append(DataTrig[DataSet])
                        
#del_keys = [ key for key in samples if 'DY' not in key ]
#for key in del_keys:
#  del samples[key]
