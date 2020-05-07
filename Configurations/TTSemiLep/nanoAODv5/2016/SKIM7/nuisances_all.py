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
ttmc += ['CHToCB_M%s'%mass for mass in ['075','080','085','090','100','110','120','130','140','150']]

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2016',
    'type': 'lnN',
    'samples': dict((skey, '1.022') for skey in mc )
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.009') for skey in mc)
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

nuisances['lumi_Ghosts'] = {
    'name': 'lumi_13TeV_Ghosts',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc )
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
        name += '_2016'

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
    'name': 'CMS_eff_trigger_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc),
}



eff_ele_syst = ['Lepton_tightElectron_'+eleWP+'_TotSF_Up'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]','Lepton_tightElectron_'+eleWP+'_TotSF_Down'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]']
#TODO : decorrelate ele ID, reco
nuisances['eff_ele'] = {
    'name': 'CMS_eff_ele_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, eff_ele_syst) for skey in mc),
}

eff_muon_syst = ['Lepton_tightMuon_'+muWP+'_TotSF_Up'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0]','Lepton_tightMuon_'+muWP+'_TotSF_Down'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0]']
#TODO : decorrelate muon ID, iso

nuisances['eff_muon'] = {
    'name': 'CMS_eff_muon_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, eff_muon_syst) for skey in mc),
}

pu_syst=['puWeightUp/puWeight','puWeightDown/puWeight']


nuisances['PU'] = {
    'name': 'CMS_PU',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, pu_syst) for skey in mc),
    #'AsLnN': '1',
}





JECUnc_nom_branches = [
    'Jet_pt_nom',
    'MET_CHToCB_pt_nom',
    'initial_dijet_M_nom',         
    'initial_dijet_M_high_nom',    
    'fitted_dijet_M_nom',          
    'fitted_dijet_M_high_nom',     
    'best_chi2_nom',               
    'fitter_status_nom',           
    'down_type_jet_b_tagged_nom',  
    'hadronic_top_b_jet_idx_nom',  
    'leptonic_top_b_jet_idx_nom',  
    'w_ch_up_type_jet_idx_nom',    
    'w_ch_down_type_jet_idx_nom',  
    'hadronic_top_b_jet_pull_nom', 
    'w_ch_up_type_jet_pull_nom',   
    'w_ch_down_type_jet_pull_nom', 
    'hadronic_top_M_nom',          
    'leptonic_top_M_nom',          
    'leptonic_W_M_nom',            
    'hadronic_top_pt_nom',         
]

unclustEn_branches = []
unclustEn_branches.extend(JECUnc_nom_branches[1:])


# import from samples*.py
def GetJECVariationDict(nom_branches,suffix):
    out_dict = {}
    for nom_branch in nom_branches:
      out_dict[nom_branch] = nom_branch.replace("nom",suffix)
    return out_dict


nuisances['jesTotal'] = {
    'name': 'CMS_jesTotal',
    'kind': 'branch_custom',
    'type': 'shape',
    'BrFromToUp'  : GetJECVariationDict(JECUnc_nom_branches,"jesTotalUp"),
    'BrFromToDown' : GetJECVariationDict(JECUnc_nom_branches,"jesTotalDown"),
    'samples': dict((skey, ['1.','1.']) for skey in mc),
    'folderUp'   : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_Total'),
    'folderDown' : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_Total'),
}

nuisances['jer'] = {
    'name': 'CMS_jer_2016',
    'kind': 'branch_custom',
    'type': 'shape',
    'BrFromToUp'  : GetJECVariationDict(JECUnc_nom_branches,"jerUp"),
    'BrFromToDown' : GetJECVariationDict(JECUnc_nom_branches,"jerDown"),
    'samples': dict((skey, ['1.','1.']) for skey in mc),
    'folderUp'   : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_Total'),
    'folderDown' : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_Total'),
}

nuisances['unclustEn'] = {
    'name': 'CMS_unclustEn_2016',
    'kind': 'branch_custom',
    'type': 'shape',
    'BrFromToUp'  : GetJECVariationDict(unclustEn_branches,"unclustEnUp"),
    'BrFromToDown' : GetJECVariationDict(unclustEn_branches,"unclustEnDown"),
    'samples': dict((skey, ['1.','1.']) for skey in mc),
    'folderUp'   : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_Total'),
    'folderDown' : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_Total'),
}



