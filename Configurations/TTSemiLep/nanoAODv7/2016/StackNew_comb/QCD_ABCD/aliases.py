import os
import copy
import inspect

##---WP2016---##
from WPandCut2016 import *


##-End WP--##


configurations = '%s/src/SNuAnalytics/Configurations/TTSemiLep' % os.getenv('CMSSW_BASE')
print configurations




mc   = [skey for skey in samples if skey not in ('Fake', 'DATA')]

# veto loose lepton

aliases['nLooseLep'] = {
        'expr': 'Sum$( abs(Lepton_pdgId) == 11 && Lepton_pt > 15. && abs(Lepton_eta) < 2.5) + Sum$( abs(Lepton_pdgId) == 13 && Lepton_pt > 15. && abs(Lepton_eta) < 2.4)'
        #'expr': 'Sum$(Electron_cutBased_Fall17_V1 >= 2 && Electron_pt > 15. && abs(Electron_eta) < 2.5) + Sum$(Muon_looseId > 0.5 && Muon_pt > 8. && abs(Muon_eta) < 2.4)'
        }

# Electron_cutBased_Fall17_V1 >= 2 : 2 is loose, 3 is medium, 4 is tight
# nLooseLep == 1 is required for single lepton channel
# (tight lepton with additional loose lepton)     > (1 loose lepton) > (1 tight lepton with no additional lepton)
# nLooseLep == 2 is required for di-lepton channel
# (tight two lepton with additional loose lepton) > (2 loose lepton) > (2 tight lepton with no additional lepton)


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
#Electron_vidNestedWPBitmap 
#0 - MinPtCut
#1 - GsfEleSCEtaMultiRangeCut
#2 - GsfEleDEtaInSeedCut
#3 - GsfEleDPhiInCut
#4 - GsfEleFull5x5SigmaIEtaIEtaCut
#5 - GsfEleHadronicOverEMEnergyScaledCut
#6 - GsfEleEInverseMinusPInverseCut
#7 - GsfEleRelPFIsoScaledCut
#8 - GsfEleConversionVetoCut
#9 - GsfEleMissingHitsCut
#(abs(Lepton_EtaSC[0])< 1.479)
# medium 0.0478+0.506/pT
# tight  0.0287+0.506/pT
# (medium - tight) = 0.0191       ->                 #up
# (medium - tight)*(3/4) = 0.0143 -> 0.043 +0.506/pT #nominal
# (medium - tight)*(1/2) = 0.0096 -> 0.0383+0.506/pT #down
#(abs(Lepton_EtaSC[0])>= 1.479)
# medium 0.0658+0.963/pT
# tight  0.0445+0.963/pT
# (medium - tight) = 0.0213       ->                 #up
# (medium - tight)*(3/4) = 0.0160 -> 0.0605+0.963/pT #nominal
# (medium - tight)*(1/2) = 0.0107 -> 0.0552+0.963/pT #down

aliases['eleCH_noTight'] = {
        'expr' : '(   (abs(Lepton_pdgId[0])==11)\
                   && (Lepton_isTightElectron_d0dz_'+eleWP+'[0]<0.5)\
                   && Alt$(Electron_vidNestedWPBitmap[Lepton_electronIdx[0]] == (4 + 4<<(3*1) + 4<<(3*2) + 4<<(3*3) + 4<<(3*4) + 4<<(3*5) + 4<<(3*6) + 3<<(3*7) + 4<<(3*8) + 4<<(3*9)),0)\
                   && (   (abs(Lepton_EtaSC[0])< 1.479)*(Electron_pfRelIso03_all[Lepton_electronIdx[0]] <0.043 +0.506/Lepton_pt[0])\
                       || (abs(Lepton_EtaSC[0])>=1.479)*(Electron_pfRelIso03_all[Lepton_electronIdx[0]] <0.0605+0.963/Lepton_pt[0])\
                   )\
                   && Lepton_electron_d0dz_cut[0]\
                   && (Lepton_pt[0] > '+elePtCut+')\
                   && (fabs(Lepton_eta[0]) < 2.5)\
                  )',
        }

