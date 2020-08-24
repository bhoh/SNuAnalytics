#ONLY_FINALCUT=True

import os
import sys
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/../')


#-----Variable Deinition-----#
from WPandCut2016 import *

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
supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut+' && ((isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0)))'+'&&'+'('+METtype+'_nom_pt >'+METcutBst+')'


##---Lepton Categorization---##



LepCats={}
if 'ele' in configration_py:
    LepCats['eleCH']='(Lepton_isTightElectron_'+eleWP+'[0]>0.5)'
if 'mu' in configration_py:
    LepCats['muCH']='(Lepton_isTightMuon_'+muWP+'[0]>0.5)'
if not ('mu' in configration_py) and not ('ele' in configration_py): ##for shape factory 
    LepCats={
        '_':'1',
        'eleCH':'(Lepton_isTightElectron_'+eleWP+'[0]>0.5)',
        'muCH':'(Lepton_isTightMuon_'+muWP+'[0]>0.5)',
    }
if ('ele' in configration_py) and ('mu' in configration_py): ##for plotting
    LepCats={
        '_':'1',
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



PtOverMlnJCut= {}
PtOverMlnJCut['NoPtOverMcut']='1'
PtOverMlnJCut['PtOverM04']='(lnJ_'+WTAG+'_nom_minPtWOverM > 0.4)'
PtOverMlnJCut['PtOverM04low']='(lnJ_'+WTAG+'_nom_minPtWOverM <= 0.4)'

    
MEKDCut={}
MEKDCut['NoMEKDCut']='1'
MEKDCut['MEKDTAG']='(MEKD_Bst_C_'+MELA_C_BOOST_WP+'_M'+str(MELA_MASS_BOOST_WP)+"> 0.5)"
MEKDCut['UNTAGGED']='(MEKD_Bst_C_'+MELA_C_BOOST_WP+'_M'+str(MELA_MASS_BOOST_WP)+"< 0.5)"

##--For QCD Study
WlepMtCut = {}
WlepMtCut['WlepMtOver50'] = '(Wlep_nom_Mt > 50)'
WlepMtCut['WlepMtUnder50'] = '(Wlep_nom_Mt <= 50)'
WlepMtCut['NoWlepMtCut'] = '1'




##--BoostedProdCats, BoostedRegionCats, BoostedPtOverMlnJCat
for LepCut in LepCats:
    for ProdCut in BoostedProdCats:
        for RegionCut in BoostedRegionCats:
            cutname_base=LepCut+'_'+ProdCut+'_'+RegionCut
            formula_base=LepCats[LepCut]+'&&'+BoostedProdCats[ProdCut]+'&&'+BoostedRegionCats[RegionCut]

            if FORFINAL: ##For final result
                if (not 'GGF' in ProdCut) and (not 'VBF' in ProdCut): continue ##VBF/GGF category only
                if ('eleCH' in LepCut) or ('eleCH' in LepCut): continue ##Combine ele/mu ch
                for MEKD in ['MEKDTAG','UNTAGGED']: ##MEKD Category
                    cutname=cutname_base+'_'+MEKD
                    ##Add final cuts
                    formula=formula_base+'&&'+MEKDCut[MEKD]+'&&'+PtOverMlnJCut['PtOverM04']
                    cuts[cutname]=formula
            
            if N1CUT: ##For AN plots
                ##--- each flv/ each sb sr top /ALL Production / apply ptOverM
                if 'GGF' in ProdCut or 'VBF' in ProdCut: continue ##inclusive for production channel
                ##---Remove PtOverMcut(NoPtOverMcut)
                cutname=cutname_base+'_NoPtOverMcut'
                formula=formula_base
                cuts[cutname]=formula

                ##---Only without MEKD Category
                cutname=cutname_base+'_NoMEKDCut'
                formula=formula_base+'&&'+PtOverMlnJCut['PtOverM04']
                cuts[cutname]=formula


##---For QCDCR Study
if QCDCR:
    for LepCut in LepCats:
        ##--reverse PtOverM
        cutname_base=LepCut+'_PtOverM04low'
        formula_base=LepCats[LepCut]+'&&'+PtOverMlnJCut['PtOverM04low']
        ##--WlepMt >50
        cutname=cutname_base+'_WlepMtOver50'
        formula=formula_base+'&&'+WlepMtCut['WlepMtOver50']
        cuts[cutname]=formula
        
        ##--WlepMt < 50
        cutname=cutname_base+'_WlepMtUnder50'
        formula=formula_base+'&&'+WlepMtCut['WlepMtUnder50']
        cuts[cutname]=formula
    
##---End of Boosted


print "Ncuts=",len(cuts)

for c in sorted(cuts):
    print c
