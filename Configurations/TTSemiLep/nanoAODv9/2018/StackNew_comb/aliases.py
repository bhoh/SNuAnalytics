import os
import copy
import inspect

#-----Variable Deinition-----#
try:
  from WPandCut2018 import *
except ImportError:
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv9/2018/StackNew_comb"
  sys.path.append(BASE_PATH)
  from WPandCut2018 import *


##-End WP--##


configurations = '%s/src/SNuAnalytics/Configurations/TTSemiLep' % os.getenv('CMSSW_BASE')
print configurations




mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]
ttmc_syst = ['TTLJ','TTLJ_jj','TTLJ_cc','TTLJ_bb','TTLJ_bj','TTLL','TTLL_jj','TTLL_cc','TTLL_bb','TTLL_bj']

# veto loose lepton

aliases['nLooseLep'] = {
        'expr': 'Sum$( abs(Lepton_pdgId) == 11 && Lepton_pt > 15. && abs(Lepton_eta) < 2.5) + Sum$( abs(Lepton_pdgId) == 13 && Lepton_pt > 15. && abs(Lepton_eta) < 2.4)'
        #'expr': 'Sum$(Electron_cutBased_Fall17_V1 >= 2 && Electron_pt > 15. && abs(Electron_eta) < 2.5) + Sum$(Muon_looseId > 0.5 && Muon_pt > 8. && abs(Muon_eta) < 2.4)'
        }

# lepton cut

aliases['eleCH'] = {
        'expr' : '(   (abs(Lepton_pdgId[0])==11)\
                   && (Lepton_isTightElectron_'+eleWP+'[0]>0.5)\
                   && (Lepton_pt[0] > '+elePtCut+')\
                   && (fabs(Lepton_eta[0]) < 2.5)\
                  )',
        }

aliases['muCH'] = {
        'expr' : '(   (abs(Lepton_pdgId[0])==13)\
                   && (Lepton_isTightMuon_'+muWP+'[0]>0.5)\
                   && (Lepton_pt[0] > '+muPtCut+')\
                   && (fabs(Lepton_eta[0]) < 2.4)\
                  )',
        }

#######
aliases['isOSpair'] = {
        'expr' : 'Lepton_pdgId[0]*Alt$(Lepton_pdgId[1],-999)<0',
        }

aliases['eeCH'] = {
        'expr' : '(   (abs(Lepton_pdgId[0])==11)\
                   && (Lepton_isTightElectron_'+eleWP+'[0]>0.5)\
                   && (Lepton_pt[0] > '+eePtCut[0]+')\
                   && (fabs(Lepton_eta[0]) < 2.5)\
                   && (abs(Alt$(Lepton_pdgId[1],-999))==11)\
                   && (Alt$(Lepton_isTightElectron_'+eleWP+'[1],-999)>0.5)\
                   && (Alt$(Lepton_pt[1],-999) > '+eePtCut[1]+')\
                   && (fabs(Alt$(Lepton_eta[1],-999)) < 2.5)\
                  )',
        }

aliases['mmCH'] = {
        'expr' : '(   (abs(Lepton_pdgId[0])==13)\
                   && (Lepton_isTightMuon_'+muWP+'[0]>0.5)\
                   && (Lepton_pt[0] > '+mmPtCut[0]+')\
                   && (fabs(Lepton_eta[0]) < 2.4)\
                   && (abs(Alt$(Lepton_pdgId[1],-999))==13)\
                   && (Alt$(Lepton_isTightMuon_'+muWP+'[1],-999)>0.5)\
                   && (Alt$(Lepton_pt[1],-999) > '+mmPtCut[1]+')\
                   && (fabs(Alt$(Lepton_eta[1],-999)) < 2.4)\
                  )',
        }

