import os
import sys
sys.path.append(os.getcwd())

##---Setting Flags

FilesPerJob=30
FilesPerJobMainBKG=2
FilesPerJobDATA=100

elePtBins=[0., 30.,32.,33.,34., 35., 36.,37.,38.,40.,42.,45.,50., 60., 100., 200.,]
eleEtaBins=[-2.5, -2.1, -1.570, -1.440, -0.800, 0., 0.800, 1.440, 1.570, 2.100, 2.500]

configurations = '%s/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/data/' % os.getenv('CMSSW_BASE')
xrootdPath = 'root://cms-xrdr.private.lo:2094'
treeBaseDir = "/xrootd/store/user/jhchoi/Latino/HWWNano/"
##--Set Campaign and Step--##
CAMPAIGN='Autumn18_102X_nAODv6_Full2018v6'
STEP="MCl1loose2018v6__MCCorr2018v6"

CAMPAIGN_DATA='Run2018_102X_nAODv6_Full2018v6'
STEP_DATA="DATAl1loose2018v6"

directory=treeBaseDir+CAMPAIGN+'/'+STEP

##----WP
Year='2018'
eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'
##---SF & Weight to use
SFweight='puWeight*EMTFbug_veto*LepWPCut[0]*LepWPweight[0]'
