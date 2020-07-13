Periods=['A','B','C','D','E','F','G','H']
Years=['2016','2017','2018']

##--To get sample names from DATA samples--##
from LatinoAnalysis.NanoGardener.framework.samples.Run2016_102X_nAODv5 import Samples as DATA2016v5
from LatinoAnalysis.NanoGardener.framework.samples.Run2017_102X_nAODv5 import Samples as DATA2017v5
from LatinoAnalysis.NanoGardener.framework.samples.Run2018_102X_nAODv6 import Samples as DATA2018v6


##--Datasets  we are using
ALLDATAS=DATA2016v5.keys()+DATA2017v5.keys()+DATA2018v6.keys()



##--To make list of datasetname sored in period
DATAbyPeriod={} ##e.g DATAbyPeriod['B'] => list of datasamples names with period B
for p in Periods:
    DATAbyPeriod[p]=[]
for d in ALLDATAS:
    #print d
    for p in Periods:
        for yr in Years:
            if "Run"+yr+p in d:
                DATAbyPeriod[p].append(d)


Steps={}##initialize steps dictionary

##define one by one
Steps['CorrJetMC'] =  {
    'isChain': False,
    'do4MC': True,
    'do4Data': False,
    'import': 'LatinoAnalysis.NanoGardener.modules.jetmetHelperRun2Regrouped',
#    'declare': 'corr_jet_mc = createJMECorrector(isMC=True,dataYear=RPLME_YEAR, jesUncert="Total,Absolute,BBEC1,EC2,FlavorQCD,HF,RelativeBal,Absolute_RPLME_YEAR,BBEC1_RPLME_YEAR,EC2_RPLME_YEAR,HF_RPLME_YEAR,RelativeSample_RPLME_YEAR", redojec=True, jetType="AK4PFchs")',
    'declare': 'corr_jet_mc = createJMECorrector(isMC=True,dataYear=RPLME_YEAR, jesUncert="All", redojec=True, jetType="AK4PFchs")',
    'module':  'corr_jet_mc()'
}

Steps['CorrJetDATA'] =  { ## period inclusive
    'isChain': True,
    'do4MC': False,
    'do4Data': True,
    'subTargets':[]
}


Steps['CorrFatJetMC'] =  {
    'isChain': False,
    'do4MC': True,
    'do4Data': False,
    'import': 'LatinoAnalysis.NanoGardener.modules.jetmetHelperRun2Regrouped',
    'declare': 'corr_fatjet_mc = createJMECorrector(isMC=True,dataYear=RPLME_YEAR, jesUncert="Total", redojec=True, jetType="AK8PFPuppi")',
    'module':  'corr_fatjet_mc()'
}

Steps['CorrFatJetDATA'] =  { ## period inclusive
    'isChain': True,
    'do4MC': False,
    'do4Data': True,
    'subTargets':[]
}

for period in Periods:
    ##AK4
    Steps['CorrJetDATA']['subTargets'].append('CorrJetDATA_'+period) ##includes steps for all periods

    
    Steps['CorrJetDATA_'+period] =  { ## CorrJetDATA_B -> onlySample : sample list with period B
        'isChain': False,
        'do4MC': False,
        'do4Data': True,
        'import': 'LatinoAnalysis.NanoGardener.modules.jetmetHelperRun2Regrouped',
        'declare': 'corr_jet_data'+period+' = createJMECorrector(isMC=False,dataYear=RPLME_YEAR,runPeriod="'+period+'", jesUncert="Total",redojec=True, jetType="AK4PFchs")',
        'module':  'corr_jet_data'+period+'()',
        'onlySample':DATAbyPeriod[period]
    }
    ##AK8
    Steps['CorrFatJetDATA']['subTargets'].append('CorrFatJetDATA_'+period) ##includes steps for all periods
    Steps['CorrFatJetDATA_'+period] =  { ## CorrJetDATA_B -> onlySample : sample list with period B 
        'isChain': False,
        'do4MC': False,
        'do4Data': True,
        'import': 'LatinoAnalysis.NanoGardener.modules.jetmetHelperRun2Regrouped',
        'declare': 'corr_fatjet_data'+period+' = createJMECorrector(isMC=False,dataYear=RPLME_YEAR,runPeriod="'+period+'", jesUncert="Total",redojec=True, jetType="AK8PFPuppi")',
        'module':  'corr_fatjet_data'+period+'()',
        'onlySample':DATAbyPeriod[period]
    }

##--corrMET
Steps['CorrMET'] = {
    'isChain'    : False ,
    'do4MC'      : True  ,
    'do4Data'    : True  ,
    'import'  : 'LatinoAnalysis.NanoGardener.modules.JetNomToMETPropagation',
    'declare' : 'corrmet = lambda : JetNomToMETPropagation()',
    'module'  : 'corrmet()'
}