aliases['emCH'] = {
        'expr' : '(   (abs(Lepton_pdgId[0])==11)\
                   && (Lepton_isTightElectron_'+eleWP+'[0]>0.5)\
                   && (Lepton_pt[0] > '+emPtCut[0]+')\
                   && (fabs(Lepton_eta[0]) < 2.5)\
                   && (abs(Alt$(Lepton_pdgId[1],-999))==13)\
                   && (Alt$(Lepton_isTightMuon_'+muWP+'[1],-999)>0.5)\
                   && (Alt$(Lepton_pt[1],-999) > '+emPtCut[1]+')\
                   && (fabs(Alt$(Lepton_eta[1],-999)) < 2.4)\
                  )',
        }

aliases['meCH'] = {
        'expr' : '(   (abs(Lepton_pdgId[0])==13)\
                   && (Lepton_isTightMuon_'+muWP+'[0]>0.5)\
                   && (Lepton_pt[0] > '+mePtCut[0]+')\
                   && (fabs(Lepton_eta[0]) < 2.4)\
                   && (abs(Alt$(Lepton_pdgId[1],-999))==11)\
                   && (Alt$(Lepton_isTightElectron_'+eleWP+'[1],-999)>0.5)\
                   && (Alt$(Lepton_pt[1],-999) > '+mePtCut[1]+')\
                   && (fabs(Alt$(Lepton_eta[1],-999)) < 2.5)\
                  )',
        }

aliases['sngCH'] = {
        'expr' : '(nLooseLep==1) && (eleCH || muCH)'
        }

aliases['dblCH'] = {
        'expr' : '(nLooseLep==2) && (eeCH || mmCH || meCH || emCH)'
        }

### OTF pileup reweight SF

puReweightSF_path = "/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/LatinoAnalysis/NanoGardener/python/data/PUweights/2018/PileupWeight2018.root"
aliases['OTF_puWeight'] = {
    'linesToAdd': [
        '.L %s/patches/puweight.cc+' % configurations
    ],
    'class': 'puReweight',
    'args': (puReweightSF_path, "MC_2018_central", "", ""),
    'samples': mc
}

aliases['OTF_puWeightUp'] = {
    'linesToAdd': [
        '.L %s/patches/puweight.cc+' % configurations
    ],
    'class': 'puReweight',
    'args': (puReweightSF_path, "MC_2018_sig_up", "", ""),
    'samples': mc
}

aliases['OTF_puWeightDown'] = {
    'linesToAdd': [
        '.L %s/patches/puweight.cc+' % configurations
    ],
    'class': 'puReweight',
    'args': (puReweightSF_path, "MC_2018_sig_down", "", ""),
    'samples': mc
}

### -- electron trigger efficiency SF -- ###
EleTrigEffSFSource = '%s/src/SNuAnalytics/Configurations/TTSemiLep/patches/scale_factors/egammaEffi_Vcb_trig_2018.root' % os.getenv('CMSSW_BASE')
### -- muon trigger efficiency SF -- ###
MuTrigEffSFSource = '%s/src/SNuAnalytics/Configurations/TTSemiLep/patches/scale_factors/Efficiencies_muon_generalTracks_Z_Run2018_UL_SingleMuonTriggers.root' % os.getenv('CMSSW_BASE')
### lepton eff.
EleTrigEffMCHistName   = 'sim'
MuTrigEffMCHistName    = 'NUM_IsoMu24_DEN_CutBasedIdTight_and_PFIsoTight_abseta_pt_efficiencyMC'
EleTrigEffDATAHistName = 'data'
MuTrigEffDATAHistName  = 'NUM_IsoMu24_DEN_CutBasedIdTight_and_PFIsoTight_abseta_pt_efficiencyData'

aliases['OTF_SingleTrig_MC_Eff'] = {
    'linesToAdd': [
        '.L %s/patches/leptoneff.cc+' % configurations
    ],
    'class': 'LeptonEff',
    'args': (EleTrigEffSFSource,MuTrigEffSFSource,EleTrigEffMCHistName,MuTrigEffMCHistName,'etapt','etapt'),
    'samples': mc
}

