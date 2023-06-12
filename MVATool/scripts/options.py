import ROOT
from collections import OrderedDict
try:
  from KerasModel_ttToHplus import KerasModel
except ImportError:
  import os, sys
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/MVATool/python/"
  sys.path.append(BASE_PATH)
  from KerasModel_ttToHplus import KerasModel


# Grid Search
# DNN:
# nLayer
# nBatch
# L2 norm
#
#
# BDT:
# nTrees
# shrinkage
#
#

#options = OrderedDict({
#  'DNN_High_year_comb_Batch500_btagging' : {
#    'train_year' : 'year_comb',
#    'train_samples' :  ['TTLJ_powheg_Train', 'TTLJ_powheg_Test', 'CHToCB_High_Train', 'CHToCB_High_Test', ],
#    'variables' : {'include_mass_label':False, 'include_dijet_pt':True, 'include_ctagging':False, 'include_year_label':True },
#    'factory' : {
#      'name' : "TMVAClassification_DNN_High_year_comb_Batch500_btagging",
#      'options' : ":".join(["!V",
#  	                  "!Silent",
#  			  "Color",
#  			  "DrawProgressBar",
#  			  "Transformations=I",
#  			  "AnalysisType=Classification",
#  		         ]),
#      #'weight' : "",
#      #'weight' : "1.",
#      'weight' : "XSWeight",
#    },
#  
#    'prepareTrees' : ":".join([
#                   #"SplitMode=Alternate",
#                   #"SplitMode=Random",
#                   #"MixMode=Random",
#  			     "!V",
#  			     #"nTrain_Signal=20000",
#  			     #"nTrain_Background=20000",
#  			     #"nTest_Signal=40000",
#  			     #"nTest_Background=40000",
#               	            ]),
#    'bookMethod' : [
#      {
#        'type' : ROOT.TMVA.Types.kPyKeras,
#        'name' : "DNN",
#        'options' : ":".join(["H",
#                              "!V",
#          		    #"VarTransform=N,D",
#          		    "VarTransform=N",
#          		    "FilenameModel=model_DNN_High_year_comb_Batch500_btagging.h5",
#          		    "NumEpochs=100",
#                      "SaveBestOnly=true",
#          		    "BatchSize=500",
#                      "verbose=2",
#                      "TriesEarlyStopping=1",
#                      #"LearningRateSchedule=1,0.001;2,0.002;3,0.003;4,0.004;5,0.005;10,0.001",
#                      #"ValidationSize=0.2",
#          	           ]),
#      },
#    ],
#  },     
#        
#  'DNN_Low_year_comb_Batch500_btagging' : {
#    'train_year' : 'year_comb',
#    'train_samples' :  ['TTLJ_powheg_Train', 'TTLJ_powheg_Test', 'CHToCB_Low_Train', 'CHToCB_Low_Test', ],
#    'variables' : {'include_mass_label':False, 'include_dijet_pt':True, 'include_ctagging':False, 'include_year_label':True},
#    'factory' : {
#      'name' : "TMVAClassification_DNN_Low_year_comb_Batch500_btagging",
#      'options' : ":".join(["!V",
#  	                  "!Silent",
#  			  "Color",
#  			  "DrawProgressBar",
#  			  "Transformations=I",
#  			  "AnalysisType=Classification",
#  		         ]),
#      #'weight' : "",
#      #'weight' : "1.",
#      'weight' : "XSWeight",
#    },
#  
#    'prepareTrees' : ":".join([
#                   #"SplitMode=Alternate",
#                   #"SplitMode=Random",
#                   #"MixMode=Random",
#  			     "!V",
#  			     #"nTrain_Signal=20000",
#  			     #"nTrain_Background=20000",
#  			     #"nTest_Signal=40000",
#  			     #"nTest_Background=40000",
#               	            ]),
#    'bookMethod' : [
#      {
#        'type' : ROOT.TMVA.Types.kPyKeras,
#        'name' : "DNN",
#        'options' : ":".join(["H",
#                              "!V",
#          		    #"VarTransform=N,D",
#          		    "VarTransform=N",
#          		    "FilenameModel=model_DNN_Low_year_comb_Batch500_btagging.h5",
#          		    "NumEpochs=100",
#                      "SaveBestOnly=true",
#          		    "BatchSize=500",
#                      "verbose=2",
#                      "TriesEarlyStopping=1",
#                      #"LearningRateSchedule=1,0.001;2,0.002;3,0.003;4,0.004;5,0.005;10,0.001",
#                      #"ValidationSize=0.2",
#          	           ]),
#      },
#    ],
#  },
#  'DNN_High_year_comb_Batch500_ctagging' : {
#    'train_year' : 'year_comb',
#    'train_samples' :  ['TTLJ_powheg_Train', 'TTLJ_powheg_Test', 'CHToCB_High_Train', 'CHToCB_High_Test', ],
#    'variables' : {'include_mass_label':False, 'include_dijet_pt':True, 'include_btagging':False , 'include_year_label':True},
#    'factory' : {
#      'name' : "TMVAClassification_DNN_High_year_comb_Batch500_ctagging",
#      'options' : ":".join(["!V",
#  	                  "!Silent",
#  			  "Color",
#  			  "DrawProgressBar",
#  			  "Transformations=I",
#  			  "AnalysisType=Classification",
#  		         ]),
#      #'weight' : "",
#      #'weight' : "1.",
#      'weight' : "XSWeight",
#    },
#  
#    'prepareTrees' : ":".join([
#                   #"SplitMode=Alternate",
#                   #"SplitMode=Random",
#                   #"MixMode=Random",
#  			     "!V",
#  			     #"nTrain_Signal=20000",
#  			     #"nTrain_Background=20000",
#  			     #"nTest_Signal=40000",
#  			     #"nTest_Background=40000",
#               	            ]),
#    'bookMethod' : [
#      {
#        'type' : ROOT.TMVA.Types.kPyKeras,
#        'name' : "DNN",
#        'options' : ":".join(["H",
#                              "!V",
#          		    #"VarTransform=N,D",
#          		    "VarTransform=N",
#          		    "FilenameModel=model_DNN_High_year_comb_Batch500_ctagging.h5",
#          		    "NumEpochs=100",
#                      "SaveBestOnly=true",
#          		    "BatchSize=500",
#                      "verbose=2",
#                      "TriesEarlyStopping=1",
#                      #"LearningRateSchedule=1,0.001;2,0.002;3,0.003;4,0.004;5,0.005;10,0.001",
#                      #"ValidationSize=0.2",
#          	           ]),
#      },
#    ],
#  },     
#        
#  'DNN_Low_year_comb_Batch500_ctagging' : {
#    'train_year' : 'year_comb',
#    'train_samples' :  ['TTLJ_powheg_Train', 'TTLJ_powheg_Test', 'CHToCB_Low_Train', 'CHToCB_Low_Test', ],
#    'variables' : {'include_mass_label':False, 'include_dijet_pt':True, 'include_btagging':False, 'include_year_label':True},
#    'factory' : {
#      'name' : "TMVAClassification_DNN_Low_year_comb_Batch500_ctagging",
#      'options' : ":".join(["!V",
#  	                  "!Silent",
#  			  "Color",
#  			  "DrawProgressBar",
#  			  "Transformations=I",
#  			  "AnalysisType=Classification",
#  		         ]),
#      #'weight' : "",
#      #'weight' : "1.",
#      'weight' : "XSWeight",
#    },
#  
#    'prepareTrees' : ":".join([
#                   #"SplitMode=Alternate",
#                   #"SplitMode=Random",
#                   #"MixMode=Random",
#  			     "!V",
#  			     #"nTrain_Signal=20000",
#  			     #"nTrain_Background=20000",
#  			     #"nTest_Signal=40000",
#  			     #"nTest_Background=40000",
#               	            ]),
#    'bookMethod' : [
#      {
#        'type' : ROOT.TMVA.Types.kPyKeras,
#        'name' : "DNN",
#        'options' : ":".join(["H",
#                              "!V",
#          		    #"VarTransform=N,D",
#          		    "VarTransform=N",
#          		    "FilenameModel=model_DNN_Low_year_comb_Batch500_ctagging.h5",
#          		    "NumEpochs=100",
#                      "SaveBestOnly=true",
#          		    "BatchSize=500",
#                      "verbose=2",
#                      "TriesEarlyStopping=1",
#                      #"LearningRateSchedule=1,0.001;2,0.002;3,0.003;4,0.004;5,0.005;10,0.001",
#                      #"ValidationSize=0.2",
#          	           ]),
#      },
#    ],
#  },
#})

