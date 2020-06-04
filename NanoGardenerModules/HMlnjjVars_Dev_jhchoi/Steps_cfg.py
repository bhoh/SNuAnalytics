import os
import copy
Steps={}##initializWe steps dictionary



###---Wtagger(FatJet) Module def---##
Steps['WtaggerProducer'] =  {
    'isChain': False,
    'do4MC': True,
    'do4Data': False,
    'import': 'LatinoAnalysis.NanoGardener.modules.WtaggerProducer',
    'declare': 'wtaggermc = lambda:WtaggerProducer(isData=False,year=RPLME_YEAR)',
    'module':  'wtaggermc()',
}

Steps['WtaggerProducer_nom'] =  {##    def __init__(self,isData, year,sysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown']): ##jes,jer,jms,jmr

    'isChain': False,
    'do4MC': True,
    'do4Data': False,
    'import': 'LatinoAnalysis.NanoGardener.modules.WtaggerProducer',
    'declare': 'wtaggermc = lambda:WtaggerProducer(isData=False,year=RPLME_YEAR,sysvars=["nom"])',
    'module':  'wtaggermc()',
}

Steps['WtaggerProducer_fatjetsys'] =  {##    def __init__(self,isData, year,sysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown']): ##jes,jer,jms,jmr

    'isChain': False,
    'do4MC': True,
    'do4Data': False,
    'import': 'LatinoAnalysis.NanoGardener.modules.WtaggerProducer',
    'declare': 'wtaggermc = lambda:WtaggerProducer(isData=False,year=RPLME_YEAR)',
    'module':  'wtaggermc()',
}


Steps['WtaggerProducer_data'] =  {
    'isChain': False,
    'do4MC': False,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WtaggerProducer',
    'declare': 'wtaggerdata = lambda:WtaggerProducer(isData=True,year=RPLME_YEAR)',
    'module':  'wtaggerdata()',
}

###----W->jj tagger (ak4)---###
Steps['WjjtaggerProducer'] =  {##    def __init__(self,year,sysvars=None):
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WjjtaggerProducer',
    'declare': 'wjjtagger = lambda:WjjtaggerProducer(year=RPLME_YEAR, sysvars="all")',
    'module':  'wjjtagger()',
}


Steps['WjjtaggerProducer_nom'] =  {##    def __init__(self,year,sysvars=None):
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WjjtaggerProducer',
    'declare': 'wjjtagger = lambda:WjjtaggerProducer(year=RPLME_YEAR, sysvars=["nom"], pairalgos=["dM","dMchi2Resolution"])',
    'module':  'wjjtagger()',
}


Steps['WjjtaggerProducer_data'] =  {##    def __init__(self,year,sysvars=None):
    'isChain': False,
    'do4MC': False,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WjjtaggerProducer',
    'declare': 'wjjtagger = lambda:WjjtaggerProducer(year=RPLME_YEAR, sysvars=["nom"], pairalgos=["dM","dMchi2Resolution"])',
    'module':  'wjjtagger()',
}


Steps['WjjtaggerProducer_jetsysup'] =  {##    def __init__(self,year,sysvars=None):
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WjjtaggerProducer',
    'declare': 'wjjtagger = lambda:WjjtaggerProducer(year=RPLME_YEAR, sysvars="up", pairalgos=["dM","dMchi2Resolution"])',
    'module':  'wjjtagger()',
}
#jsyssources
Steps['WjjtaggerProducer_jetsysup_correlate'] =  {##    def __init__(self,year,sysvars=None):
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WjjtaggerProducer',
    'declare': 'wjjtagger = lambda:WjjtaggerProducer(year=RPLME_YEAR, sysvars="up", pairalgos=["dM","dMchi2Resolution"],jsyssources="correlate")',
    'module':  'wjjtagger()',
}


Steps['WjjtaggerProducer_jetsysdown_correlate'] =  {##    def __init__(self,year,sysvars=None):
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WjjtaggerProducer',
    'declare': 'wjjtagger = lambda:WjjtaggerProducer(year=RPLME_YEAR, sysvars="down", pairalgos=["dM","dMchi2Resolution"],jsyssources="correlate")',
    'module':  'wjjtagger()',
}

Steps['WjjtaggerProducer_jetsysup_uncorrelate'] =  {##    def __init__(self,year,sysvars=None):
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WjjtaggerProducer',
    'declare': 'wjjtagger = lambda:WjjtaggerProducer(year=RPLME_YEAR, sysvars="up", pairalgos=["dM","dMchi2Resolution"],jsyssources="uncorrelate")',
    'module':  'wjjtagger()',
}


