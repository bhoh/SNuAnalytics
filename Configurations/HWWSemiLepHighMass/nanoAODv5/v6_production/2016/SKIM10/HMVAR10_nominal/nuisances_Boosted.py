UseRegroupJES=True
from WPandCut2016 import *
from FatJet_Jet_SysBranches import *
print "UseRegroupJES=",UseRegroupJES

import os

SITE=os.uname()[1]


xrootdPath=''
if    'iihe' in SITE :
  xrootdPath  = 'dcap://maite.iihe.ac.be/'
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/'
elif  'cern' in SITE :
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'

elif  'sdfarm' in SITE:
  xrootdPath = 'root://cms-xrdr.private.lo:2094'
  treeBaseDir = "/xrd/store/user/jhchoi/Latino/HWWNano/"


#eleWP='mva_90p_Iso2016'
#muWP='cut_Tight80x'


mc = [skey for skey in samples if skey != 'DATA']






nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2016',
    'type': 'lnN',
    'samples': dict((skey, '1.022') for skey in mc )
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.009') for skey in mc)
}


nuisances['lumi_BBDefl'] = {
    'name': 'lumi_13TeV_BBDefl',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc )
}

nuisances['lumi_DynBeta'] = {
    'name': 'lumi_13TeV_DynBeta',
    'type': 'lnN',
    'samples': dict((skey, '1.005') for skey in mc )
}

nuisances['lumi_Ghosts'] = {
    'name': 'lumi_13TeV_Ghosts',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc )
}


#for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
for shift in ['lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['Alt$((btagSF%sup)/(btagSF),1.0)' % shift, 'Alt$((btagSF%sdown)/(btagSF),1.0)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2016'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
    }



trig_syst = ['Alt$(TriggerEffWeight_1l_u/TriggerEffWeight_1l,1.0)','Alt$(TriggerEffWeight_1l_d/TriggerEffWeight_1l,1.0)']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc),
}


prefire_syst = ['Alt$(PrefireWeight_Up/PrefireWeight,1.0)', 'Alt$(PrefireWeight_Down/PrefireWeight,1.0)']


nuisances['prefire'] = {
    'name': 'CMS_eff_prefiring_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, prefire_syst) for skey in mc),
}



#eff_e_syst = ['Lepton_tightElectron_'+eleWP+'_TotSF_Up'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]','Lepton_tightElectron_'+eleWP+'_TotSF_Down'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]']
eff_e_syst = ['Alt$(Lepton_tightElectron_'+eleWP+'_TotSF_Up'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0],1.0)','Alt$(Lepton_tightElectron_'+eleWP+'_TotSF_Down'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0],1.0)']
nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, eff_e_syst) for skey in mc),
}

#MCl1loose2016v5__MCCorr2016v5__METup__Semilep2016_whad30__CorrFatJetMass__HMlnjjSel

nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2016',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_nom_ElepTup',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_nom_ElepTdo',
  #'AsLnN': '1'
}

eff_m_syst = ['Alt$(Lepton_tightMuon_'+muWP+'_TotSF_Up'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0],1.0)','Alt$(Lepton_tightMuon_'+muWP+'_TotSF_Down'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0],1.0)']
nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, eff_m_syst) for skey in mc),
}



nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2016',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_nom_MupTup',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_nom_MupTdo',

}


nuisances['met'] = {
    'name': 'CMS_scale_met_2016',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_nom_METup',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_nom_METdo',
    #'AsLnN': '1'
}

pu_syst=['puWeightUp/puWeight','puWeightDown/puWeight']


nuisances['PU'] = {
    'name': 'CMS_PU_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, pu_syst) for skey in mc),
    #'AsLnN': '1',
}


nuisances['UE']  = {
                'name'  : 'UE_CP5',
                'skipCMS' : 1,
                'type': 'lnN',
                'samples': dict((skey, '1.015') for skey in mc),
}


from MakeSampleDict import *

samples_value=MakeSampleDict(samples,'LHEScaleWeight',"LHEScaleWeight[0]")

nuisances['QCDscale'] = {
    'name': 'QCDscale',
    'skipCMS': 1,
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': samples_value,
}

