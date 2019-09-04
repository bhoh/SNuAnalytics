
##Small number of variables -> faster
### Number of variables => Number of times running loops

#-----Variable Deinition-----#                                                                                                                                                                                                                               \
                                                                                                                                                                                                                                                              




eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'

METtype='Puppi'

if METtype=='' or METtype=='PF':
    MET_pt='MET_pt'
    MET_phi='MET_phi'
    Wlep_px='Wlep_px_PF'
    Wlep_py='Wlep_py_PF'
    Wlep_pz='Wlep_pz_PF'
    Wlep_E='Wlep_E_PF'
    Wlep_pt='Wlep_pt_PF'
    Wlep_eta='Wlep_eta_PF'
    Wlep_phi='Wlep_phi_PF'
    Wlep_mass='Wlep_mass_PF'


else:
    MET_pt=METtype+'MET_pt'
    MET_phi=METtype+'MET_phi'
    Wlep_px='Wlep_px_'+METtype
    Wlep_py='Wlep_py_'+METtype
    Wlep_pz='Wlep_pz_'+METtype
    Wlep_E='Wlep_E_'+METtype
    Wlep_pt='Wlep_pt_'+METtype
    Wlep_eta='Wlep_eta_'+METtype
    Wlep_phi='Wlep_phi_'+METtype
    Wlep_mass='Wlep_mass_'+METtype


LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'

bAlgo='DeepB'
bWP='0.2219'

isbjet='(CleanJet_jetIdx[CleanJetNotFat_jetIdx]>0 && CleanJet_pt[CleanJetNotFat_jetIdx]>20 && fabs(CleanJet_eta[CleanJetNotFat_jetIdx]) < 2.4 && Jet_btag'+bAlgo+'[CleanJet_jetIdx[CleanJetNotFat_jetIdx]] > '+bWP+'  )'
nbjet='(Sum$'+isbjet+')'
btagSF_each='( '+isbjet+'*Alt$(Jet_btagSF_shape, 1) + !'+isbjet+'*1 )'
logbtagSF='(Sum$(  TMath::Log('+btagSF_each+')))'
btagSF='(TMath::Exp( '+logbtagSF+' ))'


ww_px_pow2=' pow(     Whad_pt*cos(Whad_phi)+'+Wlep_px+', 2    )'
ww_px='(     Whad_pt*cos(Whad_phi)+'+Wlep_px+')'
ww_py_pow2=' pow(     Whad_pt*cos(Whad_phi)+'+Wlep_py+', 2    )'
ww_py='(     Whad_pt*cos(Whad_phi)+'+Wlep_py+')'
ww_pz_pow2=' pow(     Whad_pt*cos(Whad_phi)+'+Wlep_pz+', 2    )'
ww_pz='(     Whad_pt*cos(Whad_phi)+'+Wlep_pz+')'
ww_E_pow2=' pow(     Whad_pt*cos(Whad_phi)+'+Wlep_E+', 2    )'
ww_E='(     Whad_pt*cos(Whad_phi)+'+Wlep_E+')'

mww = '( sqrt( '+ww_E_pow2+' - '+ww_px_pow2+' - '+ww_py_pow2+' -'+ww_pz_pow2+'    )     )'
ww_pt='( sqrt( '+ww_px_pow2+' + '+ww_py_pow2+'  )  )'
ww_phi = '(atan('+ww_py+'/'+ww_px+' ) )'
ww_eta=' ( asinh('+ww_pz+'/'+ww_pt+') )'

wlep_mt='(sqrt(pow('+Wlep_E+',2) - pow('+Wlep_pz+',2)  ))'
lvqq_mt='(sqrt('+ww_E_pow2+'-'+ww_pz_pow2+'))'

#------End of Variable Definition-----#     






##---
variables['Event'] = {
    'name' : '1',
    'range':(1,0,1),
    'xaxis':'1',
    'fold': 3
}



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









variables['Wlep_pt'] = {
'name' : Wlep_pt,
    'range':(100,0,800),
    'xaxis':'Wlep_pt',
    'fold':0

}

variables['Wlep_eta'] = {
'name' : Wlep_eta,
    'range':(40,-3,3),
    'xaxis':'Wlep_eta',
    'fold':0

}

variables['Wlep_phi'] = {
'name' : Wlep_phi,
    'range':(50,-3.5,3.5),
    'xaxis':'Wlep_phi',
    'fold':0

}



variables['min(Wlep_pt,Whad_pt)_over_mww']={
    'name' : 'min('+Wlep_pt+',Whad_pt)/'+mww+'',
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
'name' : MET_pt,
    'range':(100,0,500),
    'xaxis':'MET_pt',
    'fold':0

}

variables['MET_phi'] = {
'name' : MET_phi,
    'range':(100,-4,4),
    'xaxis':'MET_phi',
    'fold':0

}


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




variables['lvqq_mt']={
    'name' : lvqq_mt,
    'range':(100,0,500),
    'xaxis':'lvqq_mt',
    'fold':0
}

variables['wlep_mt']={
    'name' : wlep_mt,
    'range':(100,0,200),
    'xaxis':'wlep_mt',
    'fold':0
}

