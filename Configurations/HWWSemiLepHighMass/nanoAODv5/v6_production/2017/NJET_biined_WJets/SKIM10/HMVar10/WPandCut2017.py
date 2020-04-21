import os
##---
#/cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Configurations/HWWSemiLepHighMass
configurations = '%s/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/data/' % os.getenv('CMSSW_BASE')
os.system('cp '+configurations+'/Wtagger_cfg.py .')
os.system('cp '+configurations+'/Wjjtagger_cfg.py .')

from Wtagger_cfg import WJID
from Wjjtagger_cfg import MYALGO,JETCUTS
Year='2017'
eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'

bAlgo='DeepB'
bWP='0.1522'


elePtCut='38'
muPtCut='30'

ALGO="dMchi2Resolution"
WTAG="HP45"

tau21SF=str(WJID['2017'][WTAG]['effSF']['nom'])
tau21SFup=str(WJID['2017'][WTAG]['effSF']['up'])
tau21SFdown=str(WJID['2017'][WTAG]['effSF']['down'])

jetptmin=str(JETCUTS['2017']['ptmin'])
jetetamax=str(JETCUTS['2017']['etamax'])

MELA_MASS_BOOST=[400,900,1500]
MELA_MASS_RESOL=[200,400]


METtype="PuppiMET"
METcutBst='40'
METcutRes='30'
