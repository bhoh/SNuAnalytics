#ONLY_FINALCUT=True

import os
import sys
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/../')


#-----Variable Deinition-----#
from WPandCut2016 import *
print "ONLY_FINALCUT=",ONLY_FINALCUT
cuts={}


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
supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut+' && ((isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0)))'


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



##---Boosted---##
##---common categorization -> GGF/VBF
BoostedProdCats={}
BoostedProdCats['BoostedALL']='(isBoost)'
BoostedProdCats['BoostedGGF']='(isBoost && !isVBF_Boost_'+WTAG+'_nom)'
BoostedProdCats['BoostedVBF']='(isBoost && isVBF_Boost_'+WTAG+'_nom)'


if 'GGF' in configration_py : 
    BoostedProdCats={}
    BoostedProdCats['BoostedGGF']='(!isVBF_Boost_'+WTAG+'_nom)'
if 'VBF' in configration_py : 
    BoostedProdCats={}
    BoostedProdCats['BoostedVBF']='(isVBF_Boost_'+WTAG+'_nom)'
if 'ALL' in configration_py:
    BoostedProdCats['BoostedALL']='(1)'


BoostedRegionCats={}

##BJetBstNotVBF_DeepAK8WP1_nom_cjidx
#nBJetBstNotVBF_DeepAK8WP1_nom
#nBJetBoost_'+WTAG+'_nom
BoostedRegionCats['SR']='(nBJetBoost_'+WTAG+'_nom ==0) && (isBoostSR_'+WTAG+'_nom)'
BoostedRegionCats['TOP'] ='(nBJetBoost_'+WTAG+'_nom  > 0) && (isBoostSR_'+WTAG+'_nom)'
BoostedRegionCats['SB']='(nBJetBoost_'+WTAG+'_nom ==0) && (isBoostSB_'+WTAG+'_nom)'
if 'SR' in configration_py:
    BoostedRegionCats={}
    BoostedRegionCats={'SR':'(nBJetBoost_'+WTAG+'_nom ==0) && (isBoostSR_'+WTAG+'_nom)'}
if 'TOP' in configration_py:
    BoostedRegionCats={}
    #BoostedRegionCats['TOP'] ='(nBJetBoost_'+WTAG+'_nom  > 0) && (isBoost_'+WTAG+'_nom)'
    BoostedRegionCats['TOP'] ='(nBJetBoost_'+WTAG+'_nom  > 0) && (isBoostSR_'+WTAG+'_nom)'
if 'SB' in configration_py:
    BoostedRegionCats={}
    BoostedRegionCats['SB']='(nBJetBoost_'+WTAG+'_nom ==0) && (isBoostSB_'+WTAG+'_nom)'

if 'ALL' in configration_py:
    BoostedRegionCats={}
    BoostedRegionCats['ALL']='(isBoost_'+WTAG+'_nom)'

BoostedMETCat={}
if not ONLY_FINALCUT : BoostedMETCat['NoMET']='1'
BoostedMETCat['METOver40']='('+METtype+'_nom_pt >'+METcutBst+')'##PuppiMET_nom_pt


BoostedPtOverMlnJCat= {}
if not ONLY_FINALCUT: BoostedPtOverMlnJCat['NoPtOverMcut']='1'
if 'ALL' in configration_py:
    BoostedPtOverMlnJCat= {}
    BoostedPtOverMlnJCat['ALL']='(1)'
BoostedPtOverMlnJCat['PtOverM04']='(lnJ_'+WTAG+'_nom_minPtWOverM > 0.4)'

BoostedMEKDCat={}
BoostedMEKDCat['_']='1'
BoostedMEKDCat['MEKDTAG']='(MEKD_Bst_C_'+MELA_C_BOOST_WP+'_M'+str(MELA_MASS_BOOST_WP)+"> 0.5)"
BoostedMEKDCat['UNTAGGED']='(MEKD_Bst_C_'+MELA_C_BOOST_WP+'_M'+str(MELA_MASS_BOOST_WP)+"< 0.5)"
if 'ALL' in configration_py:
    BoostedMEKDCat={}
    BoostedMEKDCat['ALL']='(1)'

BoostedDphiCat={}
#BoostedDphiCat['dphiww2']='(dPhi_WW_boosted[0] > 2.0)'
BoostedDphiCat['_']='(1)'

##--BoostedProdCats, BoostedRegionCats, BoostedPtOverMlnJCat
for LepCut in LepCats:
    for ProdCut in BoostedProdCats:
        for RegionCut in BoostedRegionCats:
            for METCut in BoostedMETCat:
                for PtOvMCut in BoostedPtOverMlnJCat:
                    for dphiCut in BoostedDphiCat:
                        if 'VBF' in ProdCut : 
                            cuts[LepCut+'__'+ProdCut+'__'+RegionCut+'__'+METCut+'__'+PtOvMCut+'__'+dphiCut] = LepCats[LepCut]\
                                                                        +'&&'+BoostedProdCats[ProdCut]\
                                                                        +'&&'+BoostedRegionCats[RegionCut]\
                                                                        +'&&'+BoostedMETCat[METCut]\
                                                                        +'&&'+BoostedPtOverMlnJCat[PtOvMCut]\
                                                                        +'&&'+BoostedDphiCat[dphiCut]
                            
                        else:
                            for MEKDCut in BoostedMEKDCat:
                                cuts[LepCut+'__'+ProdCut+'__'+RegionCut+'__'+METCut+'__'+PtOvMCut+"__"+MEKDCut+'__'+dphiCut] = LepCats[LepCut]\
                                                                        +'&&'+BoostedProdCats[ProdCut]\
                                                                        +'&&'+BoostedRegionCats[RegionCut]\
                                                                        +'&&'+BoostedMETCat[METCut]\
                                                                        +'&&'+BoostedPtOverMlnJCat[PtOvMCut]\
                                                                        +'&&'+BoostedMEKDCat[MEKDCut]\
                                                                        +'&&'+BoostedDphiCat[dphiCut]
##---End of Boosted


print "Ncuts=",len(cuts)

