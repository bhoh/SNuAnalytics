#   def __init__(self, jetid=0, minpt=200.0, maxeta=2.4, max_tau21=0.45, mass_range=[65, 105],
#                    over_lepR =0.8, over_jetR = 0.8, input_branch_suffix="", output_branch_map=""):
##NOTE##
###HMSemilepSkimv6_5 has nanoAOD nominal JEC of CleanFatJet. ->Lastestone?
####->Check Jet_msoftdrop_nom == msoftdrop
####->Check Jet_pt_norm == Jet_pt
Steps={
    'CleanFatJet' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  'declare'    : 'fatjetMaker = lambda : FatJetMaker(jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8, input_branch_prefix="nom")',
                  'module'     : 'fatjetMaker()',
            'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',

    },

###---JES---##
    'CleanFatJet_JESup' : {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
        'declare'    : 'fatjetMaker_jesup = lambda : FatJetMaker( input_branch_prefix="jesTotalUp", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
        'module'     : 'fatjetMaker_jesup()',
        'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',

    },

    'CleanFatJet_JESdo' : {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
        'declare'    : 'fatjetMaker_jesdo = lambda : FatJetMaker( input_branch_prefix="jesTotalDown", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
        'module'     : 'fatjetMaker_jesdo()',
        'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
    },

###--JER----###
    'CleanFatJet_JERup' : {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
        'declare'    : 'fatjetMaker_jesup = lambda : FatJetMaker( input_branch_prefix="jerUp", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
        'module'     : 'fatjetMaker_jerup()',
        'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
    },

    'CleanFatJet_JERdo' : {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
        'declare'    : 'fatjetMaker_jerdo = lambda : FatJetMaker( input_branch_prefix="jerDown", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
        'module'     : 'fatjetMaker_jerdo()',
        'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',

    },
    


    ###---JMS---###
    'CleanFatJet_JMSup' : {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
        # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules                                                                                       
        'declare'    : 'fatjetMaker_jmsup = lambda : FatJetMaker( input_branch_prefix="jmsUp", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
        'module'     : 'fatjetMaker_jmsup()',
        'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
    },
    
    'CleanFatJet_JMSdo' : {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
        # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules                                                                                       
        'declare'    : 'fatjetMaker_jmsdo = lambda : FatJetMaker( input_branch_prefix="jmsDown", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
        'module'     : 'fatjetMaker_jmsdo()',
        'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
    },

    'CleanFatJet_JMRup' : {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
        # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules                                                                                       
        'declare'    : 'fatjetMaker_jmrup = lambda : FatJetMaker( input_branch_prefix="jmrUp", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
        'module'     : 'fatjetMaker_jmrup()',
        'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
    },
    'CleanFatJet_JMRdo' : {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
        'declare'    : 'fatjetMaker_jmrdo = lambda : FatJetMaker( input_branch_prefix="jmrDown", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
        'module'     : 'fatjetMaker_jmrdo()',
        'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
    },

}
