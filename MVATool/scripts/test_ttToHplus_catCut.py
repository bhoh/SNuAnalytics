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
  ('2018','TTLJ_powheg') :
  [
    '/xrootd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__genCHToCB_2018__kinFitTTSemiLep_2018__mvaTreeCHToCB_2018/nanoLatino_TTToSemiLeptonic__part%s.root'%idx for idx in range(16)
  ],
  ('2018','CHToCB_High') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__genCHToCB_2018__kinFitTTSemiLep_2018__mvaTreeCHToCB_2018/nanoLatino_CHToCB_M130__part0.root',
  '/xrootd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__genCHToCB_2018__kinFitTTSemiLep_2018__mvaTreeCHToCB_2018/nanoLatino_CHToCB_M140__part0.root',
  '/xrootd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__genCHToCB_2018__kinFitTTSemiLep_2018__mvaTreeCHToCB_2018/nanoLatino_CHToCB_M150__part0.root',
  '/xrootd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__genCHToCB_2018__kinFitTTSemiLep_2018__mvaTreeCHToCB_2018/nanoLatino_CHToCB_M150__part1.root',
  ],
  ('2018','CHToCB_Low') :
  ['/xrootd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__genCHToCB_2018__kinFitTTSemiLep_2018__mvaTreeCHToCB_2018/nanoLatino_CHToCB_M075__part0.root',
  '/xrootd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__genCHToCB_2018__kinFitTTSemiLep_2018__mvaTreeCHToCB_2018/nanoLatino_CHToCB_M080__part0.root',
  '/xrootd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__genCHToCB_2018__kinFitTTSemiLep_2018__mvaTreeCHToCB_2018/nanoLatino_CHToCB_M085__part0.root',
  '/xrootd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__genCHToCB_2018__kinFitTTSemiLep_2018__mvaTreeCHToCB_2018/nanoLatino_CHToCB_M090__part0.root',
  '/xrootd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__genCHToCB_2018__kinFitTTSemiLep_2018__mvaTreeCHToCB_2018/nanoLatino_CHToCB_M100__part0.root',
  '/xrootd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__genCHToCB_2018__kinFitTTSemiLep_2018__mvaTreeCHToCB_2018/nanoLatino_CHToCB_M110__part0.root',
  '/xrootd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__genCHToCB_2018__kinFitTTSemiLep_2018__mvaTreeCHToCB_2018/nanoLatino_CHToCB_M120__part0.root',
  ],
}


variables = OrderedDict()
spectators = OrderedDict()

spectators['gen_dijet_mass'] = {
    'definition' : 'gen_dijet_mass',
  }

#variables[''] = {
#    'definition' : '',
#    'type' : 'D'
#  }
variables['csv_jet0_mvaCHToCB'] = {
    'definition' : 'csv_jet0_mvaCHToCB',
    'type' : 'D'
  }
variables['csv_jet1_mvaCHToCB'] = {
    'definition' : 'csv_jet1_mvaCHToCB',
    'type' : 'D'
  }
variables['csv_jet2_mvaCHToCB'] = {
    'definition' : 'csv_jet2_mvaCHToCB',
    'type' : 'D'
  }
variables['avg_csv_had_top'] = {
    'definition' : 'avg_csv_had_top := (csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3',
    'type' : 'D'
  }
variables['2nd_moment_csv_jet0_mvaCHToCB'] = {
        'definition' : '2nd_moment_csv_jet0_mvaCHToCB := (csv_jet0_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)*(csv_jet0_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)',
    'type' : 'D'
  }
variables['2nd_moment_csv_jet1_mvaCHToCB'] = {
        'definition' : '2nd_moment_csv_jet1_mvaCHToCB := (csv_jet1_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)*(csv_jet1_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)',
    'type' : 'D'
  }
variables['2nd_moment_csv_jet2_mvaCHToCB'] = {
        'definition' : '2nd_moment_csv_jet2_mvaCHToCB := (csv_jet2_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)*(csv_jet2_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)',
    'type' : 'D'
  }
variables['dijet_deltaR0_mvaCHToCB'] = {
    'definition' : 'dijet_deltaR0_mvaCHToCB',
    'type' : 'D'
  }
variables['dijet_deltaR1_mvaCHToCB'] = {
    'definition' : 'dijet_deltaR1_mvaCHToCB',
    'type' : 'D'
  }
variables['Hplus_b_deltaR0_mvaCHToCB'] = {
    'definition' : 'Hplus_b_deltaR0_mvaCHToCB',
    'type' : 'D'
  }
variables['Hplus_b_deltaR_mvaCHToCB'] = {
    'definition' : 'Hplus_b_deltaR1_mvaCHToCB',
    'type' : 'D'
  }
