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




#------End of Variable Definition-----#




cuts['FatSR']='IsFatSig && !IsFatTop' +'&&'\
		+ LepWPCut

cuts['FatSB']='IsFatSB && !IsFatTop' + '&&'\
		+ LepWPCut

cuts['FatTop']='IsFatSig && IsFatTop' + '&&'\
                + LepWPCut

cuts['JjSR']='IsJjSig && !IsJjTop'+'&&'\
		+LepWPCut

cuts['JjSB']='IsJjSB && !IsJjTop'+'&&'\
		+LepWPCut

cuts['JjTop']='IsJjSig && !IsJjTop'+'&&'\
		+LepWPCut
