'''variables['mll']  = {   'name': '',
                        'range' : (90,150,1500),
                        'xaxis' : 'p_{T} 1st fatjet',
                        'fold'  : 3
                        }

'''
##Small number of variables -> faster
### Number of variables => Number of times running loops

eleWP='mva_90p_Iso2016'
muWP='cut_Tight80x'

LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
bAlgo='DeepB'
bWP='0.2217'



isbjet='(Jet_jetId>0 && Jet_pt>20 && fabs(Jet_eta) < 2.4 && Jet_btag'+bAlgo+' > '+bWP+' &&  ( Iteration$ != idx_j1  ) && ( Iteration$ != idx\
_j2 ))'
nbjet='(Sum$'+isbjet+')'
btagSF_each='( '+isbjet+'*Alt$(Jet_btagSF_shape, 1) + !'+isbjet+'*1 )'
logbtagSF='(Sum$(  TMath::Log('+btagSF_each+')))'
btagSF='(TMath::Exp( '+logbtagSF+' ))'




ww_px_pow2=' pow(     Whad_pt[0]*cos(Whad_phi[0])+ Wlep_px, 2    )'
ww_px='(     Whad_pt[0]*cos(Whad_phi[0])+ Wlep_px )'
ww_py_pow2=' pow(     Whad_pt[0]*sin(Whad_phi[0])+ Wlep_py, 2    )'
ww_py=' (Whad_pt[0]*sin(Whad_phi[0])+ Wlep_py)'
ww_pz_pow2=' pow(     Whad_pt[0]*sinh(Whad_eta[0])+ Wlep_pz,2    )'
ww_pz=' ( Whad_pt[0]*sinh(Whad_eta[0])+ Wlep_pz    )'
ww_E_pow2 ='pow(    sqrt(pow( Whad_pt[0]*cosh(Whad_eta[0]),2) +pow( Whad_msoftdrop[0],2))  + Wlep_E ,2) '
mww = '( sqrt( '+ww_E_pow2+' - '+ww_px_pow2+' - '+ww_py_pow2+' -'+ww_pz_pow2+'    )     )'
ww_pt='( sqrt( '+ww_px_pow2+' + '+ww_py_pow2+'  )  )'
ww_phi = '(atan('+ww_py+'/'+ww_px+' ) )'
ww_eta=' ( asinh('+ww_pz+'/'+ww_pt+') )'


notBoostedSelection='(nPreselFatJet==0)'

wlep_mt='(sqrt(pow(Wlep_E,2) - pow(Wlep_pz,2)  ))'
lvqq_mt='(sqrt('+ww_E_pow2+'-'+ww_pz_pow2+'))'





##---
variables['Event'] = {
    'name' : '1',
    'range':(1,0,1),
    'xaxis':'1',
    'fold': 3
}


'''
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


'''

variables['Whad_pt'] = {
    'name' : 'Whad_pt',
    'range':(50,150,600),
    'xaxis':'Whad_pt',
    'fold':0
}
variables['Whad_eta'] = {
    'name' : 'Whad_eta',
    'range':(40,-3,3),
    'xaxis':'Whad_eta',
    'fold':0
}
variables['Whad_phi'] = {
    'name' : 'Whad_phi',
    'range':(40,-3.5,3.5),
    'xaxis':'Whad_phi',
    'fold':0
}

variables['Whad_mass'] = {
    'name' : 'Whad_mass',
    'range':(100,0.,300.),
    'xaxis':'Whad_mass',
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
    'range':(100,0,800),
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
    'name' : 'min(Wlep_pt,Whad_pt)/'+mww+'',
    'range':(20,0,1),
    'xaxis':'min(Wlep_pt,Whad_pt)/Mww',
    'fold':0

}


variables['mww']={
    'name':mww,
    'range':(80,0,5000),
    'xaxis':'mww',
    'fold':0
}

variables['ww_pt']={
    'name':ww_pt,
    'range':(50,0,400),
    'xaxis':'ww_pt',
    'fold':0
}

variables['ww_eta']={
    'name':ww_eta,
    'range':(50,-3.5,3.5),
    'xaxis':'ww_eta',
    'fold':0
}


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


'''
variables ['Lepton_pdgId[0]'] = {
    'name' : 'Lepton_pdgId[0]',
    'range':(30, -15,15),
    'xaxis':'pdgId(Leading lep)',
    'fold':3
}

'''
variables ['PV_npvs']={
    'name' : 'PV_npvs',
    'range' : (80,0,80),
    'xaxis' : 'PV_npvs',
    'fold':3
}



variables['nbjet']={
    'name' : nbjet,
    'range':(10,0,10),
    'xaxis':'nbjet',
    'fold':3

}


variables['btagSF']={
    'name' : btagSF,
    'range':(100,-2,2),
    'xaxis':'btagSF',
    'fold':0
}


variables['btagSF_each']={
    'name' : btagSF_each,
    'range':(100,-2,2),
    'xaxis':'btagSF_each',
    'fold':0
}



variables['lvqq_mt']={
    'name' : lvqq_mt,
    'range':(100,0,500),
    'xaxis':'lvqq_mt',
    'fold':0
}

