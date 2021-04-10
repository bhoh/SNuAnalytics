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
mc += ['TT','TT+bb','TT+bj','TT+cc','TT+jj','Others']
mc += ['TTLJ_jj','TTLJ_cc','TTLJ_bb','TTLJ_bj','TTLL_jj','TTLL_cc','TTLL_bb','TTLL_bj']
#ttmc_syst = ['TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLJ+jj','TTLL+bb','TTLL+bj','TTLL+cc','TTLL+jj']
ttmc_syst = ['TTLJ','TTLJ_jj','TTLJ_cc','TTLJ_bb','TTLJ_bj','TTLL','TTLL_jj','TTLL_cc','TTLL_bb','TTLL_bj']
ttmc_syst += ['TT','TT+bb','TT+bj','TT+cc','TT+jj']
ttmc = [ skey for skey in ttmc_syst ]
ttmc += ['CHToCB_M%s'%mass for mass in ['075','080','085','090','100','110','120','130','140','150','160']]
qcdmc = ['QCD_EM','QCD_bcToE','QCD_MU']
qcdmc += ['QCD']

include_mva = True
regrouped_jec = True if '_final' in opt.pycfg else False  #will include regrouped jec in final

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
#nuisances['qcd_envelop_tt_hf'] = {
#    'name': 'qcd_envelop_tt_hf',
#    'type': 'shape',
#    #'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b','sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b','sng_4j_muCH_2b','sng_jbin_muCH_4j_2b','sng_jbin_muCH_5j_2b','sng_jbin_muCH_6j_2b','sng_4j_muCH_3b','sng_jbin_muCH_4j_3b','sng_jbin_muCH_5j_3b','sng_jbin_muCH_6j_3b','sng_jbin_muCH_4b'],
#    'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b','sng_4j_muCH_3b','sng_jbin_muCH_4j_3b','sng_jbin_muCH_5j_3b','sng_jbin_muCH_6j_3b','sng_jbin_muCH_4b'],
#    #'AsShape' : 1,
#    'samples': dict((skey, ['1.','1.']) for skey in qcdmc),
#    'group': 'experimental',
#}
#nuisances['qcd_envelop_btag'] = {
#    'name': 'qcd_envelop_btag',
#    'type': 'shape',
#    'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b','sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b','sng_4j_muCH_2b','sng_jbin_muCH_4j_2b','sng_jbin_muCH_5j_2b','sng_jbin_muCH_6j_2b','sng_4j_muCH_3b','sng_jbin_muCH_4j_3b','sng_jbin_muCH_5j_3b','sng_jbin_muCH_6j_3b','sng_jbin_muCH_4b'],
#    #'AsShape' : 1,
#    'samples': dict((skey, ['1.','1.']) for skey in qcdmc),
#    'group': 'experimental',
#}



#hist_path_dict = {}
#hist_path_dict['mu_2b']  = 'sng_4j_muCH_2b/MuonEta/histo_TF_data_driven'
#hist_path_dict['mu_3b']  = 'sng_4j_muCH_3b/MuonEta/histo_TF_data_driven'
#hist_path_dict['ele_2b'] = 'sng_4j_eleCH_2b/EleSCEta/histo_TF_data_driven'
#hist_path_dict['ele_3b'] = 'sng_4j_eleCH_3b/EleSCEta/histo_TF_data_driven'
#for syst in ['mu_2b', 'mu_3b','ele_2b','ele_3b']:
#  # i th bin syst
#  hist_source = '%s/src/SNuAnalytics/Configurations/TTSemiLep/patches/ABCD_SF/ABCD_data_driven_SF_2016.root' % os.getenv('CMSSW_BASE')
#  f = ROOT.TFile(hist_source,"READ")
#  h = f.Get(hist_path_dict[syst])
#  Nbins = h.GetNbinsX()
#  for i in range(1,Nbins+1):
#    name = "ABCD_SF_%s_bins%d_2016"%(syst,int(i))
#    nuisances[name] = {
#        'name': name,
#        'type': 'shape',
#        #'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b','sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b','sng_4j_muCH_2b','sng_jbin_muCH_4j_2b','sng_jbin_muCH_5j_2b','sng_jbin_muCH_6j_2b','sng_4j_muCH_3b','sng_jbin_muCH_4j_3b','sng_jbin_muCH_5j_3b','sng_jbin_muCH_6j_3b','sng_jbin_muCH_4b'],
#        'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b','sng_4j_muCH_2b','sng_jbin_muCH_4j_2b','sng_jbin_muCH_5j_2b','sng_jbin_muCH_6j_2b',],
#        'samples': dict((skey, ['1.','1.']) for skey in qcdmc),
#        'group': 'experiment',
#    }

QCD_data_driven = False

