import os

scriptname=opt.nuisancesFile

SITE=os.uname()[1]


xrootdPath=''
if    'iihe' in SITE :
  xrootdPath  = 'dcap://maite.iihe.ac.be/'
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/'
elif  'cern' in SITE :
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'

elif  'sdfarm' in SITE:
  xrootdPath = 'root://cms-xrdr.private.lo:2094'
  treeBaseDir = "/xrd/store/user/jhchoi/Latino/HWWNano/"



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


#for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
for shift in ['lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
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



eff_m_syst = ['Lepton_tightMuon_'+muWP+'_TotSF_Up'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0]','Lepton_tightMuon_'+muWP+'_TotSF_Down'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0]']

nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, eff_m_syst) for skey in mc),
}


eff_tau21_syst = ['(0.97-0.06)/(0.97)','(0.97+0.06)/(0.97)']
if 'Boosted' in scriptname: 
  nuisances['eff_tau21'] = {
    
    'name': 'CMS_eff_tau21_2017',
    'kind': 'weight',
    'type': 'shape',
  'samples': dict((skey, eff_tau21_syst) for skey in mc),
  
  }




nuisances['jes'] = {
    'name': 'CMS_scale_j_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
  'folderUp': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSkimJHv6_7__JESup_Total_HMVAR7',
  'folderDown': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSkimJHv6_7__JESdo_Total_HMVAR7',
}



nuisances['fatjes'] = {
    'name': 'CMS_scale_fj_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
  'folderUp': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSkimJHv6_7__FATJESup_HMVAR7',
  'folderDown': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSkimJHv6_7__FATJESdo_HMVAR7',

}




nuisances['fatjer'] = {
    'name': 'CMS_res_fj_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
  'folderUp': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSkimJHv6_7__FATJERup_HMVAR7',
  'folderDown': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSkimJHv6_7__FATJERdo_HMVAR7',

}



nuisances['fatjms'] = {
    'name': 'CMS_scale_msd_fj_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
  'folderUp': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSkimJHv6_7__FATJMSup_HMVAR7',
  'folderDown': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSkimJHv6_7__FATJMSdo_HMVAR7',

}





nuisances['fatjmr'] = {
    'name': 'CMS_res_msd_fj_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
  'folderUp': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSkimJHv6_7__FATJMRup_HMVAR7',
  'folderDown': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSkimJHv6_7__FATJMRdo_HMVAR7',

}


nuisances['mupt'] = {
    'name': 'CMS_scale_muon_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
  'folderUp': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSkimJHv6_7__MupTup_HMVAR7',
  'folderDown': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSkimJHv6_7__MupTdo_HMVAR7',
}


nuisances['elept'] = {
    'name': 'CMS_scale_electron_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
  'folderUp': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSkimJHv6_7__ElepTup_HMVAR7',
  'folderDown': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSkimJHv6_7__ElepTdo_HMVAR7',
}


nuisances['met'] = {
    'name': 'CMS_scale_met_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
  'folderUp': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSkimJHv6_7__METdo_HMVAR7',
  'folderDown': xrootdPath+'/'+treeBaseDir+'/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSkimJHv6_7__METdo_HMVAR7',
}

pu_syst=['puWeightUp/puWeight','puWeightDown/puWeight']


nuisances['PU'] = {
    'name': 'CMS_PU_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, pu_syst) for skey in mc),
}


##ratepaara norm
nuisances['wjets0j_norm'] = {
  'name'  : 'CMS_w_norm0j',
  'samples':{'Wjets0j'},
  'type'  : 'rateParam',
}

nuisances['wjets1j_norm'] = {
  'name'  : 'CMS_w_norm1j',
  'samples':{'Wjets1j'},
  'type'  : 'rateParam',
}
nuisances['wjets2j_norm'] = {
  'name'  : 'CMS_w_norm1j',
  'samples':{'Wjets2j'},
  'type'  : 'rateParam',
}

nuisances['top_norm'] = {
  'name'  : 'CMS_top_norm',
  'samples':{'top'},
  'type'  : 'rateParam',
}
nuisances['cms_qcdem_mc_norm'] = {
  'name': 'cms_qcdem_mc_norm',
  'samples':['QCD_EM'],
  'type'  : 'rateParam',  
}
nuisances['cms_qcdmu_mc_norm'] = {
  'name': 'cms_qcdmu_mc_norm',
  'samples':['QCD_MU'],
  'type'  : 'rateParam',  
}
nuisances['cms_qcdbctoe_mc_norm'] = {
  'name': 'cms_qcdbctoe_mc_norm',
  'samples':['QCD_bcToE'],
  'type'  : 'rateParam',  
}

## Use the following if you want to apply the automatic combine MC stat nuisances.
'''
nuisances['stat'] = {
    'type': 'auto',
    'maxPoiss': '10',
    'includeSignal': '0',
    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': {}
}
'''
