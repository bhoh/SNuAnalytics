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




mc = [skey for skey in samples if skey != 'DATA' and 'QCD' not in skey]
mc += ['TT','TT+bb','TT+bj','TT+cc','TT+jj','nonTT']
mc += ['TTLJ_jj','TTLJ_cc','TTLJ_bb','TTLJ_bj','TTLL_jj','TTLL_cc','TTLL_bb','TTLL_bj']
#ttmc_syst = ['TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLJ+jj','TTLL+bb','TTLL+bj','TTLL+cc','TTLL+jj']
ttmc_syst = ['TTLJ','TTLJ_jj','TTLJ_cc','TTLJ_bb','TTLJ_bj','TTLL','TTLL_jj','TTLL_cc','TTLL_bb','TTLL_bj']
ttmc_syst += ['TT','TT+bb','TT+bj','TT+cc','TT+jj']
ttmc = [ skey for skey in ttmc_syst ]
ttmc += ['CHToCB_M%s'%mass for mass in ['075','080','085','090','100','110','120','130','140','150','160']]
qcdmc = ['QCD_EM','QCD_bcToE','QCD_MU']
qcdmc += ['QCD']


## Use the following if you want to apply the automatic combine MC stat nuisances.
#nuisances['stat'] = {
#    'type': 'auto',
#    'maxPoiss': '10',
#    'includeSignal': '0',
#    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
#    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
#    'samples': {}
#}
#
#
#nuisances['lumi_Uncorrelated'] = {
#        'name': 'lumi_13TeV_2017',
#        'type': 'lnN',
#        'samples': dict((skey, '1.02') for skey in mc ),
#    'group': 'experimental',
#}
#
#nuisances['lumi_XYFact'] = {
#        'name': 'lumi_13TeV_XYFact',
#        'type': 'lnN',
#        'samples': dict((skey, '1.008') for skey in mc),
#    'group': 'experimental',
#}
#
#nuisances['lumi_LScale'] = {
#        'name': 'lumi_13TeV_LSCale',
#        'type': 'lnN',
#        'samples': dict((skey, '1.003') for skey in mc ),
#    'group': 'experimental',
#}
#
#nuisances['lumi_BBDefl'] = {
#        'name': 'lumi_13TeV_BBDefl',
#        'type': 'lnN',
#        'samples': dict((skey, '1.004') for skey in mc ),
#    'group': 'experimental',
#}
#
#nuisances['lumi_DynBeta'] = {
#        'name': 'lumi_13TeV_DynBeta',
#        'type': 'lnN',
#        'samples': dict((skey, '1.005') for skey in mc ),
#    'group': 'experimental',
#}
#
#nuisances['lumi_CurrCalib'] = {
#        'name': 'lumi_13TeV_CurrCalib',
#        'type': 'lnN',
#        'samples': dict((skey, '1.003') for skey in mc ),
#    'group': 'experimental',
#}
#
#nuisances['lumi_Ghosts'] = {
#        'name': 'lumi_13TeV_Ghosts',
#        'type': 'lnN',
#        'samples': dict((skey, '1.001') for skey in mc ),
#    'group': 'experimental',
#}
#
#nuisances['ttXsec'] = {
#    'name': 'ttXsec',
#    'type': 'lnN',
#    'samples': dict((skey, '1.06114') for skey in ttmc),
#    'group': 'theory',
#}
#nuisances['ttbbXsec'] = {
#    'name': 'ttbbXsec',
#    'type': 'rateParam',
#    'samples': {'TT+bb':'1 [0.66,1.5]'},
#    'group': 'theory',
#}
#nuisances['ttbjXsec'] = {
#    'name': 'ttbbXsec',
#    'type': 'rateParam',
#    'samples': {'TT+bj':'1 [0.66,1.5]'},
#    'group': 'theory',
#}
#nuisances['ttccXsec'] = {
#    'name': 'ttccXsec',
#    'type': 'rateParam',
#    'samples': {'TT+cc':'1 [0.66,1.5]'},
#    'group': 'theory',
#}
#nuisances['ttjjXsec'] = {
#    'name': 'ttjjXsec',
#    'type': 'rateParam',
#    #'samples': {'TT+jj':'(364.35-@0*1.433-@1*6.782-@2*28.21)/(327.93)    ttbbXsec,ttbjXsec,ttccXsec'},
#    'samples': {'TT+jj':'(364.35-@0*(1.433+6.782)-@1*28.21)/(327.93)    ttbbXsec,ttccXsec'},
#    'group': 'theory',
#}
##nuisances['ttjjXsec'] = {
##    'name': 'ttjjXsec',
##    'type': 'lnU',
##     #'AsShape' : 1,
##    'samples': dict((skey, 1.5) for skey in ['TTLJ+jj','TTLL+jj']+['TT','TT+jj']),
##    'group': 'theory',
##}
##ttbbXsec_syst = '1.5'
##nuisances['ttbbXsec'] = {
##    'name': 'ttbbXsec',
##    'type': 'lnU',
##     #'AsShape' : 1,
##    'samples': dict((skey, ttbbXsec_syst) for skey in ['TTLJ+bb','TTLL+bb']+['TT','TT+bb']),
##    'group': 'theory',
##}
##nuisances['ttbjXsec'] = {
##    'name': 'ttbjXsec',
##    'type': 'lnU',
##     #'AsShape' : 1,
##    'samples': dict((skey, 1.5) for skey in ['TTLJ+bj','TTLL+bj']+['TT','TT+bj']),
##    'group': 'theory',
##}
##nuisances['ttccXsec'] = {
##    'name': 'ttccXsec',
##    'type': 'lnU',
##    #'AsShape' : 1,
##    'samples': dict((skey, '1.5') for skey in ['TTLJ+cc','TTLL+cc']+['TT','TT+cc']), #conservatively
##    'group': 'theory',
##}
#
#
#nuisances['qcdXsec'] = {
#    'name': 'qcdXsec',
#    'type': 'lnU',
#    #'AsShape' : 1,
#    'samples': dict((skey, '2.0') for skey in qcdmc),
#    'group': 'theory',
#}
#
#Top_pTrw = '( TMath::Sqrt(TMath::Exp(-1.43717e-02 - 1.18358e-04*{TOP_GEN_PT} - 1.70651e-07*{TOP_GEN_PT}*{TOP_GEN_PT} + 4.47969/({TOP_GEN_PT}+28.7)) * TMath::Exp(-1.43717e-02 - 1.18358e-04*{ANTITOP_GEN_PT} - 1.70651e-07*{ANTITOP_GEN_PT}*{ANTITOP_GEN_PT} + 4.47969/({ANTITOP_GEN_PT}+28.7))))'.format(TOP_GEN_PT='((topGenPt>472)*472 + (topGenPt<=472)*topGenPt)', ANTITOP_GEN_PT='((antitopGenPt>472)*472 + (antitopGenPt<=472)*antitopGenPt)')
#nuisances['Top_pTreweight'] = {
#    'name': 'Top_pTreweight',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': { key : [Top_pTrw,'1.'] for key in ttmc_syst },
#    'group': 'theory',
#}

