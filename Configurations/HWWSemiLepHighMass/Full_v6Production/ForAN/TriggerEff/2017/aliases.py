import os
import copy
import inspect
import numpy as np

##---WP---##
from WPandCut2017 import *
##-End WP--##

##--Get Boosted OR Resolved--##
if 'opt' in globals():
    configration_py=opt.aliasesFile
else:
    configration_py=sys.argv[0]
##End of 


configurations = '%s/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/' % os.getenv('CMSSW_BASE')
print configurations

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]



##--Lepton ISO/ID/RECO
aliases['LepWPweight']={
    #'expr':' Lepton_promptgenmatched[0] ? (((Lepton_isTightElectron_'+eleWP+'[0]>0.5)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]'+')) + ((Lepton_isTightMuon_'+muWP+'[0]>0.5)*(Lepton_tightMuon_'+muWP+'_TotSF'+'[0]'+'))) : 1',
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


#Electron_deltaEtaSC

aliases['eleTrigMatch']={
    'expr':'Lepton_electronIdx[0]<0 ? 0 : (Sum$((    (TrigObj_filterBits/(1<<2))%2==1) &&  (pow(TrigObj_eta-Lepton_eta[0]-Electron_deltaEtaSC[Lepton_electronIdx[0]],2)+pow(TrigObj_phi-Lepton_phi[0],2) < 0.01) &&(Trigger_sngEl)   )>0)'
}
aliases['Lepton_etaSC']={
    'expr':' Lepton_electronIdx < 0 ? Lepton_eta : Lepton_eta+Electron_deltaEtaSC[Lepton_electronIdx]'
}
