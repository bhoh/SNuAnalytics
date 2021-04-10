#!/usr/bin/env python

import os, sys

from collections import OrderedDict


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
    'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Summer16_102X_nAODv7_Full2016v7/CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016__mvaTreeCHToCB/nanoLatino_TT_TuneCUETP8M2T4_PSweights__part%s.root'%idx for idx in range(42)

  ],
  ('2017','TTLJ_powheg') :
  [
    'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv7_Full2017v7/CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017__mvaTreeCHToCB/nanoLatino_TTToSemiLeptonic__part%s.root'%idx for idx in range(14)
  ],
  ('2018','TTLJ_powheg') :
  [
    'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv7_Full2018v7/CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018__mvaTreeCHToCB/nanoLatino_TTToSemiLeptonic__part%s.root'%idx for idx in range(12)
  ],
  ('2016','CHToCB_High') :
  [
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Summer16_102X_nAODv7_Full2016v7/CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016__mvaTreeCHToCB/nanoLatino_CHToCB_M120__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Summer16_102X_nAODv7_Full2016v7/CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016__mvaTreeCHToCB/nanoLatino_CHToCB_M130__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Summer16_102X_nAODv7_Full2016v7/CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016__mvaTreeCHToCB/nanoLatino_CHToCB_M140__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Summer16_102X_nAODv7_Full2016v7/CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016__mvaTreeCHToCB/nanoLatino_CHToCB_M150__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Summer16_102X_nAODv7_Full2016v7/CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016__mvaTreeCHToCB/nanoLatino_CHToCB_M160__part*.root',
  ],
  ('2017','CHToCB_High') :
  [
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv7_Full2017v7/CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017__mvaTreeCHToCB/nanoLatino_CHToCB_M120__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv7_Full2017v7/CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017__mvaTreeCHToCB/nanoLatino_CHToCB_M130__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv7_Full2017v7/CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017__mvaTreeCHToCB/nanoLatino_CHToCB_M140__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv7_Full2017v7/CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017__mvaTreeCHToCB/nanoLatino_CHToCB_M150__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv7_Full2017v7/CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017__mvaTreeCHToCB/nanoLatino_CHToCB_M160__part*.root',
  ],
  ('2018','CHToCB_High') :
  [
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv7_Full2018v7/CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018__mvaTreeCHToCB/nanoLatino_CHToCB_M120__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv7_Full2018v7/CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018__mvaTreeCHToCB/nanoLatino_CHToCB_M130__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv7_Full2018v7/CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018__mvaTreeCHToCB/nanoLatino_CHToCB_M140__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv7_Full2018v7/CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018__mvaTreeCHToCB/nanoLatino_CHToCB_M150__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv7_Full2018v7/CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018__mvaTreeCHToCB/nanoLatino_CHToCB_M160__part*.root',
  ],
  ('2016','CHToCB_Low') :
  [
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Summer16_102X_nAODv7_Full2016v7/CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016__mvaTreeCHToCB/nanoLatino_CHToCB_M080__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Summer16_102X_nAODv7_Full2016v7/CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016__mvaTreeCHToCB/nanoLatino_CHToCB_M090__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Summer16_102X_nAODv7_Full2016v7/CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016__mvaTreeCHToCB/nanoLatino_CHToCB_M100__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Summer16_102X_nAODv7_Full2016v7/CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016__mvaTreeCHToCB/nanoLatino_CHToCB_M110__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Summer16_102X_nAODv7_Full2016v7/CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016__mvaTreeCHToCB/nanoLatino_CHToCB_M120__part*.root',
  ],
  ('2017','CHToCB_Low') :
  [
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv7_Full2017v7/CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017__mvaTreeCHToCB/nanoLatino_CHToCB_M080__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv7_Full2017v7/CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017__mvaTreeCHToCB/nanoLatino_CHToCB_M090__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv7_Full2017v7/CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017__mvaTreeCHToCB/nanoLatino_CHToCB_M100__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv7_Full2017v7/CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017__mvaTreeCHToCB/nanoLatino_CHToCB_M110__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv7_Full2017v7/CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017__mvaTreeCHToCB/nanoLatino_CHToCB_M120__part*.root',
  ],
  ('2018','CHToCB_Low') :
  [
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv7_Full2018v7/CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018__mvaTreeCHToCB/nanoLatino_CHToCB_M080__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv7_Full2018v7/CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018__mvaTreeCHToCB/nanoLatino_CHToCB_M090__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv7_Full2018v7/CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018__mvaTreeCHToCB/nanoLatino_CHToCB_M100__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv7_Full2018v7/CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018__mvaTreeCHToCB/nanoLatino_CHToCB_M110__part*.root',
   'root://cms-xrdr.private.lo:2094//xrd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv7_Full2018v7/CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018__mvaTreeCHToCB/nanoLatino_CHToCB_M120__part*.root',
  ],
}


