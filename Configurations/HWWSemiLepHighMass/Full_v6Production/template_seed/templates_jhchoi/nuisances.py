NotUseTreeBase=False
#UseRegroupJES=False
import os
import sys
from FatJet_Jet_SysBranches import * 
from WPandCut2016 import *



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


if 'opt' in globals():
    configration_py=opt.nuisancesFile
else:
    configration_py=sys.argv[0]
print "configration_py=",configration_py


mc = [skey for skey in samples if (skey != 'DATA' and skey !='PseudoData')]
print mc
if CombineMultiV:
  mc+=['MultiV']
  for s in MultiV:
    if s in mc: mc.remove(s)
if CombineWjets and Year!='2016':
  mc+=['Wjets']
  for s in Wjets:
    if s in mc : mc.remove(s)
if CombineH125:
  mc+=['h125']
  for s in H125:
    if s in mc : mc.remove(s)
if Combine_ggWW:
  mc+=['ggWW']
if Combine_qqWWqq:
  mc+=['qqWWqq']



import sys
sys.path.insert(0, "MassPoints")
from List_MX import *
from List_MX_VBF import *
if CombineSBI:
  for MX in List_MX:
    mc+=['ggHWWlnuqq_M'+str(MX)+'_SBI']
  for MX in List_MX_VBF:
    mc+=['vbfHWWlnuqq_M'+str(MX)+'_SBI']



##---Luminosity---##
##--Ref: https://twiki.cern.ch/twiki/bin/view/CMS/TWikiLUM#LumiComb
if Year=='2016':
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


  

if Year=='2017':
  nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2017',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc )
  }
  
  nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.008') for skey in mc)
  }
  
  nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc )
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
  
  nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc )
  }
  
  nuisances['lumi_Ghosts'] = {
    'name': 'lumi_13TeV_Ghosts',
    'type': 'lnN',
    'samples': dict((skey, '1.001') for skey in mc )
  }

if Year=='2018':
  nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2018',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc )
  }
  
  nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.008') for skey in mc)
  }
  
  nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc )
  }
  
  nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc )
  }



#for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
for shift in ['lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    
    btag_syst = ['(btagSF%sup)/(btagSF)<10 ? (btagSF%sup)/(btagSF) : 1.0' % (shift,shift), '(btagSF%sdown)/(btagSF) < 10 ? (btagSF%sdown)/(btagSF) : 1.0' % (shift,shift)]
    
    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_'+Year

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        #'samples': dict((skey, btag_syst) for skey in mc),
      'samples':{}
    }
    for skey in mc:
      nuisances['btag_shape_%s' % shift]['samples'][skey]=btag_syst


trig_syst = ['TriggerEffWeight_1l_u/TriggerEffWeight_1l < 10 ? TriggerEffWeight_1l_u/TriggerEffWeight_1l : 1.0','TriggerEffWeight_1l_d/TriggerEffWeight_1l < 10 ? TriggerEffWeight_1l_d/TriggerEffWeight_1l : 1.0']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_'+Year,
    'kind': 'weight',
    'type': 'shape',
    'samples': {},
}
for skey in mc:
  nuisances['trigg']['samples'][skey]=trig_syst
                                                         
#              dict((skey, trig_syst) for skey in mc),

prefire_syst = ['PrefireWeight_Up/PrefireWeight < 10 ? PrefireWeight_Up/PrefireWeight : 1', 'PrefireWeight_Down/PrefireWeight < 10 ? PrefireWeight_Down/PrefireWeight : 1']

if not Year=='2018':
  nuisances['prefire'] = {
    'name': 'CMS_eff_prefiring_'+Year,
    'kind': 'weight',
    'type': 'shape',
    #'samples': dict((skey, prefire_syst) for skey in mc),
    'samples':{}
  }
  for skey in mc:
    nuisances['prefire']['samples'][skey]=prefire_syst




#eff_e_syst = ['Lepton_tightElectron_'+eleWP+'_IdIsoSF_Up'+'[0]/Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]','Lepton_tightElectron_'+eleWP+'_IdIsoSF_Down'+'[0]/Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]']


eff_e_syst = ['Lepton_tightElectron_'+eleWP+'_TotSF_Up'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0] < 10 ? Lepton_tightElectron_'+eleWP+'_TotSF_Up'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0] : 1.0','Lepton_tightElectron_'+eleWP+'_TotSF_Down'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0] < 10 ? Lepton_tightElectron_'+eleWP+'_TotSF_Down'+'[0]/Lepton_tightElectron_'+eleWP+'_TotSF'+'[0] : 1.0']

