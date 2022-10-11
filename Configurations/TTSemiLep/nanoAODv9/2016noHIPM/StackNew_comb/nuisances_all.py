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

include_mva = True
regrouped_jec = True if '_final' in opt.pycfg or '_comb' in opt.pycfg else False  #will include regrouped jec in final
QCD_data_driven = False
include_bincl = True if not '_final' in opt.pycfg else False
lnN_eff_ele = False


splitTTLL = False
merge_trig_syst = True
lnN_UE_Tune = True
tt_psweight = True
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
    'name': 'lumi_uncorr_2016',
    'type': 'lnN',
    'samples': dict((skey, '1.01') for skey in mc ),
    'group': 'experimental',
}

nuisances['lumi_corr'] = {
    'name': 'lumi_corr',
    'type': 'lnN',
    'samples': dict((skey, '1.006') for skey in mc ),
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
    'samples': {'TT+bb':'1.0 [0.8,1.3] '},
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
    'samples': {'TT+cc':'1 [0.8,1.3] '},
    'group': 'theory',
}
nuisances['ttccXsec_param'] = {
    'name': 'ttccXsec',
    'type': 'param',
    'constraint': '1.0  0.3',
    'samples': {},
    'group': 'theory',
}

#ttbbXsec: 1.746610', 'ttbjXsec: 8.265863', 'ttccXsec: 33.970058', 'ttjjXsec: 407.677469
# (451.66-@0*(1.7466+8.2659)-@1*33.970)/(407.68)

nuisances['ttjjXsec'] = {
    'name': 'ttjjXsec',
    'type': 'rateParam',
    #'samples': {'TT+jj':'(364.35-@0*1.433-@1*6.782-@2*28.21)/(327.93)    ttbbXsec,ttbjXsec,ttccXsec'},
    'samples': {'TT+jj':'(451.66-@0*(1.7466+8.2659)-@1*33.970)/(407.68)    ttbbXsec,ttccXsec'},  #XXX 364.35 : Xsec of TTLJ, but TT+jj is TTLJ+TTLL. it's wrong.
    #'samples': {'TT+jj':'(364.35-@0*(1.433+6.782)-1.*28.21)/(327.93)    ttbbXsec'},
    'group': 'theory',
}
if splitTTLL:
  nuisances['ttbbXsec']['samples'] = {'TTLJ+bb':'1 [0.8,1.5] ','TTLL+bb':'1 [0.8,1.5] '}
  nuisances['ttccXsec']['samples'] = {'TTLJ+cc':'1 [0.8,1.5] ','TTLL+cc':'1 [0.8,1.5] '}
  nuisances['ttjjXsec']['samples'] = {'TTLJ+jj':'(364.35-@0*(1.433+6.782)-@1*28.21)/(327.93)    ttbbXsec,ttccXsec','TTLL+jj':'(364.35-@0*(1.433+6.782)-@1*28.21)/(327.93)    ttbbXsec,ttccXsec'}


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