Steps['WjjtaggerProducer_jetsysdown_uncorrelate'] =  {##    def __init__(self,year,sysvars=None):
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WjjtaggerProducer',
    'declare': 'wjjtagger = lambda:WjjtaggerProducer(year=RPLME_YEAR, sysvars="down", pairalgos=["dM","dMchi2Resolution"],jsyssources="uncorrelate")',
    'module':  'wjjtagger()',
}



##---Wlep tagger--##

Steps['WlepMakerKR'] = {
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMakerKR',
    'declare': 'wlepmaker = lambda:WlepMakerKR(METtype="PuppiMET",year=RPLME_YEAR)',
    'module':  'wlepmaker()',

}



Steps['WlepMakerKR_jetsys'] = {##ak4 jet sys
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMakerKR',
    'declare': 'wlepmaker = lambda:WlepMakerKR(METtype="PuppiMET",year=RPLME_YEAR)',
    'module':  'wlepmaker()',
}
Steps['WlepMakerKR_jetsysup'] = {##ak4 jet sys
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMakerKR',
    'declare': 'wlepmaker = lambda:WlepMakerKR(METtype="PuppiMET",year=RPLME_YEAR,jsysvars="up")',
    'module':  'wlepmaker()',
}
Steps['WlepMakerKR_jetsysdown'] = {##ak4 jet sys
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMakerKR',
    'declare': 'wlepmaker = lambda:WlepMakerKR(METtype="PuppiMET",year=RPLME_YEAR,jsysvars="down")',
    'module':  'wlepmaker()',
}
Steps['WlepMakerKR_jetsysup_correlate'] = {##ak4 jet sys
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMakerKR',
    'declare': 'wlepmaker = lambda:WlepMakerKR(METtype="PuppiMET",year=RPLME_YEAR,jsysvars="up",jsyssources="correlate")',
    'module':  'wlepmaker()',
}
Steps['WlepMakerKR_jetsysdown_correlate'] = {##ak4 jet sys
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMakerKR',
    'declare': 'wlepmaker = lambda:WlepMakerKR(METtype="PuppiMET",year=RPLME_YEAR,jsysvars="down",jsyssources="correlate")',
    'module':  'wlepmaker()',
}

Steps['WlepMakerKR_jetsysup_uncorrelate'] = {##ak4 jet sys
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMakerKR',
    'declare': 'wlepmaker = lambda:WlepMakerKR(METtype="PuppiMET",year=RPLME_YEAR,jsysvars="up",jsyssources="uncorrelate")',
    'module':  'wlepmaker()',
}
Steps['WlepMakerKR_jetsysdown_uncorrelate'] = {##ak4 jet sys
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMakerKR',
    'declare': 'wlepmaker = lambda:WlepMakerKR(METtype="PuppiMET",year=RPLME_YEAR,jsysvars="down",jsyssources="uncorrelate")',
    'module':  'wlepmaker()',
}


Steps['WlepMakerKR_nom'] = {
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMakerKR',
    'declare': 'wlepmaker = lambda:WlepMakerKR(METtype="PuppiMET",jsysvars=["nom"],year=RPLME_YEAR)',
    'module':  'wlepmaker()',

}

Steps['WlepMakerKR_data'] = {
    'isChain': False,
    'do4MC': False,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMakerKR',
    'declare': 'wlepmaker = lambda:WlepMakerKR(METtype="PuppiMET",jsysvars=["nom"],year=RPLME_YEAR)',
    'module':  'wlepmaker()',

}

###--Analyzer
Steps['HMlnjjVars_Dev_jhchoi10_nom'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):
    ##Use for data/nom
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi10',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],jetsysvars=["nom"],pairalgos=["dMchi2Resolution","dM"])',
    'module':  'hmlnjjvar()',

}

Steps['HMlnjjVars_Dev_jhchoi11_nom'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):
    ##Use for data/nom
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi10',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],jetsysvars=["nom"],pairalgos=["dMchi2Resolution","dM"])',
    'module':  'hmlnjjvar()',

}


Steps['HMlnjjVars_Dev_jhchoi10_test'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):
    ##Use for data/nom
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi10_test',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],jetsysvars=["nom"],pairalgos=["dMchi2Resolution","dM"])',
    'module':  'hmlnjjvar()',

}
Steps['HMlnjjVars_Dev_jhchoi10_sys'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi10',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",pairalgos=["dMchi2Resolution","dM"])',
    'module':  'hmlnjjvar()',

}


Steps['HMlnjjVars_Dev_jhchoi10_jetsys'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi10',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],pairalgos=["dMchi2Resolution","dM"])',
    'module':  'hmlnjjvar()',

}



