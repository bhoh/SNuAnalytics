#-----Variable Deinition-----#
bAlgo='DeepB'


#------End of Variable Definition-----#


variables['Event'] = {
    'name' : '1',
    'range':(1,0,1),
    'xaxis':'1',
    'fold': 3
}


variables['CleanFatJetPassMBoostedSB_tau21']={
    'name' : 'CleanFatJetPassMBoostedSB_tau21[0]',
    'range':(20,0,1),
    'xaxis':'FatJet #tau_{21}',
    'fold':0
}

variables['CleanFatJetPassMBoostedSB_pt']={
    'name' : 'CleanFatJetPassMBoostedSB_pt[0]',
    'range':(50,100,1000),
    'xaxis':'FatJet P_{T} [GeV]',
    'fold':0
}

variables['CleanFatJetPassMBoostedSB_mass']={
    'name' : 'CleanFatJetPassMBoostedSB_mass[0]',
    'range':(50,40,250),
    'xaxis':'FatJet Mass [GeV]',
    'fold':0
}

variables['CleanFatJetPassMBoostedSB_WptOvHfatM']={
    'name' : 'CleanFatJetPassMBoostedSB_WptOvHfatM[0]',
    'range':(20,0,1),
    'xaxis':'min(W_{pT})/M(WW)',
    'fold':0
}

variables['CleanFatJetPassMBoostedSB_HlnFat_mass']={
    'name' : 'CleanFatJetPassMBoostedSB_HlnFat_mass[0]',
    'range':(80,0,4000),
    'xaxis':'m_{lnJ} [GeV]',
    'fold':0
}

variables['CleanFatJetPassMBoostedSR_tau21']={
    'name' : 'CleanFatJetPassMBoostedSB_tau21[0]',
    'range':(20,0,1),
    'xaxis':'FatJet #tau_{21}',
    'fold':0
}

variables['CleanFatJetPassMBoostedSR_pt']={
    'name' : 'CleanFatJetPassMBoostedSB_pt[0]',
    'range':(50,100,1000),
    'xaxis':'FatJet P_{T} [GeV]',
    'fold':0
}

variables['CleanFatJetPassMBoostedSR_mass']={
    'name' : 'CleanFatJetPassMBoostedSR_mass[0]',
    'range':(50,40,250),
    'xaxis':'FatJet Mass [GeV]',
    'fold':0
}

variables['CleanFatJetPassMBoostedSR_WptOvHfatM']={
    'name' : 'CleanFatJetPassMBoostedSR_WptOvHfatM[0]',
    'range':(20,0,1),
    'xaxis':'min(Wlep_{pT},WJ_{pT})/M(WW)',
    'fold':0
}
variables['CleanFatJetPassMBoostedSR_HlnFat_mass']={
    'name' : 'CleanFatJetPassMBoostedSB_HlnFat_mass[0]',
    'range':(80,0,4000),
    'xaxis':'m_{lnJ} [GeV]',
    'fold':0
}


variables['WptOvHak4M']={
    'name' : 'WptOvHak4M',
    'range':(20,0,1),
    'xaxis':'min(Wlep_{pT},Wjj_{pT})/M(WW)',
    'fold':0
}

variables['lepton_pt']={
    'name' : 'Lepton_pt[0]',
    'range':(50,25,600),
    'xaxis':'lepton P_{T} [GeV]',
    'fold':0

}
variables['lepton_eta']={
    'name' : 'Lepton_eta[0]',
    'range':(100,-5,5),
    'xaxis':'lepton #eta',
    'fold':0
}
variables['CleanJet_pt[0]']={
    'name' : 'CleanJet_pt[0]',
    'range':(50,20,600),
    'xaxis':'jet P_{T} [GeV]',
    'fold':0
}
variables['CleanJet_eta[0]']={
    'name' : 'CleanJet_eta[0]',
    'range':(100,-5,5),
    'xaxis':'jet #eta',
    'fold':0
}

variables['CleanJet_phi[0]']={
    'name' : 'CleanJet_phi[0]',
    'range':(50,-4,4),
    'xaxis':'jet #phi',
    'fold':0
}

