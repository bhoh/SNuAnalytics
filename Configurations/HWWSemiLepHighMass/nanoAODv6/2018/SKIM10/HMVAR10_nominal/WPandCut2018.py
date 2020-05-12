
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

btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_102XSF_V1.csv' % os.getenv('CMSSW_BASE')
bAlgo='DeepB'
bWP='0.1241'


elePtCut='35'
muPtCut='27'

ALGO="dMchi2Resolution"
WTAG="HP45"

SFweight='puWeight*trigWeight*EMTFbug_veto*LepWPCut*LepWPweight*btagSF*PUJetIdSF*HEMweight*tau21SFnom'

tau21SF=str(WJID['2018'][WTAG]['effSF']['nom'])
tau21SFup=str(WJID['2018'][WTAG]['effSF']['up'])
tau21SFdown=str(WJID['2018'][WTAG]['effSF']['down'])

jetptmin=str(JETCUTS['2018']['ptmin'])
jetetamax=str(JETCUTS['2018']['etamax'])

MELA_MASS_BOOST=[400,900,1500]
MELA_C_BOOST=['1','0.1','0.01','0.001','0.0001','0.00001','0.000001','0.0000001','0.00000001']

MELA_MASS_RESOL=[200,400]
MELA_C_RESOL=['1','0.1','0.01','0.001','0.0001','0.00001','0.000001','0.0000001','0.00000001']


METtype="PuppiMET"
METcutBst='40'
METcutRes='30'
