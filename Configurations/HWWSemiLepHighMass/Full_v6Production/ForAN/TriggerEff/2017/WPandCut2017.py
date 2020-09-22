import os
import sys
sys.path.append(os.getcwd())

##---Setting Flags
###--nuisance

##---shape submission
FilesPerJob=30
FilesPerJobMainBKG=2
FilesPerJobDATA=100
##---
elePtBins=[0., 30., 35., 36.,37.,38.,40.,42.,45.,50.,65.,70.,80.,100.,200.,]
eleEtaBins=[-2.5, -2.1, -1.570, -1.440, -0.800, 0., 0.800, 1.440, 1.570, 2.100, 2.500]
#/cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Configurations/HWWSemiLepHighMass
configurations = '%s/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/data/' % os.getenv('CMSSW_BASE')
xrootdPath = 'root://cms-xrdr.private.lo:2094'
treeBaseDir = "/xrootd/store/user/jhchoi/Latino/HWWNano/"
##--Set Campaign and Step--##
CAMPAIGN='Fall2017_102X_nAODv5_Full2017v6'
#STEP="MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_V11_nom"
STEP="MCl1loose2017v6__MCCorr2017v6"

CAMPAIGN_DATA='Run2017_102X_nAODv5_Full2017v6'
#STEP_DATA="DATAl1loose2017v6__HMSemilepSKIMv6_10_data__HMFull_V11_data"
STEP_DATA="DATAl1loose2017v6"

directory=treeBaseDir+CAMPAIGN+'/'+STEP


##----WP
Year='2017'
eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'

##---SF & Weight to use
SFweight='puWeight*EMTFbug_veto*PrefireWeight*LepWPweight[0]*LepWPCut[0]'
