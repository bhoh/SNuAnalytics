import os
Steps={
  'formulasMC' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_YEAR.py\')' ,
                 },

    
    'JESBase' : {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.JECMaker' ,
        'declare'    : 'JES = lambda : JECMaker(globalTag="Regrouped_RPLME_JESGT", types=["Total", "Absolute", "Absolute_RPLME_YEAR", "BBEC1", "BBEC1_RPLME_YEAR", "EC2", "EC2_RPLME_YEAR", "FlavorQCD", "HF", "HF_RPLME_YEAR", "RelativeBal", "RelativeSample_RPLME_YEAR"], jetFlav="AK4PFchs")',
        'module'     : 'JES()',
    },
    
    
    

    
    'do_JESup_Absolute' : {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.PtCorrApplier',
        'declare'    : 'JESAbsoluteup = lambda : PtCorrApplier(Coll="CleanJet", CorrSrc="jecUncertAbsolute", kind="up", doMET=True, METobjects = ["MET","PuppiMET","RawMET"])',
        'module'     : 'JESAbsoluteup()',
        
    },
    
    'JESup_Absolute' :   {
        'isChain'    : True ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'subTargets' : ['JESBase','do_JESup_Absolute','formulasMC'],
        'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
        
    },

}

VAR_KIND_DICT={
'do':'Do',
'up':'Up'
}
##JES sources##
LIST_JES_SOURCE=['Total', 'Absolute',  'BBEC1', 'EC2',  'FlavorQCD', 'HF',  'RelativeBal']
for yr in ['2016','2017','2018']:
    LIST_JES_SOURCE+=['Absolute_'+yr, 'BBEC1_'+yr, 'EC2_'+yr, 'HF_'+yr, 'RelativeSample_'+yr ]
##End of defining JES sources## 

##--up/down steps--##
for jes_source in LIST_JES_SOURCE:
    for var in ['up','do']:
        Steps['JES'+var+'_'+jes_source]={
            'isChain'    : True ,
            'do4MC'      : True  ,
            'do4Data'    : False  ,
            'subTargets' : ['JESBase','do_JES'+var+'_'+jes_source,'formulasMC'],
            'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
        }

        Steps['do_JES'+var+'_'+jes_source] = { ##do means execute
            'isChain'    : False ,
            'do4MC'      : True  ,
            'do4Data'    : False  ,
            'import'     : 'LatinoAnalysis.NanoGardener.modules.PtCorrApplier',
            'declare'    : 'JES'+jes_source+var+' = lambda : PtCorrApplier(Coll="CleanJet", CorrSrc="jecUncert'+jes_source+'", kind="'+VAR_KIND_DICT[var]+'", doMET=True, METobjects = ["MET","PuppiMET","RawMET"])',
            'module'     : 'JES'+jes_source+var+'()',

        }

