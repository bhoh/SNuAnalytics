#-----Variable Deinition-----#
try:
  from WPandCut2018 import *
except ImportError:
  import os, sys
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv6/2018/StackNew_comb"
  sys.path.append(BASE_PATH)
  from WPandCut2018 import *


#------End of Variable Definition-----#
#variables={}

variables['Event'] = {
    'name' : '1',
    'range':(1,0,2),
    'xaxis':'1',
    'fold': 0
}

common_KF_cuts = '(fabs(hadronic_top_b_jet_pull_nom)<2 &&\
           fabs(w_ch_up_type_jet_pull_nom)<2  &&\
           fabs(w_ch_down_type_jet_pull_nom)<2 &&\
           fitter_status_nom==0)\
'
name_template = "{0}*({1}==1) + (-9999)*({1}==0)"
#( down_type_jet_b_tagged_nom>2 && down_type_jet_b_tagged_nom==1)

for key in ["initial_dijet_M_nom",'initial_dijet_M_high_nom','fitted_dijet_M_nom','fitted_dijet_M_high_nom']:

  variables[key.replace("_nom","")] = {
      'name' : name_template.format(key,common_KF_cuts),
      'range':(36,0,180),
      'xaxis':'#it{M_{jj}} [GeV]',
      'fold':0
  
  }
  variables[key.replace("_nom","")+"_down_type_jet_b_tagged"] = {
      'name' : name_template.format(key,common_KF_cuts + "*" + "(nBJets_WP_M >2 && down_type_jet_b_tagged_nom==1)"),
      'range':(36,0,180),
      'xaxis':'#it{M_{jj}} [GeV]',
      'fold':0
  }
#'best_chi2',

variables['best_chi2'] = {
    'name': name_template.format('best_chi2_nom','(fitter_status_nom>0)'),
    'range':(150,0,30),
    'xaxis': 'best #chi^{2}',
    'fold': 1
}
variables['fitter_status'] = {
    'name': 'fitter_status_nom',
    'range':(10,-5,5),
    'xaxis': 'fitter_status',
    'fold': 1
}

for key in ['down_type_jet_b_tagged_nom','hadronic_top_b_jet_idx_nom','leptonic_top_b_jet_idx_nom','w_ch_up_type_jet_idx_nom','w_ch_down_type_jet_idx_nom']:
    variables[key.replace("_nom","")] = {
        'name': name_template.format(key,common_KF_cuts),
        'range':(20,0,20),
        'xaxis': 'index',
        'fold': 1
    }


for key in ['hadronic_top_b_jet_pull_nom','w_ch_up_type_jet_pull_nom','w_ch_down_type_jet_pull_nom']: 
    variables[key.replace("_nom","")+'_noCut'] = {
        'name': name_template.format(key,'(fitter_status_nom==0)'),
        'range':(100,-10,10),
        'xaxis': 'pull',
        'fold': 0
    }

    variables[key.replace("_nom","")] = {
        'name': name_template.format(key,common_KF_cuts),
        'range':(100,-10,10),
        'xaxis': 'pull',
        'fold': 0
    }

for key in ['hadronic_top_M_nom','leptonic_top_M_nom','leptonic_W_M_nom']:
    variables[key.replace("_nom","")] = {
        'name': name_template.format(key,common_KF_cuts),
        'range':(60,0,300),
        'xaxis': '#it{M} [GeV]',
        'fold': 0
    }

for key in ['hadronic_top_pt_nom']:
    variables[key.replace("_nom","")] = {
        'name': name_template.format(key,common_KF_cuts),
        'range':(60,0,600),
        'xaxis': key,
        'fold': 0
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

variables['2nd_leading_jet_pt']={
    'name' : 'Jet_pt_nom[SelectedJetIdx[1]]',
    'range':(50,30,600),
    'xaxis':'2^{nd} leading jet P_{T} [GeV]',
    'fold':0

}
variables['3rd_leading_jet_pt']={
    'name' : 'Jet_pt_nom[SelectedJetIdx[2]]',
    'range':(50,30,600),
    'xaxis':'3^{rd} leading jet P_{T} [GeV]',
    'fold':0

}
variables['4th_leading_jet_pt']={
    'name' : 'Jet_pt_nom[SelectedJetIdx[3]]',
    'range':(50,30,600),
    'xaxis':'4^{th} leading jet P_{T} [GeV]',
    'fold':0

}
variables['1st_leading_b_jet_pt']={
    'name' : 'Jet_pt_nom[SelectedBJetIdx[0]]',
    'range':(50,30,600),
    'xaxis':'1^{st} leading b jet P_{T} [GeV]',
    'fold':0

}

variables['2nd_leading_b_jet_pt']={
    'name' : 'Jet_pt_nom[SelectedBJetIdx[1]]',
    'range':(50,30,600),
    'xaxis':'2^{nd} leading b jet P_{T} [GeV]',
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
    'range':(100,-5,5),
    'xaxis':'Lepton #eta',
    'fold':0
}

#variables['bjet_'+bAlgo]={
#    'name' : 'Jet_btag'+bAlgo+'[CleanJet_jetIdx[BJetResolved_cjidx]]',
#    'range':(25,0,1),
#    'xaxis':'bjet_'+bAlgo,
#    'fold':0
#
#}

variables['PuppiMet']={
    'name' : 'METAlias',
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

variables ['nCleanJet30_2p5']={
    'name' : 'nCleanJet30_2p5',
    'range' : (6,4,10),
    'xaxis' : 'jet multiplicity',
    'fold':0
}

variables ['nBJets_WP_M']={
    'name' : 'nBJets_WP_M',
    'range' : (6,2,8),
    'xaxis' : 'b tagged jet multiplicity',
    'fold':0
}

#variables ['nCleanJet30_2p5_lepveto0p4']={
#    'name' : 'nCleanJet30_2p5_lepveto0p4',
#    'range' : (6,4,10),
#    'xaxis' : 'jet multiplicity',
#    'fold':0
#}
#variables ['nCleanJet30_2p5_tightlepvetoID']={
#    'name' : 'nCleanJet30_2p5_tightlepvetoID',
#    'range' : (6,4,10),
#    'xaxis' : 'jet multiplicity',
#    'fold':0
#}
#variables ['nCleanJet30_2p5_tightlepvetoID_lepveto0p4']={
#    'name' : 'nCleanJet30_2p5_tightlepvetoID_lepveto0p4',
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




print "len(variables)=",len(variables)
