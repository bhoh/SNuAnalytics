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
mc += ['TT','TT+bb','TT+bj','TT+cc','TT+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLJ+jj','TTLL+bb','TTLL+bj','TTLL+cc','TTLL+jj','Others']
mc += ['TTLJ_jj','TTLJ_cc','TTLJ_bb','TTLJ_bj','TTLL_jj','TTLL_cc','TTLL_bb','TTLL_bj']
mc += ['CHToCB_M080_yield']
#ttmc_syst = ['TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLJ+jj','TTLL+bb','TTLL+bj','TTLL+cc','TTLL+jj']
ttmc_syst = ['TTLJ','TTLJ_jj','TTLJ_cc','TTLJ_bb','TTLJ_bj','TTLL','TTLL_jj','TTLL_cc','TTLL_bb','TTLL_bj']
ttmc_syst += ['TT','TT+bb','TT+bj','TT+cc','TT+jj','TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLJ+jj','TTLL+bb','TTLL+bj','TTLL+cc','TTLL+jj',]
ttmc_syst += ['CHToCB_M080_yield']
ttmc = [ skey for skey in ttmc_syst ]
ttmc += ['CHToCB_M%s'%mass for mass in ['075','080','085','090','100','110','120','130','140','150','160']]
ttbbmc = [ ttmc_ for ttmc_ in ttmc if 'bb' in ttmc_ or 'bj' in ttmc_ ]
ttbbmc += ['CHToCB_M080_yield']
ttccmc = [ ttmc_ for ttmc_ in ttmc if 'cc' in ttmc_ ]
ttccmc += ['CHToCB_M080_yield']
qcdmc = ['QCD_EM','QCD_bcToE','QCD_MU']
qcdmc += ['QCD']

include_mva   = False
regrouped_jec = True if '_final' in opt.pycfg or '_comb' in opt.pycfg else False  #will include regrouped jec in final
QCD_data_driven = True
include_bincl = True if not '_final' in opt.pycfg else False
lnN_eff_ele = False

splitTTLL = False
merge_trig_syst = True
lnN_UE_Tune = True
splitQCDscale_tt = False


## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat'] = {
    'type': 'auto',
    'maxPoiss': '5',
    'includeSignal': '0',
    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': {}
}

nuisances['lumi_uncorr'] = {
    'name': 'lumi_uncorr_2018',
    'type': 'lnN',
    'samples': dict((skey, '1.015') for skey in mc ),
    'group': 'experimental',
}

nuisances['lumi_corr'] = {
    'name': 'lumi_corr',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc ),
    'group': 'experimental',
}

nuisances['lumi_corr_17_18'] = {
    'name': 'lumi_corr_17_18',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc ),
    'group': 'experimental',
}

nuisances['ttXsec'] = {
    'name': 'ttXsec',
    'type': 'lnN',
    #'AsShape' : 1,
    'samples': dict((skey, '1.06114') for skey in ttmc),
    'group': 'theory',
}
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
    'samples': {'TT+bb':'1.0 [0.8,1.8] '},
    'group': 'theory',
}
nuisances['ttbbXsec_param'] = {
    'name': 'ttbbXsec',
    'type': 'param',
    'constraint': '1.0  0.3',
    'samples': {},
    'group': 'theory',
}
#nuisances['ttbjXsec'] = {
#    'name': 'ttbbXsec',
#    'type': 'rateParam',
#    'samples': {'TT+bj':'1.2 [0.8,1.8] '},
#    'group': 'theory',
#}
nuisances['ttccXsec'] = {
    'name': 'ttccXsec',
    'type': 'rateParam',
    'samples': {'TT+cc':'1 [0.8,1.5] '},
    'group': 'theory',
}
nuisances['ttccXsec_param'] = {
    'name': 'ttccXsec',
    'type': 'param',
    'constraint': '1.0  0.3',
    'samples': {},
    'group': 'theory',
}

nuisances['ttjjXsec'] = {
    'name': 'ttjjXsec',
    'type': 'rateParam',
    #'samples': {'TT+jj':'(364.35-@0*1.433-@1*6.782-@2*28.21)/(327.93)    ttbbXsec,ttbjXsec,ttccXsec'},
    'samples': {'TT+jj':'(451.66-@0*(1.7466+8.2659)-@1*33.970)/(407.68)   ttbbXsec,ttccXsec'},
    #'samples': {'TT+jj':'(364.35-@0*(1.433+6.782)-1.*28.21)/(327.93)    ttbbXsec'}, #XXX 364.35 : Xsec of TTLJ, but TT+jj is TTLJ+TTLL. it's wrong. 
    'group': 'theory',
}
if splitTTLL:
  nuisances['ttbbXsec']['samples'] = {'TTLJ+bb':'1 [0.8,1.5] ','TTLL+bb':'1 [0.8,1.5] '}
  nuisances['ttccXsec']['samples'] = {'TTLJ+cc':'1 [0.8,1.5] ','TTLL+cc':'1 [0.8,1.5] '}
  nuisances['ttjjXsec']['samples'] = {'TTLJ+jj':'(364.35-@0*(1.433+6.782)-@1*28.21)/(327.93)    ttbbXsec,ttccXsec','TTLL+jj':'(364.35-@0*(1.433+6.782)-@1*28.21)/(327.93)    ttbbXsec,ttccXsec'}


