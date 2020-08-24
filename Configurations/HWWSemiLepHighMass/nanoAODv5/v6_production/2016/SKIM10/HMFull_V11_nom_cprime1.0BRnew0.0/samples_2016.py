FilesPerJob=10
FilesPerJobMainBKG=2
FilesPerJobDATA=40

TESTRUN=False

import math
import os
import sys
sys.path.append(os.getcwd())

#-----Variable Deinition-----#
from WPandCut2016 import *

#------End of Variable Definition-----#



import glob
import copy
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *



samples={}





METFilter_MC   = 'METFilter_MC'

METFilter_DATA = 'METFilter_DATA'

################################################                                                                                             
############ DATA DECLARATION ##################                                                                                             
################################################ 
DataRun = [
    ['B','Run2016B-Nano1June2019_ver2-v1'],
    ['C','Run2016C-Nano1June2019-v1'],
    ['D','Run2016D-Nano1June2019-v1'],
    ['E','Run2016E-Nano1June2019-v1'],
    ['F','Run2016F-Nano1June2019-v1'],
    ['G','Run2016G-Nano1June2019-v1'],
    ['H','Run2016H-Nano1June2019-v1'],
]


DataSets = ['SingleMuon',\
'SingleElectron'
]

DataTrig = {
            'SingleMuon'     : 'Trigger_sngMu' ,
            'SingleElectron' : '!Trigger_sngMu && Trigger_sngEl' ,
           }


##--sig

import sys
sys.path.insert(0, "MassPoints")
from List_MX import *
from List_MX_VBF import *

##--Load kfactor--##
handle=open('kfactor/kfactor.py','r')
exec(handle)
handle.close()
##--Powheg NLO xsec
handle=open('kfactor/NormToPowheg.py','r')
exec(handle)
handle.close()
#from FilterMelaReweights import GetMinMaxCuts
handle=open('MELACUT/'+model+'.py')
exec(handle)
handle.close()

for MX in List_MX:

  cut=melaggf[MX]
  normS='('+kfactor['ggHWWlnuqq_M'+str(MX)]+')'
  normI='('+str(math.sqrt(float(kfactor['ggHWWlnuqq_M'+str(MX)])*float(NormToPowheg['ggHWWlnuqq_M'+str(MX)])))+')'
  normB='('+NormToPowheg['ggHWWlnuqq_M'+str(MX)]+')'

  samples['ggHWWlnuqq_M'+str(MX)+'_S'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                                 'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom'+'*'+model+'*'+normS+'*'+cut,
                                                 'FilesPerJob' : FilesPerJob,
                                               }

  samples['ggHWWlnuqq_M'+str(MX)+'_B'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                                 'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom'+'*'+model+'_B'+'*'+normB+'*'+cut,
                                                 'FilesPerJob' : FilesPerJob,
                                               }
  samples['ggHWWlnuqq_M'+str(MX)+'_SI'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                                 'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom'+'*('+model+'*'+normS+'+'+model+'_I'+'*'+normI+')*'+cut,
                                                 'FilesPerJob' : FilesPerJob,
                                               }



for MX in List_MX_VBF:
  cut=melavbf[MX]

  normS='('+kfactor['vbfHWWlnuqq_M'+str(MX)]+')'
  normI='('+str(math.sqrt(float(kfactor['vbfHWWlnuqq_M'+str(MX)])*float(NormToPowheg['vbfHWWlnuqq_M'+str(MX)])))+')'
  normB='('+NormToPowheg['vbfHWWlnuqq_M'+str(MX)]+')'
  samples['vbfHWWlnuqq_M'+str(MX)+'_S'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                            'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom'+'*'+model+'*'+normS+'*'+cut,
                                            # 'weight' : 'XSWeight*SFweight*METFilter_MC'+'*'+model+'*'+cut,
                                                 'FilesPerJob' : FilesPerJob,
                                               }
  samples['vbfHWWlnuqq_M'+str(MX)+'_B'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                            'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom'+'*'+model+'_B'+'*'+normB+'*'+cut,
                                            'FilesPerJob' : FilesPerJob,
  }
  samples['vbfHWWlnuqq_M'+str(MX)+'_SI'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                            'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom'+'*('+model+'*'+normS+'+'+model+'_I'+'*'+normI+')*'+cut,
                                            'FilesPerJob' : FilesPerJob,
  }




