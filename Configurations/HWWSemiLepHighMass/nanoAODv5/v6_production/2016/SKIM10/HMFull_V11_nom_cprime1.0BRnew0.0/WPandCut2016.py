import os
##---
#/cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Configurations/HWWSemiLepHighMass
configurations = '%s/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/data/' % os.getenv('CMSSW_BASE')
SITE=os.uname()[1]
xrootdPath=''
if    'iihe' in SITE :
  xrootdPath  = 'dcap://maite.iihe.ac.be/'
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/'
elif  'cern' in SITE :
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'
elif  'sdfarm' in SITE:
  xrootdPath = 'root://cms-xrdr.private.lo:2094'
  treeBaseDir = "/xrootd/store/user/jhchoi/Latino/HWWNano/"

CAMPAIGN='Summer16_102X_nAODv5_Full2016v6'
STEP="MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_V11_nom/"


CAMPAIGN_DATA='Run2016_102X_nAODv5_Full2016v6'
STEP_DATA="DATAl1loose2016v6__HMSemilepSKIMv6_10_data__HMFull_V11_data"


directory=treeBaseDir+CAMPAIGN+'/'+STEP




os.system('cp '+configurations+'/Wtagger_cfg.py .')
os.system('cp '+configurations+'/Wjjtagger_cfg.py .')

from Wtagger_cfg import WJID
from Wjjtagger_cfg import MYALGO,JETCUTS
Year='2016'
eleWP='mva_90p_Iso2016'
muWP='cut_Tight80x'

bAlgo='DeepB'
bWP='0.2217'
btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_2016LegacySF_V1.csv' % os.getenv('CMSSW_BASE')

elePtCut='30'
muPtCut='30'

ALGO="dMchi2Resolution"
#WTAG="HP40"
#WTAG="DeepAK8WP5"
WTAG="DeepAK8WP2p5"

SFweight='puWeight*EMTFbug_veto*PrefireWeight*trigWeight*LepWPweight*LepWPCut*btagSF*PUJetIdSF'
#SFweight+='*WtaggerSFnom'

WtaggerSF=str(WJID['2016'][WTAG]['effSF']['nom']).replace('WtaggerFatjet_'+WTAG+'_nom_pt','Alt$(WtaggerFatjet_'+WTAG+'_nom_pt,0)')
WtaggerSFup=str(WJID['2016'][WTAG]['effSF']['up']).replace('WtaggerFatjet_'+WTAG+'_nom_pt','Alt$(WtaggerFatjet_'+WTAG+'_nom_pt,0)')
WtaggerSFdown=str(WJID['2016'][WTAG]['effSF']['down']).replace('WtaggerFatjet_'+WTAG+'_nom_pt','Alt$(WtaggerFatjet_'+WTAG+'_nom_pt,0)')

jetptmin=str(JETCUTS['2016']['ptmin'])
jetetamax=str(JETCUTS['2016']['etamax'])

MELA_MASS_BOOST=[400,900,1500]
MELA_MASS_BOOST=[1500]
MELA_C_BOOST=['1','0.1','0.01','0.001','0.0001','0.00001','0.000001','0.0000001','0.00000001']
MELA_C_BOOST=['0.000001']
MELA_MASS_BOOST_WP=1500
MELA_C_BOOST_WP='0.000001'

MELA_MASS_RESOL=[200,400]
MELA_MASS_RESOL=[400]
MELA_C_RESOL=['1','0.1','0.01','0.001','0.0001','0.00001','0.000001','0.0000001','0.00000001']
MELA_C_RESOL=['0.001']
MELA_MASS_RESOL_WP=400
MELA_C_RESOL_WP='0.001'



METtype="PuppiMET"
METcutBst='40'
METcutRes='30'

##---MELA S/B/I reweight
model='cprime1.0BRnew0.0'
#model='RelW0.02'


##---Setup
UseRegroupJES=False
CombineMultiV=False ##Turn off when making shapes and combing multiv/ Turn on when mkRuncards, plotting
MultiV=['WW','WZ','ZZ','WWW','WWZ','WZZ','ZZZ',]
CombineH125=False
H125=['ZHWWlnuqq_M125','WpHWWlnuqq_M125','WmHWWlnuqq_M125',
       'ggHtautaulnuqq_M125','vbfHtautaulnuqq_M125','WmHtautaulnuqq_M125','WpHtautaulnuqq_M125','ZHtautaulnuqq_M125']


Combine_qqWWqq=False
qqWWqq=['WWJJ','vbfHWWlnuqq_M125']
Combine_ggWW=False
ggWW=['ggHWWlnuqq_M125']
CombineSBI=False


CombineWjets=False