aliases['OTF_SingleTrig_DATA_Eff'] = {
    'linesToAdd': [
        '.L %s/patches/leptoneff.cc+' % configurations
    ],
    'class': 'LeptonEff',
    'args': (EleTrigEffSFSource,MuTrigEffSFSource,EleTrigEffDATAHistName,MuTrigEffDATAHistName,'etapt','etapt'),
    'samples': mc
}
#
#ver1
eff_ele_syst   = '((nLooseLep==1)*(eleCH*Lepton_tightElectron_{eleWP}_TotSF[0]+muCH) + (nLooseLep==2)*(1))'.format(eleWP=eleWP,muWP=muWP)
#ver2
#eff_ele_syst   = '((nLooseLep==1)*((eleCH)*Lepton_tightElectron_{eleWP}_IdIsoSF[0]+muCH) + (nLooseLep==2)*((!mmCH)*Lepton_tightElectron_{eleWP}_IdIsoSF[0]*Lepton_tightElectron_{eleWP}_IdIsoSF[1]+mmCH))'.format(eleWP=eleWP,muWP=muWP)
eff_ele_syst_u = eff_ele_syst.replace('_TotSF','_TotSF_Up').replace('(nLooseLep==2)*(1)','(nLooseLep==2)*(LepSF2l__ele_{eleWP}__Up)'.format(eleWP=eleWP))
eff_ele_syst_d = eff_ele_syst.replace('_TotSF','_TotSF_Down').replace('(nLooseLep==2)*(1)','(nLooseLep==2)*(LepSF2l__ele_{eleWP}__Do)'.format(eleWP=eleWP))
#ver2
#eff_ele_syst_u = eff_ele_syst.replace('_IdIsoSF','_IdIsoSF_Up')
#eff_ele_syst_d = eff_ele_syst.replace('_IdIsoSF','_IdIsoSF_Down')
#
eff_muon_syst   = '((nLooseLep==1)*(muCH*Lepton_tightMuon_{muWP}_TotSF[0]+eleCH) + (nLooseLep==2)*(1))'.format(eleWP=eleWP,muWP=muWP)
eff_muon_syst_u = eff_muon_syst.replace('_TotSF','_TotSF_Up').replace('(nLooseLep==2)*(1)','(nLooseLep==2)*(LepSF2l__mu_{muWP}__Up)'.format(muWP=muWP))
eff_muon_syst_d = eff_muon_syst.replace('_TotSF','_TotSF_Down').replace('(nLooseLep==2)*(1)','(nLooseLep==2)*(LepSF2l__mu_{muWP}__Do)'.format(muWP=muWP))
#eff_muon_syst = ['Lepton_tightMuon_'+muWP+'_TotSF_Up'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0]','Lepton_tightMuon_'+muWP+'_TotSF_Down'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0]']

aliases['id_ele_up'] = {
    'expr': 'Alt$({UP}/{NOM},1)'.format(UP=eff_ele_syst_u,NOM=eff_ele_syst),
    'samples': mc
}

aliases['id_ele_down'] = {
    'expr': 'Alt$({DOWN}/{NOM},1)'.format(DOWN=eff_ele_syst_d,NOM=eff_ele_syst),
    'samples': mc
}

aliases['id_mu_up'] = {
    'expr': 'Alt$({UP}/{NOM},1.)'.format(UP=eff_muon_syst_u,NOM=eff_muon_syst),
    'samples': mc
}

aliases['id_mu_down'] = {
    'expr': 'Alt$({DOWN}/{NOM},1.)'.format(DOWN=eff_muon_syst_d,NOM=eff_muon_syst),
    'samples': mc
}

#trig_syst = ['TriggerEffWeight_1l_u/TriggerEffWeight_1l','TriggerEffWeight_1l_d/TriggerEffWeight_1l']
trig_ele_syst    = 'Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)'
trig_ele_syst_u  = trig_ele_syst.replace('Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)','Alt$(OTF_SingleTrig_DATA_Eff[1]/OTF_SingleTrig_MC_Eff[2],1)')
trig_ele_syst_d  = trig_ele_syst.replace('Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)','Alt$(OTF_SingleTrig_DATA_Eff[2]/OTF_SingleTrig_MC_Eff[1],1)')
trig_mu_syst     = 'Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)'
trig_mu_syst_u   = trig_mu_syst.replace('Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)','Alt$(OTF_SingleTrig_DATA_Eff[3]/OTF_SingleTrig_MC_Eff[4],1)')
trig_mu_syst_d   = trig_mu_syst.replace('Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)','Alt$(OTF_SingleTrig_DATA_Eff[4]/OTF_SingleTrig_MC_Eff[3],1)')

