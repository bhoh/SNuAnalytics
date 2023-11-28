#-----Variable Deinition-----#
try:
  from WPandCut2018 import *
except ImportError:
  import os, sys
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv9/2018/StackNew_comb"
  sys.path.append(BASE_PATH)
  from WPandCut2018 import *

include_mva = True

variables['Event_passKF'] = {
    #'name' : '1',
    'name' : '(status_nom==0)+(-9999)*(status_nom>0)+(-9999)*(status_nom<0)',
    'range':(1,0,2),
    'xaxis':'1',
    'fold': 0
}

variables['Event_failKF'] = {
    #'name' : '1',
    'name' : '(-9999)*(status_nom==0)+(status_nom>0)+(status_nom<0)',
    'range':(1,0,2),
    'xaxis':'1',
    'fold': 0
}



variables['3_4rd_leading_b_disc'] = {
    'name' : ('Jet_btagDeepFlavB[SelectedBJetIdx[2]]','Jet_btagDeepFlavB[SelectedBJetIdx[3]]'),
    'unroll' : True,
    'range':([0.,0.0490,0.2783,0.7100,1.0],[0.,0.0490,0.2783,0.7100,1.0]),
    'xaxis':'b disc.',
    'fold': 0,
    'cuts': ['dbl_4j','dbl_4j_eeORmmORemORme'],
}
common_KF_cuts = '(status_nom==0)'
name_template = "{0}*({1}==1) + (-0.01)*({1}==0)"
#( down_type_jet_b_tagged_nom>2 && down_type_jet_b_tagged_nom==1)

#for key in ["initial_dijet_M_nom",'initial_dijet_M_high_nom','fitted_dijet_M_nom','fitted_dijet_M_high_nom']:
for key in ["initial_dijet_M_nom",'fitted_dijet_M_nom','fitted_dijet_M_high_nom']:
#for key in ['fitted_dijet_M_nom','fitted_dijet_M_high_nom']:

  variables[key.replace("_nom","")] = {
      'name' : name_template.format(key,common_KF_cuts),
      'range':(45,0,180),
      'xaxis':'#it{M_{jj}} [GeV]',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown'],
  
  }
  variables[key.replace("_nom","")+"_down_type_jet_b_tagged"] = {
      'name' : name_template.format(key,common_KF_cuts + "*" + "((nBJets_WP_M+nBJets_WP_M_25to30) >2 && down_type_jet_b_tagged_nom==1)"),
      'range':(45,0,180),
      'xaxis':'#it{M_{jj}} [GeV]',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown'],
  }
  variables[key.replace("_nom","")+"_down_type_jet_not_b_tagged"] = {
      'name' : name_template.format(key,common_KF_cuts + "*" + "((nBJets_WP_M+nBJets_WP_M_25to30) >2 && down_type_jet_b_tagged_nom==0)"),
      'range':(45,0,180),
      'xaxis':'#it{M_{jj}} [GeV]',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown'],
  }

