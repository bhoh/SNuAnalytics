'''variables['mll']  = {   'name': '',
                        'range' : (90,150,1500),
                        'xaxis' : 'p_{T} 1st fatjet',
                        'fold'  : 3
                        }

'''
##Small number of variables -> faster
### Number of variables => Number of times running loops
njet='(Sum$(Jet_jetId>0 && Jet_pt>30 && fabs(Jet_eta) < 2.4))'
nbjet='(Sum$(Jet_jetId>0 && Jet_pt>20 && fabs(Jet_eta) < 2.4 && Jet_btagDeepB > 0.2217 &&  ( sqrt( pow(Jet_eta - PreselFatJet_eta[0],2) + pow(Jet_phi - PreselFatJet_phi[0],2)) >\
 0.8) ))'
ww_px_pow2=' pow(     PreselFatJet_pt[0]*cos(PreselFatJet_phi[0])+ Wlep_px, 2    )'
ww_px='(     PreselFatJet_pt[0]*cos(PreselFatJet_phi[0])+ Wlep_px )'
ww_py_pow2=' pow(     PreselFatJet_pt[0]*sin(PreselFatJet_phi[0])+ Wlep_py, 2    )'
ww_py=' (PreselFatJet_pt[0]*sin(PreselFatJet_phi[0])+ Wlep_py)'
ww_pz_pow2=' pow(     PreselFatJet_pt[0]*sinh(PreselFatJet_eta[0])+ Wlep_pz,2    )'
ww_pz=' ( PreselFatJet_pt[0]*sinh(PreselFatJet_eta[0])+ Wlep_pz    )'
ww_E_pow2 ='pow(    sqrt(pow( PreselFatJet_pt[0]*cosh(PreselFatJet_eta[0]),2) +pow( PreselFatJet_msoftdrop[0],2))  + Wlep_E ,2) '
mww = '( sqrt( '+ww_E_pow2+' - '+ww_px_pow2+' - '+ww_py_pow2+' -'+ww_pz_pow2+'    )     )'
ww_pt='( sqrt( '+ww_px_pow2+' + '+ww_py_pow2+'  )  )'
ww_phi = '(atan('+ww_py+'/'+ww_px+' ) )'
ww_eta=' ( asinh('+ww_pz+'/'+ww_pt+') )'



##For checking##

variables['Event'] = {
    'name' : '1',
    'range':(1,0,1),
    'xaxis':'1',
    'fold': 3
}



##--Electron Momentum--##
variables['electron_pt'] = { 
'name' : 'Electron_pt[0]',
'range':(50,20,120),
'xaxis':'p_{T1}(e)',
'fold': 0
}
                     

variables['electron_eta'] = {
'name' : 'Electron_eta[0]',
'range':(40,-3,3),
'xaxis':'#eta(e)',
'fold':0
}

variables['electron_phi'] = {
'name' : 'Electron_phi[0]',
'range':(40,-3,3),
'xaxis':'#phi(e)',
'fold':0
}


variables['muon_pt'] = {
'name' : 'Muon_pt[0]',
'range':(50,20,120),
'xaxis':'p_{T}(#mu)',
'fold':0
    }



variables['muon_eta'] = {
'name' : 'Muon_eta[0]',
'range':(40,-3,3),
'xaxis':'#eta(#mu)',
'fold':0
}
variables['muon_phi'] = {
'name' : 'Muon_phi[0]',
'range':(40,-3,3),
'xaxis':'#phi(#mu)[0]',
'fold':0
}



variables['Lepton_pt[0]'] = {
'name' : 'Lepton_pt[0]',
    'range': (50,20,120),
    'xaxis':'p_{T}(leading lep)',
    'fold':0
}


variables['Lepton_eta[0]'] = {
    'name' : 'Lepton_eta[0]',
    'range':(40,-3,3),
    'xaxis':'#eta(leading lep)',
    'fold':0

}
variables['Lepton_phi[0]'] = {
'name' : 'Lepton_phi[0]',
    'range':(40,-3,3),
    'xaxis':'#phi(leading lep)',
    'fold':0

}

variables['Lepton_pt[1]'] = {
'name' : 'Lepton_pt[1]',
    'range': (50,20,120),
    'xaxis':'p_{T}(leading lep)',
    'fold':0
}


variables['Lepton_eta[1]'] = {
    'name' : 'Lepton_eta[1]',
    'range':(40,-3,3),
    'xaxis':'#eta(leading lep)',
    'fold':0

}
variables['Lepton_phi[1]'] = {
'name' : 'Lepton_phi[1]',
    'range':(40,-3,3),
    'xaxis':'#phi(leading lep)',
    'fold':0

}









variables ['PV_npvs']={
    'name' : 'PV_npvs',
    'range' : (80,0,80),
    'xaxis' : 'PV_npvs',
    'fold':0
}



variables['nbjet']={
    'name' : nbjet,
    'range':(10,0,10),
    'xaxis':'nbjet',
    'fold':3

}
variables['njet']={
    'name' : njet,
    'range':(10,0,10),
    'xaxis':'njet',
    'fold':3

}

variables['MET_pt']={
    'name' : 'MET_pt',
    'range':(100,0,400),
    'xaxis':'MET_pt',
    'fold':0

}

variables['MET_phi']={
    'name' : 'MET_phi',
    'range':(40,-4,4),
    'xaxis':'MET_phi',
    'fold':0

}

variables['PuppiMET_pt']={
    'name' : 'PuppiMET_pt',
    'range':(100,0,400),
    'xaxis':'PuppiMET_pt',
    'fold':0

}

variables['PuppiMET_phi']={
    'name' : 'PuppiMET_phi',
    'range':(40,-4,4),
    'xaxis':'PuppiMET_phi',
    'fold':0

}

variables['RawMET_pt']={
    'name' : 'RawMET_pt',
    'range':(100,0,400),
    'xaxis':'RawMET_pt',
    'fold':0

}

variables['RawMET_phi']={
    'name' : 'RawMET_phi',
    'range':(40,-4,4),
    'xaxis':'RawMET_phi',
    'fold':0

}




variables ['mll']={
    'name' : 'mll',
    'range' : (30,60,120),
    'xaxis' : 'mll',
    'fold':0
}
