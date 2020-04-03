#import my.Wlep_sel
#import my.final_fatjetsel



#supercut = 'nCleanFatJet==1'



#-----Variable Deinition-----#




eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'
Year='2017'


LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepCut="(  Lepton_pt[0]>30 \
&& ( fabs(Lepton_eta[0])  < 2.1*(abs(Lepton_pdgId[0])==11) \
||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
&& ( ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
||   ( Alt$( Lepton_pt[1],-1) < 10*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
)\
)"
LepPtCut='(Lepton_pt[0] > 38*(abs(Lepton_pdgId[0])==11))'




#------End of Variable Definition-----#
supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut

LepCats={}
LepCats['']='(1)'
#LepCats['ElectronCh']='(abs(Lepton_pdgId[0])==11)'
#LepCats['MuonCh']='(abs(Lepton_pdgId[0])==13)'


ProcCats={}
#ProcCats['BoostVbfSR']   ='BoostVbfSR'
ProcCats['BoostNoVbfSR'] ='BoostNoVbfSR'
#ProcCats['ResolVbfSR']   ='ResolVbfSR && !BoostVbfSR && !BoostNoVbfSR'
ProcCats['ResolNoVbfSR'] ='ResolNoVbfSR && !BoostVbfSR && !BoostNoVbfSR'
    


for Lep in LepCats:
    for process in ProcCats: 
        cuts[Lep+process+Year]=\
                LepCats[Lep]\
	        +'&&'+ProcCats[process]

