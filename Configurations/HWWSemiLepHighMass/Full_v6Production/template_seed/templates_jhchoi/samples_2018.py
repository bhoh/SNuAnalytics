#FilesPerJob=30
#FilesPerJobMainBKG=2
#FilesPerJobDATA=100


import os
import math
import sys
sys.path.append(os.getcwd())

#-----Variable Deinition-----#
from WPandCut2018 import *
#from GetXsecInNtuple import GetXsecInNtuple
#------End of Variable Definition-----#


import glob
import copy
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *



samples={}

SITE=os.uname()[1]

directory=treeBaseDir+CAMPAIGN+'/'+STEP



################################################                                                                                             
############ DATA DECLARATION ##################                                                                                             
################################################ 
DataRun = [
    ['A','Run2018A-Nano25Oct2019-v1'] ,
    ['B','Run2018B-Nano25Oct2019-v1'] ,
    ['C','Run2018C-Nano25Oct2019-v1'] ,
    ['D','Run2018D-Nano25Oct2019_ver2-v1'] ,

]

DataSets = ['SingleMuon',\
'EGamma'
]

DataTrig = {
            'SingleMuon'     : 'Trigger_sngMu' ,
            'EGamma' : 'Trigger_sngEl && !Trigger_sngMu' ,
           }



mcCommonWeight='XSWeight*SFweight*METFilter_MC'

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
  normI='(1)'
  normB='(1)'
  if PowhegNorm:
    normI='('+str(math.sqrt(float(kfactor['ggHWWlnuqq_M'+str(MX)])*float(NormToPowheg['ggHWWlnuqq_M'+str(MX)])))+')'
    normB='('+NormToPowheg['ggHWWlnuqq_M'+str(MX)]+')'


  samples['ggHWWlnuqq_M'+str(MX)+'_S'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                                 'weight' : mcCommonWeight+'*WtaggerSFnom'+'*'+model+'*'+normS+'*'+cut,
                                                 'FilesPerJob' : FilesPerJob,
                                               }

  samples['ggHWWlnuqq_M'+str(MX)+'_B'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                                 'weight' : mcCommonWeight+'*WtaggerSFnom'+'*'+model+'_B'+'*'+normB+'*'+cut,
                                                 'FilesPerJob' : FilesPerJob,
                                               }

  samples['ggHWWlnuqq_M'+str(MX)+'_SI'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                                 'weight' : mcCommonWeight+'*WtaggerSFnom'+'*('+model+'*'+normS+'+'+model+'_I'+'*'+normI+')*'+cut,
                                                 'FilesPerJob' : FilesPerJob,
                                               }




for MX in List_MX_VBF:
  cut=melavbf[MX]

  normS='('+kfactor['vbfHWWlnuqq_M'+str(MX)]+')'
  normI='(1)'
  normB='(1)'
  if PowhegNorm:
    normI='('+str(math.sqrt(float(kfactor['vbfHWWlnuqq_M'+str(MX)])*float(NormToPowheg['vbfHWWlnuqq_M'+str(MX)])))+')'
    normB='('+NormToPowheg['vbfHWWlnuqq_M'+str(MX)]+')'
  samples['vbfHWWlnuqq_M'+str(MX)+'_S'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                            'weight' : mcCommonWeight+'*WtaggerSFnom'+'*'+model+'*'+normS+'*'+cut,
                                            # 'weight' : mcCommonWeight+'*'+model+'*'+cut,
                                            'FilesPerJob' : FilesPerJob,
                                               }
  samples['vbfHWWlnuqq_M'+str(MX)+'_B'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                            'weight' : mcCommonWeight+'*WtaggerSFnom'+'*'+model+'_B'+'*'+normB+'*'+cut,
                                            'FilesPerJob' : FilesPerJob,
  }
  samples['vbfHWWlnuqq_M'+str(MX)+'_SI'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),
                                            'weight' : mcCommonWeight+'*WtaggerSFnom'+'*('+model+'*'+normS+'+'+model+'_I'+'*'+normI+')*'+cut,
                                            'FilesPerJob' : FilesPerJob,
  }





samples['Wjets0j'] = {    'name'   :
                          getSampleFiles(directory,'WJetsToLNu-0J',False,'nanoLatino_'),
                          'weight' : mcCommonWeight,
                          'FilesPerJob' : FilesPerJobMainBKG,

}
samples['Wjets1j'] = {    'name'   :
                          getSampleFiles(directory,'WJetsToLNu-1J',False,'nanoLatino_'),
                          'weight' : mcCommonWeight,
                          'FilesPerJob' : FilesPerJobMainBKG,
}
samples['Wjets2j'] = {    'name'   :
                          getSampleFiles(directory,'WJetsToLNu-2J',False,'nanoLatino_'),
                          'weight' : mcCommonWeight,
                          'FilesPerJob' : FilesPerJobMainBKG,
}

