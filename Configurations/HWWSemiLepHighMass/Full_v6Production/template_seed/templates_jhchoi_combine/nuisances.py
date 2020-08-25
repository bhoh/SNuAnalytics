NotUseTreeBase=False
#UseRegroupJES=False



import os
import sys
sys.path.insert(0, "SysBranch")
if 'opt' in globals():
    configration_py=opt.nuisancesFile
else:
    configration_py=sys.argv[0]


print "configration_py=",configration_py
from FatJet_Jet_SysBranches import * 
from WPandCut2016 import *

bst=''
if 'Boosted' in configration_py:
  bst='Boosted'
elif 'Resolved' in configration_py:
  bst='Resolved'


#cuts
cut_GGF0=[]
cut_GGF1=[]
cut_VBF0=[]
cut_VBF1=[]



for c in cuts:
  if 'GGF' in c:
    if 'MEKDTAG':
      cut_GGF0.append(c)
    elif 'UNTAGGED':
      cut_GGF1.append(c)
    
  elif 'VBF':
    if 'MEKDTAG':
      cut_VBF0.append(c)
    elif 'UNTAGGED':
      cut_VBF1.append(c)
      



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





mc = [skey for skey in samples if (skey != 'DATA' and skey !='PseudoData')]
print mc




import sys
sys.path.insert(0, "MassPoints")
from List_MX import *
from List_MX_VBF import *



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


trig_syst = ['TriggerEffWeight_1l_u/TriggerEffWeight_1l < 10 ? TriggerEffWeight_1l_u/TriggerEffWeight_1l*(TriggerEffWeight_1l>0.02)+(TriggerEffWeight_1l<=0.02) : 1.0','TriggerEffWeight_1l_d/TriggerEffWeight_1l < 10 ? TriggerEffWeight_1l_d/TriggerEffWeight_1l*(TriggerEffWeight_1l>0.02)+(TriggerEffWeight_1l<=0.02) : 1.0']

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

pdfAccept={}
handle=open('PDF/nuisance_pdf.py','r')
exec(handle)
handle.close()

for n in nMember_sample:
  print "# of member->",n
  if int(n)==0:continue
  for s in nMember_sample[n]:
    #print s
    pdfAccept[s]=["abs(LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0]) < 10 ? LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0] : 1.0" for i in range(n)] ## outlyer in top sample

nuisances['pdfAccept'] = {
    'name': 'pdfAccept',
    'kind': 'weight_rms',
    'type': 'shape',
    'samples': pdfAccept,
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







CATS=['GGF0','GGF1','VBF0','VBF1']
##--wjets rateparam
for cat in CATS: 
    if not CombineWjets:
        for wjet in Wjets:
            nuisances[wjet+'norm_'+cat+'_'+bst]={
                'name': 'Wjetsnorm_'+bst+'_'+cat+'_'+Year,
                #'type': 'lnN',
                'type'  : 'rateParam',
                'samples': {
                    #'Wjets0j':'1.0',
                    #'Wjets1j':'1.0',
                    wjet:'1.0',
                }      
                ,
                #'cuts':cut_GGF0
            }
  
        
            exec("nuisances['"+wjet+"'+'norm_'+"+"'"+cat+"'"+"+'_'+bst]['cuts']=cut_"+cat+"")

    else:
        nuisances['Wjetsnorm_'+cat+'_'+bst]={
            'name': 'Wjetsnorm_'+bst+'_'+cat+'_'+Year,
            'type'  : 'rateParam',
            'samples': {
                'Wjets':'1.0',
            },
        
        }
        exec("nuisances['Wjetsnorm_'+"+"'"+cat+"'"+"+'_'+bst]['cuts']=cut_"+cat+"")
  
##--top rateparam
for cat in CATS: 
  nuisances['topnorm_'+cat+'_'+bst]={
    'name': 'topnorm_'+bst+'_'+cat+'_'+Year,
    'samples': {
      'top':'1.0',
    },
    'type'  : 'rateParam',
  }
  exec("nuisances['topnorm_'+"+"'"+cat+"'"+"+'_'+bst]['cuts']=cut_"+cat+"")

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
      #'MultiV':'1.1',
    }
}
if not CombineMultiV:
    for multiv in MultiV:
        nuisances['MultiVnorm']['samples'][multiv]='1.2'
else:
    nuisances['MultiVnorm']['samples']['MultiV']='1.2'
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



if StatOnly:
  del nuisances
  nuisances={}
  nuisances['dummy']={
    'name': 'dummy',
    'type': 'lnN',
    'samples': dict((skey, '1.0001') for skey in mc )
  }
print "nNuisances=",len(nuisances)