if QCD_data_driven:
  nuisances['qcd_iso_e'] = {
      'name': 'iso_e',
      'type': 'shape',
      'cuts': ['sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b','sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b'],
      #'AsShape' : 1,
      'samples': dict((skey, ['1.','1.']) for skey in qcdmc),
      'group': 'experimental',
  }
  nuisances['qcd_iso_m'] = {
      'name': 'iso_m',
      'type': 'shape',
      'cuts': ['sng_4j_muCH_2b','sng_jbin_muCH_4j_2b','sng_jbin_muCH_5j_2b','sng_jbin_muCH_6j_2b','sng_4j_muCH_3b','sng_jbin_muCH_4j_3b','sng_jbin_muCH_5j_3b','sng_jbin_muCH_6j_3b','sng_jbin_muCH_4b'],
      #'AsShape' : 1,
      'samples': dict((skey, ['1.','1.']) for skey in qcdmc),
      'group': 'experimental',
  }
  nuisances['qcd_norm_e_2b_2016'] = {
      'name': 'qcd_norm_e_2b_2016',
      'type': 'lnN',
      'cuts': ['sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b'],
      #'AsShape' : 1,
      'samples': dict((skey, '1.5') for skey in qcdmc),
      'group': 'experimental',
  }
  nuisances['qcd_norm_e_3b_2016'] = {
      'name': 'qcd_norm_e_3b_2016',
      'type': 'lnN',
      'cuts': ['sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b'],
      #'AsShape' : 1,
      'samples': dict((skey, '1.5') for skey in qcdmc),
      'group': 'experimental',
  }
  nuisances['qcd_norm_m_2b_2016'] = {
      'name': 'qcd_norm_m_2b_2016',
      'type': 'lnN',
      'cuts': ['sng_4j_muCH_2b','sng_jbin_muCH_4j_2b','sng_jbin_muCH_5j_2b','sng_jbin_muCH_6j_2b'],
      #'AsShape' : 1,
      'samples': dict((skey, '1.5') for skey in qcdmc),
      'group': 'experimental',
  }
  nuisances['qcd_norm_m_3b_2016'] = {
      'name': 'qcd_norm_m_3b_2016',
      'type': 'lnN',
      'cuts': ['sng_4j_muCH_3b','sng_jbin_muCH_4j_3b','sng_jbin_muCH_5j_3b','sng_jbin_muCH_6j_3b','sng_jbin_muCH_4b'],
      #'AsShape' : 1,
      'samples': dict((skey, '1.5') for skey in qcdmc),
      'group': 'experimental',
  }
else:
  nuisances['qcd_norm'] = {
      'name': 'qcd_norm',
      'type': 'lnN',
      'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b','sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b','sng_4j_muCH_2b','sng_jbin_muCH_4j_2b','sng_jbin_muCH_5j_2b','sng_jbin_muCH_6j_2b','sng_4j_muCH_3b','sng_jbin_muCH_4j_3b','sng_jbin_muCH_5j_3b','sng_jbin_muCH_6j_3b','sng_jbin_muCH_4b'],
      #'AsShape' : 1,
      'samples': dict((skey, '2.0') for skey in qcdmc),
      'group': 'experimental',
  }

nuisances['STNorm'] = {
    'name': 'STNorm',
    'type': 'lnN',
    'AsShape' : 1,
    'samples': dict((skey, '1.1') for skey in ['ST','Others']),
    'group': 'experimental',
}
nuisances['DYNorm'] = {
    'name': 'DYNorm',
    'type': 'lnN',
    'AsShape' : 1,
    'samples': dict((skey, '1.1') for skey in ['DY','Others']),
    'group': 'experimental',
}
nuisances['WjNorm'] = {
    'name': 'WjNorm',
    'type': 'lnN',
    'AsShape' : 1,
    'samples': dict((skey, '1.1') for skey in ['Wjets','Others']),
    'group': 'experimental',
}
nuisances['VVNorm'] = {
    'name': 'VVNorm',
    'type': 'lnN',
    'AsShape' : 1,
    'samples': dict((skey, '1.1') for skey in ['WZ','WW','ZZ','Others']),
    'group': 'experimental',
}
nuisances['TTVNorm'] = {
    'name': 'TTVNorm',
    'type': 'lnN',
    'AsShape' : 1,
    'samples': dict((skey, '1.1') for skey in ['TTWjets','TTZjets','ttH','Others']),
    'group': 'experimental',
}