addSampleWeight(samples, 'Wjets0j', 'WJetsToLNu-0J', kfactor['Wjets0j'])
addSampleWeight(samples, 'Wjets1j', 'WJetsToLNu-1J', kfactor['Wjets1j'])
addSampleWeight(samples, 'Wjets2j', 'WJetsToLNu-2J', kfactor['Wjets2j'])

addSampleWeight(samples, 'Wjets0j', 'WJetsToLNu_0J', 'MjjShape')
addSampleWeight(samples, 'Wjets1j', 'WJetsToLNu_1J', 'MjjShape')
addSampleWeight(samples, 'Wjets2j', 'WJetsToLNu_2J', 'MjjShape')



############ DY ############                                                                                                   
ptllDYW_NLO = '((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'


samples['DY'] = {    'name'   :   getSampleFiles(directory,'DYJetsToLL_M-50-LO',False,'nanoLatino_')
                     + getSampleFiles(directory,'DYJetsToLL_M-10to50-LO',False,'nanoLatino_'),
                     'weight' : mcCommonWeight,
                     'FilesPerJob' : FilesPerJobMainBKG,
}
addSampleWeight(samples,'DY','DYJetsToLL_M-50',ptllDYW_LO)
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)

                 

samples['top'] = {    'name'   :   getSampleFiles(directory,'TTToSemiLeptonic_ext3',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_t-channel_top',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_t-channel_antitop',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_s-channel_ext1',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_tW_antitop_ext1',False,'nanoLatino_')
                      + getSampleFiles(directory,'ST_tW_top_ext1',False,'nanoLatino_')
                      + getSampleFiles(directory,'TTTo2L2Nu',False,'nanoLatino_') 
                      ,
                      'weight' : mcCommonWeight,
                      'FilesPerJob' : FilesPerJobMainBKG,
                      #'FilesPerJob' : 40,
                    }
addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic_ext3','Top_pTrw')
addSampleWeight(samples,'top','ST_tW_antitop_ext1','WtaggerSFnom')
addSampleWeight(samples,'top','ST_tW_top_ext1','WtaggerSFnom')
addSampleWeight(samples,'top','ST_t-channel_top','WtaggerSFnom')
addSampleWeight(samples,'top','ST_t-channel_antitop','WtaggerSFnom')
addSampleWeight(samples,'top','ST_s-channel_ext1','WtaggerSFnom')

##--QCD


if not DIVIDEQCD:
  samples['QCD'] = { 'name':[],
                   'weight' : mcCommonWeight+'*('+mcCommonWeight+'<150)',
                     'FilesPerJob' : FilesPerJob,
  }

  for QCD in QCD_MU+QCD_EM+QCD_bcToE:
    samples['QCD']['name'] += getSampleFiles(directory,QCD,False,'nanoLatino_')
    
  for QCD in QCD_MU:
    addSampleWeight(samples,'QCD',QCD,'(abs(Lepton_pdgId[0])==13)')
    addSampleWeight(samples,'QCD',QCD,kfactor[QCD])
  for QCD in QCD_EM:
    addSampleWeight(samples,'QCD',QCD,'(abs(Lepton_pdgId[0])==11)')
    addSampleWeight(samples,'QCD',QCD,kfactor[QCD])
  for QCD in QCD_bcToE:
    addSampleWeight(samples,'QCD',QCD,'(abs(Lepton_pdgId[0])==11)')

else:
  for QCD in QCD_MU+QCD_EM+QCD_bcToE:
    samples[QCD] = { 'name':[],
                     'weight' : mcCommonWeight+'*('+mcCommonWeight+'<150)',
                     'FilesPerJob' : FilesPerJob,
                   }

  for QCD in QCD_MU+QCD_EM+QCD_bcToE:
    samples[QCD]['name'] += getSampleFiles(directory,QCD,False,'nanoLatino_')
    
  for QCD in QCD_MU:
    addSampleWeight(samples,QCD,QCD,'(abs(Lepton_pdgId[0])==13)')
    addSampleWeight(samples,QCD,QCD,kfactor[QCD])
  for QCD in QCD_EM:
    addSampleWeight(samples,QCD,QCD,'(abs(Lepton_pdgId[0])==11)')
    addSampleWeight(samples,QCD,QCD,kfactor[QCD])
  for QCD in QCD_bcToE:
    addSampleWeight(samples,QCD,QCD,'(abs(Lepton_pdgId[0])==11)')




##--MultiBoson
samples['WW'] = {    'name'   :   getSampleFiles(directory,'WWToLNuQQ',False,'nanoLatino_') ,
                     'weight' : mcCommonWeight+'*WtaggerSFnom*(Sum$(GenJet_pt > 30) <= 3 )',
                     'FilesPerJob' : FilesPerJobMainBKG,                 
}