aliases['eleCH_noTight_isoDown'] = {
        'expr' : '(   (abs(Lepton_pdgId[0])==11)\
                   && (Lepton_isTightElectron_d0dz_'+eleWP+'[0]<0.5)\
                   && Alt$(Electron_vidNestedWPBitmap[Lepton_electronIdx[0]] == (4 + 4<<(3*1) + 4<<(3*2) + 4<<(3*3) + 4<<(3*4) + 4<<(3*5) + 4<<(3*6) + 3<<(3*7) + 4<<(3*8) + 4<<(3*9)),0)\
                   && (   (abs(Lepton_EtaSC[0])< 1.479)*(Electron_pfRelIso03_all[Lepton_electronIdx[0]] <0.0383+0.506/Lepton_pt[0])\
                       || (abs(Lepton_EtaSC[0])>=1.479)*(Electron_pfRelIso03_all[Lepton_electronIdx[0]] <0.0552+0.963/Lepton_pt[0])\
                   )\
                   && Lepton_electron_d0dz_cut[0]\
                   && (Lepton_pt[0] > '+elePtCut+')\
                   && (fabs(Lepton_eta[0]) < 2.5)\
                  )',
        }
aliases['eleCH_noTight_isoUp'] = {
        'expr' : '(   (abs(Lepton_pdgId[0])==11)\
                   && (Lepton_isTightElectron_d0dz_'+eleWP+'[0]<0.5)\
                   && Alt$(Electron_vidNestedWPBitmap[Lepton_electronIdx[0]] == (4 + 4<<(3*1) + 4<<(3*2) + 4<<(3*3) + 4<<(3*4) + 4<<(3*5) + 4<<(3*6) + 3<<(3*7) + 4<<(3*8) + 4<<(3*9)),0)\
                   && Lepton_electron_d0dz_cut[0]\
                   && (Lepton_pt[0] > '+elePtCut+')\
                   && (fabs(Lepton_eta[0]) < 2.5)\
                  )',
        }
aliases['muCH_noTight'] = {
        'expr' : '(   (abs(Lepton_pdgId[0])==13)\
                   && (Lepton_isTightMuon_'+muWP+'[0]<0.5)\
                   && (Alt$(Muon_tightId[Lepton_muonIdx[0]],-1)==1)\
                   && (Alt$(Muon_pfRelIso04_all[Lepton_muonIdx[0]],999)<0.20)\
                   && (Lepton_pt[0] > '+muPtCut+')\
                   && (fabs(Lepton_eta[0]) < 2.4)\
                  )',
        }
aliases['muCH_noTight_isoDown'] = {
        'expr' : '(   (abs(Lepton_pdgId[0])==13)\
                   && (Lepton_isTightMuon_'+muWP+'[0]<0.5)\
                   && (Alt$(Muon_tightId[Lepton_muonIdx[0]],-1)==1)\
                   && (Alt$(Muon_pfRelIso04_all[Lepton_muonIdx[0]],999)<0.175)\
                   && (Lepton_pt[0] > '+muPtCut+')\
                   && (fabs(Lepton_eta[0]) < 2.4)\
                  )',
        }
aliases['muCH_noTight_isoUp'] = {
        'expr' : '(   (abs(Lepton_pdgId[0])==13)\
                   && (Lepton_isTightMuon_'+muWP+'[0]<0.5)\
                   && (Alt$(Muon_tightId[Lepton_muonIdx[0]],-1)==1)\
                   && (Alt$(Muon_pfRelIso04_all[Lepton_muonIdx[0]],999)<0.225)\
                   && (Lepton_pt[0] > '+muPtCut+')\
                   && (fabs(Lepton_eta[0]) < 2.4)\
                  )',
        }
aliases['isOSpair'] = {
        'expr' : 'Lepton_pdgId[0]*Alt$(Lepton_pdgId[1],-999)<0',
        }
#XXX rearrange code later
aliases['TightElWithCut'] = {
        'expr' : '(   (abs(Lepton_pdgId)==11)\
                   && (Lepton_isTightElectron_d0dz_'+eleWP+'>0.5)\
                   && (Lepton_pt > '+elePtCut+')\
                   && (fabs(Lepton_eta) < 2.5)\
                  )',
        }

#######
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


#  number of truth leptons in TT

aliases['nLHELep_TT'] = {
            'expr': 'Sum$(abs(LHEPart_pdgId)==11 || abs(LHEPart_pdgId)==13 ||abs(LHEPart_pdgId)==15)',
            'samples': [ sample for sample in mc if 'TTLJ' in sample or 'TTLL' in sample ]
            }

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
    'args': (30.,2.4), # pT, |eta| cut
    'samples': samples.keys(),
}


# B tagging

aliases['nBJets_WP_M'] = {
            'expr': 'Sum$(Jet_pt_nom[CleanJet_jetIdx] > 30. && abs(CleanJet_eta) < 2.4 && Jet_btagDeepFlavB[CleanJet_jetIdx] > 0.3093 )'
            }

