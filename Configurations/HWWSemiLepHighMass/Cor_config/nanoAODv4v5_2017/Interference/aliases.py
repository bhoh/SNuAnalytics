import os
import copy
import inspect


configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations)

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]
SigMcLNuQQ = [skey for skey in samples if skey  in 
                              ('ggh125LNuQQ','ggh125LNuQQ_SI','ggh125LNuQQ_I',
                               'HWWLNuQQ','ggWWLNuQQ')]

massesModelsFile = "massesModels.py"
if os.path.exists(massesModelsFile) :
  handle = open(massesModelsFile,'r')
  exec(handle)
  handle.close()
else:
  print "!!! ERROR file ", massesModelsFile, " does not exist."


model_I = model+'_I' # (meSBI-meSpow-meHBI)/meSpow --> I(pole + h) + I(pole + B)
model_I_Honly = model+ '_I_Honly' # (meS_Honly-meH-meSpow)/meSpow --> I(pole + h)
model_I_Bonly = model+ '_I_Bonly' # (meS(po)BI-meSpow-meB)/meSpow --> I(pole + B)
model_I_HB = model+'_I_HB' # (meS125BI-meB-meH)/meSpow (meSBI-meB-meH)/meSpow --> I(h + B)
model_B = model+'_B' # meB/meS(pole)
model_H = model+'_H' # (meH)/meSpow --> h/pole No interference btw

aliases['I_H_w_B'] = {
    'expr': '('+model_I_Bonly+'>-4 && '+model_I_Bonly+' <4)*'+model_I_Bonly+' + ('+model_I_Bonly+' <=-4 ||'+model_I_Bonly+' >=4)* 0.01906',
    'samples': SigMcLNuQQ
}
aliases['I_H_w_hB'] = {
    'expr': '('+model_I+' >-4 && '+model_I+' <4)*'+model_I+' + ('+model_I+' <=-4 ||'+model_I+'>=4)* 0.04423',
    'samples': SigMcLNuQQ
}

#aliases['I_H_w_hB'] = {
#    'linesToAdd': [
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
#        '.L %s/patches/MelaWeightPatch.cc+' % configurations
#    ],
#    'class': 'MelaWeightCorr',
#    'args': (model,),
#    'samples': mc
#}
#
#btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_94XSF_V2_B_F.csv' % os.getenv('CMSSW_BASE')
#
#aliases['Jet_btagSF_shapeFix'] = {
#    'linesToAdd': [
#        'gSystem->Load("libCondFormatsBTauObjects.so");',
#        'gSystem->Load("libCondToolsBTau.so");',
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
#        '.L %s/patches/btagsfpatch.cc+' % configurations
#    ],
#    'class': 'BtagSF',
#    'args': (btagSFSource,),
#    'samples': mc
#}
#

#aliases['bVeto'] = {
#    'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0'
#}
#
#aliases['bReq'] = {
#    'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) >= 1'
#}
#
#
#aliases['bVetoSF'] = {
#    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
#    'samples': mc
#}
#
#aliases['bReqSF'] = {
#    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
#    'samples': mc
#}
#aliases['zeroJet'] = {
#    'expr': 'Alt$(CleanJet_pt[0], 0) < 30.'
#}
#aliases['topcr'] = {
#    'expr': '((zeroJet && !bVeto) || bReq)'
#}
#
#
#aliases['btagSF'] = {
#    'expr': '(bVeto || (topcr && zeroJet))*bVetoSF + (topcr && !zeroJet)*bReqSF',
#    'samples': mc
#}