#nuisances['ttXsec'] = {
#    'name': 'ttXsec',
#    'type': 'lnN',
#    #'AsShape' : 1,
#    'samples': dict((skey, '1.06114') for skey in ttmc),
#    'group': 'theory',
#}
#nuisances['ttbbXsec'] = {
#    'name': 'ttbbXsec',
#    'type': 'lnN',
#    #'AsShape' : 1,
#    'samples': dict((skey, '0.769/1.5') for skey in ['TT+bb','TT+bj']),
#    'group': 'theory',
#}
#nuisances['ttccXsec'] = {
#    'name': 'ttccXsec',
#    'type': 'lnN',
#    #'AsShape' : 1,
#    'samples': dict((skey, '0.769/1.5') for skey in ['TT+cc']),
#    'group': 'theory',
#}
nuisances['ttbbXsec'] = {
    'name': 'ttbbXsec',
    'type': 'rateParam',
    'samples': {'TT+bb':'1.2 [0.8,1.8] '},
    'group': 'theory',
}
#nuisances['ttbjXsec'] = {
#    'name': 'ttbbXsec',
#    'type': 'rateParam',
#    'samples': {'TT+bj':'1.2 [0.8,1.8] '},
#    'group': 'theory',
#}
#nuisances['ttccXsec'] = {
#    'name': 'ttccXsec',
#    'type': 'rateParam',
#    'samples': {'TT+cc':'1 [0.8,1.5] '},
#    'group': 'theory',
#}
nuisances['ttjjXsec'] = {
    'name': 'ttjjXsec',
    'type': 'rateParam',
    #'samples': {'TT+jj':'(364.35-@0*1.433-@1*6.782-@2*28.21)/(327.93)    ttbbXsec,ttbjXsec,ttccXsec'},
    #'samples': {'TT+jj':'(364.35-@0*(1.433+6.782)-@1*28.21)/(327.93)    ttbbXsec,ttccXsec'},
    'samples': {'TT+jj':'(364.35-@0*(1.433+6.782)-1.*28.21)/(327.93)    ttbbXsec'},
    'group': 'theory',
}
#nuisances['DYNorm_2016'] = {
#    'name': 'DYNorm_2016',
#    'type': 'rateParam',
#    'samples': {'DY':'1 '},
#    'cuts' : ['dbl_4j','dbl_4j_ee','dbl_4j_em','dbl_4j_me','dbl_4j_mm','dbl_4j_ee_onZ','dbl_4j_mm_onZ'],
#    'group': 'experimental',
#}
#nuisances['ttjjXsec'] = {
#    'name': 'ttjjXsec',
#    'type': 'lnU',
#     #'AsShape' : 1,
#    'samples': dict((skey, 1.5) for skey in ['TTLJ+jj','TTLL+jj']+['TT','TT+jj']),
#    'group': 'theory',
#}
#ttbbXsec_syst = '1.5'
#nuisances['ttbbXsec'] = {
#    'name': 'ttbbXsec',
#    'type': 'lnU',
#     #'AsShape' : 1,
#    'samples': dict((skey, ttbbXsec_syst) for skey in ['TTLJ+bb','TTLL+bb']+['TT','TT+bb']),
#    'group': 'theory',
#}
#nuisances['ttbjXsec'] = {
#    'name': 'ttbjXsec',
#    'type': 'lnU',
#     #'AsShape' : 1,
#    'samples': dict((skey, 1.5) for skey in ['TTLJ+bj','TTLL+bj']+['TT','TT+bj']),
#    'group': 'theory',
#}
#nuisances['ttccXsec'] = {
#    'name': 'ttccXsec',
#    'type': 'lnU',
#    #'AsShape' : 1,
#    'samples': dict((skey, '1.5') for skey in ['TTLJ+cc','TTLL+cc']+['TT','TT+cc']), #conservatively
#    'group': 'theory',
#}

##old ttH multilepton, data-NLO
Top_pTrw = '(TMath::Sqrt(TMath::Exp(-0.158631 + 2.00214e-04*{TOP_GEN_PT} - 3.09496e-07*{TOP_GEN_PT}*{TOP_GEN_PT} + 34.93/({TOP_GEN_PT}+135.633)) * TMath::Exp(-0.158631 + 2.00214e-04*{ANTITOP_GEN_PT} - 3.09496e-07*{ANTITOP_GEN_PT}*{ANTITOP_GEN_PT} + 34.93/({ANTITOP_GEN_PT}+135.633))))'.format(TOP_GEN_PT='((topGenPt>472)*472 + (topGenPt<=472)*topGenPt)', ANTITOP_GEN_PT='((antitopGenPt>472)*472 + (antitopGenPt<=472)*antitopGenPt)')
#Top_pTrw = 'TMath::Sqrt((0.103*TMath::Exp(-0.0118*{TOP_GEN_PT})-0.000134*{TOP_GEN_PT}+0.973)*(0.103*TMath::Exp(-0.0118*{ANTITOP_GEN_PT})-0.000134*{ANTITOP_GEN_PT}+0.973))'.format(TOP_GEN_PT='topGenPt', ANTITOP_GEN_PT='antitopGenPt')
#M2T4 derived myself
#Top_pTrw2 = 'TMath::Sqrt((1.41*TMath::Exp(-0.00481*{TOP_GEN_PT})-0.0001411*{TOP_GEN_PT}+0.935)*(1.41*TMath::Exp(-0.00481*{ANTITOP_GEN_PT})-0.0001411*{ANTITOP_GEN_PT}+0.935))'.format(TOP_GEN_PT='topGenPt', ANTITOP_GEN_PT='antitopGenPt')