aliases['trig_ele_up'] = {
    'expr': 'Alt$({UP}/{NOM},1.)'.format(UP=trig_ele_syst_u,NOM=trig_ele_syst),
    'samples': mc
}

aliases['trig_ele_down'] = {
    'expr': 'Alt$({DOWN}/{NOM},1.)'.format(DOWN=trig_ele_syst_d,NOM=trig_ele_syst),
    'samples': mc
}

aliases['trig_mu_up'] = {
    'expr': 'Alt$({UP}/{NOM},1.)'.format(UP=trig_mu_syst_u,NOM=trig_mu_syst),
    'samples': mc
}

aliases['trig_mu_down'] = {
    'expr': 'Alt$({DOWN}/{NOM},1.)'.format(DOWN=trig_mu_syst_d,NOM=trig_mu_syst),
    'samples': mc
}

#MuIDSFSource = '%s/src/SNuAnalytics/Configurations/TTSemiLep/patches/scale_factors/2018_ID_TH2_SFs_pt_abseta.root' % os.getenv('CMSSW_BASE')
#MuIDSFHistName = 'NUM_TightID_DEN_TrackerMuons_pt_abseta'
#
#aliases['OTF_MuID_POGTight_SF'] = {
#    'linesToAdd': [
#        '.L %s/patches/leptonsf.cc+' % configurations
#    ],
#    'class': 'LeptonSF',
#    'args': (MuIDSFSource,MuIDSFHistName,'pteta'),
#    #'samples': mc
#
#}
#MuISOSFSource = '%s/src/SNuAnalytics/Configurations/TTSemiLep/patches/scale_factors/2018_RunABCD_SF_ISO.root' % os.getenv('CMSSW_BASE')
#MuISOSFHistName = 'NUM_TightRelIso_DEN_TightIDandIPCut_pt_abseta'
#
#aliases['OTF_MuISO_SF'] = {
#    'linesToAdd': [
#        '.L %s/patches/leptonsf.cc+' % configurations
#    ],
#    'class': 'LeptonSF',
#    'args': (MuISOSFSource,MuISOSFHistName,'pteta'),
#    #'samples': mc
#
#}
# trig matching

#aliases['trigMatching_sng_ele'] = {
#            'expr': '(abs(Lepton_pdgId[0])==11) && Sum$( ((Lepton_eta[0]-TrigObj_eta)*(Lepton_eta[0]-TrigObj_eta)+(Lepton_phi[0]-TrigObj_phi)*(Lepton_phi[0]-TrigObj_phi))<0.1*0.1 && TrigObj_filterBits & 2 )>0.5'
#            }
# Jet cut

aliases['nCleanJet20_2p4'] = {
            'expr': 'Sum$(Jet_pt_nom[CleanJet_jetIdx] > 20. && abs(CleanJet_eta) < 2.4)'
            }

aliases['nCleanJet25_2p4'] = {
            'expr': 'Sum$(Jet_pt_nom[CleanJet_jetIdx] > 25. && abs(CleanJet_eta) < 2.4)'
            }

aliases['nCleanJet25to30_2p4'] = {
            'expr': 'Sum$(Jet_pt_nom[CleanJet_jetIdx] > 25. && Jet_pt_nom[CleanJet_jetIdx] <= 30. && abs(CleanJet_eta) < 2.4 )'
            }

aliases['nCleanJet30_2p4'] = {
            'expr': 'Sum$(Jet_pt_nom[CleanJet_jetIdx] > 30. && abs(CleanJet_eta) < 2.4)'
            }

aliases['SelectedJetIdx'] = {
    'linesToAdd' : [
        '.L %s/patches/selectedjet.cc+' % configurations,
    ],
    'class': 'SelectedJet',
    'args': (25.,2.4), # pT, |eta| cut
    'samples': samples.keys(),
}

