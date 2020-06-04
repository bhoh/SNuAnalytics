mc = [skey for skey in samples if (skey != 'DATA' and skey !='PseudoData')]

nuisances['stat'] = {
    'type': 'auto',
    'maxPoiss': '10',
    'includeSignal': '1',
    'typeStat':'bbb',
    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': dict((skey, {}) for skey in mc),

}

nuisances['stat'] = {
    'type': 'auto',
    'maxPoiss': '10',
    'includeSignal': '0',
    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': {}
}
'''
nuisances['dummy'] = {
    'type': 'lnN',
    'name': 'dummy',
    'samples': dict((skey, '1.001') for skey in mc),


}

'''