variables['nbjetBoosted']={
    'name' : 'nbjetBoosted_jetIdx',
    'range':(10,0,10.),
    'xaxis':'nbjets',
    'fold':3
}

variables['nbjetResolved']={
    'name' : 'nbjetResolved_jetIdx',
    'range':(10,0,10.),
    'xaxis':'nbjets',
    'fold':3
}






variables['bjet_etaBoosted']={
    'name' : 'Jet_eta[bjetBoosted_jetIdx]',
    'range':(100,-5,5),
    'xaxis':'bjet_eta',
    'fold':0
}

variables['bjet_etaResolved']={
    'name' : 'Jet_eta[bjetResolved_jetIdx]',
    'range':(100,-5,5),
    'xaxis':'bjet_eta',
    'fold':0
}

variables['bjet_ptBoosted']={
    'name' : 'Jet_pt[bjetBoosted_jetIdx]',
    'range':(50,0,600),
    'xaxis':'bjet_pt',
    'fold':0
}
variables['bjet_ptResolved']={
    'name' : 'Jet_pt[bjetResolved_jetIdx]',
    'range':(50,0,600),
    'xaxis':'bjet_pt',
    'fold':0
}

variables['bjet_'+bAlgo+'Boosted']={
    'name' : 'Jet_btag'+bAlgo+'[bjetBoosted_jetIdx]',
    'range':(50,0,1),
    'xaxis':'bjet_'+bAlgo,
    'fold':0

}

variables['bjet_'+bAlgo+'Resolved']={
    'name' : 'Jet_btag'+bAlgo+'[bjetResolved_jetIdx]',
    'range':(50,0,1),
    'xaxis':'bjet_'+bAlgo,
    'fold':0
}





variables['PuppiMet']={
    'name' : 'PuppiMET_pt',
    'range':(50,0,600),
    'xaxis':'MET [GeV]',
    'fold':0
}

variables['Wlep_pt']={
    'name' : 'Wlep_pt_Puppi',
    'range':(50,50,1000),
    'xaxis':'W_{Lep} P_{T} [GeV]',
    'fold':0
}

variables['lnjj_mt']={
    'name' : 'Hlnjj_mt',
    'range':(50,0,400),
    'xaxis':'lnjj m_{T} [GeV]',
    'fold':0
}





variables ['PV_npvs']={
    'name' : 'PV_npvs',
    'range' : (80,0,80),
    'xaxis' : 'PV_npvs',
    'fold':3
}




variables['jj_mass'] = {
    'name' : 'Whad_mass',
    'range':(50,40,250),
    'xaxis':'m_{jj} [GeV]',
    'fold':0
}

variables['jj_pt'] = {
    'name' : 'Whad_pt',
    'range':(50,50,900),
    'xaxis':'jj P_{T} [GeV]',
    'fold':0
}

variables['LnJJ_mass']={
    'name': 'Hlnjj_mass',
    'range':(80,0,4000),
    'xaxis':'m_{lnjj} [GeV]',
    'fold':0
}


variables['Wlep_mt']={
    'name': 'Wlep_mt',
    'range':(80,0,4000),
    'xaxis':'mt_{Wlep} [GeV]',
    'fold':0
}


variables['vbfFat_jj_dEta']={
    'name': 'vbfFat_jj_dEta',
    'range':(100,0,10),
    'xaxis':'#Delta#eta(jj)',
    'fold':0
}
variables['vbfFat_jj_mass']={
    'name': 'vbfFat_jj_mass',
    'range':(100,0,1000),
    'xaxis':'M(jj) [GeV]',
    'fold':0
}


variables['vbfjj_jj_dEta']={
    'name': 'vbfjj_jj_dEta',
    'range':(100,0,10),
    'xaxis':'#Delta(#eta)(jj)',
    'fold':0
}

variables['vbfjj_jj_mass']={
    'name': 'vbfjj_jj_mass',
    'range':(100,0,1000),
    'xaxis':'M(jj) [GeV]',
    'fold':0
}