#nuisances['DYNorm_2018'] = {
#    'name': 'DYNorm_2018',
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
#  hist_source = '%s/src/SNuAnalytics/Configurations/TTSemiLep/patches/ABCD_SF/ABCD_data_driven_SF_2018.root' % os.getenv('CMSSW_BASE')
#  f = ROOT.TFile(hist_source,"READ")
#  h = f.Get(hist_path_dict[syst])
#  Nbins = h.GetNbinsX()
#  for i in range(1,2*Nbins+1): # [1:Nbins+1] : not HEM, [Nbins+1:2*Nbins+1] : HEM
#    name = "ABCD_SF_%s_bins%d_2018"%(syst,int(i))
#    nuisances[name] = {
#        #XXX name change ABCD_SF -> TF
#        'name': name,
#        'type': 'shape',
#        #'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b','sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b','sng_4j_muCH_2b','sng_jbin_muCH_4j_2b','sng_jbin_muCH_5j_2b','sng_jbin_muCH_6j_2b','sng_4j_muCH_3b','sng_jbin_muCH_4j_3b','sng_jbin_muCH_5j_3b','sng_jbin_muCH_6j_3b','sng_jbin_muCH_4b'],
#        'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b','sng_4j_muCH_2b','sng_jbin_muCH_4j_2b','sng_jbin_muCH_5j_2b','sng_jbin_muCH_6j_2b'],
#        'samples': dict((skey, ['1.','1.']) for skey in qcdmc),
#        'group': 'experiment',
#    }

#