Steps['HMlnjjVars_Dev_jhchoi10_jetsysup'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi10',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],jetsysvars="up",pairalgos=["dMchi2Resolution","dM"])',
    'module':  'hmlnjjvar()',

}


Steps['HMlnjjVars_Dev_jhchoi10_jetsysdown'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi10',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],jetsysvars="down",pairalgos=["dMchi2Resolution","dM"])',
    'module':  'hmlnjjvar()',

}

Steps['HMlnjjVars_Dev_jhchoi10_jetsysup_correlate'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi10',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],jetsysvars="up",pairalgos=["dMchi2Resolution","dM"],jsyssources="correlate")',
    'module':  'hmlnjjvar()',

}


Steps['HMlnjjVars_Dev_jhchoi10_jetsysdown_correlate'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi10',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],jetsysvars="down",pairalgos=["dMchi2Resolution","dM"],jsyssources="correlate")',
    'module':  'hmlnjjvar()',

}


Steps['HMlnjjVars_Dev_jhchoi10_jetsysup_uncorrelate'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi10',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],jetsysvars="up",pairalgos=["dMchi2Resolution","dM"],jsyssources="uncorrelate")',
    'module':  'hmlnjjvar()',

}


Steps['HMlnjjVars_Dev_jhchoi10_jetsysdown_uncorrelate'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi10',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],jetsysvars="down",pairalgos=["dMchi2Resolution","dM"],jsyssources="uncorrelate")',
    'module':  'hmlnjjvar()',

}


Steps['HMlnjjVars_Dev_jhchoi10_fatjetsys'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi10',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",jetsysvars=["nom"],pairalgos=["dMchi2Resolution","dM"])',
    'module':  'hmlnjjvar()',

}



##--Chain
Steps['HMFull_jhchoi10_nom']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,

    'subTargets':['WlepMakerKR_nom','WtaggerProducer_nom','WjjtaggerProducer_nom','HMlnjjVars_Dev_jhchoi10_nom'],

}

Steps['HMFull_jhchoi11_nom']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMakerKR_nom','WtaggerProducer_nom','WjjtaggerProducer_nom','HMlnjjVars_Dev_jhchoi11_nom'],


}

Steps['HMFull_jhchoi10_sys']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMakerKR_jetsys','WtaggerProducer_fatjetsys','WjjtaggerProducer_jetsys','HMlnjjVars_Dev_jhchoi10_sys'],

}



Steps['HMFull_jhchoi10_jetsys']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMakerKR_jetsys','WtaggerProducer_nom','WjjtaggerProducer_jetsys','HMlnjjVars_Dev_jhchoi10_jetsys'],

}

Steps['HMFull_jhchoi10_jetsysup']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMakerKR_jetsysup','WtaggerProducer_nom','WjjtaggerProducer_jetsysup','HMlnjjVars_Dev_jhchoi10_jetsysup'],

}


Steps['HMFull_jhchoi10_jetsysdown']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMakerKR_jetsysdown','WtaggerProducer_nom','WjjtaggerProducer_jetsysdown','HMlnjjVars_Dev_jhchoi10_jetsysdown'],

}


Steps['HMFull_jhchoi10_jetsysup_correlate']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMakerKR_jetsysup_correlate','WtaggerProducer_nom','WjjtaggerProducer_jetsysup_correlate','HMlnjjVars_Dev_jhchoi10_jetsysup_correlate'],

}


Steps['HMFull_jhchoi10_jetsysdown_correlate']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMakerKR_jetsysdown_correlate','WtaggerProducer_nom','WjjtaggerProducer_jetsysdown_correlate','HMlnjjVars_Dev_jhchoi10_jetsysdown_correlate'],

}

Steps['HMFull_jhchoi10_jetsysup_uncorrelate']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMakerKR_jetsysup_uncorrelate','WtaggerProducer_nom','WjjtaggerProducer_jetsysup_uncorrelate','HMlnjjVars_Dev_jhchoi10_jetsysup_uncorrelate'],

}


Steps['HMFull_jhchoi10_jetsysdown_uncorrelate']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMakerKR_jetsysdown_uncorrelate','WtaggerProducer_nom','WjjtaggerProducer_jetsysdown_uncorrelate','HMlnjjVars_Dev_jhchoi10_jetsysdown_uncorrelate'],

}

Steps['HMFull_jhchoi10_fatjetsys']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMakerKR_nom','WtaggerProducer_fatjetsys','WjjtaggerProducer_nom','HMlnjjVars_Dev_jhchoi10_fatjetsys'],

}


