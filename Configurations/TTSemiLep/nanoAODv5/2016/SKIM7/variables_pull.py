#-----Variable Deinition-----#
try:
  from WPandCut2016 import *
except ImportError:
  import os, sys
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv5/2016/SKIM7"
  sys.path.append(BASE_PATH)
  from WPandCut2016 import *


#------End of Variable Definition-----#
#variables={}



common_KF_cuts = '(fabs(hadronic_top_b_jet_pull)<2 &&\
           fabs(w_ch_up_type_jet_pull)<2  &&\
           fabs(w_ch_down_type_jet_pull)<2 &&\
           fitter_status==0)\
'
name_template = "{0}*({1}==1) + (-9999)*({1}==0)"
#( down_type_jet_b_tagged>2 && down_type_jet_b_tagged==1)

for key in ['hadronic_top_b_jet_pull','w_ch_up_type_jet_pull','w_ch_down_type_jet_pull']: 
    variables[key+'_noCut'] = {
        'name': name_template.format(key,'(fitter_status==0)'),
        'range':(100,-10,10),
        'xaxis': 'pull',
        'fold': 0
    }

    variables[key] = {
        'name': name_template.format(key,common_KF_cuts),
        'range':(100,-10,10),
        'xaxis': 'pull',
        'fold': 0
    }


print "len(variables)=",len(variables)