if QCD_data_driven:
  #eleORmuCH case only consider "ele" nuisance to avoid double counting
  nuisances['qcd_iso_e_2b'] = {
      'name': 'antiiso_ele',
      #'rename': 'antiiso_ele_2b_2018',
      'type': 'shape',
      'AsLnN': '1',
      #'symmetrize_ttsyst': True,
      'cuts': ['sng_4j_eleORmuCH_2b','sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b'],
      #'AsShape' : 1,
      'samples': dict((skey, ['1.','1.']) for skey in qcdmc),
      'group': 'experimental',
  }
  nuisances['qcd_iso_e_3b'] = {
      'name': 'antiiso_ele',
      #'rename': 'antiiso_ele_3b_2018',
      'type': 'shape',
      'AsLnN': '1',
      #'symmetrize_ttsyst': True,
      'cuts': ['sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b'],
      #'AsShape' : 1,
      'samples': dict((skey, ['1.','1.']) for skey in qcdmc),
      'group': 'experimental',
  }
  nuisances['qcd_iso_m_2b'] = {
      'name': 'antiiso_mu',
      #'rename': 'antiiso_mu_2b_2018',
      'type': 'shape',
      'AsLnN': '1',
      #'symmetrize_ttsyst': True,
      'cuts': ['sng_4j_muCH_2b','sng_jbin_muCH_4j_2b','sng_jbin_muCH_5j_2b','sng_jbin_muCH_6j_2b'], #not include 'sng_4j_eleORmuCH_2b','sng_4j_eleORmuCH_3b', to avoid double counting
      #'AsShape' : 1,
      'samples': dict((skey, ['1.','1.']) for skey in qcdmc),
      'group': 'experimental',
  }
  nuisances['qcd_iso_m_3b'] = {
      'name': 'antiiso_mu',
      #'rename': 'antiiso_mu_3b_2018',
      'type': 'shape',
      'AsLnN': '1',
      #'symmetrize_ttsyst': True,
      'cuts': ['sng_4j_muCH_3b','sng_jbin_muCH_4j_3b','sng_jbin_muCH_5j_3b','sng_jbin_muCH_6j_3b','sng_jbin_muCH_4b'], #not include 'sng_4j_eleORmuCH_2b','sng_4j_eleORmuCH_3b', to avoid double counting
      #'AsShape' : 1,
      'samples': dict((skey, ['1.','1.']) for skey in qcdmc),
      'group': 'experimental',
  }
  #qcd_norm_year_uncorr = False
  #nuisances['qcd_norm_e_2b_2018'] = {
  #    'name': 'qcd_norm_e_2b'+'_2018' if qcd_norm_year_uncorr else '',
  #    'type': 'lnN',
  #    'cuts': ['sng_4j_eleORmuCH_2b','sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b'],
  #    #'AsShape' : 1,
  #    'samples': dict((skey, '1.5') for skey in qcdmc),
  #    'group': 'experimental',
  #}
  #nuisances['qcd_norm_e_3b_2018'] = {
  #    'name': 'qcd_norm_e_3b'+'_2018' if qcd_norm_year_uncorr else '',
  #    'type': 'lnN',
  #    'cuts': ['sng_4j_eleORmuCH_3b','sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b'],
  #    #'AsShape' : 1,
  #    'samples': dict((skey, '1.5') for skey in qcdmc),
  #    'group': 'experimental',
  #}
  #nuisances['qcd_norm_m_2b_2018'] = {
  #    'name': 'qcd_norm_m_2b'+'_2018' if qcd_norm_year_uncorr else '',
  #    'type': 'lnN',
  #    'cuts': ['sng_4j_muCH_2b','sng_jbin_muCH_4j_2b','sng_jbin_muCH_5j_2b','sng_jbin_muCH_6j_2b'],
  #    #'AsShape' : 1,
  #    'samples': dict((skey, '1.5') for skey in qcdmc),
  #    'group': 'experimental',
  #}
  #nuisances['qcd_norm_m_3b_2018'] = {
  #    'name': 'qcd_norm_m_3b'+'_2018' if qcd_norm_year_uncorr else '',
  #    'type': 'lnN',
  #    'cuts': ['sng_4j_muCH_3b','sng_jbin_muCH_4j_3b','sng_jbin_muCH_5j_3b','sng_jbin_muCH_6j_3b','sng_jbin_muCH_4b'],
  #    #'AsShape' : 1,
  #    'samples': dict((skey, '1.5') for skey in qcdmc),
  #    'group': 'experimental',
  #}
  nuisances['qcd_norm'] = {
      'name': 'qcd_norm_2018',
      'type': 'lnN',
      'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b','sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b','sng_4j_muCH_2b','sng_jbin_muCH_4j_2b','sng_jbin_muCH_5j_2b','sng_jbin_muCH_6j_2b','sng_4j_muCH_3b','sng_jbin_muCH_4j_3b','sng_jbin_muCH_5j_3b','sng_jbin_muCH_6j_3b','sng_jbin_muCH_4b'],
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
#old ttH multilepton, data-NLO
Top_pTrw = '( TMath::Sqrt(TMath::Exp(-1.43717e-02 - 1.18358e-04*{TOP_GEN_PT} - 1.70651e-07*{TOP_GEN_PT}*{TOP_GEN_PT} + 4.47969/({TOP_GEN_PT}+28.7)) * TMath::Exp(-1.43717e-02 - 1.18358e-04*{ANTITOP_GEN_PT} - 1.70651e-07*{ANTITOP_GEN_PT}*{ANTITOP_GEN_PT} + 4.47969/({ANTITOP_GEN_PT}+28.7))))'.format(TOP_GEN_PT='((topGenPt>472)*472 + (topGenPt<=472)*topGenPt)', ANTITOP_GEN_PT='((antitopGenPt>472)*472 + (antitopGenPt<=472)*antitopGenPt)')

# TOP PAG NNLO-NLO
#Top_pTrw = 'TMath::Sqrt((0.103*TMath::Exp(-0.0118*{TOP_GEN_PT})-0.000134*{TOP_GEN_PT}+0.973)*(0.103*TMath::Exp(-0.0118*{ANTITOP_GEN_PT})-0.000134*{ANTITOP_GEN_PT}+0.973))'.format(TOP_GEN_PT='topGenPt', ANTITOP_GEN_PT='antitopGenPt')
nuisances['Top_pTreweight'] = {
    'name': 'Top_pTreweight',
    'kind': 'weight',
    'type': 'shape',
    #'symmetrize_ttsyst': True,
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


if merge_trig_syst:
  if not lnN_eff_ele:
    nuisances['eff_ele'] = {
        'name': 'eff_ele',
        #'rename': 'eff_lepton',
        'kind': 'weight',
        'type': 'shape',
        # extrapolation to DY -> ttbar topologies: less than 1%
        'samples': dict((skey, ['1.+TMath::Sqrt((id_ele_up-1)*(id_ele_up-1) + (trig_ele_up-1)*(trig_ele_up-1) + 0.01*0.01)','1.-TMath::Sqrt((1-id_ele_down)*(1-id_ele_down) + (1-trig_ele_down)*(1-trig_ele_down) + 0.01*0.01)']) for skey in mc),
        'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b','sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b','dbl_4j_eeORmmORemORme','dbl_4j','dbl_4j_ee','dbl_4j_em','dbl_4j_me','dbl_4j_ee_onZ',],
        'group': 'experimental',
    }
  else:
    nuisances['eff_ele'] = {
        'name': 'eff_ele',
        #'name': 'eff_lepton',
        'type': 'lnN',
        'samples': dict((skey, '1.02') for skey in mc),
        'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b','sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b','dbl_4j_eeORmmORemORme','dbl_4j','dbl_4j_ee','dbl_4j_em','dbl_4j_me','dbl_4j_ee_onZ',],
        'group': 'experimental',
    }
  nuisances['eff_muon'] = {
      'name': 'eff_muon',
      #'rename': 'eff_lepton',
      'kind': 'weight',
      'type': 'shape',
      # extrapolation to DY -> ttbar topologies: less than 0.5%
      'samples': dict((skey, ['1.+TMath::Sqrt((id_mu_up-1)*(id_mu_up-1) + (trig_mu_up-1)*(trig_mu_up-1) + 0.005*0.005)','1.-TMath::Sqrt((1-id_mu_down)*(1-id_mu_down) + (1-trig_mu_down)*(1-trig_mu_down) + 0.005*0.005)']) for skey in mc),
      'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_muCH_2b','sng_jbin_muCH_4j_2b','sng_jbin_muCH_5j_2b','sng_jbin_muCH_6j_2b','sng_4j_muCH_3b','sng_jbin_muCH_4j_3b','sng_jbin_muCH_5j_3b','sng_jbin_muCH_6j_3b','sng_jbin_muCH_4b','dbl_4j_eeORmmORemORme','dbl_4j','dbl_4j_mm','dbl_4j_em','dbl_4j_me','dbl_4j_mm_onZ',],
      'group': 'experimental',
  }
