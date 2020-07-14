import os
##---
#/cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Configurations/HWWSemiLepHighMass
configurations = '%s/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/data/' % os.getenv('CMSSW_BASE')
os.system('cp '+configurations+'/Wtagger_cfg.py .')
os.system('cp '+configurations+'/Wjjtagger_cfg.py .')

from Wtagger_cfg import WJID
from Wjjtagger_cfg import MYALGO,JETCUTS
Year='2018'
eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'

xrootdPath = 'root://cms-xrdr.private.lo:2094'
treeBaseDir = "/xrootd/store/user/jhchoi/Latino/HWWNano/"

CAMPAIGN='Autumn18_102X_nAODv6_Full2018v6'
STEP="MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__HMFull_V11_nom/"
CAMPAIGN_DATA='Run2018_102X_nAODv6_Full2018v6'
STEP_DATA="DATAl1loose2018v6__HMSemilepSKIMv6_10_data__HMFull_V11_data/"



btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_102XSF_V1.csv' % os.getenv('CMSSW_BASE')
bAlgo='DeepB'
bWP='0.1241'


elePtCut='35'
muPtCut='27'

ALGO="dMchi2Resolution"
#WTAG="DeepAK8WP5MD"
WTAG="DeepAK8WP2p5"

SFweight='puWeight*trigWeight[0]*EMTFbug_veto*LepWPCut[0]*LepWPweight[0]*btagSF*PUJetIdSF*HEMweight'

#SFweight+='*WtaggerSFnom'

WtaggerSF=str(WJID['2018'][WTAG]['effSF']['nom']).replace('WtaggerFatjet_'+WTAG+'_nom_pt','Alt$(WtaggerFatjet_'+WTAG+'_nom_pt,0)')
WtaggerSFup=str(WJID['2018'][WTAG]['effSF']['up']).replace('WtaggerFatjet_'+WTAG+'_nom_pt','Alt$(WtaggerFatjet_'+WTAG+'_nom_pt,0)')
WtaggerSFdown=str(WJID['2018'][WTAG]['effSF']['down']).replace('WtaggerFatjet_'+WTAG+'_nom_pt','Alt$(WtaggerFatjet_'+WTAG+'_nom_pt,0)')

jetptmin=str(JETCUTS['2018']['ptmin'])
jetetamax=str(JETCUTS['2018']['etamax'])

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
#model='RelW0.02'
model='cprime1.0BRnew0.0'

##--Setup
UseRegroupJES=False
CombineMultiV=False ##Turn off when making shapes and combing multiv/ Turn on when mkRuncards, plotting
MultiV=['WW','WZ','ZZ','WWW','WWZ','WZZ','ZZZ',]
CombineH125=False
H125=['ZHWWlnuqq_M125','WpHWWlnuqq_M125','WmHWWlnuqq_M125',
       'ggHtautaulnuqq_M125','vbfHtautaulnuqq_M125','WmHtautaulnuqq_M125','WpHtautaulnuqq_M125','ZHtautaulnuqq_M125']
CombineWjets=False
Wjets=['Wjets0j','Wjets1j','Wjets2j']
Combine_qqWWqq=False
qqWWqq=['WWJJ','vbfHWWlnuqq_M125']
Combine_ggWW=False
CombineSBI=False