nuisances['Top_pTreweight'] = {
    'name': 'Top_pTreweight',
    'kind': 'weight',
    'type': 'shape',
    #'symmetrize_ttsyst': True,
    'samples': { key : [Top_pTrw,'1.'] for key in ttmc_syst },
    'group': 'theory',
}
#nuisances['Top_pTreweight_M2T4'] = {
#    'name': 'Top_pTreweight_M2T4',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': { key : [Top_pTrw2,'1.'] for key in ttmc_syst },
#    'group': 'theory',
#}
#for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
for shift in ['lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_up, btag_down = '(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift
    btag_syst = ['({var}<9999?{var}:1.)'.format(var=btag_up),'({var}<9999?{var}:1.)'.format(var=btag_down)]


    name = 'btag_%s' % shift
    if 'stats' in shift:
        name += '_2016'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
        'group': 'experimental',
    }


#trig_syst = ['TriggerEffWeight_1l_u/TriggerEffWeight_1l','TriggerEffWeight_1l_d/TriggerEffWeight_1l']
trig_ele_syst    = '((nLooseLep==1)*(eleCH*OTF_SingleEleTrig_SF[0]+muCH) + (nLooseLep==2)*((!mmCH)*Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)+mmCH))'
trig_ele_syst_u  = trig_ele_syst.replace('OTF_SingleEleTrig_SF[0]','OTF_SingleEleTrig_SF[1]').replace('Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)','Alt$(OTF_SingleTrig_DATA_Eff[1]/OTF_SingleTrig_MC_Eff[2],1)')
trig_ele_syst_d  = trig_ele_syst.replace('OTF_SingleEleTrig_SF[0]','OTF_SingleEleTrig_SF[2]').replace('Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)','Alt$(OTF_SingleTrig_DATA_Eff[2]/OTF_SingleTrig_MC_Eff[1],1)')
trig_mu_syst    = '((nLooseLep==1)*(muCH*OTF_SingleMuTrig_SF[0]+eleCH) + (nLooseLep==2)*((!eeCH)*Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)+eeCH))'
trig_mu_syst_u  = trig_mu_syst.replace('OTF_SingleMuTrig_SF[0]','OTF_SingleMuTrig_SF[1]').replace('Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)','Alt$(OTF_SingleTrig_DATA_Eff[3]/OTF_SingleTrig_MC_Eff[4],1)')
trig_mu_syst_d  = trig_mu_syst.replace('OTF_SingleMuTrig_SF[0]','OTF_SingleMuTrig_SF[2]').replace('Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)','Alt$(OTF_SingleTrig_DATA_Eff[4]/OTF_SingleTrig_MC_Eff[3],1)')

trig_ele_syst_list = ['Alt$({UP}/{NOM},1.)'.format(UP=trig_ele_syst_u,NOM=trig_ele_syst),'Alt$({DOWN}/{NOM},1.)'.format(DOWN=trig_ele_syst_d,NOM=trig_ele_syst)]
trig_mu_syst_list  = ['Alt$({UP}/{NOM},1.)'.format(UP=trig_mu_syst_u,NOM=trig_mu_syst),'Alt$({DOWN}/{NOM},1.)'.format(DOWN=trig_mu_syst_d,NOM=trig_mu_syst)]


nuisances['trig_ele'] = {
    'name': 'eff_trigger_ele_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_ele_syst_list) for skey in mc),
    'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b','sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b','dbl_4j_eeORmmORemORme','dbl_4j','dbl_4j_ee','dbl_4j_em','dbl_4j_me','dbl_4j_ee_onZ',],
    'group': 'experimental',
}
nuisances['trig_mu'] = {
    'name': 'eff_trigger_mu_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_mu_syst_list) for skey in mc),
    'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_muCH_2b','sng_jbin_muCH_4j_2b','sng_jbin_muCH_5j_2b','sng_jbin_muCH_6j_2b','sng_4j_muCH_3b','sng_jbin_muCH_4j_3b','sng_jbin_muCH_5j_3b','sng_jbin_muCH_6j_3b','sng_jbin_muCH_4b','dbl_4j_eeORmmORemORme','dbl_4j','dbl_4j_mm','dbl_4j_em','dbl_4j_me','dbl_4j_mm_onZ',],
    'group': 'experimental',
}
nuisances['prefire'] = {
    'name': 'eff_prefiring_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey,['PrefireWeight_Up/PrefireWeight','PrefireWeight_Down/PrefireWeight']) for skey in mc),
    'group': 'experimental',
}


#ver1
eff_ele_syst   = '((nLooseLep==1)*(eleCH*Lepton_tightElectron_{eleWP}_TotSF[0]+muCH) + (nLooseLep==2)*(1))'.format(eleWP=eleWP,muWP=muWP)
#ver2
#eff_ele_syst   = '((nLooseLep==1)*((eleCH)*Lepton_tightElectron_{eleWP}_IdIsoSF[0]+muCH) + (nLooseLep==2)*((!mmCH)*Lepton_tightElectron_{eleWP}_IdIsoSF[0]*Lepton_tightElectron_{eleWP}_IdIsoSF[1]+mmCH))'.format(eleWP=eleWP,muWP=muWP)
eff_ele_syst_u = eff_ele_syst.replace('_TotSF','_TotSF_Up').replace('(nLooseLep==2)*(1)','(nLooseLep==2)*(LepSF2l__ele_{eleWP}__Up)'.format(eleWP=eleWP))
eff_ele_syst_d = eff_ele_syst.replace('_TotSF','_TotSF_Down').replace('(nLooseLep==2)*(1)','(nLooseLep==2)*(LepSF2l__ele_{eleWP}__Do)'.format(eleWP=eleWP))
#eff_ele_syst_u = eff_ele_syst.replace('_IdIsoSF','_IdIsoSF_Up').replace('(nLooseLep==2)*(1)','(nLooseLep==2)*(LepSF2l__ele_{eleWP}__Up*(Lepton_RecoSF[0]*Lepton_RecoSF[1])/(Lepton_RecoSF_Up[0]*Lepton_RecoSF_Up[1]))'.format(eleWP=eleWP))
#eff_ele_syst_d = eff_ele_syst.replace('_IdIsoSF','_IdIsoSF_Down').replace('(nLooseLep==2)*(1)','(nLooseLep==2)*(LepSF2l__ele_{eleWP}__Do*(Lepton_RecoSF[0]*Lepton_RecoSF[1])/(Lepton_RecoSF_Down[0]*Lepton_RecoSF_Down[1]))'.format(eleWP=eleWP))
#ver2
#eff_ele_syst_u = eff_ele_syst.replace('_IdIsoSF','_IdIsoSF_Up')
#eff_ele_syst_d = eff_ele_syst.replace('_IdIsoSF','_IdIsoSF_Down')

