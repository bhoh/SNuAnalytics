ONLY_FINAL= False

import os
import sys
sys.path.append(os.getcwd())

print "ONLY_FINAL=",ONLY_FINAL
#-----Variable Deinition-----#
from WPandCut2017 import *

#cuts={}



print 'opt.cutsFile=',opt.cutsFile
LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepCut="(  Lepton_pt[0]>30 \
&& ( fabs(Lepton_eta[0])  < 2.5*(abs(Lepton_pdgId[0])==11) \
||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
&& ( ( Alt$( Lepton_isLoose[1]*Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
||   ( Alt$( Lepton_isLoose[1]*Lepton_pt[1],-1) < 10*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
)\
)"
LepPtCut='(Lepton_pt[0] > ('+elePtCut+'*(abs(Lepton_pdgId[0])==11) + '+muPtCut+'*(abs(Lepton_pdgId[0])==13)) )'



#------End of Variable Definition-----#
#supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut+'&&isFatJetEvent[0]'
supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut


##---Lepton Categorization---##



LepCats={}
if 'ele' in opt.cutsFile:
    LepCats['eleCH']='(Lepton_isTightElectron_'+eleWP+'[0]>0.5)'
elif 'mu' in opt.cutsFile:
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
#if 'GGF' in opt.cutsFile : 
BoostedProdCats['BstGGF_SR']='(isBoost_'+WTAG+'_nom && !isVBF_Boost_'+WTAG+'_nom)'\
    + '&& (nBJetBoost_'+WTAG+'_nom==0)'\
    + '&& (isBoostSR_'+WTAG+'_nom)'
BoostedProdCats['BstGGF_noWin']='(isBoost_'+WTAG+'_nom && !isVBF_Boost_'+WTAG+'_nom)'\
    + '&& (nBJetBoost_'+WTAG+'_nom==0)'
BoostedProdCats['BstGGF_noWin_noBveto']='(isBoost_'+WTAG+'_nom && !isVBF_Boost_'+WTAG+'_nom)'

#if 'VBF' in opt.cutsFile : 
BoostedProdCats['BstVBF_SR']='(isBoost_'+WTAG+'_nom && isVBF_Boost_'+WTAG+'_nom)'\
    + '&& (nBJetBstNotVBF_'+WTAG+'_nom==0)'\
    + '&& (isBoostSR_'+WTAG+'_nom)'
BoostedProdCats['BstVBF_noWin']='(isBoost_'+WTAG+'_nom && isVBF_Boost_'+WTAG+'_nom)'\
    + '&& (nBJetBstNotVBF_'+WTAG+'_nom==0)'
BoostedProdCats['BstVBF_noWin_noBveto']='(isBoost_'+WTAG+'_nom && isVBF_Boost_'+WTAG+'_nom)'




BoostedRegionCats={}
#if 'SR' in opt.cutsFile:
BoostedRegionCats['SR']='(nBJetBoost_'+WTAG+'_nom==0) &&(nBJetBstNotVBF_'+WTAG+'_nom==0) (isBoostSR_'+WTAG+'_nom)'
BoostedRegionCats['SRwoMass']='(nBJetBoost_'+WTAG+'_nom==0) && (isBoostSR_'+WTAG+'_nom)'
BoostedRegionCats['BstPlTop']='(1)'
#if 'TOP' in opt.cutsFile:
#BoostedRegionCats['TOP'] ='(nBJetBoost_'+WTAG+'_nom > 0) && (isBoost_'+WTAG+'_nom)'
#if 'SB' in opt.cutsFile:
#BoostedRegionCats['SB']='(nBJetBoost_'+WTAG+'_nom==0) && (isBoostSB_'+WTAG+'_nom)'


BoostedMETCat={}
if not ONLY_FINAL : BoostedMETCat['NoMET']='1'
BoostedMETCat['METOver40']='('+METtype+'_nom_pt >'+METcutBst+')'##PuppiMET_nom_pt


BoostedPtOverMlnJCat= {}
if not ONLY_FINAL: BoostedPtOverMlnJCat['NoPtOverMcut']='1'
BoostedPtOverMlnJCat['PtOverM04']='lnJ_'+WTAG+'_nom_minPtWOverM > 0.4'



#BoostedMEKDCat={}
#BoostedMEKDCat['_']='1'
#BoostedMEKDCat['MEKDTAG']='(MEKD_Bst_C_'+MELA_C_BOOST_WP+'_M'+str(MELA_MASS_BOOST_WP)+"> 0.5)"
#BoostedMEKDCat['UNTAGGED']='(MEKD_Bst_C_'+MELA_C_BOOST_WP+'_M'+str(MELA_MASS_BOOST_WP)+"< 0.5)"

##--BoostedProdCats, BoostedRegionCats, BoostedPtOverMlnJCat
for LepCut in LepCats:
    for ProdCut in BoostedProdCats:
        #for RegionCut in BoostedRegionCats:
            for METCut in BoostedMETCat:
                for PtOvMCut in BoostedPtOverMlnJCat:
                    if 'VBF' in ProdCut : 
                        cuts[LepCut+'_'+ProdCut+'_'+METCut+'_'+PtOvMCut] = LepCats[LepCut]\
                                                                        +'&&'+BoostedProdCats[ProdCut]\
                                                                        +'&&'+BoostedMETCat[METCut]\
                                                                        +'&&'+BoostedPtOverMlnJCat[PtOvMCut]
                    else:
                        #for mepBasic in mepBasicCuts:
                          cuts[LepCut+'_'+ProdCut+'_'+METCut+'_'+PtOvMCut] = LepCats[LepCut]\
                                                                        +'&&'+BoostedProdCats[ProdCut]\
                                                                        +'&&'+BoostedMETCat[METCut]\
                                                                        +'&&'+BoostedPtOverMlnJCat[PtOvMCut]
##---End of Boosted


print "Ncuts=",len(cuts)