if QCD_data_driven:
  #eleORmuCH case only consider "ele" nuisance to avoid double counting
  nuisances['qcd_iso_e_2b'] = {
      'name': 'antiiso_ele',
      #'rename': 'antiiso_ele_2b_2016',
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
      #'rename': 'antiiso_ele_3b_2016',
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
      #'rename': 'antiiso_mu_2b_2016',
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
      #'rename': 'antiiso_mu_3b_2016',
      'type': 'shape',
      'AsLnN': '1',
      #'symmetrize_ttsyst': True,
      'cuts': ['sng_4j_muCH_3b','sng_jbin_muCH_4j_3b','sng_jbin_muCH_5j_3b','sng_jbin_muCH_6j_3b','sng_jbin_muCH_4b'], #not include 'sng_4j_eleORmuCH_2b','sng_4j_eleORmuCH_3b', to avoid double counting
      #'AsShape' : 1,
      'samples': dict((skey, ['1.','1.']) for skey in qcdmc),
      'group': 'experimental',
  }
  #qcd_norm_year_uncorr = False
  #nuisances['qcd_norm_e_2b_2016'] = {
  #    'name': 'qcd_norm_e_2b'+'_2016' if qcd_norm_year_uncorr else '',
  #    'type': 'lnN',
  #    'cuts': ['sng_4j_eleORmuCH_2b','sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b'],
  #    #'AsShape' : 1,
  #    'samples': dict((skey, '1.5') for skey in qcdmc),
  #    'group': 'experimental',
  #}
  #nuisances['qcd_norm_e_3b_2016'] = {
  #    'name': 'qcd_norm_e_3b'+'_2016' if qcd_norm_year_uncorr else '',
  #    'type': 'lnN',
  #    'cuts': ['sng_4j_eleORmuCH_3b','sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b'],
  #    #'AsShape' : 1,
  #    'samples': dict((skey, '1.5') for skey in qcdmc),
  #    'group': 'experimental',
  #}
  #nuisances['qcd_norm_m_2b_2016'] = {
  #    'name': 'qcd_norm_m_2b'+'_2016' if qcd_norm_year_uncorr else '',
  #    'type': 'lnN',
  #    'cuts': ['sng_4j_muCH_2b','sng_jbin_muCH_4j_2b','sng_jbin_muCH_5j_2b','sng_jbin_muCH_6j_2b'],
  #    #'AsShape' : 1,
  #    'samples': dict((skey, '1.5') for skey in qcdmc),
  #    'group': 'experimental',
  #}
  #nuisances['qcd_norm_m_3b_2016'] = {
  #    'name': 'qcd_norm_m_3b'+'_2016' if qcd_norm_year_uncorr else '',
  #    'type': 'lnN',
  #    'cuts': ['sng_4j_muCH_3b','sng_jbin_muCH_4j_3b','sng_jbin_muCH_5j_3b','sng_jbin_muCH_6j_3b','sng_jbin_muCH_4b'],
  #    #'AsShape' : 1,
  #    'samples': dict((skey, '1.5') for skey in qcdmc),
  #    'group': 'experimental',
  #}
  nuisances['qcd_norm'] = {
      'name': 'qcd_norm_2016',
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
    'samples': dict((skey, '1.2') for skey in ['ST','Others']),
    'group': 'experimental',
}
nuisances['DYNorm'] = {
    'name': 'DYNorm',
    'type': 'lnN',
    'AsShape' : 1,
    'samples': dict((skey, '1.2') for skey in ['DY','Others']),
    'group': 'experimental',
}
nuisances['WjNorm'] = {
    'name': 'WjNorm',
    'type': 'lnN',
    'AsShape' : 1,
    'samples': dict((skey, '1.2') for skey in ['Wjets','Others']),
    'group': 'experimental',
}
nuisances['VVNorm'] = {
    'name': 'VVNorm',
    'type': 'lnN',
    'AsShape' : 1,
    'samples': dict((skey, '1.2') for skey in ['WZ','WW','ZZ','Others']),
    'group': 'experimental',
}
nuisances['TTVNorm'] = {
    'name': 'TTVNorm',
    'type': 'lnN',
    'AsShape' : 1,
    'samples': dict((skey, '1.1') for skey in ['TTWjets','TTZjets','ttH','Others']),
    'group': 'experimental',
}



