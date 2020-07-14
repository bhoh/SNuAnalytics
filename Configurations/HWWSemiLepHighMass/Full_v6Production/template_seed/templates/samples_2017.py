FilesPerJob=30
FilesPerJobMainBKG=2
FilesPerJobDATA=60


import math
import os

import sys
sys.path.append(os.getcwd())


#-----Variable Deinition-----#
from WPandCut2017 import *
#from GetXsecInNtuple import GetXsecInNtuple
#------End of Variable Definition-----#

import glob
import copy
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *



samples={}



directory=treeBaseDir+CAMPAIGN+'/'+STEP

################################################                                                                                             
############ DATA DECLARATION ##################                                                                                             
################################################ 
DataRun = [
    ['B','Run2017B-Nano1June2019-v1'],
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
                                            # 'weight' : 'XSWeight*SFweight*METFilter_MC'+'*'+model+'_B'+'*'+cut,
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
  
samples['Wjets0j'] = {    'name'   :   
                          getSampleFiles(directory,'WJetsToLNu-0J',False,'nanoLatino_')
                          ,
                          'weight' : 'XSWeight*SFweight*METFilter_MC',
                          #'FilesPerJob' : 4,
                          'FilesPerJob' : FilesPerJobMainBKG,
                        }
samples['Wjets1j'] = {    'name'   :   
                          getSampleFiles(directory,'WJetsToLNu-1J',False,'nanoLatino_')
                          ,
                          'weight' : 'XSWeight*SFweight*METFilter_MC',
                        #'FilesPerJob' : 4,
                          'FilesPerJob' : FilesPerJobMainBKG,
                        }
samples['Wjets2j'] = {    'name'   :   
                          getSampleFiles(directory,'WJetsToLNu-2J',False,'nanoLatino_')
                          ,
                          'weight' : 'XSWeight*SFweight*METFilter_MC',
                          #'FilesPerJob' : 4,
                          'FilesPerJob' : FilesPerJobMainBKG,
                        }
##https://indico.cern.ch/event/673253/contributions/2756806/attachments/1541203/2416962/20171016_VJetsXsecsUpdate_PH-GEN.pdf

addSampleWeight(samples, 'Wjets0j', 'WJetsToLNu-0J', kfactor['Wjets0j'])
addSampleWeight(samples, 'Wjets1j', 'WJetsToLNu-1J', kfactor['Wjets1j'])
addSampleWeight(samples, 'Wjets2j', 'WJetsToLNu-2J', kfactor['Wjets2j'])




############ DY ############                                                                                                   
ptllDYW_NLO = '((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'


samples['DY'] = {    'name'   :   getSampleFiles(directory,'DYJetsToLL_M-50',False,'nanoLatino_')
                     + getSampleFiles(directory,'DYJetsToLL_M-10to50-LO',False,'nanoLatino_'),
                     'weight' : 'XSWeight*SFweight*METFilter_MC',
                     #'FilesPerJob' : 10,
                     'FilesPerJob' : FilesPerJobMainBKG,
}
addSampleWeight(samples,'DY','DYJetsToLL_M-50',ptllDYW_NLO)
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)



