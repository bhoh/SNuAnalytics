#!/usr/bin/env python

import os, sys

from collections import OrderedDict
from variables import *


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


file_names = {
  ('2016','TTLJ_powheg') :
  [
    '/cms_scratch/bhoh/mva_TTLJ_powheg_2016.root',
  ],
  ('2017','TTLJ_powheg') :
  [
    '/cms_scratch/bhoh/mva_TTLJ_powheg_2017.root',
  ],
  ('2018','TTLJ_powheg') :
  [
    '/cms_scratch/bhoh/mva_TTLJ_powheg_2018.root',
  ],
  ('2016','CHToCB_High') :
  [
    '/cms_scratch/bhoh/mva_CHToCB_High_2016.root'
  ],
  ('2017','CHToCB_High') :
  [
    '/cms_scratch/bhoh/mva_CHToCB_High_2017.root'
  ],
  ('2018','CHToCB_High') :
  [
    '/cms_scratch/bhoh/mva_CHToCB_High_2018.root'
  ],
  ('2016','CHToCB_Low') :
  [
    '/cms_scratch/bhoh/mva_CHToCB_Low_2016.root'
  ],
  ('2017','CHToCB_Low') :
  [
    '/cms_scratch/bhoh/mva_CHToCB_Low_2017.root'
  ],
  ('2018','CHToCB_Low') :
  [
    '/cms_scratch/bhoh/mva_CHToCB_Low_2018.root'
  ],
}



cuts = {
  #( Lepton_isTightElectron_POGTight[0]>0.5 || Lepton_isTightMuon_cut_Tight_POG[0] > 0.5 )
  
  #'sig' : '(nbtags_event_mvaCHToCB_nom>=3 && nbtags_had_top_mvaCHToCB_nom>=2) && Lepton_genmatched[0]>0.5 && Lepton_pt[0] > 30. && ((abs(Lepton_pdgId[0])==11 && ( abs(Lepton_eta[0])<2.5 )) || (abs(Lepton_pdgId[0])==13 && ( abs(Lepton_eta[0])<2.4 ))) && PuppiMET_pt > 20.', # (event%3)>0 too pass 1/3
  'sig' : 'Lepton_genmatched[0]>0.5 && Lepton_pt[0] > 30. && ((abs(Lepton_pdgId[0])==11 && ( abs(Lepton_eta[0])<2.5 )) || (abs(Lepton_pdgId[0])==13 && ( abs(Lepton_eta[0])<2.4 ))) && PuppiMET_pt > 20.', # (event%3)>0 too pass 1/3
  # && Sum$(abs(LHEPart_pdgId)==11 || abs(LHEPart_pdgId)==13 || abs(LHEPart_pdgId)==15)==1 
  #'bkg' : '(nbtags_event_mvaCHToCB_nom>=3 && nbtags_had_top_mvaCHToCB_nom>=2) && Lepton_genmatched[0]>0.5 && Lepton_pt[0] > 30. && ((abs(Lepton_pdgId[0])==11 && ( abs(Lepton_eta[0])<2.5 )) || (abs(Lepton_pdgId[0])==13 && ( abs(Lepton_eta[0])<2.4 ))) && PuppiMET_pt > 20.',
  'bkg' : 'Lepton_genmatched[0]>0.5 && Lepton_pt[0] > 30. && ((abs(Lepton_pdgId[0])==11 && ( abs(Lepton_eta[0])<2.5 )) || (abs(Lepton_pdgId[0])==13 && ( abs(Lepton_eta[0])<2.4 ))) && PuppiMET_pt > 20.',
}