###########################################                                                                                                  
#############  BACKGROUNDS  ###############                                                                                                  
###########################################                                                                                                  

samples['Wjets'] = {    'name'   :   getSampleFiles(directory,'WJetsToLNu_ext2',False,'nanoLatino_'),
                        'weight' : 'XSWeight*SFweight*METFilter_MC',
                        'FilesPerJob' : FilesPerJobMainBKG,
                        #'EventsPerJob' : 100000,
                 }


############ DY ############                                                                                                   
ptllDYW_NLO = '((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'


samples['DY'] = {    'name'   :   getSampleFiles(directory,'DYJetsToLL_M-50-LO_ext2',False,'nanoLatino_')
                     + getSampleFiles(directory,'DYJetsToLL_M-10to50-LO',False,'nanoLatino_'),
                     'weight' : 'XSWeight*SFweight*METFilter_MC',
                     'FilesPerJob' : FilesPerJob,
}
#addSampleWeight(samples,'DY','DYJetsToLL_M-50',ptllDYW_NLO)
#addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)

                 

samples['top'] = {    'name'   :   getSampleFiles(directory,'TTToSemiLeptonic',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_t-channel_top',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_t-channel_antitop',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_s-channel',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_tW_antitop',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_tW_top',False,'nanoLatino_')
                      + getSampleFiles(directory,'TTTo2L2Nu',False,'nanoLatino_') 
                      ,
                      'weight' : 'XSWeight*SFweight*METFilter_MC',
                      'FilesPerJob' : FilesPerJobMainBKG,
                      #'EventsPerJob' : 100000,
                      #'FilesPerJob' : 40,
                    }
addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw*WtaggerSFnom')
addSampleWeight(samples,'top','ST_tW_antitop','WtaggerSFnom')
addSampleWeight(samples,'top','ST_tW_top','WtaggerSFnom')
addSampleWeight(samples,'top','ST_t-channel_top','WtaggerSFnom')
addSampleWeight(samples,'top','ST_t-channel_antitop','WtaggerSFnom')
addSampleWeight(samples,'top','ST_s-channel_antitop','WtaggerSFnom')


##--QCD
samples['QCD_MU'] = {    'name'   :   getSampleFiles(directory,'QCD_Pt-15to20_MuEnrichedPt5',False,'nanoLatino_')
                      +getSampleFiles(directory,'QCD_Pt-20toInf_MuEnrichedPt15',False,'nanoLatino_'),
                     'weight' : 'XSWeight*SFweight*METFilter_MC',
                     'FilesPerJob' : FilesPerJob,
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
                  'weight' : 'XSWeight*SFweight*METFilter_MC',
                  'FilesPerJob' : FilesPerJob,
}


samples['QCD_bcToE'] = {'name'   :
                  getSampleFiles(directory,'QCD_Pt_20to30_bcToE',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt_30to80_bcToE',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt_80to170_bcToE',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt_170to250_bcToE',False,'nanoLatino_')
                  +getSampleFiles(directory,'QCD_Pt_250toInf_bcToE',False,'nanoLatino_')
                  ,
                  'weight' : 'XSWeight*SFweight*METFilter_MC',
                  'FilesPerJob' : FilesPerJob,
}
##--MultiBoson
samples['WW'] = {    'name'   :   getSampleFiles(directory,'WWToLNuQQ',False,'nanoLatino_') ,
                     'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom',
                     'FilesPerJob' : FilesPerJob,                 
}



samples['WZ'] = {    'name'   :   getSampleFiles(directory,'WZ',False,'nanoLatino_') ,
                     'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom',
                 }

samples['ZZ'] = {    'name'   :   getSampleFiles(directory,'ZZ',False,'nanoLatino_') ,
                     'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom',
                 }


samples['WWW'] = {    'name'   :   getSampleFiles(directory,'WWW',False,'nanoLatino_') ,
                      'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom',
                 }

samples['WZZ'] = {    'name'   :   getSampleFiles(directory,'WZZ',False,'nanoLatino_') ,
                      'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom',
                 }
samples['ZZZ'] = {    'name'   :   getSampleFiles(directory,'ZZZ',False,'nanoLatino_') ,
                      'weight' : 'XSWeight*SFweight*METFilter_MC',
                 }

samples['WWZ'] = {    'name'   :   getSampleFiles(directory,'WWZ',False,'nanoLatino_') ,
                      'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom',
                 }

samples['WWJJ'] = {    'name'   :   getSampleFiles(directory,'WpWmJJ_EWK_noTop',False,'nanoLatino_') ,
                                         'weight' : 'XSWeight*SFweight*WtaggerSFnom*METFilter_MC*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)',
                                         'FilesPerJob' : FilesPerJob,
                                       }


samples['ggHWWlnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M125',False,'nanoLatino_'),
                               'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom',
                                    'FilesPerJob' : FilesPerJob,
                            }

samples['vbfHWWlnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M125',False,'nanoLatino_'),
                                'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom',
                                'FilesPerJob' : FilesPerJob,
                              }

