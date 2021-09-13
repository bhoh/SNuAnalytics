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
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv7/2016/StackNew_comb"
  sys.path.append(BASE_PATH)
  from WPandCut2016 import *

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
  treeBaseDir = "/xrootd/store/user/jhchoi/Latino/HWWNano/"

include_mva = False

CAMPAIGN='Summer16_102X_nAODv7_Full2016v7'
#STEP="MCl1loose2016v7__MCCorr2016v7__CHToCBLepton2016v7__CHToCBJetMETCorr__kinFitTTSemiLep_2016"
if include_mva:
  STEP="CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016__mvaCHToCB_2016"
else:
  STEP="CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016"
#STEP="MCl1loose2016v7__MCCorr2016v7"


CAMPAIGN_DATA='Run2016_102X_nAODv7_Full2016v7'
#STEP_DATA="DATAl1loose2016v7__DATACHToCBLepton2016v7__CHToCBJetMETCorr_data__kinFitTTSemiLep_2016"
if include_mva:
  STEP_DATA="DATACHToCBLepton2016v7__CHToCBJetMETCorr_data__kinFitTTSemiLepV4_2016__mvaCHToCB_2016"
else:
  STEP_DATA="DATACHToCBLepton2016v7__CHToCBJetMETCorr_data__kinFitTTSemiLepV4_2016"
#STEP_DATA="DATAl1loose2016v7"


#directory=treeBaseDir+CAMPAIGN+'/'+STEP
directory=xrootdPath+'//xrd/store/user/jhchoi/Latino/HWWNano/'+CAMPAIGN+'/'+STEP


def makeMCDirectory(var=''):
   if var=='':
       return xrootdPath+'//xrd/store/user/jhchoi/Latino/HWWNano/'+CAMPAIGN+'/'+STEP
   else:
       return xrootdPath+'//xrd/store/user/jhchoi/Latino/HWWNano/'+CAMPAIGN+'/'+STEP + "{var}".format(var=var)

def makeMCDirectory_mva(var):
  campaign_dir = xrootdPath+'//xrd/store/user/jhchoi/Latino/HWWNano/'+CAMPAIGN
  split_STEPs = STEP.split('__')
  STEP_new = '__'.join(split_STEPs[:-1])
  print(STEP_new)
  return campaign_dir+'/'+STEP_new + "{var}".format(var=var)



LepWPCut='(Lepton_isTightElectron_d0dz_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'

#eleWPweight='((Lepton_isTightElectron_d0dz_'+eleWP+'[0]>0.5)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]'+'))'
eleWPweight='((abs(Lepton_pdgId[0])==11)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]'+'))'
#eleWPweight='((abs(Lepton_pdgId[0])==11)*(Lepton_RecoSF'+'[0]'+'))'
#eleWPweight+='*Alt$(1/(Lepton_RecoSF'+'[0]'+'),1)'
#eleWPweight+='*(TriggerEffWeight_1l)'
eleWPweight+='*(HLT_Ele27_WPTight_Gsf==1)*(OTF_SingleEleTrig_SF)'
#eleWPweight+='*(HLT_Ele27_WPTight_Gsf==1)'

#muWPweight='((Lepton_isTightMuon_'+muWP+'[0]>0.5)*(Lepton_tightMuon_'+muWP+'_TotSF'+'[0]'+'))'
muWPweight='((abs(Lepton_pdgId[0])==13)*(Lepton_tightMuon_'+muWP+'_TotSF'+'[0]'+'))'
#muWPweight+='*(TriggerEffWeight_1l)'
muWPweight+='*(OTF_SingleMuTrig_SF)'
muWPweight+='*(Trigger_sngMu>0.5)'


#LepWPweight='((nLepton==1)*(%s + %s)+(nLepton>=2)*TriggerEffWeight_2l*Lepton_RecoSF[0]*Alt$(Lepton_RecoSF[1],0)*LepSF2l__ele_%s__mu_%s)'%(eleWPweight,muWPweight,eleWP,muWP)
#LepWPweight='(%s + %s)'%(eleWPweight,muWPweight)

# if there's a second lepton below veto lepton cut, but pass the double lepton trigger, it can cause a deviation.
LepWPweight='((nLooseLep==1)*(%s + %s)+(nLooseLep==2)*(HLT_Ele27_WPTight_Gsf==1 || Trigger_sngMu==1)*Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)*Lepton_RecoSF[0]*Alt$(Lepton_RecoSF[1],0)*LepSF2l__ele_%s__mu_%s)'%(eleWPweight,muWPweight,eleWP,muWP)
XSWeight      = 'XSWeight'

