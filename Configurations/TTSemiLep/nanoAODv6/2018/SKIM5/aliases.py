import os
import copy
import inspect

##---WP2017---##
from WPandCut2018 import *


##-End WP--##


configurations = '%s/src/SNuAnalytics/Configurations/TTSemiLep/' % os.getenv('CMSSW_BASE')
print configurations




mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

# Jet cut

aliases['nCleanJet20_2p5'] = {
            'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5)'
            }

aliases['nCleanJet30_2p5'] = {
            'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5)'
            }

# B tagging

aliases['nBJets_WP_M'] = {
            'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.4184)'
            }


###---Btag SF---###

btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_102XSF_V1.csv' % os.getenv('CMSSW_BASE')
btagNormSource = '%s/src/SNuAnalytics/Configurations/TTSemiLep/patches/BTagReshapeNorm.root' % os.getenv('CMSSW_BASE')

aliases['Jet_btagSF_shapeFix'] = {
    'linesToAdd': [
        'gSystem->Load("libCondFormatsBTauObjects.so");',
        'gSystem->Load("libCondToolsBTau.so");',
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
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
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
        '.L %s/patches/btagnormpatch.cc+' % configurations
    ],
    'class': 'BtagReshapeNorm',
    'args': (btagNormSource,"top"),
    'samples': mc
}



aliases['btagSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(CleanJet_pt<=30 || abs(CleanJet_eta)>=2.5))))',
    'samples': mc
}

aliases['btagSFNorm_top'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFixNorm_top[CleanJet_jetIdx]+1*(CleanJet_pt<=30 || abs(CleanJet_eta)>=2.5))))',
    'samples': mc
}

#for shift in ['jes', 'lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
#    #aliases['Jet_btagSF_shapeFix_up_%s' % shift] = {                                                                                                         
#    aliases['Jet_btagSF%sup_shapeFix' % shift] = {
#        'class': 'BtagSF',
#        'args': (btagSFSource, 'up_' + shift),
#        'samples': mc
#    }
#    aliases['Jet_btagSF%sdown_shapeFix' % shift] = {
#        'class': 'BtagSF',
#        'args': (btagSFSource, 'down_' + shift),
#        'samples': mc
#    }
# 
#    aliases['btagSF%sup' % shift] = {
#        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
#        'samples': mc
#    }
#
#    aliases['btagSF%sdown' % shift] = {
#        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
#        'samples': mc
#    }
#


#aliases['Wlep_Mt']={
#    'linesToAdd':[ '.L %s/functions/GetMt.C+' % configurations], ##float GetMt(float pt1, float phi1, float m1, float pt2, float phi2, float m2 )
#    'expr':'GetMt(Lepton_pt[0],Lepton_phi[0],0,PuppiMET_pt,PuppiMET_phi,0)'
#}

#aliases['lnjj_Mt_alt']={
#    'expr':'GetMt(Lepton_pt[0],Lepton_phi[0],0,PuppiMET_pt,PuppiMET_phi,0,Whad_pt,Whad_phi,Whad_mass)'
#}
#

### -- PU ID SF -- ###
PUIDSFSource = '%s/src/LatinoAnalysis/NanoGardener/python/data/JetPUID_effcyandSF.root' % os.getenv('CMSSW_BASE')

aliases['Jet_PUID_SF_L'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
        '.L %s/patches/pujetidsf_event.cc+' % configurations
    ],
    'class': 'PUJetIdEventSF',
    'args': (PUIDSFSource,"2018","loose"),
    'samples': mc
}