samples['ZHWWlnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'HZJ_HToWW_M125',False,'nanoLatino_'),
                                'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom',
                                'FilesPerJob' : FilesPerJob,
                              }
samples['WpHWWlnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'HWplusJ_HToWW_M125',False,'nanoLatino_'),
                                'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom',
                                'FilesPerJob' : FilesPerJob,
                              }
samples['WmHWWlnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'HWminusJ_HToWW_M125',False,'nanoLatino_'),
                                'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom',
                          'FilesPerJob' : FilesPerJob,
                              }


samples['ggHtautaulnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'GluGluHToTauTau_M125',False,'nanoLatino_'),
                                'weight' : 'XSWeight*SFweight*METFilter_MC',
                                'FilesPerJob' : FilesPerJob,
                              }
samples['vbfHtautaulnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'VBFHToTauTau_M125',False,'nanoLatino_'),
                                'weight' : 'XSWeight*SFweight*METFilter_MC',
                                'FilesPerJob' : FilesPerJob,
                              }
samples['ZHtautaulnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'HZJ_HToTauTau_M125',False,'nanoLatino_'),
                                'weight' : 'XSWeight*SFweight*METFilter_MC',
                                'FilesPerJob' : FilesPerJob,
                              }
samples['WmHtautaulnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'HWminusJ_HToTauTau_M125',False,'nanoLatino_'),
                                'weight' : 'XSWeight*SFweight*METFilter_MC',
                                'FilesPerJob' : FilesPerJob,
                              }
samples['WpHtautaulnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'HWplusJ_HToTauTau_M125',False,'nanoLatino_'),
                                'weight' : 'XSWeight*SFweight*METFilter_MC',
                                'FilesPerJob' : FilesPerJob,
                              }


samples['DATA']  = {   'name': [ ] ,
                       'weight' : 'METFilter_DATA*LepWPCut' ,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : FilesPerJobDATA,
                  }

#print samples['DATA']



for Run in DataRun :
        directoryDATA = treeBaseDir+CAMPAIGN_DATA+'/'+STEP_DATA
        for DataSet in DataSets :
                FileTarget = getSampleFiles(directoryDATA,DataSet+'_'+Run[1],True,'nanoLatino_')
                for iFile in FileTarget:

                        #print(iFile)
                        
                        samples['DATA']['name'].append(iFile)
                        samples['DATA']['weights'].append(DataTrig[DataSet])
                        

if TESTRUN:
  samples={}
  samples['GluGluHToWWToLNuQQ_M400'] = {    'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M400',False,'nanoLatino_') ,
                        'weight' : 'XSWeight*SFweight*METFilter_MC'
                      }

if CombineMultiV:
  print "CombineMultiV=",CombineMultiV
  samples['MultiV']={}
  for s in MultiV:
    if s in samples:
      del samples[s]
if CombineH125:
  print "CombineH125=",CombineH125
  samples['h125']={}
  for s in H125:
    if s in samples:
      del samples[s]
  