nuisances['eff_e'] = {
    'name': 'CMS_eff_e_'+Year,
    'kind': 'weight',
    'type': 'shape',
    #'samples': dict((skey, eff_e_syst) for skey in mc),
  'samples':{},
}
for skey in mc:
  nuisances['eff_e']['samples'][skey]=eff_e_syst



eff_m_syst = ['Lepton_tightMuon_'+muWP+'_TotSF_Up'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0] < 10 ? Lepton_tightMuon_'+muWP+'_TotSF_Up'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0] : 1.0','Lepton_tightMuon_'+muWP+'_TotSF_Down'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0] < 10 ? Lepton_tightMuon_'+muWP+'_TotSF_Down'+'[0]/Lepton_tightMuon_'+muWP+'_TotSF'+'[0] : 1.0']

nuisances['eff_m'] = {
    'name': 'CMS_eff_m_'+Year,
    'kind': 'weight',
    'type': 'shape',
    #'samples': dict((skey, eff_m_syst) for skey in mc),
  'samples':{}
}
for skey in mc:
  nuisances['eff_m']['samples'][skey]=eff_m_syst


eff_Wtag_syst = ['WtaggerSFdown/WtaggerSFnom','WtaggerSFup/WtaggerSFnom']
if 'Boosted' in configration_py: 
  nuisances['eff_Wtag'] = {
    
    'name': 'CMS_eff_Wtag_'+Year,
    'kind': 'weight',
    'type': 'shape',
    #'samples': dict((skey, eff_Wtag_syst) for skey in mc),
    'samples':{}
  }
  for skey in mc:
    nuisances['eff_Wtag']['samples'][skey]=eff_Wtag_syst

if not NotUseTreeBase:
  fatjetsys=['fatjes','fatjer','fatjms','fatjmr']
  if 'DeepAK8' in WTAG:
    fatjetsys=['fatjes','fatjer']
  for s in fatjetsys:
    nuisances[s] = {
      'name': 'CMS_'+s+'_'+Year,
      'type': 'shape',
      'kind': 'branch_custom',
      #'samples': dict((skey, ['1', '1']) for skey in mc),
      'samples':{},
      'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_fatjetsys'),
      'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_fatjetsys'),
      #'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_fatjetsys',
      
    }
    for skey in mc:
      nuisances[s]['samples'][skey]=['1','1']

    nuisances[s]['BrFromToUp']={}
    nuisances[s]['BrFromToDown']={}
    for br in HMBoostBranches+WBranches:
      nuisances[s]['BrFromToUp'][br]=br.replace("nom",s.replace('fat','')+"up")
      #print nuisances[s]['BrFromToUp'][br]
      nuisances[s]['BrFromToDown'][br]=br.replace("nom",s.replace('fat','')+"down")
      
    nuisances['mupt'] = {
      'name': 'CMS_scale_muon_'+Year,
      'kind': 'tree',
      'type': 'shape',
      'samples':{},
      #'samples': dict((skey, ['1', '1']) for skey in mc),
      #'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_nom_MupTup',
      #'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_nom_MupTdo',
      'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_nom_MupTup'),
      'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_nom_MupTdo'),
    }
    for skey in mc:
      nuisances['mupt']['samples'][skey]=['1','1']


    nuisances['elept'] = {
      'name': 'CMS_scale_electron_'+Year,
      'kind': 'tree',
      'type': 'shape',
      #'samples': dict((skey, ['1', '1']) for skey in mc),
      'samples':{},
      'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_nom_ElepTup'),
      'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_nom_ElepTdo'),
      #'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_nom_ElepTup',
      #'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_nom_ElepTdo',
      
    }
    for skey in mc:
      nuisances['elept']['samples'][skey]=['1','1']


    nuisances['met'] = {
      'name': 'CMS_scale_met_'+Year,
      'kind': 'tree',
      'type': 'shape',
      #'samples': dict((skey, ['1', '1']) for skey in mc),
      'samples':{},
      'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_nom_METup'),
      'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_nom_METup'),
      #'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_nom_METup',
      #'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_nom_METdo',
    }
    for skey in mc:
      nuisances['met']['samples'][skey]=['1','1']

pu_syst=['puWeightUp/puWeight','puWeightDown/puWeight']


nuisances['PU'] = {
    'name': 'CMS_PU_'+Year,
    'kind': 'weight',
    'type': 'shape',
    #'samples': dict((skey, pu_syst) for skey in mc),
  'samples':{},
}
for skey in mc:
  nuisances['PU']['samples'][skey]=pu_syst

#nuisances['UE']  = {
#                'name'  : 'UE_CP5',
#                'type': 'lnN',
#                'samples': dict((skey, '1.015') for skey in mc),
#}



