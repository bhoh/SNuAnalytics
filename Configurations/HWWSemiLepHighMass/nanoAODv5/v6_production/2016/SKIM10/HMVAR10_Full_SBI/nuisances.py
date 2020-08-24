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

if CombineMultiV:
  mc+=['MultiV']
  for s in MultiV:
    if s in mc: mc.remove(s)
if CombineH125:
  mc+=['h125']
  for s in H125:
    if s in mc: mc.remove(s)
if Combine_ggWW:
  mc+=['Combine_ggWW']
if Combine_qqWWqq:
  mc+=['Combine_qqWWqq']
if CombineSBI:
  for MX in List_MX:
    mc+=['ggHWWlnuqq_M'+str(MX)+'_SBI']
  for MX in List_MX_VBF:
    mc+=['vbfHWWlnuqq_M'+str(MX)+'_SBI']

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
    btag_syst = ['(btagSF%sup)/(btagSF)<10 ? (btagSF%sup)/(btagSF) : 1.0' % (shift,shift), '(btagSF%sdown)/(btagSF) < 10 ? (btagSF%sdown)/(btagSF) : 1.0' % (shift,shift)]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2016'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
    }



trig_syst = ['TriggerEffWeight_1l_u/TriggerEffWeight_1l < 10 ? TriggerEffWeight_1l_u/TriggerEffWeight_1l : 1.0','TriggerEffWeight_1l_d/TriggerEffWeight_1l < 10 ? TriggerEffWeight_1l_d/TriggerEffWeight_1l : 1.0']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc),
}


prefire_syst = ['PrefireWeight_Up/PrefireWeight < 10 ? PrefireWeight_Up/PrefireWeight : 1', 'PrefireWeight_Down/PrefireWeight < 10 ? PrefireWeight_Down/PrefireWeight : 1']


nuisances['prefire'] = {
    'name': 'CMS_eff_prefiring_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, prefire_syst) for skey in mc),
}




eff_e_syst = ['Lepton_tightElectron_'+eleWP+'_TotSF_Up'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0] < 10 ? Lepton_tightElectron_'+eleWP+'_TotSF_Up'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0] : 1.0','Lepton_tightElectron_'+eleWP+'_TotSF_Down'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0] < 10 ? Lepton_tightElectron_'+eleWP+'_TotSF_Down'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0] : 1.0']

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

eff_m_syst = ['Lepton_tightMuon_'+muWP+'_TotSF_Up'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0] < 10 ? Lepton_tightMuon_'+muWP+'_TotSF_Up'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0] : 1.0','Lepton_tightMuon_'+muWP+'_TotSF_Down'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0] < 10 ? Lepton_tightMuon_'+muWP+'_TotSF_Down'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0] : 1.0']

nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, eff_m_syst) for skey in mc),
}


for s in ['fatjes','fatjer','fatjms','fatjmr']:
  nuisances[s] = {
    'name': 'CMS_'+s+'_2018',
    'type': 'shape',
    'kind': 'branch_custom',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': xrootdPath+'/'+treeBaseDir+'/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_fatjetsys',
    'folderDown': xrootdPath+'/'+treeBaseDir+'/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_fatjetsys',

  }
  nuisances[s]['BrFromToUp']={}
  nuisances[s]['BrFromToDown']={}
  for br in HMBoostBranches+WBranches:
    nuisances[s]['BrFromToUp'][br]=br.replace("nom",s.replace('fat','')+"up")
    nuisances[s]['BrFromToDown'][br]=br.replace("nom",s.replace('fat','')+"down")



nuisances['mupt'] = {
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
                'type': 'lnN',
                'samples': dict((skey, '1.015') for skey in mc),
}


#from MakeSampleDict import *

#samples_value=MakeSampleDict(samples,'LHEScaleWeight',"LHEScaleWeight[0]")


