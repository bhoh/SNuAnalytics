#!/usr/bin/env python

import os, sys

from collections import OrderedDict
from variables import Variables


import ROOT
from ROOT import TFile, TTree
try:
  from MLTools_ttToHplus import MLTools
  from TMVATools_ttToHplus import TMVATools
except ImportError:
  import os
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/MVATool/python/"
  sys.path.append(BASE_PATH)
  from MLTools_ttToHplus import MLTools
  from TMVATools_ttToHplus import TMVATools


# first argument will be passed from .sh script
procId = sys.argv[1]

file_names = {
  ('2016HIPM','TTLJ_powheg_Train') :
  [
    '/cms_scratch/bhoh/mva_TTLJ_powheg_2016HIPM_Train.root',
  ],
  ('2016noHIPM','TTLJ_powheg_Train') :
  [
    '/cms_scratch/bhoh/mva_TTLJ_powheg_2016noHIPM_Train.root',
  ],
  ('2017','TTLJ_powheg_Train') :
  [
    '/cms_scratch/bhoh/mva_TTLJ_powheg_2017_Train.root',
  ],
  ('2018','TTLJ_powheg_Train') :
  [
    '/cms_scratch/bhoh/mva_TTLJ_powheg_2018_Train.root',
  ],
  ('2016HIPM','CHToCB_Train') :
  [
    #'/cms_scratch/bhoh/mva_CHToCB_M075_2016HIPM_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M080_2016HIPM_Train.root',
    #'/cms_scratch/bhoh/mva_CHToCB_M085_2016HIPM_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M090_2016HIPM_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M100_2016HIPM_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M110_2016HIPM_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M120_2016HIPM_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M130_2016HIPM_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M140_2016HIPM_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M150_2016HIPM_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M160_2016HIPM_Train.root',
  ],
  ('2016noHIPM','CHToCB_Train') :
  [
    #'/cms_scratch/bhoh/mva_CHToCB_M075_2016noHIPM_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M080_2016noHIPM_Train.root',
    #'/cms_scratch/bhoh/mva_CHToCB_M085_2016noHIPM_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M090_2016noHIPM_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M100_2016noHIPM_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M110_2016noHIPM_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M120_2016noHIPM_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M130_2016noHIPM_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M140_2016noHIPM_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M150_2016noHIPM_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M160_2016noHIPM_Train.root',
  ],
  ('2017','CHToCB_Train') :
  [
    #'/cms_scratch/bhoh/mva_CHToCB_M075_2017_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M080_2017_Train.root',
    #'/cms_scratch/bhoh/mva_CHToCB_M085_2017_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M090_2017_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M100_2017_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M110_2017_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M120_2017_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M130_2017_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M140_2017_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M150_2017_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M160_2017_Train.root',
  ],
  ('2018','CHToCB_Train') :
  [
    #'/cms_scratch/bhoh/mva_CHToCB_M075_2018_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M080_2018_Train.root',
    #'/cms_scratch/bhoh/mva_CHToCB_M085_2018_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M090_2018_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M100_2018_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M110_2018_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M120_2018_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M130_2018_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M140_2018_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M150_2018_Train.root',
    '/cms_scratch/bhoh/mva_CHToCB_M160_2018_Train.root',
  ],

  #
  ('2016HIPM','TTLJ_powheg_Test') :
  [
    '/cms_scratch/bhoh/mva_TTLJ_powheg_2016HIPM_Test.root',
  ],
  ('2016noHIPM','TTLJ_powheg_Test') :
  [
    '/cms_scratch/bhoh/mva_TTLJ_powheg_2016noHIPM_Test.root',
  ],
  ('2017','TTLJ_powheg_Test') :
  [
    '/cms_scratch/bhoh/mva_TTLJ_powheg_2017_Test.root',
  ],
  ('2018','TTLJ_powheg_Test') :
  [
    '/cms_scratch/bhoh/mva_TTLJ_powheg_2018_Test.root',
  ],
  ('2016HIPM','CHToCB_Test') :
  [
    #'/cms_scratch/bhoh/mva_CHToCB_M075_2016HIPM_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M080_2016HIPM_Test.root',
    #'/cms_scratch/bhoh/mva_CHToCB_M085_2016HIPM_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M090_2016HIPM_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M100_2016HIPM_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M110_2016HIPM_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M120_2016HIPM_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M130_2016HIPM_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M140_2016HIPM_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M150_2016HIPM_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M160_2016HIPM_Test.root',
  ],
  ('2016noHIPM','CHToCB_Test') :
  [
    #'/cms_scratch/bhoh/mva_CHToCB_M075_2016noHIPM_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M080_2016noHIPM_Test.root',
    #'/cms_scratch/bhoh/mva_CHToCB_M085_2016noHIPM_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M090_2016noHIPM_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M100_2016noHIPM_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M110_2016noHIPM_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M120_2016noHIPM_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M130_2016noHIPM_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M140_2016noHIPM_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M150_2016noHIPM_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M160_2016noHIPM_Test.root',
  ],
  ('2017','CHToCB_Test') :
  [
    #'/cms_scratch/bhoh/mva_CHToCB_M075_2017_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M080_2017_Test.root',
    #'/cms_scratch/bhoh/mva_CHToCB_M085_2017_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M090_2017_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M100_2017_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M110_2017_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M120_2017_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M130_2017_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M140_2017_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M150_2017_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M160_2017_Test.root',
  ],
  ('2018','CHToCB_Test') :
  [
    #'/cms_scratch/bhoh/mva_CHToCB_M075_2018_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M080_2018_Test.root',
    #'/cms_scratch/bhoh/mva_CHToCB_M085_2018_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M090_2018_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M100_2018_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M110_2018_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M120_2018_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M130_2018_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M140_2018_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M150_2018_Test.root',
    '/cms_scratch/bhoh/mva_CHToCB_M160_2018_Test.root',
  ],


}