else:
  nuisances['trig_ele'] = {
      'name': 'eff_trigger_ele_2018',
      'kind': 'weight',
      'type': 'shape',
      'samples': dict((skey, ['trig_ele_up','trig_ele_down']) for skey in mc),
      'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b','sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b','dbl_4j_eeORmmORemORme','dbl_4j','dbl_4j_ee','dbl_4j_em','dbl_4j_me','dbl_4j_ee_onZ',],
      'group': 'experimental',
  }
  
  nuisances['trig_mu'] = {
      'name': 'eff_trigger_mu_2018',
      'kind': 'weight',
      'type': 'shape',
      'samples': dict((skey, ['trig_mu_up','trig_mu_down']) for skey in mc),
      'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_muCH_2b','sng_jbin_muCH_4j_2b','sng_jbin_muCH_5j_2b','sng_jbin_muCH_6j_2b','sng_4j_muCH_3b','sng_jbin_muCH_4j_3b','sng_jbin_muCH_5j_3b','sng_jbin_muCH_6j_3b','sng_jbin_muCH_4b','dbl_4j_eeORmmORemORme','dbl_4j','dbl_4j_mm','dbl_4j_em','dbl_4j_me','dbl_4j_mm_onZ',],
      'group': 'experimental',
  }
  
  if not lnN_eff_ele:
    nuisances['eff_ele'] = {
        'name': 'eff_ele',
        #'rename': 'eff_lepton',
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, ['id_ele_up','id_ele_down']) for skey in mc),
        'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b','sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b','dbl_4j_eeORmmORemORme','dbl_4j','dbl_4j_ee','dbl_4j_em','dbl_4j_me','dbl_4j_ee_onZ',],
        'group': 'experimental',
    }
  else:
    nuisances['eff_ele'] = {
        'name': 'eff_ele',
        #'name': 'eff_lepton',
        'type': 'lnN',
        'samples': dict((skey, '1.02') for skey in mc),
        'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b','sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b','dbl_4j_eeORmmORemORme','dbl_4j','dbl_4j_ee','dbl_4j_em','dbl_4j_me','dbl_4j_ee_onZ',],
        'group': 'experimental',
    }
  #eff_ele_reco_syst  = "((nLooseLep==1)*(Lepton_RecoSF[0]) + (nLooseLep==2)*(Lepton_RecoSF[0]*Alt$(Lepton_RecoSF[1],1)))" #filled 1 for muon
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
  nuisances['eff_muon'] = {
      'name': 'eff_muon',
      #'rename': 'eff_lepton',
      'kind': 'weight',
      'type': 'shape',
      'samples': dict((skey, ['id_mu_up','id_mu_down']) for skey in mc),
      'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_muCH_2b','sng_jbin_muCH_4j_2b','sng_jbin_muCH_5j_2b','sng_jbin_muCH_6j_2b','sng_4j_muCH_3b','sng_jbin_muCH_4j_3b','sng_jbin_muCH_5j_3b','sng_jbin_muCH_6j_3b','sng_jbin_muCH_4b','dbl_4j_eeORmmORemORme','dbl_4j','dbl_4j_mm','dbl_4j_em','dbl_4j_me','dbl_4j_mm_onZ',],
      'group': 'experimental',
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
    'leptonic_top_b_jet_pull_nom', 
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
      syst_ = syst.replace('RPLME_YEAR','2018')
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
          'folderUp'   : makeMCDirectory('_jetMETSyst_{SKIM}'.format(SKIM=skim_)) if not include_mva else makeMCDirectory_mva('_jetMETSyst_{SKIM}__mvaCHToCB_2018_jetMETSyst_{SKIM}'.format(SKIM=skim_))    ,
          'folderDown' : makeMCDirectory('_jetMETSyst_{SKIM}'.format(SKIM=skim_)) if not include_mva else makeMCDirectory_mva('_jetMETSyst_{SKIM}__mvaCHToCB_2018_jetMETSyst_{SKIM}'.format(SKIM=skim_)),
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
      #'((btagSFjesup/btagSF)<9999?(btagSFjesup/btagSF):1)','((btagSFjesdown/btagSF)<9999?(btagSFjesdown/btagSF):1)'
      #'samples': dict((skey, ['((btagSFjesup/btagSF)<9999?(btagSFjesup/btagSF):1)','((btagSFjesdown/btagSF)<9999?(btagSFjesdown/btagSF):1)']) for skey in mc),
      'samples': dict((skey, ['1.','1.']) for skey in mc),
      'folderUp'   : makeMCDirectory('_jetMETSyst_TotalUp')   if not include_mva else makeMCDirectory_mva('_jetMETSyst_TotalUp__mvaCHToCB_2018_jetMETSyst_TotalUp')    ,
      'folderDown' : makeMCDirectory('_jetMETSyst_TotalDown') if not include_mva else makeMCDirectory_mva('_jetMETSyst_TotalDown__mvaCHToCB_2018_jetMETSyst_TotalDown'),
      'FromNormTree': ['Jet_pt_jesTotalUp','Jet_pt_jesTotalDown','btagSFjesup','btagSFjesdown'],
  }
