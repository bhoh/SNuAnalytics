mc = [skey for skey in samples if (skey != 'DATA' and skey !='PseudoData')]
##

nuisances['dummy'] = {
    'name': 'dummy',
    'type': 'lnN',
    'samples': dict((skey, '1.0001') for skey in mc )
}