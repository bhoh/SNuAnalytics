#-----Variable Deinition-----#
try:
  from WPandCut2016 import *
except ImportError:
  import os, sys
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv7/2016/StackNew_comb"
  sys.path.append(BASE_PATH)
  from WPandCut2016 import *


#------End of Variable Definition-----#
#variables={}

include_mva = False

variables['Event'] = {
    'name' : '1',
    'range':(1,0,2),
    'xaxis':'1',
    'fold': 0
}

variables['Bins'] = {
    'name' : '0*(nCleanJet30_2p4==2 && nBJets_WP_M==2)+1*(nCleanJet30_2p4==3 && nBJets_WP_M==2)+2*(nCleanJet30_2p4>=4 && nBJets_WP_M==2)+3*(nCleanJet30_2p4+nCleanJet20to30_2p4_PU_M==3 && nBJets_WP_M+nBJets_WP_M_20to30==3)+4*(nCleanJet30_2p4+nCleanJet20to30_2p4_PU_M>=4 && nBJets_WP_M+nBJets_WP_M_20to30==3)+5*(nCleanJet30_2p4+nCleanJet20to30_2p4_PU_M>=4 && nBJets_WP_M+nBJets_WP_M_20to30>=4)',
    'range':(6,0,6),
    'xaxis':'Bins',
    'fold': 0,
    'cuts': ['dbl_2j','dbl_2j_eeORmmORemORme'],
}
variables['3rd_leading_b_disc'] = {
    'name' : 'Jet_btagDeepFlavB[SelectedBJetIdx[2]]',
    'range':(10,0,1),
    'xaxis':'b disc.',
    'fold': 0,
    'cuts': ['dbl_4j','dbl_4j_eeORmmORemORme'],
}
variables['4rd_leading_b_disc'] = {
    'name' : 'Jet_btagDeepFlavB[SelectedBJetIdx[3]]',
    'range':(10,0,1),
    'xaxis':'b disc.',
    'fold': 0,
    'cuts': ['dbl_4j','dbl_4j_eeORmmORemORme'],
}
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
      'range':(36,0,180),
      'xaxis':'#it{M_{jj}} [GeV]',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  
  }
  variables[key.replace("_nom","")+"_down_type_jet_b_tagged"] = {
      'name' : name_template.format(key,common_KF_cuts + "*" + "(nBJets_WP_M >2 && down_type_jet_b_tagged_nom==1)"),
      'range':(36,0,180),
      'xaxis':'#it{M_{jj}} [GeV]',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  }
  if include_mva:
    mva_template = '(({MVA_VAR}>{MVA_CUT})*(179.9*({VAR2}>=180)+({VAR2}<180)*{VAR2}+180)+({MVA_VAR}<={MVA_CUT})*(179.9*({VAR1}>=180)+({VAR1}<180)*{VAR1}))/{BIN_INTERVAL}'
    mva_template_failMVA = '(({MVA_VAR}<={MVA_CUT})*({VAR})+({MVA_VAR}>{MVA_CUT})*999)'
    mva_template_passMVA = '(({MVA_VAR}>{MVA_CUT})*({VAR})+({MVA_VAR}<={MVA_CUT})*999)'

    #2016 : set sig 100, bkg 1000 optimize S/sqrt(S+B) 
    Cut_DNN_High_nom  = 0.7344
    Cut_DNN_Low_nom   = 0.6827
    Cut_BDT_High_nom  = 0.3718
    Cut_BDT_Low_nom   = 0.2712
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
          'cuts': ['sng_4j','sng_4j_eleORmuCH'],
      }
    for var_key, var_name in [('DNN_High_failMVA',Name_DNN_High_nom_failMVA),('DNN_Low_failMVA',Name_DNN_Low_nom_failMVA),('BDT_High_failMVA',Name_BDT_High_nom_failMVA),('BDT_Low_failMVA',Name_BDT_Low_nom_failMVA)]:
      variables[key.replace("_nom","")+"_down_type_jet_b_tagged_"+var_key] = {
          'name' : name_template.format(var_name,common_KF_cuts + "*" + "(nBJets_WP_M >2 && down_type_jet_b_tagged_nom==1)"),
          'range':(36,0,180),
          'xaxis':'#it{M_{jj}}',
          'fold':0,
          'cuts': ['sng_4j','sng_4j_eleORmuCH'],
      }
    for var_key, var_name in [('DNN_High_passMVA',Name_DNN_High_nom_passMVA),('DNN_Low_passMVA',Name_DNN_Low_nom_passMVA),('BDT_High_passMVA',Name_BDT_High_nom_passMVA),('BDT_Low_passMVA',Name_BDT_Low_nom_passMVA)]:
      variables[key.replace("_nom","")+"_down_type_jet_b_tagged_"+var_key] = {
          'name' : name_template.format(var_name,common_KF_cuts + "*" + "(nBJets_WP_M >2 && down_type_jet_b_tagged_nom==1)"),
          'range':(36,0,180),
          'xaxis':'#it{M_{jj}}',
          'fold':0,
          'cuts': ['sng_4j','sng_4j_eleORmuCH'],
      }