#variations = ['1', 'LHEScaleWeight[1]/LHEScaleWeight[0]', 'LHEScaleWeight[3]/LHEScaleWeight[0]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]/LHEScaleWeight[0]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]/LHEScaleWeight[0]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]/LHEScaleWeight[0]']##0,1,3,5,7,8

##---QCDscale
####--Use predefined one


#print samples_value
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



if CombineWjets and Year!='2016':
  ##Check whether any MultiV sample has this nuisance variation
  doVar=False
  for n in nMember_sample:
    if int(n)==0:continue
    if len(set(nMember_sample[n]) & set(Wjets))!=0:doVar=True
  if doVar:
    if not 4 in nMember_sample:nMember_sample[4]=[]
    nMember_sample[4].append('Wjets')
    print "doQCDScale for Wjets"
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


if Combine_ggWW:
  doVar=False
  for n in nMember_sample:
    if int(n)==0:continue
    if len(set(nMember_sample[n]) & set(H125))!=0:doVar=True
  if doVar:
    if not 4 in nMember_sample:nMember_sample[4]=[]
    nMember_sample[4].append('ggWW')
    print "doQCDScale for ggWW"

if Combine_qqWWqq:
  doVar=False
  for n in nMember_sample:
    if int(n)==0:continue
    if len(set(nMember_sample[n]) & set(H125))!=0:doVar=True
  if doVar:
    if not 4 in nMember_sample:nMember_sample[4]=[]
    nMember_sample[4].append('qqWWqq')
    print "doQCDScale for qqWWqq"



for n in nMember_sample:
  print "# of member->",n
  if int(n)==0:continue
  for s in nMember_sample[n]:
    #print s
    QCDscale[s]=["abs(LHEScaleWeight["+str(i)+"]/LHEScaleWeight[0]) < 10 ? LHEScaleWeight["+str(i)+"]/LHEScaleWeight[0] : 1.0" for i in range(n)] ## outlyer in top sample


nuisances['QCDscaleAccept'] = {
  'name': 'QCDscaleAccept',
  'kind': 'weight_envelope',
  'type': 'shape',
  'samples':QCDscale,
}
#from MakeSampleDict import *
#CaclLenBranch
#nMember_sample=CaclLenBranch(samples,'LHEPdfWeight') ## {33:[DY,Wjets....]}
pdfAccept={}
#PDF4LHC15_nnlo_30_pdfas={}
#NNPDF31_nnlo_hessian_pdfas={}
##--ReadFromPredefined one
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
    
if CombineWjets and Year!='2016':
  ##Check whether any MultiV sample has this nuisance variation
  doVar=False
  for n in nMember_sample:
    if int(n)==0:continue
    if len(set(nMember_sample[n]) & set(Wjets))!=0:doVar=True
  if doVar:
    if not 4 in nMember_sample:nMember_sample[4]=[]
    nMember_sample[4].append('Wjets')
    print "dopdfAccept for Wjets"
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
if Combine_ggWW:
  ##Check whether any MultiV sample has this nuisance variation
  doVar=False
  for n in nMember_sample:
    if int(n)==0:continue
    if len(set(nMember_sample[n]) & set(ggWW))!=0:doVar=True
  if doVar:
    if not 4 in nMember_sample:nMember_sample[4]=[]
    nMember_sample[4].append('ggWW')
    print "dopdfAccept for ggWW"

if Combine_qqWWqq:
  ##Check whether any MultiV sample has this nuisance variation
  doVar=False
  for n in nMember_sample:
    if int(n)==0:continue
    if len(set(nMember_sample[n]) & set(qqWWqq))!=0:doVar=True
  if doVar:
    if not 4 in nMember_sample:nMember_sample[4]=[]
    nMember_sample[4].append('qqWWqq')
    print "dopdfAccept for qqWWqq"



for n in nMember_sample:
  print "# of member->",n
  if int(n)==0:continue
  #if n==33:
  #  for s in nMember_sample[n]:
  #    PDF4LHC15_nnlo_30_pdfas[s]=["LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0] < 10 ? LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0] : 1.0" for i in range(n)]
  #    #PDF4LHC15_nnlo_30_pdfas
  #elif n>=102:
  #  for s in nMember_sample[n]:
  #    NNPDF31_nnlo_hessian_pdfas[s]=["LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0] < 10 ? LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0] : 1.0" for i in range(n)]
  for s in nMember_sample[n]:
    #print s
    pdfAccept[s]=["abs(LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0]) < 10 ? LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0] : 1.0" for i in range(n)] ## outlyer in top sample
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
#print pdfAccept
nuisances['pdfAccept'] = {
    'name': 'pdfAccept',
    'kind': 'weight_rms',
    'type': 'shape',
    'samples': pdfAccept,
}



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

