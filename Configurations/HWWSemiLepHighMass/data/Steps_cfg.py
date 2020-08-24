Steps={}##initializWe steps dictionary

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



Steps['WtaggerProducer_sys'] =  {##    def __init__(self,isData, year,sysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown']): ##jes,jer,jms,jmr

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

Steps['WjjtaggerProducer_sys'] =  {##    def __init__(self,year,sysvars=None):
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WjjtaggerProducer',
    'declare': 'wjjtagger = lambda:WjjtaggerProducer(year=RPLME_YEAR, sysvars="all", pairalgos=["dM","dMchi2Resolution"])',
    'module':  'wjjtagger()',
}


Steps['WhadronChain']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WjjtaggerProducer','WjjtaggerProducer_nom'],
}

Steps['WhadronChainFullJetSys']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'subTargets':['WtaggerProducer','WjjtaggerProducer'],
}


Steps['WhadronChain_data']={
    'isChain':True,
    'do4MC':False,
    'do4Data':True,
    'subTargets':['WtaggerProducer_data','WjjtaggerProducer_nom'],
}


Steps['WhadronChain_data_test']={
    'isChain':True,
    'do4MC':False,
    'do4Data':True,
    'selection':'"Entry$ < 10000"',
    'subTargets':['WtaggerProducer_data','WjjtaggerProducer_nom'],
}

Steps['WtaggerProducer_data_test'] =  {
    'isChain': False,
    'do4MC': False,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WtaggerProducer',
    'declare': 'wtaggerdata = lambda:WtaggerProducer(isData=True,year=RPLME_YEAR)',
    'module':  'wtaggerdata()',
}

Steps['WlepMaker'] = {
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMaker',
    'declare': 'wlepmaker = lambda:WlepMaker(METtype="PuppiMET")',
    'module':  'wlepmaker()',

}


Steps['WlepMaker_test'] = {
    'isChain': False,
    'do4MC': True,
    'do4Data': True,
    'selection':'"Entry$ < 1000"',
    'import': 'LatinoAnalysis.NanoGardener.modules.WlepMaker',
    'declare': 'wlepmaker = lambda:WlepMaker(METtype="PuppiMET")',
    'module':  'wlepmaker()',

}




Steps['WmakerChain_data_test']={
    'isChain':True,
    'do4MC':False,
    'do4Data':True,
    'selection':'"Entry$ < 10000"',
    'subTargets':['WlepMaker','WtaggerProducer_data','WjjtaggerProducer_nom'],
}


Steps['WmakerChain_nom_test']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'selection':'"Entry$ < 10000"',
    'subTargets':['WlepMaker','WtaggerProducer_nom','WjjtaggerProducer_nom'],
}


Steps['WmakerChain_sys_test']={
    'isChain':True,
    'do4MC':True,
    'do4Data':False,
    'selection':'"Entry$ < 10000"',
    'subTargets':['WlepMaker','WtaggerProducer_sys','WjjtaggerProducer_sys'],
}