eff_ele_syst_list = ['Alt$({UP}/{NOM},1)'.format(UP=eff_ele_syst_u,NOM=eff_ele_syst),'Alt$({DOWN}/{NOM},1)'.format(DOWN=eff_ele_syst_d,NOM=eff_ele_syst)]

nuisances['eff_ele'] = {
    'name': 'eff_ele',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, eff_ele_syst_list) for skey in mc),
    'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b','sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b','dbl_4j_eeORmmORemORme','dbl_4j','dbl_4j_ee','dbl_4j_em','dbl_4j_me','dbl_4j_ee_onZ',],
    'group': 'experimental',
}
#eff_ele_reco_syst  = "((nLooseLep==1)*(Lepton_RecoSF[0]) + (nLooseLep==2)*(Lepton_RecoSF[0]*Alt$(Lepton_RecoSF[1],1)))"
#eff_ele_reco_syst_u = eff_ele_reco_syst.replace('_RecoSF','_RecoSF_Up')
#eff_ele_reco_syst_d = eff_ele_reco_syst.replace('_RecoSF','_RecoSF_Down')
#eff_ele_reco_syst_list = ['{UP}/{NOM}'.format(UP=eff_ele_reco_syst_u,NOM=eff_ele_reco_syst),'{DOWN}/{NOM}'.format(DOWN=eff_ele_reco_syst_d,NOM=eff_ele_reco_syst)]
#nuisances['eff_ele_reco'] = {
#    'name': 'eff_ele_reco',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, eff_ele_reco_syst_list) for skey in mc),
#    'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b','sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b','dbl_4j_eeORmmORemORme','dbl_4j','dbl_4j_ee','dbl_4j_em','dbl_4j_me','dbl_4j_ee_onZ',],
#    'group': 'experimental',
#}
#eff_muon_syst = ['Lepton_tightMuon_'+muWP+'_TotSF_Up'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0]','Lepton_tightMuon_'+muWP+'_TotSF_Down'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0]']
#TODO : decorrelate muon ID, iso
eff_muon_syst   = '((nLooseLep==1)*(muCH*Lepton_tightMuon_{muWP}_TotSF[0]+eleCH) + (nLooseLep==2)*(1))'.format(eleWP=eleWP,muWP=muWP)
eff_muon_syst_u = eff_muon_syst.replace('_TotSF','_TotSF_Up').replace('(nLooseLep==2)*(1)','(nLooseLep==2)*(LepSF2l__mu_{muWP}__Up)'.format(muWP=muWP))
eff_muon_syst_d = eff_muon_syst.replace('_TotSF','_TotSF_Down').replace('(nLooseLep==2)*(1)','(nLooseLep==2)*(LepSF2l__mu_{muWP}__Do)'.format(muWP=muWP))
eff_muon_syst_list = ['Alt$({UP}/{NOM},1.)'.format(UP=eff_muon_syst_u,NOM=eff_muon_syst),'Alt$({DOWN}/{NOM},1.)'.format(DOWN=eff_muon_syst_d,NOM=eff_muon_syst)]

nuisances['eff_muon'] = {
    'name': 'eff_muon',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, eff_muon_syst_list) for skey in mc),
    'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_muCH_2b','sng_jbin_muCH_4j_2b','sng_jbin_muCH_5j_2b','sng_jbin_muCH_6j_2b','sng_4j_muCH_3b','sng_jbin_muCH_4j_3b','sng_jbin_muCH_5j_3b','sng_jbin_muCH_6j_3b','sng_jbin_muCH_4b','dbl_4j_eeORmmORemORme','dbl_4j','dbl_4j_mm','dbl_4j_em','dbl_4j_me','dbl_4j_mm_onZ',],
    'group': 'experimental',
}


pu_syst=['puWeightUp/puWeight','puWeightDown/puWeight']


