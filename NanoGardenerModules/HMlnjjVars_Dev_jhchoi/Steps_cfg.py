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

Steps['WlepMaker'] = {
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMaker',
    'declare': 'wlepmaker = lambda:WlepMaker(METtype="PuppiMET",year=RPLME_YEAR)',
    'module':  'wlepmaker()',

}



Steps['WlepMaker_jetsys'] = {##ak4 jet sys
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMaker',
    'declare': 'wlepmaker = lambda:WlepMaker(METtype="PuppiMET",year=RPLME_YEAR)',
    'module':  'wlepmaker()',
}
Steps['WlepMaker_jetsysup'] = {##ak4 jet sys
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMaker',
    'declare': 'wlepmaker = lambda:WlepMaker(METtype="PuppiMET",year=RPLME_YEAR,jsysvars="up")',
    'module':  'wlepmaker()',
}
Steps['WlepMaker_jetsysdown'] = {##ak4 jet sys
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMaker',
    'declare': 'wlepmaker = lambda:WlepMaker(METtype="PuppiMET",year=RPLME_YEAR,jsysvars="down")',
    'module':  'wlepmaker()',
}
Steps['WlepMaker_jetsysup_correlate'] = {##ak4 jet sys
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMaker',
    'declare': 'wlepmaker = lambda:WlepMaker(METtype="PuppiMET",year=RPLME_YEAR,jsysvars="up",jsyssources="correlate")',
    'module':  'wlepmaker()',
}
Steps['WlepMaker_jetsysdown_correlate'] = {##ak4 jet sys
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMaker',
    'declare': 'wlepmaker = lambda:WlepMaker(METtype="PuppiMET",year=RPLME_YEAR,jsysvars="down",jsyssources="correlate")',
    'module':  'wlepmaker()',
}

Steps['WlepMaker_jetsysup_uncorrelate'] = {##ak4 jet sys
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMaker',
    'declare': 'wlepmaker = lambda:WlepMaker(METtype="PuppiMET",year=RPLME_YEAR,jsysvars="up",jsyssources="uncorrelate")',
    'module':  'wlepmaker()',
}
Steps['WlepMaker_jetsysdown_uncorrelate'] = {##ak4 jet sys
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMaker',
    'declare': 'wlepmaker = lambda:WlepMaker(METtype="PuppiMET",year=RPLME_YEAR,jsysvars="down",jsyssources="uncorrelate")',
    'module':  'wlepmaker()',
}


Steps['WlepMaker_nom'] = {
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMaker',
    'declare': 'wlepmaker = lambda:WlepMaker(METtype="PuppiMET",jsysvars=["nom"],year=RPLME_YEAR)',
    'module':  'wlepmaker()',

}

Steps['WlepMaker_data'] = {
    'isChain': False,
    'do4MC': False,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMaker',
    'declare': 'wlepmaker = lambda:WlepMaker(METtype="PuppiMET",jsysvars=["nom"],year=RPLME_YEAR)',
    'module':  'wlepmaker()',

}

###--Analyzer
Steps['HMlnjjVars_Dev_jhchoi9_nom'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):
    ##Use for data/nom
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi9',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],jetsysvars=["nom"],pairalgos=["dMchi2Resolution","dM"])',
    'module':  'hmlnjjvar()',

}
Steps['HMlnjjVars_Dev_jhchoi9_sys'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi9',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",pairalgos=["dMchi2Resolution","dM"])',
    'module':  'hmlnjjvar()',

}


Steps['HMlnjjVars_Dev_jhchoi9_jetsys'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi9',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],pairalgos=["dMchi2Resolution","dM"])',
    'module':  'hmlnjjvar()',

}



Steps['HMlnjjVars_Dev_jhchoi9_jetsysup'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi9',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],jetsysvars="up",pairalgos=["dMchi2Resolution","dM"])',
    'module':  'hmlnjjvar()',

}


Steps['HMlnjjVars_Dev_jhchoi9_jetsysdown'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi9',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],jetsysvars="down",pairalgos=["dMchi2Resolution","dM"])',
    'module':  'hmlnjjvar()',

}

Steps['HMlnjjVars_Dev_jhchoi9_jetsysup_correlate'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi9',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],jetsysvars="up",pairalgos=["dMchi2Resolution","dM"],jsyssources="correlate")',
    'module':  'hmlnjjvar()',

}


Steps['HMlnjjVars_Dev_jhchoi9_jetsysdown_correlate'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi9',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],jetsysvars="down",pairalgos=["dMchi2Resolution","dM"],jsyssources="correlate")',
    'module':  'hmlnjjvar()',

}


Steps['HMlnjjVars_Dev_jhchoi9_jetsysup_uncorrelate'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi9',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],jetsysvars="up",pairalgos=["dMchi2Resolution","dM"],jsyssources="uncorrelate")',
    'module':  'hmlnjjvar()',

}


Steps['HMlnjjVars_Dev_jhchoi9_jetsysdown_uncorrelate'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi9',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],jetsysvars="down",pairalgos=["dMchi2Resolution","dM"],jsyssources="uncorrelate")',
    'module':  'hmlnjjvar()',

}


Steps['HMlnjjVars_Dev_jhchoi9_fatjetsys'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi9',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",jetsysvars=["nom"],pairalgos=["dMchi2Resolution","dM"])',
    'module':  'hmlnjjvar()',

}



##--Chain
Steps['HMFull_jhchoi9_nom']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMaker_nom','WtaggerProducer_nom','WjjtaggerProducer_nom','HMlnjjVars_Dev_jhchoi9_nom'],

}