aliases['SelectedBJetIdx'] = {
    'linesToAdd' : [
        '.L %s/patches/selectedbjet.cc+' % configurations,
    ],
    'class': 'SelectedBJet',
    'args': (25.,2.4, 0., True), # pT, |eta| cut, csv cut(not used variable)
    'samples': samples.keys(),
}


# MET

#XXX
#aliases['MET_CHToCB_pt_nom'] = {
#            'expr': 'Alt$(MET_CHToCB_pt_nom, PuppiMET_pt)',
#            #'expr': 'MET_CHToCB_pt_nom'
#            }
Top_pTrw = 'TMath::Sqrt((0.103*TMath::Exp(-0.0118*{TOP_GEN_PT})-0.000134*{TOP_GEN_PT}+0.973)*(0.103*TMath::Exp(-0.0118*{ANTITOP_GEN_PT})-0.000134*{ANTITOP_GEN_PT}+0.973))'.format(TOP_GEN_PT='topGenPt', ANTITOP_GEN_PT='antitopGenPt')
aliases['Top_pTrw'] = {
     'expr': Top_pTrw,
     'samples': ttmc_syst,
}
#aliases['ttGenPt'] = {
#     'expr': 'TMath::Sqrt( topGenPt*topGenPt + antitopGenPt*antitopGenPt + 2*topGenPt*antitopGenPt*TMath::Cos(topGenPhi - antitopGenPhi) )',
#     'samples': ttmc_syst,
#}
#
#aliases['avgtopGenMass'] = {
#     'expr': 'TMath::Sqrt( topGenMass * antitopGenMass )',
#     'samples': ttmc_syst,
#}

# top pt reweight

#aliases['topGenPt_max'] = {
#    'expr': '(topGenPt>472)*472 + (topGenPt<=472)*topGenPt',
#    'samples': ['TTLJ+jj','TTLJ+bj','TTLJ+bb','TTLJ+cc','TTLL+jj','TTLL+bj','TTLL+bb','TTLL+cc'],
#}
#
#aliases['antitopGenPt_max'] = {
#    'expr': '(antitopGenPt>472)*472 + (antitopGenPt<=472)*antitopGenPt',
#    'samples': ['TTLJ+jj','TTLJ+bj','TTLJ+bb','TTLJ+cc','TTLL+jj','TTLL+bj','TTLL+bb','TTLL+cc'],
#}

# if (anti)topGenPt variables not exists in systematic trees(ex. hdampUp/Down), it cause error.
#aliases['Top_pTrw'] = {
#    'expr': '( TMath::Sqrt(TMath::Exp(-1.43717e-02 - 1.18358e-04*topGenPt - 1.70651e-07*topGenPt*topGenPt + 4.47969/(topGenPt+28.7)) * TMath::Exp(-1.43717e-02 - 1.18358e-04*antitopGenPt - 1.70651e-07*antitopGenPt*antitopGenPt + 4.47969/(antitopGenPt+28.7))))',
#    'samples': ['TTLJ+jj','TTLJ+bj','TTLJ+bb','TTLJ+cc','TTLL+jj','TTLL+bj','TTLL+bb','TTLL+cc'],
#}

# B tagging

aliases['nBJets_WP_M'] = {
            'expr': 'Sum$(Jet_pt_nom[CleanJet_jetIdx] > 30. && abs(CleanJet_eta) < 2.4 && Jet_btagDeepFlavB[CleanJet_jetIdx] > 0.2783)'
            #'expr': 'Sum$(Jet_pt_nom[CleanJet_jetIdx] > ( ((nLooseLep==2 && Iteration$<2) || nLooseLep<2)?30.:20. ) && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.4184)'
            }
aliases['nBJets_WP_M_25to30'] = {
            'expr': 'Sum$(Jet_pt_nom[CleanJet_jetIdx] > 25. && Jet_pt_nom[CleanJet_jetIdx] <= 30. && abs(CleanJet_eta) < 2.4 && Jet_btagDeepFlavB[CleanJet_jetIdx] > 0.2783)'
            }




