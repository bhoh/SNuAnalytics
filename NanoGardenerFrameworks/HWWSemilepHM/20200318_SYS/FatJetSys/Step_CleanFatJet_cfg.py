import os
#   def __init__(self, jetid=0, minpt=200.0, maxeta=2.4, max_tau21=0.45, mass_range=[65, 105],
#                    over_lepR =0.8, over_jetR = 0.8, input_branch_suffix="", output_branch_map=""):
##NOTE##
###HMSemilepSkimv6_5 has nanoAOD nominal JEC of CleanFatJet. ->Lastestone?
####->Check Jet_msoftdrop_nom == msoftdrop
####->Check Jet_pt_norm == Jet_pt
Steps={
    'CleanFatJet' : {#input_branch_suffix
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  'declare'    : 'fatjetMaker = lambda : FatJetMaker(jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8, input_branch_suffix="nom")',
                  'module'     : 'fatjetMaker()',
            'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',

    },

###---JES---##
    'CleanFatJet_JESup' : {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
        'declare'    : 'fatjetMaker_jesup = lambda : FatJetMaker( input_branch_suffix="jesTotalUp", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
        'module'     : 'fatjetMaker_jesup()',
        'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',

    },

    'CleanFatJet_JESdo' : {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
        'declare'    : 'fatjetMaker_jesdo = lambda : FatJetMaker( input_branch_suffix="jesTotalDown", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
        'module'     : 'fatjetMaker_jesdo()',
        'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
    },

###--JER----###
    'CleanFatJet_JERup' : {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
        'declare'    : 'fatjetMaker_jerup = lambda : FatJetMaker( input_branch_suffix="jerUp", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
        'module'     : 'fatjetMaker_jerup()',
        'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
    },

    'CleanFatJet_JERdo' : {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
        'declare'    : 'fatjetMaker_jerdo = lambda : FatJetMaker( input_branch_suffix="jerDown", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
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
        'declare'    : 'fatjetMaker_jmsup = lambda : FatJetMaker( input_branch_suffix="jmsUp", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
        'module'     : 'fatjetMaker_jmsup()',
        'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
    },
    
    'CleanFatJet_JMSdo' : {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
        # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules                                                                                       
        'declare'    : 'fatjetMaker_jmsdo = lambda : FatJetMaker( input_branch_suffix="jmsDown", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
        'module'     : 'fatjetMaker_jmsdo()',
        'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
    },

    'CleanFatJet_JMRup' : {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
        # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules                                                                                       
        'declare'    : 'fatjetMaker_jmrup = lambda : FatJetMaker( input_branch_suffix="jmrUp", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
        'module'     : 'fatjetMaker_jmrup()',
        'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
    },
    'CleanFatJet_JMRdo' : {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
        'declare'    : 'fatjetMaker_jmrdo = lambda : FatJetMaker( input_branch_suffix="jmrDown", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
        'module'     : 'fatjetMaker_jmrdo()',
        'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',
    },


    'HMlnjjVars_Dev_jhchoi6':  {
        'isChain'    : False ,
        'do4MC'      : True ,
        'do4Data'    : True ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi6',
        'declare'    : 'HMlnjjVars_Dev_jhchoi = lambda : HMlnjjVarsClass_Dev_jhchoi(RPLME_YEAR,METtype="PuppiMET")',
        'module' : 'HMlnjjVars_Dev_jhchoi()'
        ##    def __init__(self,year,METtype='PuppiMET,',doSkim=False,doHardSkim=False):
    },

    'HMlnjjVars_Dev_jhchoi7':  {
        'isChain'    : False ,
        'do4MC'      : True ,
        'do4Data'    : True ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi7',
        'declare'    : 'HMlnjjVars_Dev_jhchoi = lambda : HMlnjjVarsClass_Dev_jhchoi(RPLME_YEAR,METtype="PuppiMET")',
        'module' : 'HMlnjjVars_Dev_jhchoi()'
        ##    def __init__(self,year,METtype='PuppiMET,',doSkim=False,doHardSkim=False):
    }


}

LIST_SOURCE=['JES','JER','JMS','JMR']
LIST_VAR=['up','do']
for SOURCE in LIST_SOURCE:
    for VAR in LIST_VAR:
        Steps['HMlnjjVars_Dev_jhchoi6_FAT'+SOURCE+VAR]={
            'isChain' : True,
            'do4MC' : True,
            'do4Data' : False,
            'subTargets' : ['CleanFatJet_'+SOURCE+VAR,'HMlnjjVars_Dev_jhchoi6'],
            'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',

        }

        Steps['FAT'+SOURCE+VAR+'_HMVAR7']={
            'isChain' : True,
            'do4MC' : True,
            'do4Data' : False,
            'subTargets' : ['CleanFatJet_'+SOURCE+VAR,'HMlnjjVars_Dev_jhchoi7'],
            'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200318_SYS/semilep_branch_jhchoi.txt',

        }
        


#for key in Steps:
#    print key
