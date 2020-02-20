#import my.Wlep_sel
#import my.final_fatjetsel



#supercut = 'nCleanFatJet==1'



#-----Variable Deinition-----#



Year='2018'
eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'



LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepPtCut='(Lepton_pt[0] > 35*(abs(Lepton_pdgId[0])==11))'
LepCut="(  Lepton_pt[0]>30 \
&& ( fabs(Lepton_eta[0])  < 2.1*(abs(Lepton_pdgId[0])==11) \
||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
&& ( ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
||   ( Alt$( Lepton_pt[1],-1) < 10*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
)\
)"




#------End of Variable Definition-----#
supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut

LepCats={}
LepCats['']='(1)'
LepCats['ElectronCh']='(abs(Lepton_pdgId[0])==11)'
LepCats['MuonCh']='(abs(Lepton_pdgId[0])==13)'


BoostCats={}
BoostCats['BoostedSR']='IsBoostedSR'
#BoostCats['BoostedSB']='IsBoostedSB'
#BoostCats['BoostedTop']='IsBoostedTopCR'
    
BoostProcCats={}
BoostProcCats['']='1'
BoostProcCats['ggf']='!IsVbfFat'
BoostProcCats['vbf']='IsVbfFat'


ResolveCats={}
ResolveCats['ResolvedSR']='IsResolvedSR&&(nCleanFatJet==0)'
#ResolveCats['ResolvedSB']='IsResolvedSB&&(nCleanFatJet==0)'
#ResolveCats['ResolvedTop']='IsResolvedTopCR&&(nCleanFatJet==0)'
    
ResolveProcCats={}
ResolveProcCats['']='1'
ResolveProcCats['ggf']='!IsVbfjj'
ResolveProcCats['vbf']='IsVbfjj'




##===Define cuts===###
for Lep in LepCats:
    


    for BCat in BoostCats: 
        for BProcCat in BoostProcCats:
            cuts[Lep+BProcCat+BCat+Year]=BoostCats[BCat]\
                +'&&'+BoostProcCats[BProcCat]\
                +'&&'+LepCats[Lep]

    for RCat in ResolveCats: 
        for RProcCat in ResolveProcCats:
            cuts[Lep+RProcCat+RCat+Year]=ResolveCats[RCat]\
                +'&&'+ResolveProcCats[RProcCat]\
                +'&&'+LepCats[Lep]

