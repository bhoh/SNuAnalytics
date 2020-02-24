#-----Variable Deinition-----#


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
STEP="MCl1loose2017v5__MCCorr2017v5__Semilep2017__HMlnjjSelBWRew_Dev__HMlnjjVarsGen"


directory=treeBaseDir+CAMPAIGN+'/'+STEP



XSWeight      = 'XSWeight'
#SFweight      = 'SFweight'+Nlep+'l*'+LepWPweight+'*'+LepWPCut
#SFweight = 'puWeight*\
#TriggerEffWeight_1l*\
#Lepton_RecoSF[0]*\
#EMTFbug_veto'

eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'
LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepWPweight='(((Lepton_isTightElectron_'+eleWP+'[0]>0.5)*(Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]'+')) + ((Lepton_isTightMuon_'+muWP+'[0]>0.5)*(Lepton_tightMuon_'+muWP+'_IdIsoSF'+'[0]'+')))'
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


#SFweight=SFweight+'*'+btagSF

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

###########################################
############### SIGNAL ####################
###########################################


massesModelsFile = "massesModels.py"
if os.path.exists(massesModelsFile) :
  handle = open(massesModelsFile,'r')
  exec(handle)
  handle.close()
else:
  print "!!! ERROR file ", massesModelsFile, " does not exist."




# h125
samples['ggh125LNuQQ'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M125',False,'nanoLatino_')
      				     ,
                               'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                               #'weight' : XSWeight,
                               'FilesPerJob' : 20,
                             }
# h+ I(h125 +B) 
samples['ggh125lnjj_SI'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M125',False,'nanoLatino_')
      				     ,
                               'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                               #'weight' : XSWeight,
                               'FilesPerJob' : 20,
                             }
addSampleWeight(samples, 'ggh125lnjj_SI', 'GluGluHToWWToLNuQQ_M125'
                     , '(1+'+ 'I_sigXww125' +')')

# I(h125 +B) 
samples['ggh125LNuQQ_I'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M125',False,'nanoLatino_')
      				     ,
                               'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                               #'weight' : XSWeight,
                               'FilesPerJob' : 20,
                             }
addSampleWeight(samples, 'ggh125LNuQQ_I', 'GluGluHToWWToLNuQQ_M125', '(I_sigXww125)')

samples['ggWW'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M125',False,'nanoLatino_')
      				     ,
                               'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                               #'weight' : XSWeight,
                               'FilesPerJob' : 20,
                             }
addSampleWeight(samples, 'ggWW', 'GluGluHToWWToLNuQQ_M125', '(wwOVsig125)')

# h125
#samples['vbfh125LNuQQ'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M125',False,'nanoLatino_')
#      				     ,
#                               'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                               #'weight' : XSWeight,
#                               'FilesPerJob' : 20,
#                             }
## h+ I(h125 +B) 
#samples['vbfh125LNuQQ_SBI'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M125',False,'nanoLatino_')
#      				     ,
#                               'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                               #'weight' : XSWeight,
#                               'FilesPerJob' : 20,
#                             }
#addSampleWeight(samples, 'vbfh125LNuQQ_SBI', 'VBFHToWWToLNuQQ_M125', '(' +'1'+'+'+model_I_Bonly+ ')')
#
## I(h125 +B) 
#samples['vbfh125LNuQQ_I'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M125',False,'nanoLatino_')
#      				     ,
#                               'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                               #'weight' : XSWeight,
#                               'FilesPerJob' : 20,
#                             }
#addSampleWeight(samples, 'vbfh125LNuQQ_I', 'VBFHToWWToLNuQQ_M125', '(' +model_I_Bonly+ ')')
#
#
#
#
#
for MX in List_MX:
  mass = str(MX)
  # pole
  samples['ggHwwLnqq_M'+mass] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+mass,False,'nanoLatino_'),
                                 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                                 #'weight' : XSWeight,
                                 'FilesPerJob' : 20,
                               }

#  # signal, I, and ggWW : we don't need this at the moment
#  samples['ggHwwLnqq_SBI_ggWW_M'+mass] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+mass,False,'nanoLatino_')
#                                   ,
#                                 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                                 #'weight' : XSWeight,
#                                 'FilesPerJob' : 20,
#                               }
#  addSampleWeight(samples, 'ggHwwLnqq_SBI_ggWW_M'+mass, 'GluGluHToWWToLNuQQ_M'+mass, '('+ '1+' +model_I+ '+' + model_B +')')
#
  # H + I(Hh + HB)
  samples['ggHwwLnqq_SBI_M'+mass] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+mass,False,'nanoLatino_')
					     ,
                                 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                                 #'weight' : XSWeight,
                                 'FilesPerJob' : 20,
                               }
  addSampleWeight(samples, 'ggHWWLNuQQ_SBI_M'+mass, 'GluGluHToWWToLNuQQ_M'+mass, '('+'1+' +'I_sigXh0_sigXww'+ ')')

  #  I(Hh + HB)
  samples['ggHWWLNuQQ_I_M'+mass] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+mass,False,'nanoLatino_')
