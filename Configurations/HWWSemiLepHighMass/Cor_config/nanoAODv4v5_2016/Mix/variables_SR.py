#-----Variable Deinition-----#                                                                                                                               #------End of Variable Definition-----#


variables['CleanFatJetPassMBoostedSR_HlnFat_mass']={
    'name' : 'CleanFatJetPassMBoostedSR_HlnFat_mass[0]',
    #'range':(80,0,4000),
    'range':([0,200,210,230,250,300,350,400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000,5000,6000],),
    'xaxis':'m_{lnJ} [GeV]',
    'divideByBinWidth':1,
    'fold':0
}



variables['LnJJ_mass']={
    'name': 'Hlnjj_mass',
    'range':([0,200,210,230,250,300,350,400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000,5000,6000],),
    'xaxis':'m_{lnjj} [GeV]',
    'divideByBinWidth':1,
    'fold':0
}


variables['events']={
    'name': '1',
    'range':(1,0,2),
    'xaxis':'event',
    'fold':0
}


