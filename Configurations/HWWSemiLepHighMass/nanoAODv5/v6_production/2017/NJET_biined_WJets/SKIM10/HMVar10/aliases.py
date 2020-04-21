import os
import copy
import inspect

##---WP2017---##
from WPandCut2017 import *
_ALGO="_"+ALGO

##-End WP--##


configurations = '%s/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/' % os.getenv('CMSSW_BASE')
print configurations




mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]





###---Btag SF---###
btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_94XSF_V2_B_F.csv' % os.getenv('CMSSW_BASE')
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
aliases['btagSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
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



##--PUID
puidSFSource = '%s/src/LatinoAnalysis/NanoGardener/python/data/JetPUID_effcyandSF.root' % os.getenv('CMSSW_BASE')
aliases['PUJetIdSF'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
        '.L %s/patches/pujetidsf_event.cc+' % configurations
    ],
    'class': 'PUJetIdEventSF',
    'args': (puidSFSource, '2017', 'loose'),
    'samples': mc
}



###--Tau21 ID eff. SF
aliases['tau21SFnom']={
    'expr' : tau21SF+'*(isBoost_'+WTAG+'_nom) + 1*(!isBoost_'+WTAG+'_nom)',
    'samples' : mc
}
aliases['tau21SFup']={
    'expr' : tau21SFup+'*(isBoost_'+WTAG+'_nom) + 1*(!isBoost_'+WTAG+'_nom)',
    'samples' : mc
}
aliases['tau21SFdown']={
    'expr' : tau21SFdown+'*(isBoost_'+WTAG+'_nom) + 1*(!isBoost_'+WTAG+'_nom)',
    'samples' : mc
}


##---TrigSF
aliases['trigWeight']={
    'expr' : 'TriggerEffWeight_1l*'+'(Lepton_isTightMuon_'+muWP+'[0]>0.5) + Trigger_sngEl*(Lepton_isTightElectron_'+eleWP+'[0]>0.5)', ##eletron trig_eff_SF isnot valid yet
    'samples':mc
}
##--Lepton ISO/ID/RECO
aliases['LepWPweight']={
    'expr':'(((Lepton_isTightElectron_'+eleWP+'[0]>0.5)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]'+')) + ((Lepton_isTightMuon_'+muWP+'[0]>0.5)*(Lepton_tightMuon_'+muWP+'_TotSF'+'[0]'+')))',
    'samples':mc
}

aliases['SFweight']={
    'expr':'puWeight*trigWeight*EMTFbug_veto*PrefireWeight*LepWPweight*btagSF*PUJetIdSF',
    'samples':mc
}



aliases['nJetPassBKin']={
    'expr':'Sum$(CleanJet_pt>20 && abs(CleanJet_eta)<2.5)'
}

aliases['JetMultplicity']={
    'expr':'Sum$(CleanJet_pt>'+jetptmin+' && abs(CleanJet_eta)<'+jetetamax+')'
}

aliases['JetMultplicity_eta4p7']={
    'expr':'Sum$(CleanJet_pt>'+jetptmin+' && abs(CleanJet_eta)<4.7)'
}


for M_MELA in MELA_MASS_BOOST:
    M=str(M_MELA)
    P_S='meP'+M+'_Bst_ggf_S_'+WTAG+'_nom'
    P_B='meP'+M+'_Bst_ggf_B_'+WTAG+'_nom'
    P_S_B=P_B+'/'+P_S
    aliases['MEKD_'+str(M)]={
        'expr':'1/(1+'+P_S_B+')'
    }


for M_MELA in MELA_MASS_RESOL:
    M=str(M_MELA)
    P_S='meP'+M+'_Res_ggf_S_'+ALGO+'_nom'
    P_B='meP'+M+'_Res_ggf_B_'+ALGO+'_nom'
    P_S_B=P_B+'/'+P_S
    aliases['MEKD_'+str(M)]={
        'expr':'1/(1+'+P_S_B+')'
    }



##--some missing branch
#PuppiMET_nom_pt
aliases['PuppiMET_nom_pt']={
    'expr':'sqrt(PuppiMET_nom_px*PuppiMET_nom_px+PuppiMET_nom_py*PuppiMET_nom_py)'
}
