Steps={}##initialize steps dictionary

Steps['WtaggerProducer2018'] =  {
    'isChain': False,
    'do4MC': True,
    'do4Data': False,
    'import': 'LatinoAnalysis.NanoGardener.modules.WtaggerProducer',
    'declare': 'wtaggermc = lambda:WtaggerProducer(isData=False,year=2018)',
    'module':  'wtaggermc()'
}
