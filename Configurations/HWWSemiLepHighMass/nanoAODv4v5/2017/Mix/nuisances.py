import os

SITE=os.uname()[1]


xrootdPath=''
if    'iihe' in SITE :
  xrootdPath  = 'dcap://maite.iihe.ac.be/'
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/'
elif  'cern' in SITE :
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'

elif  'sdfarm' in SITE:
  xrootdPath = 'root://cms-xrdr.private.lo:2094'
  treeBaseDir = "/xrootd/store/user/jhchoi/Latino/HWWNano/"



eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'


mc = [skey for skey in samples if skey != 'DATA']







nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2017',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc )
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.008') for skey in mc)
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc )
}

nuisances['lumi_BBDefl'] = {
    'name': 'lumi_13TeV_BBDefl',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc )
}

nuisances['lumi_DynBeta'] = {
    'name': 'lumi_13TeV_DynBeta',
    'type': 'lnN',
    'samples': dict((skey, '1.005') for skey in mc )
}

nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc )
}

nuisances['lumi_Ghosts'] = {
    'name': 'lumi_13TeV_Ghosts',
    'type': 'lnN',
    'samples': dict((skey, '1.001') for skey in mc )
}


for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2017'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
    }



trig_syst = ['TriggerEffWeight_1l_u/TriggerEffWeight_1l','TriggerEffWeight_1l_d/TriggerEffWeight_1l']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc),
}


prefire_syst = ['PrefireWeight_Up/PrefireWeight', 'PrefireWeight_Down/PrefireWeight']


nuisances['prefire'] = {
    'name': 'CMS_eff_prefiring_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, prefire_syst) for skey in mc),
}



#eff_e_syst = ['Lepton_tightElectron_'+eleWP+'_IdIsoSF_Up'+'[0]/Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]','Lepton_tightElectron_'+eleWP+'_IdIsoSF_Down'+'[0]/Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]']
eff_e_syst = ['Lepton_tightElectron_'+eleWP+'_TotSF_Up'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]','Lepton_tightElectron_'+eleWP+'_TotSF_Down'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]']

nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, eff_e_syst) for skey in mc),
}

#MCl1loose2017v5__MCCorr2017v5__METup__Semilep2017_whad30__CorrFatJetMass__HMlnjjSelBWR
nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__ElepTup__Semilep2017_whad30__CorrFatJetMass__HMlnjjSelBWR/',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__ElepTdo__Semilep2017_whad30__CorrFatJetMass__HMlnjjSelBWR/',
    
}

eff_m_syst = ['Lepton_tightMuon_'+muWP+'_TotSF_Up'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0]','Lepton_tightMuon_'+muWP+'_TotSF_Down'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0]']


nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, eff_m_syst) for skey in mc),
}



nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__MupTup__Semilep2017_whad30__CorrFatJetMass__HMlnjjSelBWR/',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__MupTdo__Semilep2017_whad30__CorrFatJetMass__HMlnjjSelBWR/',
    
}

nuisances['jes'] = {
    'name': 'CMS_scale_j_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__JESup__Semilep2017_whad30__CorrFatJetMass__HMlnjjSelBWR/',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__JESdo__Semilep2017_whad30__CorrFatJetMass__HMlnjjSelBWR/',
    
}


nuisances['fatjes'] = {
    'name': 'CMS_scale_fatj_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__Semilep2017_whad30__CorrFatJetMass__FatJetMass_up__HMlnjjSelBWR/',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__Semilep2017_whad30__CorrFatJetMass__FatJetMass_do__HMlnjjSelBWR/',
    
}

nuisances['fatjer'] = {
    'name': 'CMS_scale_fatjres_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__Semilep2017_whad30__CorrFatJetMass__FatJetMassRes_up__HMlnjjSelBWR/',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__Semilep2017_whad30__CorrFatJetMass__FatJetMassRes_do__HMlnjjSelBWR/',
    
}

nuisances['met'] = {
    'name': 'CMS_scale_met_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__METup__Semilep2017_whad30__CorrFatJetMass__HMlnjjSelBWR/',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__METdo__Semilep2017_whad30__CorrFatJetMass__HMlnjjSelBWR/',
    
}

pu_syst=['puWeightUp/puWeight','puWeightDown/puWeight']


nuisances['PU'] = {
    'name': 'CMS_PU_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, pu_syst) for skey in mc),
    
}




nuisances['tau21'] = {
  'name': 'CMS_eff_vtag_tau21_sf_13TeV',
  'type': 'lnN',
  'samples': dict((skey, '1.04') for skey in mc )
  
  #'Samples': dict((skey, tau21_syst) for skey in mc )
}



'''
nuisances['dummy'] = {
  'name': 'dummy',
  'type': 'lnN',
  'samples': dict((skey, '1.0000000000000000001') for skey in mc )
  
  #'Samples': dict((skey, tau21_syst) for skey in mc )
}

'''




'''
##Need to investigate which sample has this weight.
ps_syst=['PSWeight[0]', 'PSWeight[1]', 'PSWeight[2]', 'PSWeight[3]']

nuisances['PS']  = {
    'name': 'PS',
    'type': 'shape',
    'kind': 'weight_envelope',
    'samples':dict((skey, ps_syst) for skey in mc),
    'AsLnN': '1'
}
'''