if include_mva:
  for key in ['fitted_dijet_M_nom','fitted_dijet_M_high_nom']:
    mva_template = '(({MVA_VAR}<={MVA_CUT1})*(179.9*({VAR2}>=180)+({VAR2}<180)*{VAR2}) + ({MVA_VAR}>{MVA_CUT1} && {MVA_VAR}<={MVA_CUT2})*(179.9*({VAR2}>=180)+({VAR2}<180)*{VAR2}+180) + ({MVA_VAR}>{MVA_CUT2})*(179.9*({VAR2}>=180)+({VAR2}<180)*{VAR2}+360))/{BIN_INTERVAL}'

    #2018 : set sig 100, bkg 1000 optimize S/sqrt(S+B) 
    Cut_DNN_High_nom1  = 0.45 # sig 70% eff
    Cut_DNN_High_nom2  = 0.75 # sig 30% eff
    Cut_DNN_Low_nom1   = 0.48 # sig 70% eff
    Cut_DNN_Low_nom2   = 0.78 # sig 30% eff
    Name_DNN_High_nom = mva_template.format(MVA_VAR='DNN_High_nom', MVA_CUT1 = Cut_DNN_High_nom1, MVA_CUT2 = Cut_DNN_High_nom2, VAR1='fitted_dijet_M_nom',VAR2=key,BIN_INTERVAL='4.') 
    Name_DNN_Low_nom  = mva_template.format(MVA_VAR='DNN_Low_nom' , MVA_CUT1 = Cut_DNN_Low_nom1, MVA_CUT2 = Cut_DNN_Low_nom2, VAR1='fitted_dijet_M_nom',VAR2=key,BIN_INTERVAL='4.') 
   
    for var_key, var_name in [('DNN_High',Name_DNN_High_nom),('DNN_Low',Name_DNN_Low_nom)]:
      variables[key.replace("_nom","")+"_"+var_key] = {
          'name' : name_template.format(var_name,common_KF_cuts + "*" + "((nBJets_WP_M+nBJets_WP_M_25to30) ==2)"),
          'range':(135,0,135),
          'xaxis':'#it{M_{jj}} bins', #0 to 36 for not pass MVA, 36 to 72 for pass MVA, 5 GeV per 1 bin
          'fold':0,
          'blind': {'sng_4j_eleCH_3b': 'full', 'sng_4j_muCH_3b': 'full', 'sng_4j_eleORmuCH_3b': 'full'},
          'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown'],
      }
      variables[key.replace("_nom","")+"_down_type_jet_b_tagged_"+var_key] = {
          'name' : name_template.format(var_name,common_KF_cuts + "*" + "((nBJets_WP_M+nBJets_WP_M_25to30) >2 && down_type_jet_b_tagged_nom==1)"),
          'range':(135,0,135),
          'xaxis':'#it{M_{jj}} bins', #0 to 36 for not pass MVA, 36 to 72 for pass MVA, 5 GeV per 1 bin
          'fold':0,
          'blind': {'sng_4j_eleCH_3b': 'full', 'sng_4j_muCH_3b': 'full', 'sng_4j_eleORmuCH_3b': 'full'},
          'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown'],
      }

  variables["DNN_High_mass"] = {
      'name' : name_template.format("DNN_High_mass_nom",common_KF_cuts),
      'range':(11,-0.1,1),
      'xaxis':'DNN score',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown'],
  
  }
  variables["DNN_High_mass"+"_down_type_jet_b_tagged"] = {
      'name' : name_template.format("DNN_High_mass_nom",common_KF_cuts + "*" + "((nBJets_WP_M+nBJets_WP_M_25to30) >2 && down_type_jet_b_tagged_nom==1)"),
      'range':(11,-0.1,1),
      'xaxis':'DNN score',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown'],
  }
  variables["DNN_Low_mass"] = {
      'name' : name_template.format("DNN_Low_mass_nom",common_KF_cuts),
      'range':(11,-0.1,1),
      'xaxis':'DNN score',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown'],
  
  }
  variables["DNN_Low_mass"+"_down_type_jet_b_tagged"] = {
      'name' : name_template.format("DNN_Low_mass_nom",common_KF_cuts + "*" + "((nBJets_WP_M+nBJets_WP_M_25to30) >2 && down_type_jet_b_tagged_nom==1)"),
      'range':(11,-0.1,1),
      'xaxis':'DNN score',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown'],
  }
  #
  #
  #
  variables["DNN_Low"] = {
      'name' : name_template.format("DNN_Low_nom",common_KF_cuts),
      'range':(11,-0.1,1),
      'xaxis':'DNN score',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown'],
  
  }
  variables["DNN_High"] = {
      'name' : name_template.format("DNN_High_nom",common_KF_cuts),
      'range':(11,-0.1,1),
      'xaxis':'DNN score',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_isoUp','sng_4j_isoDown','sng_jbin','sng_4j_eleORmuCH','sng_4j_eleORmuCH_isoUp','sng_4j_eleORmuCH_isoDown'],
  
  }

#------End of Variable Definition-----#
#variables={}

print "len(variables)=",len(variables)