nuisances['PU'] = {
    'name': 'PU',
    'kind': 'weight',
    'type': 'shape',
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
    'chi2_nom',               
    'status_nom',           
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
if include_mva:
  JECUnc_nom_branches.extend([
    'BDT_High_nom',                            
    'BDT_Low_nom',                            
    'DNN_High_nom',
    'DNN_Low_nom',
    'csv_jet0_mvaCHToCB_nom',
    'csv_jet1_mvaCHToCB_nom',
    'csv_jet2_mvaCHToCB_nom',
    'avg_csv_had_top_nom',
    'second_moment_csv_jet0_mvaCHToCB_nom',
    'second_moment_csv_jet1_mvaCHToCB_nom',
    'second_moment_csv_jet2_mvaCHToCB_nom',
    'dijet_deltaR0_mvaCHToCB_nom',
    'dijet_deltaR1_mvaCHToCB_nom',
    'Hplus_b_deltaR0_mvaCHToCB_nom',
    'Hplus_b_deltaR1_mvaCHToCB_nom',
    'bb_deltaR_mvaCHToCB_nom',
    'min_deltaR_bb_event_mvaCHToCB_nom',
    'HT_btagged_M_nom',
    'HT_not_btagged_M_nom',
  ])

unclustEn_branches = []
unclustEn_branches.extend(JECUnc_nom_branches[1:])


# import from samples*.py
def GetJECVariationDict(nom_branches,suffix):
    out_dict = {}
    for nom_branch in nom_branches:
      out_dict[nom_branch] = nom_branch.replace("nom",suffix)
    return out_dict

# jec variation
if regrouped_jec:

  jes_syst_uncorr = ['jesAbsolute_RPLME_YEAR','jesBBEC1_RPLME_YEAR','jesEC2_RPLME_YEAR','jesHF_RPLME_YEAR','jesRelativeSample_RPLME_YEAR']
  jes_syst_corr = ['jesAbsolute','jesBBEC1','jesEC2','jesFlavorQCD','jesHF','jesRelativeBal']
  jes_syst = jes_syst_uncorr + jes_syst_corr
  #syst_uncorr
  for syst in jes_syst:
      syst_ = syst.replace('RPLME_YEAR','2016')
      skim_ = syst.replace('RPLME_YEAR','uncorr')
      btag_jes_up   = "btagSF{SYST}up".format(SYST=syst_)
      btag_jes_down = "btagSF{SYST}down".format(SYST=syst_)
      BrFromToUp_dict   = GetJECVariationDict(JECUnc_nom_branches, syst_ + "Up")
      BrFromToDown_dict = GetJECVariationDict(JECUnc_nom_branches,syst_ + "Down")
      BrFromToUp_dict.update({'btagSF':btag_jes_up})
      BrFromToDown_dict.update({'btagSF':btag_jes_down})
      nuisances[syst_] = {
          'name': syst_,
          'kind': 'branch_custom',
          'type': 'shape',
          'BrFromToUp'  : BrFromToUp_dict,
          'BrFromToDown' : BrFromToDown_dict,
          #'samples': dict((skey, ['1.','1.']) for skey in mc),
          'samples': dict((skey, ['1.','1.']) for skey in mc),
          'folderUp'   : makeMCDirectory('_jetMETSyst_{SKIM}'.format(SKIM=skim_)) if not include_mva else makeMCDirectory_mva('_jetMETSyst_{SKIM}__mvaCHToCB_2016_jetMETSyst_{SKIM}'.format(SKIM=skim_))    ,
          'folderDown' : makeMCDirectory('_jetMETSyst_{SKIM}'.format(SKIM=skim_)) if not include_mva else makeMCDirectory_mva('_jetMETSyst_{SKIM}__mvaCHToCB_2016_jetMETSyst_{SKIM}'.format(SKIM=skim_)),
          'group': 'experimental',
          'FromNormTree': [btag_jes_up, btag_jes_down],
      }

else:

  BrFromToUp_jesTotal   = GetJECVariationDict(JECUnc_nom_branches,"jesTotalUp")
  BrFromToDown_jesTotal = GetJECVariationDict(JECUnc_nom_branches,"jesTotalDown")
  BrFromToUp_jesTotal.update({'btagSF':'btagSFjesup'})
  BrFromToDown_jesTotal.update({'btagSF':'btagSFjesdown'})
  nuisances['jesTotal'] = {
      'name': 'jesTotal',
      'kind': 'branch_custom',
      'type': 'shape',
      'BrFromToUp'   :BrFromToUp_jesTotal,
      'BrFromToDown' :BrFromToDown_jesTotal,
      #'samples': dict((skey, ['((btagSFjesup/btagSF)<9999?(btagSFjesup/btagSF):1)','((btagSFjesdown/btagSF)<9999?(btagSFjesdown/btagSF):1)']) for skey in mc),
      'samples': dict((skey, ['1.','1.']) for skey in mc),
      'folderUp'   : makeMCDirectory('_jetMETSyst_TotalUp')   if not include_mva else makeMCDirectory_mva('_jetMETSyst_TotalUp__mvaCHToCB_2016_jetMETSyst_TotalUp')    ,
      'folderDown' : makeMCDirectory('_jetMETSyst_TotalDown') if not include_mva else makeMCDirectory_mva('_jetMETSyst_TotalDown__mvaCHToCB_2016_jetMETSyst_TotalDown'),
      'FromNormTree': ['Jet_pt_jesTotalUp','Jet_pt_jesTotalDown','btagSFjesup','btagSFjesdown'],
  }


nuisances['jer'] = {
    'name': 'jer_2016',
    'kind': 'branch_custom',
    'type': 'shape',
    'BrFromToUp'  : GetJECVariationDict(JECUnc_nom_branches,"jerUp"),
    'BrFromToDown' : GetJECVariationDict(JECUnc_nom_branches,"jerDown"),
    'samples': dict((skey, ['1.','1.']) for skey in mc),
    'folderUp'   : makeMCDirectory('_jetMETSyst_TotalUp')   if not include_mva else makeMCDirectory_mva('_jetMETSyst_TotalUp__mvaCHToCB_2016_jetMETSyst_TotalUp')    ,
    'folderDown' : makeMCDirectory('_jetMETSyst_TotalDown') if not include_mva else makeMCDirectory_mva('_jetMETSyst_TotalDown__mvaCHToCB_2016_jetMETSyst_TotalDown'),
    'FromNormTree': ['Jet_pt_jerUp','Jet_pt_jerDown'],
    'group': 'experimental',
}

nuisances['unclustEn'] = {
    'name': 'unclustEn_2016',
    'kind': 'branch_custom',
    'type': 'shape',
    'BrFromToUp'  : GetJECVariationDict(unclustEn_branches,"unclustEnUp"),
    'BrFromToDown' : GetJECVariationDict(unclustEn_branches,"unclustEnDown"),
    'samples': dict((skey, ['1.','1.']) for skey in mc),
    'folderUp'   : makeMCDirectory('_jetMETSyst_TotalUp')   if not include_mva else makeMCDirectory_mva('_jetMETSyst_TotalUp__mvaCHToCB_2016_jetMETSyst_TotalUp')    ,
    'folderDown' : makeMCDirectory('_jetMETSyst_TotalDown') if not include_mva else makeMCDirectory_mva('_jetMETSyst_TotalDown__mvaCHToCB_2016_jetMETSyst_TotalDown'),
    'FromNormTree': ['Jet_pt_unclustEnUp','Jet_pt_unclustEnDown'],
    'group': 'experimental',
}



#samples_ttsyst = {}
#for skey in [ skey_ for skey_ in ttmc if 'CHToCB_M' not in skey_ ]:
#    if skey=='TTLL':
#        samples_ttsyst[skey] = ['0.','0.']
#    else:
#        samples_ttsyst[skey] = ['1.','1.']
#
nuisances['TuneCUETP8M2T4'] = {
    'name': 'TuneCUETP8M2T4',
    'kind': 'tree',
    'type': 'shape',
    #'symmetrize_ttsyst': True,
    'samples': dict((skey, ['1.','1.']) for skey in ttmc_syst),
    'folderUp'   : makeMCDirectory('__UEup'),
    'folderDown' : makeMCDirectory('__UEdo'),
    'group': 'theory',
}

nuisances['hdamp'] = {
    'name': 'hdamp_M2T4',
    'kind': 'tree',
    'type': 'shape',
    #'symmetrize_ttsyst': True,
    'samples': dict((skey, ['1.','1.']) for skey in ttmc_syst ),
    'folderUp'   : makeMCDirectory('__HDAMPup'),
    'folderDown' : makeMCDirectory('__HDAMPdo'),
    'group': 'theory',

}

nuisances['mtop'] = {
    'name': 'mtop',
    'kind': 'tree',
    'type': 'shape',
    #'symmetrize_ttsyst': True,
    'samples': dict((skey, ['0.973','1.028']) for skey in ttmc_syst),
    'folderUp'   : makeMCDirectory('__MTOPup'),
    'folderDown' : makeMCDirectory('__MTOPdo'),
    'group': 'theory',

}

nuisances['PU_ID_L'] = {
    'name': 'eff_puid_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['Jet_PUID_SF_L[1]/Jet_PUID_SF_L[0]','Jet_PUID_SF_L[2]/Jet_PUID_SF_L[0]']) for skey in mc),
    'group': 'experimental',
}

isr_syst=['PSWeight[2]','PSWeight[0]']
fsr_syst=['PSWeight[3]','PSWeight[1]']

nuisances['ISR_TT'] = {
    'name': 'ttbar_isr',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, isr_syst) for skey in ttmc  ),
    'group': 'theory',

}