if CombineWjets and Year!='2016':
  ##Check whether any MultiV sample has this nuisance variation
  doVar=False
  for n in nMember_sample:
    if int(n)==0:continue
    if len(set(nMember_sample[n]) & set(Wjets))!=0:doVar=True
  if doVar:
    if not 4 in nMember_sample:nMember_sample[4]=[]
    nMember_sample[4].append('Wjets')
    print "dopPS for Wjets"
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


##--Wjet's PS ->GenJet_HT based

if (not 'Wjets2j' in PSWeightISR) and ('Wjets2j' in mc):
  #PSWeightISR['Wjets2j']=['(nCleanGenJet==0)*1.02073379725 + (nCleanGenJet==1)*1.00825569824 + (nCleanGenJet==2)*0.990047642726 + (nCleanGenJet>=3)*1.03131711638', '(nCleanGenJet==0)*1.08896203086 + (nCleanGenJet==1)*1.01920761264 + (nCleanGenJet==2)*0.95445991422 + (nCleanGenJet>=3)*0.943177239895']
  #PSWeightISR['Wjets2j']=['0+(GenJet_HT > 400)*1.02282764557+(GenJet_HT > 70 && GenJet_HT <= 120)*0.974387625178+(GenJet_HT > 30 && GenJet_HT <= 70)*0.988087051534+(GenJet_HT > 200 && GenJet_HT <= 400)*1.01679418064+(GenJet_HT <= 30)*1.0+(GenJet_HT > 120 && GenJet_HT <= 200)*0.997271021553','0+(GenJet_HT > 400)*0.950626120853+(GenJet_HT > 70 && GenJet_HT <= 120)*1.00105914046+(GenJet_HT > 30 && GenJet_HT <= 70)*1.11648762101+(GenJet_HT > 200 && GenJet_HT <= 400)*0.959141678475+(GenJet_HT <= 30)*1.0+(GenJet_HT > 120 && GenJet_HT <= 200)*0.972278737036']
  PSWeightISR['Wjets2j']=['0+(Generator_scalePDF <= 30)*1.02025191022+(Generator_scalePDF > 70 && Generator_scalePDF <= 120)*0.99651149795+(Generator_scalePDF > 200 && Generator_scalePDF <= 400)*0.995480156042+(Generator_scalePDF > 30 && Generator_scalePDF <= 70)*0.995146877066+(Generator_scalePDF > 120 && Generator_scalePDF <= 200)*0.996027577128+(Generator_scalePDF > 400)*0.995700813891','0+(Generator_scalePDF <= 30)*0.971925927735+(Generator_scalePDF > 70 && Generator_scalePDF <= 120)*0.96820275154+(Generator_scalePDF > 200 && Generator_scalePDF <= 400)*0.954866106773+(Generator_scalePDF > 30 && Generator_scalePDF <= 70)*0.971383511214+(Generator_scalePDF > 120 && Generator_scalePDF <= 200)*0.960125276113+(Generator_scalePDF > 400)*0.937674933085']
if (not 'Wjets1j' in PSWeightISR) and ('Wjets1j' in mc):
  #PSWeightISR['Wjets1j']=['(nCleanGenJet==0)*1.01196205511 + (nCleanGenJet==1)*0.988257181952 + (nCleanGenJet==2)*1.00024240789 + (nCleanGenJet>=3)*1.00733695938', '(nCleanGenJet==0)*1.03784403902 + (nCleanGenJet==1)*0.974773803373 + (nCleanGenJet==2)*0.967005316899 + (nCleanGenJet>=3)*0.913844099339']
  #PSWeightISR['Wjets1j']=['0+(GenJet_HT > 400)*0.962973193021+(GenJet_HT > 70 && GenJet_HT <= 120)*0.990586097447+(GenJet_HT > 30 && GenJet_HT <= 70)*0.966548822569+(GenJet_HT > 200 && GenJet_HT <= 400)*1.00452326609+(GenJet_HT <= 30)*1.00021481431+(GenJet_HT > 120 && GenJet_HT <= 200)*1.01441122134','0+(GenJet_HT > 400)*0.968428606677+(GenJet_HT > 70 && GenJet_HT <= 120)*0.987822393319+(GenJet_HT > 30 && GenJet_HT <= 70)*1.01186216922+(GenJet_HT > 200 && GenJet_HT <= 400)*0.967129636404+(GenJet_HT <= 30)*1.1354746121+(GenJet_HT > 120 && GenJet_HT <= 200)*0.971849089095']
  PSWeightISR['Wjets1j']=['0+(Generator_scalePDF <= 30)*1.01574729081+(Generator_scalePDF > 70 && Generator_scalePDF <= 120)*0.961068768092+(Generator_scalePDF > 200 && Generator_scalePDF <= 400)*0.935804712154+(Generator_scalePDF > 30 && Generator_scalePDF <= 70)*0.985002349551+(Generator_scalePDF > 120 && Generator_scalePDF <= 200)*0.946564187005+(Generator_scalePDF > 400)*0.926780494085','0+(Generator_scalePDF <= 30)*0.985082442064+(Generator_scalePDF > 70 && Generator_scalePDF <= 120)*0.987483595751+(Generator_scalePDF > 200 && Generator_scalePDF <= 400)*0.979527084291+(Generator_scalePDF > 30 && Generator_scalePDF <= 70)*0.987521058993+(Generator_scalePDF > 120 && Generator_scalePDF <= 200)*0.983920599031+(Generator_scalePDF > 400)*0.976536789681']