#variables['dijet_ptD0_mvaCHToCB'] = {
#    'definition' : 'dijet_ptD0_mvaCHToCB',
#    'type' : 'D'
#  }
#variables['dijet_ptD1_mvaCHToCB'] = {
#    'definition' : 'dijet_ptD1_mvaCHToCB',
#    'type' : 'D'
#  }
variables['bb_deltaR_mvaCHToCB'] = {
    'definition' : 'bb_deltaR_mvaCHToCB',
    'type' : 'D'
  }
variables['min_deltaR_bb_event_mvaCHToCB'] = {
    'definition' : 'min_deltaR_bb_event_mvaCHToCB',
    'type' : 'D'
  }
#variables['min_deltaR_jj_event_mvaCHToCB'] = { #minor
#    'definition' : 'min_deltaR_jj_event_mvaCHToCB',
#    'type' : 'D'
#  }
#variables['had_top_pt_scalar_sum_mvaCHToCB'] = { #minor
#    'definition' : 'had_top_pt_scalar_sum_mvaCHToCB',
#    'type' : 'D'
#  }

#variables['HT_btagged_L'] = {
#    'definition' : 'HT_btagged_L',
#    'type' : 'D'
#  }
#variables['HT_not_btagged_L'] = {
#    'definition' : 'HT_not_btagged_L',
#    'type' : 'D'
#  }
variables['HT_btagged_M'] = {
    'definition' : 'HT_btagged_M',
    'type' : 'D'
  }
variables['HT_not_btagged_M'] = {
    'definition' : 'HT_not_btagged_M',
    'type' : 'D'
  }
#variables['HT_btagged_T'] = {
#    'definition' : 'HT_btagged_T',
#    'type' : 'D'
#  }
#variables['HT_not_btagged_T'] = {
#    'definition' : 'HT_not_btagged_T',
#    'type' : 'D'
#  }
variables['mbb_mvaCHToCB'] = {
    'definition' : 'mbb_mvaCHToCB',
    'type' : 'D'
  }
variables['mcb0_mvaCHToCB'] = {
    'definition' : 'mcb0_mvaCHToCB',
    'type' : 'D'
  }
variables['mcb1_mvaCHToCB'] = {
    'definition' : 'mcb1_mvaCHToCB',
    'type' : 'D'
  }
variables['hadronic_top_mass_mvaCHToCB'] = {
    'definition' : 'hadronic_top_mass_mvaCHToCB',
    'type' : 'D'
  }
cuts = {
  'sig' : '(nbtags_event_mvaCHToCB>=3 && nbtags_had_top_mvaCHToCB>=2)',
  'bkg' : '(nbtags_event_mvaCHToCB>=3 && nbtags_had_top_mvaCHToCB>=2)',
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
    #'weight' : "",
    'weight' : "1.",
    #'weight' : "baseW*Xsec",
  },
  'prepareTrees' : ":".join(["SplitMode=Alternate",
			     "!V",
			     #"nTrain_Signal=20000",
			     #"nTrain_Background=20000",
			     #"nTest_Signal=20000",
			     #"nTest_Background=20000",
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
        		    "NumEpochs=1000",
        		    "BatchSize=1000",
                    "TriesEarlyStopping=30",
        	           ]),
    },
    {
      'type' : ROOT.TMVA.Types.kBDT,
      'name' : "BDT_800_MinNodeSize2of10",
      'options' : ":".join(["!H",
                            "!V",
        		    "VarTransform=N,D",
                   	    "NTrees=800",
        		    "MaxDepth=3",
        		    "MinNodeSize=20%",
        		    "BoostType=Grad",
        		    "SeparationType=GiniIndex",
        		    "nCuts=100",
        		    "PruneMethod=NoPruning",
        	           ])
    },
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
	'TTLJ_powheg',
    'CHToCB_High',
    #'CHToCB_Low',
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
  ml_tools.SetSpectators(spectators)
  ml_tools.SetCuts(cuts)
  ml_tools.SetOptions(options)

  ml_tools.doTrain(['%s_Events'%sig for sig in ['CHToCB_High']],['%s_Events'%bkg for bkg in ['TTLJ_powheg']],'%s'%train_year,'out_train_%s.root'%train_year)
  #ml_tools.doTrain(['%s_Events'%sig for sig in ['CHToCB_Low']],['%s_Events'%bkg for bkg in ['TTLJ_powheg']],'%s'%train_year,'out_train_%s.root'%train_year)
  #
  #---------------------------------------------------
  #
  os.system('mv TMVAClassification TMVAClassification_%s'%(train_year))
  os.system('mkdir out_root_%s'%(train_year))
  os.system('mv out_*.root out_root_%s'%(train_year))