# end of jec variation

nuisances['jer'] = {
    'name': 'jer_2018',
    #'rename': 'jer',
    #'symmetrize_ttsyst': True,
    'kind': 'branch_custom',
    'type': 'shape',
    'BrFromToUp'  : GetJECVariationDict(JECUnc_nom_branches,"jerUp"),
    'BrFromToDown' : GetJECVariationDict(JECUnc_nom_branches,"jerDown"),
    'samples': dict((skey, ['1.','1.']) for skey in mc),
    'folderUp'   : makeMCDirectory('_jetMETSyst_TotalUp')   if not include_mva else  makeMCDirectory_mva('_jetMETSyst_TotalUp__mvaCHToCB_2018_jetMETSyst_TotalUp')    ,
    'folderDown' : makeMCDirectory('_jetMETSyst_TotalDown') if not include_mva else  makeMCDirectory_mva('_jetMETSyst_TotalDown__mvaCHToCB_2018_jetMETSyst_TotalDown'),
    'FromNormTree': ['Jet_pt_jerUp','Jet_pt_jerDown'],
    'group': 'experimental',
}

nuisances['unclustEn'] = {
    'name': 'unclustEn_2018',
    'kind': 'branch_custom',
    'type': 'shape',
    'BrFromToUp'  : GetJECVariationDict(unclustEn_branches,"unclustEnUp"),
    'BrFromToDown' : GetJECVariationDict(unclustEn_branches,"unclustEnDown"),
    'samples': dict((skey, ['1.','1.']) for skey in mc),
    'folderUp'   : makeMCDirectory('_jetMETSyst_TotalUp')    if not include_mva else  makeMCDirectory_mva('_jetMETSyst_TotalUp__mvaCHToCB_2018_jetMETSyst_TotalUp')      ,
    'folderDown' : makeMCDirectory('_jetMETSyst_TotalDown')  if not include_mva else  makeMCDirectory_mva('_jetMETSyst_TotalDown__mvaCHToCB_2018_jetMETSyst_TotalDown')  ,
    'FromNormTree': ['Jet_pt_unclustEnUp','Jet_pt_unclustEnDown'],
    'group': 'experimental',
}

nuisances['HEM'] = {
    'name': 'HEM',
    'kind': 'branch_custom',
    'type': 'shape',
    'OneSided' : True,
    'BrFromToUp'  : GetJECVariationDict(JECUnc_nom_branches,"HEM"),
    #'BrFromToDown' : GetJECVariationDict(JECUnc_nom_branches,"nom"),
    'samples': dict((skey, ['1.','1.']) for skey in mc),
    'folderUp'   : makeMCDirectory('_jetMETSyst_HEM') if not include_mva else makeMCDirectory_mva('_jetMETSyst_HEM__mvaCHToCB_2018_jetMETSyst_HEM'),
    'group': 'experimental',
}

