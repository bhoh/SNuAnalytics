import os
import copy
import inspect

##---WP2017---##
from WPandCut2017 import *


##-End WP--##


configurations = '%s/src/SNuAnalytics/Configurations/TTSemiLep' % os.getenv('CMSSW_BASE')
print configurations

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

# veto loose lepton

aliases['nLooseLep'] = {
        'expr': 'Sum$( abs(Lepton_pdgId) == 11 && Lepton_pt > 15. && abs(Lepton_eta) < 2.5) + Sum$( abs(Lepton_pdgId) == 13 && Lepton_pt > 15. && abs(Lepton_eta) < 2.4)'
        #'expr': 'Sum$(Electron_cutBased_Fall17_V1 >= 2 && Electron_pt > 15. && abs(Electron_eta) < 2.5) + Sum$(Muon_looseId > 0.5 && Muon_pt > 8. && abs(Muon_eta) < 2.4)'
        }

# lepton cut
aliases['Lepton_EtaSC'] = {
        'expr' : 'Lepton_eta + (Lepton_electronIdx>=0)*Alt$(Electron_deltaEtaSC[(Lepton_electronIdx>=0)*Lepton_electronIdx],0)'
        }
aliases['Lepton_electron_dxy'] = {
        'expr' : 'Alt$(Electron_dxy[(Lepton_electronIdx>=0)*Lepton_electronIdx],999)'
        }
aliases['Lepton_electron_dz'] = {
        'expr' : 'Alt$(Electron_dz[(Lepton_electronIdx>=0)*Lepton_electronIdx],999)'
        }
aliases['Lepton_electron_gap_veto'] = {
        'expr' : 'abs(Lepton_EtaSC) >1.56 || abs(Lepton_EtaSC) < 1.4442'
        }
aliases['Lepton_electron_d0dz_cut'] = {
        'expr' : '(({barrelCut}) || ({endcapCut}))'.format(
                      barrelCut='abs(Lepton_EtaSC) <  1.479 && abs(Lepton_electron_dxy)<0.05 && abs(Lepton_electron_dz)<0.1',
                      endcapCut='abs(Lepton_EtaSC) >= 1.479 && abs(Lepton_electron_dxy)<0.1  && abs(Lepton_electron_dz)<0.2'
            )
        }

aliases['Lepton_isTightElectron_d0dz_'+eleWP] = {
        #'expr' : 'Lepton_isTightElectron_{eleWP}'.format(eleWP=eleWP), #debug
        'expr' : 'Lepton_isTightElectron_{eleWP} && (Lepton_electron_d0dz_cut) && Lepton_electron_gap_veto'.format(eleWP=eleWP)
        }

