#-----Variable Deinition-----#
try:
  from WPandCut2018 import *
except ImportError:
  import os, sys
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv7/2018/StackNew_comb"
  sys.path.append(BASE_PATH)
  from WPandCut2018 import *


#------End of Variable Definition-----#
#variables={}

include_mva = False


common_KF_cuts = '(status_nom==0)'
name_template = "{0}*({1}==1) + (-9999)*({1}==0)"
#( down_type_jet_b_tagged_nom>2 && down_type_jet_b_tagged_nom==1)


for key in ['hadronic_top_pt_nom']:
    variables[key.replace("_nom","")] = {
        'name': name_template.format(key,common_KF_cuts),
        'range':(60,0,600),
        'xaxis': key,
        'fold': 0
    }
#for key in ["initial_dijet_M_nom",'initial_dijet_M_high_nom','fitted_dijet_M_nom','fitted_dijet_M_high_nom']:
for key in ['fitted_dijet_M_nom','fitted_dijet_M_high_nom']:

  variables[key.replace("_nom","")] = {
      'name' : name_template.format(key,common_KF_cuts),
      'range':(30,0,180),
      'xaxis':'#it{M_{jj}} [GeV]',
      'fold':0
  
  }
  variables[key.replace("_nom","")+"_down_type_jet_b_tagged"] = {
      'name' : name_template.format(key,common_KF_cuts + "*" + "(nBJets_WP_M >2 && down_type_jet_b_tagged_nom==1)"),
      'range':(30,0,180),
      'xaxis':'#it{M_{jj}} [GeV]',
      'fold':0
  }
  if include_mva:
    mva_template = '(({MVA_VAR}>{MVA_CUT})*(179.9*({VAR2}>=180)+({VAR2}<180)*{VAR2}+180)+({MVA_VAR}<={MVA_CUT})*(179.9*({VAR1}>=180)+({VAR1}<180)*{VAR1}))/{BIN_INTERVAL}'

    #2018 : set sig 100, bkg 1000 optimize S/sqrt(S+B) 
    Cut_DNN_High_nom  = 0.7169
    Cut_DNN_Low_nom   = 0.6775
    Cut_BDT_High_nom  = 0.4094
    Cut_BDT_Low_nom   = 0.2281
    Name_DNN_High_nom = mva_template.format(MVA_VAR='DNN_High_nom', MVA_CUT = Cut_DNN_High_nom,VAR1='fitted_dijet_M_nom',VAR2=key,BIN_INTERVAL='5.') 
    Name_DNN_Low_nom  = mva_template.format(MVA_VAR='DNN_Low_nom' , MVA_CUT = Cut_DNN_Low_nom,VAR1='fitted_dijet_M_nom',VAR2=key,BIN_INTERVAL='5.') 
    Name_BDT_High_nom = mva_template.format(MVA_VAR='BDT_High_nom', MVA_CUT = Cut_BDT_High_nom,VAR1='fitted_dijet_M_nom',VAR2=key,BIN_INTERVAL='5.') 
    Name_BDT_Low_nom  = mva_template.format(MVA_VAR='BDT_Low_nom' , MVA_CUT = Cut_BDT_Low_nom,VAR1='fitted_dijet_M_nom',VAR2=key,BIN_INTERVAL='5.')
    
    for var_key, var_name in [('DNN_High',Name_DNN_High_nom),('DNN_Low',Name_DNN_Low_nom),('BDT_High',Name_BDT_High_nom),('BDT_Low',Name_BDT_Low_nom)]:
      variables[key.replace("_nom","")+"_down_type_jet_b_tagged_"+var_key] = {
          'name' : name_template.format(var_name,common_KF_cuts + "*" + "(nBJets_WP_M >2 && down_type_jet_b_tagged_nom==1)"),
          'range':(72,0,72),
          'xaxis':'Bins', #0 to 36 for not pass MVA, 36 to 72 for pass MVA, 5 GeV per 1 bin
          'fold':0
      }
#variables ['nCleanJet30_2p4_lepveto0p4']={
#    'name' : 'nCleanJet30_2p4_lepveto0p4',
#    'range' : (6,4,10),
#    'xaxis' : 'jet multiplicity',
#    'fold':0
#}
#variables ['nCleanJet30_2p4_tightlepvetoID']={
#    'name' : 'nCleanJet30_2p4_tightlepvetoID',
#    'range' : (6,4,10),
#    'xaxis' : 'jet multiplicity',
#    'fold':0
#}
#variables ['nCleanJet30_2p4_tightlepvetoID_lepveto0p4']={
#    'name' : 'nCleanJet30_2p4_tightlepvetoID_lepveto0p4',
#    'range' : (6,4,10),
#    'xaxis' : 'jet multiplicity',
#    'fold':0
#}

