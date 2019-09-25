#import my.Wlep_sel
#import my.final_fatjetsel



supercut = 'nLepton>0'


#-----Variable Deinition-----#




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


ww_px_pow2=' pow(     CleanFatJet_pt[0]*cos(CleanFatJet_phi[0])+'+Wlep_px+', 2    )'
ww_px='(     CleanFatJet_pt[0]*cos(CleanFatJet_phi[0])+'+Wlep_px+')'
ww_py_pow2=' pow(     CleanFatJet_pt[0]*cos(CleanFatJet_phi[0])+'+Wlep_py+', 2    )'
ww_py='(     CleanFatJet_pt[0]*cos(CleanFatJet_phi[0])+'+Wlep_py+')'
ww_pz_pow2=' pow(     CleanFatJet_pt[0]*cos(CleanFatJet_phi[0])+'+Wlep_pz+', 2    )'
ww_pz='(     CleanFatJet_pt[0]*cos(CleanFatJet_phi[0])+'+Wlep_pz+')'
ww_E_pow2=' pow(     CleanFatJet_pt[0]*cos(CleanFatJet_phi[0])+'+Wlep_E+', 2    )'
ww_E='(     CleanFatJet_pt[0]*cos(CleanFatJet_phi[0])+'+Wlep_E+')'

mww = '( sqrt( '+ww_E_pow2+' - '+ww_px_pow2+' - '+ww_py_pow2+' -'+ww_pz_pow2+'    )     )'
ww_pt='( sqrt( '+ww_px_pow2+' + '+ww_py_pow2+'  )  )'
ww_phi = '(atan('+ww_py+'/'+ww_px+' ) )'
ww_eta=' ( asinh('+ww_pz+'/'+ww_pt+') )'


boost_Base='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
    +LepWPCut+'&&'\
    +'(( Alt$( Lepton_pt[1],-1) < 15*( Alt$(Lepton_pdgId[1], 11) * Alt$(Lepton_pdgId[1], 11) ==11*11) ) || ( Alt$( Lepton_pt[1],-1) < 10* (Alt$(Lepton_pdgId[1], 13) * Alt$(Lepton_pdgId[1], 13) ==13*13 )) )'+'&&'\
    +'( '+MET_pt+' > 40 )'+'&&'\
    +'(nCleanFatJet>0)' + '&&' + 'Alt$(CleanFatJet_pt[0], -1) > 200'

#------End of Variable Definition-----#
cuts['boost_SR']= boost_Base + '&&'\
    +'('+nbjet+'<1)' + '&&'\
    +'(CleanFatJet_tau21[0] < 0.4)' + '&&'\
    +'(min('+Wlep_pt+',CleanFatJet_pt[0])/('+mww+') > 0.4)' + '&&'\
    +'(CleanFatJet_mass[0]> 65 && CleanFatJet_mass[0]< 105 )'


cuts['boost_SB']= boost_Base + '&&'\
    +'('+nbjet+'<1)' + '&&'\
    +'(CleanFatJet_tau21[0] < 0.4)' + '&&'\
    +'(min('+Wlep_pt+',CleanFatJet_pt[0])/('+mww+') > 0.4)' + '&&'\
    +'( (CleanFatJet_mass[0]> 40 && CleanFatJet_mass[0]< 65) || ( CleanFatJet_mass[0]<250 && CleanFatJet_mass[0]>105 ) )'

cuts['boost_SRB']= boost_Base + '&&'\
    +'('+nbjet+'<1)' + '&&'\
    +'(CleanFatJet_tau21[0] < 0.4)' + '&&'\
    +'(min('+Wlep_pt+',CleanFatJet_pt[0])/('+mww+') > 0.4)' + '&&'\
    +'( (CleanFatJet_mass[0]> 40 && CleanFatJet_mass[0]< 250) )'

cuts['boost_Top']= boost_Base + '&&'\
    +'('+nbjet+'>0)' + '&&'\
    +'(CleanFatJet_tau21[0] < 0.4)' + '&&'\
    +'(min('+Wlep_pt+',CleanFatJet_pt[0])/('+mww+') > 0.4)' + '&&'\
    +'( (CleanFatJet_mass[0]> 65 && CleanFatJet_mass[0]< 105) )'


#cuts['boost_SBmPtovM']= boost_Base + '&&'\
#    +'('+nbjet+'<1)' + '&&'\
#    +'(CleanFatJet_tau21[0] < 0.4)' + '&&'\
#    +'( (CleanFatJet_mass[0]> 40 && CleanFatJet_mass[0]< 65) || ( CleanFatJet_mass[0]<250 && CleanFatJet_mass[0]>105 ) )'
#
#
#cuts['boost_SRmPtovM']= boost_Base + '&&'\
#    +'('+nbjet+'<1)' + '&&'\
#    +'(CleanFatJet_tau21[0] < 0.4)' + '&&'\
#    +'(CleanFatJet_mass[0]> 65 && CleanFatJet_mass[0]< 105 )'
#
#cuts['boost_SBmtau21']= boost_Base + '&&'\
#    +'('+nbjet+'<1)' + '&&'\
#    +'(min('+Wlep_pt+',CleanFatJet_pt[0])/('+mww+') > 0.4)' + '&&'\
#    +'( (CleanFatJet_mass[0]> 40 && CleanFatJet_mass[0]< 65) || ( CleanFatJet_mass[0]<250 && CleanFatJet_mass[0]>105 ) )'
#
#
#cuts['boost_SRmtau21']= boost_Base + '&&'\
#    +'('+nbjet+'<1)' + '&&'\
#    +'(min('+Wlep_pt+',CleanFatJet_pt[0])/('+mww+') > 0.4)' + '&&'\
#    +'(CleanFatJet_mass[0]> 65 && CleanFatJet_mass[0]< 105 )'
#