##HEMweight
Steps['HEMweightMC'] ={#HEMweight.py##2018                                                                                                                                                                       
    'isChain'    : False ,
    'do4MC'      : True  ,
    'do4Data'    : False  ,
    'import'  : 'LatinoAnalysis.NanoGardener.modules.HEMweight',
    'declare' : 'HEMVeto2018 = lambda : HEMweight(isData=False, dataYear=RPLME_YEAR,jetColl="CleanJet",cmssw = "Full2018",seed=65539)',
    'module'  : 'HEMVeto2018()'
    
}


Steps['HEMweightDATA'] ={#HEMweight.py##2018                                                                                                                                                                     
    'isChain'    : False ,
    'do4MC'      : False  ,
    'do4Data'    : True  ,
    'import'  : 'LatinoAnalysis.NanoGardener.modules.HEMweight',
    'declare' : 'HEMVeto2018 = lambda : HEMweight(isData=True, dataYear=RPLME_YEAR,jetColl="CleanJet",cmssw = "Full2018",seed=65539)',
    'module'  : 'HEMVeto2018()'
    
}

#for s in  Steps['CorrJetDATA_C']['onlySample']:
#    print s


##Now All necessary steps are defined

Steps['HMSemilepSKIMv6_10']= { ##To ReRun CleanFatJet                                                                                                                                                          
    'isChain'    : True  ,
    'do4MC'      : True  ,
    'do4Data'    : False  ,
    'selection'  :'"( (Lepton_pt[0]>20) && ( Alt$( Lepton_pt[1],-1) < 20 ) )"',
    'subTargets' : ['wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK','CorrJetMC', 'CorrFatJetMC','CorrMET','HEMweightMC'],
}##['wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK',

Steps['HMSemilepSKIMv6_10_test']= { ##To ReRun CleanFatJet                                                                                                                                                          
    'isChain'    : True  ,
    'do4MC'      : True  ,
    'do4Data'    : False  ,
    'selection'  :'"( Entry$ < 100 )"',
    'subTargets' : ['wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK','CorrJetMC', 'CorrFatJetMC','CorrMET','HEMweightMC'],
}##['wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK',


Steps['HMSemilepSKIMv6_10_test_dummy']= { ##To ReRun CleanFatJet                                                                                                                                                          
    'isChain'    : True  ,
    'do4MC'      : True  ,
    'do4Data'    : False  ,
    'selection'  :'"( Entry$ < 100 )"',
    'subTargets' : ['wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK','CorrJetMC', 'CorrFatJetMC','HEMweightMC'],
}##['wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK',


Steps['HMSemilepSKIMv6_10_data']= { ##To ReRun CleanFatJet                                                                                                                                                          
    'isChain'    : True  ,
    'do4MC'      : False  ,
    'do4Data'    : True  ,
    'selection'  :'"( (Lepton_pt[0]>20) && ( Alt$( Lepton_pt[1],-1) < 20 ) )"',
    'subTargets' : ['CorrJetDATA', 'CorrFatJetDATA','CorrMET','HEMweightDATA'],
}

Steps['HMSemilepSKIMv6_10_data_test']= { ##To ReRun CleanFatJet                                                                                                                                                          
    'isChain'    : True  ,
    'do4MC'      : False  ,
    'do4Data'    : True  ,
    'selection'  :'"(Entry$ < 100)"',
    'subTargets' : ['CorrJetDATA', 'CorrFatJetDATA','CorrMET','HEMweightDATA'],
}
Steps['HMSemilepSKIMv6_10_data_test_dummy']= { ##To ReRun CleanFatJet                                                                                                                                                          
    'isChain'    : True  ,
    'do4MC'      : False  ,
    'do4Data'    : True  ,
    'selection'  :'"(Entry$ < 100)"',
    'subTargets' : ['CorrJetDATA', 'CorrFatJetDATA','HEMweightDATA'],
}