aliases['eleCH'] = {
        'expr' : '(   (abs(Lepton_pdgId[0])==11)\
                   && (Lepton_isTightElectron_d0dz_'+eleWP+'[0]>0.5)\
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
                   && (Lepton_isTightElectron_d0dz_'+eleWP+'[0]>0.5)\
                   && (Lepton_pt[0] > '+eePtCut[0]+')\
                   && (fabs(Lepton_eta[0]) < 2.5)\
                   && (abs(Alt$(Lepton_pdgId[1],-999))==11)\
                   && (Alt$(Lepton_isTightElectron_d0dz_'+eleWP+'[1],-999)>0.5)\
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
                   && (Lepton_isTightElectron_d0dz_'+eleWP+'[0]>0.5)\
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
                   && (Alt$(Lepton_isTightElectron_d0dz_'+eleWP+'[1],-999)>0.5)\
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



# Jet cut

aliases['nCleanJet20_2p5'] = {
            'expr': 'Sum$(Jet_pt_nom[CleanJet_jetIdx] > 20. && abs(CleanJet_eta) < 2.5)'
            }

aliases['nCleanJet20to30_2p5_PU_M'] = {
            'expr': 'Sum$(Jet_pt_nom[CleanJet_jetIdx] > 20. && Jet_pt_nom[CleanJet_jetIdx] <= 30. && abs(CleanJet_eta) < 2.5 && (Jet_puId[CleanJet_jetIdx] & (1 << 1)) )'
            }

aliases['nCleanJet30_2p5'] = {
            'expr': 'Sum$(Jet_pt_nom[CleanJet_jetIdx] > 30. && abs(CleanJet_eta) < 2.5)'
            }

aliases['SelectedJetIdx'] = {
    'linesToAdd' : [
        '.L %s/patches/selectedjet.cc+' % configurations,
    ],
    'class': 'SelectedJet',
    'args': (30.,2.5), # pT, |eta| cut
    'samples': samples.keys(),
}
aliases['SelectedBJetIdx'] = {
    'linesToAdd' : [
        '.L %s/patches/selectedbjet.cc+' % configurations,
    ],
    'class': 'SelectedBJet',
    'args': (20.,2.5, 0.), # pT, |eta| cut, csv cut(not used variable)
    'samples': samples.keys(),
}

# B tagging

aliases['nBJets_WP_M'] = {
            'expr': 'Sum$(Jet_pt_nom[CleanJet_jetIdx] > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepFlavB[CleanJet_jetIdx] > 0.3033 )'
            }

aliases['nBJets_WP_M_20to30'] = {
            'expr': 'Sum$(Jet_pt_nom[CleanJet_jetIdx] > 20. && Jet_pt_nom[CleanJet_jetIdx] <= 30. && abs(CleanJet_eta) < 2.5 && (Jet_puId[CleanJet_jetIdx] & (1 << 1)) && Jet_btagDeepFlavB[CleanJet_jetIdx] > 0.3033)'
            }

###---Btag SF---###

btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepFlavour_94XSF_V4_B_F_JESreduced.csv' % os.getenv('CMSSW_BASE')
btagNormSource = '%s/src/SNuAnalytics/Configurations/TTSemiLep/patches/BTagReshapeNorm_2017.root' % os.getenv('CMSSW_BASE')

aliases['Jet_btagSF_shapeFix'] = {
    'linesToAdd': [
        'gSystem->Load("libCondFormatsBTauObjects.so");',
        'gSystem->Load("libCondToolsBTau.so");',
        #'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
        '.L %s/patches/btagsfpatch.cc+' % configurations
    ],
    'class': 'BtagSF',
    'args': (btagSFSource, "central", "2017", "deepjet"),
    'samples': mc
}

aliases['Jet_btagSF_shapeFixNorm_top'] = {
    'linesToAdd': [
        'gSystem->Load("libCondFormatsBTauObjects.so");',
        'gSystem->Load("libCondToolsBTau.so");',
        #'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
        '.L %s/patches/btagnormpatch.cc+' % configurations
    ],
    'class': 'BtagReshapeNorm',
    'args': (btagNormSource,"top"),
    'samples': mc
}

aliases['btagSF'] = {
        'expr': 'TMath::Exp(Sum$(TMath::Log(((Jet_pt_nom[CleanJet_jetIdx]>30 && abs(CleanJet_eta)<2.5))*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(Jet_pt_nom[CleanJet_jetIdx]<=30 || abs(CleanJet_eta)>=2.5)))+Sum$(TMath::Log(((Jet_pt_nom[CleanJet_jetIdx]>20 && Jet_pt_nom[CleanJet_jetIdx]<=30 && (Jet_puId[CleanJet_jetIdx] & (1<<1)) && abs(CleanJet_eta)<2.5))*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(Jet_pt_nom[CleanJet_jetIdx]<=20 || Jet_pt_nom[CleanJet_jetIdx]>30 || !(Jet_puId[CleanJet_jetIdx] & (1<<1))|| abs(CleanJet_eta)>=2.5))))',
    'samples': mc
}
aliases['btagSFNorm_top'] = {
    #'expr': 'TMath::Exp(Sum$(TMath::Log((Jet_pt_nom[CleanJet_jetIdx]>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFixNorm_top[CleanJet_jetIdx]+1*(Jet_pt_nom[CleanJet_jetIdx]<=30 || abs(CleanJet_eta)>=2.5))))',
    'expr' : '1',
    'samples': mc
}

jes_syst_uncorr = ['jesAbsolute_2017','jesBBEC1_2017','jesEC2_2017','jesHF_2017','jesRelativeSample_2017']
jes_syst_corr = ['jesAbsolute','jesBBEC1','jesEC2','jesFlavorQCD','jesHF','jesRelativeBal']
jes_syst = jes_syst_uncorr + jes_syst_corr
for shift in jes_syst + ['lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
    #aliases['Jet_btagSF_shapeFix_up_%s' % shift] = {                                                                                                         
    aliases['Jet_btagSF%sup_shapeFix' % shift] = {
        'class': 'BtagSF',
        'args': (btagSFSource, 'up_' + shift, "2017", "deepjet"),
        'samples': mc
    }
    aliases['Jet_btagSF%sdown_shapeFix' % shift] = {
        'class': 'BtagSF',
        'args': (btagSFSource, 'down_' + shift, "2017", "deepjet"),
        'samples': mc
    }
 
    aliases['btagSF%sup' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
        'samples': mc
    }

    aliases['btagSF%sdown' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
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
### -- electron trigger obj. -- ###
aliases['TrigMatching_sngEl'] = {
            'expr': 'Sum$(TrigObj_filterBits & 1024 && TrigObj_id == 11) > 0'
            }

### -- electron trigger efficiency SF -- ###
#EleTrigEffSFSource = '%s/src/SNuAnalytics/Configurations/TTSemiLep/patches/scale_factors/EleTrigEffAndSF.root' % os.getenv('CMSSW_BASE')
#EleTrigEffSFHistName   = 'SF_2017BCDEF_SF'
#EleTrigEffSFHistName_u = 'SF_up_2017BCDEF_SF_up'
#EleTrigEffSFHistName_d = 'SF_down_2017BCDEF_SF_down'
#POG
EleTrigEffSFSource = '%s/src/SNuAnalytics/Configurations/TTSemiLep/patches/scale_factors/egammaEffi.txt_EGM2D_2017runBCDEF_passTight_HLT_Ele32_WPTight_BHO.root' % os.getenv('CMSSW_BASE')
EleTrigEffSFHistName = 'EGamma_SF2D'

aliases['OTF_SingleEleTrig_SF'] = {
    'linesToAdd': [
        '.L %s/patches/leptonsf.cc+' % configurations
    ],
    'class': 'LeptonSF',
    'args': (EleTrigEffSFSource,EleTrigEffSFHistName, 'etapt'),
    #'samples': mc

}
#aliases['OTF_SingleEleTrig_SF_u'] = {
#    'linesToAdd': [
#        '.L %s/patches/leptonsf.cc+' % configurations
#    ],
#    'class': 'LeptonSF',
#    'args': (EleTrigEffSFSource,EleTrigEffSFHistName_u, 'etapt'),
#    #'samples': mc
#
#}
#
#aliases['OTF_SingleEleTrig_SF_d'] = {
#    'linesToAdd': [
#        '.L %s/patches/leptonsf.cc+' % configurations
#    ],
#    'class': 'LeptonSF',
#    'args': (EleTrigEffSFSource,EleTrigEffSFHistName_d, 'etapt'),
#    #'samples': mc
#
#}
### -- muon trigger efficiency SF -- ###
MuTrigEffSFSource_RunBtoF = '%s/src/SNuAnalytics/Configurations/TTSemiLep/patches/scale_factors/EfficienciesAndSF_RunBtoF_Nov17Nov2017.root' % os.getenv('CMSSW_BASE')
MuTrigEffSFHistName_RunBtoF = 'IsoMu27_PtEtaBins/abseta_pt_ratio'

aliases['OTF_SingleMuTrig_SF'] = {
    'linesToAdd': [
        '.L %s/patches/leptonsf.cc+' % configurations
    ],
    'class': 'LeptonSF',
    'args': (MuTrigEffSFSource_RunBtoF,MuTrigEffSFHistName_RunBtoF,'etapt'),
    #'samples': mc

}
### lepton eff.
EleTrigEffMCHistName   = 'EGamma_EffMC2D'
MuTrigEffMCHistName    = 'IsoMu27_PtEtaBins/efficienciesMC/abseta_pt_MC'
EleTrigEffDATAHistName = 'EGamma_EffData2D'
MuTrigEffDATAHistName  = 'IsoMu27_PtEtaBins/efficienciesDATA/abseta_pt_DATA'

aliases['OTF_SingleTrig_MC_Eff'] = {
    'linesToAdd': [
        '.L %s/patches/leptoneff.cc+' % configurations
    ],
    'class': 'LeptonEff',
    'args': (EleTrigEffSFSource,MuTrigEffSFSource_RunBtoF,EleTrigEffMCHistName,MuTrigEffMCHistName,'etapt','etapt'),
    'samples': mc
}

aliases['OTF_SingleTrig_DATA_Eff'] = {
    'linesToAdd': [
        '.L %s/patches/leptoneff.cc+' % configurations
    ],
    'class': 'LeptonEff',
    'args': (EleTrigEffSFSource,MuTrigEffSFSource_RunBtoF,EleTrigEffDATAHistName,MuTrigEffDATAHistName,'etapt','etapt'),
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
trig_ele_syst    = '((nLooseLep==1)*(eleCH*OTF_SingleEleTrig_SF[0]+muCH) + (nLooseLep==2)*((!mmCH)*Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)+mmCH))'
trig_ele_syst_u  = trig_ele_syst.replace('OTF_SingleEleTrig_SF[0]','OTF_SingleEleTrig_SF[1]').replace('Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)','Alt$(OTF_SingleTrig_DATA_Eff[1]/OTF_SingleTrig_MC_Eff[2],1)')
trig_ele_syst_d  = trig_ele_syst.replace('OTF_SingleEleTrig_SF[0]','OTF_SingleEleTrig_SF[2]').replace('Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)','Alt$(OTF_SingleTrig_DATA_Eff[2]/OTF_SingleTrig_MC_Eff[1],1)')
trig_mu_syst    = '((nLooseLep==1)*(muCH*OTF_SingleMuTrig_SF[0]+eleCH) + (nLooseLep==2)*((!eeCH)*Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)+eeCH))'
trig_mu_syst_u  = trig_mu_syst.replace('OTF_SingleMuTrig_SF[0]','OTF_SingleMuTrig_SF[1]').replace('Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)','Alt$(OTF_SingleTrig_DATA_Eff[3]/OTF_SingleTrig_MC_Eff[4],1)')
trig_mu_syst_d  = trig_mu_syst.replace('OTF_SingleMuTrig_SF[0]','OTF_SingleMuTrig_SF[2]').replace('Alt$(OTF_SingleTrig_DATA_Eff[0]/OTF_SingleTrig_MC_Eff[0],1)','Alt$(OTF_SingleTrig_DATA_Eff[4]/OTF_SingleTrig_MC_Eff[3],1)')

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

### -- PU ID SF -- ###
PUIDSFSource = '%s/src/LatinoAnalysis/NanoGardener/python/data/PUID_80XTraining_EffSFandUncties.root' % os.getenv('CMSSW_BASE')
aliases['Jet_PUID_SF_L'] = {
    'linesToAdd': [
        #'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
        '.L %s/patches/pujetidsf_event_new.cc+' % configurations
    ],
    'class': 'PUJetIdEventSF',
    'args': (PUIDSFSource,"2017","loose"),
    'samples': mc
}
aliases['SelectedJetIdx'] = {
    'linesToAdd' : [
        '.L %s/patches/selectedjet.cc+' % configurations,
    ],
    'class': 'SelectedJet',
    'args': (30.,2.5), # pT, |eta| cut
    'samples': samples.keys(),
}
#aliases['topGen'] = {
#    'expr' : '(GenPart_pdgId == 6) && (GenPart_statusFlags >> 13 & 1)',
#    'samples': ['TTLJ']
#}
#aliases['topGenPt'] = {
#    'expr' : '(Sum$(topGen==1)==1)*Sum$((topGen==1)*GenPart_pt)',
#    'samples': ['TTLJ']
#}
#aliases['antitopGen'] = {
#    'expr' : '(GenPart_pdgId == -6) && (GenPart_statusFlags >> 13 & 1)',
#    'samples': ['TTLJ']
#}
#aliases['antitopGenPt'] = {
#    'expr' : '(Sum$(antitopGen==1)==1)*Sum$((antitopGen==1)*GenPart_pt)',
#    'samples': ['TTLJ']
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
#    'args': ("2017"),
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