if not 'comb' in opt.pycfg or not lnN_UE_Tune:
  nuisances['TuneCP5'] = {
      'name': 'TuneCP5',
      'kind': 'tree',
      'type': 'shape',
      #'symmetrize_ttsyst': True,
      #'syncronize_stat' : True,
      'samples': dict((skey, ['1.','1.']) for skey in ttmc_syst),
      'folderUp'   : makeMCDirectory('__UEup'),
      'folderDown' : makeMCDirectory('__UEdo'),
      'group': 'theory',
  
  }
else:
  nuisances['TuneCP5'] = {
      'name': 'CMS_TuneCP5',
      'type': 'lnN',
      'samples': dict((skey, '1.015') for skey in ttmc_syst + ['ST','Others']),
      'group': 'theory',
  
  }

if not 'comb' in opt.pycfg:

  nuisances['hdamp'] = {
      'name': 'hdamp',
      'kind': 'tree',
      'type': 'shape',
      #'symmetrize_ttsyst': True,
      #'syncronize_stat' : True,
      'samples': dict((skey, ['1.','1.']) for skey in ttmc_syst ),
      'folderUp'   : makeMCDirectory('__HDAMPup'),
      'folderDown' : makeMCDirectory('__HDAMPdo'),
      'group': 'theory',
  
  }

  hdamp_syst_up   = '(nLepton==1)*((nCleanJet20_2p5<4)+(nCleanJet20_2p5==4)*(1.0208)+(nCleanJet20_2p5==5)*(1.0067)+(nCleanJet20_2p5>=6)*(1.0326)) + (nLepton!=1)*((nCleanJet20_2p5<4)+(nCleanJet20_2p5==4)*(1.0142)+(nCleanJet20_2p5==5)*(1.0438)+(nCleanJet20_2p5>=6)*(1.0921))'
  hdamp_syst_down = '(nLepton==1)*((nCleanJet20_2p5<4)+(nCleanJet20_2p5==4)*(0.9832)+(nCleanJet20_2p5==5)*(0.9918)+(nCleanJet20_2p5>=6)*(0.9622)) + (nLepton!=1)*((nCleanJet20_2p5<4)+(nCleanJet20_2p5==4)*(0.9611)+(nCleanJet20_2p5==5)*(0.9478)+(nCleanJet20_2p5>=6)*(0.9031))'
  nuisances['hdamp_weight'] = {
      'name': 'hdamp_weight',
      'kind': 'weight',
      'type': 'shape',
      #'symmetrize_ttsyst': True,
      #'syncronize_stat' : True,
      'samples': dict((skey, [hdamp_syst_up, hdamp_syst_down]) for skey in ttmc_syst ),
      'group': 'theory',
  }