SFweight = 'puWeight*\
PrefireWeight*\
EMTFbug_veto\
'
SFweight=SFweight+'*'+LepWPCut+'*'+LepWPweight

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


################################################
###############  PU ID SF  ######################
################################################

SFweight+="*Jet_PUID_SF_L[0]"
#XXX test
#SFweight+="*1"

################################################
############### TT specific SF  ################
################################################

TTSFweight_SemiLeptonic = '(btagSFNorm_top * (nLHELep_TT==1))'
TTSFweight_2L2Nu        = '(btagSFNorm_top * (nLHELep_TT==2))'
#TTSFweight_SemiLeptonic = '(nLHELep_TT==1)'
#TTSFweight_2L2Nu        = '(nLHELep_TT==2)'
TTbj        = '(genTtbarId%100==51 || genTtbarId%100==52)'
TTbb       = '(genTtbarId%100>=53 && genTtbarId%100<=55)'
TTcc       = '(genTtbarId%100>=41 && genTtbarId%100<=45)'
TTjj       = '(!%s && !%s && !%s)'%(TTbj,TTbb,TTcc)
ttch      = '(1/364.35)'

################################################                                                                                             
############   MET  FILTERS  ###################                                                                                             
################################################                                                                                             

METFilter_MC   = 'METFilter_MC'

METFilter_DATA = 'METFilter_DATA'

################################################                                                                                             
############ DATA DECLARATION ##################                                                                                             
################################################ 
DataRun = [
    ['B','Run2016B-02Apr2020_ver2-v1'],
    ['C','Run2016C-02Apr2020-v1'],
    ['D','Run2016D-02Apr2020-v1'],
    ['E','Run2016E-02Apr2020-v1'],
    ['F','Run2016F-02Apr2020-v1'],
    ['G','Run2016G-02Apr2020-v1'],
    ['H','Run2016H-02Apr2020-v1'],
]

DataSets = ['SingleMuon',\
'SingleElectron'
]

DataTrig = {
            'SingleMuon'     : 'Trigger_sngMu',
            'SingleElectron' : '!Trigger_sngMu && HLT_Ele27_WPTight_Gsf',
           }




#DataTrig = {
#    'MuonEG'         : 'Trigger_ElMu',
#    'SingleMuon'     : '!Trigger_ElMu && Trigger_sngMu',
#    'SingleElectron' : '!Trigger_ElMu && !Trigger_sngMu && Trigger_sngEl',
#    'DoubleMuon'     : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && Trigger_dblMu',
#    'DoubleEG'       : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && !Trigger_dblMu && Trigger_dblEl'
#}



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

