import os
import sys
sys.path.append(os.getcwd())

##---
#/cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Configurations/HWWSemiLepHighMass
configurations = '%s/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/data/' % os.getenv('CMSSW_BASE')

os.system('cp '+configurations+'/Wtagger_cfg.py .')
os.system('cp '+configurations+'/Wjjtagger_cfg.py .')


#from Wtagger_cfg import WJID
#from Wjjtagger_cfg import MYALGO,JETCUTS
handle=open('Wtagger_cfg.py','r')
exec(handle)
handle.close()
handle=open('Wjjtagger_cfg.py','r')
exec(handle)
handle.close()
Year='2017'
eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'

btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_94XSF_V2_B_F.csv' % os.getenv('CMSSW_BASE')
bAlgo='DeepB'
bWP='0.1522'


elePtCut='38'
muPtCut='30'

ALGO="dMchi2Resolution"
WTAG="DeepAK8WP5"
#WTAG="HP45"

SFweight='puWeight*trigWeight*EMTFbug_veto*PrefireWeight*LepWPweight*LepWPCut*btagSF*PUJetIdSF'
#if 'HP' in WTAG: SFweight+="*tau21SFnom"
#if 'DeepAK8' in WTAG: SFweight+="*deepAK8SFnom"
SFweight+='*WtaggerSFnom'


WtaggerSF=str(WJID['2017'][WTAG]['effSF']['nom']).replace('WtaggerFatjet_'+WTAG+'_nom_pt','Alt$(WtaggerFatjet_'+WTAG+'_nom_pt,0)')
WtaggerSFup=str(WJID['2017'][WTAG]['effSF']['up']).replace('WtaggerFatjet_'+WTAG+'_nom_pt','Alt$(WtaggerFatjet_'+WTAG+'_nom_pt,0)')
WtaggerSFdown=str(WJID['2017'][WTAG]['effSF']['down']).replace('WtaggerFatjet_'+WTAG+'_nom_pt','Alt$(WtaggerFatjet_'+WTAG+'_nom_pt,0)')


jetptmin=str(JETCUTS['2017']['ptmin'])
jetetamax=str(JETCUTS['2017']['etamax'])

MELA_MASS_BOOST=[400,900,1500]
MELA_MASS_BOOST=[1500]
MELA_C_BOOST=['1','0.1','0.01','0.001','0.0001','0.00001','0.000001','0.0000001','0.00000001']
MELA_C_BOOST=['0.000001']
MELA_MASS_BOOST_WP=1500
MELA_C_BOOST_WP='0.000001'

MELA_MASS_RESOL=[200,400]
MELA_MASS_RESOL=[400]
MELA_C_RESOL=['1','0.1','0.01','0.001','0.0001','0.00001','0.000001','0.0000001','0.00000001']
MELA_C_RESOL=['0.00001']
MELA_MASS_RESOL_WP=400
MELA_C_RESOL_WP='0.00001'


METtype="PuppiMET"
METcutBst='40'
METcutRes='30'

##---MELA S/B/I reweight
model='RelW0.02'


##---