QCDscale={}
handle=open('QCDscale/nuisance_QCDscale.py','r')
exec(handle)
handle.close()
if CombineMultiV:
  ##Check whether any MultiV sample has this nuisance variation
  doVar=False
  for n in nMember_sample:
    if int(n)==0:continue
    if len(set(nMember_sample[n]) & set(MultiV))!=0:doVar=True
  if doVar:
    if not 4 in nMember_sample:nMember_sample[4]=[]
    nMember_sample[4].append('MultiV')
    print "doQCDScale for MultiV"
if CombineH125:
  ##Check whether any MultiV sample has this nuisance variation
  doVar=False
  for n in nMember_sample:
    if int(n)==0:continue
    if len(set(nMember_sample[n]) & set(H125))!=0:doVar=True
  if doVar:
    if not 4 in nMember_sample:nMember_sample[4]=[]
    nMember_sample[4].append('h125')
    print "doQCDScale for h125"


for n in nMember_sample:
  print "# of member->",n
  if int(n)==0:continue
  for s in nMember_sample[n]:
    print s
    QCDscale[s]=["abs(LHEScaleWeight["+str(i)+"]/LHEScaleWeight[0]) < 10 ? LHEScaleWeight["+str(i)+"]/LHEScaleWeight[0] : 1.0" for i in range(n)] ## outlyer in top sample                                  

nuisances['QCDscaleAccept'] = {
    'name': 'QCDscaleAccept',
    'skipCMS': 1,
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': QCDscale,
}

#CaclLenBranch
#nMember_sample=CaclLenBranch(samples,'LHEPdfWeight') ## {33:[DY,Wjets....]}
pdfAccept={}
#PDF4LHC15_nnlo_30_pdfas={}
#NNPDF31_nnlo_hessian_pdfas={}
handle=open('PDF/nuisance_pdf.py','r')
exec(handle)
handle.close()
if CombineMultiV:
  ##Check whether any MultiV sample has this nuisance variation                                                                                                                                             
  doVar=False
  for n in nMember_sample:
    if int(n)==0:continue
    if len(set(nMember_sample[n]) & set(MultiV))!=0:doVar=True
  if doVar:
    if not 4 in nMember_sample:nMember_sample[4]=[]
    nMember_sample[4].append('MultiV')
    print "dopdfAccept for MultiV"

if CombineH125:
  ##Check whether any MultiV sample has this nuisance variation
  doVar=False
  for n in nMember_sample:
    if int(n)==0:continue
    if len(set(nMember_sample[n]) & set(H125))!=0:doVar=True
  if doVar:
    if not 4 in nMember_sample:nMember_sample[4]=[]
    nMember_sample[4].append('h125')
    print "dopdfAccept for h125"



for n in nMember_sample:
  print "----# of errset in this pdf-->",n
  if int(n) == 0 : continue
  for s in nMember_sample[n]:
    print s
  #if n==33:
  #  for s in nMember_sample[n]:
  #    PDF4LHC15_nnlo_30_pdfas[s]=["LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0] < 10 ? LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0] : 1.0" for i in range(n)]
  #    #PDF4LHC15_nnlo_30_pdfas
  #elif n>=100:
  #  for s in nMember_sample[n]:
  #    NNPDF31_nnlo_hessian_pdfas[s]=["LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0] < 10 ? LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0] : 1.0" for i in range(n)]
  for s in nMember_sample[n]:
    print s
    pdfAccept[s]=["abs(LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0]) < 10 ? LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0] : 1.0" for i in range(n)]

nuisances['pdfAccept'] = {
    'name': 'pdfAccept',
    'kind': 'weight_rms',
    'type': 'shape',
    'samples': pdfAccept,
}

#nuisances['PDF4LHC15_nnlo_30_pdfas'] = {
#    'name': 'PDF4LHC15_nnlo_30_pdfas',
#    'kind': 'weight_rms',
#    'type': 'shape',
#    'samples': PDF4LHC15_nnlo_30_pdfas
#}
#nuisances['NNPDF31_nnlo_hessian_pdfas'] = {
#    'name': 'NNPDF31_nnlo_hessian_pdfas',
#    'kind': 'weight_rms',
#    'type': 'shape',
#    'samples': NNPDF31_nnlo_hessian_pdfas
#}