if (not 'Wjets0j' in PSWeightISR) and ('Wjets0j' in mc):
  #PSWeightISR['Wjets0j']=['(nCleanGenJet==0)*0.998308713597 + (nCleanGenJet==1)*1.024326639 + (nCleanGenJet==2)*1.00490579097 + (nCleanGenJet>=3)*1.06382313494', '(nCleanGenJet==0)*0.994847559816 + (nCleanGenJet==1)*0.970837169317 + (nCleanGenJet==2)*0.921111283973 + (nCleanGenJet>=3)*0.92527429617']
  #PSWeightISR['Wjets0j']=['0+(GenJet_HT > 400)*1.01589926595+(GenJet_HT > 70 && GenJet_HT <= 120)*1.05279090416+(GenJet_HT > 30 && GenJet_HT <= 70)*0.994167274582+(GenJet_HT > 200 && GenJet_HT <= 400)*1.11410733613+(GenJet_HT <= 30)*0.972590691039+(GenJet_HT > 120 && GenJet_HT <= 200)*1.09252671572','0+(GenJet_HT > 400)*0.956427381446+(GenJet_HT > 70 && GenJet_HT <= 120)*0.97125484587+(GenJet_HT > 30 && GenJet_HT <= 70)*0.996834396868+(GenJet_HT > 200 && GenJet_HT <= 400)*0.928136301813+(GenJet_HT <= 30)*1.00340682861+(GenJet_HT > 120 && GenJet_HT <= 200)*0.945789565124']
  PSWeightISR['Wjets0j']=['0+(Generator_scalePDF <= 30)*1.00127568888+(Generator_scalePDF > 70 && Generator_scalePDF <= 120)*0.978540370507+(Generator_scalePDF > 200 && Generator_scalePDF <= 400)*0.954244686078+(Generator_scalePDF > 30 && Generator_scalePDF <= 70)*0.995165400376+(Generator_scalePDF > 120 && Generator_scalePDF <= 200)*0.968173347126+(Generator_scalePDF > 400)*1.0','0+(Generator_scalePDF <= 30)*0.994353001158+(Generator_scalePDF > 70 && Generator_scalePDF <= 120)*0.99013029032+(Generator_scalePDF > 200 && Generator_scalePDF <= 400)*0.991640490155+(Generator_scalePDF > 30 && Generator_scalePDF <= 70)*0.994218687669+(Generator_scalePDF > 120 && Generator_scalePDF <= 200)*0.99372153802+(Generator_scalePDF > 400)*1.0']