##old ttH multilepton, NLO-NNLO fit
#(TMath::Sqrt(TMath::Exp(1.61468e-03 + 3.46659e-06*topGenPt - 8.90557e-08*topGenPt*topGenPt) * TMath::Exp(1.61468e-03 + 3.46659e-06*antitopGenPt - 8.90557e-08*antitopGenPt*antitopGenPt))) # CUETP8 -> CP5
Top_pTrw = '(TMath::Sqrt(TMath::Exp(-0.158631 + 2.00214e-04*{TOP_GEN_PT} - 3.09496e-07*{TOP_GEN_PT}*{TOP_GEN_PT} + 34.93/({TOP_GEN_PT}+135.633)) * TMath::Exp(-0.158631 + 2.00214e-04*{ANTITOP_GEN_PT} - 3.09496e-07*{ANTITOP_GEN_PT}*{ANTITOP_GEN_PT} + 34.93/({ANTITOP_GEN_PT}+135.633)))  *  (TMath::Sqrt(TMath::Exp(1.61468e-03 + 3.46659e-06*topGenPt - 8.90557e-08*topGenPt*topGenPt) * TMath::Exp(1.61468e-03 + 3.46659e-06*antitopGenPt - 8.90557e-08*antitopGenPt*antitopGenPt))) )'.format(TOP_GEN_PT='((topGenPt>472)*472 + (topGenPt<=472)*topGenPt)', ANTITOP_GEN_PT='((antitopGenPt>472)*472 + (antitopGenPt<=472)*antitopGenPt)')
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