Steps['wwNLOEWK'] = {
    'isChain'    : False ,
    'do4MC'      : True  ,
    'do4Data'    : False  ,
    'import'     : 'LatinoAnalysis.NanoGardener.modules.qq2vvEWKcorrectionsWeightProducer' ,
    'declare'    : 'wwNLOEWK = lambda : vvNLOEWKcorrectionWeightProducer("ww")',
    'module'     : 'wwNLOEWK()',
    'onlySample' : [ 'WWTo2L2Nu', 'WWTo2L2Nu_CP5Up', 'WWTo2L2Nu_CP5Down',
                     'WmToLNu_WmTo2J_QCD', 'WpToLNu_WpTo2J_QCD', 'WpToLNu_WmTo2J_QCD', 'WpTo2J_WmToLNu_QCD','WW-LO','WWToLNuQQ','WpWmJJ_EWK_noTop','WpWmJJ_QCD_noTop','WpWmJJ_EWK_QCD_noHiggs','WpWmJJ_EWK_QCD_noTop_noHiggs','WWToLNuQQ','WWToLNuQQ_AMCNLOFXFX','WWToLNuQQ_AMCATNLO'
                 ]
} 
Steps['wzNLOEWK'] = {
    'isChain'    : False ,
    'do4MC'      : True  ,
    'do4Data'    : False  ,
    'import'     : 'LatinoAnalysis.NanoGardener.modules.qq2vvEWKcorrectionsWeightProducer' ,
    'declare'    : 'wzNLOEWK = lambda : vvNLOEWKcorrectionWeightProducer("wz")',
    'module'     : 'wzNLOEWK()',
    'onlySample' : ['WZTo3LNu', 'WZTo3LNu_ext1', 'WZTo2L2Q', 'WZTo3LNu_mllmin01', 'WZTo3LNu_powheg',
                    'WmTo2J_ZTo2L_QCD', 'WmToLNu_ZTo2J_QCD', 'WpTo2J_ZTo2L_QCD', 'WpToLNu_ZTo2J_QCD','WZ','WZ_ext',
                ]
} 
Steps['zzNLOEWK'] = {
    'isChain'    : False ,
    'do4MC'      : True  ,
    'do4Data'    : False  ,
    'import'     : 'LatinoAnalysis.NanoGardener.modules.qq2vvEWKcorrectionsWeightProducer' ,
    'declare'    : 'zzNLOEWK = lambda : vvNLOEWKcorrectionWeightProducer("zz")',
    'module'     : 'zzNLOEWK()',
    'onlySample' : ['ZZTo2L2Nu','ZZTo2L2Nu_ext1','ZZTo2L2Nu_ext2', 'ZZTo4L','ZZTo4L_ext1','ZZTo4L_ext2', 'ZZTo2L2Q',
                    'ZTo2L_ZTo2J_QCD','ZZ','ZZ_ext1',
            ]
} 
Steps['wNLOEWK'] = {
    'isChain'    : False ,
    'do4MC'      : True  ,
    'do4Data'    : False  ,
    'import'     : 'LatinoAnalysis.NanoGardener.modules.qq2VEWKcorrectionsWeightProducer' ,
    'declare'    : 'wNLOEWK = lambda : vNLOEWKcorrectionWeightProducer("w")',
    'module'     : 'wNLOEWK()',
    'onlySample' : [
        ####                                                                                                                                            
        'WJetsToLNu-LO','WJetsToLNu-LO_ext1'
        'WJetsToLNu','WJetsToLNu_ext2',
        'WJetsToLNu_HT70_100','WJetsToLNu_HT100_200',
        'WJetsToLNu_HT200_400','WJetsToLNu_HT400_600',
        'WJetsToLNu_HT600_800','WJetsToLNu_HT800_1200',
        'WJetsToLNu_HT1200_2500','WJetsToLNu_HT2500_inf',
        'WJetsToLNu-0J','WJetsToLNu-1J','WJetsToLNu-2J',
    ]
} 
Steps['zNLOEWK'] = {
    'isChain'    : False ,
    'do4MC'      : True  ,
    'do4Data'    : False  ,
    'import'     : 'LatinoAnalysis.NanoGardener.modules.qq2VEWKcorrectionsWeightProducer' ,
    'declare'    : 'wNLOEWK = lambda : vNLOEWKcorrectionWeightProducer("z")',
    'module'     : 'wNLOEWK()',
    'onlySample' : [
        #### DY                                                                                                                                        
        'DYJetsToLL_M-5to50-LO',
        'DYJetsToLL_M-10to50',
        'DYJetsToLL_M-50','DYJetsToLL_M-50_ext1',
        'DYJetsToLL_M-10to50ext3','DYJetsToLL_M-50-LO',
        'DYJetsToLL_M-50-LO-ext1','DYJetsToLL_M-10to50-LO',
        'DYJetsToTT_MuEle_M-50','DYJetsToLL_M-50_ext2',
        'DYJetsToLL_M-10to50-LO-ext1',
        # ... Low Mass HT                                                                                                                              
        'DYJetsToLL_M-4to50_HT-100to200',
        'DYJetsToLL_M-4to50_HT-100to200-ext1',
        'DYJetsToLL_M-4to50_HT-200to400',
        'DYJetsToLL_M-4to50_HT-200to400-ext1',
        'DYJetsToLL_M-4to50_HT-400to600',
        'DYJetsToLL_M-4to50_HT-400to600-ext1',
        'DYJetsToLL_M-4to50_HT-600toInf',
        'DYJetsToLL_M-4to50_HT-600toInf-ext1',
        # ... high Mass HT                                                                                                                             
        'DYJetsToLL_M-50_HT-70to100',
        'DYJetsToLL_M-50_HT-100to200',
        'DYJetsToLL_M-50_HT-200to400',
        'DYJetsToLL_M-50_HT-400to600',
        'DYJetsToLL_M-50_HT-600to800',
        'DYJetsToLL_M-50_HT-800to1200',
        'DYJetsToLL_M-50_HT-1200to2500',
        'DYJetsToLL_M-50_HT-2500toInf',
        ''
    ]
}


