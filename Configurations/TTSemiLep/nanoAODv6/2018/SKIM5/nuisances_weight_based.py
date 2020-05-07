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
ttmc = ['TTLJ+jj','TTLJ+bb','TTLJ+cc','TTLJ+bj','TTLL']


nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2018',
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

nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc )
}

nuisances['ttXsec'] = {
    'name': 'ttXsec',
    'type': 'lnN',
    'samples': dict((skey, '1.06114') for skey in ttmc)
}

nuisances['ttbbXsec'] = {
    'name': 'ttbbXsec',
    'type': 'lnN',
    'samples': dict((skey, '1.206/0.793') for skey in ['TTLJ+bb'])
}


for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2018'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
    }



trig_syst = ['TriggerEffWeight_1l_u/TriggerEffWeight_1l','TriggerEffWeight_1l_d/TriggerEffWeight_1l']
#TODO decolerate muon, electron trigger?
#TODO define alias ElTriggerEffWeight_1l, MuTriggerEffWeight_1l
nuisances['trig'] = {
    'name': 'CMS_eff_trigger_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc),
}



eff_ele_syst = ['Lepton_tightElectron_'+eleWP+'_TotSF_Up'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]','Lepton_tightElectron_'+eleWP+'_TotSF_Down'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]']
#TODO : decorrelate ele ID, reco
nuisances['eff_ele'] = {
    'name': 'CMS_eff_ele_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, eff_ele_syst) for skey in mc),
}

'''
nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2018',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__ElepTup__Semilep2018_whad30__CorrFatJetMass__HMlnjjSelBWR/',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__ElepTdo__Semilep2018_whad30__CorrFatJetMass__HMlnjjSelBWR/',
    #'AsLnN': '1'
}
'''
eff_muon_syst = ['Lepton_tightMuon_'+muWP+'_TotSF_Up'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0]','Lepton_tightMuon_'+muWP+'_TotSF_Down'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0]']
#TODO : decorrelate muon ID, iso

nuisances['eff_muon'] = {
    'name': 'CMS_eff_muon_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, eff_muon_syst) for skey in mc),
}





'''
nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2018',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__MupTup__Semilep2018_whad30__CorrFatJetMass__HMlnjjSelBWR/',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__MupTdo__Semilep2018_whad30__CorrFatJetMass__HMlnjjSelBWR/',
    #'AsLnN': '1'
}

nuisances['jes'] = {
    'name': 'CMS_scale_j_2018',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__JESup__Semilep2018_whad30__CorrFatJetMass__HMlnjjSelBWR/',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__JESdo__Semilep2018_whad30__CorrFatJetMass__HMlnjjSelBWR/',
    #'AsLnN': '1'
}


nuisances['fatjes'] = {
    'name': 'CMS_scale_fatj_2018',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__Semilep2018_whad30__CorrFatJetMass__FatJetMass_up__HMlnjjSelBWR/',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__Semilep2018_whad30__CorrFatJetMass__FatJetMass_do__HMlnjjSelBWR/',
    #'AsLnN': '1'
}

nuisances['fatjer'] = {
    'name': 'CMS_scale_fatjres_2018',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__Semilep2018_whad30__CorrFatJetMass__FatJetMassRes_up__HMlnjjSelBWR/',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__Semilep2018_whad30__CorrFatJetMass__FatJetMassRes_do__HMlnjjSelBWR/',
    #'AsLnN': '1'
}

nuisances['met'] = {
    'name': 'CMS_scale_met_2018',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__METup__Semilep2018_whad30__CorrFatJetMass__HMlnjjSelBWR/',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__METdo__Semilep2018_whad30__CorrFatJetMass__HMlnjjSelBWR/',
    #'AsLnN': '1'
}

'''
pu_syst=['puWeightUp/puWeight','puWeightDown/puWeight']


nuisances['PU'] = {
    'name': 'CMS_PU',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, pu_syst) for skey in mc),
    #'AsLnN': '1',
}


#ps_syst=['PSWeight[0]', 'PSWeight[1]', 'PSWeight[2]', 'PSWeight[3]']
#nuisances['PS']  = {
#    'name': 'PS',
#    'type': 'shape',
#    'kind': 'weight_envelope',
#    'samples':dict((skey, ps_syst) for skey in ['TTLJ+jj']),
#    #'AsLnN': '1'
#}

##lhe_scale_syst = [ 'LHEScaleWeight[%s]'%i for i in range(9) ]
##nuisances['LHEScaleWeight'] = {
##    'name': 'LHEScaleWeight',
##    'type': 'shape',
##    'kind': 'weight_envelope',
##    'samples':dict((skey, lhe_scale_syst) for skey in mc),
##        
##}
#
##will add LHEPdfWeight