nuisances['prefire'] = {
    'name': 'eff_prefiring_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey,['L1PreFiringWeight_Up/L1PreFiringWeight_Nom','L1PreFiringWeight_Dn/L1PreFiringWeight_Nom']) for skey in mc),
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
      'name': 'eff_trigger_ele_2016',
      'kind': 'weight',
      'type': 'shape',
      'samples': dict((skey, ['trig_ele_up','trig_ele_down']) for skey in mc),
      'cuts': ['sng_4j','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleCH_2b','sng_jbin_eleCH_4j_2b','sng_jbin_eleCH_5j_2b','sng_jbin_eleCH_6j_2b','sng_4j_eleCH_3b','sng_jbin_eleCH_4j_3b','sng_jbin_eleCH_5j_3b','sng_jbin_eleCH_6j_3b','sng_jbin_eleCH_4b','dbl_4j_eeORmmORemORme','dbl_4j','dbl_4j_ee','dbl_4j_em','dbl_4j_me','dbl_4j_ee_onZ',],
      'group': 'experimental',
  }
  
  nuisances['trig_mu'] = {
      'name': 'eff_trigger_mu_2016',
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
  nuisances['eff_muon'] = {
      'name': 'eff_muon',
      #'rename': 'eff_lepton',
      'kind': 'weight',
      'type': 'shape',
      'samples': dict((skey, ['id_mu_up','id_mu_down']) for skey in mc),
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
if True:

  jes_syst = ['jesFlavorQCD','jesTotalNoFlavor']
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
          'folderUp'   : makeMCDirectory('_jetMETSyst_{SKIM}Up'.format(SKIM=skim_)) if not include_mva else makeMCDirectory_mva('_jetMETSyst_{SKIM}Up__mvaCHToCB_2016_jetMETSyst_{SKIM}Up'.format(SKIM=skim_))    ,
          'folderDown' : makeMCDirectory('_jetMETSyst_{SKIM}Down'.format(SKIM=skim_)) if not include_mva else makeMCDirectory_mva('_jetMETSyst_{SKIM}Down__mvaCHToCB_2016_jetMETSyst_{SKIM}Down'.format(SKIM=skim_)),
          'group': 'experimental',
          'FromNormTree': [btag_jes_up, btag_jes_down],
      }


nuisances['jer0'] = {
    'name': 'jer0_2016',
    #'rename': 'jer0',
    #'symmetrize_ttsyst': True,
    'kind': 'branch_custom',
    'type': 'shape',
    'BrFromToUp'  : GetJECVariationDict(JECUnc_nom_branches,"jer0Up"),
    'BrFromToDown' : GetJECVariationDict(JECUnc_nom_branches,"jer0Down"),
    'samples': dict((skey, ['1.','1.']) for skey in mc),
    'folderUp'   : makeMCDirectory('_jetMETSyst_jer0Up')   if not include_mva else  makeMCDirectory_mva('_jetMETSyst_jer0Up__mvaCHToCB_2016_jetMETSyst_jer0Up')    ,
    'folderDown' : makeMCDirectory('_jetMETSyst_jer0Down') if not include_mva else  makeMCDirectory_mva('_jetMETSyst_jer0Down__mvaCHToCB_2016_jetMETSyst_jer0Down'),
    'FromNormTree': ['Jet_pt_jer0Up','Jet_pt_jer0Down'],
    'group': 'experimental',
}

nuisances['jer1'] = {
    'name': 'jer1_2016',
    #'rename': 'jer1',
    #'symmetrize_ttsyst': True,
    'kind': 'branch_custom',
    'type': 'shape',
    'BrFromToUp'  : GetJECVariationDict(JECUnc_nom_branches,"jer1Up"),
    'BrFromToDown' : GetJECVariationDict(JECUnc_nom_branches,"jer1Down"),
    'samples': dict((skey, ['1.','1.']) for skey in mc),
    'folderUp'   : makeMCDirectory('_jetMETSyst_jer1Up')   if not include_mva else  makeMCDirectory_mva('_jetMETSyst_jer1Up__mvaCHToCB_2016_jetMETSyst_jer1Up')    ,
    'folderDown' : makeMCDirectory('_jetMETSyst_jer1Down') if not include_mva else  makeMCDirectory_mva('_jetMETSyst_jer1Down__mvaCHToCB_2016_jetMETSyst_jer1Down'),
    'FromNormTree': ['Jet_pt_jer1Up','Jet_pt_jer1Down'],
    'group': 'experimental',
}

nuisances['unclustEn'] = {
    'name': 'unclustEn_2016',
    'kind': 'branch_custom',
    'type': 'shape',
    'BrFromToUp'  : GetJECVariationDict(unclustEn_branches,"unclustEnUp"),
    'BrFromToDown' : GetJECVariationDict(unclustEn_branches,"unclustEnDown"),
    'samples': dict((skey, ['1.','1.']) for skey in mc),
    'folderUp'   : makeMCDirectory('_jetMETSyst_unclustEnUp')    if not include_mva else  makeMCDirectory_mva('_jetMETSyst_unclustEnUp__mvaCHToCB_2016_jetMETSyst_unclustEnUp')      ,
    'folderDown' : makeMCDirectory('_jetMETSyst_unclustEnDown')  if not include_mva else  makeMCDirectory_mva('_jetMETSyst_unclustEnDown__mvaCHToCB_2016_jetMETSyst_unclustEnDown')  ,
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

if not 'comb' in opt.pycfg or not lnN_UE_Tune:
  nuisances['TuneCP5'] = {
      'name': 'TuneCP5',
      'kind': 'tree',
      'type': 'shape',
      #'symmetrize_ttsyst': True,
      #'syncronize_stat' : True,
      'samples': dict((skey, ['1.','1.']) for skey in ttmc_syst),
      # name_TT*_*[Up|Down] are defined in samples_ttbarCat.py
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
      #XXX
      'name': 'hdamp_M2T4',
      'rename': 'hdamp',
      'kind': 'tree',
      'type': 'shape',
      #'symmetrize_ttsyst': True,
      #'syncronize_stat' : True,
      'samples': dict((skey, ['1.','1.']) for skey in ttmc_syst ),
      'folderUp'   : makeMCDirectory('__HDAMPup'),
      'folderDown' : makeMCDirectory('__HDAMPdo'),
      'group': 'theory',
  
  }

  hdamp_syst_up   = "(ttGenPt<0.00)*(1.) + (ttGenPt>=0.00 && ttGenPt<10.00)*(0.98)+ (ttGenPt>=10.00 && ttGenPt<20.00)*(0.98)+ (ttGenPt>=20.00 && ttGenPt<30.00)*(0.99)+ (ttGenPt>=30.00 && ttGenPt<40.00)*(0.98)+ (ttGenPt>=40.00 && ttGenPt<50.00)*(0.99)+ (ttGenPt>=50.00 && ttGenPt<60.00)*(1.00)+ (ttGenPt>=60.00 && ttGenPt<80.00)*(1.00)+ (ttGenPt>=80.00 && ttGenPt<100.00)*(1.01)+ (ttGenPt>=100.00 && ttGenPt<200.00)*(1.02)+ (ttGenPt>=200.00 && ttGenPt<1000.00)*(1.06) + (ttGenPt>=1000.00)*(1.)"
  hdamp_syst_down = "(ttGenPt<0.00)*(1.) + (ttGenPt>=0.00 && ttGenPt<10.00)*(1.04)+ (ttGenPt>=10.00 && ttGenPt<20.00)*(1.04)+ (ttGenPt>=20.00 && ttGenPt<30.00)*(1.03)+ (ttGenPt>=30.00 && ttGenPt<40.00)*(1.02)+ (ttGenPt>=40.00 && ttGenPt<50.00)*(1.01)+ (ttGenPt>=50.00 && ttGenPt<60.00)*(1.01)+ (ttGenPt>=60.00 && ttGenPt<80.00)*(0.99)+ (ttGenPt>=80.00 && ttGenPt<100.00)*(0.97)+ (ttGenPt>=100.00 && ttGenPt<200.00)*(0.93)+ (ttGenPt>=200.00 && ttGenPt<1000.00)*(0.91) + (ttGenPt>=1000.00)*(1.)"
  mtop_syst_up    = '(hadronic_top_M_nom<140.00)*(1.) + (hadronic_top_M_nom>=140.00 && hadronic_top_M_nom<145.00)*(0.96)+ (hadronic_top_M_nom>=145.00 && hadronic_top_M_nom<150.00)*(0.97)+ (hadronic_top_M_nom>=150.00 && hadronic_top_M_nom<155.00)*(0.96)+ (hadronic_top_M_nom>=155.00 && hadronic_top_M_nom<160.00)*(0.97)+ (hadronic_top_M_nom>=160.00 && hadronic_top_M_nom<165.00)*(0.96)+ (hadronic_top_M_nom>=165.00 && hadronic_top_M_nom<170.00)*(0.99)+ (hadronic_top_M_nom>=170.00 && hadronic_top_M_nom<175.00)*(0.98)+ (hadronic_top_M_nom>=175.00 && hadronic_top_M_nom<180.00)*(0.99)+ (hadronic_top_M_nom>=180.00 && hadronic_top_M_nom<185.00)*(1.00)+ (hadronic_top_M_nom>=185.00 && hadronic_top_M_nom<190.00)*(1.01)+ (hadronic_top_M_nom>=190.00 && hadronic_top_M_nom<195.00)*(1.00)+ (hadronic_top_M_nom>=195.00 && hadronic_top_M_nom<200.00)*(1.01) + (hadronic_top_M_nom>=200.00)*(1.)'
  mtop_syst_down  = '(hadronic_top_M_nom<140.00)*(1.) + (hadronic_top_M_nom>=140.00 && hadronic_top_M_nom<145.00)*(1.05)+ (hadronic_top_M_nom>=145.00 && hadronic_top_M_nom<150.00)*(1.04)+ (hadronic_top_M_nom>=150.00 && hadronic_top_M_nom<155.00)*(1.06)+ (hadronic_top_M_nom>=155.00 && hadronic_top_M_nom<160.00)*(1.04)+ (hadronic_top_M_nom>=160.00 && hadronic_top_M_nom<165.00)*(1.03)+ (hadronic_top_M_nom>=165.00 && hadronic_top_M_nom<170.00)*(1.03)+ (hadronic_top_M_nom>=170.00 && hadronic_top_M_nom<175.00)*(1.01)+ (hadronic_top_M_nom>=175.00 && hadronic_top_M_nom<180.00)*(1.00)+ (hadronic_top_M_nom>=180.00 && hadronic_top_M_nom<185.00)*(1.00)+ (hadronic_top_M_nom>=185.00 && hadronic_top_M_nom<190.00)*(1.00)+ (hadronic_top_M_nom>=190.00 && hadronic_top_M_nom<195.00)*(1.01)+ (hadronic_top_M_nom>=195.00 && hadronic_top_M_nom<200.00)*(0.99) + (hadronic_top_M_nom>=200.00)*(1.)'
  nuisances['hdamp_weight'] = {
      'name': 'hdamp_weight',
      'kind': 'weight',
      'type': 'shape',
      #'symmetrize_ttsyst': True,
      #'syncronize_stat' : True,
      'samples': dict((skey, [hdamp_syst_up, hdamp_syst_down]) for skey in ttmc_syst ),
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
  nuisances['mtop_weight'] = {
      'name': 'mtop_weight',
      'kind': 'weight',
      'type': 'shape',
      #'symmetrize_ttsyst': True,
      #'syncronize_stat' : True,
      'samples': dict((skey, [mtop_syst_up, mtop_syst_down]) for skey in ttmc_syst ),
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
  nuisances['mtop_weight'] = {
      'name': 'mtop_weight',
      'rename': 'mtop',
      'kind': 'weight',
      'type': 'shape',
      #'symmetrize_ttsyst': True,
      #'syncronize_stat' : True,
      'samples': dict((skey, ['1.','1.']) for skey in ttmc_syst ),
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

if not 'comb' in opt.pycfg:
  if tt_psweight:
    nuisances['ISR_TT_weight'] = {
        'name': 'ttbar_isr',
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, isr_syst) for skey in ttmc),
    
    }
  else:
    nuisances['ISR_TT_weight'] = {
        'name': 'ttbar_isr',
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, isr_syst) for skey in ttmc if 'CHToCB' in skey),
    
    }
    nuisances['ISR_TT_tree'] = {
        'name': 'ttbar_isr',
        'kind': 'tree',
        'type': 'shape',
        'samples': dict((skey, ['1.0','1.0']) for skey in ttmc if not 'CHToCB' in skey),
        #flip Up and Down histogram
        'folderDown'   : makeMCDirectory('__ISRup'),
        'folderUp' : makeMCDirectory('__ISRdo'),
    }
else:
  nuisances['ISR_TTjj'] = {
      'name': 'ttbar_isr',
      'rename': 'ttjj_isr',
      'kind': 'weight',
      'type': 'shape',
      #'syncronize_stat' : True,
      'samples': dict((skey, isr_syst) for skey in ttmc if skey not in ttbbmc+ttccmc),
      'group': 'theory',
  
  }
  nuisances['ISR_TTcc'] = {
      'name': 'ttbar_isr',
      'rename': 'ttcc_isr',
      'kind': 'weight',
      'type': 'shape',
      #'syncronize_stat' : True,
      'samples': dict((skey, isr_syst) for skey in ttccmc ),
      'group': 'theory',
  
  }
  nuisances['ISR_TTbb'] = {
      'name': 'ttbar_isr',
      'rename': 'ttbb_isr',
      'kind': 'weight',
      'type': 'shape',
      #'syncronize_stat' : True,
      'samples': dict((skey, isr_syst) for skey in ttbbmc ),
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
    'group': 'theory',

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

lhe_scale_syst_ttlj_4j = ['(nCleanJet20_2p4>=4)*(1.1192)+(nCleanJet20_2p4<4)','(nCleanJet20_2p4>=4)*(0.8838)+(nCleanJet20_2p4<4)']
lhe_scale_syst_ttlj_5j = ['(nCleanJet20_2p4>=5)*(1.0098)+(nCleanJet20_2p4<5)','(nCleanJet20_2p4>=5)*(0.9930)+(nCleanJet20_2p4<5)']
lhe_scale_syst_ttlj_6j = ['(nCleanJet20_2p4>=6)*(1.0209)+(nCleanJet20_2p4<6)','(nCleanJet20_2p4>=6)*(0.9858)+(nCleanJet20_2p4<6)']

lhe_scale_syst_ttll_4j = ['(nCleanJet20_2p4>=2)*(1.1192)+(nCleanJet20_2p4<2)','(nCleanJet20_2p4>=2)*(0.8838)+(nCleanJet20_2p4<2)']
lhe_scale_syst_ttll_5j = ['(nCleanJet20_2p4>=3)*(1.0098)+(nCleanJet20_2p4<3)','(nCleanJet20_2p4>=3)*(0.9930)+(nCleanJet20_2p4<3)']
lhe_scale_syst_ttll_6j = ['(nCleanJet20_2p4>=4)*(1.1585/1.1192/1.0098)+(nCleanJet20_2p4<4)','(nCleanJet20_2p4>=4)*(0.8626/0.8838/0.9930)+(nCleanJet20_2p4<4)']

lhe_scale_syst_chtocb_4j  = ['(nCleanJet20_2p4>=4)*(1.2831)+(nCleanJet20_2p4<4)','(nCleanJet20_2p4>=4)*(0.7931)+(nCleanJet20_2p4<4)']
lhe_scale_syst_chtocb_5j  = ['(nCleanJet20_2p4>=5)*(1.0043)+(nCleanJet20_2p4<5)','(nCleanJet20_2p4>=5)*(0.9960)+(nCleanJet20_2p4<5)']
lhe_scale_syst_chtocb_6j  = ['(nCleanJet20_2p4>=6)*(1.0061)+(nCleanJet20_2p4<6)','(nCleanJet20_2p4>=6)*(0.9945)+(nCleanJet20_2p4<6)']

lhe_scale_syst_tt_4j = lambda skey: lhe_scale_syst_ttlj_4j*('TTLJ' in skey) + lhe_scale_syst_ttll_4j*('TTLL' in skey) + lhe_scale_syst_chtocb_4j*('CHToCB' in skey)
lhe_scale_syst_tt_5j = lambda skey: lhe_scale_syst_ttlj_5j*('TTLJ' in skey) + lhe_scale_syst_ttll_5j*('TTLL' in skey) + lhe_scale_syst_chtocb_5j*('CHToCB' in skey) 
lhe_scale_syst_tt_6j = lambda skey: lhe_scale_syst_ttlj_6j*('TTLJ' in skey) + lhe_scale_syst_ttll_6j*('TTLL' in skey) + lhe_scale_syst_chtocb_6j*('CHToCB' in skey) 



if not 'comb' in opt.pycfg:
  nuisances['QCDscale_tt'] = {
      'name': 'QCDscale_tt',
      'type': 'shape', # not treat this in plot maker and datacard maker
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


lhe_scale_syst_st_4j_var = ['Alt$(LHEScaleWeight[0],1.058898)', 'Alt$(LHEScaleWeight[1],1.058810)', 'Alt$(LHEScaleWeight[3],0.993666)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-4],1.009240)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-2],0.945656)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-1],0.956605)']
lhe_scale_syst_st_5j_var = ['Alt$(LHEScaleWeight[0],1.073054)', 'Alt$(LHEScaleWeight[1],1.067547)', 'Alt$(LHEScaleWeight[3],0.997817)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-4],1.005757)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-2],0.939583)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-1],0.947824)']
lhe_scale_syst_st_6j_var = ['Alt$(LHEScaleWeight[0],1.099488)', 'Alt$(LHEScaleWeight[1],1.082491)', 'Alt$(LHEScaleWeight[3],1.007635)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-4],0.996998)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-2],0.929305)', 'Alt$(LHEScaleWeight[Length$(LHEScaleWeight)-1],0.930033)']


#TMath::Max(0,Length$(LHEScaleWeight)-1), (Length$(LHEScaleWeight)-1 >=0)*(Length$(LHEScaleWeight)-1)
# missing LHEScaleWeight in tW top and tW antitop
lhe_scale_syst_st = ['((nCleanJet20_2p4==4)*(1.058898)+(nCleanJet20_2p4==5)*(1.073054)+(nCleanJet20_2p4>=6)*(1.099488)+(nCleanJet20_2p4<4)*1.)', '((nCleanJet20_2p4==4)*(1.058810)+(nCleanJet20_2p4==5)*(1.067547)+(nCleanJet20_2p4>=6)*(1.082491)+(nCleanJet20_2p4<4)*1.)', '((nCleanJet20_2p4==4)*(0.993666)+(nCleanJet20_2p4==5)*(0.997817)+(nCleanJet20_2p4>=6)*(1.007635)+(nCleanJet20_2p4<4)*1.)', '((nCleanJet20_2p4==4)*(1.009240)+(nCleanJet20_2p4==5)*(1.005757)+(nCleanJet20_2p4>=6)*(0.996998)+(nCleanJet20_2p4<4)*1.)', '((nCleanJet20_2p4==4)*(0.945656)+(nCleanJet20_2p4==5)*(0.939583)+(nCleanJet20_2p4>=6)*(0.929305)+(nCleanJet20_2p4<4)*1.)', '((nCleanJet20_2p4==4)*(0.956605)+(nCleanJet20_2p4==5)*(0.947824)+(nCleanJet20_2p4>=6)*(0.930033)+(nCleanJet20_2p4<4)*1.)']

#nuisances['QCDscale_ST'] = {
#    'name': 'QCDscale_ST',
#    'type': 'shape',
#    'kind': 'weight_envelope',
#    'samples':dict((skey, lhe_scale_syst_st) for skey in ['ST','Others'] ),
#    'group': 'theory',
#        
#}
#nuisances['QCDscale_VJ'] = {
#    'name': 'QCDscale_VJ',
#    'type': 'shape',
#    'kind': 'weight_envelope',
#    'samples':dict((skey, lhe_scale_syst) for skey in ['DY','Wjets','Others'] ),
#    'group': 'theory',
#        
#}
# ZZ WZ : missng LHEPdf info
#nuisances['QCDscale_VV'] = {
#    'name': 'QCDscale_VV',
#    'type': 'shape',
#    'kind': 'weight_envelope',
#    'samples':dict((skey, lhe_scale_syst) for skey in ['VV','Others'] ),
#    'group': 'theory',
#        
#}
#nuisances['QCDscale_TTX'] = {
#    'name': 'QCDscale_TTX',
#    'type': 'shape',
#    'kind': 'weight_envelope',
#    'samples':dict((skey, lhe_scale_syst) for skey in ['TTWjets','TTZjets','ttH','Others'] ),
#    'group': 'theory',
#        
#}
lhe_pdf_weight_syst_33    = [ 'LHEPdfWeight[%s]'%i for i in range(33) ]
lhe_pdf_weight_syst_100 = [ 'LHEPdfWeight[%s]'%i for i in range(101) ]
#lhe_pdf_weight_syst = lambda skey : lhe_pdf_weight_syst_33 if 'CHToCB_M' in skey else lhe_pdf_weight_syst_100
lhe_pdf_weight_syst = lambda skey : lhe_pdf_weight_syst_100
nuisances['LHEPdfWeight'] = {
    'name': 'LHEPdfWeight',
    'type': 'shape',
    #'kind': 'weight_rms',
    'kind': 'weight_envelope',
    'samples':dict((skey, lhe_pdf_weight_syst(skey)) for skey in ttmc), # ZZ WZ : missng LHEPdf info
    #'lnNsamples': {'ST' : '1.04',
    #               }, # assign 4% derived from PDF weight variabtion in 2018
    'group': 'theory',
}

nuisances['LHEPdfAlphaS'] = {
    'name': 'LHEPdfAlphaS',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['LHEPdfWeight[102]','LHEPdfWeight[101]']) for skey in ttmc), # ZZ WZ : missng LHEPdf info
    'group': 'theory',

}
