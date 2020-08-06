#ONLY_FINALCUT=True
import os
import sys
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/../')

#-----Variable Deinition-----#
from WPandCut2016 import *
print "ONLY_FINALCUT=",ONLY_FINALCUT
_ALGO="_"+ALGO
_ALGO_="_"+ALGO+"_"


cuts={}
#opt.cutsFile=''

if 'opt' in globals():
    configration_py=opt.cutsFile
else:
    configration_py=sys.argv[0]
print "configration_py=",configration_py


LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
#LepCut="(  Lepton_pt[0]>30 \
#&& ( fabs(Lepton_eta[0])  < 2.5*(abs(Lepton_pdgId[0])==11) \
#||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
#&& ( ( Alt$( Lepton_isLoose[1]*Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
#||   ( Alt$( Lepton_isLoose[1]*Lepton_pt[1],-1) < 10*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
#)\
#)"
LepCut="((Lepton_pt[0]>30) && (fabs(Lepton_eta[0]) < 2.5  ) && (  Alt$(Lepton_isLoose[1]*Lepton_pt[1],-1) < 10 )  )"
LepPtCut='(Lepton_pt[0] > ('+elePtCut+'*(abs(Lepton_pdgId[0])==11) + '+muPtCut+'*(abs(Lepton_pdgId[0])==13)) )'



#------End of Variable Definition-----#
#supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut+'&&isFatJetEvent[0]'
supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut
METtype="PuppiMET"
#met>30
supercut +='&&(!isFinalBoostSR) &&(isResol'+_ALGO_+'nom)'

##---Lepton Categorization---##



LepCats={}
if 'ele' in configration_py:
    LepCats['eleCH']='(Lepton_isTightElectron_'+eleWP+'[0]>0.5)'
elif 'mu' in configration_py:
    LepCats['muCH']='(Lepton_isTightMuon_'+muWP+'[0]>0.5)'
else:
    LepCats={
        '_':'1',
        'eleCH':'(Lepton_isTightElectron_'+eleWP+'[0]>0.5)',
        'muCH':'(Lepton_isTightMuon_'+muWP+'[0]>0.5)',
    }

##-----Basic categorization-----##

ResolvedProdCats={}
ResolvedProdCats['ResolvedGGF']='(isResol'+_ALGO_+'nom && !isVBF_Resol'+_ALGO_+'nom)'
ResolvedProdCats['ResolvedVBF']='(isResol'+_ALGO_+'nom && isVBF_Resol'+_ALGO_+'nom)'
ResolvedProdCats['ResolvedALL']='(isResol'+_ALGO_+'nom)'

if 'GGF' in configration_py :
    ResolvedProdCats={}
    ResolvedProdCats['ResolvedGGF']='(isResol'+_ALGO_+'nom && !isVBF_Resol'+_ALGO_+'nom)'
if 'VBF' in configration_py :
    ResolvedProdCats={}
    ResolvedProdCats['ResolvedVBF']='(isResol'+_ALGO_+'nom && isVBF_Resol'+_ALGO_+'nom)'
if 'ALL' in configration_py :
    ResolvedProdCats={}
    ResolvedProdCats['ResolvedALL']='(isResol'+_ALGO_+'nom)'
    

ResolvedRegionCats={}
##--type in kin var module'_
#nBJetResol_dM_nom
#nBJetResol'+_ALGO_+'nom
#nBJetResNotVBF_dM_nom
#if 'SR' in configration_py :
ResolvedRegionCats['SR'] = '(nBJetResol'+_ALGO_+'nom == 0) && isResolSR'+_ALGO_+'nom'
#if 'SB' in configration_py :
ResolvedRegionCats['SB'] = '(nBJetResol'+_ALGO_+'nom == 0) && isResolSB'+_ALGO_+'nom'
#if 'TOP' in configration_py :
#ResolvedRegionCats['TOP'] = '(nBJetResol'+_ALGO_+'nom > 0) && isResol'+_ALGO_+'nom'
ResolvedRegionCats['TOP'] = '(nBJetResol'+_ALGO_+'nom > 0) && isResolSR'+_ALGO_+'nom'

if 'SR' in configration_py :
    ResolvedRegionCats={}
    ResolvedRegionCats={'SR':'(nBJetResol'+_ALGO_+'nom == 0) && isResolSR'+_ALGO_+'nom'}
if 'SB' in configration_py:
    ResolvedRegionCats={}
    ResolvedRegionCats['SB'] = '(nBJetResol'+_ALGO_+'nom == 0) && isResolSB'+_ALGO_+'nom'
if 'TOP' in configration_py:
    ResolvedRegionCats={}
    #ResolvedRegionCats['TOP'] = '(nBJetResol'+_ALGO_+'nom > 0) && isResol'+_ALGO_+'nom'
    ResolvedRegionCats['TOP'] = '(nBJetResol'+_ALGO_+'nom > 0) && isResolSR'+_ALGO_+'nom'