samples['top'] = {    'name'   :   getSampleFiles(directory,'TTToSemiLeptonic',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_t-channel_top',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_t-channel_antitop',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_s-channel',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_tW_antitop',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_tW_top',False,'nanoLatino_')
                      #+ getSampleFiles(directory,'TTTo2L2Nu_PSWeights',False,'nanoLatino_') 
                      ,
                      'weight' : 'XSWeight*SFweight*METFilter_MC',
                      #'FilesPerJob' : 3,
                      'FilesPerJob' : FilesPerJobMainBKG,
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

QCD_MU=['QCD_Pt-15to20_MuEnrichedPt5',
        'QCD_Pt-20to30_MuEnrichedPt5',
        'QCD_Pt-30to50_MuEnrichedPt5',
        'QCD_Pt-50to80_MuEnrichedPt5',
        'QCD_Pt-80to120_MuEnrichedPt5',
        'QCD_Pt-120to170_MuEnrichedPt5',
        'QCD_Pt-170to300_MuEnrichedPt5',
        'QCD_Pt-300to470_MuEnrichedPt5',
        'QCD_Pt-470to600_MuEnrichedPt5',
        'QCD_Pt-600to800_MuEnrichedPt5',
        'QCD_Pt-800to1000_MuEnrichedPt5',
        'QCD_Pt-1000toInf_MuEnrichedPt5',
]
QCD_EM=[
  'QCD_Pt-20to30_EMEnriched',
  'QCD_Pt-30to50_EMEnriched',
  'QCD_Pt-50to80_EMEnriched',
  'QCD_Pt-80to120_EMEnriched',
  'QCD_Pt-120to170_EMEnriched',
  'QCD_Pt-170to300_EMEnriched',
  'QCD_Pt-300toInf_EMEnriched'
]
QCD_bcToE=[
  'QCD_Pt_20to30_bcToE',
  'QCD_Pt_30to80_bcToE',
  'QCD_Pt_80to170_bcToE',
  'QCD_Pt_170to250_bcToE',
  'QCD_Pt_250toInf_bcToE',
]
samples['QCD_MU'] = { 'name':[],
                      'weight' : 'XSWeight*SFweight*METFilter_MC', 
                      'FilesPerJob' : FilesPerJob,
                    }
samples['QCD_EM'] = { 'name':[],
                      'weight' : 'XSWeight*SFweight*METFilter_MC', 
                      'FilesPerJob' : FilesPerJob,
                    }
samples['QCD_bcToE'] = { 'name':[],
                         'weight' : 'XSWeight*SFweight*METFilter_MC', 
                         'FilesPerJob' : FilesPerJob,
                       }
for QCD in QCD_MU:
  samples['QCD_MU']['name'] += getSampleFiles(directory,QCD,False,'nanoLatino_')
for QCD in QCD_EM:
  samples['QCD_EM']['name'] += getSampleFiles(directory,QCD,False,'nanoLatino_')
for QCD in QCD_bcToE:
  samples['QCD_bcToE']['name'] += getSampleFiles(directory,QCD,False,'nanoLatino_')


  
##--MultiBoson

samples['WW'] = {    'name'   :   getSampleFiles(directory,'WWToLNuQQ',False,'nanoLatino_') ,
                     'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom',
                     'FilesPerJob' : FilesPerJobMainBKG,                 
}##
##--diagram--##
#http://147.47.242.40/qqww/qqww.png
##--lhe record--##
##http://147.47.242.40/qqww/powheg_ww_event_record.png


samples['WWJJ'] = {    'name'   :   getSampleFiles(directory,'WpWmJJ_EWK_noTop',False,'nanoLatino_') ,
                      'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)',
                       'FilesPerJob' : FilesPerJob,                 
                     }


samples['WZ'] = {    'name'   :   getSampleFiles(directory,'WZ',False,'nanoLatino_') ,
                     'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom',
}

samples['ZZ'] = {    'name'   :   getSampleFiles(directory,'ZZ',False,'nanoLatino_') ,
                     'weight' : 'XSWeight*SFweight*METFilter_MC',
}


samples['WWW'] = {    'name'   :   getSampleFiles(directory,'WWW',False,'nanoLatino_') ,
                    'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom',
}

samples['WZZ'] = {    'name'   :   getSampleFiles(directory,'WZZ',False,'nanoLatino_') ,
                      'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom',
}
samples['ZZZ'] = {    'name'   :   getSampleFiles(directory,'ZZZ',False,'nanoLatino_') ,
                      'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom',
}

samples['WWZ'] = {    'name'   :   getSampleFiles(directory,'WWZ',False,'nanoLatino_') ,
                      'weight' : 'XSWeight*SFweight*METFilter_MC*WtaggerSFnom',
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




samples['ggHtautaulnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'GluGluHToTauTau_M125_newpmx',False,'nanoLatino_'),
                                   'weight' : 'XSWeight*SFweight*METFilter_MC',
                                   'FilesPerJob' : FilesPerJob,
}

samples['vbfHtautaulnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'VBFHToTauTau_M125',False,'nanoLatino_'),
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
samples['ZHtautaulnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'HZJ_HToTauTau_M125',False,'nanoLatino_'),
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


_directory=directory
for Run in DataRun :
  directory = treeBaseDir+CAMPAIGN_DATA+'/'+STEP_DATA
  for DataSet in DataSets :
    FileTarget = getSampleFiles(directory,DataSet+'_'+Run[1],True,'nanoLatino_')
    for iFile in FileTarget:
      
      #print(iFile)
      
      samples['DATA']['name'].append(iFile)
      samples['DATA']['weights'].append(DataTrig[DataSet])
      
      
      #if TESTRUN:
      #
      #  directory=_directory
      #  samples={}
      #  samples['ggHWWlnuqq_M400'] = {    'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M400',False,'nanoLatino_') ,
      #                        'weight' : 'XSWeight*SFweight*METFilter_MC' ,
      #  }
      
      
      
      
if CombineMultiV:
  samples['MultiV']={}
  for s in MultiV:
    if s in samples: 
      del samples[s]
if CombineWjets:
  samples['Wjets']={}
  for s in Wjets:
    if s in samples :
      del samples[s]
if CombineH125:
  samples['h125']={}
  for s in H125:
    if s in samples :
      del samples[s]
#print "--s list in samplepy---"
#for s in samples:
#  print s
