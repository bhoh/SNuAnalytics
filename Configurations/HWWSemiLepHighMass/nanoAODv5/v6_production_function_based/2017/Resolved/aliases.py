import os
import copy
import inspect

##---WP2017---##
from WPandCut2017 import *


##-End WP--##


configurations = '%s/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/nanoAODv5/v6_production/' % os.getenv('CMSSW_BASE')
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
'''
aliases['btagSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}
'''
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



##---JetRequirement---##
aliases['zeroJet'] = {
    'expr': 'Sum$(CleanJet_pt[CleanJetNotFat_jetIdx] > 30.)==0'
}
aliases['oneJet'] = {
    'expr': 'Sum$(CleanJet_pt[CleanJetNotFat_jetIdx] > 30.)==1'
}
aliases['twoJet'] = {
    'expr': 'Sum$(CleanJet_pt[CleanJetNotFat_jetIdx] > 30.)==2'

}

aliases['NJet'] = {
    'expr': 'Sum$(CleanJet_pt[CleanJetNotFat_jetIdx] > 30.)'
}

##--MT--##
aliases['Mt']={
    #'linesToAdd':['.L %s/functions/GetMt.C+' % configurations ],
    'linesToAdd':['.L %s/functions/TLorentzVectorFunction.C+' % configurations ],
    'expr':'Combine2PtEtaPhiM_Mt(Lepton_pt[0],0, Lepton_phi[0], 0, PuppiMET_pt,0, PuppiMET_phi, 0)'
}


aliases['isResolved']={
    'linesToAdd':['gSystem->Load("%s/functions/ResolvedRegion_C.so")' % configurations],
    'expr':'(Sum$( (CleanFatJet_pt>200.) && (CleanFatJet_mass > 40.) && (CleanFatJet_mass < 250.) && (abs(CleanFatJet_eta)<2.4) )==0) && SetWhad(Entry$) '
    #'expr':'nCleanFatJet==0'
}

##--Whad--##

aliases['WResolved_mass']={
    'expr':'Whad_mass(Entry$)'
}
aliases['WResolved_pt']={
    'expr':'Whad_pt(Entry$)'
}
aliases['WResolved_eta']={
    'expr':'Whad_eta(Entry$)'
}
aliases['WResolved_phi']={
    'expr':'Whad_phi(Entry$)'
}



##---Wlep---##

aliases['WlepPuppi_pt']={
    'expr':'WlepPuppi_pt(Entry$)',
}
aliases['WlepPuppi_eta']={
    'expr':'WlepPuppi_eta(Entry$)',
}
aliases['WlepPuppi_phi']={
    'expr':'WlepPuppi_phi(Entry$)',
}
aliases['WlepPuppi_mass']={
    'expr':'WlepPuppi_mass(Entry$)',
}


aliases['WW_mass']={    
    'expr':'Combine2PtEtaPhiM_M(WlepPuppi_pt, WlepPuppi_eta, WlepPuppi_phi,WlepPuppi_mass, WResolved_pt,WResolved_eta,WResolved_phi,WResolved_mass)',
}

aliases['WW_pt']={    
    'expr':'Combine2PtEtaPhiM_Pt(WlepPuppi_pt, WlepPuppi_eta, WlepPuppi_phi,WlepPuppi_mass, WResolved_pt,WResolved_eta,WResolved_phi,WResolved_mass)',
}


aliases['WW_Mt']={
    'expr':'sqrt(pow(WW_mass,2)+pow(WW_pt,2))'
}

##--VBF conf--##
aliases['isVBF']={
     'expr':'SetVBF(Entry$)',
}


aliases['VBF_jjdEta']={
     'expr':'Get_VBF_jjdEta(Entry$)',

}

aliases['VBF_Mjj']={
     'expr':'Get_VBF_Mjj(Entry$)',

}

##--etc--##
aliases['WptOverMWW']={
    'expr':'min(WlepPuppi_pt,WResolved_pt)/WW_mass'
}



##--NBJet--##

aliases['cjidx1']={ ##cleanjet index of not in whad
    'expr':'Get_cjidx1(Entry$)'
}
aliases['cjidx2']={
    'expr':'Get_cjidx2(Entry$)'
}


aliases['NBJet']={
    #'expr': 'Sum$( (Jet_btag'+bAlgo+'[CleanJet_jetIdx[Iteration$]] >'+bWP+') && (Jet_pt[CleanJet_jetIdx[Iteration$]] > 20 ) && (Jet_eta[CleanJet_jetIdx[Iteration$]] < 2.5) && (cjidx1!=Iteration$) && (cjidx2!=Iteration$) )'
    'expr': 'Sum$( (Jet_btag'+bAlgo+'[CleanJet_jetIdx] >'+bWP+') && (CleanJet_pt > 20 ) && (CleanJet_eta < 2.5))'
}