#					     ,
#                                 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                                 #'weight' : XSWeight,
#                                 'FilesPerJob' : 20,
#                               }
#  addSampleWeight(samples, 'ggHWWLNuQQ_I_M'+mass, 'GluGluHToWWToLNuQQ_M'+mass, '('+model_I+ ')')
#
#
#
#
#  # I(HB)
#  samples['ggHWWLNuQQ_I_B_M'+mass] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+mass,False,'nanoLatino_'),
#                                 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                                 #'weight' : XSWeight,
#                                 'FilesPerJob' : 20,
#                               }
#  addSampleWeight(samples, 'ggHWWLNuQQ_I_B_M'+mass, 'GluGluHToWWToLNuQQ_M'+mass, '(' +model_I_Bonly+ ')')
#
#  # I(Hh)
#  samples['ggHWWLNuQQ_I_h_M'+mass] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+mass,False,'nanoLatino_'),
#                                 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                                 #'weight' : XSWeight,
#                                 'FilesPerJob' : 20,
#                               }
#  addSampleWeight(samples, 'ggHWWLNuQQ_I_h_M'+mass, 'GluGluHToWWToLNuQQ_M'+mass, '(' +model_I_Honly+ ')')
#
#
#  # ggWW from the ratio to ggHWW
#  samples['ggWWLNuQQ_M'+mass] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+mass,False,'nanoLatino_'),
#                                 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                                 #'weight' : XSWeight,
#                                 'FilesPerJob' : 20,
#                               }
#  addSampleWeight(samples, 'ggWWLNuQQ_M'+mass, 'GluGluHToWWToLNuQQ_M'+mass, '(' +model_B+ ')')
#
## VBF ################################################################
#
#  # pole
#  samples['vbfHWWLNuQQ_M'+mass] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+mass,False,'nanoLatino_'),
#                                 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                                 #'weight' : XSWeight,
#                                 'FilesPerJob' : 20,
#                               }
#
#  # signal, I, and WW
#  samples['vbfHWWLNuQQ_SBI_WW_M'+mass] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+mass,False,'nanoLatino_')
#                                   ,
#                                 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                                 #'weight' : XSWeight,
#                                 'FilesPerJob' : 20,
#                               }
#  addSampleWeight(samples, 'vbfHWWLNuQQ_SBI_WW_M'+mass, 'VBFHToWWToLNuQQ_M'+mass, '('+ '1+' +model_I+ '+' + model_B + ')')
#
#  # H + I(Hh + HB)
#  samples['vbfHWWLNuQQ_SBI_M'+mass] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+mass,False,'nanoLatino_')
#					     ,
#                                 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                                 #'weight' : XSWeight,
#                                 'FilesPerJob' : 20,
#                               }
#  addSampleWeight(samples, 'vbfHWWLNuQQ_SBI_M'+mass, 'VBFHToWWToLNuQQ_M'+mass, '('+'1+' +model_I+ ')')
#
#  # I(Hh + HB)
#  samples['vbfHWWLNuQQ_I_M'+mass] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+mass,False,'nanoLatino_')
#					     ,
#                                 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                                 #'weight' : XSWeight,
#                                 'FilesPerJob' : 20,
#                               }
#  addSampleWeight(samples, 'vbfHWWLNuQQ_I_M'+mass, 'VBFHToWWToLNuQQ_M'+mass, '('+model_I+ ')')
#
#
#
#  # I(HB)
#  samples['vbfHWWLNuQQ_I_B_M'+mass] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+mass,False,'nanoLatino_'),
#                                 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                                 #'weight' : XSWeight,
#                                 'FilesPerJob' : 20,
#                               }
#  addSampleWeight(samples, 'vbfHWWLNuQQ_I_B_M'+mass, 'VBFHToWWToLNuQQ_M'+mass, '(' +model_I_Bonly+ ')')
#
#  # I(Hh)
#  samples['vbfHWWLNuQQ_I_h_M'+mass] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+mass,False,'nanoLatino_'),
#                                 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                                 #'weight' : XSWeight,
#                                 'FilesPerJob' : 20,
#                               }
#  addSampleWeight(samples, 'vbfHWWLNuQQ_I_h_M'+mass, 'VBFHToWWToLNuQQ_M'+mass, '(' +model_I_Honly+ ')')
#
#
#  # WW from the ratio to vbfHWW
#  samples['WWLNuQQ_M'+mass] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+mass,False,'nanoLatino_'),
#                                 'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
#                                 #'weight' : XSWeight,
#                                 'FilesPerJob' : 20,
#                               }
#  addSampleWeight(samples, 'WWLNuQQ_M'+mass, 'VBFHToWWToLNuQQ_M'+mass, '(' +model_B+ ')')
#
#
#
#
############################################
################ BackGround ################
############################################
##
#samples['WW-LO'] = {    'name'   :   getSampleFiles(directory,'WW-LO',False,'nanoLatino_') ,
#                            'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
#                 }
#
#
#