if (not 'Wjets2j' in PSWeightFSR) and ('Wjets2j' in mc) :
  #PSWeightFSR['Wjets2j']=['(nCleanGenJet==0)*0.9846688642 + (nCleanGenJet==1)*0.993822455978 + (nCleanGenJet==2)*1.0079856078 + (nCleanGenJet>=3)*0.97516930436', '(nCleanGenJet==0)*0.937933929929 + (nCleanGenJet==1)*0.977731417079 + (nCleanGenJet==2)*1.01892148352 + (nCleanGenJet>=3)*1.01657862777']
  #PSWeightFSR['Wjets2j']=['0+(GenJet_HT > 400)*0.982469024476+(GenJet_HT > 70 && GenJet_HT <= 120)*1.02011365404+(GenJet_HT > 30 && GenJet_HT <= 70)*1.00943633943+(GenJet_HT > 200 && GenJet_HT <= 400)*0.987254123282+(GenJet_HT <= 30)*1.0+(GenJet_HT > 120 && GenJet_HT <= 200)*1.00211192118','0+(GenJet_HT > 400)*1.00805854648+(GenJet_HT > 70 && GenJet_HT <= 120)*0.996068598342+(GenJet_HT > 30 && GenJet_HT <= 70)*0.933550970907+(GenJet_HT > 200 && GenJet_HT <= 400)*1.00974061831+(GenJet_HT <= 30)*1.0+(GenJet_HT > 120 && GenJet_HT <= 200)*1.00824420762']
  PSWeightFSR['Wjets2j']=['0+(Generator_scalePDF <= 30)*0.984743115228+(Generator_scalePDF > 70 && Generator_scalePDF <= 120)*1.00275990155+(Generator_scalePDF > 200 && Generator_scalePDF <= 400)*1.00342729716+(Generator_scalePDF > 30 && Generator_scalePDF <= 70)*1.00378269336+(Generator_scalePDF > 120 && Generator_scalePDF <= 200)*1.003097594+(Generator_scalePDF > 400)*1.00332650883','0+(Generator_scalePDF <= 30)*1.0077787804+(Generator_scalePDF > 70 && Generator_scalePDF <= 120)*1.00356677259+(Generator_scalePDF > 200 && Generator_scalePDF <= 400)*1.00300860883+(Generator_scalePDF > 30 && Generator_scalePDF <= 70)*1.00715307331+(Generator_scalePDF > 120 && Generator_scalePDF <= 200)*1.00407180645+(Generator_scalePDF > 400)*1.00365389508']
if (not 'Wjets1j' in PSWeightFSR) and ('Wjets1j' in mc):
  #PSWeightFSR['Wjets1j']=['(nCleanGenJet==0)*0.991040655987 + (nCleanGenJet==1)*1.00926231553 + (nCleanGenJet==2)*0.999811374034 + (nCleanGenJet>=3)*0.994856261395', '(nCleanGenJet==0)*0.97184106935 + (nCleanGenJet==1)*1.00937459351 + (nCleanGenJet==2)*1.00975969923 + (nCleanGenJet>=3)*1.03411262896']
  #PSWeightFSR['Wjets1j']=['0+(GenJet_HT > 400)*1.03034688294+(GenJet_HT > 70 && GenJet_HT <= 120)*1.00719341905+(GenJet_HT > 30 && GenJet_HT <= 70)*1.02626748142+(GenJet_HT > 200 && GenJet_HT <= 400)*0.997839658777+(GenJet_HT <= 30)*1.00022649931+(GenJet_HT > 120 && GenJet_HT <= 200)*0.989330418078','0+(GenJet_HT > 400)*1.0093271222+(GenJet_HT > 70 && GenJet_HT <= 120)*1.002599001+(GenJet_HT > 30 && GenJet_HT <= 70)*0.991653890057+(GenJet_HT > 200 && GenJet_HT <= 400)*1.00648469672+(GenJet_HT <= 30)*0.928268111893+(GenJet_HT > 120 && GenJet_HT <= 200)*1.00676394444']
  PSWeightFSR['Wjets1j']=['0+(Generator_scalePDF <= 30)*0.988116150431+(Generator_scalePDF > 70 && Generator_scalePDF <= 120)*1.03146702662+(Generator_scalePDF > 200 && Generator_scalePDF <= 400)*1.05256838227+(Generator_scalePDF > 30 && Generator_scalePDF <= 70)*1.01161856836+(Generator_scalePDF > 120 && Generator_scalePDF <= 200)*1.04370763385+(Generator_scalePDF > 400)*1.06128114151','0+(Generator_scalePDF <= 30)*1.00345088754+(Generator_scalePDF > 70 && Generator_scalePDF <= 120)*1.00071589772+(Generator_scalePDF > 200 && Generator_scalePDF <= 400)*1.00539578059+(Generator_scalePDF > 30 && Generator_scalePDF <= 70)*1.00146936916+(Generator_scalePDF > 120 && Generator_scalePDF <= 200)*1.00313173162+(Generator_scalePDF > 400)*1.00805405076']