variables = OrderedDict()
spectators = OrderedDict()


# do not add spectator, it should be add when using it after training. but TMVAfiller module don't support spectators
#spectators['fitted_dijet_M_nom'] = {
#    'definition' : 'fitted_dijet_M_nom',
#  }
#spectators['fitted_dijet_M_high_nom'] = {
#    'definition' : 'fitted_dijet_M_high_nom',
#  }

#variables[''] = {
#    'definition' : '',
#    'type' : 'D'
#  }
variables['csv_jet0_mvaCHToCB_nom'] = {
    'definition' : 'csv_jet0_mvaCHToCB_nom',
    'type' : 'F'
  }
variables['csv_jet1_mvaCHToCB_nom'] = {
    'definition' : 'csv_jet1_mvaCHToCB_nom',
    'type' : 'F'
  }
variables['csv_jet2_mvaCHToCB_nom'] = {
    'definition' : 'csv_jet2_mvaCHToCB_nom',
    'type' : 'F'
  }
variables['avg_csv_had_top'] = {
    'definition' : 'avg_csv_had_top := (csv_jet0_mvaCHToCB_nom+csv_jet1_mvaCHToCB_nom+csv_jet2_mvaCHToCB_nom)/3',
    'type' : 'F'
  }
variables['2nd_moment_csv_jet0_mvaCHToCB_nom'] = {
        'definition' : '2nd_moment_csv_jet0_mvaCHToCB_nom := (csv_jet0_mvaCHToCB_nom-(csv_jet0_mvaCHToCB_nom+csv_jet1_mvaCHToCB_nom+csv_jet2_mvaCHToCB_nom)/3)*(csv_jet0_mvaCHToCB_nom-(csv_jet0_mvaCHToCB_nom+csv_jet1_mvaCHToCB_nom+csv_jet2_mvaCHToCB_nom)/3)',
    'type' : 'F'
  }
variables['2nd_moment_csv_jet1_mvaCHToCB_nom'] = {
        'definition' : '2nd_moment_csv_jet1_mvaCHToCB_nom := (csv_jet1_mvaCHToCB_nom-(csv_jet0_mvaCHToCB_nom+csv_jet1_mvaCHToCB_nom+csv_jet2_mvaCHToCB_nom)/3)*(csv_jet1_mvaCHToCB_nom-(csv_jet0_mvaCHToCB_nom+csv_jet1_mvaCHToCB_nom+csv_jet2_mvaCHToCB_nom)/3)',
    'type' : 'F'
  }
variables['2nd_moment_csv_jet2_mvaCHToCB_nom'] = {
        'definition' : '2nd_moment_csv_jet2_mvaCHToCB_nom := (csv_jet2_mvaCHToCB_nom-(csv_jet0_mvaCHToCB_nom+csv_jet1_mvaCHToCB_nom+csv_jet2_mvaCHToCB_nom)/3)*(csv_jet2_mvaCHToCB_nom-(csv_jet0_mvaCHToCB_nom+csv_jet1_mvaCHToCB_nom+csv_jet2_mvaCHToCB_nom)/3)',
    'type' : 'F'
  }
variables['dijet_deltaR0_mvaCHToCB_nom'] = {
    'definition' : 'dijet_deltaR0_mvaCHToCB_nom',
    'type' : 'F'
  }
variables['dijet_deltaR1_mvaCHToCB_nom'] = {
    'definition' : 'dijet_deltaR1_mvaCHToCB_nom',
    'type' : 'F'
  }
variables['Hplus_b_deltaR0_mvaCHToCB_nom'] = {
    'definition' : 'Hplus_b_deltaR0_mvaCHToCB_nom',
    'type' : 'F'
  }
variables['Hplus_b_deltaR1_mvaCHToCB_nom'] = {
    'definition' : 'Hplus_b_deltaR1_mvaCHToCB_nom',
    'type' : 'F'
  }
#variables['dijet_ptD0_mvaCHToCB'] = {
#    'definition' : 'dijet_ptD0_mvaCHToCB',
#    'type' : 'F'
#  }
#variables['dijet_ptD1_mvaCHToCB'] = {
#    'definition' : 'dijet_ptD1_mvaCHToCB',
#    'type' : 'F'
#  }
variables['bb_deltaR_mvaCHToCB_nom'] = {
    'definition' : 'bb_deltaR_mvaCHToCB_nom',
    'type' : 'F'
  }
