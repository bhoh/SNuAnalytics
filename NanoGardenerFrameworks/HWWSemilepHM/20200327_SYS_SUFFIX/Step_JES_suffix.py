##---For suffix based, you should run from JES variation to your kinematics producer(analysis) 
#Add branch names you want to do jes variation and save here
##-->LatinoAnalysis.NanoGardener.data.BranchMapping_cfg
import os
Steps={

    'HMlnjjVars_Dev_jhchoi7' : {
        'isChain'    : False ,
        'do4MC'      : True ,
        'do4Data'    : True ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi7',
        'declare'    : 'HMlnjjVars_Dev_jhchoi = lambda : HMlnjjVarsClass_Dev_jhchoi(RPLME_YEAR)',
        'module' : 'HMlnjjVars_Dev_jhchoi()'
        ##    def __init__(self,year,METtype='PuppiMET,',doSkim=False,doHardSkim=False):                                                                                              
        
    },

    
    'JESBase' : {
        'isChain'    : False ,
        'do4MC'      : True  ,
        'do4Data'    : False  ,
        'import'     : 'LatinoAnalysis.NanoGardener.modules.JECMaker' ,
        'declare'    : 'JES = lambda : JECMaker(globalTag="Regrouped_RPLME_JESGT", types=["Total", "Absolute", "Absolute_RPLME_YEAR", "BBEC1", "BBEC1_RPLME_YEAR", "EC2", "EC2_RPLME_YEAR", "FlavorQCD", "HF", "HF_RPLME_YEAR", "RelativeBal", "RelativeSample_RPLME_YEAR"], jetFlav="AK4PFchs")',
        'module'     : 'JES()',
    },

}



#####---For JES sources and variations----#######
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

for var in ['up','do']:

    Steps['JES'+var+'_suffix']={ ##Add branches for all JES sources
        'isChain'    : True ,
        'do4MC'      : True ,
        'do4Data'    : False  ,
        'subTargets' : ['JESBase'] ##Variation from sources will be added @next loop
        #'subTargets' : ['JESBase','do_JES'+var+'_'+jes_source+'_suffix','formulasMC_JES'+var+'_'+jes_source],
        'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'

    }    



    for jes_source in LIST_JES_SOURCE:

        Steps['JES'+var+'_suffix']['subTargets'].append('do_JES'+var+'_'+jes_source+'_suffix') ## This appended step will be defined at the next lines
        Steps['JES'+var+'_suffix']['subTargets'].append('formulasMC_JES'+var+'_'+jes_source) ## This appended step will be defined at the next lines
        Steps['JES'+var+'_suffix']['subTargets'].append('HMlnjjVars_Dev_jhchoi7'+'_JES'+var+'_'+jes_source) ## This analysis step must be defined at the next lines

        Steps['do_JES'+var+'_'+jes_source+'_suffix'] = { ##do means execute
            'isChain'    : False ,
            'do4MC'      : True  ,
            'do4Data'    : False  ,
            'import'     : 'LatinoAnalysis.NanoGardener.modules.PtCorrApplier',
            'declare'    : 'JES'+jes_source+var+' = lambda : PtCorrApplier(Coll="CleanJet", CorrSrc="jecUncert'+jes_source+'", kind="'+VAR_KIND_DICT[var]+'", doMET=True, METobjects = ["MET","PuppiMET","RawMET"],suffix="_JES'+jes_source+var'"))',
            'module'     : 'JES'+jes_source+var+'()',

        }
        
        Steps['formulasMC_JES'+var+'_'+jes_source]={
            
            'isChain'    : False ,
            'do4MC'      : True  ,
            'do4Data'    : False  ,
            'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
            'declare'    : '',
            'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_YEAR.py\', branch_map="JES'+jes_source+var+'")' ,
            
        }
        Stpes['HMlnjjVars_Dev_jhchoi7'+'_JES'+var+'_'+jes_source] ={
            'isChain'    : False ,
            'do4MC'      : True ,
            'do4Data'    : True ,
            'import'     : 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi7',
            'declare'    : 'HMlnjjVars_Dev_jhchoi = lambda : HMlnjjVarsClass_Dev_jhchoi(RPLME_YEAR,bracn_map="JES'+jes_source+var+'")',
            #    def __init__(self,year,doSkim=False,doHardSkim=False,branch_map=''):

            'module' : 'HMlnjjVars_Dev_jhchoi()'
            ##    def __init__(self,year,METtype='PuppiMET,',doSkim=False,doHardSkim=False):                                                                                              


        }

    ##So, for JESup_suffix -> JESBase -> do_JESup_<SOURCE>_suffix -> formulasMC_JESup_<SOURCE>
