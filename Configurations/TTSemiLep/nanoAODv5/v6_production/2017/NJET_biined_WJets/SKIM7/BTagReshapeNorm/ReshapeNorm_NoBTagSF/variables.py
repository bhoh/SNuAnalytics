#-----Variable Deinition-----#
try:
  from WPandCut2017 import *
except ImportError:
  import os, sys
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv6/2018/SKIM5/HMVar5"
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

#### for b jets

variables['b_pt20to30_abseta0to2.5']={
    'name' : 'CleanJet_pt > 20. && CleanJet_pt<=30 && abs(CleanJet_eta)<2.5 && Jet_hadronFlavour[CleanJet_jetIdx]==5',
    'range':(2,0,2),
    'xaxis':'Bin',
    'fold':0

}
variables['b_pt30to50_abseta0to2.5']={
    'name' : 'CleanJet_pt > 30. && CleanJet_pt<= 50. && abs(CleanJet_eta)<2.5 && Jet_hadronFlavour[CleanJet_jetIdx]==5',
    'range':(2,0,2),
    'xaxis':'Bin',
    'fold':0

}
variables['b_pt50to70_abseta0to2.5']={
    'name' : 'CleanJet_pt > 50. && CleanJet_pt<= 70. && abs(CleanJet_eta)<2.5 && Jet_hadronFlavour[CleanJet_jetIdx]==5',
    'range':(2,0,2),
    'xaxis':'Bin',
    'fold':0

}
variables['b_pt70to100_abseta0to2.5']={
    'name' : 'CleanJet_pt > 70. && CleanJet_pt<=100. && abs(CleanJet_eta)<2.5 && Jet_hadronFlavour[CleanJet_jetIdx]==5',
    'range':(2,0,2),
    'xaxis':'Bin',
    'fold':0

}
variables['b_pt100toINF_abseta0to2.5']={
    'name' : 'CleanJet_pt > 100. && abs(CleanJet_eta)<2.5 && Jet_hadronFlavour[CleanJet_jetIdx]==5',
    'range':(2,0,2),
    'xaxis':'Bin',
    'fold':0

}

#### for udsg jets

variables['udsg_pt20to30_abseta0to0.8']={
    'name' : 'CleanJet_pt > 20  && CleanJet_pt<= 30 && abs(CleanJet_eta)< 0.8 && Jet_hadronFlavour[CleanJet_jetIdx]==0',
    'range':(2,0,2),
    'xaxis':'Bin',
    'fold':0

}
variables['udsg_pt30to40_abseta0to0.8']={
    'name' : 'CleanJet_pt > 30 && CleanJet_pt<= 40 && abs(CleanJet_eta)<0.8 && Jet_hadronFlavour[CleanJet_jetIdx]==0',
    'range':(2,0,2),
    'xaxis':'Bin',
    'fold':0

}
variables['udsg_pt40to60_abseta0to0.8']={
    'name' : 'CleanJet_pt > 40 && CleanJet_pt<=60 && abs(CleanJet_eta)<0.8 && Jet_hadronFlavour[CleanJet_jetIdx]==0',
    'range':(2,0,2),
    'xaxis':'Bin',
    'fold':0

}
variables['udsg_pt60toINF_abseta0to0.8']={
    'name' : 'CleanJet_pt > 60 && abs(CleanJet_eta)<0.8 && Jet_hadronFlavour[CleanJet_jetIdx]==0',
    'range':(2,0,2),
    'xaxis':'Bin',
    'fold':0

} 


variables['udsg_pt20to30_abseta0.8to1.6']={
    'name' : 'CleanJet_pt > 20 && CleanJet_pt<= 30 && abs(CleanJet_eta)>=0.8 && abs(CleanJet_eta)<1.6 && Jet_hadronFlavour[CleanJet_jetIdx]==0',
    'range':(2,0,2),
    'xaxis':'Bin',
    'fold':0

}
variables['udsg_pt30to40_abseta0.8to1.6']={
    'name' : 'CleanJet_pt > 30 && CleanJet_pt<=40 && abs(CleanJet_eta)>=0.8 && abs(CleanJet_eta)<1.6 && Jet_hadronFlavour[CleanJet_jetIdx]==0',
    'range':(2,0,2),
    'xaxis':'Bin',
    'fold':0

}
variables['udsg_pt40to60_abseta0.8to1.6']={
    'name' : 'CleanJet_pt > 40 && CleanJet_pt<=60 && abs(CleanJet_eta)>=0.8 && abs(CleanJet_eta)<1.6 && Jet_hadronFlavour[CleanJet_jetIdx]==0',
    'range':(2,0,2),
    'xaxis':'Bin',
    'fold':0

}
variables['udsg_pt60toINF_abseta0.8to1.6']={
    'name' : 'CleanJet_pt > 60 && abs(CleanJet_eta)>=0.8 && abs(CleanJet_eta)<1.6 && Jet_hadronFlavour[CleanJet_jetIdx]==0',
    'range':(2,0,2),
    'xaxis':'Bin',
    'fold':0

}



variables['udsg_pt20to30_abseta1.6to2.5']={
    'name' : 'CleanJet_pt >20 && CleanJet_pt<=30 && abs(CleanJet_eta)>=1.6 && abs(CleanJet_eta)<2.5 && Jet_hadronFlavour[CleanJet_jetIdx]==0',
    'range':(2,0,2),
    'xaxis':'Bin',
    'fold':0

}
variables['udsg_pt30to40_abseta1.6to2.5']={
    'name' : 'CleanJet_pt >30  && CleanJet_pt<=40 && abs(CleanJet_eta)>=1.6 && abs(CleanJet_eta)<2.5 && Jet_hadronFlavour[CleanJet_jetIdx]==0',
    'range':(2,0,2),
    'xaxis':'Bin',
    'fold':0

}
variables['udsg_pt40to60_abseta1.6to2.5']={
    'name' : 'CleanJet_pt >40  && CleanJet_pt<=60 && abs(CleanJet_eta)>=1.6 && abs(CleanJet_eta)<2.5 && Jet_hadronFlavour[CleanJet_jetIdx]==0',
    'range':(2,0,2),
    'xaxis':'Bin',
    'fold':0

}
variables['udsg_pt60toINF_abseta1.6to2.5']={
    'name' : 'CleanJet_pt >60 && abs(CleanJet_eta)>=1.6 && abs(CleanJet_eta)<2.5 && Jet_hadronFlavour[CleanJet_jetIdx]==0',
    'range':(2,0,2),
    'xaxis':'Bin',
    'fold':0

}

#variables['bjet_'+bAlgo]={
#    'name' : 'Jet_btag'+bAlgo+'[CleanJet_jetIdx[BJetResolved_cjidx]]',
#    'range':(25,0,1),
#    'xaxis':'bjet_'+bAlgo,
#    'fold':0
#
#}



print "len(variables)=",len(variables)
