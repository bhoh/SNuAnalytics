#-----Variable Deinition-----#
try:
  from WPandCut2017 import *
except ImportError:
  import os, sys
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv9/2017/StackNew_comb"
  sys.path.append(BASE_PATH)
  from WPandCut2017 import *


include_mva   = False
exclude_BDT   = True
include_final = True

common_KF_cuts = '(status_nom==0)'
name_template = "{0}*({1}==1) + (-9999)*({1}==0)"
#( down_type_jet_b_tagged_nom>2 && down_type_jet_b_tagged_nom==1)

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

for key in ['hadronic_top_pt_nom']:
    variables[key.replace("_nom","")] = {
        'name': name_template.format(key,common_KF_cuts),
        'range':(60,0,600),
        'xaxis': 'hadronic top p_{T} [GeV]',
        'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown'],
        'fold': 0
    }

for key in ['hadronic_top_M_nom','leptonic_top_M_nom']:
    variables[key.replace("_nom","")] = {
        'name': name_template.format(key,common_KF_cuts),
        'range':(60,0,300),
        'xaxis': '#it{M} [GeV]',
        'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown'],
        'fold': 0
    }

if include_final:
  #for key in ["initial_dijet_M_nom",'initial_dijet_M_high_nom','fitted_dijet_M_nom','fitted_dijet_M_high_nom']:
  for key in ['fitted_dijet_M_nom','fitted_dijet_M_high_nom']:
  
    variables[key.replace("_nom","")] = {
        'name' : name_template.format(key,common_KF_cuts),
        'range':(30,0,180),
        'xaxis':'#it{M_{jj}} [GeV]',
        'fold':0,
        'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown'],
    
    }
    variables[key.replace("_nom","")+"_down_type_jet_b_tagged"] = {
        'name' : name_template.format(key,common_KF_cuts + "*" + "(nBJets_WP_M >2 && down_type_jet_b_tagged_nom==1)"),
        'range':(30,0,180),
        'xaxis':'#it{M_{jj}} [GeV]',
        'fold':0,
        'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown'],
    }
    if include_mva:
      mva_template = '(({MVA_VAR}>{MVA_CUT})*(179.9*({VAR2}>=180)+({VAR2}<180)*{VAR2}+180)+({MVA_VAR}<={MVA_CUT})*(179.9*({VAR1}>=180)+({VAR1}<180)*{VAR1}))/{BIN_INTERVAL}'
      mva_template_failMVA = '(({MVA_VAR}<={MVA_CUT})*({VAR})+({MVA_VAR}>{MVA_CUT})*999)'
      mva_template_passMVA = '(({MVA_VAR}>{MVA_CUT})*({VAR})+({MVA_VAR}<={MVA_CUT})*999)'
  
      #2018 : set sig 100, bkg 1000 optimize S/sqrt(S+B) 
      Cut_DNN_High_nom  = 0.6205
      Cut_DNN_Low_nom   = 0.6193
      Cut_BDT_High_nom  = 0.2685
      Cut_BDT_Low_nom   = 0.1952

      Name_DNN_High_nom = mva_template.format(MVA_VAR='DNN_High_nom', MVA_CUT = Cut_DNN_High_nom,VAR1='fitted_dijet_M_nom',VAR2=key,BIN_INTERVAL='5.') 
      Name_DNN_High_nom_failMVA = mva_template_failMVA.format(MVA_VAR='DNN_High_nom', MVA_CUT = Cut_DNN_High_nom,VAR=key) 
      Name_DNN_High_nom_passMVA = mva_template_passMVA.format(MVA_VAR='DNN_High_nom', MVA_CUT = Cut_DNN_High_nom,VAR=key) 
      Name_DNN_Low_nom  = mva_template.format(MVA_VAR='DNN_Low_nom' , MVA_CUT = Cut_DNN_Low_nom,VAR1='fitted_dijet_M_nom',VAR2=key,BIN_INTERVAL='5.') 
      Name_DNN_Low_nom_failMVA  = mva_template_failMVA.format(MVA_VAR='DNN_Low_nom' , MVA_CUT = Cut_DNN_Low_nom,VAR=key) 
      Name_DNN_Low_nom_passMVA  = mva_template_passMVA.format(MVA_VAR='DNN_Low_nom' , MVA_CUT = Cut_DNN_Low_nom,VAR=key) 
      Name_BDT_High_nom = mva_template.format(MVA_VAR='BDT_High_nom', MVA_CUT = Cut_BDT_High_nom,VAR1='fitted_dijet_M_nom',VAR2=key,BIN_INTERVAL='5.') 
      Name_BDT_High_nom_failMVA = mva_template_failMVA.format(MVA_VAR='BDT_High_nom', MVA_CUT = Cut_BDT_High_nom,VAR=key) 
      Name_BDT_High_nom_passMVA = mva_template_passMVA.format(MVA_VAR='BDT_High_nom', MVA_CUT = Cut_BDT_High_nom,VAR=key) 
      Name_BDT_Low_nom  = mva_template.format(MVA_VAR='BDT_Low_nom' , MVA_CUT = Cut_BDT_Low_nom,VAR1='fitted_dijet_M_nom',VAR2=key,BIN_INTERVAL='5.')
      Name_BDT_Low_nom_failMVA  = mva_template_failMVA.format(MVA_VAR='BDT_Low_nom' , MVA_CUT = Cut_BDT_Low_nom,VAR=key)
      Name_BDT_Low_nom_passMVA  = mva_template_passMVA.format(MVA_VAR='BDT_Low_nom' , MVA_CUT = Cut_BDT_Low_nom,VAR=key)
     
      for var_key, var_name in [('DNN_High',Name_DNN_High_nom),('DNN_Low',Name_DNN_Low_nom),('BDT_High',Name_BDT_High_nom),('BDT_Low',Name_BDT_Low_nom)]:
        variables[key.replace("_nom","")+"_down_type_jet_b_tagged_"+var_key] = {
            'name' : name_template.format(var_name,common_KF_cuts + "*" + "(nBJets_WP_M >2 && down_type_jet_b_tagged_nom==1)"),
            'range':(72,0,72),
            'xaxis':'#it{M_{jj}} bins', #0 to 36 for not pass MVA, 36 to 72 for pass MVA, 5 GeV per 1 bin
            'fold':0,
            'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown'],
        }
      for var_key, var_name in [('DNN_High_failMVA',Name_DNN_High_nom_failMVA),('DNN_Low_failMVA',Name_DNN_Low_nom_failMVA),('BDT_High_failMVA',Name_BDT_High_nom_failMVA),('BDT_Low_failMVA',Name_BDT_Low_nom_failMVA)]:
        variables[key.replace("_nom","")+"_down_type_jet_b_tagged_"+var_key] = {
            'name' : name_template.format(var_name,common_KF_cuts + "*" + "(nBJets_WP_M >2 && down_type_jet_b_tagged_nom==1)"),
            'range':(30,0,180),
            'xaxis':'#it{M_{jj}}',
            'fold':0,
            'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown'],
        }
      for var_key, var_name in [('DNN_High_passMVA',Name_DNN_High_nom_passMVA),('DNN_Low_passMVA',Name_DNN_Low_nom_passMVA),('BDT_High_passMVA',Name_BDT_High_nom_passMVA),('BDT_Low_passMVA',Name_BDT_Low_nom_passMVA)]:
        variables[key.replace("_nom","")+"_down_type_jet_b_tagged_"+var_key] = {
            'name' : name_template.format(var_name,common_KF_cuts + "*" + "(nBJets_WP_M >2 && down_type_jet_b_tagged_nom==1)"),
            'range':(30,0,180),
            'xaxis':'#it{M_{jj}}',
            'fold':0,
            'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown'],
        }

