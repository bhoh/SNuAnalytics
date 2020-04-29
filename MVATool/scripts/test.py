#!/usr/bin/env python

import os, sys

from collections import OrderedDict


import ROOT
from ROOT import TFile, TTree
try:
  from MLTools import MLTools
  from TMVATools import TMVATools
except ImportError:
  import os
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/MVATool/python/"
  sys.path.append(BASE_PATH)
  from MLTools import MLTools
  from TMVATools import TMVATools


file_names = {
  ('2018','TTLJ_powheg_Train') :
  [
    '/xrootd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_8/nanoLatino_TTToSemiLeptonic__part%s.root'%idx for idx in [0]
  ],
  ('2018','TTLJ_powheg_Test') :
  [
    '/xrootd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_8/nanoLatino_TTToSemiLeptonic__part%s.root'%idx for idx in [1]
  ],
  ('2018','HWW_M150_Train') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_8/nanoLatino_GluGluHToWWToLNuQQ_M150__part0.root'],
  ('2018','HWW_M150_Test') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_8/nanoLatino_GluGluHToWWToLNuQQ_M150__part1.root'],
}


variables = OrderedDict()

#variables[''] = {
#    'name' : '',
#    'type' : 'D'
#  }
variables['Lepton_pt'] = {
    'name' : 'Lepton_pt[0]',
    'type' : 'D'
  }

variables['Lepton_eta'] = {
    'name' : 'Lepton_eta[0]',
    'type' : 'D'
  }

variables['Lepton_phi'] = {
    'name' : 'Lepton_phi[0]',
    'type' : 'D'
  }

cuts = {
  'sig' : '',
  'bkg' : '',
}