#for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
for shift in ['lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_up, btag_down = '(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift
    btag_syst = ['({var}<9999?{var}:1.)'.format(var=btag_up),'({var}<9999?{var}:1.)'.format(var=btag_down)]

    name = 'btag_%s' % shift
    if 'stats' in shift:
        name += '_2017'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
    'group': 'experimental',
    }


##trig_syst = ['TriggerEffWeight_1l_u/TriggerEffWeight_1l','TriggerEffWeight_1l_d/TriggerEffWeight_1l']
#trig_ele_syst    = '((nLooseLep==1)*(eleCH*OTF_SingleEleTrig_SF[0]+muCH) + (nLooseLep==2)*((!mmCH)*Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)+mmCH))'
#trig_ele_syst_u  = trig_ele_syst.replace('OTF_SingleEleTrig_SF[0]','OTF_SingleEleTrig_SF[1]').replace('Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)','Alt$(OTF_SingleTrig_DATA_Eff[1]/OTF_SingleTrig_MC_Eff[1],1)')
#trig_ele_syst_d  = trig_ele_syst.replace('OTF_SingleEleTrig_SF[0]','OTF_SingleEleTrig_SF[2]').replace('Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)','Alt$(OTF_SingleTrig_DATA_Eff[2]/OTF_SingleTrig_MC_Eff[2],1)')
#trig_mu_syst    = '((nLooseLep==1)*(muCH*OTF_SingleMuTrig_SF[0]+eleCH) + (nLooseLep==2)*((!eeCH)*Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)+eeCH))'
#trig_mu_syst_u  = trig_mu_syst.replace('OTF_SingleMuTrig_SF[0]','OTF_SingleMuTrig_SF[1]').replace('Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)','Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[3],1)')
#trig_mu_syst_d  = trig_mu_syst.replace('OTF_SingleMuTrig_SF[0]','OTF_SingleMuTrig_SF[2]').replace('Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)','Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[4],1)')
#
#trig_ele_syst_list = ['Alt$({UP}/{NOM},1.)'.format(UP=trig_ele_syst_u,NOM=trig_ele_syst),'Alt$({DOWN}/{NOM},1.)'.format(DOWN=trig_ele_syst_d,NOM=trig_ele_syst)]
#trig_mu_syst_list  = ['Alt$({UP}/{NOM},1.)'.format(UP=trig_mu_syst_u,NOM=trig_mu_syst),'Alt$({DOWN}/{NOM},1.)'.format(DOWN=trig_mu_syst_d,NOM=trig_mu_syst)]
#
#
#nuisances['trig_ele'] = {
#    'name': 'eff_trigger_ele_2017',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, trig_ele_syst_list) for skey in mc),
#    'group': 'experimental',
#}
#nuisances['trig_mu'] = {
#    'name': 'eff_trigger_mu_2017',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, trig_mu_syst_list) for skey in mc),
#    'group': 'experimental',
#}
#
#nuisances['prefire'] = {
#    'name': 'eff_prefiring_2017',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey,['PrefireWeight_Up/PrefireWeight','PrefireWeight_Down/PrefireWeight']) for skey in mc),
#    'group': 'experimental',
#}
#
##eff_ele_syst = ['Lepton_tightElectron_'+eleWP+'_TotSF_Up'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]','Lepton_tightElectron_'+eleWP+'_TotSF_Down'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]']
#
#eff_ele_syst   = '((nLooseLep==1)*(eleCH*Lepton_tightElectron_{eleWP}_TotSF[0]+muCH) + (nLooseLep==2)*(1))'.format(eleWP=eleWP,muWP=muWP)
#eff_ele_syst_u = eff_ele_syst.replace('_TotSF','_TotSF_Up').replace('(nLooseLep==2)*(1)','(nLooseLep==2)*(LepSF2l__ele_{eleWP}__Up)'.format(eleWP=eleWP))
#eff_ele_syst_d = eff_ele_syst.replace('_TotSF','_TotSF_Down').replace('(nLooseLep==2)*(1)','(nLooseLep==2)*(LepSF2l__ele_{eleWP}__Do)'.format(eleWP=eleWP))
#eff_ele_syst_list = ['Alt$({UP}/{NOM},1.)'.format(UP=eff_ele_syst_u,NOM=eff_ele_syst),'Alt$({DOWN}/{NOM},1.)'.format(DOWN=eff_ele_syst_d,NOM=eff_ele_syst)]
#
##TODO : decorrelate ele ID, reco
#nuisances['eff_ele'] = {
#    'name': 'eff_ele',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, eff_ele_syst_list) for skey in mc),
#    'group': 'experimental',
#}
#
##eff_muon_syst = ['Lepton_tightMuon_'+muWP+'_TotSF_Up'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0]','Lepton_tightMuon_'+muWP+'_TotSF_Down'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0]']
##TODO : decorrelate muon ID, iso
##eff_muon_syst = ['Lepton_tightMuon_'+muWP+'_TotSF_Up'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0]','Lepton_tightMuon_'+muWP+'_TotSF_Down'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0]']
#eff_muon_syst   = '((nLooseLep==1)*(muCH*Lepton_tightMuon_{muWP}_TotSF[0]+eleCH) + (nLooseLep==2)*(1))'.format(eleWP=eleWP,muWP=muWP)
#eff_muon_syst_u = eff_muon_syst.replace('_TotSF','_TotSF_Up').replace('(nLooseLep==2)*(1)','(nLooseLep==2)*(LepSF2l__mu_{muWP}__Up)'.format(muWP=muWP))
#eff_muon_syst_d = eff_muon_syst.replace('_TotSF','_TotSF_Down').replace('(nLooseLep==2)*(1)','(nLooseLep==2)*(LepSF2l__mu_{muWP}__Do)'.format(muWP=muWP))
##TODO : decorrelate muon ID, iso
#eff_muon_syst_list = ['Alt$({UP}/{NOM},1.)'.format(UP=eff_muon_syst_u,NOM=eff_muon_syst),'Alt$({DOWN}/{NOM},1.)'.format(DOWN=eff_muon_syst_d,NOM=eff_muon_syst)]
#
#nuisances['eff_muon'] = {
#    'name': 'eff_muon',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, eff_muon_syst_list) for skey in mc),
#    'group': 'experimental',
#}
#
#pu_syst=['puWeightUp/puWeight','puWeightDown/puWeight']
#
#
#nuisances['PU'] = {
#    'name': 'PU',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, pu_syst) for skey in mc),
#    #'AsLnN': '1',
#    'group': 'theory',
#}
#
#
#
#
#
#JECUnc_nom_branches = [
#    'Jet_pt_nom',
#    'MET_CHToCB_pt_nom',
#    'initial_dijet_M_nom',         
#    'initial_dijet_M_high_nom',    
#    'fitted_dijet_M_nom',          
#    'fitted_dijet_M_high_nom',     
#    'chi2_nom',               
#    'status_nom',           
#    'down_type_jet_b_tagged_nom',  
#    'hadronic_top_b_jet_idx_nom',  
#    'leptonic_top_b_jet_idx_nom',  
#    'w_ch_up_type_jet_idx_nom',    
#    'w_ch_down_type_jet_idx_nom',  
#    'hadronic_top_b_jet_pull_nom', 
#    'w_ch_up_type_jet_pull_nom',   
#    'w_ch_down_type_jet_pull_nom', 
#    'hadronic_top_M_nom',          
#    'leptonic_top_M_nom',          
#    'leptonic_W_M_nom',            
#    'hadronic_top_pt_nom',         
#]
#
#unclustEn_branches = []
#unclustEn_branches.extend(JECUnc_nom_branches[1:])
#
#
## import from samples*.py
#def GetJECVariationDict(nom_branches,suffix):
#    out_dict = {}
#    for nom_branch in nom_branches:
#      out_dict[nom_branch] = nom_branch.replace("nom",suffix)
#    return out_dict
#
#
#
##syst_uncorr = ['jesAbsolute_RPLME_YEAR','jesBBEC1_RPLME_YEAR','jesEC2_RPLME_YEAR','jesHF_RPLME_YEAR','jesRelativeSample_RPLME_YEAR']
##syst_corr = ['jesAbsolute','jesBBEC1','jesEC2','jesFlavorQCD','jesHF','jesRelativeBal']
###syst_uncorr
##for syst in syst_uncorr:
##    syst_ = syst.replace('RPLME_YEAR','2017')
##    nuisances[syst_] = {
##        'name': syst_,
##        'kind': 'branch_custom',
##        'type': 'shape',
##        'BrFromToUp'  : GetJECVariationDict(JECUnc_nom_branches, syst_ + "Up"),
##        'BrFromToDown' : GetJECVariationDict(JECUnc_nom_branches,syst_ + "Down"),
##        'samples': dict((skey, ['1.','1.']) for skey in mc),
##        'folderUp'   : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_uncorr'),
##        'folderDown' : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_uncorr'),
##    'group': 'experimental',
##    }
##
###syst_corr
##for syst in syst_corr:
##    nuisances[syst] = {
##        'name': syst,
##        'kind': 'branch_custom',
##        'type': 'shape',
##        'BrFromToUp'  : GetJECVariationDict(JECUnc_nom_branches, syst + "Up"),
##        'BrFromToDown' : GetJECVariationDict(JECUnc_nom_branches,syst + "Down"),
##        'samples': dict((skey, ['1.','1.']) for skey in mc),
##        'folderUp'   : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_corr'),
##        'folderDown' : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_corr'),
##    'group': 'experimental',
##    }
#nuisances['jesTotal'] = {
#    'name': 'jesTotal',
#    'kind': 'branch_custom',
#    'type': 'shape',
#    'BrFromToUp'  : GetJECVariationDict(JECUnc_nom_branches,"jesTotalUp"),
#    'BrFromToDown' : GetJECVariationDict(JECUnc_nom_branches,"jesTotalDown"),
#    'samples': dict((skey, ['1.','1.']) for skey in mc),
#    'folderUp'   : makeMCDirectory('_jetMETSyst_TotalUp'),
#    'folderDown' : makeMCDirectory('_jetMETSyst_TotalDown'),
#    'FromNormTree': ['Jet_pt_jesTotalUp','Jet_pt_jesTotalDown'],
#}
#
#nuisances['jer'] = {
#    'name': 'jer_2017',
#    'kind': 'branch_custom',
#    'type': 'shape',
#    'BrFromToUp'  : GetJECVariationDict(JECUnc_nom_branches,"jerUp"),
#    'BrFromToDown' : GetJECVariationDict(JECUnc_nom_branches,"jerDown"),
#    'samples': dict((skey, ['1.','1.']) for skey in mc),
#    'folderUp'   : makeMCDirectory('_jetMETSyst_TotalUp'),
#    'folderDown' : makeMCDirectory('_jetMETSyst_TotalDown'),
#    'FromNormTree': ['Jet_pt_jerUp','Jet_pt_jerDown'],
#    'group': 'experimental',
#}
#
#nuisances['unclustEn'] = {
#    'name': 'unclustEn_2017',
#    'kind': 'branch_custom',
#    'type': 'shape',
#    'BrFromToUp'  : GetJECVariationDict(unclustEn_branches,"unclustEnUp"),
#    'BrFromToDown' : GetJECVariationDict(unclustEn_branches,"unclustEnDown"),
#    'samples': dict((skey, ['1.','1.']) for skey in mc),
#    'folderUp'   : makeMCDirectory('_jetMETSyst_TotalUp'),
#    'folderDown' : makeMCDirectory('_jetMETSyst_TotalDown'),
#    'FromNormTree': ['Jet_pt_unclustEnUp','Jet_pt_unclustEnDown'],
#    'group': 'experimental',
#}
#
#nuisances['TuneCP5'] = {
#    'name': 'TuneCP5',
#    'kind': 'tree',
#    'type': 'shape',
#    'samples': dict((skey, ['1.','1.']) for skey in ttmc_syst),
#    # name_TT*_*[Up|Down] are defined in samples_2017_ttbarCat.py
#    'folderUp'   : makeMCDirectory('__UEup'),
#    'folderDown' : makeMCDirectory('__UEdo'),
#    'group': 'theory',
#
#}
#
#nuisances['hdamp'] = {
#    'name': 'hdamp',
#    'kind': 'tree',
#    'type': 'shape',
#    'samples': dict((skey, ['1.','1.']) for skey in ttmc_syst),
#    # name_TT*_*[Up|Down] are defined in samples_2017_ttbarCat.py
#    'folderUp'   : makeMCDirectory('__HDAMPup'),
#    'folderDown' : makeMCDirectory('__HDAMPdo'),
#    'group': 'theory',
#
#}
#
#nuisances['mtop'] = {
#    'name': 'mtop',
#    'kind': 'tree',
#    'type': 'shape',
#    'samples': dict((skey, ['0.973','1.028']) for skey in ttmc_syst),
#    # name_TT*_*[Up|Down] are defined in samples_2017_ttbarCat.py
#    'folderUp'   : makeMCDirectory('__MTOPup'),
#    'folderDown' : makeMCDirectory('__MTOPdo'),
#    'group': 'theory',
#
#}
#
#nuisances['PU_ID_L'] = {
#    'name': 'eff_puid_2017',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, ['Jet_PUIDSF_loose_up/Jet_PUIDSF_loose','Jet_PUIDSF_loose_down/Jet_PUIDSF_loose']) for skey in mc),
#    'group': 'experimental',
#}
#
#
#isr_syst=['PSWeight[2]','PSWeight[0]']
#fsr_syst=['PSWeight[3]','PSWeight[1]']
#
#nuisances['ISR_TT'] = {
#    'name': 'ttbar_isr',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, isr_syst) for skey in ttmc ),
#    'group': 'theory',
#
#}
#nuisances['ISR_EWK'] = {
#    'name': 'ewk_isr',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, isr_syst) for skey in ['ST','Wjets','DY','WW','WZ','ZZ']+['nonTT']),
#    'group': 'theory',
#
#}
#nuisances['FSR_TT'] = {
#    'name': 'ttbar_fsr',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, fsr_syst) for skey in ttmc ),
#    'group': 'theory',
#
#}
#nuisances['FSR_EWK'] = {
#    'name': 'ewk_fsr',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, fsr_syst) for skey in ['ST','Wjets','DY','WW','WZ','ZZ']+['nonTT']),
#    'group': 'theory',
#
#}
#
#
#
#lhe_scale_syst = [ 'LHEScaleWeight[%s]'%i for i in range(9) ]
#nuisances['LHEScaleWeight'] = {
#    'name': 'LHEScaleWeight',
#    'type': 'shape',
#    'kind': 'weight_envelope',
#    'samples':dict((skey, lhe_scale_syst) for skey in mc if skey not in ['WW','WZ','ZZ','QCD_MU','QCD_EM','QCD_bcToE']+['nonTT','QCD']),
#    'group': 'theory',
#        
#}
#
###will add LHEPdfWeight
## ST samples have 102 set of weights, will do later for this
#lhe_pdf_weight_syst = [ 'LHEPdfWeight[%s]'%i for i in range(33) ]
#nuisances['LHEPdfWeight'] = {
#    'name': 'LHEPdfWeight',
#    'type': 'shape',
#    'kind': 'weight_envelope',
#    'samples':dict((skey, lhe_pdf_weight_syst) for skey in ttmc), #for now, do for ttbar samples
#    'group': 'theory',
#}


