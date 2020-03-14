#-----Variable Deinition-----#
from WPandCut2018 import *
import sys
#cuts={}


scriptname=opt.cutsFile

LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepCut="(  Lepton_pt[0]>30 \
&& ( fabs(Lepton_eta[0])  < 2.1*(abs(Lepton_pdgId[0])==11) \
||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
&& ( ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
||   ( Alt$( Lepton_pt[1],-1) < 10*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
)\
)"
LepPtCut='(Lepton_pt[0] > ('+elePtCut+'*(abs(Lepton_pdgId[0])==11) + '+muPtCut+'*(abs(Lepton_pdgId[0])==13)) )'



#------End of Variable Definition-----#
#supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut+'&&isFatJetEvent[0]'
supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut
METtype="PuppiMET"


##---Lepton Categorization---##



LepCats={}
if 'ele' in scriptname:
    LepCats['eleCH']='(Lepton_isTightElectron_'+eleWP+'[0]>0.5)'
elif 'mu' in scriptname:
    LepCats['muCH']='(Lepton_isTightMuon_'+muWP+'[0]>0.5)'
else:
    LepCats={
        #'_':'1',
        'eleCH':'(Lepton_isTightElectron_'+eleWP+'[0]>0.5)',
        'muCH':'(Lepton_isTightMuon_'+muWP+'[0]>0.5)',
    }

##-----Basic categorization-----##

ResolvedProdCats={
    'Resolved':'!isBoosted && isResolved',
    'ResolvedGGF':'!isBoosted && isResolved && !isVBF_Resolved',
    'ResolvedVBF':'!isBoosted && isResolved && isVBF_Resolved',
}
ResolvedRegionCats={}
##--type in kin var module
ResolvedRegionCats['SR'] = '(nBJetResolved == 0) && (Whad_mass > 65) && (Whad_mass < 105)' ##nBJetResolved_cjidx => nBJetResolved
ResolvedRegionCats['SB'] = '(nBJetResolved == 0) && ((Whad_mass < 65) || (Whad_mass > 105))'
ResolvedRegionCats['Top'] = '(nBJetResolved > 0)'

ResolvedPtOverMCats = {}
ResolvedPtOverMCats['NoPtOverMcut'] = '1'
ResolvedPtOverMCats['PtOverM035'] = 'minPtWOverMlnjj>0.35'

ResolvedWlepMtCats = {}
ResolvedWlepMtCats['NoWlepMtcut'] = '1'
ResolvedWlepMtCats['WlepMtOver50'] = 'Wlep_Mt > 50'

ResolvedWWMtCats={}
ResolvedWWMtCats['WWMtOver50']='lnjj_Mt > 50'

for LepCut in LepCats:
    for ProdCut in ResolvedProdCats:
        for RegionCut in ResolvedRegionCats:
            for PtOvMCut in ResolvedPtOverMCats:
                for WlepMtCut in ResolvedWlepMtCats:
                    for WWMtCut in ResolvedWWMtCats:
                        cuts[LepCut+'__'+ProdCut+'__'+RegionCut+'__'+PtOvMCut+'__'+WlepMtCut+'__'+WWMtCut] = LepCats[LepCut]\
                                                         +'&&'+ResolvedProdCats[ProdCut]\
                                                         +'&&'+ResolvedRegionCats[RegionCut]\
                                                         +'&&'+ResolvedPtOverMCats[PtOvMCut]\
                                                         +'&&'+ResolvedWlepMtCats[WlepMtCut]\
                                                         +'&&'+ResolvedWWMtCats[WWMtCut]
                    

#cuts['isVBF']='isVBF'
print "Ncuts=",len(cuts)