variables['hadronic_top_b_jet_bRegCorr']={
    'name' : 'Jet_pt_nom[hadronic_top_b_jet_idx_nom] * Jet_bRegCorr[hadronic_top_b_jet_idx_nom]',
    'range':(60,0,300),
    'xaxis':'Hadronic top b jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['hadronic_top_b_jet_noRegCorr']={
    'name' : 'Jet_pt_nom[hadronic_top_b_jet_idx_nom]',
    'range':(60,0,300),
    'xaxis':'Hadronic top b jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['hadronic_top_b_jet_bRegCorr_noSmear']={
    'name' : 'Jet_pt_nom[hadronic_top_b_jet_idx_nom] * Jet_bRegCorr[hadronic_top_b_jet_idx_nom] / Jet_corr_JER[hadronic_top_b_jet_idx_nom]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'Hadronic top b jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['hadronic_top_b_jet_noRegCorr_noSmear']={
    'name' : 'Jet_pt_nom[hadronic_top_b_jet_idx_nom] / Jet_corr_JER[hadronic_top_b_jet_idx_nom]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'Hadronic top b jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['hadronic_top_b_jet_jesTotalNoFlavorUp']={
    'name' : 'Jet_pt_jesTotalNoFlavorUp[hadronic_top_b_jet_idx_nom] * Jet_bRegCorr[hadronic_top_b_jet_idx_nom]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'Hadronic top b jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['hadronic_top_b_jet_jesTotalNoFlavorDown']={
    'name' : 'Jet_pt_jesTotalNoFlavorDown[hadronic_top_b_jet_idx_nom] * Jet_bRegCorr[hadronic_top_b_jet_idx_nom]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'Hadronic top b jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['hadronic_top_b_jet_jesFlavorQCDUp']={
    'name' : 'Jet_pt_jesFlavorQCDUp[hadronic_top_b_jet_idx_nom] * Jet_bRegCorr[hadronic_top_b_jet_idx_nom]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'Hadronic top b jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['hadronic_top_b_jet_jesFlavorQCDDown']={
    'name' : 'Jet_pt_jesFlavorQCDDown[hadronic_top_b_jet_idx_nom] * Jet_bRegCorr[hadronic_top_b_jet_idx_nom]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'Hadronic top b jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}

variables['W_c_jet_cRegCorr']={
    'name' : 'Jet_pt_nom[w_ch_down_type_jet_idx_nom] * Jet_cRegCorr[w_ch_down_type_jet_idx_nom]',
    'range':(60,0,300),
    'xaxis':'Hadronic W c jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['W_c_jet_noRegCorr']={
    'name' : 'Jet_pt_nom[w_ch_down_type_jet_idx_nom]',
    'range':(60,0,300),
    'xaxis':'Hadronic W c jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['W_c_jet_cRegCorr_noSmear']={
    'name' : 'Jet_pt_nom[w_ch_down_type_jet_idx_nom] * Jet_cRegCorr[w_ch_down_type_jet_idx_nom] / Jet_corr_JER[w_ch_down_type_jet_idx_nom] ',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'Hadronic W c jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['W_c_jet_noRegCorr_noSmear']={
    'name' : 'Jet_pt_nom[w_ch_down_type_jet_idx_nom] / Jet_corr_JER[w_ch_down_type_jet_idx_nom]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'Hadronic W c jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['W_c_jet_jesTotalNoFlavorUp']={
    'name' : 'Jet_pt_jesTotalNoFlavorUp[w_ch_down_type_jet_idx_nom] * Jet_cRegCorr[w_ch_down_type_jet_idx_nom]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'Hadronic W c jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['W_c_jet_jesTotalNoFlavorDown']={
    'name' : 'Jet_pt_jesTotalNoFlavorDown[w_ch_down_type_jet_idx_nom] * Jet_cRegCorr[w_ch_down_type_jet_idx_nom]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'Hadronic W c jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['W_c_jet_jesFlavorQCDUp']={
    'name' : 'Jet_pt_jesFlavorQCDUp[w_ch_down_type_jet_idx_nom] * Jet_cRegCorr[w_ch_down_type_jet_idx_nom]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'Hadronic W c jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['W_c_jet_jesFlavorQCDDown']={
    'name' : 'Jet_pt_jesFlavorQCDDown[w_ch_down_type_jet_idx_nom] * Jet_cRegCorr[w_ch_down_type_jet_idx_nom]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'Hadronic W c jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['leptonic_top_b_jet_bRegCorr']={
    'name' : 'Jet_pt_nom[leptonic_top_b_jet_idx_nom] * Jet_bRegCorr[leptonic_top_b_jet_idx_nom]',
    'range':(60,0,300),
    'xaxis':'Leptonic top b jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['leptonic_top_b_jet_noRegCorr']={
    'name' : 'Jet_pt_nom[leptonic_top_b_jet_idx_nom]',
    'range':(60,0,300),
    'xaxis':'Leptonic top b jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['leptonic_top_b_jet_bRegCorr_noSmear']={
    'name' : 'Jet_pt_nom[leptonic_top_b_jet_idx_nom] * Jet_bRegCorr[leptonic_top_b_jet_idx_nom] / Jet_corr_JER[leptonic_top_b_jet_idx_nom]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'Leptonic top b jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['leptonic_top_b_jet_noRegCorr_noSmear']={
    'name' : 'Jet_pt_nom[leptonic_top_b_jet_idx_nom] / Jet_corr_JER[leptonic_top_b_jet_idx_nom]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'Leptonic top b jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['leptonic_top_b_jet_jesTotalNoFlavorUp']={
    'name' : 'Jet_pt_jesTotalNoFlavorUp[leptonic_top_b_jet_idx_nom] * Jet_bRegCorr[leptonic_top_b_jet_idx_nom]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'Leptonic top b jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['leptonic_top_b_jet_jesTotalNoFlavorDown']={
    'name' : 'Jet_pt_jesTotalNoFlavorDown[leptonic_top_b_jet_idx_nom] * Jet_bRegCorr[leptonic_top_b_jet_idx_nom]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'Leptonic top b jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['leptonic_top_b_jet_jesFlavorQCDUp']={
    'name' : 'Jet_pt_jesFlavorQCDUp[leptonic_top_b_jet_idx_nom] * Jet_bRegCorr[leptonic_top_b_jet_idx_nom]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'Leptonic top b jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}
variables['leptonic_top_b_jet_jesFlavorQCDDown']={
    'name' : 'Jet_pt_jesFlavorQCDDown[leptonic_top_b_jet_idx_nom] * Jet_bRegCorr[leptonic_top_b_jet_idx_nom]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'Leptonic top b jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown',],
    'fold':0

}

variables['1st_leading_jet_pt_noRegCorr']={
    'name' : 'Jet_pt_nom[SelectedBJetIdx[0]]',
    'range':(60,0,300),
    'xaxis':'1^{st} leading jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown','dbl_2j','dbl_4j','dbl_4j_eeORmmORemORme'],
    'fold':0

}

variables['2nd_leading_jet_pt_noRegCorr']={
    'name' : 'Jet_pt_nom[SelectedBJetIdx[1]]',
    'range':(60,0,300),
    'xaxis':'1^{nd} leading jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown','dbl_2j','dbl_4j','dbl_4j_eeORmmORemORme'],
    'fold':0

}
variables['1st_leading_jet_pt_noRegCorr_noSmear']={
    'name' : 'Jet_pt_nom[SelectedBJetIdx[0]] / Jet_corr_JER[SelectedBJetIdx[0]]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'1^{st} leading jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown','dbl_2j','dbl_4j','dbl_4j_eeORmmORemORme'],
    'fold':0

}

variables['2nd_leading_jet_pt_noRegCorr_noSmear']={
    'name' : 'Jet_pt_nom[SelectedBJetIdx[1]] / Jet_corr_JER[SelectedBJetIdx[1]]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'1^{nd} leading jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown','dbl_2j','dbl_4j','dbl_4j_eeORmmORemORme'],
    'fold':0

}
variables['1st_leading_jet_pt_bRegCorr']={
    'name' : 'Jet_pt_nom[SelectedBJetIdx[0]] * Jet_bRegCorr[SelectedBJetIdx[0]]',
    'range':(60,0,300),
    'xaxis':'1^{st} leading jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown','dbl_2j','dbl_4j','dbl_4j_eeORmmORemORme'],
    'fold':0

}

variables['2nd_leading_jet_pt_bRegCorr']={
    'name' : 'Jet_pt_nom[SelectedBJetIdx[1]] * Jet_bRegCorr[SelectedBJetIdx[1]]',
    'range':(60,0,300),
    'xaxis':'2^{nd} leading jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown','dbl_2j','dbl_4j','dbl_4j_eeORmmORemORme'],
    'fold':0

}
variables['1st_leading_jet_pt_bRegCorr_noSmear']={
    'name' : 'Jet_pt_nom[SelectedBJetIdx[0]] * Jet_bRegCorr[SelectedBJetIdx[0]] / Jet_corr_JER[SelectedBJetIdx[0]]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'1^{st} leading jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown','dbl_2j','dbl_4j','dbl_4j_eeORmmORemORme'],
    'fold':0

}

variables['2nd_leading_jet_pt_bRegCorr_noSmear']={
    'name' : 'Jet_pt_nom[SelectedBJetIdx[1]] * Jet_bRegCorr[SelectedBJetIdx[1]] / Jet_corr_JER[SelectedBJetIdx[1]]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'2^{nd} leading jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown','dbl_2j','dbl_4j','dbl_4j_eeORmmORemORme'],
    'fold':0

}
variables['1st_leading_jet_pt_jesTotalNoFlavorUp']={
    'name' : 'Jet_pt_jesTotalNoFlavorUp[SelectedBJetIdx[0]] * Jet_bRegCorr[SelectedBJetIdx[0]]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'1^{st} leading jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown','dbl_2j','dbl_4j','dbl_4j_eeORmmORemORme'],
    'fold':0

}

variables['2nd_leading_jet_pt_jesTotalNoFlavorUp']={
    'name' : 'Jet_pt_jesTotalNoFlavorUp[SelectedBJetIdx[1]] * Jet_bRegCorr[SelectedBJetIdx[1]]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'2^{nd} leading jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown','dbl_2j','dbl_4j','dbl_4j_eeORmmORemORme'],
    'fold':0

}
variables['1st_leading_jet_pt_jesTotalNoFlavorDown']={
    'name' : 'Jet_pt_jesTotalNoFlavorDown[SelectedBJetIdx[0]] * Jet_bRegCorr[SelectedBJetIdx[0]]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'1^{st} leading jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown','dbl_2j','dbl_4j','dbl_4j_eeORmmORemORme'],
    'fold':0

}

variables['2nd_leading_jet_pt_jesTotalNoFlavorDown']={
    'name' : 'Jet_pt_jesTotalNoFlavorDown[SelectedBJetIdx[1]] * Jet_bRegCorr[SelectedBJetIdx[1]]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'2^{nd} leading jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown','dbl_2j','dbl_4j','dbl_4j_eeORmmORemORme'],
    'fold':0

}

variables['1st_leading_jet_pt_jesFlavorQCDUp']={
    'name' : 'Jet_pt_jesFlavorQCDUp[SelectedBJetIdx[0]] * Jet_bRegCorr[SelectedBJetIdx[0]]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'1^{st} leading jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown','dbl_2j','dbl_4j','dbl_4j_eeORmmORemORme'],
    'fold':0

}

variables['2nd_leading_jet_pt_jesFlavorQCDUp']={
    'name' : 'Jet_pt_jesFlavorQCDUp[SelectedBJetIdx[1]] * Jet_bRegCorr[SelectedBJetIdx[1]]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'2^{nd} leading jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown','dbl_2j','dbl_4j','dbl_4j_eeORmmORemORme'],
    'fold':0

}
variables['1st_leading_jet_pt_jesFlavorQCDDown']={
    'name' : 'Jet_pt_jesFlavorQCDDown[SelectedBJetIdx[0]] * Jet_bRegCorr[SelectedBJetIdx[0]]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'1^{st} leading jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown','dbl_2j','dbl_4j','dbl_4j_eeORmmORemORme'],
    'fold':0

}

variables['2nd_leading_jet_pt_jesFlavorQCDDown']={
    'name' : 'Jet_pt_jesFlavorQCDDown[SelectedBJetIdx[1]] * Jet_bRegCorr[SelectedBJetIdx[1]]',
    'range':(60,0,300),
    'samples': mc,
    'xaxis':'2^{nd} leading jet P_{T} [GeV]',
    'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown','dbl_2j','dbl_4j','dbl_4j_eeORmmORemORme'],
    'fold':0

}



print "len(variables)=",len(variables)