#variables['Whad_pt']={
#    'name':'Whad_pt',
#    'range':(100,0,1000),
#    'xaxis':'Whad_pt',
#    'fold': 0,
#
#}
#variables['Whad_mass']={
#    'name':'Whad_mass',
#    'range':(42,40,250),
#    'xaxis':'Whad_mass',
#    'fold': 0,
#
#}


#variables['nBJetResolved']={
#    'name':'Sum$(BJetResolved_cjidx)',
#    'range':(5,0,5),
#    'xaxis':'nBJetResolved',
#    'fold':0,
#}
variables['1st_leading_jet_pt']={
    'name' : 'Jet_pt_nom[SelectedJetIdx[0]]',
    'range':(50,30,600),
    'xaxis':'1^{st} leading jet P_{T} [GeV]',
    'fold':0

}
variables['1st_leading_jet_eta']={
    'name' : 'Jet_eta[SelectedJetIdx[0]]',
    'range':(50,-2.5,2.5),
    'xaxis':'1^{st} leading jet eta [GeV]',
    'fold':0

}
variables['Lepton_pt[0]']={
    'name' : 'Lepton_pt[0]',
    'range':(50,25,600),
    'xaxis':'Lepton P_{T} [GeV]',
    'fold':0

}
variables['Lepton_eta[0]']={
    'name' : 'Lepton_eta[0]',
    'range':(50,-2.5,2.5),
    'xaxis':'Lepton #eta',
    'fold':0
}
variables['Lepton_pt[1]']={
    'name' : 'Lepton_pt[1]',
    'range':(50,25,600),
    'xaxis':'Lepton P_{T} [GeV]',
    'fold':0

}
variables['Lepton_eta[1]']={
    'name' : 'Lepton_eta[1]',
    'range':(50,-2.5,2.5),
    'xaxis':'Lepton #eta',
    'fold':0
}
variables['mll'] = {
    'name' : 'mll',
    'range':(40,0,200),
    'xaxis':'#it{m_{ll}} [GeV]',
    'fold': 1
}
#variables['bjet_'+bAlgo]={
#    'name' : 'Jet_btag'+bAlgo+'[CleanJet_jetIdx[BJetResolved_cjidx]]',
#    'range':(25,0,1),
#    'xaxis':'bjet_'+bAlgo,
#    'fold':0
#
#}

variables['PuppiMet']={
    'name' : 'MET_CHToCB_pt_nom',
    'range':(50,0,600),
    'xaxis':'MET [GeV]',
    'fold':0
}

#variables['Wlep_Mt']={
#    'name' : 'Wlep_Mt',
#    'range':(100,0,300),
#    'xaxis':'Wlep_Mt',
#    'fold':0
#}
#variables['Wlep_mass']={
#    'name' : 'Wlep_mass',
#    'range':(100,0,300),
#    'xaxis':'Wlep_mass',
#    'fold':0
#}
#variables['Wlep_pt']={
#    'name' : 'Wlep_pt',
#    'range':(100,0,300),
#    'xaxis':'Wlep_pt',
#    'fold':0
#}

variables ['PV_npvs']={
    'name' : 'PV_npvs',
    'range' : (80,0,80),
    'xaxis' : 'PV_npvs',
    'fold':0
}

variables ['nCleanJet20_2p4']={
    'name' : 'nCleanJet20_2p4',
    'range' : (8,2,10),
    'xaxis' : 'jet multiplicity',
    'fold':0
}

variables ['nCleanJet30_2p4']={
    'name' : 'nCleanJet30_2p4',
    'range' : (8,2,10),
    'xaxis' : 'jet multiplicity',
    'fold':0
}

variables ['nCleanJet20to30_2p4_PU_M']={
    'name' : 'nCleanJet20to30_2p4_PU_M',
    'range' : (8,0,8),
    'xaxis' : 'jet multiplicity',
    'fold':0
}