variables['min_deltaR_bb_event_mvaCHToCB_nom'] = {
    'definition' : 'min_deltaR_bb_event_mvaCHToCB_nom',
    'type' : 'F'
  }
#variables['min_deltaR_jj_event_mvaCHToCB'] = { #minor
#    'definition' : 'min_deltaR_jj_event_mvaCHToCB',
#    'type' : 'F'
#  }
#variables['had_top_pt_scalar_sum_mvaCHToCB'] = { #minor
#    'definition' : 'had_top_pt_scalar_sum_mvaCHToCB',
#    'type' : 'F'
#  }

#variables['HT_btagged_L'] = {
#    'definition' : 'HT_btagged_L',
#    'type' : 'F'
#  }
#variables['HT_not_btagged_L'] = {
#    'definition' : 'HT_not_btagged_L',
#    'type' : 'F'
#  }
variables['HT_btagged_M_nom'] = {
    'definition' : 'HT_btagged_M_nom',
    'type' : 'F'
  }
variables['HT_not_btagged_M_nom'] = {
    'definition' : 'HT_not_btagged_M_nom',
    'type' : 'F'
  }
#variables['HT_btagged_T'] = {
#    'definition' : 'HT_btagged_T',
#    'type' : 'F'
#  }
#variables['HT_not_btagged_T'] = {
#    'definition' : 'HT_not_btagged_T',
#    'type' : 'F'
#  }
#variables['mbb_mvaCHToCB'] = {
#    'definition' : 'mbb_mvaCHToCB',
#    'type' : 'F'
#  }
#variables['mcb0_mvaCHToCB'] = {
#    'definition' : 'mcb0_mvaCHToCB',
#    'type' : 'F'
#  }
#variables['mcb1_mvaCHToCB'] = {
#    'definition' : 'mcb1_mvaCHToCB',
#    'type' : 'F'
#  }
#variables['hadronic_top_mass_mvaCHToCB'] = {
#    'definition' : 'hadronic_top_mass_mvaCHToCB',
#    'type' : 'F'
#  }
cuts = {
  'sig' : '(nbtags_event_mvaCHToCB_nom>=3 && nbtags_had_top_mvaCHToCB_nom>=2)', # (event%3)>0 too pass 1/3
  # && Sum$(abs(LHEPart_pdgId)==11 || abs(LHEPart_pdgId)==13 || abs(LHEPart_pdgId)==15)==1 
  'bkg' : '(nbtags_event_mvaCHToCB_nom>=3 && nbtags_had_top_mvaCHToCB_nom>=2)',
}

options_High = {
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
    #'weight' : "1.",
    'weight' : "1*(XSWeight>=0)-1*(XSWeight<0)",
  },
  'prepareTrees' : ":".join(["SplitMode=Alternate",
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
        		    "NumEpochs=200",
        		    "BatchSize=1000",
                    "verbose=2",
                    "TriesEarlyStopping=10",
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
                    "UseBaggedGrad=True",
                    "BaggedSampleFraction=0.5",
			        "MinNodeSize=2%",
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
			  "AnalysisType=Classification"
		         ]),
    #'weight' : "",
    #'weight' : "1.",
    'weight' : "1*(XSWeight>=0)-1*(XSWeight<0)",
  },
  'prepareTrees' : ":".join(["SplitMode=Alternate",
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
        		    "NumEpochs=200",
        		    "BatchSize=1000",
                    "verbose=2",
                    "TriesEarlyStopping=10",
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
                    "UseBaggedGrad=True",
                    "BaggedSampleFraction=0.5",
			        "MinNodeSize=2%",
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
    from KerasModel_ttToHplus_conv import KerasModel
    m = KerasModel()
    m.defineModel_3layer(len(variables.keys()))
    m.compile()
    m.save("model.h5")
    m.summary()
  
  ml_tools =MLTools()
  ml_tools.SetMLTools(TMVATools)

  # 100 bins for KS test
  #ROOT.TMVA.gConfig().GetVariablePlotting().fNbinsMVAoutput = 100
  #

  train_years = [
    #'2016',
    #'2017',
    '2018'
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
      #---------------------------------------------------
      #
      os.system('mv TMVAClassification TMVAClassification_%s_%s'%(sig, train_year))
      os.system('mkdir out_root_%s_%s'%(sig,train_year))
      os.system('mv out_*.root out_root_%s_%s'%(sig,train_year))