samples_ttsyst = {}
for skey in ['TTLJ+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLL']:
    if skey=='TTLL':
        samples_ttsyst[skey] = ['0.','0.']
    else:
        samples_ttsyst[skey] = ['1.','1.']

nuisances['TuneCUETP8M2T4'] = {
    'name': 'CMS_TuneCUETP8M2T4',
    'kind': 'tree',
    'type': 'shape',
    'samples': samples_ttsyst,
    # name_TT*_*[Up|Down] are defined in samples_2016_ttbarCat.py
    'filesUp'   : dict((skey, name_TTLJ_TuneCUETP8M2T4Up if 'TTLJ' in skey else name_TTLL_TuneCUETP8M2T4Up ) for skey in ['TTLJ+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLL']), 
    'filesDown' : dict((skey, name_TTLJ_TuneCUETP8M2T4Down if 'TTLJ' in skey else name_TTLL_TuneCUETP8M2T4Down ) for skey in ['TTLJ+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLL']),

}

nuisances['hdamp'] = {
    'name': 'CMS_hdamp',
    'kind': 'tree',
    'type': 'shape',
    'samples': samples_ttsyst,
    # name_TT*_*[Up|Down] are defined in samples_2016_ttbarCat.py
    'filesUp'   : dict((skey, name_TTLJ_hdampUp if 'TTLJ' in skey else name_TTLL_hdampUp ) for skey in ['TTLJ+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLL']), 
    'filesDown' : dict((skey, name_TTLJ_hdampDown if 'TTLJ' in skey else name_TTLL_hdampDown ) for skey in ['TTLJ+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLL']),

}

nuisances['mtop'] = {
    'name': 'CMS_mtop',
    'kind': 'tree',
    'type': 'shape',
    'samples': samples_ttsyst,
    # name_TT*_*[Up|Down] are defined in samples_2016_ttbarCat.py
    'filesUp'   : dict((skey, name_TTLJ_mtopUp if 'TTLJ' in skey else name_TTLL_mtopUp ) for skey in ['TTLJ+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLL']), 
    'filesDown' : dict((skey, name_TTLJ_mtopDown if 'TTLJ' in skey else name_TTLL_mtopDown ) for skey in ['TTLJ+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLL']),

}

#isr_syst=['PSWeight[2]','PSWeight[0]']
#fsr_syst=['PSWeight[3]','PSWeight[1]']
#
#nuisances['ISR_TT'] = { # 0 PSWeights for tt samples,  4 PSWeights for CHToCB samples
#    'name': 'CMS_ttbar_isr',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, isr_syst) for skey in ttmc ),
#
#}
#nuisances['ISR_EWK'] = {
#    'name': 'CMS_ewk_isr',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, isr_syst) for skey in ['ST','Wjets','DY','WW','WZ','ZZ']),
#
#}
#nuisances['FSR_TT'] = {
#    'name': 'CMS_ttbar_fsr',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, fsr_syst) for skey in ttmc ),
#
#}
#nuisances['FSR_EWK'] = {
#    'name': 'CMS_ewk_fsr',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, fsr_syst) for skey in ['ST','Wjets','DY','WW','WZ','ZZ']),
#
#}



lhe_scale_syst = [ 'LHEScaleWeight[%s]'%i for i in range(9) ]
nuisances['LHEScaleWeight'] = {
    'name': 'CMS_LHEScaleWeight',
    'type': 'shape',
    'kind': 'weight_envelope',
    'samples':dict((skey, lhe_scale_syst) for skey in mc),
        
}

##will add LHEPdfWeight
# ST samples have 102 set of weights, will do later for this
#lhe_pdf_weight_syst = [ 'LHEPdfWeight[%s]'%i for i in range(33) ] #TT samples : 100 replicas, CHToCB samples: 33 replicas
#nuisances['LHEPdfWeight'] = {
#    'name': 'CMS_LHEPdfWeight',
#    'type': 'shape',
#    'kind': 'weight_envelope',
#    'samples':dict((skey, lhe_pdf_weight_syst) for skey in ttmc), #for now, do for ttbar samples
#}


