import os
import copy

Steps = {
  'ElepTup' :   {
    'isChain'    : True ,
    'do4MC'      : True  ,
    'do4Data'    : False  ,
    'subTargets' : ['do_ElepTup','trigMCKeepRun','LeptonSF','formulasMC'],
    'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
               },

  'ElepTdo' :   {
      'isChain'    : True ,
      'do4MC'      : True  ,
      'do4Data'    : False  ,
      'subTargets' : ['do_ElepTdo','trigMCKeepRun','LeptonSF','formulasMC'],
      'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
  },
  'MupTup' :   {
    'isChain'    : True ,
    'do4MC'      : True  ,
    'do4Data'    : False  ,
    'subTargets' : ['do_MupTup','trigMCKeepRun','LeptonSF','formulasMC'],
    'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
  },

  'MupTdo' :   {
    'isChain'    : True ,
    'do4MC'      : True  ,
    'do4Data'    : False  ,
    'subTargets' : ['do_MupTdo','trigMCKeepRun','LeptonSF','formulasMC'],
    'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
  },

  'METup' :   {
     'isChain'    : True ,
     'do4MC'      : True  ,
     'do4Data'    : False  ,
     'subTargets' : ['do_METup','formulasMC'],
     'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
   },
   'METdo' :   {
       'isChain'    : True ,
       'do4MC'      : True  ,
       'do4Data'    : False  ,
       'subTargets' : ['do_METdo','formulasMC'],
       'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
   },



  'do_ElepTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'ElepTup = lambda : LeppTScalerTreeMaker(kind="Up", lepFlavor="ele", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"])',
                  'module'     : 'ElepTup()',
                },
  'trigMCKeepRun' : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigMCKR = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=True)',
                 'module'     : 'trigMCKR()',
               },

  'LeptonSF' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSFMaker' ,
                  'declare'    : 'LeptonSF = lambda : LeptonSFMaker("RPLME_CMSSW")',
                  'module'     : 'LeptonSF()',
                },

  'formulasMC' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_YEAR.py\')' ,
                 },

  'do_ElepTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'ElepTdo = lambda : LeppTScalerTreeMaker(kind="Dn", lepFlavor="ele", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"])',
                  'module'     : 'ElepTdo()',
                },

  'do_MupTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'MupTdo = lambda : LeppTScalerTreeMaker(kind="Dn", lepFlavor="mu", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"])',
                  'module'     : 'MupTdo()',
                },

  'do_MupTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'MupTup = lambda : LeppTScalerTreeMaker(kind="Up", lepFlavor="mu", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"])',
                  'module'     : 'MupTup()',
                },
  'do_METup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.MetUnclustered',
                  'declare'    : 'METup = lambda : MetUnclusteredTreeMaker(kind="Up",metCollections=["MET", "PuppiMET", "RawMET"])',
                  'module'     : 'METup()',
                },

  'do_METdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.MetUnclustered',
                  'declare'    : 'METDo = lambda : MetUnclusteredTreeMaker(kind="Dn",metCollections=["MET", "PuppiMET", "RawMET"])',
                  'module'     : 'METDo()',
                },

    ##analysis code
  'HMlnjjVars_Dev_jhchoi7' : {
    'isChain'    : False ,
    'do4MC'      : True ,
    'do4Data'    : True ,
    'import'     : 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi7',
    'declare'    : 'HMlnjjVars_Dev_jhchoi = lambda : HMlnjjVarsClass_Dev_jhchoi(RPLME_YEAR,METtype="PuppiMET")',
    'module' : 'HMlnjjVars_Dev_jhchoi()'

  },



}


##Add HMSmemilep variables
for SYS in ['ElepTup','ElepTdo','MupTup','MupTdo','METup','METdo']:
    Steps[SYS+'_HMVAR7']=copy.deepcopy(Steps[SYS])
    Steps[SYS+'_HMVAR7']['subTargets'].append('HMlnjjVars_Dev_jhchoi7')



