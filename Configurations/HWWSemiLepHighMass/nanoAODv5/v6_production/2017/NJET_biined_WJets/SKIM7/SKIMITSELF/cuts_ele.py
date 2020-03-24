#-----Variable Deinition-----#
from WPandCut2017 import *
import sys
#cuts={}

scriptname=opt.cutsFile

LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepCut="(  Lepton_pt[0]>30 \
&& ( fabs(Lepton_eta[0])  < 2.5*(abs(Lepton_pdgId[0])==11) \
||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
&& ( ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
||   ( Alt$( Lepton_pt[1],-1) < 10*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
)\
)"
LepPtCut='(Lepton_pt[0] > ('+elePtCut+'*(abs(Lepton_pdgId[0])==11) + '+muPtCut+'*(abs(Lepton_pdgId[0])==13)) )'



#------End of Variable Definition-----#
#supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut+'&&isFatJetEvent[0]'
METtype="PuppiMET"
supercut = LepWPCut+'&&'+LepPtCut+'&&'+LepCut+'&&'+METtype+'_pt'+'> 30'



##---Lepton Categorization---##



LepCats={}
if 'ele' in scriptname:
    LepCats['eleCH']='(Lepton_isTightElectron_'+eleWP+'[0]>0.5)'
elif 'mu' in scriptname:
    LepCats['muCH']='(Lepton_isTightMuon_'+muWP+'[0]>0.5)'
else:
    LepCats={
        'ALLLEP':'1',
        'eleCH':'(Lepton_isTightElectron_'+eleWP+'[0]>0.5)',
        'muCH':'(Lepton_isTightMuon_'+muWP+'[0]>0.5)',
    }

##-----Basic categorization-----##
MTCats={}
MTCats['MT0To50']="Wlep_Mt<50"
MTCats['MT50To110']="Wlep_Mt>50 && Wlep_Mt<110"
MTCats['MT110ToInf']="Wlep_Mt>110"



for LepCut in LepCats:
    for MTCut in MTCats:
        CUTNAMES=[LepCut,MTCut]
        CUTDEFS=[ LepCats[LepCut],MTCats[MTCut] ]
        cuts["__".join(CUTNAMES)] = '&&'.join(CUTDEFS)
                   
                    

#cuts['isVBF']='isVBF'
print "Ncuts=",len(cuts)