#empty PSWeights for tW
#nuisances['ISR_EWK'] = {
#    'name': 'ewk_isr',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, isr_syst) for skey in ['ST','Wjets','WW','WZ','ZZ']),
#
#}
nuisances['FSR_TT'] = {
    'name': 'ttbar_fsr',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, fsr_syst) for skey in ttmc ),

}
#nuisances['FSR_EWK'] = {
#    'name': 'ewk_fsr',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, fsr_syst) for skey in ['ST','Wjets','WW','WZ','ZZ']),
#
#}


## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
lhe_scale_syst = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']
lhe_scale_syst_tt_4j5j = lambda skey : [ '((nCleanJet20_2p4==4 || nCleanJet20_2p4==5)*%s+(nCleanJet20_2p4!=4 && nCleanJet20_2p4!=5)*1.)'%weight if 'TTLL' not in skey else '((nCleanJet20_2p4<4)*%s+(nCleanJet20_2p4>=4)*1.)'%weight for weight in lhe_scale_syst ]
lhe_scale_syst_tt_6j = lambda skey : [ '((nCleanJet20_2p4>=6)*%s+(nCleanJet20_2p4<6)*1.)'%weight if 'TTLL' not in skey else '((nCleanJet20_2p4>=4)*%s+(nCleanJet20_2p4<4)*1.)'%weight for weight in lhe_scale_syst ]

nuisances['QCDscale_tt'] = {
    'name': 'QCDscale_tt',
    'type': 'shape',
    'kind': 'weight_envelope',
    'samples':dict((skey, lhe_scale_syst) for skey in ttmc ),
    'group': 'theory',
}