samples['TTLJ'] = {    'name'   :   #getSampleFiles(directory,'TT_TuneCUETP8M2T4',False,'nanoLatino_'),
                                    getSampleFiles(directory,'TT_TuneCUETP8M2T4_PSweights',False,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+TTSFweight_SemiLeptonic+'*'+GenLepMatch+'*'+METFilter_MC,
                      #'FilesPerJob' : 4,
                      'FilesPerJob' : 1,
                      'subsamples': {
                          'jj' : TTjj,
                          'bb' : TTbb,
                          'bj' : TTbj,
                          'cc' : TTcc,
                      }

                    }


#samples['TTLJ+jj'] = {    'name'   :   getSampleFiles(directory,'TT_TuneCUETP8M2T4_PSweights',False,'nanoLatino_'),
#                      'weight' : XSWeight+'*'+SFweight+'*'+TTSFweight_SemiLeptonic+'*'+GenLepMatch+'*'+METFilter_MC+'*'+TTjj,
#                      #'FilesPerJob' : 4,
#                      'FilesPerJob' : 3,
#
#
#
#                    }
#
#
#samples['TTLJ+cc'] = {    'name'   :   getSampleFiles(directory,'TT_TuneCUETP8M2T4_PSweights',False,'nanoLatino_'),
#                      'weight' : XSWeight+'*'+SFweight+'*'+TTSFweight_SemiLeptonic+'*'+GenLepMatch+'*'+METFilter_MC+'*'+TTcc,
#                      #'FilesPerJob' : 4,
#                      'FilesPerJob' : 3,
#                    }
#
#
#samples['TTLJ+bj'] = {    'name'   :   getSampleFiles(directory,'TT_TuneCUETP8M2T4_PSweights',False,'nanoLatino_'),
#                      'weight' : XSWeight+'*'+SFweight+'*'+TTSFweight_SemiLeptonic+'*'+GenLepMatch+'*'+METFilter_MC+'*'+TTbj,
#                      #'FilesPerJob' : 4,
#                      'FilesPerJob' : 3,
#
#
#
#                    }
#
#
#samples['TTLJ+bb'] = {    'name'   :   getSampleFiles(directory,'TT_TuneCUETP8M2T4_PSweights',False,'nanoLatino_'),
#                      'weight' : XSWeight+'*'+SFweight+'*'+TTSFweight_SemiLeptonic+'*'+GenLepMatch+'*'+METFilter_MC+'*'+TTbb,
#                      #'FilesPerJob' : 4,
#                      'FilesPerJob' : 3,
#
#
#
#                    }

#name_TTLJ_TuneCUETP8M2T4Up = getSampleFiles(directory+'__splitTTSysts','TT_TuneCUETP8M2T4Up',False,'nanoLatino_')
#name_TTLJ_TuneCUETP8M2T4Down = getSampleFiles(directory+'__splitTTSysts','TT_TuneCUETP8M2T4Down',False,'nanoLatino_')
#name_TTLJ_hdampUp = getSampleFiles(directory+'__splitTTSysts','TT_hdampUp',False,'nanoLatino_')
#name_TTLJ_hdampDown = getSampleFiles(directory+'__splitTTSysts','TT_hdampDown',False,'nanoLatino_')
#name_TTLJ_mtopUp = getSampleFiles(directory+'__splitTTSysts','TT_mtopUp',False,'nanoLatino_')
#name_TTLJ_mtopDown = getSampleFiles(directory+'__splitTTSysts','TT_mtopDown',False,'nanoLatino_')



samples['TTLL'] = {    'name'   :   #getSampleFiles(directory,'TT_TuneCUETP8M2T4',False,'nanoLatino_'),
                                    getSampleFiles(directory,'TT_TuneCUETP8M2T4_PSweights',False,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+TTSFweight_2L2Nu+'*'+GenLepMatch+'*'+METFilter_MC,
                      'FilesPerJob' : 1,
                      'subsamples': {
                          'jj' : TTjj,
                          'bb' : TTbb,
                          'bj' : TTbj,
                          'cc' : TTcc,
                      }

                    }


#samples['TTLL+jj'] = {    'name'   :   getSampleFiles(directory,'TT_TuneCUETP8M2T4_PSweights',False,'nanoLatino_'),
#                      'weight' : XSWeight+'*'+SFweight+'*'+TTSFweight_2L2Nu+'*'+GenLepMatch+'*'+METFilter_MC+'*'+TTjj,
#                      'FilesPerJob' : 4,
#                    }
#samples['TTLL+bj'] = {    'name'   :   getSampleFiles(directory,'TT_TuneCUETP8M2T4_PSweights',False,'nanoLatino_'),
#                      'weight' : XSWeight+'*'+SFweight+'*'+TTSFweight_2L2Nu+'*'+GenLepMatch+'*'+METFilter_MC+'*'+TTbj,
#                      'FilesPerJob' : 4,
#                    }
#samples['TTLL+bb'] = {    'name'   :   getSampleFiles(directory,'TT_TuneCUETP8M2T4_PSweights',False,'nanoLatino_'),
#                      'weight' : XSWeight+'*'+SFweight+'*'+TTSFweight_2L2Nu+'*'+GenLepMatch+'*'+METFilter_MC+'*'+TTbb,
#                      'FilesPerJob' : 4,
#                    }
#samples['TTLL+cc'] = {    'name'   :   getSampleFiles(directory,'TT_TuneCUETP8M2T4_PSweights',False,'nanoLatino_'),
#                      'weight' : XSWeight+'*'+SFweight+'*'+TTSFweight_2L2Nu+'*'+GenLepMatch+'*'+METFilter_MC+'*'+TTcc,
#                      'FilesPerJob' : 4,
#                    }
#name_TTLL_TuneCUETP8M2T4Up = getSampleFiles(directory+'__splitTTSysts','TT_TuneCUETP8M2T4Up',False,'nanoLatino_')
#name_TTLL_TuneCUETP8M2T4Down = getSampleFiles(directory+'__splitTTSysts','TT_TuneCUETP8M2T4Down',False,'nanoLatino_')
#name_TTLL_hdampUp = getSampleFiles(directory+'__splitTTSysts','TT_hdampUp',False,'nanoLatino_')
#name_TTLL_hdampDown = getSampleFiles(directory+'__splitTTSysts','TT_hdampDown',False,'nanoLatino_')
#name_TTLL_mtopUp = getSampleFiles(directory+'__splitTTSysts','TT_mtopUp',False,'nanoLatino_')
#name_TTLL_mtopDown = getSampleFiles(directory+'__splitTTSysts','TT_mtopDown',False,'nanoLatino_')

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
                        getSampleFiles(directory,'WJetsToLNu_ext2',False,'nanoLatino_')
                        ,
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                        'FilesPerJob' : 2,
                 }

#addSampleWeight(samples, 'Wjets', 'WJetsToLNu-0J', '0.915')
#addSampleWeight(samples, 'Wjets', 'WJetsToLNu-1J', '0.915')
#addSampleWeight(samples, 'Wjets', 'WJetsToLNu-2J', '0.915')



############ DY ############                                                                                                   
ptllDYW_NLO = '((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'


samples['DY'] = {    'name'   :   getSampleFiles(directory,'DYJetsToLL_M-50-LO_ext2',False,'nanoLatino_')
                     + getSampleFiles(directory,'DYJetsToLL_M-10to50-LO',False,'nanoLatino_'),
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                     #'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+ptllDYW_LO,
                     'FilesPerJob' : 2,
}
#addSampleWeight(samples,'DY','DYJetsToLL_M-50',ptllDYW_NLO)
#addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)

                 

##--QCD
samples['QCD_MU'] = {    'name'   :   getSampleFiles(directory,'QCD_Pt-15to20_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-20toInf_MuEnrichedPt15',False,'nanoLatino_')

                      ,
                     'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(abs(Lepton_pdgId[0])==13)',
                     'FilesPerJob' : 100,
}


samples['QCD_EM'] = {'name'   :
                  #getSampleFiles(directory,'QCD_Pt-15to20_EMEnriched',False,'nanoLatino_')
                  getSampleFiles(directory,'QCD_Pt-20to30_EMEnriched',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt-30to50_EMEnriched_ext1',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt-50to80_EMEnriched_ext1',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt-80to120_EMEnriched_ext1',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt-120to170_EMEnriched_ext1',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt-170to300_EMEnriched',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt-300toInf_EMEnriched',False,'nanoLatino_')

                  ,
                  'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(abs(Lepton_pdgId[0])==11)',
                  'FilesPerJob' : 100,
}


samples['QCD_bcToE'] = {'name'   :
                  #getSampleFiles(directory,'QCD_Pt_20to30_bcToE',False,'nanoLatino_')
                  getSampleFiles(directory,'QCD_Pt_30to80_bcToE',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt_80to170_bcToE',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt_170to250_bcToE',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt_250toInf_bcToE',False,'nanoLatino_')
                  ,
                  'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(abs(Lepton_pdgId[0])==11)',
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
                     'FilesPerJob' : 1,                 
                 }
samples['TTWjets'] = {    'name'   :   getSampleFiles(directory,'TTWJetsToQQ',False,'nanoLatino_') 
                                       +getSampleFiles(directory,'TTWJetsToLNu_ext1',False,'nanoLatino_')
                                       ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                     'FilesPerJob' : 1,                 
                 }
samples['ttH'] = {    'name'   :   getSampleFiles(directory,'ttHToNonbb_M125',False,'nanoLatino_') 
                                       +getSampleFiles(directory,'ttHTobb_M125',False,'nanoLatino_')
                                       ,
                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                     'FilesPerJob' : 1,                 
                 }


# CHToCB signal
for mass in ['075','080','085','090','100','110','120','130','140','150','160']:
#for mass in ['075','080','085','090','100','110','120','130','150']:
    sample_name = 'CHToCB_M{0}'.format(mass) 
    samples[sample_name] = { 'name'    : getSampleFiles(directory,sample_name,False,'nanoLatino_'),
                                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+ttch,
                                     'FilesPerJob' : 1,
            }


samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut ,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 8,
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
                        
#del_keys = [ key for key in samples if 'DY' not in key ]
#for key in del_keys:
#  del samples[key]
