#-----Variable Deinition-----#
try:
  from WPandCut2017 import *
except ImportError:
  import os, sys
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv5/2017/StackNew_comb"
  sys.path.append(BASE_PATH)
  from WPandCut2017 import *


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

print "len(variables)=",len(variables)
