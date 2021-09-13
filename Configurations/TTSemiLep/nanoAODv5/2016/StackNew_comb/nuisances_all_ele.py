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

def CalcLenBranch(samples,branch):

    passes={}

    for s in samples:
      print "---",s,"---"
      if len(samples[s]['name'])==0:continue
      FirstFile=samples[s]['name'][0].replace("###","")
      print FirstFile
      f=ROOT.TFile.Open(FirstFile)
      tree=f.Get("Events")
      if tree.GetListOfBranches().FindObject(branch):
        print 'Length$("%s")'%branch
        tree.Draw('Length$(%s)'%branch)
        htemp=ROOT.gPad.GetPrimitive("htemp")
        n= int(htemp.GetMean())
        print n
        if not n in passes:
          passes[n]=[]
        passes[n].append(s)
      f.Close()

    return passes


#CalcLenBranch
nMember_sample=CalcLenBranch(samples,'LHEPdfWeight') ## {33:[DY,Wjets...]}
PDF4LHC15_nnlo_30_pdfas={}
NNPDF={}
PDF_ALL={}
for n in nMember_sample:
  if n==33:
    for s in nMember_sample[n]:
      PDF4LHC15_nnlo_30_pdfas[s]=['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(n)]
      #PDF4LHC15_nnlo_30_pdfas
  elif n>=100:
    for s in nMember_sample[n]:
      NNPDF[s]=['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(n)]
PDF_ALL.update(PDF4LHC15_nnlo_30_pdfas)
PDF_ALL.update(NNPDF)
PDF_ALL.update({'TT' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
PDF_ALL.update({'TT+jj' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
PDF_ALL.update({'TT+cc' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
PDF_ALL.update({'TT+bb' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
PDF_ALL.update({'nonTT' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
PDF_ALL.update({'QCD' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })

mc = [skey for skey in samples if skey != 'DATA']
mc += ['TT','TT+bb','TT+cc','TT+jj','nonTT','QCD']
ttmc_syst = ['TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLJ+jj','TTLL+bb','TTLL+bj','TTLL+cc','TTLL+jj']
ttmc_syst += ['TT','TT+bb','TT+cc','TT+jj']
ttmc = [ skey for skey in ttmc_syst ]
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
    'name': 'lumi_13TeV_2016',
    'type': 'lnN',
    'samples': dict((skey, '1.022') for skey in mc ),
    'group': 'experimental',
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.009') for skey in mc),
    'group': 'experimental',
}


nuisances['lumi_BBDefl'] = {
    'name': 'lumi_13TeV_BBDefl',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc ),
    'group': 'experimental',
}

nuisances['lumi_DynBeta'] = {
    'name': 'lumi_13TeV_DynBeta',
    'type': 'lnN',
    'samples': dict((skey, '1.005') for skey in mc ),
    'group': 'experimental',
}

nuisances['lumi_Ghosts'] = {
    'name': 'lumi_13TeV_Ghosts',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc ),
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
Top_pTrw = '(TMath::Sqrt(TMath::Exp(-0.158631 + 2.00214e-04*{TOP_GEN_PT} - 3.09496e-07*{TOP_GEN_PT}*{TOP_GEN_PT} + 34.93/({TOP_GEN_PT}+135.633)) * TMath::Exp(-0.158631 + 2.00214e-04*{ANTITOP_GEN_PT} - 3.09496e-07*{ANTITOP_GEN_PT}*{ANTITOP_GEN_PT} + 34.93/({ANTITOP_GEN_PT}+135.633))))'.format(TOP_GEN_PT='((topGenPt>472)*472 + (topGenPt<=472)*topGenPt)', ANTITOP_GEN_PT='((antitopGenPt>472)*472 + (antitopGenPt<=472)*antitopGenPt)')

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


    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2016'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'skipCMS': 1,
        'samples': dict((skey, btag_syst) for skey in mc),
        'group': 'experimental',
    }



#trig_syst = ['TriggerEffWeight_1l_u/TriggerEffWeight_1l','TriggerEffWeight_1l_d/TriggerEffWeight_1l']
trig_ele_syst = ['((abs(Lepton_pdgId[0])==11)*TriggerEffWeight_1l_u/TriggerEffWeight_1l+(abs(Lepton_pdgId[0])!=11))','((abs(Lepton_pdgId[0])==11)*TriggerEffWeight_1l_d/TriggerEffWeight_1l+(abs(Lepton_pdgId[0])!=11))']
trig_mu_syst = ['((abs(Lepton_pdgId[0])==13)*TriggerEffWeight_1l_u/TriggerEffWeight_1l+(abs(Lepton_pdgId[0])!=13))','((abs(Lepton_pdgId[0])==13)*TriggerEffWeight_1l_d/TriggerEffWeight_1l+(abs(Lepton_pdgId[0])!=13))']


nuisances['trig_ele'] = {
    'name': 'eff_trigger_ele_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_ele_syst) for skey in mc),
    'group': 'experimental',
}
nuisances['trig_mu'] = {
    'name': 'eff_trigger_mu_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_mu_syst) for skey in mc),
    'group': 'experimental',
}
nuisances['prefire'] = {
    'name': 'eff_prefiring_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey,['PrefireWeight_Up/PrefireWeight','PrefireWeight_Down/PrefireWeight']) for skey in mc),
    'group': 'experimental',
}




eff_ele_syst = ['Lepton_tightElectron_'+eleWP+'_TotSF_Up'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]','Lepton_tightElectron_'+eleWP+'_TotSF_Down'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]']
#TODO : decorrelate ele ID, reco
nuisances['eff_ele'] = {
    'name': 'eff_ele_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, eff_ele_syst) for skey in mc),
    'group': 'experimental',
}

eff_muon_syst = ['Lepton_tightMuon_'+muWP+'_TotSF_Up'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0]','Lepton_tightMuon_'+muWP+'_TotSF_Down'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0]']
#TODO : decorrelate muon ID, iso

nuisances['eff_muon'] = {
    'name': 'eff_muon_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, eff_muon_syst) for skey in mc),
    'group': 'experimental',
}


pu_syst=['puWeightUp/puWeight','puWeightDown/puWeight']


nuisances['PU'] = {
    'name': 'CMS_PU',
    'kind': 'weight',
    'type': 'shape',
    'skipCMS': 1,
    'samples': dict((skey, pu_syst) for skey in mc),
    'group': 'theory',
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

syst_uncorr = ['jesAbsolute_RPLME_YEAR','jesBBEC1_RPLME_YEAR','jesEC2_RPLME_YEAR','jesHF_RPLME_YEAR','jesRelativeSample_RPLME_YEAR']
syst_corr = ['jesAbsolute','jesBBEC1','jesEC2','jesFlavorQCD','jesHF','jesRelativeBal']
#syst_uncorr
for syst in syst_uncorr:
    syst_ = syst.replace('RPLME_YEAR','2016')
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
    'name': 'CMS_jer_2016',
    'kind': 'branch_custom',
    'type': 'shape',
    'skipCMS': 1,
    'BrFromToUp'  : GetJECVariationDict(JECUnc_nom_branches,"jerUp"),
    'BrFromToDown' : GetJECVariationDict(JECUnc_nom_branches,"jerDown"),
    'samples': dict((skey, ['1.','1.']) for skey in mc),
    'folderUp'   : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_Total'),
    'folderDown' : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_Total'),
    'group': 'experimental',
}

nuisances['unclustEn'] = {
    'name': 'CMS_unclustEn_2016',
    'kind': 'branch_custom',
    'type': 'shape',
    'skipCMS': 1,
    'BrFromToUp'  : GetJECVariationDict(unclustEn_branches,"unclustEnUp"),
    'BrFromToDown' : GetJECVariationDict(unclustEn_branches,"unclustEnDown"),
    'samples': dict((skey, ['1.','1.']) for skey in mc),
    'folderUp'   : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_Total'),
    'folderDown' : makeMCDirectory('kinFitTTSemiLep_jetMETSyst_Total'),
    'group': 'experimental',
}



samples_ttsyst = {}
for skey in [ skey_ for skey_ in ttmc if 'CHToCB_M' not in skey_ ]:
    if skey=='TTLL':
        samples_ttsyst[skey] = ['0.','0.']
    else:
        samples_ttsyst[skey] = ['1.','1.']

nuisances['TuneCUETP8M2T4'] = {
    'name': 'CMS_TuneCUETP8M2T4',
    'kind': 'tree',
    'type': 'shape',
    'skipCMS': 1,
    'samples': samples_ttsyst,
    # name_TT*_*[Up|Down] are defined in samples_2016_ttbarCat.py
    'filesUp'   : dict((skey, name_TTLJ_TuneCUETP8M2T4Up if 'TTLJ' in skey else name_TTLL_TuneCUETP8M2T4Up ) for skey in ['TTLJ+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLL+jj','TTLL+bb','TTLL+bj','TTLL+cc']), 
    'filesDown' : dict((skey, name_TTLJ_TuneCUETP8M2T4Down if 'TTLJ' in skey else name_TTLL_TuneCUETP8M2T4Down ) for skey in ['TTLJ+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLL+jj','TTLL+bb','TTLL+bj','TTLL+cc']),
    'group': 'theory',

}

nuisances['hdamp'] = {
    'name': 'CMS_hdamp',
    'kind': 'tree',
    'type': 'shape',
    'skipCMS': 1,
    'samples': samples_ttsyst,
    # name_TT*_*[Up|Down] are defined in samples_2016_ttbarCat.py
    'filesUp'   : dict((skey, name_TTLJ_hdampUp if 'TTLJ' in skey else name_TTLL_hdampUp ) for skey in ['TTLJ+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLL+jj','TTLL+bb','TTLL+bj','TTLL+cc']), 
    'filesDown' : dict((skey, name_TTLJ_hdampDown if 'TTLJ' in skey else name_TTLL_hdampDown ) for skey in ['TTLJ+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLL+jj','TTLL+bb','TTLL+bj','TTLL+cc']),
    'group': 'theory',

}

nuisances['mtop'] = {
    'name': 'CMS_mtop',
    'kind': 'tree',
    'type': 'shape',
    'skipCMS': 1,
    'samples': samples_ttsyst,
    # name_TT*_*[Up|Down] are defined in samples_2016_ttbarCat.py
    'filesUp'   : dict((skey, name_TTLJ_mtopUp if 'TTLJ' in skey else name_TTLL_mtopUp ) for skey in ['TTLJ+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLL+jj','TTLL+bb','TTLL+bj','TTLL+cc']), 
    'filesDown' : dict((skey, name_TTLJ_mtopDown if 'TTLJ' in skey else name_TTLL_mtopDown ) for skey in ['TTLJ+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLL+jj','TTLL+bb','TTLL+bj','TTLL+cc']),
    'group': 'theory',

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


## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
lhe_scale_syst = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']
nuisances['LHEScaleWeight'] = {
    'name': 'CMS_LHEScaleWeight',
    'type': 'shape',
    'kind': 'weight_envelope',
    'skipCMS': 1,
    'samples':dict((skey, lhe_scale_syst) for skey in mc if skey not in ['WW','WZ','ZZ','QCD_MU','QCD_EM','QCD_bcToE']+['nonTT','QCD']),
    'group': 'theory',
        
}

#PDF4LHC15_nnlo_30_pdfas
#NNPDF
#PDF_ALL
nuisances['LHEPdfWeight'] = {
    'name': 'CMS_LHEPdfWeight',
    'type': 'shape',
    'kind': 'weight_rms',
    'skipCMS': 1,
    'samples': PDF_ALL,
    'group': 'theory',
}