options_High = {
  'factory' : {
    'name' : "TMVAClassification",
    'options' : ":".join(["!V",
	                  "!Silent",
			  "Color",
			  "DrawProgressBar",
			  "Transformations=I",
			  "AnalysisType=Classification",
		         ]),
    #'weight' : "",
    #'weight' : "1.",
    'weight' : "XSWeight",
  },

  'prepareTrees' : ":".join([
                 "SplitMode=Alternate",
                 #"SplitMode=Random",
                 #"MixMode=Random",
			     "!V",
			     #"nTrain_Signal=50000",
			     #"nTrain_Background=100000",
			     #"nTest_Signal=50000",
			     #"nTest_Background=100000",
             	            ]),
  'bookMethod' : [
    {
      'type' : ROOT.TMVA.Types.kPyKeras,
      'name' : "DNN",
      'options' : ":".join(["H",
                            "!V",
        		    #"VarTransform=N,D",
        		    "VarTransform=G",
        		    "FilenameModel=model.h5",
        		    "NumEpochs=7",
                    "SaveBestOnly=false",
        		    "BatchSize=128",
                    "verbose=2",
                    "TriesEarlyStopping=30",
                    #"LearningRateSchedule=1,0.001;2,0.002;3,0.003;4,0.004;5,0.005;10,0.001",
                    #"ValidationSize=0.2", #why this option is not found? root version?
        	           ]),
    },
    {
      'type' : ROOT.TMVA.Types.kBDT,
      'name' : "BDT",
      'options' : ":".join(["!H",
                            "!V",
			    #"VarTransform=N,D",
			    "VarTransform=N",
                   	    "NTrees=400",
        		    "MaxDepth=2",
                    #"UseBaggedGrad=True",
                    #"BaggedSampleFraction=0.5",
			        "MinNodeSize=5%",
                    "Shrinkage=1",
        		    "BoostType=Grad",
        		    "SeparationType=GiniIndex",
                    "IgnoreNegWeightsInTraining=True",
        		    "nCuts=100",
        		    "PruneMethod=NoPruning",
        	           ])
    },
  ],

}
options_Low = {
  'factory' : {
    'name' : "TMVAClassification",
    'options' : ":".join(["!V",
	                  "!Silent",
			  "Color",
			  "DrawProgressBar",
			  "Transformations=I",
			  "AnalysisType=Classification",
		         ]),
    #'weight' : "",
    #'weight' : "1.",
    'weight' : "XSWeight",
  },

  'prepareTrees' : ":".join([
                 "SplitMode=Alternate",
                 #"SplitMode=Random",
                 #"MixMode=Random",
			     "!V",
			     #"nTrain_Signal=50000",
			     #"nTrain_Background=100000",
			     #"nTest_Signal=50000",
			     #"nTest_Background=100000",
             	            ]),
  'bookMethod' : [
    {
      'type' : ROOT.TMVA.Types.kPyKeras,
      'name' : "DNN",
      'options' : ":".join(["H",
                            "!V",
        		    #"VarTransform=N,D",
        		    "VarTransform=G",
        		    "FilenameModel=model.h5",
        		    "NumEpochs=7",
                    "SaveBestOnly=false",
        		    "BatchSize=128",
                    "verbose=2",
                    "TriesEarlyStopping=30",
                    #"LearningRateSchedule=1,0.001;2,0.002;3,0.003;4,0.004;5,0.005;10,0.001",
                    #"ValidationSize=0.2",
        	           ]),
    },
    {
      'type' : ROOT.TMVA.Types.kBDT,
      'name' : "BDT",
      'options' : ":".join(["!H",
                            "!V",
			    #"VarTransform=N,D",
			    "VarTransform=N",
                   	    "NTrees=400",
        		    "MaxDepth=2",
                    #"UseBaggedGrad=True",
                    #"BaggedSampleFraction=0.5",
			        "MinNodeSize=5%",
                    "Shrinkage=1",
        		    "BoostType=Grad",
        		    "SeparationType=GiniIndex",
                    "IgnoreNegWeightsInTraining=True",
        		    "nCuts=100",
        		    "PruneMethod=NoPruning",
        	           ])
    },
  ],
}
if __name__ == '__main__':
  #IsKeras = False
  IsKeras = True #XXX
  for option in options_High['bookMethod'] or option in options_Low['bookMethod']:
    if option['type'] == ROOT.TMVA.Types.kPyKeras:
      IsKeras = True
  if IsKeras:
    #from KerasModel_ttToHplus import KerasModel
    from KerasModel_ttToHplus_conv_res_test import KerasModel
    m = KerasModel()
    m.defineModel_3layer(len(variables.keys()))
    m.compile()
    m.save("model.h5")
    m.summary()
  
  ml_tools =MLTools()
  ml_tools.SetMLTools(TMVATools)

  # 100 bins for KS test
  ROOT.TMVA.gConfig().GetVariablePlotting().fNbinsMVAoutput = 100
  #

  train_years = [
    '2016',
    #'2017',
    #'2018'
  ]
  train_samples = [
  	'TTLJ_powheg',
    'CHToCB_High',
    'CHToCB_Low',
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
  
  
  ml_tools.SetVariables(variables)
  ml_tools.SetSpectators(spectators)
  ml_tools.SetCuts(cuts)
  
  for train_year in train_years:
    for train_sample in train_samples:
      ml_tools.SetTrees(train_sample,'Events',file_names[train_year, train_sample])
    for sig in ['CHToCB_High','CHToCB_Low']:
    #for sig in ['CHToCB_Low']:
      #set options by mass range
      if sig == 'CHToCB_High':
        ml_tools.SetOptions(options_High)
      else:
        ml_tools.SetOptions(options_Low)
      ml_tools.doTrain(['%s_Events'%sig],['%s_Events'%bkg for bkg in ['TTLJ_powheg']],'%s_%s'%(sig,train_year),'out_train_%s_%s.root'%(sig, train_year))
      #
      #ml_tools.doCrossValidation(['%s_Events'%sig],['%s_Events'%bkg for bkg in ['TTLJ_powheg']],'%s_%s'%(sig,train_year),'out_train_%s_%s.root'%(sig, train_year))
      #
      #---------------------------------------------------
      #
      os.system('mv TMVAClassification TMVAClassification_%s_%s'%(sig, train_year))
      os.system('mkdir out_root_%s_%s'%(sig,train_year))
      os.system('mv out_*.root out_root_%s_%s'%(sig,train_year))
      #os.system('mv cv_out_*.root out_root_%s_%s'%(sig,train_year))
