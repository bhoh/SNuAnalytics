
supercut = 'nLepton>0'


eleWP='mva_90p_Iso2016'
muWP='cut_Tight80x'

LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
bAlgo='DeepB'
bWP='0.2217'



isbjet='(Jet_jetId>0 && Jet_pt>20 && fabs(Jet_eta) < 2.4 && Jet_btag'+bAlgo+' > '+bWP+' &&  ( Iteration$ != idx_j1  ) && ( Iteration$ != idx_j2 ))'
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
##--Resolved Region--##

#--Need kinematic fit to select dijet pair.
#->Need module to make dijet select for Whad
#MET>30GeV
#M_T(Wlep) > 50 -> MT: m**2-px**2-py**2


#minPT(W)/Mww > 0.35
#MT(X) > 60


## SR : 65<m(jj)<105
## SB : mass inverse cut
## TT : no mass cut. b tagged

cuts['ResolveWjet_wlepMT50_bevent']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_\
pdgId[0]==13)))  )'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 30 )'+'&&'\
    +'(idx_j1 != -1)'+'&&'\
    +'(idx_j2 != -1)'+'&&'\
    +'('+nbjet+'>0)'



cuts['ResolveWjet_wlepMT50_bveto']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_\
pdgId[0]==13)))  )'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 30 )'+'&&'\
    +'(idx_j1 != -1)'+'&&'\
    +'(idx_j2 != -1)'+'&&'\
    +'('+nbjet+'==0)'




cuts['ResolveWjet__wlepMT50__bveto__Whad_mass_SB']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_\
pdgId[0]==13)))  )'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 30 )'+'&&'\
    +'(idx_j1 != -1)'+'&&'\
    +'(idx_j2 != -1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'(Whad_mass < 65) || (Whad_mass < 105)'



cuts['ResolveWjet__wlepMT50__bveto__Whad_mass_SR']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_\
pdgId[0]==13)))  )'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 30 )'+'&&'\
    +'(idx_j1 != -1)'+'&&'\
    +'(idx_j2 != -1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'(Whad_mass > 65) && (Whad_mass < 105)'


cuts['ResolveWjet__wlepMT50__bveto__Whad_mass_SR__ptw_over_mww_035']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_\
pdgId[0]==13)))  )'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 30 )'+'&&'\
    +'(idx_j1 != -1)'+'&&'\
    +'(idx_j2 != -1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'(Whad_mass > 65) && (Whad_mass < 105)'+'&&'\
    +'(min(Wlep_pt,Whad_pt)/('+mww+') > 0.35)'


cuts['ResolveWjet__wlepMT50__bveto__Whad_mass_SR__ptw_over_mww_035']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_\
pdgId[0]==13)))  )'+'&&'\
+LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( MET_pt > 30 )'+'&&'\
    +'(idx_j1 != -1)'+'&&'\
    +'(idx_j2 != -1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'(Whad_mass > 65) && (Whad_mass < 105)'+'&&'\
    +'(min(Wlep_pt,Whad_pt)/('+mww+') > 0.35)'+'&&'\
    +'('+lvqq_mt+'>60)'