handle=open('PS/nuisance_PS.py','r')
exec(handle)
handle.close()

if CombineMultiV:
  ##Check whether any MultiV sample has this nuisance variation
  doVar=False
  for n in nMember_sample:
    if int(n)==0:continue
    if len(set(nMember_sample[n]) & set(MultiV))!=0:doVar=True
  if doVar:
    if not 4 in nMember_sample:nMember_sample[4]=[]
    nMember_sample[4].append('MultiV')
    print "doPS for MultiV"

if CombineH125:
  ##Check whether any MultiV sample has this nuisance variation
  doVar=False
  for n in nMember_sample:
    if int(n)==0:continue
    if len(set(nMember_sample[n]) & set(H125))!=0:doVar=True
  if doVar:
    if not 4 in nMember_sample:nMember_sample[4]=[]
    nMember_sample[4].append('h125')
    print "doPS for h125"

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

from LatinoAnalysis.Tools.HiggsXSection  import *
HiggsXS = HiggsXSection()


import sys
sys.path.insert(0, "MassPoints")
from List_MX import *
from List_MX_VBF import *


##--xsec of signals
nuisances['pdf_Higgs_gg']  = {
  'name'  : 'pdf_Higgs_gg',
  'samples' : {},
  'type'  : 'lnN',
}
nuisances['QCDscale_Higgs_gg']  = {
  'name'  : 'QCDscale_Higgs_gg',
  'samples' : {},
  'type'  : 'lnN',
}

for MX in List_MX:
  nuisances['pdf_Higgs_gg']['samples'].update({'ggHWWlnuqq_M'+str(MX): HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH',int(MX),'pdf','bsm')})
  nuisances['QCDscale_Higgs_gg']['samples'].update({'ggHWWlnuqq_M'+str(MX): HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH',int(MX),'scale','bsm')})

nuisances['pdf_Higgs_qqbar']  = {
  'name'  : 'pdf_Higgs_qqbar',
  'type'  : 'lnN',
  'samples':{},
}
nuisances['QCDscale_Higgs_qqbar']  = {
  'name'  : 'QCDscale_Higgs_qqbar',
  'type'  : 'lnN',
  'samples':{},
}
for MX in List_MX_VBF:
  nuisances['pdf_Higgs_qqbar']['samples'].update({'vbfHWWlnuqq_M'+str(MX): HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH',int(MX),'pdf','bsm')})
  nuisances['QCDscale_Higgs_qqbar']['samples'].update({'vbfHWWlnuqq_M'+str(MX): HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH',int(MX),'scale','bsm')})

##--norm                                                                                                                                                                          
nuisances['QCDnorm']={
    'name': 'QCDnorm2016',
    'type': 'lnN',
    'samples': {
      'QCD_MU':'1.1',
      'QCD_EM':'1.1',
      'QCD_bcToE':'1.1',
      }
}


nuisances['Wnorm']={
    'name': 'Wjetsnorm2016',
    'type': 'lnN',
    'samples': {
      'Wjets':'1.1',

      }
}


nuisances['topnorm']={
    'name': 'topnorm2016',
    'type': 'lnN',
    'samples': {
      'top':'1.1',
    }
}
nuisances['dynorm']={
    'name': 'dynorm2016',
    'type': 'lnN',
    'samples': {
      'DY':'1.1',
    }
}


nuisances['MultiVnorm']={
    'name': 'MultiVnorm2016',
    'type': 'lnN',
    'samples': {
      'WW':'1.1',
      'WZ':'1.1',
      'ZZ':'1.1',
      'WWW':'1.1',
      'WWZ':'1.1',
      'WZZ':'1.1',
      'ZZZ':'1.1',
    }
}



