import os
import copy
import inspect
import numpy as np

##---WP2017---##
from WPandCut2016 import *
_ALGO="_"+ALGO

##-End WP--##
configurations = '%s/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/' % os.getenv('CMSSW_BASE')
print configurations


mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

###---Btag SF---###
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
    'expr': 'TMath::Exp(Sum$(TMath::Log((Jet_pt_nom[CleanJet_jetIdx]>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(Jet_pt_nom[CleanJet_jetIdx]<20 || abs(CleanJet_eta)>2.5))))',
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
puidSFSource = '%s/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/data/JetPUID_effcyandSF.root' % os.getenv('CMSSW_BASE')
aliases['PUJetIdSF'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
        '.L %s/patches/pujetidsf_event.cc+' % configurations
    ],
    'class': 'PUJetIdEventSF',
    'args': (puidSFSource, Year, 'loose'),
    'samples': mc
}



###--Wtagger ID eff. SF
aliases['WtaggerSFnom']={
    #'expr' : '('+WtaggerSF+')'+'*(isBoost_'+WTAG+'_nom) + 1*(!isBoost_'+WTAG+'_nom)',
    'expr' : 'isBoost_'+WTAG+'_nom ? ('+WtaggerSF+')'+' : 1',
    'samples' : mc
}
aliases['WtaggerSFup']={
    'expr' : 'isBoost_'+WTAG+'_nom ? ('+WtaggerSFup+')'+' : 1',
    #'expr' : '('+WtaggerSFup+')'+'*(isBoost_'+WTAG+'_nom) + 1*(!isBoost_'+WTAG+'_nom)',
    'samples' : mc
}
aliases['WtaggerSFdown']={
    'expr' : 'isBoost_'+WTAG+'_nom ? ('+WtaggerSFdown+')'+' : 1',
    #'expr' : '('+WtaggerSFdown+')'+'*(isBoost_'+WTAG+'_nom) + 1*(!isBoost_'+WTAG+'_nom)',
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

aliases['LepWPCut']={
    'expr':'(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
}

aliases['SFweight']={
    'expr':SFweight,
    'samples':mc
}



aliases['nJetPassBKin']={
    'expr':'Sum$(Jet_pt_nom[CleanJet_jetIdx]>20 && abs(CleanJet_eta)<2.5)'
}

aliases['JetMultplicity']={
    'expr':'Sum$(Jet_pt_nom[CleanJet_jetIdx]>'+jetptmin+' && abs(CleanJet_eta)<'+jetetamax+')'
}

aliases['JetMultplicity_eta4p7']={
    'expr':'Sum$(Jet_pt_nom[CleanJet_jetIdx]>'+jetptmin+' && abs(CleanJet_eta)<4.7)'
}


for M_MELA in MELA_MASS_BOOST:
    for C in MELA_C_BOOST:
        M=str(M_MELA)
        C=str(C)
        P_S='meP'+M+'_Bst_ggf_S_'+WTAG+'_nom'
        P_B='meP'+M+'_Bst_ggf_B_'+WTAG+'_nom'
        P_B_S=P_B+'/'+P_S
        aliases['MEKD_Bst_C_'+C+'_M'+str(M)]={
            'expr':P_S+'>0 ? '+'1/(1+'+C+'*'+P_B_S+')'+':-1'
        }


for M_MELA in MELA_MASS_RESOL:
    for C in MELA_C_RESOL:
        M=str(M_MELA)
        C=str(C)
        P_S='meP'+M+'_Res_ggf_S_'+ALGO+'_nom'
        P_B='meP'+M+'_Res_ggf_B_'+ALGO+'_nom'
        P_B_S=P_B+'/'+P_S
        aliases['MEKD_Res_C_'+C+'_M'+str(M)]={
            'expr':P_S+'>0 ? '+'1/(1+'+C+'*'+P_B_S+')'+':-1'
        }



##--some missing branch
#PuppiMET_nom_pt
#aliases['PuppiMET_nom_pt']={
#    'expr':'sqrt(PuppiMET_nom_px*PuppiMET_nom_px+PuppiMET_nom_py*PuppiMET_nom_py)'
#}
##--top pt rwgt
aliases['Top_pTrw'] = {
    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPt) - 0.000134*topGenPt + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPt) - 0.000134*antitopGenPt + 0.973))) * (TMath::Sqrt(TMath::Exp(1.61468e-03 + 3.46659e-06*topGenPt - 8.90557e-08*topGenPt*topGenPt) * TMath::Exp(1.61468e-03 + 3.46659e-06*antitopGenPt - 8.90557e-08*antitopGenPt*antitopGenPt))) + (topGenPt * antitopGenPt <= 0.)', # Same Reweighting as other years, but with additional fix for tune CUET -> CP5

    'samples': ['top']

}
aliases['LHEPartWlepPt'] = {
    #'linesToAdd': ['.L %s/HWWSemiLepHighMass/Full2017/LHEPartWlepPt.cc+' % configurations],                                                                                                                
    'linesToAdd':['.L '+os.getcwd()+'/LHEPartWlepPt.cc+'],
    'class': 'LHEPartWlepPt',
    'samples': ['Wjets0j', 'Wjets1j','Wjets2j']
}
data = np.genfromtxt(os.getenv('CMSSW_BASE')+'/src/LatinoAnalysis/Gardener/python/data/ewk/kewk_w.dat', skip_header=2, skip_footer=7)
weight_string = "("
uncert_string = "("
for row in data:
    low  = row[0]
    high = row[1]
    weight = (1+row[2])
    ucert = row[3]

    weight_string+="({}<LHEPartWlepPt[0] && LHEPartWlepPt[0]<={})*{}+".format(low, high, weight)
    uncert_string+="({}<LHEPartWlepPt[0] && LHEPartWlepPt[0]<={})*{}+".format(low, high, weight)
# remove trailing + sign and close parentheses
weight_string=weight_string[:-1]+")"
uncert_string=uncert_string[:-1]+")"

aliases['EWK_W_correction'] = {
    'expr': weight_string,
    'samples': ['Wjets0j', 'Wjets1j','Wjets2j']
}
aliases['EWK_W_correction_uncert'] = {
    'expr': uncert_string,
    # 'samples': 'Wjets'
    'samples': ['Wjets0j', 'Wjets1j','Wjets2j']
}



aliases['dPhi_WW_boosted']={
    'expr':'(WtaggerFatjet_'+WTAG+'_nom_phi-Wlep_nom_phi)'
}