samples['qqWWqq'] = {    'name'   :   getSampleFiles(directory,'WpToLNu_WmTo2J_QCD',False,'nanoLatino_')
                       +getSampleFiles(directory,'WpTo2J_WmToLNu_QCD',False,'nanoLatino_') ,

                         'weight' : mcCommonWeight+'*WtaggerSFnom*((Sum$(GenJet_pt > 30) >3 ))*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)',
                       'FilesPerJob' : FilesPerJobMainBKG,
                     }



samples['WZ'] = {    'name'   :   getSampleFiles(directory,'WZ',False,'nanoLatino_') ,
                     'weight' : mcCommonWeight+'*WtaggerSFnom',
                     'FilesPerJob' : FilesPerJob,                 
}

samples['ZZ'] = {    'name'   :   getSampleFiles(directory,'ZZ',False,'nanoLatino_') ,
                     'weight' : mcCommonWeight+'*WtaggerSFnom',
                     'FilesPerJob' : FilesPerJob,                 
}


samples['WWW'] = {    'name'   :   getSampleFiles(directory,'WWW',False,'nanoLatino_') ,
                      'weight' : mcCommonWeight+'*WtaggerSFnom',
                      'FilesPerJob' : FilesPerJob,                 
}

samples['WZZ'] = {    'name'   :   getSampleFiles(directory,'WZZ',False,'nanoLatino_') ,
                      'weight' : mcCommonWeight+'*WtaggerSFnom',
                      'FilesPerJob' : FilesPerJob,                 
}
samples['ZZZ'] = {    'name'   :   getSampleFiles(directory,'ZZZ',False,'nanoLatino_') ,
                      'weight' : mcCommonWeight,
                      'FilesPerJob' : FilesPerJob,                 
}

samples['WWZ'] = {    'name'   :   getSampleFiles(directory,'WWZ',False,'nanoLatino_') ,
                      'weight' : mcCommonWeight+'*WtaggerSFnom',
                      'FilesPerJob' : FilesPerJob,                 
}




samples['ggHWWlnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M125',False,'nanoLatino_'),
                               'weight' : mcCommonWeight+'*WtaggerSFnom',
                                    'FilesPerJob' : FilesPerJob,
                            }

samples['vbfHWWlnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'VBFHToWWToLNuQQ_M125',False,'nanoLatino_'),
                                'weight' : mcCommonWeight+'*WtaggerSFnom',
                                     'FilesPerJob' : FilesPerJob,
                              }

samples['ZHWWlnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'HZJ_HToWW_M125',False,'nanoLatino_'),
                                'weight' : mcCommonWeight+'*WtaggerSFnom',
                                'FilesPerJob' : FilesPerJob,
                              }
samples['WpHWWlnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'HWplusJ_HToWW_M125',False,'nanoLatino_'),
                                'weight' : mcCommonWeight+'*WtaggerSFnom',
                                'FilesPerJob' : FilesPerJob,
                              }
samples['WmHWWlnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'HWminusJ_HToWW_M125',False,'nanoLatino_'),
                                'weight' : mcCommonWeight+'*WtaggerSFnom',
                                'FilesPerJob' : FilesPerJob,
                              }

samples['ggHtautaulnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'GluGluHToTauTau_M125',False,'nanoLatino_'),
                                'weight' : mcCommonWeight,
                                'FilesPerJob' : FilesPerJob,
                              }

samples['vbfHtautaulnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'VBFHToTauTau_M125',False,'nanoLatino_'),
                                'weight' : mcCommonWeight,
                                'FilesPerJob' : FilesPerJob,
                              }
samples['WmHtautaulnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'HWminusJ_HToTauTau_M125',False,'nanoLatino_'),
                                'weight' : mcCommonWeight,
                                'FilesPerJob' : FilesPerJob,
                              }
samples['WpHtautaulnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'HWplusJ_HToTauTau_M125',False,'nanoLatino_'),
                                'weight' : mcCommonWeight,
                                'FilesPerJob' : FilesPerJob,
                              }
samples['ZHtautaulnuqq_M125'] = { 'name'   :   getSampleFiles(directory,'HZJ_HToTauTau_M125',False,'nanoLatino_'),
                                'weight' : mcCommonWeight,
                                'FilesPerJob' : FilesPerJob,
                              }




samples['DATA']  = {   'name': [ ] ,
                       'weight' : 'METFilter_DATA*LepWPCut' ,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : FilesPerJobDATA,
                  }


samples['PseudoData']  = {   'name': [ ] ,
                       'weight' : 'METFilter_DATA*LepWPCut' ,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 10,
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
                        

#if TESTRUN:
#  samples={}
#  samples['GluGluHToWWToLNuQQ_M400'] = {    'name'   :   getSampleFiles(directory,'GluGluHToWWToLNuQQ_M400',False,'nanoLatino_') ,
#                        'weight' : mcCommonWeight,
#                      }

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