aliases['OTF_btagSF'] = {
        'expr': 'TMath::Exp(Sum$(TMath::Log(((Jet_pt_nom[CleanJet_jetIdx]>25 && abs(CleanJet_eta)<2.4))*Jet_btagSF_deepjet_shape[CleanJet_jetIdx]+1*(Jet_pt_nom[CleanJet_jetIdx]<=25 || abs(CleanJet_eta)>=2.4))))',
    'samples': mc
}

btagSFNorm_top_1l = "(nCleanJet25_2p4<4)*(1.) + (nCleanJet25_2p4==4)*(0.999558629848) + (nCleanJet25_2p4==5)*(0.988554409403) + (nCleanJet25_2p4==6)*(0.969425114582) + (nCleanJet25_2p4==7)*(0.943688995808) + (nCleanJet25_2p4==8)*(0.913024674379) + (nCleanJet25_2p4>=9)*(0.87768790965)"
btagSFNorm_top_2l = "(nCleanJet25_2p4<4)*(1.) + (nCleanJet25_2p4==4)*(0.978329578407) + (nCleanJet25_2p4==5)*(0.960751321102) + (nCleanJet25_2p4==6)*(0.936243160494) + (nCleanJet25_2p4==7)*(0.907221221331) + (nCleanJet25_2p4==8)*(0.878125279419) + (nCleanJet25_2p4>=9)*(0.853389741223)"
aliases['btagSFNorm_top'] = {
    #'expr': 'TMath::Exp(Sum$(TMath::Log((Jet_pt[CleanJet_jetIdx]>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFixNorm_top[CleanJet_jetIdx]+1*(Jet_pt[CleanJet_jetIdx]<=30 || abs(CleanJet_eta)>=2.5))))',
    #'expr': '1.',
    'expr' : '(nLepton==1)*({FORMULA1})+(nLepton==2)*({FORMULA2})'.format(FORMULA1=btagSFNorm_top_1l, FORMULA2=btagSFNorm_top_2l),
    'samples': mc
}