aliases['nBJets_WP_M_25to30'] = {
            'expr': 'Sum$(Jet_pt_nom[CleanJet_jetIdx] > 25. && Jet_pt_nom[CleanJet_jetIdx] <= 30. && abs(CleanJet_eta) < 2.4 && Jet_btagDeepFlavB[CleanJet_jetIdx] > 0.3093 )'
            }




###---Btag SF---###

btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepJet_2016LegacySF_V1.csv' % os.getenv('CMSSW_BASE')
btagNormSource = '%s/src/SNuAnalytics/Configurations/TTSemiLep/patches/BTagReshapeNorm_2016.root' % os.getenv('CMSSW_BASE')

aliases['Jet_btagSF_shapeFix'] = {
    'linesToAdd': [
        'gSystem->Load("libCondFormatsBTauObjects.so");',
        'gSystem->Load("libCondToolsBTau.so");',
        #'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
        '.L %s/patches/btagsfpatch.cc+' % configurations
    ],
    'class': 'BtagSF',
    'args': (btagSFSource,),
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
        'expr': 'TMath::Exp(Sum$(TMath::Log(((Jet_pt_nom[CleanJet_jetIdx]>25 && abs(CleanJet_eta)<2.4))*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(Jet_pt_nom[CleanJet_jetIdx]<=25 || abs(CleanJet_eta)>=2.4))))',
    'samples': mc
}
aliases['btagSFNorm_top'] = {
    #'expr': 'TMath::Exp(Sum$(TMath::Log((Jet_pt_nom[CleanJet_jetIdx]>30 && abs(CleanJet_eta)<2.4)*Jet_btagSF_shapeFixNorm_top[CleanJet_jetIdx]+1*(Jet_pt_nom[CleanJet_jetIdx]<=30 || abs(CleanJet_eta)>=2.4))))',
    'expr' : '1',
    'samples': mc
}