Steps['HMFull_jhchoi10_data']={
    'isChain':True,
    'do4MC':False,
    'do4Data':True,
    'subTargets':['WlepMakerKR_data','WtaggerProducer_data','WjjtaggerProducer_data','HMlnjjVars_Dev_jhchoi10_nom'],

}

Steps['HMFull_jhchoi10_data_test']={
    'isChain':True,
    'do4MC':True,
    'do4Data':True,
    'subTargets':['WlepMakerKR_data','WtaggerProducer_data','WjjtaggerProducer_data','HMlnjjVars_Dev_jhchoi10_test'],

}


Steps['HMFull_jhchoi10_nom_test']={
    'isChain':True,
    'do4MC':True,
    'do4Data':True,
    'subTargets':['WlepMakerKR_nom','WtaggerProducer_nom','WjjtaggerProducer_nom','HMlnjjVars_Dev_jhchoi10_test'],

}


###--ElepT/MupT/MET
SysSteps = {
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
                  'declare'    : 'MupTdo = lambda : LeppTScalerTreeMaker(kind="Dn", lepFlavor="mu", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET\
"])',
                  'module'     : 'MupTdo()',
                },

  'do_MupTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'MupTup = lambda : LeppTScalerTreeMaker(kind="Up", lepFlavor="mu", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET\
"])',
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


}



Steps.update(SysSteps)
##--Define ElepT/MupT/MET
AnaNom="HMFull_jhchoi10_nom"

for SYS in ['ElepTup','ElepTdo','MupTup','MupTdo','METup','METdo']:
    Steps[AnaNom+"_"+SYS]=copy.deepcopy(Steps[SYS])
    Steps[AnaNom+"_"+SYS]['subTargets'].append(AnaNom)



##--Test


Steps['WlepMakerKR_test'] = {
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'selection':'"Entry$ < 1000"',
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMakerKR',
    'declare': 'wlepmaker = lambda:WlepMakerKR(METtype="PuppiMET")',
    'module':  'wlepmaker()',

}

Steps['HMlnjjVars_Dev_jhchoi10test'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'selection':'"Entry$ < 1000"',
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi10',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],jetsysvars=["nom"],pairalgos=["dMchi2Resolution","dM"])',
    'module':  'hmlnjjvar()',

}

Steps['HMlnjjVars_Dev_jhchoi10_sys_test'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'selection':'"Entry$ < 1000"',
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi10',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",pairalgos=["dMchi2Resolution","dM"])',
    'module':  'hmlnjjvar()',

}

Steps['HMFull_test']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'selection':'"Entry$ < 10000"',
    'subTargets':['WlepMakerKR_nom','WtaggerProducer_nom','WjjtaggerProducer_nom','HMlnjjVars_Dev_jhchoi10_nom'],

}


Steps['HMFull_sys_test']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'selection':'"Entry$ < 1000"',
    'subTargets':['WlepMakerKR','WtaggerProducer_fatjetsys','WjjtaggerProducer_sys','HMlnjjVars_Dev_jhchoi10_sys_test'],

}


Steps['WmakerChain_data_test']={
    'isChain':True,
    'do4MC':False,
    'do4Data':True,
    'selection':'"Entry$ < 10000"',
    'subTargets':['WlepMakerKR_data','WtaggerProducer_data','WjjtaggerProducer_nom'],
}


Steps['WmakerChain_nom_test']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'selection':'"Entry$ < 10000"',
    'subTargets':['WlepMakerKR_nom','WtaggerProducer_nom','WjjtaggerProducer_nom'],
}


Steps['WmakerChain_sys_test']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'selection':'"Entry$ < 10000"',
    'subTargets':['WlepMakerKR','WtaggerProducer_fatjetsys','WjjtaggerProducer_sys'],
}




Steps['HMFull_jhchoi10_data_test']={
    'isChain':True,
    'do4MC':False,
    'do4Data':True,
    'selection':'"Entry$ < 10000"',
    'subTargets':['WlepMakerKR_data','WtaggerProducer_data','WjjtaggerProducer_data','HMlnjjVars_Dev_jhchoi10_nom'],

}

