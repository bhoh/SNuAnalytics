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
mc += ['TT','TT+bb','TT+cc','TT+jj','nonTT','QCD']
ttmc_syst = ['TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLJ+jj','TTLL+bb','TTLL+bj','TTLL+cc','TTLL+jj']
ttmc_syst += ['TT','TT+bb','TT+cc','TT+jj']
ttmc = [ skey for skey in ttmc_syst]
ttmc += ['CHToCB_M%s'%mass for mass in ['075','080','085','090','100','110','120','130','140','150']]
qcdmc = ['QCD_EM','QCD_bcToE','QCD_MU']
qcdmc += ['QCD']


## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat'] = {
    'type': 'auto',
    'maxPoiss': '10',
    'includeSignal': '0',
    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': {}
}


nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2018',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc ),
    'group': 'experimental',
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.008') for skey in mc),
    'group': 'experimental',
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc ),
    'group': 'experimental',
}

nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc ),
    'group': 'experimental',
}

nuisances['ttXsec'] = {
    'name': 'ttXsec',
    'type': 'lnN',
    'samples': dict((skey, '1.06114') for skey in ttmc),
    'group': 'theory',
}

ttbbXsec_syst = '1.206/0.793'
nuisances['ttbbXsec'] = {
    'name': 'ttbbXsec',
    'type': 'lnN',
     #'AsShape' : 1,
    'samples': dict((skey, ttbbXsec_syst) for skey in ['TTLJ+bb','TTLL+bb']+['TT','TT+bb']),
    'group': 'theory',
}

nuisances['ttccXsec'] = {
    'name': 'ttccXsec',
    'type': 'lnU',
    #'AsShape' : 1,
    'samples': dict((skey, '1.5') for skey in ['TTLJ+cc','TTLL+cc']+['TT','TT+cc']), #conservatively
    'group': 'theory',
}

nuisances['qcdXsec'] = {
    'name': 'qcdXsec',
    'type': 'lnU',
    #'AsShape' : 1,
    'samples': dict((skey, '2.0') for skey in qcdmc),
    'group': 'theory',
}

Top_pTrw = '( TMath::Sqrt(TMath::Exp(-1.43717e-02 - 1.18358e-04*{TOP_GEN_PT} - 1.70651e-07*{TOP_GEN_PT}*{TOP_GEN_PT} + 4.47969/({TOP_GEN_PT}+28.7)) * TMath::Exp(-1.43717e-02 - 1.18358e-04*{ANTITOP_GEN_PT} - 1.70651e-07*{ANTITOP_GEN_PT}*{ANTITOP_GEN_PT} + 4.47969/({ANTITOP_GEN_PT}+28.7))))'.format(TOP_GEN_PT='((topGenPt>472)*472 + (topGenPt<=472)*topGenPt)', ANTITOP_GEN_PT='((antitopGenPt>472)*472 + (antitopGenPt<=472)*antitopGenPt)')
nuisances['Top_pTreweight'] = {
    'name': 'Top_pTreweight',
    'kind': 'weight',
    'type': 'shape',
    'samples': { key : [Top_pTrw,'1.'] for key in ttmc_syst },
    'group': 'theory',
}


#for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
for shift in ['lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_up, btag_down = '(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift
    btag_syst = ['({var}<9999?{var}:1.)'.format(var=btag_up),'({var}<9999?{var}:1.)'.format(var=btag_down)]

    name = 'btag_%s' % shift
    if 'stats' in shift:
        name += '_2018'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
        'group': 'experimental',
    }



#trig_syst = ['TriggerEffWeight_1l_u/TriggerEffWeight_1l','TriggerEffWeight_1l_d/TriggerEffWeight_1l']
trig_ele_syst = ['((abs(Lepton_pdgId[0])==11)*TriggerEffWeight_1l_u/TriggerEffWeight_1l+(abs(Lepton_pdgId[0])!=11))','((abs(Lepton_pdgId[0])==11)*TriggerEffWeight_1l_d/TriggerEffWeight_1l+(abs(Lepton_pdgId[0])!=11))']
trig_mu_syst = ['((abs(Lepton_pdgId[0])==13)*TriggerEffWeight_1l_u/TriggerEffWeight_1l+(abs(Lepton_pdgId[0])!=13))','((abs(Lepton_pdgId[0])==13)*TriggerEffWeight_1l_d/TriggerEffWeight_1l+(abs(Lepton_pdgId[0])!=13))']
# (abs(Lepton_pdgId[0])==11) electron
# (abs(Lepton_pdgId[0])==13) muon
nuisances['trig_ele'] = {
    'name': 'eff_trigger_ele_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_ele_syst) for skey in mc),
    'group': 'experimental',
}

nuisances['trig_mu'] = {
    'name': 'eff_trigger_mu_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_mu_syst) for skey in mc),
    'group': 'experimental',
}


eff_ele_syst = ['Lepton_tightElectron_'+eleWP+'_TotSF_Up'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]','Lepton_tightElectron_'+eleWP+'_TotSF_Down'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]']
#TODO : decorrelate ele ID, reco
nuisances['eff_ele'] = {
    'name': 'eff_ele_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, eff_ele_syst) for skey in mc),
    'group': 'experimental',
}

