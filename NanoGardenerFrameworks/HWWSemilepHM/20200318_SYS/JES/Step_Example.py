Steps={

    'JESup_Absolute' :   {
        'isChain'    : True ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'subTargets' : ['JESBase','do_JESup_Absolute','formulasMC'],
        'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
        
    },
    
    'JESBase' : {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.JECMaker' ,
        'declare'    : 'JES = lambda : JECMaker(globalTag="Regrouped_RPLME_JESGT", types=["Total", "Absolute", "Absolute_RPLME_YEAR", "BBEC1", "BBEC1_RPLME_YEAR", "EC2", "EC2_RPLME_YEAR", "Flav\
orQCD", "HF", "HF_RPLME_YEAR", "RelativeBal", "RelativeSample_RPLME_YEAR"], jetFlav="AK4PFchs")',
        'module'     : 'JES()',
    },
    
    
    
    ##                                                                                                                                                                                                          
    
    'do_JESup_Absolute' : {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.PtCorrApplier',
        'declare'    : 'JESAbsoluteup = lambda : PtCorrApplier(Coll="CleanJet", CorrSrc="jecUncertAbsolute", kind="up", doMET=True, METobjects = ["MET","PuppiMET","RawMET"])',
        'module'     : 'JESAbsoluteup()',
        
    }
    

#Steps
