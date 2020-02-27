#-----Variable Deinition-----#
from WPandCut2017 import *



LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepCut="(  Lepton_pt[0]>30 \
&& ( fabs(Lepton_eta[0])  < 2.1*(abs(Lepton_pdgId[0])==11) \
||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
&& ( ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
||   ( Alt$( Lepton_pt[1],-1) < 10*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
)\
)"
LepPtCut='(Lepton_pt[0] > (38*(abs(Lepton_pdgId[0])==11) + 27*(abs(Lepton_pdgId[0])==13)) )'



#------End of Variable Definition-----#
#supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut+'&&isFatJetEvent[0]'
supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut
METtype="PuppiMET"


##---Lepton Categorization---##

BoostedCats={
#'_':'1',
'IsResolved':'isResolved[0]',
#'NotFatJetEvent':'!isFatJetEvent[0]',

}

LepCats={
     #'_':'1',
    'eleCH':'(Lepton_isTightElectron_'+eleWP+'[0]>0.5)',
    'muCH':'(Lepton_isTightMuon_'+muWP+'[0]>0.5)',
}

NjetCats={
    '_':'1',
    #'0j':'zeroJet',
    #'1j':'oneJet',
    #'2j':'twoJet'
}

METCats={
    #'_':'1',
    #METtype+'0To40':'('+METtype+"_pt"+'<40)',
    METtype+'30ToInf':'('+METtype+'_pt'+'>40)',

}

PtOverMWWCats={
    '_':'1',
    'PtOverMWW0p4ToInf':'WptOverMWW > 0.3',
}


BTAGCats={
    #'_':'1',
    #'SR':'(NBJet==0 &&( WFatJet_mass > 65 && WFatJet_mass < 105))',
    #'SB':'(NBJet==0 &&( WFatJet_mass < 65 || WFatJet_mass > 105))',
    #'1b':'(NBJet==1)',
    #'2b':'(NBJet==2)',
    #'Top':'(NBJet>0 && ( WFatJet_mass > 65 && WFatJet_mass < 105))'
    '0b':'(NBJet==0)',
    'btag':'(NBJet>0)',    
    
}

MjjCats={
    'Mjj65To105':'(NBJet==0 &&( WResolved_mass > 65 && WResolved_mass < 105))',
    'MjjSB':'(NBJet==0 &&( WResolved_mass < 65 || WResolved_mass > 105))',
    
   
}

VBFCats={
    '_':'1',
    'isVBF':'isVBF',
    'ggH':'!isVBF'
}
#---Not used---##
MTCats={
    '_':'1',
    #'MT0To40':'(Mt[0]<=40)',
    'MT040ToInf':'(Mt[0]>40)',
}




for Boost in BoostedCats:
    for Lep in LepCats: 
        for METcut in METCats:
            for NJcut in NjetCats:
                for NBJcut in BTAGCats:
                    for VBFcut in VBFCats:
                        for PtOvMWWcut in PtOverMWWCats:
                            cuts[Boost+'__'+Lep+'__'+METcut+'__'+NJcut+'__'+NBJcut+'__'+VBFcut+'__'+PtOvMWWcut]=\
                            BoostedCats[Boost]\
                            +'&&'+LepCats[Lep]\
                            +'&&'+METCats[METcut]\
                            +'&&'+NjetCats[NJcut]\
                            +'&&'+BTAGCats[NBJcut]\
                            +'&&'+VBFCats[VBFcut]\
                            +'&&'+PtOverMWWCats[PtOvMWWcut]


print "Ncuts=",len(cuts)

            
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
