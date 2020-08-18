#ONLY_FINALCUT=True
import os
import sys
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/../')

#-----Variable Deinition-----#
from WPandCut2016 import *

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
supercut +='&&(!isFinalBoostSR) &&(isResol'+_ALGO_+'nom)'+'&&'+'('+METtype+'_nom_pt >'+METcutRes+')'

##---Lepton Categorization---##



LepCats={}
if 'ele' in configration_py:
    LepCats['eleCH']='(Lepton_isTightElectron_'+eleWP+'[0]>0.5)'
if 'mu' in configration_py:
    LepCats['muCH']='(Lepton_isTightMuon_'+muWP+'[0]>0.5)'
if not ('mu' in configration_py) and not ('ele' in configration_py):
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







PtOverMCut = {}
PtOverMCut['PtOverM035'] = '(lnjj'+_ALGO_+'nom_minPtWOverM>0.35)'
PtOverMCut['PtOverM035low'] = '(lnjj'+_ALGO_+'nom_minPtWOverM <= 0.35)'
PtOverMCut['NoPtOverMCut'] = '1'

WlepMtCut = {}
WlepMtCut['WlepMtOver50'] = '(Wlep_nom_Mt > 50)'
WlepMtCut['WlepMtUnder50'] = '(Wlep_nom_Mt <= 50)'
WlepMtCut['NoWlepMtCut'] = '1'

WWMtCut = {}
WWMtCut['NoWWMtCut'] = '(1)'
WWMtCut['WWMtOver60']='(lnjj'+_ALGO_+'nom_Mt > 60)'
WWMtCut['WWMtUnder60']='(lnjj'+_ALGO_+'nom_Mt <= 60)'

MEKDCut={}
MEKDCut['NoMEKDCut']='1'
MEKDCut['MEKDTAG']='(MEKD_Res_C_'+MELA_C_RESOL_WP+'_M'+str(MELA_MASS_RESOL_WP)+"> 0.5)"
MEKDCut['UNTAGGED']='(MEKD_Res_C_'+MELA_C_RESOL_WP+'_M'+str(MELA_MASS_RESOL_WP)+"< 0.5)"



for LepCut in LepCats:
    for ProdCut in ResolvedProdCats:
        for RegionCut in ResolvedRegionCats:
            ##---basic
            cutname_base=LepCut+'__'+ProdCut+'__'+RegionCut
            formula_base=LepCats[LepCut]+'&&'+ResolvedProdCats[ProdCut]+'&&'+ResolvedRegionCats[RegionCut]

            ##---Final add
            if FORFINAL: ##For final result
                if (not 'GGF' in ProdCut) and (not 'VBF' in ProdCut): continue ##VBF/GGF category only
                for MEKD in ['MEKDTAG','UNTAGGED']: ##MEKD Category
                    cutname=cutname_base+'_'+MEKD
                    ##Add final cuts
                    formula=formula_base+'&&'+MEKDCut[MEKD]+'&&'+WWMtCut['WWMtOver60']+'&&'+WlepMtCut['WlepMtOver50']+'&&'+PtOverMCut['PtOverM035']
                    cuts[cutname]=formula
            if N1CUT: ##For AN
                ##--- each flv/ each sb sr top /ALL Production / apply WWMt /apply WlepMt/apply ptoverm
                if 'GGF' in ProdCut or 'VBF' in ProdCut: continue ##inclusive for production channel
                ##----Remove PtOverMcut (NoPtOverMCut)
                cutname=cutname_base+'_NoPtOverMCut'
                formula=formula_base+'&&'+WWMtCut['WWMtOver60']+'&&'+WlepMtCut['WlepMtOver50']
                cuts[cutname]=formula
                
                ##----Remove WWMtCut (NoWWMtCut)
                cutname=cutname_base+'_NoWWMtCut'
                formula=formula_base+'&&'+WlepMtCut['WlepMtOver50']+'&&'+PtOverMCut['PtOverM035']
                cuts[cutname]=formula

                ##----Remove WlepMtCut (NoWlepMtCut)
                cutname=cutname_base+'_NoWlepMtCut'
                formula=formula_base+'&&'+WWMtCut['WWMtOver60']+'&&'+PtOverMCut['PtOverM035']
                cuts[cutname]=formula

                ##---Only without MEKD Category
                cutname=cutname_base+'_NoMEKDCut'
                formula=formula_base+'&&'+WWMtCut['WWMtOver60']+'&&'+WlepMtCut['WlepMtOver50']+'&&'+PtOverMCut['PtOverM035']
                cuts[cutname]=formula



##---For QCDCR Study
if QCDCR:
    for LepCut in LepCats:
        ##--reverse PtOverM
        cutname_base=LepCut+'_PtOverM04low'
        formula_base=LepCats[LepCut]+'&&'+PtOverMCut['PtOverM035low']
        ##--WlepMt >50
        cutname=cutname_base+'_WlepMtOver50'
        formula=formula_base+'&&'+WlepMtCut['WlepMtOver50']
        cuts[cutname]=formula

        ##--WlepMt < 50
        cutname=cutname_base+'_WlepMtUnder50'
        formula=formula_base+'&&'+WlepMtCut['WlepMtUnder50']
        cuts[cutname]=formula

        ##--WWMtOver60
        cutname=cutname_base+'_WWMtOver60'
        formula=formula_base+'&&'+WWMtCut['WWMtOver60']
        cuts[cutname]=formula

        ##--WWMtUnder60
        cutname=cutname_base+'_WWMtUnder60'
        formula=formula_base+'&&'+WWMtCut['WWMtUnder60']
        cuts[cutname]=formula


#cuts['isVBF']='isVBF'
print "Ncuts=",len(cuts)
for c in cuts:
    print c
