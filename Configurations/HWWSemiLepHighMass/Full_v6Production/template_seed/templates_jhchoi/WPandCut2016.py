import os
import sys
sys.path.append(os.getcwd())

##---Setting Flags
###--nuisance
StatOnly=True
UseRegroupJES=False


###--CUT
ONLY_PRESELCUT=False
ONLY_FINALCUT=True

###--Variable setting
OnlyFinalVariable=False


##--Corrections
MjjShapeCorr=True
PowhegNorm=False
##--For QCD norm fitting
DIVIDEQCD=False


##---shape submission
FilesPerJob=30
FilesPerJobMainBKG=2
FilesPerJobDATA=100
if StatOnly:
    FilesPerJobDATA=30

CombineMultiV=False ##Turn off when making shapes and combing multiv/ Turn on when mkRuncards, plotting
MultiV=['WW','WZ','ZZ','WWW','WWZ','WZZ','ZZZ',]
CombineH125=False
H125=['ZHWWlnuqq_M125','WpHWWlnuqq_M125','WmHWWlnuqq_M125', ##HWW
       'ggHtautaulnuqq_M125','vbfHtautaulnuqq_M125','WmHtautaulnuqq_M125','WpHtautaulnuqq_M125','ZHtautaulnuqq_M125', #Htautau
      'vbfHWWlnuqq_M125','ggHWWlnuqq_M125'] ##HWW
CombineWjets=False
Wjets=['Wjets0j','Wjets1j','Wjets2j']
Combine_qqWWqq=False
qqWWqq=['qqWWqq']
Combine_ggWW=False
ggWW=['ggWW']
CombineSBI=False



##---
#/cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Configurations/HWWSemiLepHighMass
configurations = '%s/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/data/' % os.getenv('CMSSW_BASE')
xrootdPath = 'root://cms-xrdr.private.lo:2094'
treeBaseDir = "/xrootd/store/user/jhchoi/Latino/HWWNano/"
##--Set Campaign and Step--##
CAMPAIGN='Summer16_102X_nAODv5_Full2016v6'
STEP="MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_V11_nom"

CAMPAIGN_DATA='Run2016_102X_nAODv5_Full2016v6'
STEP_DATA="DATAl1loose2016v6__HMSemilepSKIMv6_10_data__HMFull_V11_data"

directory=treeBaseDir+CAMPAIGN+'/'+STEP

##---Copy Wtagger Configuration--##
os.system('cp '+configurations+'/Wtagger_cfg.py .')
os.system('cp '+configurations+'/Wjjtagger_cfg.py .')

from Wtagger_cfg import WJID
from Wjjtagger_cfg import MYALGO,JETCUTS

##----WP
Year='2016'
eleWP='mva_90p_Iso2016'
muWP='cut_Tight80x'
##---Btag
btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_2016LegacySF_V1.csv' % os.getenv('CMSSW_BASE')
bAlgo='DeepB'
bWP='0.2217'


elePtCut='30'
muPtCut='30'

ALGO="dMchi2Resolution"
#WTAG="HP40"
#WTAG="DeepAK8WP5"
WTAG="DeepAK8WP2p5"

##---SF & Weight to use
SFweight='puWeight*EMTFbug_veto*PrefireWeight*trigWeight[0]*LepWPweight[0]*LepWPCut[0]*btagSF*PUJetIdSF'


#WtaggerSF=str(WJID['2016'][WTAG]['effSF']['nom']).replace('WtaggerFatjet_'+WTAG+'_nom_pt','Alt$(WtaggerFatjet_'+WTAG+'_nom_pt,0)')
WtaggerSF=str(WJID['2016'][WTAG]['effSF']['nom'])
#WtaggerSFup=str(WJID['2016'][WTAG]['effSF']['up']).replace('WtaggerFatjet_'+WTAG+'_nom_pt','Alt$(WtaggerFatjet_'+WTAG+'_nom_pt,0)')
WtaggerSFup=str(WJID['2016'][WTAG]['effSF']['up'])
#WtaggerSFdown=str(WJID['2016'][WTAG]['effSF']['down']).replace('WtaggerFatjet_'+WTAG+'_nom_pt','Alt$(WtaggerFatjet_'+WTAG+'_nom_pt,0)')
WtaggerSFdown=str(WJID['2016'][WTAG]['effSF']['down'])

jetptmin=str(JETCUTS['2016']['ptmin'])
jetetamax=str(JETCUTS['2016']['etamax'])


##---Mela WP----
MELA_MASS_BOOST=[400,900,1500]
MELA_MASS_BOOST=[1500]
MELA_C_BOOST=['1','0.1','0.01','0.001','0.0001','0.00001','0.000001','0.0000001','0.00000001']
MELA_C_BOOST=['0.000001']
MELA_MASS_BOOST_WP=1500
MELA_C_BOOST_WP='0.000001'

MELA_MASS_RESOL=[200,400]
MELA_MASS_RESOL=[400]
MELA_C_RESOL=['1','0.1','0.01','0.001','0.0001','0.00001','0.000001','0.0000001','0.00000001']
MELA_C_RESOL=['0.000001']
MELA_MASS_RESOL_WP=400
MELA_C_RESOL_WP='0.000001'


##--MET setup
METtype="PuppiMET"
METcutBst='40'
METcutRes='30'

##---MELA signal scenario
model='cprime1.0BRnew0.0'
#model='RelW0.02'



##--QCD list
QCD_MU=['QCD_Pt-15to20_MuEnrichedPt5','QCD_Pt-20toInf_MuEnrichedPt15']
QCD_EM=[
  'QCD_Pt-20to30_EMEnriched',
  'QCD_Pt-30to50_EMEnriched',
  'QCD_Pt-50to80_EMEnriched',
  'QCD_Pt-80to120_EMEnriched',
  'QCD_Pt-120to170_EMEnriched',
  'QCD_Pt-170to300_EMEnriched',
  'QCD_Pt-300toInf_EMEnriched'
]
QCD_bcToE=[
  'QCD_Pt_20to30_bcToE',
  'QCD_Pt_30to80_bcToE',
  'QCD_Pt_80to170_bcToE',
  'QCD_Pt_170to250_bcToE',
  'QCD_Pt_250toInf_bcToE',
]