#variables['lnjj_Mt_alt']={
#    'name': 'lnjj_Mt_alt',
#    'range':(100,0.,500.),
#    'xaxis': 'lnjj_Mt_alt',
#    'fold':1
#}
#variables['lnjj_mass']={
#    'name': 'lnjj_mass',
#    'range':([0,200,210,230,250,300,350,400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000],),
#    'divideByBinWidth':1,
#    'xaxis': 'lnjj_mass',
#    'fold':1
#}
#
#variables['minPtWOverMlnjj']={
#    'name':'minPtWOverMlnjj',
#    'range':(20,0,1),
#    'xaxis':'minPtWOverMlnjj',
#    'fold':0
#}
#
#variables['dR_l_Whad']={
#    'name':'dR_l_Whad',
#    'range':(50,0,5),
#    'xaxis':'dR_l_Whad',
#    'fold':0,
#}
#variables['dR_Wlep_Whad']={
#    'name':'dR_Wlep_Whad',
#    'range':(50,0,5),
#    'xaxis':'dR_Wlep_Whad',
#    'fold':0,
#}
#
#
#variables['dPhi_l_Whad']={
#    'name':'dPhi_l_Whad',
#    'range':(50,0,5),
#    'xaxis':'dPhi_l_Whad',
#    'fold':0,
#}
#variables['dPhi_Wlep_Whad']={
#    'name':'dPhi_Wlep_Whad',
#    'range':(50,0,5),
#    'xaxis':'dPhi_Wlep_Whad',
#    'fold':0,
#}

if include_mva:
  variables['DNN_High']={
      'name' : 'DNN_High_nom',
      'range':(50,0,1),
      'xaxis':'DNN score',
      'fold':0
  }
  variables['DNN_Low']={
      'name' : 'DNN_Low_nom',
      'range':(50,0,1),
      'xaxis':'DNN score',
      'fold':0
  }
  variables['BDT_High']={
      'name' : 'BDT_High_nom',
      'range':(50,-1,1),
      'xaxis':'BDT score',
      'fold':0
  }
  variables['BDT_Low']={
      'name' : 'BDT_Low_nom',
      'range':(50,-1,1),
      'xaxis':'BDT score',
      'fold':0
  }

  variables['csv_jet0_mvaCHToCB_nom']={
      'name' : 'csv_jet0_mvaCHToCB_nom',
      'range':(50,0,1),
      'xaxis':'b-tag disc. of jet 0',
      'fold':0
  }
  variables['csv_jet1_mvaCHToCB_nom']={
      'name' : 'csv_jet1_mvaCHToCB_nom',
      'range':(50,0,1),
      'xaxis':'b-tag disc. of jet 1',
      'fold':0
  }
  variables['csv_jet2_mvaCHToCB_nom']={
      'name' : 'csv_jet2_mvaCHToCB_nom',
      'range':(50,0,1),
      'xaxis':'b-tag disc. of jet 2',
      'fold':0
  }
  variables['avg_csv_had_top_nom']={
      'name' : 'avg_csv_had_top_nom',
      'range':(50,0,1),
      'xaxis':'avg. b-tag disc. of jet 0,1,2',
      'fold':0
  }
  variables['second_moment_csv_jet0_mvaCHToCB_nom']={
      'name' : 'second_moment_csv_jet0_mvaCHToCB_nom',
      'range':(50,0,0.5),
      'xaxis':'2^{nd} moment b-tag disc. of jet 0',
      'fold':1
  }
  variables['second_moment_csv_jet1_mvaCHToCB_nom']={
      'name' : 'second_moment_csv_jet1_mvaCHToCB_nom',
      'range':(50,0,0.5),
      'xaxis':'2^{nd} moment b-tag disc. of jet 1',
      'fold':1
  }
  variables['second_moment_csv_jet2_mvaCHToCB_nom']={
      'name' : 'second_moment_csv_jet2_mvaCHToCB_nom',
      'range':(50,0,0.5),
      'xaxis':'2^{nd} moment b-tag disc. of jet 2',
      'fold':1
  }
  variables['dijet_deltaR0_mvaCHToCB_nom']={
      'name' : 'dijet_deltaR0_mvaCHToCB_nom',
      'range':(50,0,5),
      'xaxis':'#DeltaR(c,b^{0})',
      'fold':1
  }
  variables['dijet_deltaR1_mvaCHToCB_nom']={
      'name' : 'dijet_deltaR1_mvaCHToCB_nom',
      'range':(50,0,5),
      'xaxis':'#DeltaR(c,b^{1})',
      'fold':1
  }
  variables['Hplus_b_deltaR0_mvaCHToCB_nom']={
      'name' : 'Hplus_b_deltaR0_mvaCHToCB_nom',
      'range':(50,0,7),
      'xaxis':'#DeltaR(H^{+},b_{had. top}^{0}})',
      'fold':1
  }
  variables['Hplus_b_deltaR1_mvaCHToCB_nom']={
      'name' : 'Hplus_b_deltaR1_mvaCHToCB_nom',
      'range':(50,0,7),
      'xaxis':'#DeltaR(H^{+},b_{had. top}^{1}})',
      'fold':1
  }
  variables['bb_deltaR_mvaCHToCB_nom']={
      'name' : 'bb_deltaR_mvaCHToCB_nom',
      'range':(50,0,5),
      'xaxis':'#DeltaR_{bb}',
      'fold':1
  }
  variables['min_deltaR_bb_event_mvaCHToCB_nom']={
      'name' : 'min_deltaR_bb_event_mvaCHToCB_nom',
      'range':(50,0,5),
      'xaxis':'min #DeltaR_{bb}',
      'fold':1
  }
  variables['HT_btagged_M_nom']={
      'name' : 'HT_btagged_M_nom',
      'range':(60,0,600),
      'xaxis':'HT b-tagged',
      'fold':1
  }
  variables['HT_not_btagged_M_nom']={
      'name' : 'HT_not_btagged_M_nom',
      'range':(60,0,600),
      'xaxis':'HT non b-tagged',
      'fold':1
  }

print "len(variables)=",len(variables)
