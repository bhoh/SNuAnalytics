'''variables['mll']  = {   'name': '',
                        'range' : (90,150,1500),
                        'xaxis' : 'p_{T} 1st fatjet',
                        'fold'  : 3
                        }

'''
##Small number of variables -> faster
### Number of variables => Number of times running loops

nbjet='(Sum$(Jet_jetId>0 && Jet_pt>20 && fabs(Jet_eta) < 2.4 && Jet_btagDeepB > 0.2217 &&  ( sqrt( pow(Jet_eta - PreselFatJet_eta[0],2) + pow(\
Jet_phi - PreselFatJet_phi[0],2)) > 0.8) ))'
ww_px_pow2=' pow(     PreselFatJet_pt[0]*cos(PreselFatJet_phi[0])+ Wlep_px, 2    )'
ww_py_pow2=' pow(     PreselFatJet_pt[0]*sin(PreselFatJet_phi[0])+ Wlep_py, 2    )'
ww_pz_pow2=' pow(     PreselFatJet_pt[0]*sinh(PreselFatJet_eta[0])+ Wlep_pz,2    )'
ww_E_pow2 ='pow(    sqrt(pow( PreselFatJet_pt[0]*cosh(PreselFatJet_eta[0]),2) +pow( PreselFatJet_msoftdrop[0],2))  + Wlep_E ,2) '
mww = '( sqrt( '+ww_E_pow2+' - '+ww_px_pow2+' - '+ww_py_pow2+' -'+ww_pz_pow2+'    )     )'


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


variables['nPreselFatJet'] = {                                                                                                                       
    'name' : 'nPreselFatJet',                                                                                                                            
    'range':(10,0,10),                                                                                                                         
    'xaxis':'nFatJet',                                                                                                                         
    'fold':3                                                                                                                                   
} 


'''
variables['FatJet_msoftdrop'] = {
'name' : 'FatJet_msoftdrop',
    'range':(100,0,300),
    'xaxis': '#M_{softdrop}(J)',
    'fold':0
}

variables['tau21'] = {
'name' : 'FatJet_tau2/FatJet_tau1',
    'range':(100,0,2),
    'xaxis':'#tau21',
    'fold':0
}
variables['nFatJet'] = {
'name' : 'nFatJet',
    'range':(10,0,10),
    'xaxis':'nFatJet',
    'fold':3
}

variables['FatJet_pt'] = {
    'name' : 'FatJet_pt',
    'range':(50,150,300),
    'xaxis':'FatJet_pt',
    'fold':0
}
variables['FatJet_eta'] = {
    'name' : 'FatJet_eta',
    'range':(40,-3,3),
    'xaxis':'FatJet_eta',
    'fold':0
}
variables['FatJet_phi'] = {
    'name' : 'FatJet_phi',
    'range':(40,-4,3),
    'xaxis':'FatJet_phi',
    'fold':0
}

variables['PreselFatJet_tau21']={
    'name' : 'PreselFatJet_tau2/PreselFatJet_tau1',
    'range':(20,0,1),
    'xaxis':'tau21',
    'fold':0
}

variables['PreselFatJet_pt'] = {
    'name' : 'PreselFatJet_pt',
    'range':(50,150,300),
    'xaxis':'PreselFatJet_pt',
    'fold':0
}
variables['PreselFatJet_eta'] = {
    'name' : 'PreselFatJet_eta',
    'range':(40,-3,3),
    'xaxis':'PreselFatJet_eta',
    'fold':0
}
variables['PreselFatJet_phi'] = {
    'name' : 'PreselFatJet_phi',
    'range':(40,-3.5,3.5),
    'xaxis':'PreselFatJet_phi',
    'fold':0
}



variables['PreselFatJet_msoftdrop'] = {
    'name' : 'PreselFatJet_msoftdrop',
    'range':(48,30,270),
    'xaxis':'PreselFatJet_phi',
    'fold':0
}



'''




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




'''


variables['Wlep_pt'] = {
'name' : 'Wlep_pt',
    'range':(100,0,400),
    'xaxis':'Wlep_pt',
    'fold':0

}

variables['Wlep_eta'] = {
'name' : 'Wlep_eta',
    'range':(40,-3,3),
    'xaxis':'Wlep_eta',
    'fold':0

}

variables['Wlep_phi'] = {
'name' : 'Wlep_phi',
    'range':(50,-3.5,3.5),
    'xaxis':'Wlep_phi',
    'fold':0

}



variables['min(Wlep_pt,Whad_pt)_over_mww']={
    'name' : 'min(Wlep_pt,PreselFatJet_pt)/'+mww+'',
    'range':(20,0,1),
    'xaxis':'min(Wlep_pt,Whad_pt)/Mww',
    'fold':0

}


variables['mww700']={
    'name':mww,
    'range':(80,0,5000),
    'xaxis':'mww',
    'fold':0
}


variables['mww4000']={
    'name':mww,
    'range':(30,2000,5000),
    'xaxis':'mww',
    'fold':0
}

variables['mww5000']={
    'name':mww,
    'range':(40,2000,6000),
    'xaxis':'mww',
    'fold':0
}


'''

variables['MET_pt'] = {
'name' : 'MET_pt',
    'range':(100,0,500),
    'xaxis':'MET_pt',
    'fold':0

}

variables['MET_phi'] = {
'name' : 'MET_phi',
    'range':(100,-4,4),
    'xaxis':'MET_phi',
    'fold':0

}

variables ['Lepton_pdgId[0]'] = {
    'name' : 'Lepton_pdgId[0]',
    'range':(30, -15,15),
    'xaxis':'pdgId(Leading lep)',
    'fold':3
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