jes_syst = ['jesFlavorQCD','jesTotalNoFlavor']
for shift in jes_syst + ['lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
 
    shift_ = shift.replace("jesTotalNoFlavor","jesNoFlavor")
    aliases['OTF_btagSF%sup' % shift] = {
        'expr': aliases['OTF_btagSF']['expr'].replace('Jet_btagSF_deepjet_shape', 'Jet_btagSF_deepjet_shape_up_' + shift_),
        'samples': mc
    }

    aliases['OTF_btagSF%sdown' % shift] = {
        'expr': aliases['OTF_btagSF']['expr'].replace('Jet_btagSF_deepjet_shape', 'Jet_btagSF_deepjet_shape_down_' + shift_),
        'samples': mc
    }



#aliases['Wlep_Mt']={
#    'linesToAdd':[ '.L %s/functions/GetMt.C+' % configurations], ##float GetMt(float pt1, float phi1, float m1, float pt2, float phi2, float m2 )
#    'expr':'GetMt(Lepton_pt[0],Lepton_phi[0],0,MET_CHToCB_pt_nom,PuppiMET_phi,0)'
#}

#aliases['lnjj_Mt_alt']={
#    'expr':'GetMt(Lepton_pt[0],Lepton_phi[0],0,MET_CHToCB_pt_nom,PuppiMET_phi,0,Whad_pt,Whad_phi,Whad_mass)'
#}
#

### -- PU ID SF -- ###
PUIDSFSource = '%s/src/SNuAnalytics/Configurations/TTSemiLep/patches/PUID/PUID_effAndSF_UL.root' % os.getenv('CMSSW_BASE')
aliases['Jet_PUID_SF_L'] = {
    'linesToAdd': [
        #'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
        '.L %s/patches/pujetidsf_event_new.cc+' % configurations
    ],
    'class': 'PUJetIdEventSF',
    'args': (PUIDSFSource,"UL2018","loose"),
    'samples': mc
}



#TMVA PyKeras DNN
#(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3  avg_csv_had_top
#(csv_jet0_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)*(csv_jet0_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)  2nd_moment_csv_jet0_mvaCHToCB
#(csv_jet1_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)*(csv_jet1_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)  2nd_moment_csv_jet1_mvaCHToCB
#(csv_jet2_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)*(csv_jet2_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)  2nd_moment_csv_jet2_mvaCHToCB


#aliases['avg_csv_had_top'] = {
#            'expr': '(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3'
#            }
#aliases['2nd_moment_csv_jet0_mvaCHToCB'] = {
#            'expr': '(csv_jet0_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)*(csv_jet0_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)'
#            }
#aliases['2nd_moment_csv_jet1_mvaCHToCB'] = {
#            'expr': '(csv_jet1_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)*(csv_jet1_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)'
#            }
#aliases['2nd_moment_csv_jet2_mvaCHToCB'] = {
#            'expr': '(csv_jet2_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)*(csv_jet2_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)'
#            }
#
#variable_list_high = '%s/src/SNuAnalytics/Configurations/TTSemiLep/patches/TMVAPyKerasDNN/2018/high/variables.txt' % os.getenv('CMSSW_BASE')
#aliases['score_DNN_high'] = {
#    'linesToAdd' : [
#        '.L %s/patches/TMVAPyKerasDNN/2018/high/TMVAClassification_DNN.class.C+' % configurations,
#        '.L %s/patches/tmva_pykeras_DNN.cc+' % configurations,
#    ],
#    'class': 'TMVAPyKerasDNN',
#    'args': (variable_list_high), # varialbe list txt format
#    'samples': samples.keys(),
#}


#KF_path =   '%s/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src' % os.getenv('CMSSW_BASE')
#aliases['TTKinematicFitter'] = {
#    'linesToAdd': [
#        'gSystem->Load("libCondFormatsJetMETObjects.so");',
#        #'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
#        'gSystem->AddIncludePath("-I%s/patches/KinematicFitter/include");' % configurations,
#        '.L %s/patches/KinematicFitter/src/TAbsFitConstraint.cc+' % configurations,
#        '.L %s/patches/KinematicFitter/src/TAbsFitParticle.cc+' % configurations,
#        '.L %s/patches/KinematicFitter/src/TFitConstraintM.cc+' % configurations,
#        '.L %s/patches/KinematicFitter/src/TFitConstraintMGaus.cc+' % configurations,
#        '.L %s/patches/KinematicFitter/src/TFitParticlePt.cc+' % configurations,
#        '.L %s/patches/KinematicFitter/src/TFitParticlePxPy.cc+' % configurations,
#        '.L %s/patches/KinematicFitter/src/TFitParticlePz.cc+' % configurations,
#        '.L %s/patches/KinematicFitter/src/TKinFitter_.cc+' % configurations,
#        '.L %s/patches/KinematicFitter/src/TSCorrection.cc+' % configurations,
#        '.L %s/patches/KinematicFitter/src/TKinFitterDriver.cc+' % configurations,
#        '.L %s/patches/kinematicfitter.cc+' % configurations,
#
#    ],
#    'class': 'KinematicFitter',
#    'args': ("2018"),
#    'samples': samples.keys()
#}
#
#TTKF_results = [
#'initial_dijet_M'        , 
#'initial_dijet_M_high'   ,
#'corrected_dijet_M'      ,
#'corrected_dijet_M_high' , 
#'fitted_dijet_M'         ,
#'fitted_dijet_M_high'    , 
#'best_chi2'              ,  
#'fitter_status'          ,  
#'down_type_jet_b_tagged' ,
#'hadronic_top_b_jet_idx' ,
#'leptonic_top_b_jet_idx' ,
#'w_ch_up_type_jet_idx'   , 
#'w_ch_down_type_jet_idx' , 
#'hadronic_top_b_jet_pull',   
#'w_ch_up_type_jet_pull'  , 
#'w_ch_down_type_jet_pull', 
#'hadronic_top_M'         ,  
#'leptonic_top_M'         ,   
#'leptonic_W_M'           , 
#]
#
#for iR, key in enumerate(TTKF_results):
#    aliases[key] = {
#        'expr' : 'TTKinematicFitter[%s]'%iR,
#        'samples': samples.keys()
#    }