'''
nuisances['electronpt'] = {
    'name': 'scale_e_2018',
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
    'name': 'eff_muon_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, eff_muon_syst) for skey in mc),
    'group': 'experimental',
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



syst_uncorr = ['jesAbsolute_RPLME_YEAR','jesBBEC1_RPLME_YEAR','jesEC2_RPLME_YEAR','jesHF_RPLME_YEAR','jesRelativeSample_RPLME_YEAR']
syst_corr = ['jesAbsolute','jesBBEC1','jesEC2','jesFlavorQCD','jesHF','jesRelativeBal']
#syst_uncorr
for syst in syst_uncorr:
    syst_ = syst.replace('RPLME_YEAR','2018')
    nuisances[syst_] = {
        'name': syst_,
        'kind': 'branch_custom',
        'type': 'shape',
        'BrFromToUp'  : GetJECVariationDict(JECUnc_nom_branches, syst_ + "Up"),
        'BrFromToDown' : GetJECVariationDict(JECUnc_nom_branches,syst_ + "Down"),
        'samples': dict((skey, ['1.','1.']) for skey in mc),
        'folderUp'   : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_uncorr'),
        'folderDown' : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_uncorr'),
        'group': 'experimental',
    }

#syst_corr
for syst in syst_corr:
    nuisances[syst] = {
        'name': syst,
        'kind': 'branch_custom',
        'type': 'shape',
        'BrFromToUp'  : GetJECVariationDict(JECUnc_nom_branches, syst + "Up"),
        'BrFromToDown' : GetJECVariationDict(JECUnc_nom_branches,syst + "Down"),
        'samples': dict((skey, ['1.','1.']) for skey in mc),
        'folderUp'   : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_corr'),
        'folderDown' : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_corr'),
        'group': 'experimental',
    }
#nuisances['jesTotal'] = {
#    'name': 'jesTotal',
#    'kind': 'branch_custom',
#    'type': 'shape',
#    'BrFromToUp'  : GetJECVariationDict(JECUnc_nom_branches,"jesTotalUp"),
#    'BrFromToDown' : GetJECVariationDict(JECUnc_nom_branches,"jesTotalDown"),
#    'samples': dict((skey, ['1.','1.']) for skey in mc),
#    'folderUp'   : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_Total'),
#    'folderDown' : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_Total'),
#}

nuisances['jer'] = {
    'name': 'jer_2018',
    'kind': 'branch_custom',
    'type': 'shape',
    'BrFromToUp'  : GetJECVariationDict(JECUnc_nom_branches,"jerUp"),
    'BrFromToDown' : GetJECVariationDict(JECUnc_nom_branches,"jerDown"),
    'samples': dict((skey, ['1.','1.']) for skey in mc),
    'folderUp'   : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_Total'),
    'folderDown' : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_Total'),
    'group': 'experimental',
}

nuisances['unclustEn'] = {
    'name': 'unclustEn_2018',
    'kind': 'branch_custom',
    'type': 'shape',
    'BrFromToUp'  : GetJECVariationDict(unclustEn_branches,"unclustEnUp"),
    'BrFromToDown' : GetJECVariationDict(unclustEn_branches,"unclustEnDown"),
    'samples': dict((skey, ['1.','1.']) for skey in mc),
    'folderUp'   : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_Total'),
    'folderDown' : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_Total'),
    'group': 'experimental',
}

nuisances['TuneCP5'] = {
    'name': 'TuneCP5',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1.','1.']) for skey in ttmc_syst),
    # name_TT*_*[Up|Down] are defined in samples_2018_ttbarCat.py
    'filesUp'   : dict((skey, name_TTLJ_TuneCP5Up if 'TTLJ' in skey else name_TTLL_TuneCP5Up ) for skey in ['TTLJ+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLL+jj','TTLL+bb','TTLL+bj','TTLL+cc']), 
    'filesDown' : dict((skey, name_TTLJ_TuneCP5Down if 'TTLJ' in skey else name_TTLL_TuneCP5Down ) for skey in ['TTLJ+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLL+jj','TTLL+bb','TTLL+bj','TTLL+cc']),
    'group': 'theory',

}

nuisances['hdamp'] = {
    'name': 'hdamp',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1.','1.']) for skey in ttmc_syst),
    # name_TT*_*[Up|Down] are defined in samples_2018_ttbarCat.py
    'filesUp'   : dict((skey, name_TTLJ_hdampUp if 'TTLJ' in skey else name_TTLL_hdampUp ) for skey in ['TTLJ+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLL+jj','TTLL+bb','TTLL+bj','TTLL+cc']), 
    'filesDown' : dict((skey, name_TTLJ_hdampDown if 'TTLJ' in skey else name_TTLL_hdampDown ) for skey in ['TTLJ+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLL+jj','TTLL+bb','TTLL+bj','TTLL+cc']),
    'group': 'theory',

}

nuisances['mtop'] = {
    'name': 'mtop',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1.','1.']) for skey in ttmc_syst),
    # name_TT*_*[Up|Down] are defined in samples_2018_ttbarCat.py
    'filesUp'   : dict((skey, name_TTLJ_mtopUp if 'TTLJ' in skey else name_TTLL_mtopUp ) for skey in ['TTLJ+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLL+jj','TTLL+bb','TTLL+bj','TTLL+cc']), 
    'filesDown' : dict((skey, name_TTLJ_mtopDown if 'TTLJ' in skey else name_TTLL_mtopDown ) for skey in ['TTLJ+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLL+jj','TTLL+bb','TTLL+bj','TTLL+cc']),
    'group': 'theory',

}

'''
nuisances['muonpt'] = {
    'name': 'scale_m_2018',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__MupTup__Semilep2018_whad30__CorrFatJetMass__HMlnjjSelBWR/',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__MupTdo__Semilep2018_whad30__CorrFatJetMass__HMlnjjSelBWR/',
    #'AsLnN': '1'
}