###--BWreweighter
signals=[
"GluGluHToWWToLNuQQ_M1000",
"GluGluHToWWToLNuQQ_M115",
"GluGluHToWWToLNuQQ_M120",
"GluGluHToWWToLNuQQ_M124",
"GluGluHToWWToLNuQQ_M125",
"GluGluHToWWToLNuQQ_M126",
"GluGluHToWWToLNuQQ_M130",
"GluGluHToWWToLNuQQ_M135",
"GluGluHToWWToLNuQQ_M140",
"GluGluHToWWToLNuQQ_M145",
"GluGluHToWWToLNuQQ_M150",
"GluGluHToWWToLNuQQ_M1500",
"GluGluHToWWToLNuQQ_M155",
"GluGluHToWWToLNuQQ_M160",
"GluGluHToWWToLNuQQ_M165",
"GluGluHToWWToLNuQQ_M170",
"GluGluHToWWToLNuQQ_M175",
"GluGluHToWWToLNuQQ_M180",
"GluGluHToWWToLNuQQ_M190",
"GluGluHToWWToLNuQQ_M200",
"GluGluHToWWToLNuQQ_M2000",
"GluGluHToWWToLNuQQ_M210",
"GluGluHToWWToLNuQQ_M230",
"GluGluHToWWToLNuQQ_M250",
"GluGluHToWWToLNuQQ_M2500",
"GluGluHToWWToLNuQQ_M270",
"GluGluHToWWToLNuQQ_M300",
"GluGluHToWWToLNuQQ_M3000",
"GluGluHToWWToLNuQQ_M350",
"GluGluHToWWToLNuQQ_M400",
"GluGluHToWWToLNuQQ_M4000",
"GluGluHToWWToLNuQQ_M450",
"GluGluHToWWToLNuQQ_M500",
"GluGluHToWWToLNuQQ_M5000",
"GluGluHToWWToLNuQQ_M550",
"GluGluHToWWToLNuQQ_M600",
"GluGluHToWWToLNuQQ_M650",
"GluGluHToWWToLNuQQ_M700",
"GluGluHToWWToLNuQQ_M750",
"GluGluHToWWToLNuQQ_M800",
"GluGluHToWWToLNuQQ_M900",
"VBFHToWWToLNuQQ_M1000",
"VBFHToWWToLNuQQ_M115",
"VBFHToWWToLNuQQ_M120",
"VBFHToWWToLNuQQ_M124",
"VBFHToWWToLNuQQ_M125",
"VBFHToWWToLNuQQ_M126",
"VBFHToWWToLNuQQ_M130",
"VBFHToWWToLNuQQ_M135",
"VBFHToWWToLNuQQ_M140",
"VBFHToWWToLNuQQ_M145",
"VBFHToWWToLNuQQ_M150",
"VBFHToWWToLNuQQ_M1500",
"VBFHToWWToLNuQQ_M155",
"VBFHToWWToLNuQQ_M160",
"VBFHToWWToLNuQQ_M165",
"VBFHToWWToLNuQQ_M170",
"VBFHToWWToLNuQQ_M175",
"VBFHToWWToLNuQQ_M180",
"VBFHToWWToLNuQQ_M190",
"VBFHToWWToLNuQQ_M200",
"VBFHToWWToLNuQQ_M2000",
"VBFHToWWToLNuQQ_M210",
"VBFHToWWToLNuQQ_M230",
"VBFHToWWToLNuQQ_M250",
"VBFHToWWToLNuQQ_M2500",
"VBFHToWWToLNuQQ_M270",
"VBFHToWWToLNuQQ_M300",
"VBFHToWWToLNuQQ_M3000",
"VBFHToWWToLNuQQ_M350",
"VBFHToWWToLNuQQ_M400",
"VBFHToWWToLNuQQ_M4000",
"VBFHToWWToLNuQQ_M450",
"VBFHToWWToLNuQQ_M500",
"VBFHToWWToLNuQQ_M5000",
"VBFHToWWToLNuQQ_M550",
"VBFHToWWToLNuQQ_M600",
"VBFHToWWToLNuQQ_M650",
"VBFHToWWToLNuQQ_M700",
"VBFHToWWToLNuQQ_M750",
"VBFHToWWToLNuQQ_M800",
"VBFHToWWToLNuQQ_M900",
]

Steps['BWReweight'] ={
                 'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.BWEwkSingletReweighter' ,
                  'declare'    : 'BWEwkSingRew = lambda : BWEwkSingletReweighter(year=RPLME_YEAR)',
                  'module'     : 'BWEwkSingRew()',
    'onlySample':signals,
}


Steps['HMLHEAna']={
    'isChain'    : False ,
    'do4MC'      : True ,
    'do4Data'    : False  ,
    'import'     : 'LatinoAnalysis.NanoGardener.modules.HighMassSemilepLHEAnalyzer',
    'declare'    : 'HMLHE = lambda : HighMassSemilepLHEAnalyzer()',
    'module'     : 'HMLHE()',
    #'onlySample':signals,

#HighMassSemilepLHEAnalyzer.py
}