# High mass & Low mass samples
high_mass_sample_list =  ['_M130', '_M140', '_M150', '_M160']
#low_mass_sample_list  =  ['_M075', '_M080', '_M085', '_M090', '_M100', '_M110', '_M120']
low_mass_sample_list  =  ['_M080', '_M090', '_M100', '_M110', '_M120']
high_mass_sample_filter = lambda file_name: sum([ True for mass in high_mass_sample_list if mass in file_name ]) == 1
low_mass_sample_filter  = lambda file_name: sum([ True for mass in low_mass_sample_list if mass in file_name ]) == 1

for year in ['2016HIPM', '2016noHIPM', '2017', '2018']:
  file_names[year,"CHToCB_High_Train"] = filter(high_mass_sample_filter, file_names[year,"CHToCB_Train"])
  file_names[year,"CHToCB_High_Test"]  = filter(high_mass_sample_filter, file_names[year,"CHToCB_Test"])
  file_names[year,"CHToCB_Low_Train"]  = filter(low_mass_sample_filter,  file_names[year,"CHToCB_Train"])
  file_names[year,"CHToCB_Low_Test"]   = filter(low_mass_sample_filter,  file_names[year,"CHToCB_Test"])

# 2017 + 2018
samples = [ sample for year, sample in file_names if year=="2017" ]
for sample in samples:
  if ("year_comb",sample) not in file_names:
    file_names["year_comb",sample] = file_names["2017",sample][:]
    file_names["year_comb",sample].extend( file_names["2018",sample] )
    file_names["year_comb",sample].extend( file_names["2016HIPM",sample] )
    file_names["year_comb",sample].extend( file_names["2016noHIPM",sample] )

