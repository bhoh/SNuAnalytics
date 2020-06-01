#!/usr/bin/env python

import os, sys
sys.path.append(os.getcwd())
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

Debug = True
RootDir = 'Out_Roots'
LogDir  = 'Logs'
TMVAClassDir = 'TMVAClassDir'

if not os.path.isdir(RootDir):
  os.system('mkdir %s' % RootDir)
if not os.path.isdir(LogDir):
  os.system('mkdir %s' % LogDir)
if not os.path.isdir(LogDir):
  os.system('mkdir %s' % LogDir)
if not os.path.isdir(TMVAClassDir):
  os.system('mkdir %s' % TMVAClassDir)

from files_MVA_V11pre import *

#from test_MVA_files import *

#print file_names

train_years = [
  #'2016',
  '2017',
  #'2018'
]


sig_samples = [
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
bkg_samples = [
	'TTLJ_powheg',
	'WJetsToLNu-0J',
	'WJetsToLNu-1J',
	'WJetsToLNu-2J',
]

EW_samples = [
	'TTLJ_powheg',
	'WJetsToLNu-0J',
	'WJetsToLNu-1J',
	'WJetsToLNu-2J',
]
VBF_samples = [
	'HWW_VbfM200',
	'HWW_VbfM400',
	'HWW_VbfM800',
	'HWW_VbfM1000',
	'HWW_VbfM1500',
	'HWW_VbfM2000',
	'HWW_VbfM3000',
	'HWW_VbfM4000',
	'HWW_VbfM5000',
]


HWWggf_samples = [
        #'HWW_GgfM200',
        'HWW_GgfM400',
        #'HWW_GgfM800',
        #'HWW_GgfM1000',
        'HWW_GgfM1500',
        #'HWW_GgfM2000',
        #'HWW_GgfM3000',
        #'HWW_GgfM4000',
        #'HWW_GgfM5000',
]


spectators = OrderedDict()

#variables[''] = {
#    'name' : '',
#    'type' : 'F'
#  }

cuts = {}

BoostNoVbfSR = '(isBoostSR && !isVBF_Boost && nBJetBoost==0 && meP400_BstNoT_ggf_B>0)'
ResolNoVbfSR = '(isResolSR && !isVBF_Resol && nBJetResol==0 && meP400_ResNoT_ggf_B>0)'


# settings for isHighMassGGFClass --------------
isHighMassGGFClass = True
#W_recoCats = ["Boost"]
W_recoCats = ["Boost", "Resol"]
#VarWorkPtsCat = ["1500"]
VarWorkPtsCat = ["400","1500"]
GGFClass_bkg = {'EW': EW_samples}
#GGFClass_bkg = {'EW': EW_samples, 'VBF': VBF_samples}
##----------------------------------------
#
#
#spectators['isBoostSR'] = {
#    'definition' : 'isBoostSR',
#  }
#spectators['isVBF_Boost'] = {
#    'definition' : 'isVBF_Boost',
#  }
#spectators['nBJetBoost'] = {
#    'definition' : 'nBJetBoost',
#  }
#spectators['meP400_BstNoT_ggf_B'] = {
#    'definition' : 'meP400_BstNoT_ggf_B',
#  }
#
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
#    'weight' : "XSWeight*SFweight*METFilter_MC",
    'weight' : "baseW*Xsec",
  },
  'prepareTrees' : ":".join(["SplitMode=Alternate",
			     "!V",
			     # 0 (default): split half and half 
			     #"nTrain_Signal=5000",
			     #"nTrain_Background=5000",
			     #"nTest_Signal=5000",
			     #"nTest_Background=5000",
             	            ]),
  'bookMethod' : [
    {
      'type' : ROOT.TMVA.Types.kCuts,
      'name' : "RectCut",
      'options' : ":".join(["H",
                            "!V",
        		    "VarTransform=None",
			    "CutRangeMin[0]=0",
			    "CutRangeMax[0]=1.",
			    #"VarProp[0]=FSmart",
        	           ]),
    },
    #{
    #  'type' : ROOT.TMVA.Types.kPyKeras,
    #  'name' : "DNN",
    #  'options' : ":".join(["H",
    #                        "!V",
    #    		    "VarTransform=N,D",
    #    		    "FilenameModel=model.h5",
    #    		    "NumEpochs=20",
    #    		    "BatchSize=100",
    #    	           ]),
    #},
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



for train_year in train_years:
  if not isHighMassGGFClass:
    ml_tools =MLTools()
    ml_tools.SetMLTools(TMVATools)
    for bkg in bkg_samples:
      ml_tools.SetTrees(bkg,'Events',file_names[train_year, bkg])
      for sig in sig_samples:
        ml_tools.SetTrees(sig,'Events',file_names[train_year, sig])

      ml_tools.SetVariables(variables)
      ml_tools.SetSpectators(spectators)
      ml_tools.SetCuts(cuts)
      ml_tools.SetOptions(options)

      ml_tools.doTrain(
          ['%s_Events'%sig for sig in sig_samples],
          ['%s_Events'%bkg for bkg in bkg_samples],
          '%s'%train_year,'out_train_%s.root'%train_year)
      #
      #---------------------------------------------------
      #
      os.system('rm -rf TMVAClassification_%s'%(train_year))
      os.system('mv TMVAClassification TMVAClassification_%s'%(train_year))

      
      os.system('rm -rf out_root_%s_old'%(train_year))
      os.system('mv out_root_%s out_root_%s_old'%(train_year, train_year))
      os.system('mkdir out_root_%s'%(train_year))
      os.system('mv out_*.root out_root_%s'%(train_year))
  else: # HighMass Study
    for hGF in HWWggf_samples:
      if Debug:
	print 'For signal:', hGF, '=========================================='
      ggfmass = hGF.split('GgfM')[1]
      for workpt in VarWorkPtsCat: # s/b variable working points
        for idxW in W_recoCats:
          if Debug:
            print idxW
          variables = OrderedDict()
          if idxW is "Boost":
	    if Debug:
	      print  "i'm Boosted"
	    cuts['sig'] = BoostNoVbfSR
	    cuts['bkg'] = BoostNoVbfSR
	    varKey = "Bst_Pggfh"+workpt # we don't use this key name later
            definition = 'KD:= meP'+workpt+'_BstNoT_ggf_S/(meP'+workpt+'_BstNoT_ggf_S + 0.002*meP'+workpt+'_BstNoT_ggf_B)'
            #definition = 'P_SovB:= meP'+workpt+'_BstNoT_ggf_S/meP'+workpt+'_BstNoT_ggf_B'
          elif idxW is "Resol":
            if Debug:
              print "i'm Resolved"
            cuts['sig'] = ResolNoVbfSR
            cuts['bkg'] = ResolNoVbfSR
            varKey = "Res_Pggfh"+workpt
            definition = 'KD:= meP'+workpt+'_ResNoT_ggf_S/(meP'+workpt+'_ResNoT_ggf_S + 0.002*meP'+workpt+'_ResNoT_ggf_B)'
            #definition = 'P_SovB:= meP'+workpt+'_ResNoT_ggf_S/meP'+workpt+'_ResNoT_ggf_B'
          else:
	    pass

          if Debug:
            print varKey, definition
          variables[varKey] = {
              'definition' : definition,
              'type' : 'F'
              }

	  for bkgKey in GGFClass_bkg:
	    print 'for bkg:',bkgKey
	    if bkgKey is "EW":
              sgName = hGF.replace("HWW_", "")
              bgName = 'EW0p1'
	      label = train_year+'_'+varKey+'_'+sgName+'vs'+bgName
	      sys.stdout = open('%s/log_%s.txt'% (LogDir,label),'w')
              ml_tools =MLTools()
              ml_tools.SetMLTools(TMVATools)
	      if Debug:
	        print "add signal:",hGF
	      ml_tools.SetTrees(hGF, 'Events', file_names[train_year, hGF])
	      for bkg in GGFClass_bkg[bkgKey]:
		print 'adding bkg:',bkg
	        ml_tools.SetTrees(bkg, 'Events', file_names[train_year, bkg])

	      print 'For variables:', variables
              ml_tools.SetVariables(variables)
              ml_tools.SetSpectators(spectators)
	      print 'For cuts:',cuts
              ml_tools.SetCuts(cuts)
              ml_tools.SetOptions(options)

              ml_tools.doTrain(
                  ['%s_Events'% hGF ],
                  ['%s_Events'% bg for bg in GGFClass_bkg[bkgKey]],
                  '%s'%train_year,'out_train_%s.root'% label)
	      del ml_tools

              os.system('rm -rf %s/TClass_%s'% (TMVAClassDir, label))
              os.system('mv TMVAClassification %s/TClass_%s'% (TMVAClassDir, label) )
              os.system('rm -rf %s/out_train_%s_old.root'% (RootDir,label) )
              os.system('mv %s/out_train_%s.root %s/out_train_%s_old.root' %(RootDir, label, RootDir, label ))
              os.system('mv out_train_%s.root %s/'%(label, RootDir))
              os.system('mv signal_reference_cut.txt %s/sig_refCut_%s.txt'%(LogDir, label))
	      print 'Trainning End ================'

	    elif bkgKey is "VBF":
	      print 'VBF bkg case using the same mass to ggf higgs'
	      for bkg in GGFClass_bkg[bkgKey]:
	        vbfmass = bkg.split('VbfM')[1]
	        if vbfmass == ggfmass:
	          if Debug:
	            print "adding bkg", bkg
                  sgName = hGF.replace("HWW_", "")
                  bgName = bkg.replace("HWW_", "")
		  label = train_year+'_'+varKey+'_'+sgName+'vs'+bgName
		  sys.stdout = open('%s/log_%s.txt'% (LogDir,label),'w')

                  ml_tools =MLTools()
                  ml_tools.SetMLTools(TMVATools)
	          if Debug:
	            print "add signal:",hGF
	          ml_tools.SetTrees(hGF, 'Events', file_names[train_year, hGF])
	          ml_tools.SetTrees(bkg, 'Events', file_names[train_year, bkg])
		  print 'For variables:', variables
                  ml_tools.SetVariables(variables)
                  ml_tools.SetSpectators(spectators)
		  print 'For cuts:',cuts
                  ml_tools.SetCuts(cuts)
                  ml_tools.SetOptions(options)

                  ml_tools.doTrain(
                      ['%s_Events'% hGF ],
                      ['%s_Events'% bkg ],
                      '%s'%train_year,'out_train_%s.root'% label)
	          del ml_tools

                  os.system('rm -rf %s/TClass_%s'% (TMVAClassDir, label))
                  os.system('mv TMVAClassification %s/TClass_%s'% (TMVAClassDir, label) )
                  
                  os.system('rm -rf %s/out_train_%s_old.root'% (RootDir,label) )
                  os.system('mv %s/out_train_%s.root %s/out_train_%s_old.root' %(RootDir, label, RootDir, label ))
                  os.system('mv out_train_%s.root %s/'%(label, RootDir))
                  os.system('mv signal_reference_cut.txt %s/sig_refCut_%s.txt'%(LogDir, label))
		  print 'Trainning End ================'

	    #  else: # ggf EW comparision
	    #    if Debug:
	    #      print "adding bkg",bkg 
	    #    ml_tools.SetTrees(bkg, 'Events', file_names[train_year, bkg])

            #    #ml_tools.SetTrees(bkg,'Events',file_names[train_year, bkg])



