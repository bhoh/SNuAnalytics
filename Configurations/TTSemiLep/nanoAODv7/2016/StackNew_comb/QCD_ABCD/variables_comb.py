#-----Variable Deinition-----#
try:
  from WPandCut2016 import *
except ImportError:
  import os, sys
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv5/2016/StackNew_comb"
  sys.path.append(BASE_PATH)
  from WPandCut2016 import *


#------End of Variable Definition-----#
#variables={}

include_mva = True

variables['3_4rd_leading_b_disc'] = {
    'name' : ('Jet_btagDeepFlavB[SelectedBJetIdx[2]]','Jet_btagDeepFlavB[SelectedBJetIdx[3]]'),
    'unroll' : True,
    'range':([0.,0.0614,0.3093,0.7221,1.0],[0.,0.0614,0.3093,0.7221,1.0]),
    'xaxis':'b disc.',
    'fold': 0,
    'cuts': ['dbl_4j','dbl_4j_eeORmmORemORme'],
}
common_KF_cuts = '(status_nom==0)'
name_template = "{0}*({1}==1) + (-9999)*({1}==0)"
#( down_type_jet_b_tagged_nom>2 && down_type_jet_b_tagged_nom==1)


#for key in ["initial_dijet_M_nom",'initial_dijet_M_high_nom','fitted_dijet_M_nom','fitted_dijet_M_high_nom']:
for key in ['fitted_dijet_M_nom','fitted_dijet_M_high_nom']:

  variables[key.replace("_nom","")] = {
      'name' : name_template.format(key,common_KF_cuts),
      'range':(36,0,180),
      'xaxis':'#it{M_{jj}} [GeV]',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_isoDown','sng_jbin','sng_jbin_isoDown','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoDown'],
  
  }
  variables[key.replace("_nom","")+"_down_type_jet_b_tagged"] = {
      'name' : name_template.format(key,common_KF_cuts + "*" + "(nBJets_WP_M >2 && down_type_jet_b_tagged_nom==1)"),
      'range':(36,0,180),
      'xaxis':'#it{M_{jj}} [GeV]',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_isoDown','sng_jbin','sng_jbin_isoDown','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoDown'],
  }
  if include_mva:
    mva_template = '(({MVA_VAR}>{MVA_CUT})*(179.9*({VAR2}>=180)+({VAR2}<180)*{VAR2}+180)+({MVA_VAR}<={MVA_CUT})*(179.9*({VAR1}>=180)+({VAR1}<180)*{VAR1}))/{BIN_INTERVAL}'
    mva_template_failMVA = '(({MVA_VAR}<={MVA_CUT})*({VAR})+({MVA_VAR}>{MVA_CUT})*999)'
    mva_template_passMVA = '(({MVA_VAR}>{MVA_CUT})*({VAR})+({MVA_VAR}<={MVA_CUT})*999)'

    #2016 : set sig 100, bkg 1000 optimize S/sqrt(S+B) 
    Cut_DNN_High_nom  = 0.6203
    Cut_DNN_Low_nom   = 0.5584
    Cut_BDT_High_nom  = 0.1538
    Cut_BDT_Low_nom   = 0.0287
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
          'cuts': ['sng_4j','sng_4j_isoDown','sng_jbin','sng_jbin_isoDown','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoDown'],
      }
    for var_key, var_name in [('DNN_High_failMVA',Name_DNN_High_nom_failMVA),('DNN_Low_failMVA',Name_DNN_Low_nom_failMVA),('BDT_High_failMVA',Name_BDT_High_nom_failMVA),('BDT_Low_failMVA',Name_BDT_Low_nom_failMVA)]:
      variables[key.replace("_nom","")+"_down_type_jet_b_tagged_"+var_key] = {
          'name' : name_template.format(var_name,common_KF_cuts + "*" + "(nBJets_WP_M >2 && down_type_jet_b_tagged_nom==1)"),
          'range':(36,0,180),
          'xaxis':'#it{M_{jj}}',
          'fold':0,
          'cuts': ['sng_4j','sng_4j_isoDown','sng_jbin','sng_jbin_isoDown','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoDown'],
      }
    for var_key, var_name in [('DNN_High_passMVA',Name_DNN_High_nom_passMVA),('DNN_Low_passMVA',Name_DNN_Low_nom_passMVA),('BDT_High_passMVA',Name_BDT_High_nom_passMVA),('BDT_Low_passMVA',Name_BDT_Low_nom_passMVA)]:
      variables[key.replace("_nom","")+"_down_type_jet_b_tagged_"+var_key] = {
          'name' : name_template.format(var_name,common_KF_cuts + "*" + "(nBJets_WP_M >2 && down_type_jet_b_tagged_nom==1)"),
          'range':(36,0,180),
          'xaxis':'#it{M_{jj}}',
          'fold':0,
          'cuts': ['sng_4j','sng_4j_isoDown','sng_jbin','sng_jbin_isoDown','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoDown'],
      }


print "len(variables)=",len(variables)
