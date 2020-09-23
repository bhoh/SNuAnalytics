import os
import sys
sys.path.append(os.getcwd())

##---Setting Flags

FilesPerJob=30
FilesPerJobMainBKG=2
FilesPerJobDATA=100

##---
#/cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Configurations/HWWSemiLepHighMass
configurations = '%s/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/data/' % os.getenv('CMSSW_BASE')
xrootdPath = 'root://cms-xrdr.private.lo:2094'
treeBaseDir = "/xrootd/store/user/jhchoi/Latino/HWWNano/"
##--Set Campaign and Step--##
CAMPAIGN='Summer16_102X_nAODv5_Full2016v6'
#STEP="MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_V11_nom"
STEP="MCl1loose2016v6__MCCorr2016v6"

CAMPAIGN_DATA='Run2016_102X_nAODv5_Full2016v6'
#STEP_DATA="DATAl1loose2016v6__HMSemilepSKIMv6_10_data__HMFull_V11_data"
STEP_DATA="DATAl1loose2016v6"

directory=treeBaseDir+CAMPAIGN+'/'+STEP

##----WP
Year='2016'
eleWP='mva_90p_Iso2016'
muWP='cut_Tight80x'
##---Btag


##---SF & Weight to use
SFweight='puWeight*EMTFbug_veto*PrefireWeight**LepWPweight[0]*LepWPCut[0]'
