
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
    +'( '+MET_pt+' > 30 )'+'&&'\
    +'(idx_j1 != -1)'+'&&'\
    +'(idx_j2 != -1)'+'&&'\
    +'('+nbjet+'>0)'+'&&'\
    +'('+wlep_mt+'>50)'+'&&'\
    +'((nCleanFatJet!=1))'



cuts['ResolveWjet_wlepMT50_bveto']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_\
pdgId[0]==13)))  )'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( '+MET_pt+' > 30 )'+'&&'\
    +'(idx_j1 != -1)'+'&&'\
    +'(idx_j2 != -1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'('+wlep_mt+'>50)'+'&&'\
    +'((nCleanFatJet!=1))'




cuts['ResolveWjet__wlepMT50__bveto__Whad_mass_SB']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_\
pdgId[0]==13)))  )'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( '+MET_pt+' > 30 )'+'&&'\
    +'(idx_j1 != -1)'+'&&'\
    +'(idx_j2 != -1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'(Whad_mass < 65) || (Whad_mass > 105)'+'&&'\
    +'('+wlep_mt+'>50)'+'&&'\
    +'((nCleanFatJet!=1))'


cuts['ResolveWjet__wlepMT50__bveto__Whad_mass_SR']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_\
pdgId[0]==13)))  )'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( '+MET_pt+' > 30 )'+'&&'\
    +'(idx_j1 != -1)'+'&&'\
    +'(idx_j2 != -1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'(Whad_mass > 65) && (Whad_mass < 105)'+'&&'\
    +'('+wlep_mt+'>50)'+'&&'\
    +'((nCleanFatJet!=1))'

cuts['ResolveWjet__wlepMT50__bveto__Whad_mass_SR__ptw_over_mww_035']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_\
pdgId[0]==13)))  )'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( '+MET_pt+' > 30 )'+'&&'\
    +'(idx_j1 != -1)'+'&&'\
    +'(idx_j2 != -1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'(Whad_mass > 65) && (Whad_mass < 105)'+'&&'\
    +'(min('+Wlep_pt+',Whad_pt)/('+mww+') > 0.35)'+'&&'\
    +'('+wlep_mt+'>50)'+'&&'\
    +'((nCleanFatJet!=1))'


cuts['ResolveWjet__wlepMT50__bveto__Whad_mass_SR__ptw_over_mww_035']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_\
pdgId[0]==13)))  )'+'&&'\
+LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( '+MET_pt+' > 30 )'+'&&'\
    +'(idx_j1 != -1)'+'&&'\
    +'(idx_j2 != -1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'(Whad_mass > 65) && (Whad_mass < 105)'+'&&'\
    +'(min('+Wlep_pt+',Whad_pt)/('+mww+') > 0.35)'+'&&'\
    +'('+lvqq_mt+'>60)'+'&&'\
    +'('+wlep_mt+'>50)'+'&&'\
    +'((nCleanFatJet!=1))'