nuisances['jes'] = {
    'name': 'scale_j_2018',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__JESup__Semilep2018_whad30__CorrFatJetMass__HMlnjjSelBWR/',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__JESdo__Semilep2018_whad30__CorrFatJetMass__HMlnjjSelBWR/',
    #'AsLnN': '1'
}


nuisances['fatjes'] = {
    'name': 'scale_fatj_2018',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__Semilep2018_whad30__CorrFatJetMass__FatJetMass_up__HMlnjjSelBWR/',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__Semilep2018_whad30__CorrFatJetMass__FatJetMass_do__HMlnjjSelBWR/',
    #'AsLnN': '1'
}

nuisances['fatjer'] = {
    'name': 'scale_fatjres_2018',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__Semilep2018_whad30__CorrFatJetMass__FatJetMassRes_up__HMlnjjSelBWR/',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__Semilep2018_whad30__CorrFatJetMass__FatJetMassRes_do__HMlnjjSelBWR/',
    #'AsLnN': '1'
}

nuisances['met'] = {
    'name': 'scale_met_2018',
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
    'name': 'PU',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, pu_syst) for skey in mc),
    #'AsLnN': '1',
    'group': 'theory',
}

isr_syst=['PSWeight[2]','PSWeight[0]']
fsr_syst=['PSWeight[3]','PSWeight[1]']

nuisances['ISR_TT'] = {
    'name': 'ttbar_isr',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, isr_syst) for skey in ttmc ),
    'group': 'theory',

}
#nuisances['ISR_EWK'] = {
#    'name': 'ewk_isr',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, isr_syst) for skey in ['ST','Wjets','DY','WW','WZ','ZZ']),
#
#}
nuisances['FSR_TT'] = {
    'name': 'ttbar_fsr',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, fsr_syst) for skey in ttmc ),
    'group': 'theory',

}
#nuisances['FSR_EWK'] = {
#    'name': 'ewk_fsr',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, fsr_syst) for skey in ['ST','Wjets','DY','WW','WZ','ZZ']),
#
#}



lhe_scale_syst = [ 'LHEScaleWeight[%s]'%i for i in range(9) ]
nuisances['LHEScaleWeight'] = {
    'name': 'LHEScaleWeight',
    'type': 'shape',
    'kind': 'weight_envelope',
    'samples':dict((skey, lhe_scale_syst) for skey in ttmc ),
    'group': 'theory',
        
}

##will add LHEPdfWeight
# ST samples have 102 set of weights, will do later for this
lhe_pdf_weight_syst = [ 'LHEPdfWeight[%s]'%i for i in range(33) ]
nuisances['LHEPdfWeight'] = {
    'name': 'LHEPdfWeight',
    'type': 'shape',
    'kind': 'weight_envelope',
    'samples':dict((skey, lhe_pdf_weight_syst) for skey in ttmc), #for now, do for ttbar samples
    'group': 'theory',
}