Steps['HMFull_jhchoi9_sys']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMaker_jetsys','WtaggerProducer_fatjetsys','WjjtaggerProducer_jetsys','HMlnjjVars_Dev_jhchoi9_sys'],

}



Steps['HMFull_jhchoi9_jetsys']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMaker_jetsys','WtaggerProducer_nom','WjjtaggerProducer_jetsys','HMlnjjVars_Dev_jhchoi9_jetsys'],

}

Steps['HMFull_jhchoi9_jetsysup']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMaker_jetsysup','WtaggerProducer_nom','WjjtaggerProducer_jetsysup','HMlnjjVars_Dev_jhchoi9_jetsysup'],

}


Steps['HMFull_jhchoi9_jetsysdown']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMaker_jetsysdown','WtaggerProducer_nom','WjjtaggerProducer_jetsysdown','HMlnjjVars_Dev_jhchoi9_jetsysdown'],

}


Steps['HMFull_jhchoi9_jetsysup_correlate']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMaker_jetsysup_correlate','WtaggerProducer_nom','WjjtaggerProducer_jetsysup_correlate','HMlnjjVars_Dev_jhchoi9_jetsysup_correlate'],

}


Steps['HMFull_jhchoi9_jetsysdown_correlate']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMaker_jetsysdown_correlate','WtaggerProducer_nom','WjjtaggerProducer_jetsysdown_correlate','HMlnjjVars_Dev_jhchoi9_jetsysdown_correlate'],

}

Steps['HMFull_jhchoi9_jetsysup_uncorrelate']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMaker_jetsysup_uncorrelate','WtaggerProducer_nom','WjjtaggerProducer_jetsysup_uncorrelate','HMlnjjVars_Dev_jhchoi9_jetsysup_uncorrelate'],

}


Steps['HMFull_jhchoi9_jetsysdown_uncorrelate']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMaker_jetsysdown_uncorrelate','WtaggerProducer_nom','WjjtaggerProducer_jetsysdown_uncorrelate','HMlnjjVars_Dev_jhchoi9_jetsysdown_uncorrelate'],

}

Steps['HMFull_jhchoi9_fatjetsys']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMaker_nom','WtaggerProducer_fatjetsys','WjjtaggerProducer_nom','HMlnjjVars_Dev_jhchoi9_fatjetsys'],

}


Steps['HMFull_jhchoi9_data']={
    'isChain':True,
    'do4MC':False,
    'do4Data':True,
    'subTargets':['WlepMaker_data','WtaggerProducer_data','WjjtaggerProducer_data','HMlnjjVars_Dev_jhchoi9_nom'],

}


##--Test


Steps['WlepMaker_test'] = {
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'selection':'"Entry$ < 1000"',
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMaker',
    'declare': 'wlepmaker = lambda:WlepMaker(METtype="PuppiMET")',
    'module':  'wlepmaker()',

}

Steps['HMlnjjVars_Dev_jhchoi9test'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'selection':'"Entry$ < 1000"',
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi9',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],jetsysvars=["nom"],pairalgos=["dMchi2Resolution","dM"])',
    'module':  'hmlnjjvar()',

}

Steps['HMlnjjVars_Dev_jhchoi9_sys_test'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'selection':'"Entry$ < 1000"',
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi9',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",pairalgos=["dMchi2Resolution","dM"])',
    'module':  'hmlnjjvar()',

}

Steps['HMFull_test']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'selection':'"Entry$ < 10000"',
    'subTargets':['WlepMaker_nom','WtaggerProducer_nom','WjjtaggerProducer_nom','HMlnjjVars_Dev_jhchoi9_nom'],

}


Steps['HMFull_sys_test']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'selection':'"Entry$ < 1000"',
    'subTargets':['WlepMaker','WtaggerProducer_fatjetsys','WjjtaggerProducer_sys','HMlnjjVars_Dev_jhchoi9_sys_test'],

}


Steps['WmakerChain_data_test']={
    'isChain':True,
    'do4MC':False,
    'do4Data':True,
    'selection':'"Entry$ < 10000"',
    'subTargets':['WlepMaker_data','WtaggerProducer_data','WjjtaggerProducer_nom'],
}


Steps['WmakerChain_nom_test']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'selection':'"Entry$ < 10000"',
    'subTargets':['WlepMaker_nom','WtaggerProducer_nom','WjjtaggerProducer_nom'],
}


Steps['WmakerChain_sys_test']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'selection':'"Entry$ < 10000"',
    'subTargets':['WlepMaker','WtaggerProducer_fatjetsys','WjjtaggerProducer_sys'],
}




Steps['HMFull_jhchoi9_data_test']={
    'isChain':True,
    'do4MC':False,
    'do4Data':True,
    'selection':'"Entry$ < 10000"',
    'subTargets':['WlepMaker_data','WtaggerProducer_data','WjjtaggerProducer_data','HMlnjjVars_Dev_jhchoi9_nom'],

}



##---Run--##
Steps['HMlnjjVars_Dev_jhchoi9_nom'] = {#    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'], doSkim=False, doHardSkim=False):

    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev_jhchoi9',
    'declare': 'hmlnjjvar = lambda:HMlnjjVarsClass_Dev(year=RPLME_YEAR,METtype="PuppiMET",fjsysvars=["nom"],jetsysvars=["nom"],pairalgos=["dMchi2Resolution","dM"])',
    'module':  'hmlnjjvar()',

}


Steps['HMFull_jhchoi9_nom']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WlepMaker_nom','WtaggerProducer_nom','WjjtaggerProducer_nom','HMlnjjVars_Dev_jhchoi9_nom'],

}