options = {
  'factory' : {
    'name' : "TMVAClassification",
    'options' : ":".join(["!V",
	                  "!Silent",
			  "Color",
			  "DrawProgressBar",
			  "Transformations=I",
			  "AnalysisType=Classification"
		         ]),
    'weight' : "baseW*Xsec",
  },
  'prepareTrees' : ":".join(["SplitMode=Block",
			     "!V",
			     #"nTrain_Signal=55000",
			     #"nTrain_Background=1400000",
			     #"nTest_Signal=55000",
			     #"nTest_Background=1400000",
             	            ]),
  'bookMethod' : [
    {
      'type' : ROOT.TMVA.Types.kPyKeras,
      'name' : "DNN",
      'options' : ":".join(["H",
                            "!V",
        		    "VarTransform=N,D",
        		    "FilenameModel=model.h5",
        		    "NumEpochs=20",
        		    "BatchSize=100",
        	           ]),
    },
    ##{
    #  'type' : ROOT.TMVA.Types.kBDT,
    #  'name' : "BDT_400_MinNodeSize2of10",
    #  'options' : ":".join(["!H",
    #                        "!V",
    #               	    "NTrees=400",
    #    		    "MaxDepth=2",
    #    		    "MinNodeSize=20%",
    #    		    "BoostType=Grad",
    #    		    "SeparationType=GiniIndex",
    #    		    "nCuts=100",
    #    		    "PruneMethod=NoPruning",
    #    	           ])
    #},
    #{
    #  'type' : ROOT.TMVA.Types.kBDT,
    #  'name' : "BDT",
    #  'options' : ":".join(["!H",
    #                        "!V",
	#		    "VarTransform=N",
    #               	    "NTrees=400",
    #    		    "MaxDepth=2",
	#		    "MinNodeSize=10%",
    #    		    "BoostType=Grad",
    #    		    "SeparationType=GiniIndex",
    #    		    "nCuts=100",
    #    		    "PruneMethod=NoPruning",
    #    	           ])
    #},
    #{
    #  'type' : ROOT.TMVA.Types.kBDT,
    #  'name' : "BDT_400_NEvent400",
    #  'options' : ":".join(["!H",
    #                        "!V",
    #    		    "VarTransform=N,D(dijet_deltaR,had_w_ch_deltaR)",
    #               	    "NTrees=400",
    #    		    "MaxDepth=2",
    #    		    "NEventsMin=400",
    #    		    "BoostType=Grad",
    #    		    "SeparationType=GiniIndex",
    #    		    "nCuts=100",
    #    		    "PruneMethod=NoPruning",
    #    	           ])
    #},
    #{
    #  'type' : ROOT.TMVA.Types.kBDT,
    #  'name' : "BDT_800_NEvent400_pruning",
    #  'options' : ":".join(["!H",
    #                        "!V",
    #    		    "VarTransform=N,D(dijet_deltaR,had_w_ch_deltaR,dijet_pt_avg)",
    #               	    "NTrees=800",
    #    		    "MaxDepth=2",
    #    		    "NEventsMin=400",
    #    		    "BoostType=Grad",
    #    		    "SeparationType=GiniIndex",
    #    		    "nCuts=100",
    #    		    "PruneMethod=ExpectedError",
    #    	           ])
    #},
    #{
    #  'type' : ROOT.TMVA.Types.kBDT,
    #  'name' : "BDT_400_rand",
    #  'options' : ":".join(["!H",
    #                        "!V",
    #               	    "NTrees=400",
    #    		    "MaxDepth=2",
    #    		    "UseRandomisedTrees=True",
    #    		    "UseNvars=2",
    #    		    "BoostType=Grad",
    #    		    "SeparationType=GiniIndex",
    #    		    "nCuts=100",
    #    		    "PruneMethod=NoPruning",
    #    	           ])
    #},
    #{
    #  'type' : ROOT.TMVA.Types.kBDT,
    #  'name' : "BDT_400_rand_pruning",
    #  'options' : ":".join(["!H",
    #                        "!V",
    #               	    "NTrees=400",
    #    		    "MaxDepth=2",
    #    		    "UseRandomisedTrees=True",
    #    		    "UseNvars=2",
    #    		    "BoostType=Grad",
    #    		    "SeparationType=GiniIndex",
    #    		    "nCuts=100",
    #    		    "PruneMethod=ExpectedError",
    #    	           ])
    #},
        #{ 
    #  'type' : ROOT.TMVA.Types.kDNN,
    #  'name' : "DNN",
    #  'options' : ":".join(["!H",
    #                        "!V",
    #                        "VarTransform=N",
    #    		    "ErrorStrategy=CROSSENTROPY",
    #    		    "WeightInitialization=XAVIERUNIFORM",
    #    		    "Layout=TANH|100,TANH|50,TANH|10,LINEAR",
    #    		    "TrainingStrategy="
    #    		    "LearningRate=1e-1,"
    #    		    "Momentum=0.5,"
    #    		    "Repetitions=1,"
    #    		    "ConvergenceSteps=20,"
    #    		    "BatchSize=100,"
    #    		    "DropConfig=0.0+0.5+0.5+0.0,"
    #    		    "WeightDecay=0.001,"
    #    		    "Regularization=L2,"
    #    		    "TestRepetitions=2,"
    #    		    "Multithreading=F"
    #    	           ])
    #}

  ],
}

IsKeras = False
for option in options['bookMethod']:
  if option['type'] == ROOT.TMVA.Types.kPyKeras:
    IsKeras = True
if IsKeras:
  from KerasModel import KerasModel
  m = KerasModel()
  m.defineModel_3layer(len(variables.keys()))
  m.compile()
  m.save("model.h5")
  m.summary()

ml_tools =MLTools()
ml_tools.SetMLTools(TMVATools)

train_years = [
  #'2016',
  #'2017',
  '2018'
]
train_samples = [
	'TTLJ_powheg_Train',
	'TTLJ_powheg_Test',
    'HWW_M150_Train',
    'HWW_M150_Test',
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

for train_year in train_years:
  for train_sample in train_samples:
    ml_tools.SetTrees(train_sample,'Events',file_names[train_year, train_sample])
    ml_tools.SetTrees(train_sample,'Events',file_names[train_year, train_sample])

  ml_tools.SetVariables(variables)
  ml_tools.SetCuts(cuts)
  ml_tools.SetOptions(options)

  ml_tools.doTrain(['%s_Events'%sig for sig in ['HWW_M150_Train','HWW_M150_Test']],['%s_Events'%bkg for bkg in ['TTLJ_powheg_Train','TTLJ_powheg_Test']],'%s'%train_year,'out_train_%s.root'%train_year)
  #
  #---------------------------------------------------
  #
  os.system('mv TMVAClassification TMVAClassification_%s'%(train_year))
  os.system('mkdir out_root_%s'%(train_year))
  os.system('mv out_*.root out_root_%s'%(train_year))
