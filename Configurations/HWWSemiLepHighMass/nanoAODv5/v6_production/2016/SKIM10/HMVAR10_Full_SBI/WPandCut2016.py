import os
##---
#/cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Configurations/HWWSemiLepHighMass
configurations = '%s/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/data/' % os.getenv('CMSSW_BASE')
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
WTAG="HP40"

SFweight='puWeight*EMTFbug_veto*PrefireWeight*trigWeight*LepWPweight*LepWPCut*btagSF*PUJetIdSF*tau21SFnom'

tau21SF=str(WJID['2016'][WTAG]['effSF']['nom'])
tau21SFup=str(WJID['2016'][WTAG]['effSF']['up'])
tau21SFdown=str(WJID['2016'][WTAG]['effSF']['down'])

jetptmin=str(JETCUTS['2016']['ptmin'])
jetetamax=str(JETCUTS['2016']['etamax'])

MELA_MASS_BOOST=[400,900,1500]
MELA_MASS_BOOST=[1500]
MELA_C_BOOST=['1','0.1','0.01','0.001','0.0001','0.00001','0.000001','0.0000001','0.00000001']
MELA_C_BOOST=['0.0001']
MELA_MASS_BOOST_WP=1500
MELA_C_BOOST_WP='0.0001'

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
model='RelW0.02'