if (not 'Wjets0j' in PSWeightFSR) and ('Wjets0j' in mc):
  #PSWeightFSR['Wjets0j']=['(nCleanGenJet==0)*1.00123043904 + (nCleanGenJet==1)*0.981416928606 + (nCleanGenJet==2)*0.996876072693 + (nCleanGenJet>=3)*0.952268350583', '(nCleanGenJet==0)*0.999474629797 + (nCleanGenJet==1)*1.0091202521 + (nCleanGenJet==2)*1.03597884808 + (nCleanGenJet>=3)*1.02589781018']
  #PSWeightFSR['Wjets0j']=['0+(GenJet_HT > 400)*0.988386923979+(GenJet_HT > 70 && GenJet_HT <= 120)*0.960571370528+(GenJet_HT > 30 && GenJet_HT <= 70)*1.00413680652+(GenJet_HT > 200 && GenJet_HT <= 400)*0.920648615188+(GenJet_HT <= 30)*1.02084551484+(GenJet_HT > 120 && GenJet_HT <= 200)*0.933572771743','0+(GenJet_HT > 400)*0.981072393971+(GenJet_HT > 70 && GenJet_HT <= 120)*1.00668035334+(GenJet_HT > 30 && GenJet_HT <= 70)*0.999048338812+(GenJet_HT > 200 && GenJet_HT <= 400)*1.01007665629+(GenJet_HT <= 30)*0.997023948153+(GenJet_HT > 120 && GenJet_HT <= 200)*1.00954342867']
  PSWeightFSR['Wjets0j']=['0+(Generator_scalePDF <= 30)*0.999031880465+(Generator_scalePDF > 70 && Generator_scalePDF <= 120)*1.017112972+(Generator_scalePDF > 200 && Generator_scalePDF <= 400)*1.03682332099+(Generator_scalePDF > 30 && Generator_scalePDF <= 70)*1.00359518638+(Generator_scalePDF > 120 && Generator_scalePDF <= 200)*1.02559870985+(Generator_scalePDF > 400)*1.0','0+(Generator_scalePDF <= 30)*1.00000364072+(Generator_scalePDF > 70 && Generator_scalePDF <= 120)*1.00025606176+(Generator_scalePDF > 200 && Generator_scalePDF <= 400)*1.00522420376+(Generator_scalePDF > 30 && Generator_scalePDF <= 70)*0.99951624175+(Generator_scalePDF > 120 && Generator_scalePDF <= 200)*1.00156070823+(Generator_scalePDF > 400)*1.0']



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



if not NotUseTreeBase:
  if UseRegroupJES :
    print "--UseRegroupJES--"
    for s in ['jesFlavorQCD','jesRelativeBal','jesHF','jesBBEC1','jesEC2','jesAbsolute']: ##year-correlated
      nuisances[s] = {
        'name': 'CMS_'+s,
        'kind': 'branch_custom',
        'type': 'shape',
        #'samples': dict((skey, ['1', '1']) for skey in mc),
        'samples':{},
        #'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysup_correlate',
        #'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysdown_correlate',
        'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_jetsysup_correlate'),
        'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_jetsysdown_correlate'),
      }
      for skey in mc:
        nuisances[s]['samples'][skey]=['1','1']

      nuisances[s]['BrFromToUp']={}
      nuisances[s]['BrFromToDown']={}
      for br in JetBranches+WlepBranches+WjjBranches+HMBoostBranches+HMResolBranches:
        nuisances[s]['BrFromToUp'][br]=br.replace("nom",s+"Up")
        nuisances[s]['BrFromToDown'][br]=br.replace("nom",s+"Down")

    for s in ['jesAbsolute_'+Year,'jesHF_'+Year,'jesEC2_'+Year,'jesRelativeSample_'+Year,'jesBBEC1_'+Year,'jer']: ##year-uncorrelated
      nuisances[s] = {
        'name': 'CMS_'+s,
        'kind': 'branch_custom',
        'type': 'shape',
        #'samples': dict((skey, ['1', '1']) for skey in mc),
        'samples':{},
        'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_jetsysup_uncorrelate'),
        'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_jetsysdown_uncorrelate'),
        #'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysup_uncorrelate',
        #'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysdown_uncorrelate',
      }
      for skey in mc:
        nuisances[s]['samples'][skey]=['1','1']

      if s=="jer": nuisances[s]['name']+='_'+Year
      nuisances[s]['BrFromToUp']={}
      nuisances[s]['BrFromToDown']={}
      for br in JetBranches+WlepBranches+WjjBranches+HMBoostBranches+HMResolBranches:
        nuisances[s]['BrFromToUp'][br]=br.replace("nom",s+"Up")
        nuisances[s]['BrFromToDown'][br]=br.replace("nom",s+"Down")


  else:
    print "--Not UseRegroupJES--"
    nuisances['jesTotal'] = {
      #'name': 'CMS_jesTotal_'+Year,
      'name': 'CMS_jesTotal',
      'kind': 'branch_custom',
      'type': 'shape',
      #'samples': dict((skey, ['1', '1']) for skey in mc),
      'samples':{},
      'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_jetsysup_correlate'),
      'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_jetsysdown_correlate'),
      #'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysup_correlate',
      #'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysdown_correlate',
    }
    for skey in mc:
      nuisances['jesTotal']['samples'][skey]=['1','1']

    nuisances['jesTotal']['BrFromToUp']={}
    nuisances['jesTotal']['BrFromToDown']={}
    for br in JetBranches+WlepBranches+WjjBranches+HMBoostBranches+HMResolBranches:
      nuisances['jesTotal']['BrFromToUp'][br]=br.replace("nom","jesTotalUp")
      nuisances['jesTotal']['BrFromToDown'][br]=br.replace("nom","jesTotalDown")
      
    for s in ['jer']: ##year-uncorrelated
      nuisances[s] = {
        'name': 'CMS_'+s,
        'kind': 'branch_custom',
        'type': 'shape',
        #'samples': dict((skey, ['1', '1']) for skey in mc),
        'samples':{},
        'Folderup': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_jetsysup_uncorrelate'),
        'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/'+STEP.replace('_nom','_jetsysdown_uncorrelate'),
        #'folderUp': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysup_uncorrelate',
        #'folderDown': xrootdPath+'/'+treeBaseDir+'/'+CAMPAIGN+'/MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__HMFull_jhchoi10_jetsysdown_uncorrelate',
      }
      for skey in mc:
        nuisances[s]['samples'][skey]=['1','1']

      if s=="jer": nuisances[s]['name']+='_'+Year
      nuisances[s]['BrFromToUp']={}
      nuisances[s]['BrFromToDown']={}
      for br in JetBranches+WlepBranches+WjjBranches+HMBoostBranches+HMResolBranches:
        nuisances[s]['BrFromToUp'][br]=br.replace("nom",s+"Up")
        nuisances[s]['BrFromToDown'][br]=br.replace("nom",s+"Down")