options = OrderedDict({

  'DNN_High_year_comb_l21e-4' : {
    'train_year' : 'year_comb',
    'train_samples' :  ['TTLJ_powheg_Train', 'TTLJ_powheg_Test', 'CHToCB_High_Train', 'CHToCB_High_Test', ],
    'variables' : {'include_mass_label':False, 'include_dijet_pt':True, 'include_ctagging':False, 'include_year_label':True  },
    'model' : lambda: KerasModel(l2_norm=1e-4),
    'factory' : {
      'name' : "TMVAClassification_DNN_High_year_comb_l21e-4",
      'options' : ":".join(["!V",
  	                  "!Silent",
  			  "Color",
  			  "DrawProgressBar",
  			  "Transformations=I",
  			  "AnalysisType=Classification",
  		         ]),
      #'weight' : "",
      #'weight' : "1.",
      'weight' : "XSWeight*btagSF",
    },
  
    'prepareTrees' : ":".join([
                   #"SplitMode=Alternate",
                   #"SplitMode=Random",
                   #"MixMode=Random",
  			     "!V",
  			     #"nTrain_Signal=20000",
  			     #"nTrain_Background=20000",
  			     #"nTest_Signal=40000",
  			     #"nTest_Background=40000",
               	            ]),
    'bookMethod' : [
      {
        'type' : ROOT.TMVA.Types.kPyKeras,
        'name' : "DNN",
        'options' : ":".join(["H",
                              "!V",
          		    #"VarTransform=N,D",
          		    "VarTransform=N",
          		    "FilenameModel=model_DNN_High_year_comb_l21e-4.h5",
          		    "NumEpochs=100",
                      "SaveBestOnly=true",
          		    "BatchSize=500",
                      "verbose=2",
                      "TriesEarlyStopping=10",
                      #"LearningRateSchedule=1,0.001;2,0.002;3,0.003;4,0.004;5,0.005;10,0.001",
                      #"ValidationSize=0.2",
          	           ]),
      },
    ],
  },     
        
  'DNN_Low_year_comb_l21e-4' : {
    'train_year' : 'year_comb',
    'train_samples' :  ['TTLJ_powheg_Train', 'TTLJ_powheg_Test', 'CHToCB_Low_Train', 'CHToCB_Low_Test', ],
    'variables' : {'include_mass_label':False, 'include_dijet_pt':True , 'include_ctagging':False, 'include_year_label':True },
    'model' : lambda: KerasModel(l2_norm=1e-4),
    'factory' : {
      'name' : "TMVAClassification_DNN_Low_year_comb_l21e-4",
      'options' : ":".join(["!V",
  	                  "!Silent",
  			  "Color",
  			  "DrawProgressBar",
  			  "Transformations=I",
  			  "AnalysisType=Classification",
  		         ]),
      #'weight' : "",
      #'weight' : "1.",
      'weight' : "XSWeight*btagSF",
    },
  
    'prepareTrees' : ":".join([
                   #"SplitMode=Alternate",
                   #"SplitMode=Random",
                   #"MixMode=Random",
  			     "!V",
  			     #"nTrain_Signal=20000",
  			     #"nTrain_Background=20000",
  			     #"nTest_Signal=40000",
  			     #"nTest_Background=40000",
               	            ]),
    'bookMethod' : [
      {
        'type' : ROOT.TMVA.Types.kPyKeras,
        'name' : "DNN",
        'options' : ":".join(["H",
                              "!V",
          		    #"VarTransform=N,D",
          		    "VarTransform=N",
          		    "FilenameModel=model_DNN_Low_year_comb_l21e-4.h5",
          		    "NumEpochs=100",
                      "SaveBestOnly=true",
          		    "BatchSize=500",
                      "verbose=2",
                      "TriesEarlyStopping=10",
                      #"LearningRateSchedule=1,0.001;2,0.002;3,0.003;4,0.004;5,0.005;10,0.001",
                      #"ValidationSize=0.2",
          	           ]),
      },
    ],
  },
  'DNN_High_year_comb_l25e-3' : {
    'train_year' : 'year_comb',
    'train_samples' :  ['TTLJ_powheg_Train', 'TTLJ_powheg_Test', 'CHToCB_High_Train', 'CHToCB_High_Test', ],
    'variables' : {'include_mass_label':False, 'include_dijet_pt':True, 'include_ctagging':False, 'include_year_label':True  },
    'model' : lambda: KerasModel(l2_norm=5e-3),
    'factory' : {
      'name' : "TMVAClassification_DNN_High_year_comb_l25e-3",
      'options' : ":".join(["!V",
  	                  "!Silent",
  			  "Color",
  			  "DrawProgressBar",
  			  "Transformations=I",
  			  "AnalysisType=Classification",
  		         ]),
      #'weight' : "",
      #'weight' : "1.",
      'weight' : "XSWeight*btagSF",
    },
  
    'prepareTrees' : ":".join([
                   #"SplitMode=Alternate",
                   #"SplitMode=Random",
                   #"MixMode=Random",
  			     "!V",
  			     #"nTrain_Signal=20000",
  			     #"nTrain_Background=20000",
  			     #"nTest_Signal=40000",
  			     #"nTest_Background=40000",
               	            ]),
    'bookMethod' : [
      {
        'type' : ROOT.TMVA.Types.kPyKeras,
        'name' : "DNN",
        'options' : ":".join(["H",
                              "!V",
          		    #"VarTransform=N,D",
          		    "VarTransform=N",
          		    "FilenameModel=model_DNN_High_year_comb_l25e-3.h5",
          		    "NumEpochs=100",
                      "SaveBestOnly=true",
          		    "BatchSize=500",
                      "verbose=2",
                      "TriesEarlyStopping=10",
                      #"LearningRateSchedule=1,0.001;2,0.002;3,0.003;4,0.004;5,0.005;10,0.001",
                      #"ValidationSize=0.2",
          	           ]),
      },
    ],
  },     
        
  'DNN_Low_year_comb_l25e-3' : {
    'train_year' : 'year_comb',
    'train_samples' :  ['TTLJ_powheg_Train', 'TTLJ_powheg_Test', 'CHToCB_Low_Train', 'CHToCB_Low_Test', ],
    'variables' : {'include_mass_label':False, 'include_dijet_pt':True , 'include_ctagging':False, 'include_year_label':True },
    'model' : lambda: KerasModel(l2_norm=5e-3),
    'factory' : {
      'name' : "TMVAClassification_DNN_Low_year_comb_l25e-3",
      'options' : ":".join(["!V",
  	                  "!Silent",
  			  "Color",
  			  "DrawProgressBar",
  			  "Transformations=I",
  			  "AnalysisType=Classification",
  		         ]),
      #'weight' : "",
      #'weight' : "1.",
      'weight' : "XSWeight*btagSF",
    },
  
    'prepareTrees' : ":".join([
                   #"SplitMode=Alternate",
                   #"SplitMode=Random",
                   #"MixMode=Random",
  			     "!V",
  			     #"nTrain_Signal=20000",
  			     #"nTrain_Background=20000",
  			     #"nTest_Signal=40000",
  			     #"nTest_Background=40000",
               	            ]),
    'bookMethod' : [
      {
        'type' : ROOT.TMVA.Types.kPyKeras,
        'name' : "DNN",
        'options' : ":".join(["H",
                              "!V",
          		    #"VarTransform=N,D",
          		    "VarTransform=N",
          		    "FilenameModel=model_DNN_Low_year_comb_l25e-3.h5",
          		    "NumEpochs=100",
                      "SaveBestOnly=true",
          		    "BatchSize=500",
                      "verbose=2",
                      "TriesEarlyStopping=10",
                      #"LearningRateSchedule=1,0.001;2,0.002;3,0.003;4,0.004;5,0.005;10,0.001",
                      #"ValidationSize=0.2",
          	           ]),
      },
    ],
  },
  'DNN_High_year_comb_l21e-3' : {
    'train_year' : 'year_comb',
    'train_samples' :  ['TTLJ_powheg_Train', 'TTLJ_powheg_Test', 'CHToCB_High_Train', 'CHToCB_High_Test', ],
    'variables' : {'include_mass_label':False, 'include_dijet_pt':True, 'include_ctagging':False, 'include_year_label':True  },
    'model' : lambda: KerasModel(l2_norm=1e-3),
    'factory' : {
      'name' : "TMVAClassification_DNN_High_year_comb_l21e-3",
      'options' : ":".join(["!V",
  	                  "!Silent",
  			  "Color",
  			  "DrawProgressBar",
  			  "Transformations=I",
  			  "AnalysisType=Classification",
  		         ]),
      #'weight' : "",
      #'weight' : "1.",
      'weight' : "XSWeight*btagSF",
    },
  
    'prepareTrees' : ":".join([
                   #"SplitMode=Alternate",
                   #"SplitMode=Random",
                   #"MixMode=Random",
  			     "!V",
  			     #"nTrain_Signal=20000",
  			     #"nTrain_Background=20000",
  			     #"nTest_Signal=40000",
  			     #"nTest_Background=40000",
               	            ]),
    'bookMethod' : [
      {
        'type' : ROOT.TMVA.Types.kPyKeras,
        'name' : "DNN",
        'options' : ":".join(["H",
                              "!V",
          		    #"VarTransform=N,D",
          		    "VarTransform=N",
          		    "FilenameModel=model_DNN_High_year_comb_l21e-3.h5",
          		    "NumEpochs=100",
                      "SaveBestOnly=true",
          		    "BatchSize=500",
                      "verbose=2",
                      "TriesEarlyStopping=10",
                      #"LearningRateSchedule=1,0.001;2,0.002;3,0.003;4,0.004;5,0.005;10,0.001",
                      #"ValidationSize=0.2",
          	           ]),
      },
    ],
  },     
        
  'DNN_Low_year_comb_l21e-3' : {
    'train_year' : 'year_comb',
    'train_samples' :  ['TTLJ_powheg_Train', 'TTLJ_powheg_Test', 'CHToCB_Low_Train', 'CHToCB_Low_Test', ],
    'variables' : {'include_mass_label':False, 'include_dijet_pt':True , 'include_ctagging':False, 'include_year_label':True },
    'model' : lambda: KerasModel(l2_norm=1e-3),
    'factory' : {
      'name' : "TMVAClassification_DNN_Low_year_comb_l21e-3",
      'options' : ":".join(["!V",
  	                  "!Silent",
  			  "Color",
  			  "DrawProgressBar",
  			  "Transformations=I",
  			  "AnalysisType=Classification",
  		         ]),
      #'weight' : "",
      #'weight' : "1.",
      'weight' : "XSWeight*btagSF",
    },
  
    'prepareTrees' : ":".join([
                   #"SplitMode=Alternate",
                   #"SplitMode=Random",
                   #"MixMode=Random",
  			     "!V",
  			     #"nTrain_Signal=20000",
  			     #"nTrain_Background=20000",
  			     #"nTest_Signal=40000",
  			     #"nTest_Background=40000",
               	            ]),
    'bookMethod' : [
      {
        'type' : ROOT.TMVA.Types.kPyKeras,
        'name' : "DNN",
        'options' : ":".join(["H",
                              "!V",
          		    #"VarTransform=N,D",
          		    "VarTransform=N",
          		    "FilenameModel=model_DNN_Low_year_comb_l21e-3.h5",
          		    "NumEpochs=100",
                      "SaveBestOnly=true",
          		    "BatchSize=500",
                      "verbose=2",
                      "TriesEarlyStopping=10",
                      #"LearningRateSchedule=1,0.001;2,0.002;3,0.003;4,0.004;5,0.005;10,0.001",
                      #"ValidationSize=0.2",
          	           ]),
      },
    ],
  },
  #'BDT_High_year_comb' : {
  #  'train_year' : 'year_comb',
  #  'train_samples' :  ['TTLJ_powheg_Train', 'TTLJ_powheg_Test', 'CHToCB_High_Train', 'CHToCB_High_Test', ],
  #  'variables' : {'include_mass_label':False, 'include_dijet_pt':True , 'include_ctagging':False, 'include_year_label':True },
  #  'factory' : {
  #    'name' : "TMVAClassification_BDT_High_year_comb",
  #    'options' : ":".join(["!V",
  #	                  "!Silent",
  #			  "Color",
  #			  "DrawProgressBar",
  #			  "Transformations=I",
  #			  "AnalysisType=Classification",
  #		         ]),
  #    #'weight' : "",
  #    #'weight' : "1.",
  #    'weight' : "XSWeight*btagSF",
  #  },
  #
  #  'prepareTrees' : ":".join([
  #                 #"SplitMode=Alternate",
  #                 #"SplitMode=Random",
  #                 #"MixMode=Random",
  #			     "!V",
  #			     #"nTrain_Signal=20000",
  #			     #"nTrain_Background=20000",
  #			     #"nTest_Signal=40000",
  #			     #"nTest_Background=40000",
  #             	            ]),
  #  'bookMethod' : [
  #    {
  #      'type' : ROOT.TMVA.Types.kBDT,
  #      'name' : "BDT",
  #      'options' : ":".join(["!H",
  #                            "!V",
  #			    #"VarTransform=N,D",
  #			    "VarTransform=N",
  #                   	"NTrees=400",
  #        		    "MaxDepth=2",
  #                    "UseBaggedGrad=True",
  #                    "BaggedSampleFraction=0.5",
  #			        "MinNodeSize=5%",
  #                    "Shrinkage=0.1",
  #        		    "BoostType=Grad",
  #        		    "SeparationType=GiniIndex",
  #                    #"IgnoreNegWeightsInTraining=True",
  #                    "NegWeightTreatment=InverseBoostNegWeights",
  #        		    "nCuts=100",
  #        		    "PruneMethod=NoPruning",
  #        	           ])
  #    },
  #  ],
  #},     

  #'BDT_Low_year_comb' : {
  #  'train_year' : 'year_comb',
  #  'train_samples' :  ['TTLJ_powheg_Train', 'TTLJ_powheg_Test', 'CHToCB_Low_Train', 'CHToCB_Low_Test', ],
  #  'variables' : {'include_mass_label':False, 'include_dijet_pt':True , 'include_ctagging':False, 'include_year_label':True },
  #  'factory' : {
  #    'name' : "TMVAClassification_BDT_Low_year_comb",
  #    'options' : ":".join(["!V",
  #	                  "!Silent",
  #			  "Color",
  #			  "DrawProgressBar",
  #			  "Transformations=I",
  #			  "AnalysisType=Classification",
  #		         ]),
  #    #'weight' : "",
  #    #'weight' : "1.",
  #    'weight' : "XSWeight*btagSF",
  #  },
  #
  #  'prepareTrees' : ":".join([
  #                 #"SplitMode=Alternate",
  #                 #"SplitMode=Random",
  #                 #"MixMode=Random",
  #			     "!V",
  #			     #"nTrain_Signal=20000",
  #			     #"nTrain_Background=20000",
  #			     #"nTest_Signal=40000",
  #			     #"nTest_Background=40000",
  #             	            ]),
  #  'bookMethod' : [
  #    {
  #      'type' : ROOT.TMVA.Types.kBDT,
  #      'name' : "BDT",
  #      'options' : ":".join(["!H",
  #                            "!V",
  #			    #"VarTransform=N,D",
  #			    "VarTransform=N",
  #                   	"NTrees=800",
  #        		    "MaxDepth=2",
  #                    "UseBaggedGrad=True",
  #                    "BaggedSampleFraction=0.5",
  #			        "MinNodeSize=5%",
  #                    "Shrinkage=0.01",
  #        		    "BoostType=Grad",
  #        		    "SeparationType=GiniIndex",
  #                    #"IgnoreNegWeightsInTraining=True",
  #                    "NegWeightTreatment=InverseBoostNegWeights",
  #        		    "nCuts=100",
  #        		    "PruneMethod=NoPruning",
  #        	           ])
  #    },
  #  ],
  #},  

  
})

