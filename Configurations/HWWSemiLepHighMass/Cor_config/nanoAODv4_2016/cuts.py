#import my.Wlep_sel
#import my.final_fatjetsel


'''
       handle = open(prodFile,'r')
       exec(handle)

'''

#handle = open()
#exec()


supercut = 'nLepton>0'
#supercut = 'nMuon==2 || nElectron==2'
#cuts={}

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





'''

cuts['l1_pt_eta']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'

cuts['Lepton_veto']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'

cuts['met_cut']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 40 )'

cuts['fatjet1Msoft40']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 40 )'+'&&'\
    +'(nPreselFatJet==1)'
'''
cuts['fatjet1Msoft40_bevent']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 40 )'+'&&'\
    +'(nPreselFatJet==1)'+'&&'\
    +'('+nbjet+'>0)'

cuts['fatjet1Msoft40_bvetoevent']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 40 )'+'&&'\
    +'(nPreselFatJet==1)'+'&&'\
    +'('+nbjet+'==0)'


cuts['fatjet1Msoft40_bevent_msoftdropSB']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 40 )'+'&&'\
    +'(nPreselFatJet==1)'+'&&'\
    +'('+nbjet+'>0)'+'&&'\
    +'(PreselFatJet_msoftdrop[0]< 65 || ( PreselFatJet_msoftdrop[0]<250 && PreselFatJet_msoftdrop[0]>105 ) )'


cuts['fatjet1Msoft40_bvetoevent_msoftdropSB']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 40 )'+'&&'\
    +'(nPreselFatJet==1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'(PreselFatJet_msoftdrop[0]< 65 || ( PreselFatJet_msoftdrop[0]<250 && PreselFatJet_msoftdrop[0]>105 ) )'


cuts['fatjet1Msoft40_bevent_msoftdropSR']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13))))'+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 40 )'+'&&'\
    +'(nPreselFatJet==1)'+'&&'\
    +'('+nbjet+'>0)'+'&&'\
    +'(PreselFatJet_msoftdrop[0]>65 && PreselFatJet_msoftdrop[0]<105  )'


cuts['fatjet1Msoft40_bvetoevent_msoftdropSR']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13))))'+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 40 )'+'&&'\
    +'(nPreselFatJet==1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'(PreselFatJet_msoftdrop[0]>65 && PreselFatJet_msoftdrop[0]<105  )'




cuts['fatjet1Msoft40_bevent_msoftdropSR_ptw_over_mww04']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13))))'+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 40 )'+'&&'\
    +'(nPreselFatJet==1)'+'&&'\
    +'('+nbjet+'>0)'+'&&'\
    +'(PreselFatJet_msoftdrop[0]>65 && PreselFatJet_msoftdrop[0]<105  )'+'&&'\
    +'(min(Wlep_pt,PreselFatJet_pt)/('+mww+') > 0.4)'


cuts['fatjet1Msoft40_bvetoevent_msoftdropSR_ptw_over_mww04']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13))))'+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 40 )'+'&&'\
    +'(nPreselFatJet==1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'(PreselFatJet_msoftdrop[0]>65 && PreselFatJet_msoftdrop[0]<105  )'+'&&'\
    +'(min(Wlep_pt,PreselFatJet_pt)/('+mww+') > 0.4)'




cuts['fatjet1Msoft40_bevent_msoftdropSB_tau21']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13))))'+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 40 )'+'&&'\
    +'(nPreselFatJet==1)'+'&&'\
    +'('+nbjet+'>0)'+'&&'\
    +'(PreselFatJet_msoftdrop[0]<65 || ( PreselFatJet_msoftdrop[0]<250 && PreselFatJet_msoftdrop[0]>105 )  )'+'&&'\
    +'(Alt$(PreselFatJet_tau2/PreselFatJet_tau1,1) < 0.4)'


cuts['fatjet1Msoft40_bvetoevent_msoftdropSB_tau21']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13))))'+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 40 )'+'&&'\
    +'(nPreselFatJet==1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'(PreselFatJet_msoftdrop[0]<65 || ( PreselFatJet_msoftdrop[0]<250 && PreselFatJet_msoftdrop[0]>105 )  )'+'&&'\
    +'(Alt$(PreselFatJet_tau2/PreselFatJet_tau1,1) < 0.4)'


cuts['fatjet1Msoft40_bevent_msoftdropSR_tau21']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13))))'+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 40 )'+'&&'\
    +'(nPreselFatJet==1)'+'&&'\
    +'('+nbjet+'>0)'+'&&'\
    +'(PreselFatJet_msoftdrop[0]>65 && PreselFatJet_msoftdrop[0]<105  )'+'&&'\
    +'(Alt$(PreselFatJet_tau2/PreselFatJet_tau1,1) < 0.4)'

cuts['fatjet1Msoft40_bvetoevent_msoftdropSR_tau21']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13))))'+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 40 )'+'&&'\
    +'(nPreselFatJet==1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'(PreselFatJet_msoftdrop[0]>65 && PreselFatJet_msoftdrop[0]<105  )'+'&&'\
    +'(Alt$(PreselFatJet_tau2/PreselFatJet_tau1,1) < 0.4)'


cuts['fatjet1Msoft40_bevent_msoftdropSR_ptw_over_mww_04_tau21']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13))))'+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 40 )'+'&&'\
    +'(nPreselFatJet==1)'+'&&'\
    +'('+nbjet+'>0)'+'&&'\
    +'(PreselFatJet_msoftdrop[0]>65 && PreselFatJet_msoftdrop[0]<105  )'+'&&'\
    +'(Alt$(PreselFatJet_tau2/PreselFatJet_tau1,1) < 0.4)'+'&&'\
    +'(min(Wlep_pt,PreselFatJet_pt)/('+mww+') > 0.4)'


cuts['fatjet1Msoft40_bvetoevent_msoftdropSR_ptw_over_mww_04_tau21']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13))))'+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 40 )'+'&&'\
    +'(nPreselFatJet==1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'(PreselFatJet_msoftdrop[0]>65 && PreselFatJet_msoftdrop[0]<105  )'+'&&'\
    +'(Alt$(PreselFatJet_tau2/PreselFatJet_tau1,1) < 0.4)'+'&&'\
    +'(min(Wlep_pt,PreselFatJet_pt)/('+mww+') > 0.4)'