variables ['nBJets_WP_M']={
    'name' : 'nBJets_WP_M',
    'range' : (6,2,8),
    'xaxis' : 'b tagged jet multiplicity',
    'fold':0
}

variables ['nBJets_WP_M_20to30']={
    'name' : 'nBJets_WP_M_20to30',
    'range' : (6,0,6),
    'xaxis' : 'b tagged jet multiplicity',
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
      'fold':0,
      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  }
  variables['DNN_Low']={
      'name' : 'DNN_Low_nom',
      'range':(50,0,1),
      'xaxis':'DNN score',
      'fold':0,

      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  }
  variables['BDT_High']={
      'name' : 'BDT_High_nom',
      'range':(50,-1,1),
      'xaxis':'BDT score',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  }
  variables['BDT_Low']={
      'name' : 'BDT_Low_nom',
      'range':(50,-1,1),
      'xaxis':'BDT score',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  }

  variables['csv_jet0_mvaCHToCB_nom']={
      'name' : 'csv_jet0_mvaCHToCB_nom',
      'range':(50,0,1),
      'xaxis':'b-tag disc. of jet 0',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  }
  variables['csv_jet1_mvaCHToCB_nom']={
      'name' : 'csv_jet1_mvaCHToCB_nom',
      'range':(50,0,1),
      'xaxis':'b-tag disc. of jet 1',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  }
  variables['csv_jet2_mvaCHToCB_nom']={
      'name' : 'csv_jet2_mvaCHToCB_nom',
      'range':(50,0,1),
      'xaxis':'b-tag disc. of jet 2',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  }
  variables['avg_csv_had_top_nom']={
      'name' : 'avg_csv_had_top_nom',
      'range':(50,0,1),
      'xaxis':'avg. b-tag disc. of jet 0,1,2',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  }
  variables['second_moment_csv_jet0_mvaCHToCB_nom']={
      'name' : 'second_moment_csv_jet0_mvaCHToCB_nom',
      'range':(50,0,0.5),
      'xaxis':'2^{nd} moment b-tag disc. of jet 0',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  }
  variables['second_moment_csv_jet1_mvaCHToCB_nom']={
      'name' : 'second_moment_csv_jet1_mvaCHToCB_nom',
      'range':(50,0,0.5),
      'xaxis':'2^{nd} moment b-tag disc. of jet 1',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  }
  variables['second_moment_csv_jet2_mvaCHToCB_nom']={
      'name' : 'second_moment_csv_jet2_mvaCHToCB_nom',
      'range':(50,0,0.5),
      'xaxis':'2^{nd} moment b-tag disc. of jet 2',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  }
  variables['dijet_deltaR0_mvaCHToCB_nom']={
      'name' : 'dijet_deltaR0_mvaCHToCB_nom',
      'range':(50,0,5),
      'xaxis':'#DeltaR(c,b^{0})',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  }
  variables['dijet_deltaR1_mvaCHToCB_nom']={
      'name' : 'dijet_deltaR1_mvaCHToCB_nom',
      'range':(50,0,5),
      'xaxis':'#DeltaR(c,b^{1})',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  }
  variables['Hplus_b_deltaR0_mvaCHToCB_nom']={
      'name' : 'Hplus_b_deltaR0_mvaCHToCB_nom',
      'range':(50,0,7),
      'xaxis':'#DeltaR(H^{+},b_{had. top}^{0}})',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  }
  variables['Hplus_b_deltaR1_mvaCHToCB_nom']={
      'name' : 'Hplus_b_deltaR1_mvaCHToCB_nom',
      'range':(50,0,7),
      'xaxis':'#DeltaR(H^{+},b_{had. top}^{1}})',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  }
  variables['bb_deltaR_mvaCHToCB_nom']={
      'name' : 'bb_deltaR_mvaCHToCB_nom',
      'range':(50,0,5),
      'xaxis':'#DeltaR_{bb}',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  }
  variables['min_deltaR_bb_event_mvaCHToCB_nom']={
      'name' : 'min_deltaR_bb_event_mvaCHToCB_nom',
      'range':(50,0,5),
      'xaxis':'min #DeltaR_{bb}',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  }
  variables['HT_btagged_M_nom']={
      'name' : 'HT_btagged_M_nom',
      'range':(60,0,600),
      'xaxis':'HT b-tagged',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  }
  variables['HT_not_btagged_M_nom']={
      'name' : 'HT_not_btagged_M_nom',
      'range':(60,0,600),
      'xaxis':'HT non b-tagged',
      'fold':0,
      'cuts': ['sng_4j','sng_4j_eleORmuCH'],
  }


print "len(variables)=",len(variables)