#nuisances['QCDscale_tt_4j5j'] = {
#    'name': 'QCDscale_tt_4j5j',
#    'type': 'shape',
#    'kind': 'weight_envelope',
#    'samples':dict((skey, lhe_scale_syst_tt_4j5j(skey)) for skey in ttmc ),
#    'group': 'theory',
#        
#}
#nuisances['QCDscale_tt_6j'] = {
#    'name': 'QCDscale_tt_6j',
#    'type': 'shape',
#    'kind': 'weight_envelope',
#    'samples':dict((skey, lhe_scale_syst_tt_6j(skey)) for skey in ttmc ),
#    'group': 'theory',
#        
#}

lhe_scale_syst_st_4j_var = ['Alt$(LHEScaleWeight[0],1.058898)', 'Alt$(LHEScaleWeight[1],1.058810)', 'Alt$(LHEScaleWeight[3],0.993666)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-4],1.009240)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-2],0.945656)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-1],0.956605)']
lhe_scale_syst_st_5j_var = ['Alt$(LHEScaleWeight[0],1.073054)', 'Alt$(LHEScaleWeight[1],1.067547)', 'Alt$(LHEScaleWeight[3],0.997817)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-4],1.005757)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-2],0.939583)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-1],0.947824)']
lhe_scale_syst_st_6j_var = ['Alt$(LHEScaleWeight[0],1.099488)', 'Alt$(LHEScaleWeight[1],1.082491)', 'Alt$(LHEScaleWeight[3],1.007635)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-4],0.996998)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-2],0.929305)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-1],0.930033)']


#TMath::Max(0,Length$(LHEScaleWeight)-1), (Length$(LHEScaleWeight)-1 >=0)*(Length$(LHEScaleWeight)-1)
# missing LHEScaleWeight in tW top and tW antitop
lhe_scale_syst_st = ['((nCleanJet20_2p4==4)*(1.058898)+(nCleanJet20_2p4==5)*(1.073054)+(nCleanJet20_2p4>=6)*(1.099488)+(nCleanJet20_2p4<4)*1.)', '((nCleanJet20_2p4==4)*(1.058810)+(nCleanJet20_2p4==5)*(1.067547)+(nCleanJet20_2p4>=6)*(1.082491)+(nCleanJet20_2p4<4)*1.)', '((nCleanJet20_2p4==4)*(0.993666)+(nCleanJet20_2p4==5)*(0.997817)+(nCleanJet20_2p4>=6)*(1.007635)+(nCleanJet20_2p4<4)*1.)', '((nCleanJet20_2p4==4)*(1.009240)+(nCleanJet20_2p4==5)*(1.005757)+(nCleanJet20_2p4>=6)*(0.996998)+(nCleanJet20_2p4<4)*1.)', '((nCleanJet20_2p4==4)*(0.945656)+(nCleanJet20_2p4==5)*(0.939583)+(nCleanJet20_2p4>=6)*(0.929305)+(nCleanJet20_2p4<4)*1.)', '((nCleanJet20_2p4==4)*(0.956605)+(nCleanJet20_2p4==5)*(0.947824)+(nCleanJet20_2p4>=6)*(0.930033)+(nCleanJet20_2p4<4)*1.)']

nuisances['QCDscale_ST'] = {
    'name': 'QCDscale_ST',
    'type': 'shape',
    'kind': 'weight_envelope',
    'samples':dict((skey, lhe_scale_syst_st) for skey in ['ST','Others'] ),
    'group': 'theory',
        
}
nuisances['QCDscale_VJ'] = {
    'name': 'QCDscale_VJ',
    'type': 'shape',
    'kind': 'weight_envelope',
    'samples':dict((skey, lhe_scale_syst) for skey in ['DY','Wjets','Others'] ),
    'group': 'theory',
        
}
# ZZ WZ : missng LHEPdf info
#nuisances['QCDscale_VV'] = {
#    'name': 'QCDscale_VV',
#    'type': 'shape',
#    'kind': 'weight_envelope',
#    'samples':dict((skey, lhe_scale_syst) for skey in ['VV','Others'] ),
#    'group': 'theory',
#        
#}
nuisances['QCDscale_TTX'] = {
    'name': 'QCDscale_TTX',
    'type': 'shape',
    'kind': 'weight_envelope',
    'samples':dict((skey, lhe_scale_syst) for skey in ['TTWjets','TTZjets','ttH','Others'] ),
    'group': 'theory',
        
}
lhe_pdf_weight_syst_33    = [ 'LHEPdfWeight[%s]'%i for i in range(33) ]
lhe_pdf_weight_syst_100 = [ 'LHEPdfWeight[%s]'%i for i in range(100) ]
lhe_pdf_weight_syst = lambda skey : lhe_pdf_weight_syst_33 if 'CHToCB_M' in skey else lhe_pdf_weight_syst_100
nuisances['LHEPdfWeight'] = {
    'name': 'LHEPdfWeight',
    'type': 'shape',
    'kind': 'weight_rms',
    'samples':dict((skey, lhe_pdf_weight_syst(skey)) for skey in mc if skey not in ['WW','WZ','ZZ','ST']), # ZZ WZ ST: missng LHEPdf info
    'lnNsamples': {'ST' : '1.04',
                   }, # assign 4% derived from PDF weight variabtion in 2018
    'group': 'theory',
}