for shift in ['jes', 'lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
    #aliases['Jet_btagSF_shapeFix_up_%s' % shift] = {                                                                                                         
    aliases['Jet_btagSF%sup_shapeFix' % shift] = {
        'class': 'BtagSF',
        'args': (btagSFSource, 'up_' + shift),
        'samples': mc
    }
    aliases['Jet_btagSF%sdown_shapeFix' % shift] = {
        'class': 'BtagSF',
        'args': (btagSFSource, 'down_' + shift),
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

### -- electron trigger efficiency SF -- ###
EleTrigEffSFSource = '%s/src/SNuAnalytics/Configurations/TTSemiLep/patches/scale_factors/egammaEffi.txt_EGM2D_2016runBCDEFGH_passTight_HLT_Ele30_WPTight_BHO.root' % os.getenv('CMSSW_BASE')
EleTrigEffSFHistName = 'EGamma_SF2D'
#EleTrigEffSFSource = '%s/src/SNuAnalytics/Configurations/TTSemiLep/patches/scale_factors/EleTrigEffAndSF.root' % os.getenv('CMSSW_BASE')
#EleTrigEffSFHistName   = 'SF_2016BCDEFGH_SF'
#EleTrigEffSFHistName_u = 'SF_up_2016BCDEFGH_SF_up'
#EleTrigEffSFHistName_d = 'SF_down_2016BCDEFGH_SF_down'

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
MuTrigEffSFSource_RunBtoF = '%s/src/SNuAnalytics/Configurations/TTSemiLep/patches/scale_factors/EfficienciesAndSF_RunBtoF.root' % os.getenv('CMSSW_BASE')
MuTrigEffSFHistName_RunBtoF = 'IsoMu24_OR_IsoTkMu24_PtEtaBins/abseta_pt_ratio'

aliases['OTF_SingleMuTrig_SF_RunBtoF'] = {
    'linesToAdd': [
        '.L %s/patches/leptonsf.cc+' % configurations
    ],
    'class': 'LeptonSF',
    'args': (MuTrigEffSFSource_RunBtoF,MuTrigEffSFHistName_RunBtoF,'etapt'),
    #'samples': mc

}
MuTrigEffSFSource_Period4 = '%s/src/SNuAnalytics/Configurations/TTSemiLep/patches/scale_factors/EfficienciesAndSF_Period4.root' % os.getenv('CMSSW_BASE')
MuTrigEffSFHistName_Period4 = 'IsoMu24_OR_IsoTkMu24_PtEtaBins/abseta_pt_ratio'

aliases['OTF_SingleMuTrig_SF_Period4'] = {
    'linesToAdd': [
        '.L %s/patches/leptonsf.cc+' % configurations
    ],
    'class': 'LeptonSF',
    'args': (MuTrigEffSFSource_Period4,MuTrigEffSFHistName_Period4,'etapt'),
    #'samples': mc

}

# lumi. RunBtoF : 19.720 / fb, RunGH : 16.146 /fb
aliases['OTF_SingleMuTrig_SF'] = {
    'expr' : '(OTF_SingleMuTrig_SF_RunBtoF * 19.720  + OTF_SingleMuTrig_SF_Period4 * 16.146  )/(19.720 + 16.146)',
}

### lepton eff.
EleTrigEffMCHistName   = 'EGamma_EffMC2D'
MuTrigEffMCHistName    = 'IsoMu24_OR_IsoTkMu24_PtEtaBins/efficienciesMC/abseta_pt_MC'
EleTrigEffDATAHistName = 'EGamma_EffData2D'
MuTrigEffDATAHistName  = 'IsoMu24_OR_IsoTkMu24_PtEtaBins/efficienciesDATA/abseta_pt_DATA'

aliases['OTF_SingleTrig_MC_Eff_RunBtoF'] = {
    'linesToAdd': [
        '.L %s/patches/leptoneff.cc+' % configurations
    ],
    'class': 'LeptonEff',
    'args': (EleTrigEffSFSource,MuTrigEffSFSource_RunBtoF,EleTrigEffMCHistName,MuTrigEffMCHistName,'etapt','etapt'),
    'samples': mc
}
aliases['OTF_SingleTrig_MC_Eff_Period4'] = {
    'linesToAdd': [
        '.L %s/patches/leptoneff.cc+' % configurations
    ],
    'class': 'LeptonEff',
    'args': (EleTrigEffSFSource,MuTrigEffSFSource_Period4,EleTrigEffMCHistName,MuTrigEffMCHistName,'etapt','etapt'),
    'samples': mc
}
# lumi. RunBtoF : 19.720 / fb, RunGH : 16.146 /fb
aliases['OTF_SingleTrig_MC_Eff'] = {
    'expr' : '(OTF_SingleTrig_MC_Eff_RunBtoF * 19.720  + OTF_SingleTrig_MC_Eff_Period4 * 16.146  )/(19.720 + 16.146)',
    'samples': mc
}


aliases['OTF_SingleTrig_DATA_Eff_RunBtoF'] = {
    'linesToAdd': [
        '.L %s/patches/leptoneff.cc+' % configurations
    ],
    'class': 'LeptonEff',
    'args': (EleTrigEffSFSource,MuTrigEffSFSource_RunBtoF,EleTrigEffDATAHistName,MuTrigEffDATAHistName,'etapt','etapt'),
    'samples': mc
}
aliases['OTF_SingleTrig_DATA_Eff_Period4'] = {
    'linesToAdd': [
        '.L %s/patches/leptoneff.cc+' % configurations
    ],
    'class': 'LeptonEff',
    'args': (EleTrigEffSFSource,MuTrigEffSFSource_Period4,EleTrigEffDATAHistName,MuTrigEffDATAHistName,'etapt','etapt'),
    'samples': mc
}
# lumi. RunBtoF : 19.720 / fb, RunGH : 16.146 /fb
aliases['OTF_SingleTrig_DATA_Eff'] = {
    'expr' : '(OTF_SingleTrig_DATA_Eff_RunBtoF * 19.720  + OTF_SingleTrig_DATA_Eff_Period4 * 16.146  )/(19.720 + 16.146)',
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
    'args': (PUIDSFSource,"2016","loose"),
    'samples': mc
}

aliases['SelectedJetIdx'] = {
    'linesToAdd' : [
        '.L %s/patches/selectedjet.cc+' % configurations,
    ],
    'class': 'SelectedJet',
    'args': (30.,2.4), # pT, |eta| cut
    'samples': samples.keys(),
}
#aliases['topGen'] = {
#    'expr' : '(GenPart_pdgId == 6) && (GenPart_statusFlags >> 13 & 1)',
#    'samples': ['TTLL','TTLJ']
#}
#aliases['topGenPt'] = {
#    'expr' : '(Sum$(topGen==1)==1)*Sum$((topGen==1)*GenPart_pt)',
#    'samples': ['TTLL','TTLJ']
#}
#aliases['antitopGen'] = {
#    'expr' : '(GenPart_pdgId == -6) && (GenPart_statusFlags >> 13 & 1)',
#    'samples': ['TTLL','TTLJ']
#}
#aliases['antitopGenPt'] = {
#    'expr' : '(Sum$(antitopGen==1)==1)*Sum$((antitopGen==1)*GenPart_pt)',
#    'samples': ['TTLL','TTLJ']
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