if 'ALL' in configration_py:
    ResolvedRegionCats={}
    #ResolvedRegionCats['TOP'] = '(nBJetResol'+_ALGO_+'nom > 0) && isResol'+_ALGO_+'nom'
    ResolvedRegionCats['ALL'] = '( isResol'+_ALGO_+'nom)'






ResolvedMETCat={}
if not ONLY_FINALCUT : ResolvedMETCat['NoMET']='1'
ResolvedMETCat['METOver30']='('+METtype+'_nom_pt >'+METcutRes+')' ##PuppiMET_nom_pt




ResolvedPtOverMCats = {}
if not ONLY_FINALCUT:ResolvedPtOverMCats['NoPtOverMcut'] = '1'
if 'ALL' in configration_py:
    ResolvedPtOverMCats = {}
    ResolvedPtOverMCats['ALL']='(1)'
ResolvedPtOverMCats['PtOverM035'] = '(lnjj'+_ALGO_+'nom_minPtWOverM>0.35)'

ResolvedWlepMtCats = {}
if not ONLY_FINALCUT:ResolvedWlepMtCats['NoWlepMtcut'] = '1'
if 'ALL' in configration_py:
    ResolvedWlepMtCats = {}
    ResolvedWlepMtCats['ALL'] = '(1)'
ResolvedWlepMtCats['WlepMtOver50'] = '(Wlep_nom_Mt > 50)'

ResolvedWWMtCats={}
if not ONLY_FINALCUT:ResolvedWWMtCats['NoWWMtOvercut']='1'
if 'ALL' in configration_py:
    ResolvedWWMtCats={}
    ResolvedWWMtCats['ALL']='(1)'
ResolvedWWMtCats['WWMtOver60']='(lnjj'+_ALGO_+'nom_Mt > 60)'

ScoreCats={}
#if not ONLY_FINALCUT : 
ScoreCats['ScoreALL']='(1)'
ScoreCats['Score0To30']='(Whad'+_ALGO_+'nom_ScoreToLeast<30)'
if not ONLY_FINALCUT : ScoreCats['Score30ToInf']='(Whad'+_ALGO_+'nom_ScoreToLeast>30)'

ResolvedMEKDCat={}
ResolvedMEKDCat['_']='1'
ResolvedMEKDCat['MEKDTAG']='(MEKD_Res_C_'+MELA_C_RESOL_WP+'_M'+str(MELA_MASS_RESOL_WP)+"> 0.5)"
ResolvedMEKDCat['UNTAGGED']='(MEKD_Res_C_'+MELA_C_RESOL_WP+'_M'+str(MELA_MASS_RESOL_WP)+"< 0.5)"
if 'ALL' in configration_py:
    ResolvedMEKDCat={}
    ResolvedMEKDCat['ALL']='(1)'

for LepCut in LepCats:
    for ProdCut in ResolvedProdCats:
        for RegionCut in ResolvedRegionCats:
            for METCut in ResolvedMETCat:
                for PtOvMCut in ResolvedPtOverMCats:
                    for WlepMtCut in ResolvedWlepMtCats:
                        for WWMtCut in ResolvedWWMtCats:
                            for ScoreCut in ScoreCats:
                                if 'VBF' in ProdCut:
                                    cuts[LepCut+'__'+ProdCut+'__'+RegionCut+'__'+METCut+'__'+PtOvMCut+'__'+WlepMtCut+'__'+WWMtCut+'__'+ScoreCut] = LepCats[LepCut]\
                                                         +'&&'+ResolvedProdCats[ProdCut]\
                                                         +'&&'+ResolvedRegionCats[RegionCut]\
                                                         +'&&'+ResolvedMETCat[METCut]\
                                                         +'&&'+ResolvedPtOverMCats[PtOvMCut]\
                                                         +'&&'+ResolvedWlepMtCats[WlepMtCut]\
                                                         +'&&'+ResolvedWWMtCats[WWMtCut]\
                                                         +'&&'+ScoreCats[ScoreCut]

                                else:
                                    for MEKDCut in ResolvedMEKDCat:
                                        cuts[LepCut+'__'+ProdCut+'__'+RegionCut+'__'+METCut+'__'+PtOvMCut+'__'+WlepMtCut+'__'+WWMtCut+'__'+ScoreCut+'__'+MEKDCut] = LepCats[LepCut]\
                                                         +'&&'+ResolvedProdCats[ProdCut]\
                                                         +'&&'+ResolvedRegionCats[RegionCut]\
                                                         +'&&'+ResolvedMETCat[METCut]\
                                                         +'&&'+ResolvedPtOverMCats[PtOvMCut]\
                                                         +'&&'+ResolvedWlepMtCats[WlepMtCut]\
                                                         +'&&'+ResolvedWWMtCats[WWMtCut]\
                                                         +'&&'+ScoreCats[ScoreCut]\
                                                         +'&&'+ResolvedMEKDCat[MEKDCut]
                                        

#cuts['isVBF']='isVBF'
print "Ncuts=",len(cuts)