batch_size = [200,500,1000]
options = OrderedDict()
#keys = ['DNN_High_year_comb_{INDEX1}_{INDEX2}_{INDEX3}', 'DNN_Low_year_comb_{INDEX1}_{INDEX2}_{INDEX3}','DNN_High_dijet_M_year_comb_{INDEX1}_{INDEX2}_{INDEX3}', 'DNN_Low_dijet_M_year_comb_{INDEX1}_{INDEX2}_{INDEX3}',]
keys = ['DNN_High_year_comb_{INDEX1}_{INDEX2}_{INDEX3}', 'DNN_Low_year_comb_{INDEX1}_{INDEX2}_{INDEX3}',]
keys += ['DNN_dijet_M_year_comb_{INDEX1}_{INDEX2}_{INDEX3}', ]
for idx1 in range(3):
  for idx2 in range(3):
    for idx3 in range(3):
      for key in keys:
        options[key.format(INDEX1=idx1, INDEX2=idx2, INDEX3=idx3)] = {
          'train_year' : 'year_comb',
          'train_samples' :  ['TTLJ_powheg_Train', 'TTLJ_powheg_Test', 'CHToCB_High_Train', 'CHToCB_High_Test', ],
          'variables' : {'include_mass_label':False, 'include_dijet_pt':True, 'include_ctagging':False, 'include_year_label':True  },
          'model' : lambda: KerasModel(index1=idx1, index2=idx2),
          'factory' : {
            'name' : "TMVAClassification_" + key.format(INDEX1=idx1, INDEX2=idx2, INDEX3=idx3),
            'options' : ":".join(["!V",
        	                  "!Silent",
        			  "Color",
        			  "DrawProgressBar",
        			  "Transformations=I",
        			  "AnalysisType=Classification",
        		         ]),
            #'weight' : "",
            #'weight' : "1.",
            'weight' : "XSWeight*btagSF",
          },
        
          'prepareTrees' : ":".join([
                         #"SplitMode=Alternate",
                         #"SplitMode=Random",
                         #"MixMode=Random",
        			     "!V",
        			     #"nTrain_Signal=20000",
        			     #"nTrain_Background=20000",
        			     #"nTest_Signal=40000",
        			     #"nTest_Background=40000",
                     	            ]),
          'bookMethod' : [
            {
              'type' : ROOT.TMVA.Types.kPyKeras,
              'name' : "DNN",
              'options' : ":".join(["H",
                                    "!V",
                		    #"VarTransform=N,D",
                		    "VarTransform=N",
                		    "FilenameModel=model_"+ key.format(INDEX1=idx1, INDEX2=idx2, INDEX3=idx3) + ".h5",
                		    "NumEpochs=100",
                            "SaveBestOnly=true",
                		    "BatchSize={}".format(batch_size[idx3]),
                            "verbose=2",
                            "TriesEarlyStopping=10",
                            #"LearningRateSchedule=1,0.001;2,0.002;3,0.003;4,0.004;5,0.005;10,0.001",
                            #"ValidationSize=0.2",
                	           ]),
            },
          ],
        }
        #set trained samples
        if '_High_' in key:
          options[key.format(INDEX1=idx1, INDEX2=idx2, INDEX3=idx3)]['train_samples'] =  ['TTLJ_powheg_Train', 'TTLJ_powheg_Test', 'CHToCB_High_Train', 'CHToCB_High_Test', ]
        elif '_Low_' in key:
          options[key.format(INDEX1=idx1, INDEX2=idx2, INDEX3=idx3)]['train_samples'] =  ['TTLJ_powheg_Train', 'TTLJ_powheg_Test', 'CHToCB_Low_Train', 'CHToCB_Low_Test', ]
        else:
          options[key.format(INDEX1=idx1, INDEX2=idx2, INDEX3=idx3)]['train_samples'] =  ['TTLJ_powheg_Train', 'TTLJ_powheg_Test', 'CHToCB_Train', 'CHToCB_Test', ]

        #set variables
        if '_dijet_M_' in key:
            options[key.format(INDEX1=idx1, INDEX2=idx2, INDEX3=idx3)]['variables'] = {'include_mass_label':False, 'include_dijet_pt':True, 'include_ctagging':False, 'include_year_label':True, 'include_dijet_M':True, }
        else:
          options[key.format(INDEX1=idx1, INDEX2=idx2, INDEX3=idx3)]['variables'] = {'include_mass_label':False, 'include_dijet_pt':True, 'include_ctagging':False, 'include_year_label':True, 'include_dijet_M':False, }







if __name__ == '__main__':
    import pprint as pp
    pp.pprint(dict(options))