cuts = {
  #( Lepton_isTightElectron_POGTight[0]>0.5 || Lepton_isTightMuon_cut_Tight_POG[0] > 0.5 )
  
  #'sig' : '(nbtags_event_mvaCHToCB_nom>=3 && nbtags_had_top_mvaCHToCB_nom>=2) && Lepton_genmatched[0]>0.5 && Lepton_pt[0] > 30. && ((abs(Lepton_pdgId[0])==11 && ( abs(Lepton_eta[0])<2.5 )) || (abs(Lepton_pdgId[0])==13 && ( abs(Lepton_eta[0])<2.4 ))) && PuppiMET_pt > 20.', # (event%3)>0 too pass 1/3
  'sig' : '1', # (event%3)>0 too pass 1/3
  # && Sum$(abs(LHEPart_pdgId)==11 || abs(LHEPart_pdgId)==13 || abs(LHEPart_pdgId)==15)==1 
  #'bkg' : '(nbtags_event_mvaCHToCB_nom>=3 && nbtags_had_top_mvaCHToCB_nom>=2) && Lepton_genmatched[0]>0.5 && Lepton_pt[0] > 30. && ((abs(Lepton_pdgId[0])==11 && ( abs(Lepton_eta[0])<2.5 )) || (abs(Lepton_pdgId[0])==13 && ( abs(Lepton_eta[0])<2.4 ))) && PuppiMET_pt > 20.',
  'bkg' : '1',
}

from options import *

if __name__ == '__main__':
  
  ml_tools =MLTools()
  ml_tools.SetMLTools(TMVATools)

  # 100 bins for KS test
  ROOT.TMVA.gConfig().GetVariablePlotting().fNbinsMVAoutput = 100
  print(ROOT.TMVA.gConfig().GetIONames().fWeightFileDir)
  #

  train_years = [
    #'2016HIPM',
    #'2016noHIPM',
    #'2017',
    #'2018',
    'year_comb'
  ]
  train_samples = [
  	'TTLJ_powheg_Train',
  	'TTLJ_powheg_Test',
    'CHToCB_Train',
    'CHToCB_Test',
    #'CHToCB_High_Train',
    #'CHToCB_High_Test',
    #'CHToCB_Low_Train',
    #'CHToCB_Low_Test',
    #'CHToCB_M090',
    #'CHToCB_M100',
  	#'CHToCB_M110',
  	#'CHToCB_M120',
  	#'CHToCB_M130',
  	#'CHToCB_M140',
  	#'CHToCB_M150',
  	#'CHToCB_M090to110',
  	#'CHToCB_M120to150',
  	#'CHToCB_M090to150'
  ]
  
  option_key = options.keys()[int(procId)]

  mvaVars = Variables()
  for key in options[option_key]['variables']:
    setattr(mvaVars, key, options[option_key]['variables'][key])

  # 'variables' : {'include_mass_label':False, },

  ml_tools.SetVariables(mvaVars.getVariables())
  ml_tools.SetSpectators({})
  ml_tools.SetCuts(cuts)
  

  train_year    = options[option_key]['train_year']
  train_samples = options[option_key]['train_samples']
  for train_sample in train_samples:
    ml_tools.SetTrees(train_sample,'Events',file_names[train_year, train_sample])
  sig = 'CHToCB'
  if sum([ True for train_sample in train_samples if '_High' in train_sample])> 0:
    sig += '_High'
  elif sum([ True for train_sample in train_samples if '_Low' in train_sample])> 0:
    sig += '_Low'
  #set options
  ml_tools.SetOptions(options[option_key])
  ml_tools.doTrain(['%s_Train_Events'%sig, '%s_Test_Events'%sig],['%s_Events'%bkg for bkg in ['TTLJ_powheg_Train','TTLJ_powheg_Test']],'%s_%s'%(sig,train_year),'out_train_%s_%s.root'%(sig, option_key))
  #
  #ml_tools.doCrossValidation(['%s_Events'%sig],['%s_Events'%bkg for bkg in ['TTLJ_powheg']],'%s_%s'%(sig,train_year),'out_train_%s_%s.root'%(sig, train_year))
  #
  #---------------------------------------------------
  #
  #os.system('mv TMVAClassification TMVAClassification_%s_%s'%(sig, train_year))
  #os.system('mkdir out_root_%s_%s'%(sig,train_year))
  #os.system('mv out_*.root out_root_%s_%s'%(sig,train_year))
  #os.system('mv cv_out_*.root out_root_%s_%s'%(sig,train_year))