else:
  nuisances['hdamp_weight'] = {
      'name': 'hdamp_weight',
      'rename': 'hdamp',
      'kind': 'weight',
      'type': 'shape',
      #'symmetrize_ttsyst': True,
      #'syncronize_stat' : True,
      'samples': dict((skey, ['1.','1.']) for skey in ttmc_syst ),
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
    'name': 'eff_puid_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['Jet_PUID_SF_L[1]/Jet_PUID_SF_L[0]','Jet_PUID_SF_L[2]/Jet_PUID_SF_L[0]']) for skey in mc),
    'group': 'experimental',
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

if not 'comb' in opt.pycfg:
  nuisances['ISR_TT'] = {
      'name': 'ttbar_isr',
      'kind': 'weight',
      'type': 'shape',
      'samples': dict((skey, isr_syst) for skey in ttmc ),
      'group': 'theory',
  
  }
else:
  nuisances['ISR_TTjj'] = {
      'name': 'ttbar_isr',
      'rename': 'ttjj_isr',
      'kind': 'weight',
      'type': 'shape',
      'samples': dict((skey, isr_syst) for skey in ttmc if skey not in ttbbmc+ttccmc),
      'group': 'theory',
  
  }
  nuisances['ISR_TTcc'] = {
      'name': 'ttbar_isr',
      'rename': 'ttcc_isr',
      'kind': 'weight',
      'type': 'shape',
      'samples': dict((skey, isr_syst) for skey in ttccmc ),
      'group': 'theory',
  
  }
  nuisances['ISR_TTbb'] = {
      'name': 'ttbar_isr',
      'rename': 'ttbb_isr',
      'kind': 'weight',
      'type': 'shape',
      'samples': dict((skey, isr_syst) for skey in ttbbmc ),
      'group': 'theory',
  
  }
#empty PSWeights for tW
#nuisances['ISR_EWK'] = {
#    'name': 'ewk_isr',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, isr_syst) for skey in ['ST','Wjets','WW','WZ','ZZ']+['Others']),
#
#}
nuisances['FSR_TT'] = {
    'name': 'ttbar_fsr',
    'kind': 'weight',
    'shape': 0.5,
    'type': 'shape',
    'samples': dict((skey, fsr_syst) for skey in ttmc ),
    'group': 'theory',

}
#nuisances['FSR_EWK'] = {
#    'name': 'ewk_fsr',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': dict((skey, fsr_syst) for skey in ['ST','Wjets','WW','WZ','ZZ']+['Others']),
#
#}


#old
#lhe_scale_syst = [ 'LHEScaleWeight[%s]'%i for i in range(9) ]
## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
lhe_scale_syst = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']
lhe_scale_syst_tt_4j5j = lambda skey : [ '((nCleanJet20_2p5==4 || nCleanJet20_2p5==5)*%s+(nCleanJet20_2p5!=4 && nCleanJet20_2p5!=5)*1.)'%weight if 'TTLL' not in skey else '((nCleanJet20_2p5<4)*%s+(nCleanJet20_2p5>=4)*1.)'%weight for weight in lhe_scale_syst ]
lhe_scale_syst_tt_6j = lambda skey : [ '((nCleanJet20_2p5>=6)*%s+(nCleanJet20_2p5<6)*1.)'%weight if 'TTLL' not in skey else '((nCleanJet20_2p5>=4)*%s+(nCleanJet20_2p5<4)*1.)'%weight for weight in lhe_scale_syst ]

lhe_scale_syst_ttlj_4j = ['(nCleanJet20_2p5>=4)*(1.1085)+(nCleanJet20_2p5<4)','(nCleanJet20_2p5>=4)*(0.8883)+(nCleanJet20_2p5<4)']
lhe_scale_syst_ttlj_5j = ['(nCleanJet20_2p5>=5)*(1.0122)+(nCleanJet20_2p5<5)','(nCleanJet20_2p5>=5)*(0.9915)+(nCleanJet20_2p5<5)']
lhe_scale_syst_ttlj_6j = ['(nCleanJet20_2p5>=6)*(1.0244)+(nCleanJet20_2p5<6)','(nCleanJet20_2p5>=6)*(0.9835)+(nCleanJet20_2p5<6)']

lhe_scale_syst_chtocb_4j = ['(nCleanJet20_2p5>=4)*(1.2833)+(nCleanJet20_2p5<4)','(nCleanJet20_2p5>=4)*(0.7931)+(nCleanJet20_2p5<4)']
lhe_scale_syst_chtocb_5j = ['(nCleanJet20_2p5>=5)*(1.0050)+(nCleanJet20_2p5<5)','(nCleanJet20_2p5>=5)*(0.9954)+(nCleanJet20_2p5<5)']
lhe_scale_syst_chtocb_6j = ['(nCleanJet20_2p5>=6)*(1.0043)+(nCleanJet20_2p5<6)','(nCleanJet20_2p5>=6)*(0.9961)+(nCleanJet20_2p5<6)']

lhe_scale_syst_ttll_4j =['(nCleanJet20_2p5>=2)*(1.1085)+(nCleanJet20_2p5<2)','(nCleanJet20_2p5>=2)*(0.8883)+(nCleanJet20_2p5<2)']
lhe_scale_syst_ttll_5j =['(nCleanJet20_2p5>=3)*(1.0122)+(nCleanJet20_2p5<3)','(nCleanJet20_2p5>=3)*(0.9915)+(nCleanJet20_2p5<3)']
lhe_scale_syst_ttll_6j =['(nCleanJet20_2p5>=4)*(1.1531/1.1085/1.0122)+(nCleanJet20_2p5<4)','(nCleanJet20_2p5>=4)*(0.8641/0.8883/0.9915)+(nCleanJet20_2p5<4)']

lhe_scale_syst_tt_4j = lambda skey: lhe_scale_syst_ttlj_4j*('TTLJ' in skey) + lhe_scale_syst_chtocb_4j*('CHToCB' in skey) + lhe_scale_syst_ttll_4j*('TTLL' in skey)
lhe_scale_syst_tt_5j = lambda skey: lhe_scale_syst_ttlj_5j*('TTLJ' in skey) + lhe_scale_syst_chtocb_5j*('CHToCB' in skey) + lhe_scale_syst_ttll_5j*('TTLL' in skey)
lhe_scale_syst_tt_6j = lambda skey: lhe_scale_syst_ttlj_6j*('TTLJ' in skey) + lhe_scale_syst_chtocb_6j*('CHToCB' in skey) + lhe_scale_syst_ttll_6j*('TTLL' in skey)

if not 'comb' in opt.pycfg:
  nuisances['QCDscale_tt'] = {
      'name': 'QCDscale_tt',
      'type': 'shape', 
      'kind': 'weight_envelope',
      'samples':dict((skey, lhe_scale_syst) for skey in ttmc ),
      'group': 'theory',
  }
if not splitQCDscale_tt:
  nuisances['QCDscale_tt'] = {
      'name': 'QCDscale_tt',
      'type': 'shape', 
      'kind': 'weight_envelope',
      'samples':dict((skey, lhe_scale_syst) for skey in ttmc ),
      'group': 'theory',
  }
else:
  nuisances['QCDscale_tt_'] = {
      'name': 'QCDscale_tt',
      'type': 'shape',
      # if kind is not specified, skiped in shape factory
      'samples':dict((skey, lhe_scale_syst) for skey in ttmc if skey not in ttbbmc+ttccmc ),
      'group': 'theory',
  }
  nuisances['QCDscale_ttbb'] = {
      'name': 'QCDscale_tt',
      'rename': 'QCDscale_ttbb',
      'type': 'shape',
      # if kind is not specified, skiped in shape factory
      'samples':dict((skey, lhe_scale_syst) for skey in ttbbmc ),
      'group': 'theory',
  }
  nuisances['QCDscale_ttcc'] = {
      'name': 'QCDscale_tt',
      'rename': 'QCDscale_ttcc',
      'type': 'shape',
      # if kind is not specified, skiped in shape factory
      'samples':dict((skey, lhe_scale_syst) for skey in ttccmc ),
      'group': 'theory',
  }
#nuisances['QCDscale_tt_4j'] = {
#    'name': 'QCDscale_tt_4j',
#    'type': 'shape',
#    'kind': 'weight',
#    'samples':dict((skey, lhe_scale_syst_tt_4j(skey)) for skey in ttmc ),
#    'group': 'theory',
#        
#}
#nuisances['QCDscale_tt_5j'] = {
#    'name': 'QCDscale_tt_5j',
#    'type': 'shape',
#    'kind': 'weight',
#    'samples':dict((skey, lhe_scale_syst_tt_5j(skey)) for skey in ttmc ),
#    'group': 'theory',
#        
#}
#nuisances['QCDscale_tt_6j'] = {
#    'name': 'QCDscale_tt_6j',
#    'type': 'shape',
#    'kind': 'weight',
#    'samples':dict((skey, lhe_scale_syst_tt_6j(skey)) for skey in ttmc ),
#    'group': 'theory',
#        
#}
#
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

lhe_scale_syst_st = ['Alt$(LHEScaleWeight[0],(nCleanJet20_2p5==4)*(1.058898)+(nCleanJet20_2p5==5)*(1.073054)+(nCleanJet20_2p5>=6)*(1.099488)+(nCleanJet20_2p5<4)*1.)', 'Alt$(LHEScaleWeight[1],(nCleanJet20_2p5==4)*(1.058810)+(nCleanJet20_2p5==5)*(1.067547)+(nCleanJet20_2p5>=6)*(1.082491)+(nCleanJet20_2p5<4)*1.)', 'Alt$(LHEScaleWeight[3],(nCleanJet20_2p5==4)*(0.993666)+(nCleanJet20_2p5==5)*(0.997817)+(nCleanJet20_2p5>=6)*(1.007635)+(nCleanJet20_2p5<4)*1.)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-4],(nCleanJet20_2p5==4)*(1.009240)+(nCleanJet20_2p5==5)*(1.005757)+(nCleanJet20_2p5>=6)*(0.996998)+(nCleanJet20_2p5<4)*1.)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-2],(nCleanJet20_2p5==4)*(0.945656)+(nCleanJet20_2p5==5)*(0.939583)+(nCleanJet20_2p5>=6)*(0.929305)+(nCleanJet20_2p5<4)*1.)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-1],(nCleanJet20_2p5==4)*(0.956605)+(nCleanJet20_2p5==5)*(0.947824)+(nCleanJet20_2p5>=6)*(0.930033)+(nCleanJet20_2p5<4)*1.)']

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
##will add LHEPdfWeight
# ST samples have 102 set of weights, will do later for this

lhe_pdf_weight_syst_33    = [ 'LHEPdfWeight[%s]'%i for i in range(33) ]
# if index >= Length(LHEPdfWeight) -> fill nominal pdf (this is vaild on HESSIAN PDF)
lhe_pdf_weight_syst_100 = [ 'LHEPdfWeight[(%s<Length$(LHEPdfWeight))*%s]'%(i,i) for i in range(100) ]
lhe_pdf_weight_syst = lambda skey : lhe_pdf_weight_syst_33 if 'ST' != skey else lhe_pdf_weight_syst_100
nuisances['LHEPdfWeight'] = {
    'name': 'LHEPdfWeight',
    'type': 'shape',
    'kind': 'weight_envelope',
    'samples':dict((skey, lhe_pdf_weight_syst(skey)) for skey in mc if skey not in ['WW','WZ','ZZ']), # ZZ WZ : missng LHEPdf info
    'group': 'theory',
}