## Use the following if you want to apply the automatic combine MC stat nuisances.

nuisances['stat'] = {
    'type': 'auto',
    'maxPoiss': '10',
    'includeSignal': '0',
    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': {}
}




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
    'name': 'QCDnorm'+Year,
    'type': 'lnN',
    'samples': {
      'QCD_MU':'1.1',
      'QCD_EM':'1.1',
      'QCD_bcToE':'1.1',
      }
}



if Year=='2016':
  nuisances['Wnorm']={
    'name': 'Wjetsnorm'+Year,
    #'type': 'lnN',
    'type'  : 'rateParam',
    'samples': {
      #'Wjets':'1.1',
      'Wjets':'1.0',
    }
  }
elif CombineWjets:
  nuisances['Wnorm']={
    'name': 'Wjetsnorm'+Year,
    #'type': 'lnN',
    'type'  : 'rateParam',
    'samples': {
      #'Wjets':'1.1',
      'Wjets':'1.0',
    }
  }
else:
  nuisances['W0jnorm']={
    'name': 'Wjets0jnorm'+Year,
    #'type': 'lnN',
    'type'  : 'rateParam',
    'samples': {
      #'Wjets0j':'1.1',
      'Wjets0j':'1.0',
      
    }
  }

  
  nuisances['W1jnorm']={
  'name': 'Wjets1jnorm'+Year,
    #'type': 'lnN',
    'samples': {
      #'Wjets1j':'1.1',
      'Wjets1j':'1.0',
    },
    'type'  : 'rateParam',
    #'cuts'  : '''''
    
  }
  
  
  nuisances['W2jnorm']={
    'name': 'Wjets2jnorm'+Year,
    #'type': 'lnN',
    'samples': {
      #'Wjets2j':'1.1',
      'Wjets2j':'1.0',
    },
    'type'  : 'rateParam',
  }
  

  
  
nuisances['topnorm']={
    'name': 'topnorm'+Year,
    #'type': 'lnN',
    'samples': {
      #'top':'1.1',
      'top':'1.0',
    },
  'type'  : 'rateParam',
}
nuisances['dynorm']={
    'name': 'dynorm'+Year,
    'type': 'lnN',
    'samples': {
      'DY':'1.1',
    }
}


nuisances['MultiVnorm']={
    'name': 'MultiVnorm'+Year,
    'type': 'lnN',
    'samples': {
      'MultiV':'1.1',
    }
}

nuisances['stat'] = {
    'type': 'auto',
    'maxPoiss': '10',
    'includeSignal': '0',
    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': {}
}
  

for n in nuisances.values():
    n['skipCMS'] = 1


#for n in sorted(nuisances): 
#  #USEONLY
#  if not n in USEONLY:
#    del nuisances[n]
print "nNuisances=",len(nuisances)
