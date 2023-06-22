##---
Year='2018'
#eleWP='mvaFall17V1Iso_WP90'
eleWP='POGTight'
#eleWP='cutFall17V1Iso_Tight'
#muWP='cut_Tight_HWWW'
muWP='cut_Tight_POG'

bAlgo='DeepB'
bWP='0.1241'


maxtau21='0.45'
min_jetId='4'
max_jetId='10'

FatSel=['MW','PT']

elePtCut='35'
muPtCut='27'
## double lep pt cut
eePtCut=('35','35') #('26','15') # HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL
mmPtCut=('27','27') #('20','11') # HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8
emPtCut=('35','27') #('26','15') # HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ
mePtCut=('27','35') #('26','15') # HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL
