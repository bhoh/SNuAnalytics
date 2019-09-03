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
njet='(Sum$(Jet_jetId>0 && Jet_pt>30 && fabs(Jet_eta) < 2.4))'
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

eleWP='mva_90p_Iso2016'
#eleWP='cut_WP_Tight80X'
muWP='cut_Tight80x'
LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5) && (Lepton_isTightElectron_'+eleWP+'[1]>0.5 || Lepton_isTightMuon_'+muWP+'[1]>0.5)'
OS_SameFlavour='((Lepton_pdgId[0]+Lepton_pdgId[1])==0)'


cuts['two_tight_lep']=\
                       '(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
                       '(  Lepton_pt[1]> 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13  && fabs(Lepton_eta[1])  < (2.1*(abs(Lepton_pdgId[1])==11) + 2.4*(abs(Lepton_pdgId[1]==13)))  )'+'&&'\
                       +'( Alt$( Lepton_pt[2],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )&&'\
                       +LepWPCut+'&&'\
                       +OS_SameFlavour


cuts['two_tight_lep__met_over_40']=\
                       '(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
                       '(  Lepton_pt[1]> 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13  && fabs(Lepton_eta[1])  < (2.1*(abs(Lepton_pdgId[1])==11) + 2.4*(abs(Lepton_pdgId[1]==13)))  )'+'&&'\
                       +'( Alt$( Lepton_pt[2],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )&&'\
                       +LepWPCut+'&&'\
                       +'(MET_pt>40)&&'\
                       +OS_SameFlavour


cuts['two_tight_lep__met_below_40']=\
                       '(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
                       '(  Lepton_pt[1]> 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13  && fabs(Lepton_eta[1])  < (2.1*(abs(Lepton_pdgId[1])==11) + 2.4*(abs(Lepton_pdgId[1]==13)))  )'+'&&'\
                       +'( Alt$( Lepton_pt[2],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )&&'\
                       +LepWPCut+'&&'\
                       +'(MET_pt<40)&&'\
                       +OS_SameFlavour



cuts['two_tight_lep__atleast_1jet']=\
                       '(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
                       '(  Lepton_pt[1]> 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13  && fabs(Lepton_eta[1])  < (2.1*(abs(Lepton_pdgId[1])==11) + 2.4*(abs(Lepton_pdgId[1]==13)))  )'+'&&'\
                       +'( Alt$( Lepton_pt[2],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )&&'\
                       +LepWPCut+'&&'\
                       +'('+njet+'>0.5)&&'\
                       +OS_SameFlavour


cuts['two_tight_lep__met_over_40__atleast_1jet']=\
                       '(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
                       '(  Lepton_pt[1]> 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13  && fabs(Lepton_eta[1])  < (2.1*(abs(Lepton_pdgId[1])==11) + 2.4*(abs(Lepton_pdgId[1]==13)))  )'+'&&'\
                       +'( Alt$( Lepton_pt[2],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )&&'\
                       +LepWPCut+'&&'\
                       +'(MET_pt>40)&&'\
                       +'('+njet+'>0.5)&&'\
                       +OS_SameFlavour


cuts['two_tight_lep__met_below_40__atleast_1jet']=\
                       '(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
                       '(  Lepton_pt[1]> 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13  && fabs(Lepton_eta[1])  < (2.1*(abs(Lepton_pdgId[1])==11) + 2.4*(abs(Lepton_pdgId[1]==13)))  )'+'&&'\
                       +'( Alt$( Lepton_pt[2],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )&&'\
                       +LepWPCut+'&&'\
                       +'(MET_pt<40)&&'\
                       +'('+njet+'>0.5)&&'\
                       +OS_SameFlavour



cuts['two_tight_lep__atleast_2jet']=\
                       '(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
                       '(  Lepton_pt[1]> 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13  && fabs(Lepton_eta[1])  < (2.1*(abs(Lepton_pdgId[1])==11) + 2.4*(abs(Lepton_pdgId[1]==13)))  )'+'&&'\
                       +'( Alt$( Lepton_pt[2],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )&&'\
                       +LepWPCut+'&&'\
                       +'('+njet+'>1.5)&&'\
                       +OS_SameFlavour


cuts['two_tight_lep__met_over_40__atleast_2jet']=\
                       '(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
                       '(  Lepton_pt[1]> 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13  && fabs(Lepton_eta[1])  < (2.1*(abs(Lepton_pdgId[1])==11) + 2.4*(abs(Lepton_pdgId[1]==13)))  )'+'&&'\
                       +'( Alt$( Lepton_pt[2],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )&&'\
                       +LepWPCut+'&&'\
                       +'(MET_pt>40)&&'\
                       +'('+njet+'>1.5)&&'\
                       +OS_SameFlavour


cuts['two_tight_lep__met_below_40__atleast_2jet']=\
                       '(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
                       '(  Lepton_pt[1]> 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13  && fabs(Lepton_eta[1])  < (2.1*(abs(Lepton_pdgId[1])==11) + 2.4*(abs(Lepton_pdgId[1]==13)))  )'+'&&'\
                       +'( Alt$( Lepton_pt[2],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )&&'\
                       +LepWPCut+'&&'\
                       +'(MET_pt<40)&&'\
                       +'('+njet+'>1.5)&&'\
                       +OS_SameFlavour