#CaclLenBranch                                                                                                                                                                    
nMember_sample=CaclLenBranch(samples,'LHEPdfWeight') ## {33:[DY,Wjets....]}                                                                                                       
PDF4LHC15_nnlo_30_pdfas={}
NNPDF31_nnlo_hessian_pdfas={}
for n in nMember_sample:
  if n==33:
    for s in nMember_sample[n]:
      PDF4LHC15_nnlo_30_pdfas[s]=["Alt$(LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0],1.0)" for i in range(n)]
      #PDF4LHC15_nnlo_30_pdfas                                                                                                                                                    
  elif n>=102:
    for s in nMember_sample[n]:
      NNPDF31_nnlo_hessian_pdfas[s]=["Alt$(LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0],1.0)" for i in range(n)]


nuisances['PDF4LHC15_nnlo_30_pdfas'] = {
    'name': 'PDF4LHC15_nnlo_30_pdfas',
    'kind': 'weight_rms',
    'type': 'shape',
    'samples': PDF4LHC15_nnlo_30_pdfas
}
nuisances['NNPDF31_nnlo_hessian_pdfas'] = {
    'name': 'NNPDF31_nnlo_hessian_pdfas',
    'kind': 'weight_rms',
    'type': 'shape',
    'samples': NNPDF31_nnlo_hessian_pdfas
}

nMember_sample=CaclLenBranch(samples,'PSWeight')
PSWeightISR={}
PSWeightFSR={}
for n in nMember_sample:
  if n == 4:
   for s in nMember_sample[n]:
     PSWeightISR[s]=["PSWeight[0]","PSWeight[1]"]
     PSWeightFSR[s]=["PSWeight[2]","PSWeight[3]"]

nuisances['PS_ISR']={
  'name': 'PS_ISR',
  'kind': 'weight',
  'type': 'shape',
  'samples':PSWeightISR,
}

nuisances['PS_FSR']={
  'name': 'PS_FSR',
  'kind': 'weight',
  'type': 'shape',
  'samples':PSWeightFSR,
}


if UseRegroupJES:
  for s in ['jesFlavorQCD','jesRelativeBal','jesHF','jesBBEC1','jesEC2','jesAbsolute']: ##year-correlated                                                                         
    nuisances[s] = {
      'name': 'CMS_'+s,
      'kind': 'branch_custom',
      'type': 'shape',
      'samples': dict((skey, ['1', '1']) for skey in mc),
      'folderUp': xrootdPath+'/'+treeBaseDir+'/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysup_correlate',
      'folderDown': xrootdPath+'/'+treeBaseDir+'/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysdown_correlate',
    }
    nuisances[s]['BrFromToUp']={}
    nuisances[s]['BrFromToDown']={}
    for br in JetBranches+WlepBranches+WjjBranches+HMBoostBranches+HMResolBranches:
      nuisances[s]['BrFromToUp'][br]=br.replace("nom",s+"Up")
      nuisances[s]['BrFromToDown'][br]=br.replace("nom",s+"Down")

  for s in ['jesAbsolute_2016','jesHF_2016','jesEC2_2016','jesRelativeSample_2016','jesBBEC1_2016','jer']: ##year-uncorrelated                                                    
    nuisances[s] = {
      'name': 'CMS_'+s,
      'kind': 'branch_custom',
      'type': 'shape',
      'samples': dict((skey, ['1', '1']) for skey in mc),
      'folderUp': xrootdPath+'/'+treeBaseDir+'/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysup_uncorrelate',
      'folderDown': xrootdPath+'/'+treeBaseDir+'/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysdown_uncorrelate',
    }
    if s=="jer": nuisances[s]['name']+='_2016'
    nuisances[s]['BrFromToUp']={}
    nuisances[s]['BrFromToDown']={}
    for br in JetBranches+WlepBranches+WjjBranches+HMBoostBranches+HMResolBranches:
      nuisances[s]['BrFromToUp'][br]=br.replace("nom",s+"Up")
      nuisances[s]['BrFromToDown'][br]=br.replace("nom",s+"Down")

else:

  nuisances['jesTotal'] = {
    'name': 'CMS_jesTotal_2016',
    'kind': 'branch_custom',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysup_correlate',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysdown_correlate',
  }
  nuisances['jesTotal']['BrFromToUp']={}
  nuisances['jesTotal']['BrFromToDown']={}
  for br in JetBranches+WlepBranches+WjjBranches+HMBoostBranches+HMResolBranches:
    nuisances['jesTotal']['BrFromToUp'][br]=br.replace("nom","jesTotalUp")
    nuisances['jesTotal']['BrFromToDown'][br]=br.replace("nom","jesTotalDown")
