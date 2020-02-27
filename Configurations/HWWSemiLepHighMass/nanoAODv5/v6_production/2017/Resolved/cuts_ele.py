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
METtype="PuppiMET"


##---Lepton Categorization---##
LepCats={
    #'':'1',
    'eleCH':'(Lepton_isTightElectron_'+eleWP+'[0]>0.5)',
    #'muCH':'(Lepton_isTightMuon_'+muWP+'[0]>0.5)',
}

NjetCats={
    '':'1',
    '0j':'zeroJet',
    '1j':'oneJet',
    '2j':'twoJet'
}

METCats={
    '':'1',
    METtype+'0To50':'('+METtype+"_pt"+'<50)',
    METtype+'50ToInf':'('+METtype+'_pt'+'>=50)',

}

for Lep in LepCats:
    for METcut in METCats:
        for NJcut in NjetCats:
            cuts[Lep+'__'+METcut+'__'+NJcut]=LepCats[Lep]\
                                              +'&&'+METCats[METcut]\
                                              +'&&'+NjetCats[NJcut]
    
'''


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
            #if Lep=='ElectronCh':
            #    cuts[Lep+RProcCat+RCat]+='&&PuppiMET_pt > 100'
        
'''
