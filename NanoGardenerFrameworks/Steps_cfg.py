#!/usr/bin/env python

import os

## --------------------------------- Some predefined sequence Chains -----------------------------------------

LNuQQSamples=[ 'GluGluHToWWToLNuQQ_M1000', 'GluGluHToWWToLNuQQ_M115', 'GluGluHToWWToLNuQQ_M120', 'GluGluHToWWToLNuQQ_M124', 'GluGluHToWWToLNuQQ_M125', 'GluGluHToWWToLNuQQ_M126', 'GluGluHToWWToLNuQQ_M130', 'GluGluHToWWToLNuQQ_M135', 'GluGluHToWWToLNuQQ_M140', 'GluGluHToWWToLNuQQ_M145', 'GluGluHToWWToLNuQQ_M150', 'GluGluHToWWToLNuQQ_M1500', 'GluGluHToWWToLNuQQ_M155', 'GluGluHToWWToLNuQQ_M160', 'GluGluHToWWToLNuQQ_M165', 'GluGluHToWWToLNuQQ_M170', 'GluGluHToWWToLNuQQ_M175', 'GluGluHToWWToLNuQQ_M180', 'GluGluHToWWToLNuQQ_M190', 'GluGluHToWWToLNuQQ_M200', 'GluGluHToWWToLNuQQ_M2000', 'GluGluHToWWToLNuQQ_M210', 'GluGluHToWWToLNuQQ_M230', 'GluGluHToWWToLNuQQ_M250', 'GluGluHToWWToLNuQQ_M2500', 'GluGluHToWWToLNuQQ_M270', 'GluGluHToWWToLNuQQ_M300', 'GluGluHToWWToLNuQQ_M3000', 'GluGluHToWWToLNuQQ_M350', 'GluGluHToWWToLNuQQ_M400', 'GluGluHToWWToLNuQQ_M4000', 'GluGluHToWWToLNuQQ_M450', 'GluGluHToWWToLNuQQ_M500', 'GluGluHToWWToLNuQQ_M5000', 'GluGluHToWWToLNuQQ_M550', 'GluGluHToWWToLNuQQ_M600', 'GluGluHToWWToLNuQQ_M650', 'GluGluHToWWToLNuQQ_M700', 'GluGluHToWWToLNuQQ_M750', 'GluGluHToWWToLNuQQ_M750_NWA', 'GluGluHToWWToLNuQQ_M800', 'GluGluHToWWToLNuQQ_M900', 'VBFHToWWToLNuQQ_M1000', 'VBFHToWWToLNuQQ_M115', 'VBFHToWWToLNuQQ_M120', 'VBFHToWWToLNuQQ_M124', 'VBFHToWWToLNuQQ_M125', 'VBFHToWWToLNuQQ_M126', 'VBFHToWWToLNuQQ_M130', 'VBFHToWWToLNuQQ_M135', 'VBFHToWWToLNuQQ_M140', 'VBFHToWWToLNuQQ_M145', 'VBFHToWWToLNuQQ_M150', 'VBFHToWWToLNuQQ_M1500', 'VBFHToWWToLNuQQ_M155', 'VBFHToWWToLNuQQ_M160', 'VBFHToWWToLNuQQ_M165', 'VBFHToWWToLNuQQ_M170', 'VBFHToWWToLNuQQ_M175', 'VBFHToWWToLNuQQ_M180', 'VBFHToWWToLNuQQ_M190', 'VBFHToWWToLNuQQ_M200', 'VBFHToWWToLNuQQ_M2000', 'VBFHToWWToLNuQQ_M210', 'VBFHToWWToLNuQQ_M230', 'VBFHToWWToLNuQQ_M250', 'VBFHToWWToLNuQQ_M2500', 'VBFHToWWToLNuQQ_M270', 'VBFHToWWToLNuQQ_M300', 'VBFHToWWToLNuQQ_M3000', 'VBFHToWWToLNuQQ_M350', 'VBFHToWWToLNuQQ_M400', 'VBFHToWWToLNuQQ_M4000', 'VBFHToWWToLNuQQ_M450', 'VBFHToWWToLNuQQ_M500', 'VBFHToWWToLNuQQ_M5000', 'VBFHToWWToLNuQQ_M550', 'VBFHToWWToLNuQQ_M600', 'VBFHToWWToLNuQQ_M650', 'VBFHToWWToLNuQQ_M700', 'VBFHToWWToLNuQQ_M750', 'VBFHToWWToLNuQQ_M750_NWA', 'VBFHToWWToLNuQQ_M800', 'VBFHToWWToLNuQQ_M900' ]

TwoL2NuSamples=[ 'GluGluHToWWTo2L2Nu_M115', 'GluGluHToWWTo2L2Nu_M120', 'GluGluHToWWTo2L2Nu_M124', 'GluGluHToWWTo2L2Nu_M125', 'GluGluHToWWTo2L2Nu_M126', 'GluGluHToWWTo2L2Nu_M130', 'GluGluHToWWTo2L2Nu_M135', 'GluGluHToWWTo2L2Nu_M140', 'GluGluHToWWTo2L2Nu_M145', 'GluGluHToWWTo2L2Nu_M150', 'GluGluHToWWTo2L2Nu_M155', 'GluGluHToWWTo2L2Nu_M160', 'GluGluHToWWTo2L2Nu_M165', 'GluGluHToWWTo2L2Nu_M170', 'GluGluHToWWTo2L2Nu_M175', 'GluGluHToWWTo2L2Nu_M180', 'GluGluHToWWTo2L2Nu_M190', 'GluGluHToWWTo2L2Nu_M200', 'GluGluHToWWTo2L2Nu_M210', 'GluGluHToWWTo2L2Nu_M230', 'GluGluHToWWTo2L2Nu_M250', 'GluGluHToWWTo2L2Nu_M270', 'GluGluHToWWTo2L2Nu_M300', 'GluGluHToWWTo2L2Nu_M350', 'GluGluHToWWTo2L2Nu_M400', 'GluGluHToWWTo2L2Nu_M450', 'GluGluHToWWTo2L2Nu_M500', 'GluGluHToWWTo2L2Nu_M550', 'GluGluHToWWTo2L2Nu_M600', 'GluGluHToWWTo2L2Nu_M650', 'GluGluHToWWTo2L2Nu_M700', 'GluGluHToWWTo2L2Nu_M750', 'GluGluHToWWTo2L2Nu_M800', 'GluGluHToWWTo2L2Nu_M900', 'GluGluHToWWTo2L2Nu_M1000', 'GluGluHToWWTo2L2Nu_M1500', 'GluGluHToWWTo2L2Nu_M2000', 'GluGluHToWWTo2L2Nu_M2500', 'GluGluHToWWTo2L2Nu_M3000', 'GluGluHToWWTo2L2Nu_M4000', 'GluGluHToWWTo2L2Nu_M5000', 'GluGluHToWWTo2L2Nu_JHUGen698_M300', 'GluGluHToWWTo2L2Nu_JHUGen698_M350', 'GluGluHToWWTo2L2Nu_JHUGen698_M400', 'GluGluHToWWTo2L2Nu_JHUGen698_M450', 'GluGluHToWWTo2L2Nu_JHUGen698_M500', 'GluGluHToWWTo2L2Nu_JHUGen698_M550', 'GluGluHToWWTo2L2Nu_JHUGen698_M600', 'GluGluHToWWTo2L2Nu_JHUGen698_M650', 'GluGluHToWWTo2L2Nu_JHUGen698_M700', 'GluGluHToWWTo2L2Nu_JHUGen698_M750', 'GluGluHToWWTo2L2Nu_JHUGen698_M800', 'GluGluHToWWTo2L2Nu_JHUGen698_M900', 'GluGluHToWWTo2L2Nu_JHUGen698_M1000', 'GluGluHToWWTo2L2Nu_JHUGen698_M1500', 'GluGluHToWWTo2L2Nu_JHUGen698_M2000', 'GluGluHToWWTo2L2Nu_JHUGen698_M2500', 'GluGluHToWWTo2L2Nu_JHUGen698_M3000', 'GluGluHToWWTo2L2Nu_JHUGen698_M4000', 'GluGluHToWWTo2L2Nu_JHUGen698_M5000', 'GluGluHToWWTo2L2Nu_JHUGen714_M4000', 'GluGluHToWWTo2L2Nu_JHUGen714_M5000', 'VBFHToWWTo2L2Nu_M115', 'VBFHToWWTo2L2Nu_M120', 'VBFHToWWTo2L2Nu_M124', 'VBFHToWWTo2L2Nu_M125', 'VBFHToWWTo2L2Nu_M126', 'VBFHToWWTo2L2Nu_M130', 'VBFHToWWTo2L2Nu_M135', 'VBFHToWWTo2L2Nu_M140', 'VBFHToWWTo2L2Nu_M145', 'VBFHToWWTo2L2Nu_M150', 'VBFHToWWTo2L2Nu_M155', 'VBFHToWWTo2L2Nu_M160', 'VBFHToWWTo2L2Nu_M165', 'VBFHToWWTo2L2Nu_M170', 'VBFHToWWTo2L2Nu_M175', 'VBFHToWWTo2L2Nu_M180', 'VBFHToWWTo2L2Nu_M190', 'VBFHToWWTo2L2Nu_M200', 'VBFHToWWTo2L2Nu_M210', 'VBFHToWWTo2L2Nu_M230', 'VBFHToWWTo2L2Nu_M250', 'VBFHToWWTo2L2Nu_M270', 'VBFHToWWTo2L2Nu_M300', 'VBFHToWWTo2L2Nu_M350', 'VBFHToWWTo2L2Nu_M400', 'VBFHToWWTo2L2Nu_M450', 'VBFHToWWTo2L2Nu_M500', 'VBFHToWWTo2L2Nu_M550', 'VBFHToWWTo2L2Nu_M600', 'VBFHToWWTo2L2Nu_M650', 'VBFHToWWTo2L2Nu_M700', 'VBFHToWWTo2L2Nu_M750', 'VBFHToWWTo2L2Nu_M800', 'VBFHToWWTo2L2Nu_M900', 'VBFHToWWTo2L2Nu_M1000', 'VBFHToWWTo2L2Nu_M1500', 'VBFHToWWTo2L2Nu_M2000', 'VBFHToWWTo2L2Nu_M2500', 'VBFHToWWTo2L2Nu_M3000', 'VBFHToWWTo2L2Nu_M4000', 'VBFHToWWTo2L2Nu_M5000', 
'VBFHToWWTo2L2Nu_JHUGen698_M300', 'VBFHToWWTo2L2Nu_JHUGen698_M350', 'VBFHToWWTo2L2Nu_JHUGen698_M400', 'VBFHToWWTo2L2Nu_JHUGen698_M450', 'VBFHToWWTo2L2Nu_JHUGen698_M500', 'VBFHToWWTo2L2Nu_JHUGen698_M550', 'VBFHToWWTo2L2Nu_JHUGen698_M600', 'VBFHToWWTo2L2Nu_JHUGen698_M650', 'VBFHToWWTo2L2Nu_JHUGen698_M700', 'VBFHToWWTo2L2Nu_JHUGen698_M750', 'VBFHToWWTo2L2Nu_JHUGen698_M800', 'VBFHToWWTo2L2Nu_JHUGen698_M900', 'VBFHToWWTo2L2Nu_JHUGen698_M1000', 'VBFHToWWTo2L2Nu_JHUGen698_M1500', 'VBFHToWWTo2L2Nu_JHUGen698_M2000', 'VBFHToWWTo2L2Nu_JHUGen698_M2500', 'VBFHToWWTo2L2Nu_JHUGen698_M3000', 'VBFHToWWTo2L2Nu_JHUGen698_M4000', 'VBFHToWWTo2L2Nu_JHUGen698_M5000', 'VBFHToWWTo2L2Nu_JHUGen714_M4000', 'VBFHToWWTo2L2Nu_JHUGen714_M5000' ]

# Import samples and cuts configuration for VBSjjlnu analysi
exec(open(os.getenv("CMSSW_BASE") + "/src/LatinoAnalysis/NanoGardener/python/framework/samples/VBSjjlnu_samples.py"))

# -------------------------------------------- HERE WE GO ----------------------------------------------------

def createFATJESvariation(type, kind="Up"):
  typeShort = type
  if type == "Total":
    typeShort = ""
  dictionary = {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.PtCorrApplier',
                  'declare'    : 'FATJES%s%s = lambda : PtCorrApplier(Coll="CleanFatJet", CorrSrc="jecUncert%s", kind="%s", doMET=True, METobjects = ["MET","PuppiMET","RawMET"], suffix="_FATJES%s%s")' %(typeShort, kind.lower(), type, kind, typeShort, kind.lower()),
                  'module'     : 'FATJES%s%s()' %(typeShort, kind.lower())
               }
  return dictionary 


def createJESvariation(type, kind="Up"):
  typeShort = type
  if type == "Total":
    typeShort = ""
  dictionary = {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.PtCorrApplier',
                  'declare'    : 'JES%s%s = lambda : PtCorrApplier(Coll="CleanJet", CorrSrc="jecUncert%s", kind="%s", doMET=True, METobjects = ["MET","PuppiMET","RawMET"], suffix="_JES%s%s")' %(typeShort, kind.lower(), type, kind, typeShort, kind.lower()),
                  'module'     : 'JES%s%s()' %(typeShort, kind.lower())
               }
  return dictionary 


def createJESchain(type, kind="Up"):
  typeShort = type
  if type == "Total":
    typeShort = ""
  toreplace = typeShort+kind.lower()  
  #chainTemplate = ['do_JESVAR_suffix','l2Kin_JESVAR', 'l3Kin_JESVAR', 'l4Kin_JESVAR','DYMVA_JESVAR','MonoHiggsMVA_JESVAR','formulasMC_JESVAR'] 
  #chainTemplate = ['do_JESVAR_suffix','l2Kin_JESVAR', 'l3Kin_JESVAR', 'l4Kin_JESVAR','formulasMC_JESVAR'] 
  chainTemplate = ['do_JESVAR_suffix','formulasMC_JESVAR'] 
  chain = []
  for item in chainTemplate:
    chain.append(item.replace("VAR", toreplace))
  return chain  

def createFATJESchain(type, kind="Up"):
  typeShort = type
  if type == "Total":
    typeShort = ""
  toreplace = typeShort+kind.lower()  
  #chainTemplate = ['do_JESVAR_suffix','l2Kin_JESVAR', 'l3Kin_JESVAR', 'l4Kin_JESVAR','DYMVA_JESVAR','MonoHiggsMVA_JESVAR','formulasMC_JESVAR'] 
  chainTemplate = ['do_FATJESVAR_suffix','formulasMC_FATJESVAR'] 
  chain = []
  for item in chainTemplate:
    chain.append(item.replace("VAR", toreplace))
  return chain  
    
def addJESchainMembers():
  dictionary = {}
  for type in ["Total", "Absolute", "Absolute_RPLME_YEAR", "BBEC1", "BBEC1_RPLME_YEAR", "EC2", "EC2_RPLME_YEAR", "FlavorQCD", "HF", "HF_RPLME_YEAR", "RelativeBal", "RelativeSample_RPLME_YEAR"]:
    for kind in ["Up", "Do"]:
      typeShort = type
      if type == "Total":
        typeShort = ""  
      mapname = "JES"+typeShort+kind.lower()
      #print 'l2Kin_'+mapname
      dictionary['l2Kin_'+mapname] = {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="%s")' %mapname ,
               }
      dictionary['l3Kin_'+mapname] = {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="%s")' %mapname ,
               }
      dictionary['l4Kin_'+mapname] = {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="%s")' %mapname ,
               }
      dictionary['formulasMC_'+mapname] = {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_YEAR.py\', branch_map="%s")' %mapname ,
                 }
      dictionary['DYMVA_'+mapname] = {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_MAPNAME = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_v5_cfg.py\', branch_map="MAPNAME")'.replace("MAPNAME", mapname) ,
                  'module'     : 'DYMVA_MAPNAME()'.replace("MAPNAME", mapname),
            } 
      dictionary['MonoHiggsMVA_'+mapname] = {
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_MAPNAME = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="MAPNAME")'.replace("MAPNAME", mapname),
                  'module'   : 'MonoHiggsMVA_MAPNAME()'.replace("MAPNAME", mapname),
               }
  
  return dictionary 


def prepare_VBSjjlnu_syst(basename, selection):
  dictionary = {}
  for syst in ["JES", "MupT", "ElepT", "MET"]:
    for j in ['up', 'do']:
      dictionary[basename+"_"+ syst + j] = {
      'isChain'    : True ,
      'do4MC'      : True  ,
      'do4Data'    : False  ,
      'selection'  : selection,
      'subTargets': ['do_{0}{1}'.format(syst, j),
                    'wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK',
                    'trigMC', 'CorrFatJetMC', 'CleanFatJet', 
                    'VBSjjlnu_pairing', 'VBSjjlnu_kin'],
      'onlySample' : vbsjjlnu_samples_bkg + vbsjjlnu_samples_signal
      }
      if syst == "JES":
        dictionary[basename+"_"+ syst + j]["subTargets"] = ['JESBaseTotal'] + dictionary[basename+"_"+ syst + j]["subTargets"] 
  return dictionary

def prepare_VBSjjlnu_Fatjet_syst(basename, selection):
  dictionary = {}
  for syst in ['JES', 'JMS']:
    for j in ['up', 'do']:
      dictionary[basename+ "_" + syst + j] = {
      'isChain'    : True ,
      'do4MC'      : True  ,
      'do4Data'    : False  ,
      'selection'  : selection,
      'subTargets': ['wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK',
                    'trigMC', 'CorrFatJetMC', 
                    'CleanFatJet_{0}{1}'.format(syst, j), 
                    'VBSjjlnu_pairing', 'VBSjjlnu_kin'],
      'onlySample' : vbsjjlnu_samples_bkg + vbsjjlnu_samples_signal
      }
  return dictionary



def prepare_HMsemilep_Fatjet_syst(basename):
    dictionary = {}
    for syst in ['JES', 'JMS']:
      for j in ['up', 'do']:
        dictionary[basename+ "_" + syst + j] = {
          'isChain'    : True ,
          'do4MC'      : True  ,
          'do4Data'    : False  ,
          'subTargets': ['wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK','trigMC','CorrFatJetMC', 'CleanFatJet_{0}{1}'.format(syst, j),]
                       }
    return dictionary

def prepare_HMsemilep_syst(basename):
  for syst in ["JES", "MupT", "ElepT", "MET"]:
    for j in ['up', 'do']:
      dictionary[basename+"_"+ syst + j] = {
      'isChain'    : True ,
      'do4MC'      : True  ,
      'do4Data'    : False  ,
      'selection'  : selection,
      'subTargets': ['do_{0}{1}'.format(syst, j),
                    'wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK',
                    'trigMC', 'CorrFatJetMC', 'CleanFatJet',]
      }
      if syst == "JES":
        dictionary[basename+"_"+ syst + j]["subTargets"] = ['JESBaseTotal'] + dictionary[basename+"_"+ syst + j]["subTargets"]
  return dictionary


def prepare_CHToCB_syst(base_name):
    dictionary = {}
    syst_tot = ['jer','jesTotal','unclustEn']
    syst_uncorr = ['jesAbsolute_RPLME_YEAR','jesBBEC1_RPLME_YEAR','jesEC2_RPLME_YEAR','jesHF_RPLME_YEAR','jesRelativeSample_RPLME_YEAR']
    syst_corr = ['jesAbsolute','jesBBEC1','jesEC2','jesFlavorQCD','jesHF','jesRelativeBal']
    syst_all = syst_tot + syst_uncorr + syst_corr
    for syst in syst_all:
      for j in ['Up','Down']:
        dictionary[base_name+ "_" + syst + j] = {
                  'isChain'    : False,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.KinFitterProducer' ,
                  'declare'    : 'kinFitting_{0}{1} = lambda : KinFitterProducer(RPLME_YEAR,syst_suffix="{0}{1}")'.format(syst,j),
                  'module'     : 'kinFitting_{0}{1}()'.format(syst,j),
                  #'outputbranchsel'  : os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerModules/removeNomBranch_CHToCB.txt',
               }

    #make chain
    dictionary[base_name+"_"+"jetMETSyst_TotalUp"] = {
                  'isChain'    : True,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'subTargets': [base_name+"_" + syst + j for syst in syst_tot for j in ['Up']],
                  #'outputbranchsel'  : os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerModules/removeNomBranch_CHToCB.txt',
               }
    dictionary[base_name+"_"+"jetMETSyst_TotalDown"] = {
                  'isChain'    : True,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'subTargets': [base_name+"_" + syst + j for syst in syst_tot for j in ['Down']],
                  #'outputbranchsel'  : os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerModules/removeNomBranch_CHToCB.txt',
               }
    dictionary[base_name+"_"+"jetMETSyst_uncorrUp"] = {
                  'isChain'    : True,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'subTargets': [base_name+"_" + syst + j for syst in syst_uncorr for j in ['Up']],
                  #'outputbranchsel'  : os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerModules/removeNomBranch_CHToCB.txt',
               }
    dictionary[base_name+"_"+"jetMETSyst_uncorrDown"] = {
                  'isChain'    : True,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'subTargets': [base_name+"_" + syst + j for syst in syst_uncorr for j in ['Down']],
                  #'outputbranchsel'  : os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerModules/removeNomBranch_CHToCB.txt',
               }
    dictionary[base_name+"_"+"jetMETSyst_corrUp"] = {
                  'isChain'    : True,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'subTargets': [base_name+"_" + syst + j for syst in syst_corr for j in ['Up']],
                  #'outputbranchsel'  : os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerModules/removeNomBranch_CHToCB.txt',
               }
    dictionary[base_name+"_"+"jetMETSyst_corrDown"] = {
                  'isChain'    : True,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'subTargets': [base_name+"_" + syst + j for syst in syst_corr for j in ['Down']],
                  #'outputbranchsel'  : os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerModules/removeNomBranch_CHToCB.txt',
               }
    return dictionary


Steps = {

# ------------------------------------------------ CHAINS ----------------------------------------------------

  'MCnofilter' : {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'subTargets' : ['leptonMaker'],
                 },

## ------- MC:

# 'MCl1loose2016': {
#                 'isChain'    : True  ,
#                 'do4MC'      : True  ,
#                 'do4Data'    : False ,
#                 'selection'  : '"(nElectron>0 && Electron_pt[0]>10) || (nMuon>0 && Muon_pt[0]>10)"' , 
#                 'subTargets' : ['baseW', 'leptonMaker','lepSel', 'puW2016', 'l2Kin', 'l3Kin', 'l4Kin', 'btagPerJet2016', 'btagPerEvent'],
#               },

# 'MCl1loose2017': {
#                 'isChain'    : True  ,
#                 'do4MC'      : True  ,
#                 'do4Data'    : False ,
#                 'selection'  : '"((nElectron+nMuon)>0)"' ,
#                 'subTargets' : ['leptonMaker','lepSel', 'puW2017', 'l2Kin', 'l3Kin', 'l4Kin', 'btagPerJet2017', 'btagPerEvent'],
#               },


  'MCl1loose2016' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL', 'ggHTheoryUncertainty', 'DressedLeptons'],
                                 # 'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },

  'MCl1loose2016v5' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },

                               #   'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
  'MCl2loose2016_hmumu' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel_hmumu_2016','CleanJetCut',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch','TriggerObjectMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },

  'MCl1loose2016v6' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom', 'CorrFatJetMC', 'CleanFatJet',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],  
                  },

  # FIXME: check btagPerJet2016, btagPerEvent
  # FIXME: Cfg 'trigMC','LeptonSF','puW'
  'MCCorr2016' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','btagPerJet2016',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto'],
                },

  # copied but still missing the MonoH triggers -> will be patched later
  'MCCorr2016v5' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','btagPerJet2016',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto'],
                },

  'MCCorr2016v5mh' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','btagPerJet2016',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto',
                                     'MHTrigMC','MHSwitch','formulasMCMH' ],
                },

  'MCCorr2016v6' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','btagPerJet2016',
                                     'rochesterMC','trigMC','trigMC_Cut','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto',
                                     'wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK','HiggsGenVars',
                                     'MHTrigMC','MHSwitch','formulasMCMH' ],
                },

  'MCCorr2016_hmumu' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','btagPerJet2016',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'formulasMC','EmbeddingVeto'],
                },

  'MCCorr2016tmp'  : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','puW','rochesterMC','l2Kin','formulasMC16tmp'],
                     'onlySample' : ['DYJetsToLL_M-50_ext2'],
                 },

  'MCMonoH2016' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['MHTrigMC','MHSwitch','MonoHiggsMVA','l3Kin','formulasMCMH'],
                 },

  'MCMonoH' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['MHTrigMC','MHSwitch','MonoHiggsMVA','l3Kin','formulasMCMH'],
                 },

  'DATAMonoH' : {
                     'isChain'    : True  ,
                     'do4MC'      : False  ,
                     'do4Data'    : True ,
                     'subTargets' : ['MHTrigData','MHSwitch','MonoHiggsMVA','l3Kin'],
                 },


### OLD Stuff begin

  'MCl1loose2017v2': {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel', 'puW2017', 'l2Kin', 'l3Kin', 'l4Kin', 'btagPerJet2017', 'btagPerEvent','PrefCorr2017'],
                },

  'MCCorr2017OLD' : {
                 'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'subTargets' : ['baseW','PrefCorr2017','jetSel','CleanJetCut', 'btagPerJet2017', 'btagPerEvent' ,
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL',
                                  'ggHTheoryUncertainty', 'DressedLeptons', 'WGammaStar',
                                  'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC'],
                    },

  'MCCorr2017_SemiLep' : {
                 'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'subTargets' : ['jetSel','CleanJetCut', 
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL',
                                  'ggHTheoryUncertainty', 'DressedLeptons', 
                                  'rochesterMC','trigMC'],
                    },

### OLD stuff End

  'MCl1loose2017' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },

  'MCl1loose2017v5' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },

  'MCl1loose2017v6' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom','CorrFatJetMC', 'CleanFatJet',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],  
                  },


  'MCCorr2017' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','btagPerJet2017',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto'],
                },

  'MCCorr2017v5' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','btagPerJet2017',
                                     'rochesterMC','trigMC','MHTrigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','MHSwitch','formulasMC','EmbeddingVeto'],
                },

  'MCCorr2017v6' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','btagPerJet2017',
                                     'rochesterMC','trigMC','trigMC_Cut','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto',
                                     'wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK','HiggsGenVars',  
                                     'MHTrigMC','MHSwitch','formulasMCMH' ],
                },


  'MCCorr2017LP19' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','btagPerJet2017',
                                     'rochesterMCLP19','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19','EmbeddingVeto'],
                },


  'PUFIXLP19' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['puW','formulasMCLP19'],
  },               

  'MVAFix' : { 
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : [ 'DYMVA','MonoHiggsMVA' ] ,
             }, 

  'MCl1loose2018' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },

  'MCl1loose2018v5' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },

  'MCl1loose2018v6' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom','CorrFatJetMC', 'CleanFatJet',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],  
                  },

  'MCCorr2018' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','btagPerJet2018',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto'],
                },
  # copied but still missing the MonoH triggers -> will be patched later
  'MCCorr2018v5' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','btagPerJet2018',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto'],
                },

  'MCCorr2018v6' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','btagPerJet2018',
                                     'rochesterMC','trigMC','trigMC_Cut','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto',
                                     'wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK', 'wNLOEWK',
                                     'MHTrigMC','MHSwitch','formulasMCMH' ],
                },


  'MCGenOnly': {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'subTargets' : ['PromptParticlesGenVars','GenVar', 'HiggsGenVars', 'ggHTheoryUncertainty', 'DressedLeptons',
                                  'baseW'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/MCGenOnly_outputbranches.txt'
               },

  'l23Kin': {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : True ,
                  'subTargets' : ['l2Kin', 'l3Kin'],
            },

## ------- WgStar MC:

  'MCWgStar2017' : { 
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'selection'  : '"((nElectron+nMuon)>1)"' ,
                     'subTargets' : ['leptonMaker','WgSSel', 
                                     'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar'],
                     'onlySample' : [
                                   'Wg500','Wg_AMCNLOFXFX','WZTo3LNu','Wg_MADGRAPHMLM',
                                   #'Wg500','Wg_AMCNLOFXFX','WZTo3LNu','WgStarLNuEE','WgStarLNuMuMu','Wg_MADGRAPHMLM',
                                   'DYJetsToLL_M-10to50', 'DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',
                                   'DYJetsToLL_M-5to50-LO','DYJetsToLL_M-50-LO-ext1',
                                   'TTTo2L2Nu', 'ST_tW_antitop', 'ST_tW_top', 'ST_s-channel', 'ST_t-channel_antitop', 'ST_t-channel_top', 'ZZTo2L2Nu',
                                   'ZZTo4L', 'ZZTo2L2Q', 
                                   'WWW', 'WWZ', 'WZZ', 'ZZZ',
                                   'GluGluToWWToENEN',
                                   'GluGluToWWToENMN',
                                   'GluGluToWWToENTN',
                                   'GluGluToWWToMNEN',
                                   'GluGluToWWToMNMN',
                                   'GluGluToWWToMNTN',
                                   'GluGluToWWToTNEN',
                                   'GluGluToWWToTNMN',
                                   'GluGluToWWToTNTN',
                                   'WZTo2L2Q','WZTo3LNu_mllmin01','WZTo3LNu', 'Zg', 
                                 ]
                   },

  'MCWgStarCorr2017' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','jetSel','CleanJetCut','btagPerJet2017', 'btagPerEvent',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC'],
                    },

   'MCWgStarCorr2017LP19' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','jetSel','CleanJetCut','btagPerJet2017', 'btagPerEvent',
                                     'rochesterMCLP19','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
                    }, 

#   ---> v5

 'MCWgStar201Xv5' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'selection'  : '"((nElectron+nMuon)>1)"' ,
                     'subTargets' : ['leptonMaker','WgSSel','jetSelCustom',
                                     'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar','ggHTheoryUncertainty', 'DressedLeptons'],
                     'onlySample' : [
                                   'Wg500',
                                   'Wg_AMCNLOFXFX','Wg_AMCNLOFXFX_ext2','Wg_AMCNLOFXFX_ext3',
                                   'WZTo3LNu','WZTo3LNu_ext1',
                                   'WZTo3LNu_mllmin01',
                                   'WZTo3LNu_powheg',
                                   'Wg_MADGRAPHMLM',
                                   #'Wg500','Wg_AMCNLOFXFX','WZTo3LNu','WgStarLNuEE','WgStarLNuMuMu','Wg_MADGRAPHMLM',
                                   'DYJetsToLL_M-10to50','DYJetsToLL_M-10to50_ext1',
                                   'DYJetsToLL_M-50','DYJetsToLL_M-50_ext','DYJetsToLL_M-50_ext1','DYJetsToLL_M-50_ext2', 
                                   'DYJetsToLL_M-5to50-LO',
                                   'DYJetsToLL_M-50-LO','DYJetsToLL_M-50-LO_ext1','DYJetsToLL_M-50-LO_ext2',
                                   'TTTo2L2Nu', 
                                   'ST_tW_antitop','ST_tW_antitop_ext1','ST_tW_antitop_noHad','ST_tW_antitop_noHad_ext1', 
                                   'ST_tW_top','ST_tW_top_ext1','ST_tW_top_noHad','ST_tW_top_noHad_ext1', 
                                   'ST_s-channel','ST_s-channel_ext1', 
                                   'ST_t-channel_antitop', 
                                   'ST_t-channel_top', 
                                   'ZZTo2L2Nu','ZZTo2L2Nu_ext1','ZZTo2L2Nu_ext2',
                                   'ZZTo4L','ZZTo4L_ext1','ZZTo4L_ext2', 
                                   'ZZTo2L2Q',
                                   'WWW', 'WWZ', 'WZZ', 'ZZZ',
                                   'GluGluToWWToENEN',
                                   'GluGluToWWToENMN',
                                   'GluGluToWWToENTN',
                                   'GluGluToWWToMNEN',
                                   'GluGluToWWToMNMN',
                                   'GluGluToWWToMNTN',
                                   'GluGluToWWToTNEN',
                                   'GluGluToWWToTNMN',
                                   'GluGluToWWToTNTN',
                                   'WZTo2L2Q','Zg',
                                 ]
                   },

  'MCWgStarCorr2016v5' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','btagPerJet2016',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto'],
                   },

  'MCWgStarCorr2017v5' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','btagPerJet2017',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto'],
                   },

  'MCWgStarCorr2018v5' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','btagPerJet2018',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC','EmbeddingVeto'],
                   }, 


## ------- DATA:
    
  'DATAl1loose2016': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],
                },

  'DATAl1loose2016v5': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  #'subTargets' : ['leptonMaker','lepSel','jetSelCustom', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData','MHTrigData','MHSwitch', 'formulasDATA'],
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],
                 },

  'DATAl1loose2016v6': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom','CorrFatJetData','CleanFatJet','rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData','MHTrigData','MHSwitch', 'formulasDATA'],
                 },


  'DATAl1loose2017': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],
                },

  'DATAl1loose2017LP19': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut', 'rochesterDATALP19' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATALP19'],
                },

  'DATAl1loose2017v5': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData','MHTrigData','MHSwitch', 'formulasDATA'],
                },

  'DATAl1loose2017v6': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom','CorrFatJetData','CleanFatJet', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData','MHTrigData','MHSwitch', 'formulasDATA'],
                },


# 'DATAl1loose2017': {
#                 'isChain'    : True  ,
#                 'do4MC'      : False ,
#                 'do4Data'    : True  ,
#                 'selection'  : '"((nElectron+nMuon)>0)"' ,
#                 'subTargets' : ['leptonMaker','lepSel', 'l2Kin', 'l3Kin', 'l4Kin','trigData','formulasDATA'],
#               }, 

  'DATAl1loose2017v2': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel', 'l2Kin', 'l3Kin', 'l4Kin','trigData','formulasDATA'],
                },

  'DATACorr2017' : {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'subTargets' : ['rochesterDATA','jetSel','CleanJetCut','l2Kin', 'l3Kin', 'l4Kin','formulasDATA'],
                },

  'DATAl1loose2018': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],
                },

  'DATAl1loose2018v5': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],
                },


  'DATAl1loose2018v6': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom','CorrFatJetData','CleanFatJet', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData','MHTrigData','MHSwitch', 'formulasDATA'],
                },


  'jetSelfix': {
                  'isChain'    : True  ,
                  'do4MC'      : True ,
                  'do4Data'    : True  , 
                  'subTargets' : ['jetSel','l2Kin', 'l3Kin', 'l4Kin']
               },

## ------- WgStar DATA:

    'DATAWgStar2017v2' : { 
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','WgSSel', 'rochesterDATA','jetSel','CleanJetCut' , 'l2Kin', 'l3Kin', 'l4Kin','trigData','formulasDATA'],
                   },

   'DATAWgStar2017LP19': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','WgSSel','jetSel','CleanJetCut', 'rochesterDATALP19' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATALP19'],
                },


##     --> v5

    'DATAWgStar2016v5' : {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','WgSSel', 'rochesterDATA','jetSelCustom', 'l2Kin', 'l3Kin', 'l4Kin','trigData','formulasDATA'],
                   },


    'DATAWgStar2017v5' : {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','WgSSel', 'rochesterDATA','jetSelCustom', 'l2Kin', 'l3Kin', 'l4Kin','trigData','formulasDATA'],
                   },

    'DATAWgStar2018v5' : {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','WgSSel', 'rochesterDATA','jetSelCustom', 'l2Kin', 'l3Kin', 'l4Kin','trigData','formulasDATA'],
                   },


## ------- EMBEDDING:

    'Embedding2018' : { 
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'subTargets' : ['EmbeddingWeights2018','trigMCKeepRun','LeptonSF','formulasEMBED'],
                   },

    'Embedding2017' : { 
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'subTargets' : ['EmbeddingWeights2017','trigMCKeepRun','LeptonSF','formulasEMBED'],
                   },

    'Embedding2016' : { 
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'subTargets' : ['EmbeddingWeights2016','trigMCKeepRun','LeptonSF','formulasEMBED'],
                   },

## ------- HIGH MASS:




  'HMSemilepSkimJH2016v6_3' : {
    'isChain'    : True  ,
    'do4MC'      : True  ,
    'do4Data'    : False  ,
    'selection'  :'"(Lepton_pt[0]>20 \
    && ( fabs(Lepton_eta[0])  < 2.5*(abs(Lepton_pdgId[0])==11) \
    ||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
    && ( ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
    ||   ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
    ))&&\
    (Trigger_sngMu || Trigger_sngEl)&&\
    ((Sum$(CleanJet_pt > 20) > 1) || (nCleanFatJet > 0 ))\
    "',    

    'subTargets' : ['l1tightOR2016v6','wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK', 'trigMC', 'CorrFatJetMC', 'CleanFatJet' ],

  },##['wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK',

  ##
#'CorrFatJetData', 'CleanFatJet'
  'HMSemilepSkimJH2016v6_3_data' : {
    'isChain'    : True  ,
    'do4MC'      : False  ,
    'do4Data'    : True  ,
    'selection'  :'"(Lepton_pt[0]>20 \
    && ( fabs(Lepton_eta[0])  < 2.5*(abs(Lepton_pdgId[0])==11) \
    ||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
    && ( ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
    ||   ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
    ))&&\
    (Trigger_sngMu || Trigger_sngEl)&&\
    ((Sum$(CleanJet_pt > 20) > 1) || (nCleanFatJet > 0 ))\
    "',    

    'subTargets' : ['l1tightOR2016v6','CorrFatJetData','CleanFatJet'],

  },##['wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK',


 'HMSemilepSkimJH2017v6_3' : {
     'isChain'    : True  ,
    'do4MC'      : True  ,
    'do4Data'    : False  ,
    'selection'  :'"(  Lepton_pt[0]>20 \
    && ( fabs(Lepton_eta[0])  < 2.5*(abs(Lepton_pdgId[0])==11) \
    ||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
    && ( ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
    ||   ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
    ))&&\
    (Trigger_sngMu || Trigger_sngEl)&&\
    ((Sum$(CleanJet_pt > 20) > 1) || (nCleanFatJet > 0 ))\
    "',
    'subTargets' : ['l1tightOR2017v6','wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK', 'trigMC', 'CorrFatJetMC', 'CleanFatJet' ],
  },    

 'HMSemilepSkimJH2017v6_3_data' : {
     'isChain'    : True  ,
    'do4MC'      : False  ,
    'do4Data'    : True  ,
    'selection'  :'"(  Lepton_pt[0]>20 \
    && ( fabs(Lepton_eta[0])  < 2.5*(abs(Lepton_pdgId[0])==11) \
    ||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
    && ( ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
    ||   ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
    ))&&\
    (Trigger_sngMu || Trigger_sngEl)&&\
    ((Sum$(CleanJet_pt > 20) > 1) || (nCleanFatJet > 0 ))\
    "',
    'subTargets' : ['l1tightOR2017v6','CorrFatJetData','CleanFatJet'],

  },    
 
  'HMSemilepSkimJH2018v6_3' : {
    'isChain'    : True  ,
    'do4MC'      : True  ,
    'do4Data'    : False  ,
    'selection'  :'"(  Lepton_pt[0]>20 \
    && ( fabs(Lepton_eta[0])  < 2.5*(abs(Lepton_pdgId[0])==11)\
    ||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
    && ( ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
    ||   ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
    ))&&\
    (Trigger_sngMu || Trigger_sngEl)&&\
    ((Sum$(CleanJet_pt > 20) > 1) || (nCleanFatJet > 0 ))\
    "',
    'subTargets' : ['l1tightOR2018v6','wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK', 'trigMC', 'CorrFatJetMC', 'CleanFatJet' ],

  },

  'HMSemilepSkimJH2018v6_3_data' : {
    'isChain'    : True  ,
    'do4MC'      : False  ,
    'do4Data'    : True  ,
    'selection'  :'"(  Lepton_pt[0]>20 \
    && ( fabs(Lepton_eta[0])  < 2.5*(abs(Lepton_pdgId[0])==11)\
    ||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
    && ( ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
    ||   ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
    ))&&\
    (Trigger_sngMu || Trigger_sngEl)&&\
    ((Sum$(CleanJet_pt > 20) > 1) || (nCleanFatJet > 0 ))\
    "',
    'subTargets' : ['l1tightOR2018v6','CorrFatJetData','CleanFatJet'],

  },

  'HMSemilepSkimJH2016v6_2' : {
    'isChain'    : True  ,
    'do4MC'      : True  ,
    'do4Data'    : True  ,
    'selection'  :'"(Lepton_pt[0]>20 \
    && ( fabs(Lepton_eta[0])  < 2.5*(abs(Lepton_pdgId[0])==11) \
    ||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
    && ( ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
    ||   ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
    ))&&\
    (Trigger_sngMu || Trigger_sngEl)&&\
    ((Sum$(CleanJet_pt > 20) > 1) || (nCleanFatJet > 0 ))\
    "',    

    'subTargets' : ['l1tightOR2016v6','BWReweight'],

  },##['wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK',

  'HMSemilepSkimJH2017v6_2' : {
     'isChain'    : True  ,
    'do4MC'      : True  ,
    'do4Data'    : True  ,
    'selection'  :'"(  Lepton_pt[0]>20 \
    && ( fabs(Lepton_eta[0])  < 2.5*(abs(Lepton_pdgId[0])==11) \
    ||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
    && ( ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
    ||   ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
    ))&&\
    (Trigger_sngMu || Trigger_sngEl)&&\
    ((Sum$(CleanJet_pt > 20) > 1) || (nCleanFatJet > 0 ))\
    "',
    'subTargets' : ['l1tightOR2017v6','BWReweight'], ##need MELA discriminator

  },

  'HMSemilepSkimJH2018v6_2' : {
    'isChain'    : True  ,
    'do4MC'      : True  ,
    'do4Data'    : True  ,
    'selection'  :'"(  Lepton_pt[0]>20 \
    && ( fabs(Lepton_eta[0])  < 2.5*(abs(Lepton_pdgId[0])==11) \
    ||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
    && ( ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
    ||   ( Alt$( Lepton_pt[1],-1) < 15*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
    ))&&\
    (Trigger_sngMu || Trigger_sngEl)&&\
    ((Sum$(CleanJet_pt > 20) > 1) || (nCleanFatJet > 0 ))\
    "',
    'subTargets' : ['l1tightOR2018v6','BWReweight'],

  },


  'HMSemilepJH' : {
    'isChain'    : True  ,
    'do4MC'      : True  ,
    'do4Data'    : True  ,
    'subTargets' : ['whadJetSel','wlepMaker'],

  },


  'HMSemilepJH_JESup' : {
    'isChain'    : True  ,
    'do4MC'      : True  ,
    'do4Data'    : True  ,
    'subTargets' : ['whadJetSel_JESup','wlepMaker_JESup'],

  },




    'Semilep2016' : { 
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['l1tightOR2016v5','PreselFatJet','whadJetSel','wlepMaker'],
                  #'onlySample' : LNuQQSamples,
                   },

    'Semilep2017' : { 
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['PreselFatJet','whadJetSel','wlepMaker'],
                  #'subTargets' : ['l1tightOR2017v5','PreselFatJet','whadJetSel','wlepMaker'],
                  #'onlySample' : LNuQQSamples,
                   },

    'Semilep2018' : { 
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['l1tightOR2018v5','PreselFatJet','whadJetSel','wlepMaker'],
                  #'onlySample' : LNuQQSamples,
                   },

    'HighMass' : { 
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['HMvars','BWReweight'],
                   },
   
 'HMSemilepSkimJH2017v6_5' : {
     'isChain'    : True  ,
    'do4MC'      : True  ,
    'do4Data'    : False  ,
    'selection'  :'"(  Lepton_pt[0]>20 \
    && ( fabs(Lepton_eta[0])  < 2.5*(abs(Lepton_pdgId[0])==11) \
    ||   fabs(Lepton_eta[0])  < 2.4*(abs(Lepton_pdgId[0])==13))\
    && ( ( Alt$( Lepton_pt[1],-1) < 20*( abs( Alt$(Lepton_pdgId[1], 11)) ==11) )\
    ||   ( Alt$( Lepton_pt[1],-1) < 20*( abs( Alt$(Lepton_pdgId[1], 13)) ==13) )\
    ))&&\
    (Trigger_sngMu || Trigger_sngEl)\
    &&(PuppiMET_pt > 20)\
    "',
    'subTargets' : ['l1tightOR2017v6','wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK', 'trigMC', 'CorrFatJetMC', 'CleanFatJet' ],
  },    

    'HMlnjjLepVetoBWRew'  : {
                  'isChain'    : True,
                  'do4MC'      : True,
                  'do4Data'    : True,
                  'selection'  : '"(Lepton_pt[0] > 30 && (Alt$(Lepton_pt[1], 0) < 10))"',
                  'subTargets' : ['BWReweight'],
		  },

     #'selection'  : '"(Lepton_pt[0] > 30 && (Alt$(Lepton_pt[1], 0) < 10))"',
     #'subTargets' : ['BWReweight'],


  'HighMassSemilepLHEAnalyzer': {
    'isChain'    : False ,
    'do4MC'      : True  ,
    'do4Data'    : False  ,
    'import'  : 'LatinoAnalysis.NanoGardener.modules.HighMassSemilepLHEAnalyzer',
    'declare' : 'HighMassSemilepLHEAna = lambda : HighMassSemilepLHEAnalyzer()',
    'module'  : 'HighMassSemilepLHEAna()'
  },

  'HighMassSemilepLHEAnalyzerVBF': {
    'isChain'    : False ,
    'do4MC'      : True  ,
    'do4Data'    : False  ,
    'import'  : 'LatinoAnalysis.NanoGardener.modules.HighMassSemilepLHEAnalyzerVBF',
    'declare' : 'HighMassSemilepLHEAnaVBF = lambda : HighMassSemilepLHEAnalyzerVBF()',
    'module'  : 'HighMassSemilepLHEAnaVBF()'
  },

    'HMlnjjFatJet' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  'declare'    : 'fatjetMaker = lambda : FatJetMaker(jetid=1, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=1.0, over_jetR=0.8)',
                  'module'     : 'fatjetMaker()'
    },

		  #	|| Alt$( !Lepton_isLoose[1],1 ) )



# ------------------------------------------------ MODULES ---------------------------------------------------

## ------- MODULES: Exo analyses                                                                                                                                    
    'TopPlusDMRunIILegacy': {
                   'isChain'    : True ,
                   'do4MC'      : True  ,
                   'do4Data'    : False ,
                   'import'     : 'LatinoAnalysis.NanoGardener.modules.mt2Producer' ,
                   'subTargets' : ['mT2Davis'],
    },

    'mT2Davis': {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : True ,
                   'import'     : 'LatinoAnalysis.NanoGardener.modules.mt2Producer' ,
                   'module'     : 'mt2Producer()' ,
    },

## ------- MODULES: MonoHiggs

#### MHTrigs step only works for 2016 and 2017 for now !!!!!!
  'MHTrigData' : { 
                  'isChain'  : False ,
                  'do4MC'    : False ,
                  'do4Data'  : True  ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                  'declare'  : 'MHTrigData = lambda : TrigMaker("RPLME_CMSSW",True,keepRunP=True,cfg_path="LatinoAnalysis/NanoGardener/python/data/TrigMakerMonoHiggs_cfg.py")',
                  'module'   : 'MHTrigData()',
               },

  'MHTrigMC'   : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : False ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                  'declare'  : 'MHTrigMC = lambda : TrigMaker("RPLME_CMSSW",False,keepRunP=True,cfg_path="LatinoAnalysis/NanoGardener/python/data/TrigMakerMonoHiggs_cfg.py")',
                  'module'   : 'MHTrigMC()',
               },
####
  'MHSwitch' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.Switch' ,
                  'declare'  : 'MHSwitch = lambda : Switch(cmssw="RPLME_CMSSW", cfg_path="LatinoAnalysis/NanoGardener/python/data/switch/MH_triggerSwitch_cfg.py")',
                  'module'   : 'MHSwitch()',
               },

  'MonoHiggsMVA' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py")',
                  'module'   : 'MonoHiggsMVA()',
               },

               
  'MonoHiggsMVA_ElepTup' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_ElepTup = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="ElepTup")',
                  'module'   : 'MonoHiggsMVA_ElepTup()',
               },

               
  'MonoHiggsMVA_ElepTdo' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_ElepTdo = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="ElepTdo")',
                  'module'   : 'MonoHiggsMVA_ElepTdo()',
               },

  'MonoHiggsMVA_MupTup' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_MupTup = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="MupTup")',
                  'module'   : 'MonoHiggsMVA_MupTup()',
               },

               
  'MonoHiggsMVA_MupTdo' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_MupTdo = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="MupTdo")',
                  'module'   : 'MonoHiggsMVA_MupTdo()',
               },
  'MonoHiggsMVA_METup' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_METup = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="METup")',
                  'module'   : 'MonoHiggsMVA_METup()',
               },

               
  'MonoHiggsMVA_METdo' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_METdo = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="METdo")',
                  'module'   : 'MonoHiggsMVA_METdo()',
               },
  'MonoHiggsMVA_JESup' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_JESup = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="JESup")',
                  'module'   : 'MonoHiggsMVA_JESup()',
               },

               
  'MonoHiggsMVA_JESdo' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA_JESdo = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py", branch_map="JESdo")',
                  'module'   : 'MonoHiggsMVA_JESdo()',
               },

## ------- MODULES: MC Kinematic
  
  'PromptParticlesGenVars' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.PromptParticlesGenVarsProducer' ,
                  'declare'    : 'PromptParticlesGenVars = lambda : PromptParticlesGenVarsProducer()',
                  'module'     : 'PromptParticlesGenVars()',
                  } , 


  'GenVar'       : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenVarProducer' ,
                  'declare'    : 'GenVar = lambda : GenVarProducer()',
                  'module'     : 'GenVar()' ,
                   },

  'GenLeptonMatch' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenLeptonMatchProducer' ,
                  'declare'    : 'GenLeptonMatch = lambda : GenLeptonMatchProducer()',
                  'module'     : 'GenLeptonMatch()' ,
                   },

  'TriggerObjectMatch' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TriggerObjectMatchProducer' ,
                  'declare'    : 'TriggerObjectMatch = lambda : TriggerObjectMatchProducer()',
                  'module'     : 'TriggerObjectMatch()' ,
                   },

   'HiggsGenVars' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.HiggsGenVarsProducer' ,
                  'declare'    : 'HiggsGenVars = lambda : HiggsGenVarsProducer()',
                  'module'     : 'HiggsGenVars()',
                  } ,                 

   'DressedLeptons': {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False  ,
                   'import'     : 'LatinoAnalysis.NanoGardener.modules.DressedLeptonProducer' ,
                   'declare'    : 'dressedLeptons = lambda : DressedLeptonProducer(0.3)',
                   'module'     : 'dressedLeptons()' 
                  },

   'ggHTheoryUncertainty':  {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False  ,
                   'import'     : 'LatinoAnalysis.NanoGardener.modules.GGHUncertaintyProducer' ,
                   'declare'    : 'ggHUncertaintyProducer = lambda : GGHUncertaintyProducer()',
                   'module'     : 'ggHUncertaintyProducer()',
                   'onlySample' : [
                                  'GluGluHToWWTo2L2NuPowheg_M125_PrivateNano',
                                  'GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2NuPowhegNNLOPS_M125_private',
                                  'GluGluHToWWTo2L2NuPowhegNNLOPS_M125',
                                  'GGHjjToWWTo2L2Nu_minloHJJ_M125'
                                  ]
                  },    

   'TopGenVars' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TopGenVarsProducer' ,
                  'declare'    : 'TopGenVars = lambda : TopGenVarsProducer()',
                  'module'     : 'TopGenVars()',
                  'onlySample' : [
                                  'TTTo2L2Nu',
                                  'TTTo2L2Nu_PSWeights_CP5Down',
                                  'TTTo2L2Nu_PSWeights_CP5Up',
                                  'TTTo2L2Nu_PSWeights',
                                  'TTToSemiLeptonic',
                                  'TTWjets',
                                  'TTWjets_ext1'
                                  'TTZjets',
                                  'TTZjets_ext1',
                                  'ST_s-channel',
                                  'ST_s-channel_ext1',
                                  'ST_t-channel_antitop',
                                  'ST_t-channel_top',
                                  'ST_tW_antitop',
                                  'ST_tW_antitop_ext1',
                                  'ST_tW_top',
                                  'ST_tW_top_ext1',
                                 ]
                  } ,

    'wwNLL' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.wwNLLcorrectionWeightProducer' ,
                  'declare'    : 'wwNLL = lambda : wwNLLcorrectionWeightProducer()',
                  'module'     : 'wwNLL()',
                  'onlySample' : ['WW-LO', 'WWTo2L2Nu', 'WWTo2L2Nu_CP5Up', 'WWTo2L2Nu_CP5Down']
                  } ,

    'wwNLOEWK' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.qq2vvEWKcorrectionsWeightProducer' ,
                  'declare'    : 'wwNLOEWK = lambda : vvNLOEWKcorrectionWeightProducer("ww")',
                  'module'     : 'wwNLOEWK()',
                  'onlySample' : [ 'WWTo2L2Nu', 'WWTo2L2Nu_CP5Up', 'WWTo2L2Nu_CP5Down',
                                  'WmToLNu_WmTo2J_QCD', 'WpToLNu_WpTo2J_QCD', 'WpToLNu_WmTo2J_QCD', 'WpTo2J_WmToLNu_QCD'
                                  ]
                  } ,


    'wzNLOEWK' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.qq2vvEWKcorrectionsWeightProducer' ,
                  'declare'    : 'wzNLOEWK = lambda : vvNLOEWKcorrectionWeightProducer("wz")',
                  'module'     : 'wzNLOEWK()',
                  'onlySample' : ['WZTo3LNu', 'WZTo3LNu_ext1', 'WZTo2L2Q', 'WZTo3LNu_mllmin01', 'WZTo3LNu_powheg',
                                  'WmTo2J_ZTo2L_QCD', 'WmToLNu_ZTo2J_QCD', 'WpTo2J_ZTo2L_QCD', 'WpToLNu_ZTo2J_QCD'
                                  ]
                  } ,

    'zzNLOEWK' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.qq2vvEWKcorrectionsWeightProducer' ,
                  'declare'    : 'zzNLOEWK = lambda : vvNLOEWKcorrectionWeightProducer("zz")',
                  'module'     : 'zzNLOEWK()',
                  'onlySample' : ['ZZTo2L2Nu','ZZTo2L2Nu_ext1','ZZTo2L2Nu_ext2', 'ZZTo4L','ZZTo4L_ext1','ZZTo4L_ext2', 'ZZTo2L2Q',
                                  'ZTo2L_ZTo2J_QCD'
                                  ]
                  } ,

    'wNLOEWK' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.qq2VEWKcorrectionsWeightProducer' ,
                  'declare'    : 'wNLOEWK = lambda : vNLOEWKcorrectionWeightProducer("w")',
                  'module'     : 'wNLOEWK()',
                  'onlySample' : [
                                  ####
                                  'WJetsToLNu-LO','WJetsToLNu-LO_ext1'
                                  'WJetsToLNu',
                                  'WJetsToLNu_HT70_100','WJetsToLNu_HT100_200',
                                  'WJetsToLNu_HT200_400','WJetsToLNu_HT400_600',
                                  'WJetsToLNu_HT600_800','WJetsToLNu_HT800_1200',
                                  'WJetsToLNu_HT1200_2500','WJetsToLNu_HT2500_inf',
                                  ]
                  } ,

    'zNLOEWK' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.qq2VEWKcorrectionsWeightProducer' ,
                  'declare'    : 'wNLOEWK = lambda : vNLOEWKcorrectionWeightProducer("z")',
                  'module'     : 'wNLOEWK()',
                  'onlySample' : [  
                                   #### DY
                                  'DYJetsToLL_M-5to50-LO',
                                  'DYJetsToLL_M-10to50',
                                  'DYJetsToLL_M-50','DYJetsToLL_M-50_ext1',
                                  'DYJetsToLL_M-10to50ext3','DYJetsToLL_M-50-LO',
                                  'DYJetsToLL_M-50-LO-ext1','DYJetsToLL_M-10to50-LO',
                                  'DYJetsToTT_MuEle_M-50','DYJetsToLL_M-50_ext2',
                                  'DYJetsToLL_M-10to50-LO-ext1',
                                   # ... Low Mass HT
                                  'DYJetsToLL_M-4to50_HT-100to200',
                                  'DYJetsToLL_M-4to50_HT-100to200-ext1',
                                  'DYJetsToLL_M-4to50_HT-200to400',
                                  'DYJetsToLL_M-4to50_HT-200to400-ext1',
                                  'DYJetsToLL_M-4to50_HT-400to600',
                                  'DYJetsToLL_M-4to50_HT-400to600-ext1',
                                  'DYJetsToLL_M-4to50_HT-600toInf',
                                  'DYJetsToLL_M-4to50_HT-600toInf-ext1',
                                   # ... high Mass HT
                                  'DYJetsToLL_M-50_HT-70to100',
                                  'DYJetsToLL_M-50_HT-100to200',
                                  'DYJetsToLL_M-50_HT-200to400',
                                  'DYJetsToLL_M-50_HT-400to600',
                                  'DYJetsToLL_M-50_HT-600to800',
                                  'DYJetsToLL_M-50_HT-800to1200',
                                  'DYJetsToLL_M-50_HT-1200to2500',
                                  'DYJetsToLL_M-50_HT-2500toInf',
                                  ]
                  } ,


#
#  This woudl be for Z>nunu sample, but we currently don't use it
#
#    'zvvNLOEWK' : {
#                  'isChain'    : False ,
#                  'do4MC'      : True  ,
#                  'do4Data'    : False  ,
#                  'import'     : 'LatinoAnalysis.NanoGardener.modules.qq2VEWKcorrectionsWeightProducer' ,
#                  'declare'    : 'wNLOEWK = lambda : vNLOEWKcorrectionWeightProducer("zvv")',
#                  'module'     : 'wNLOEWK()',
#                  'onlySample' : [''
#                                  ]
#                  } ,


    'WGammaStar' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.WGammaStar',
                  'declare'    : 'wGS = lambda : WGammaStarV2()',
                  'module'     : 'wGS()',
                  } ,

    'redoWGammaStar' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.WGammaStar',
                  'declare'    : 'wGS = lambda : WGammaStar()',
                  'module'     : 'wGS()',
                  'onlySample' : ['WZTo3LNu','Wg_MADGRAPHMLM','WZ','WZTo2L2Q'],
                  } ,

    'BWReweight' : { 
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.BWEwkSingletReweighter' ,
                  'declare'    : 'BWEwkSingRew = lambda : BWEwkSingletReweighter(year=RPLME_YEAR)',
                  'module'     : 'BWEwkSingRew()',
                  'onlySample' : TwoL2NuSamples + LNuQQSamples,
               },

    'MelaDisc' : { 
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.MelaDiscriminator' ,
                  'declare'    : 'MelaDisc = lambda : MelaDiscClass(year=RPLME_YEAR)',
                  'module'     : 'MelaDisc()',
               },

    'HMvars' : { 
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.HMvariables' ,
                  'declare'    : 'HMvars = lambda : HighMassVariables()',
                  'module'     : 'HMvars()',
               },

    'HMlnjjVarsGen' : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.HMlnjjVarsGen' ,
                  'declare'    : 'HMlnjjVarsGen = lambda : HMlnjjVarsGenClass("MC")',
                  'module'     : 'HMlnjjVarsGen()',
               },

    'HMlnjjVars' : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars' ,
                  'declare'    : 'HMlnjjVars = lambda : HMlnjjVarsClass(RPLME_YEAR)',
                  'module'     : 'HMlnjjVars()',
               },

    'HMlnjjVars_Dev' : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.HMlnjjVars_Dev' ,
                  'declare'    : 'HMlnjjVars_Dev = lambda : HMlnjjVarsClass_Dev(RPLME_YEAR,METtype="PuppiMET")',
                  'module'     : 'HMlnjjVars_Dev()',
               },

    'MelaHighMassKD' : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.melaHighMassKD' ,
                  'declare'    : 'MelaHighMassKD = lambda : MelaHighMassKDClass(RPLME_YEAR)',
                  'module'     : 'MelaHighMassKD()',
               },


    'assignRun': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.RunAssigner' ,
                  'declare'    : 'assignRun = lambda: RunAssigner("RPLME_CMSSW")',
                  'module'     : 'assignRun()',
            },

## ------- ChargedHiggsToCB

    'kinFitTTSemiLep_2018': {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  #'selection'  : '"Entry$<1000"',
                  #XXX
                  #2018 cuts
                  #XXX
                  #XXX
                  'selection'  : '"((Sum$(Jet_pt_nom[CleanJet_jetIdx] > 20. &&\
                                        abs(CleanJet_eta) < 2.5\
                                       ) >= 4) &&\
                                   (Sum$(Jet_pt_nom[CleanJet_jetIdx] > 20. &&\
                                        abs(CleanJet_eta) < 2.5 &&\
                                        Jet_btagDeepB[CleanJet_jetIdx] > 0.4184\
                                       )>=2))\
                                  "',
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.KinFitterProducer' ,
                  'declare'    : 'kinFitting = lambda : KinFitterProducer(RPLME_YEAR)',
                  'module'     : 'kinFitting()',
                  'outputbranchsel'  : os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerModules/removeBranch_CHToCB.txt',
               },
    'kinFitTTSemiLep_2017': {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  #'selection'  : '"Entry$<1000"',
                  #XXX
                  #2017 cuts
                  #XXX
                  #XXX
                  'selection'  : '"((Sum$(Jet_pt_nom[CleanJet_jetIdx] > 20. &&\
                                        abs(CleanJet_eta) < 2.5\
                                       ) >= 4) &&\
                                   (Sum$(Jet_pt_nom[CleanJet_jetIdx] > 20. &&\
                                        abs(CleanJet_eta) < 2.5 &&\
                                        Jet_btagDeepB[CleanJet_jetIdx] > 0.4941\
                                       )>=2))\
                                  "',
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.KinFitterProducer' ,
                  'declare'    : 'kinFitting = lambda : KinFitterProducer(RPLME_YEAR)',
                  'module'     : 'kinFitting()',
                  'outputbranchsel'  : os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerModules/removeBranch_CHToCB.txt',
               },
    'kinFitTTSemiLep_2016': {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  #'selection'  : '"Entry$<1000"',
                  #XXX
                  #2016 cuts
                  #XXX
                  #XXX
                  'selection'  : '"((Sum$(Jet_pt_nom[CleanJet_jetIdx] > 20. &&\
                                        abs(CleanJet_eta) < 2.4\
                                       ) >= 4) &&\
                                   (Sum$(Jet_pt_nom[CleanJet_jetIdx] > 20. &&\
                                        abs(CleanJet_eta) < 2.4 &&\
                                        Jet_btagDeepB[CleanJet_jetIdx] > 0.6321\
                                       )>=2))\
                                  "',
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.KinFitterProducer' ,
                  'declare'    : 'kinFitting = lambda : KinFitterProducer(RPLME_YEAR)',
                  'module'     : 'kinFitting()',
                  'outputbranchsel'  : os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerModules/removeBranch_CHToCB.txt',
               },

    'GenKinFitTTSemiLep_2018': {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  #'selection'  : '"Entry$<1000"',
                  'selection'  : '""',
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenKinFitterProducer' ,
                  'declare'    : 'GenKinFitting = lambda : GenKinFitterProducer(RPLME_YEAR)',
                  'module'     : 'GenKinFitting()',
               },



    '4j2b_CHToCB_2018' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '"((Sum$(Jet_pt_nom[CleanJet_jetIdx] > 30. &&\
                                        abs(CleanJet_eta) < 2.5\
                                       ) >= 4) &&\
                                   (Sum$(Jet_pt_nom[CleanJet_jetIdx] > 30. &&\
                                        abs(CleanJet_eta) < 2.5 &&\
                                        Jet_btagDeepB[CleanJet_jetIdx] > 0.4184\
                                       )>=2))\
                                  "',
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.Dummy',
                  'module'     : 'Dummy()',
              },
    'pruneNorm' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.Dummy',
                  'module'     : 'Dummy()',
                  'outputbranchsel'  : os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerModules/removeNomBranch_CHToCB.txt',
              },

    'genCHToCB_2016' : {
                  'isChain'    : True,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  #XXX
                  #2016 cuts
                  #XXX
                  #XXX
                  #'selection'  : '"((Sum$(Jet_pt_nom[CleanJet_jetIdx] > 20. &&\
                  #                      abs(CleanJet_eta) < 2.4\
                  #                     ) >= 4)\
                  #                  )\
                  #                "',
                  'subTargets' : ['Dummy','genCHToCB','TopGenVars_CHToCB'],
                  'outputbranchsel'  : os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerModules/removeBranch_CHToCB.txt',
              },

    'genCHToCB_2017' : {
                  'isChain'    : True,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  #XXX
                  #2017 cuts
                  #XXX
                  #XXX
                  #'selection'  : '"((Sum$(Jet_pt_nom[CleanJet_jetIdx] > 20. &&\
                  #                      abs(CleanJet_eta) < 2.5\
                  #                     ) >= 4)\
                  #                 )\
                  #                "',
                  'subTargets' : ['Dummy','genCHToCB','TopGenVars_CHToCB'],
                  'outputbranchsel'  : os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerModules/removeBranch_CHToCB.txt',
              },

    'genCHToCB_2018' : {
                  'isChain'    : True,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  #XXX
                  #2018 cuts
                  #XXX
                  #XXX
                  #'selection'  : '"((Sum$(Jet_pt_nom[CleanJet_jetIdx] > 20. &&\
                  #                      abs(CleanJet_eta) < 2.5\
                  #                     ) >= 4))\
                  #                "',
                  'subTargets' : ['Dummy','genCHToCB','TopGenVars_CHToCB'],
                  'outputbranchsel'  : os.getenv('CMSSW_BASE') + '/src/SNuAnalytics/NanoGardenerModules/removeBranch_CHToCB.txt',
              },

    'genCHToCB' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.genCHToCB',
                  'module'     : 'genCHToCB()',
                  'onlySample' : [
                                  'TTTo2L2Nu',
                                  'TTTo2L2Nu_PSWeights_CP5Down',
                                  'TTTo2L2Nu_PSWeights_CP5Up',
                                  'TTTo2L2Nu_PSWeights',
                                  'TTTo2L2Nu_TuneCP5Up',
                                  'TTTo2L2Nu_TuneCP5Down',
                                  'TTTo2L2Nu_hdampUp',
                                  'TTTo2L2Nu_hdampDown',
                                  'TTTo2L2Nu_mtopUp',
                                  'TTTo2L2Nu_mtopDown',
                                  'TTToSemiLeptonic',
                                  'TTToSemiLeptonic_ext3',
                                  'TTToSemiLeptonic_TuneCP5Up',
                                  'TTToSemiLeptonic_TuneCP5Down',
                                  'TTToSemiLeptonic_hdampUp',
                                  'TTToSemiLeptonic_hdampDown',
                                  'TTToSemiLeptonic_mtopUp',
                                  'TTToSemiLeptonic_mtopDown',
                                  'TT_TuneCUETP8M2T4Up',
                                  'TT_TuneCUETP8M2T4Down',
                                  'TT_hdampUp',
                                  'TT_hdampDown',
                                  'TT_mtopUp',
                                  'TT_mtopDown',
                                  'TTWjets',
                                  'TTWjets_ext1'
                                  'TTZjets',
                                  'TTZjets_ext1',
                                  'ST_s-channel',
                                  'ST_s-channel_ext1',
                                  'ST_t-channel_antitop',
                                  'ST_t-channel_top',
                                  'ST_tW_antitop',
                                  'ST_tW_antitop_ext1',
                                  'ST_tW_top',
                                  'ST_tW_top_ext1',
                                  'CHToCB_M075',
                                  'CHToCB_M080',
                                  'CHToCB_M085',
                                  'CHToCB_M090',
                                  'CHToCB_M100',
                                  'CHToCB_M110',
                                  'CHToCB_M120',
                                  'CHToCB_M130',
                                  'CHToCB_M140',
                                  'CHToCB_M150',
                                  'CHToCB_M160',
                                 ]
              },

    'mvaTreeCHToCB_2018': {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  #'selection'  : '"Entry$<1000"',
                  #XXX
                  'selection'  : '"((Sum$(Jet_pt_nom[CleanJet_jetIdx] > 20. &&\
                                        abs(CleanJet_eta) < 2.5\
                                       ) >= 4) &&\
                                   (Sum$(Jet_pt_nom[CleanJet_jetIdx] > 20. &&\
                                        abs(CleanJet_eta) < 2.5 &&\
                                        Jet_btagDeepB[CleanJet_jetIdx] > 0.4184\
                                       )>=2))\
                                  "',
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.mvaTreeCHToCB' ,
                  'declare'    : 'mvaTreeCHToCB_ = lambda : mvaTreeCHToCB(RPLME_YEAR)',
                  'module'     : 'mvaTreeCHToCB_()',
               },

   'TopGenVars_CHToCB' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TopGenVarsProducer' ,
                  'declare'    : 'TopGenVars = lambda : TopGenVarsProducer()',
                  'module'     : 'TopGenVars()',
                  'onlySample' : [
                                  'TTTo2L2Nu',
                                  'TTTo2L2Nu_PSWeights_CP5Down',
                                  'TTTo2L2Nu_PSWeights_CP5Up',
                                  'TTTo2L2Nu_PSWeights',
                                  'TTTo2L2Nu_TuneCP5Up',
                                  'TTTo2L2Nu_TuneCP5Down',
                                  'TTTo2L2Nu_hdampUp',
                                  'TTTo2L2Nu_hdampDown',
                                  'TTTo2L2Nu_mtopUp',
                                  'TTTo2L2Nu_mtopDown',
                                  'TTToSemiLeptonic',
                                  'TTToSemiLeptonic_ext3',
                                  'TTToSemiLeptonic_TuneCP5Up',
                                  'TTToSemiLeptonic_TuneCP5Down',
                                  'TTToSemiLeptonic_hdampUp',
                                  'TTToSemiLeptonic_hdampDown',
                                  'TTToSemiLeptonic_mtopUp',
                                  'TTToSemiLeptonic_mtopDown',
                                  'TT_TuneCUETP8M2T4Up',
                                  'TT_TuneCUETP8M2T4Down',
                                  'TT_hdampUp',
                                  'TT_hdampDown',
                                  'TT_mtopUp',
                                  'TT_mtopDown',
                                  'TTWjets',
                                  'TTWjets_ext1'
                                  'TTZjets',
                                  'TTZjets_ext1',
                                  'ST_s-channel',
                                  'ST_s-channel_ext1',
                                  'ST_t-channel_antitop',
                                  'ST_t-channel_top',
                                  'ST_tW_antitop',
                                  'ST_tW_antitop_ext1',
                                  'ST_tW_top',
                                  'ST_tW_top_ext1',
                                  'CHToCB_M075',
                                  'CHToCB_M080',
                                  'CHToCB_M085',
                                  'CHToCB_M090',
                                  'CHToCB_M100',
                                  'CHToCB_M110',
                                  'CHToCB_M120',
                                  'CHToCB_M130',
                                  'CHToCB_M140',
                                  'CHToCB_M150',
                                  'CHToCB_M160',
                                 ]
                  } ,
## ------- TEST MODULES
  'LeptonSF_BHO' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSFMaker_BHO' ,
                  'declare'    : 'LeptonSF_BHO = lambda : LeptonSFMaker_BHO("RPLME_CMSSW")',
                  'module'     : 'LeptonSF_BHO()',
                },
## ------- MODULES: Object Handling

  'Dummy' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.Dummy' ,
                  'module'     : 'Dummy()',
            },

  'leptonMaker': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonMaker' ,
                  'declare'    : 'leptonMaker = lambda : LeptonMaker()' ,
                  'module'     : 'leptonMaker()' ,
               }, 

   'lepSel': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSel' ,
                  'declare'    : 'leptonSel = lambda : LeptonSel("RPLME_CMSSW", "Loose", 1)' ,
                  'module'     : 'leptonSel()' ,
               },

   'WgSSel' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSel' ,
                  'declare'    : 'leptonSel = lambda : LeptonSel("RPLME_CMSSW", "WgStar", 2)' ,
                  'module'     : 'leptonSel()' ,
               },             

   'jetSel'  : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JetSel' ,
                  # jetid=2,pujetid='loose',minpt=15.0,maxeta=4.7,jetColl="CleanJet"
                  'declare'    : 'jetSel = lambda : JetSel(2,"medium",15.0,4.7,"CleanJet")' ,
                  'module'     : 'jetSel()' ,
               },

   'jetSelCustom' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JetSel' ,
                  # jetid=2,pujetid='loose',minpt=15.0,maxeta=4.7,jetColl="CleanJet"
                  'declare'    : 'jetSel = lambda : JetSel(2,"custom",15.0,4.7,"CleanJet")' ,
                  'module'     : 'jetSel()' ,
               },


   'CleanJetCut' : {
                 'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.CopyCleanJet',
                  'declare'    : 'cleanJetCut = lambda : CopyCleanJet(newcollectionname="CleanJetCut", cuts=["eta>2.65","eta<3.139"])',
                  'module'     : 'cleanJetCut()',
               }, 


    'CorrFatJetData' :  {
                'isChain': False,
                'do4MC': False,
                'do4Data': True,
                'import': 'PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2',
                'declare': 'corr_fatjet_data = createJMECorrector(isMC=False,dataYear=RPLME_YEAR,jesUncert="Total", redojec=True, jetType="AK8PFPuppi")',
                'module':  'corr_fatjet_data()'
    },

    'CorrFatJetMC' :  {
                'isChain': False,
                'do4MC': True,
                'do4Data': False,
                'import': 'PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2',
                'declare': 'corr_fatjet_mc = createJMECorrector(isMC=True,dataYear=RPLME_YEAR, jesUncert="Total", redojec=True, jetType="AK8PFPuppi")',
                'module':  'corr_fatjet_mc()'
    },

    'CorrJetMC' :  {
                'isChain': False,
                'do4MC': True,
                'do4Data': False,
                'import': 'PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2',
                'declare': 'corr_jet_mc = createJMECorrector(isMC=True,dataYear=RPLME_YEAR, jesUncert="Total", redojec=True, jetType="AK4PFchs")',
                'module':  'corr_jet_mc()'
    },

    'BinByBinFatJetMCJER' :  {
                'isChain': False,
                'do4MC': True,
                'do4Data': False,
                'import': 'LatinoAnalysis.NanoGardener.modules.BinByBinJERMaker',
                'declare': 'bin_by_bin_JER_maker = lambda : BinByBinJERMaker(jetColl="CleanFatJet", jer_bin_list=[0,1])',
                'module':  'bin_by_bin_JER_maker()'
    },
    'BinByBinJetMCJER' :  {
                'isChain': False,
                'do4MC': True,
                'do4Data': False,
                #'selection'  : '"Entry$<100"', #XXX 
                'import': 'LatinoAnalysis.NanoGardener.modules.BinByBinJERMaker',
                'declare': 'bin_by_bin_JER_maker = lambda : BinByBinJERMaker(jetColl="CleanJet", jer_bin_list=[0,1,2,3,4,5])',
                'module':  'bin_by_bin_JER_maker()'
    },
    'BinByBinJetMCJERChain' :  {
                'isChain': True,
                'do4MC': True,
                'do4Data': False,
                'subTargets' : ['CorrJetMC','BinByBinJetMCJER'],
    },

    'HEMweightMC' : {
                'isChain': False,
                'do4MC': True,
                'do4Data': False,
                'import': 'LatinoAnalysis.NanoGardener.modules.HEMweight',
                'declare': 'HEMweightMC = lambda : HEMweight(isData=False,dataYear=RPLME_YEAR,jetColl="CleanJet")',
                'module':  'HEMweightMC()'

    },

    'HEMweightData' : {
                'isChain': False,
                'do4MC': False,
                'do4Data': True,
                'import': 'LatinoAnalysis.NanoGardener.modules.HEMweight',
                'declare': 'HEMweightData = lambda : HEMweight(isData=True,dataYear=RPLME_YEAR,jetColl="CleanJet")',
                'module':  'HEMweightData()'

    },

    'CleanFatJet' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules
                  'declare'    : 'fatjetMaker = lambda : FatJetMaker(jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8, branch_prefix="nom")',
                  'module'     : 'fatjetMaker()'
    },

    # 'CorrFatJetMass' : {
    #               'isChain'    : False ,
    #               'do4MC'      : True  ,
    #               'do4Data'    : False  ,
    #               'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMassScaler',
    #               'declare'    : 'fatjetmass_scaler = lambda : FatJetMassScaler(year=RPLME_YEAR, type="scale_smear", kind="Central",collection="CleanFatJet")',
    #               'module'     : 'fatjetmass_scaler()'
    # },


   'susyGen': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.SusyGenVarsProducer' ,
                  'module'     : 'SusyGenVarsProducer()' ,
               },
    
    ##--High Mass SemiLeptonic channel
  'wlepMaker' : {
                  'isChain'   : False ,
                  'do4MC'     : True  ,
                  'do4Data'   : True  ,
                  'import'    : 'LatinoAnalysis.NanoGardener.modules.WlepMaker',
                  'declare'   : 'wlepMkr = lambda : WlepMaker()',
                  'module'    : 'wlepMkr()',
     },

  'wlepMaker_JESup' : {
                  'isChain'   : False ,
                  'do4MC'     : True  ,
                  'do4Data'   : True  ,
                  'import'    : 'LatinoAnalysis.NanoGardener.modules.WlepMaker',
                  'declare'   : 'wlepMkr_JESup = lambda : WlepMaker(branch_map="JESup")',
                  'module'    : 'wlepMkr_JESup()',
     },
    'whadJetSel' : {
                  'isChain'   : False ,
                  'do4MC'     : True  ,
                  'do4Data'   : True  ,
                  'import'    : 'LatinoAnalysis.NanoGardener.modules.WhadJetSel',
                  'declare'   : 'whadJetSel = lambda : WhadJetSel(2,"custom",30.0,2.4,"CleanJet")',
                  'module'    : 'WhadJetSel()',
    },

    'whadJetSel_JESup' : {
                  'isChain'   : False ,
                  'do4MC'     : True  ,
                  'do4Data'   : True  ,
                  'import'    : 'LatinoAnalysis.NanoGardener.modules.WhadJetSel',
                  'declare'   : 'whadJetSel_JESup = lambda : WhadJetSel(2,"custom",30.0,2.4,"CleanJet",branch_map="JESup")',
                  'module'    : 'WhadJetSel_JESup()',
    },

    'PreselFatJet' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  'declare'    : 'fatjetMaker = lambda : FatJetMaker(jetid=1, minpt=200, maxeta=2.4, max_tau21=9999., mass_range=[40, 13000], over_lepR=0.8, over_jetR=0.8)',
                  'module'     : 'fatjetMaker()'
    },


## ------- MODULES: Trigger

  'PrefCorr2016' : { 
                 'isChain'    : False ,
                 'do4MC'      : True ,
                 'do4Data'    : False  ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.PrefireCorr' ,
                 'declare'    : 'prefCorr2017 = lambda : PrefCorr(jetroot="L1prefiring_jetpt_2016BtoH.root", jetmapname="L1prefiring_jetpt_2016BtoH", photonroot="L1prefiring_photonpt_2016BtoH.root", photonmapname="L1prefiring_photonpt_2016BtoH", UseEMpT=0)',
                 'module'     : 'prefCorr2017()',
               },

  'PrefCorr2017' : { 
                 'isChain'    : False ,
                 'do4MC'      : True ,
                 'do4Data'    : False  ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.PrefireCorr' ,
                 'declare'    : 'prefCorr2017 = lambda : PrefCorr(jetroot="L1prefiring_jetpt_2017BtoF.root", jetmapname="L1prefiring_jetpt_2017BtoF", photonroot="L1prefiring_photonpt_2017BtoF.root", photonmapname="L1prefiring_photonpt_2017BtoF", UseEMpT=0)',
                 'module'     : 'prefCorr2017()',
               },

  'trigData' : { 'isChain'    : False ,
                 'do4MC'      : False ,
                 'do4Data'    : True  ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigData = lambda : TrigMaker("RPLME_CMSSW",isData=True,keepRunP=False)',
                 'module'     : 'trigData()',
               },

 
  'trigMC'   : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigMC = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=False)',
                 'module'     : 'trigMC()',
               },

  'trigMC_lnjj'   : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker_lnjj' ,
                 'declare'    : 'trigMC_lnjj = lambda : TrigMaker_lnjj("RPLME_CMSSW",isData=False,keepRunP=False)',
                 'module'     : 'trigMC_lnjj()',
               },

  'trigMC_Cut'   : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'CBtrigMC = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=True,cfg_path="LatinoAnalysis/NanoGardener/python/data/TrigMaker_CutBased_cfg.py")',
                 'module'     : 'CBtrigMC()',
               },

 'TrigMC_hmumu'   : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : False ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                  'declare'  : 'MHTrigMC = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=True,cfg_path="LatinoAnalysis/NanoGardener/python/data/TrigMaker_hmumu_cfg.py")',
                  'module'   : 'MHTrigMC()',
               },

  'trigMCKeepRun' : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigMCKR = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=True)',
                 'module'     : 'trigMCKR()',
               },

  # TODO: We shouldn't be instantiating almost exactly identical modules for each variation
  # Perhaps create a global "static" instance which the variations can refer to?
  'trigMCKeepRun_ElepTup' : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigMCKR_ElepTup = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=True, branch_map="ElepTup")',
                 'module'     : 'trigMCKR_ElepTup()',
               },

  'trigMCKeepRun_ElepTdo' : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigMCKR_ElepTdo = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=True, branch_map="ElepTdo")',
                 'module'     : 'trigMCKR_ElepTdo()',
               },
               
  'trigMCKeepRun_MupTup' : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigMCKR_MupTup = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=True, branch_map="MupTup")',
                 'module'     : 'trigMCKR_MupTup()',
               },

  'trigMCKeepRun_MupTdo' : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigMCKR_MupTdo = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=True, branch_map="MupTdo")',
                 'module'     : 'trigMCKR_MupTdo()',
               },

## ------- MODULES: JEC

  'JECupdateMC2017': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.jetRecalib' ,
                  'declare'    : 'jetRecalib2017MC = lambda : jetRecalib(globalTag="Fall17_17Nov2017_V32_MC", jetCollections=["CleanJet"], metCollections=["MET"])',
                  'module'     : 'jetRecalib2017MC()',
                 },    

  'JECupdateDATA2017': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.jetRecalib' ,
                  'module'     : 'jetRecalib2017RPLME_RUN()', ### <--- TODO
                 },    

## ------- MODULES: MC Weights

  'baseW'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.Grafter' ,
                  'module'     : 'Grafter(["baseW/F=RPLME_baseW","Xsec/F=RPLME_XSection"])',
               },  

  'btagPerJet2016': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer' ,
                  'declare'    : 'btagSFProducer2016 = lambda : btagSFProducer(era="Legacy2016", algo="deepcsv")',
                  'module'     : 'btagSFProducer2016()',
                 },

  'btagPerJet2017': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer' ,
                  'declare'    : 'btagSFProducer2017 = lambda : btagSFProducer(era="2017", algo="deepcsv")',
                  'module'     : 'btagSFProducer2017()',
                 },               

  'btagPerJet2018': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer' ,
                  'declare'    : 'btagSFProducer2018 = lambda : btagSFProducer(era="2018", algo="deepcsv")',
                  'module'     : 'btagSFProducer2018()',
                 },

  'btagPerEvent': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.BTagEventWeightProducer' ,
                  'declare'    : '',
                  'module'     : 'BTagEventWeightProducer()',
        
                },


  'LeptonSF' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSFMaker' ,
                  'declare'    : 'LeptonSF = lambda : LeptonSFMaker("RPLME_CMSSW")',
                  'module'     : 'LeptonSF()',
                },
  'LeptonSF_ElepTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSFMaker' ,
                  'declare'    : 'LeptonSF_ElepTup = lambda : LeptonSFMaker("RPLME_CMSSW", branch_map="ElepTup")',
                  'module'     : 'LeptonSF_ElepTup()',
                },
  'LeptonSF_ElepTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSFMaker' ,
                  'declare'    : 'LeptonSF_ElepTdo = lambda : LeptonSFMaker("RPLME_CMSSW", branch_map="ElepTdo")',
                  'module'     : 'LeptonSF_ElepTdo()',
                },
  'LeptonSF_MupTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSFMaker' ,
                  'declare'    : 'LeptonSF_MupTup = lambda : LeptonSFMaker("RPLME_CMSSW", branch_map="MupTup")',
                  'module'     : 'LeptonSF_MupTup()',
                },
  'LeptonSF_MupTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSFMaker' ,
                  'declare'    : 'LeptonSF_MupTdo = lambda : LeptonSFMaker("RPLME_CMSSW", branch_map="MupTdo")',
                  'module'     : 'LeptonSF_MupTdo()',
                },

  'JetSF': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JetSFMaker' ,
                  'declare'    : 'JetSF = lambda : JetSFMaker("RPLME_CMSSW")',
                  'module'     : 'JetSF()',
                },

## ------ Charge Flip

  'ChargeFlip' : {
                 'isChain'     : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['ChargeFlipDY','ChargeFlipWW','ChargeFlipTop'],
                  'onlySample' : ['DYJetsToLL_M-10to50-LO','DYJetsToLL_M-50','WWTo2L2Nu', 'GluGluToWWToENEN', 'GluGluToWWToENMN', 'GluGluToWWToENTN', 'GluGluToWWToMNEN', 'GluGluToWWToMNMN', 'GluGluToWWToMNTN', 'GluGluToWWToTNEN', 'GluGluToWWToTNMN', 'GluGluToWWToTNTN' , 'TTTo2L2Nu', 'ST_s-channel', 'ST_t-channel_antitop', 'ST_t-channel_top', 'ST_tW_antitop', 'ST_tW_top']
                 },

  'ChargeFlipDY' : {
                 'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.ChargeFlipWeight' ,
                  'declare'    : 'ChargeFlipDY = lambda : ChargeFlipWeight("RPLME_CMSSW","DY")',
                  'module'     : 'ChargeFlipDY()',
                  'onlySample' : ['DYJetsToLL_M-10to50-LO','DYJetsToLL_M-50'],
                 },

   'ChargeFlipWW' : {
                 'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.ChargeFlipWeight' ,
                  'declare'    : 'ChargeFlipWW = lambda : ChargeFlipWeight("RPLME_CMSSW","WW")',
                  'module'     : 'ChargeFlipWW()',
                  'onlySample' : ['WWTo2L2Nu', 'GluGluToWWToENEN', 'GluGluToWWToENMN', 'GluGluToWWToENTN', 'GluGluToWWToMNEN', 'GluGluToWWToMNMN', 'GluGluToWWToMNTN', 'GluGluToWWToTNEN', 'GluGluToWWToTNMN', 'GluGluToWWToTNTN' ]
                 },

   'ChargeFlipTop' : {
                 'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.ChargeFlipWeight' ,
                  'declare'    : 'ChargeFlipTop = lambda : ChargeFlipWeight("RPLME_CMSSW","Top")',
                  'module'     : 'ChargeFlipTop()',
                  'onlySample' : [ 'TTTo2L2Nu', 'ST_s-channel', 'ST_t-channel_antitop', 'ST_t-channel_top', 'ST_tW_antitop', 'ST_tW_top']
                    },

   'ChargeFlipClosure' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.ChargeFlipWeight' ,
                  'declare'    : 'ChargeFlipClosusre = lambda : ChargeFlipWeight("RPLME_CMSSW","DY",False)',
                  'module'     : 'ChargeFlipClosusre()',
                  'onlySample' : ['DYJetsToLL_M-10to50-LO','DYJetsToLL_M-50'],
                 },

## ------- Pile-Up weights

  'puW'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.runDependentPuW' ,
                  'declare'    : 'puWeight = lambda : runDependentPuW("RPLME_CMSSW")',
                  'module'     : 'puWeight()', 
             } , 

  'puW2016': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer' ,
                  'declare'    : 'pufile_mc2016="%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/pileup_profile_Summer16.root" % os.environ["CMSSW_BASE"]; pufile_data2016="%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/PileupData_GoldenJSON_Full2016.root" % os.environ["CMSSW_BASE"]',
                  'module'     : 'puWeightProducer(pufile_mc2016,pufile_data2016,"pu_mc","pileup",verbose=False)',

                },
              
  'puW2017': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer' ,
                  'declare'    : 'pufile_data2017="%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/pileup_Cert_294927-306462_13TeV_PromptReco_Collisions17_withVar.root" % os.environ["CMSSW_BASE"]',
                  'module'     : 'puWeightProducer("auto",pufile_data2017,"pu_mc","pileup",verbose=False)',
  },

   'susyW': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.SusyWeightsProducer' ,
                  'module'     : 'SusyWeightsProducer("RPLME_CMSSW")' ,
             },

## ------- MODULES: Embedding

  'EmbeddingWeights2018' : { 
                 'isChain'    : False ,
                 'do4MC'      : False ,
                 'do4Data'    : True  ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.EmbeddedWeights' ,
                 'declare'    : 'embed = lambda : EmbedWeights(workspacefile="htt_scalefactors_v18_1_em-channel.root")',
                 'module'     : 'embed()',
               },

  'EmbeddingWeights2017' : { 
                 'isChain'    : False ,
                 'do4MC'      : False ,
                 'do4Data'    : True  ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.EmbeddedWeights' ,
                 'declare'    : 'embed = lambda : EmbedWeights(workspacefile="htt_scalefactors_2017_v1.root")',
                 'module'     : 'embed()',
               },

  'EmbeddingWeights2016' : { 
                 'isChain'    : False ,
                 'do4MC'      : False ,
                 'do4Data'    : True  ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.EmbeddedWeights' ,
                 'declare'    : 'embed = lambda : EmbedWeights(workspacefile="htt_scalefactors_v16_12_embedded.root")',
                 'module'     : 'embed()',
               },

  'EmbeddingVeto' : { 
                 'isChain'    : False ,
                 'do4MC'      : True ,
                 'do4Data'    : False  ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.EmbeddedVeto' ,
                 'declare'    : 'embedveto = lambda : EmbedVeto()',
                 'module'     : 'embedveto()',
               },

## ------- MODULES: Fakes

  'fakeWMC' : {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'subTargets' : ['fakeWstep','formulasFAKE'],
                  'onlySample' : [ 'Zg', 'WZTo3LNu_mllmin01', 'Wg_MADGRAPHMLM', 'WZTo3LNu' ] , 
                   }, 

  'fakeWp2NB'  : {
                  'isChain'    : True ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'subTargets' : ['fakeWstep','formulasFAKE'],
                   },
  'fakeWelewithiso'  : {
                  'isChain'    : True ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'subTargets' : ['fakeWstep','formulasFAKE'],
                   },

  'fakeW_CutBasedTest'  : {
                  'isChain'    : True ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'subTargets' : ['fakeWstep','formulasFAKE'],
                   },



  'fakeW'  : {
                  'isChain'    : True ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'subTargets' : ['fakeWstep','formulasFAKE'],
                   },
    
  'fakeW1l'  : {
                'isChain'    : True ,
                'do4MC'      : False ,
                'do4Data'    : True ,
                'selection'  : '"Alt$(Lepton_pt[1],0)<=10"',
                'subTargets' : ['fakeWstep1l','formulasFAKE1l'],
                  },


  'fakeWPUFIXLP19'  : {
                  'isChain'    : True ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'subTargets' : ['fakeWstep','formulasFAKE'],
                   },


  'fakeWstep'   : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonFakeWMaker',
                  'declare'    : '',
                  'module'     : 'LeptonFakeWMaker("RPLME_CMSSW")',
              },

  'fakeWstep1l'   : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonFakeWMaker',
                  'declare'    : '',
                  'module'     : 'LeptonFakeWMaker("RPLME_CMSSW", min_nlep=1)',
              },

## ------- MODULES: Rochester corrections

  'rochesterMC'   : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.rochester_corrections',
                  'declare'    : 'rochesterMC = lambda : rochester_corr(False,RPLME_YEAR)',
                  'module'     : 'rochesterMC()',
              },

  'rochesterDATA'   : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.rochester_corrections',
                  'declare'    : 'rochesterDATA = lambda : rochester_corr(True,RPLME_YEAR)',
                  'module'     : 'rochesterDATA()',
              },

  'rochesterDATALP19'   : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.rochester_corrections',
                  'declare'    : 'rochesterDATA = lambda : rochester_corr(True,RPLME_YEAR,"Lepton",[\'MET\',\'PuppiMET\',\'RawMET\',\'TkMET\'])',
                  'module'     : 'rochesterDATA()',
              },

  'rochesterMCLP19'   : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.rochester_corrections',
                  'declare'    : 'rochesterMC = lambda : rochester_corr(False,RPLME_YEAR,"Lepton",[\'MET\',\'PuppiMET\',\'RawMET\',\'TkMET\'])',
                  'module'     : 'rochesterMC()',
              },


## ------- MODULES: Kinematic

  'l2Kin'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer()' ,
               },  

  'l2Kin_ElepTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="ElepTup")' ,
               },

  'l2Kin_ElepTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="ElepTdo")' ,
               },

  'l2Kin_MupTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="MupTup")' ,
               },

  'l2Kin_MupTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="MupTdo")' ,
               },
  'l2Kin_METup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="METup")' ,
               },

  'l2Kin_METdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="METdo")' ,
               },
  'l2Kin_JESup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="JESup")' ,
               },

  'l2Kin_JESdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer(branch_map="JESdo")' ,
               },

  'l3Kin'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer()' ,
               },
  

  'l3Kin_ElepTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="ElepTdo")' ,
               },

  'l3Kin_ElepTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="ElepTup")' ,
               },
  'l3Kin_MupTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="MupTdo")' ,
               },

  'l3Kin_MupTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="MupTup")' ,
               },
  'l3Kin_METdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="METdo")' ,
               },

  'l3Kin_METup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="METup")' ,
               },
  'l3Kin_JESdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="JESdo")' ,
               },

  'l3Kin_JESup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer(branch_map="JESup")' ,
               },
  
  'l4Kin'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer()' ,
               }, 

  'l4Kin_ElepTup'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="ElepTup")' ,
               }, 
               

  'l4Kin_ElepTdo'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="ElepTdo")' ,
               },

  'l4Kin_MupTup'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="MupTup")' ,
               }, 
               

  'l4Kin_MupTdo'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="MupTdo")' ,
               },
  'l4Kin_METup'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="METup")' ,
               }, 
               

  'l4Kin_METdo'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="METdo")' ,
               },
  'l4Kin_JESup'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="JESup")' ,
               }, 
               

  'l4Kin_JESdo'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer(branch_map="JESdo")' ,
               },
## ------- MODULES: Adding Formulas

# .... 2016/2017/... : switch in the code RPLME_YEAR

  'formulasMC' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_YEAR.py\')' ,
                 },
   

  'formulasMC_ElepTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_YEAR.py\', branch_map="ElepTup")' ,
                 },

  'formulasMC_ElepTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_YEAR.py\', branch_map="ElepTdo")' ,
                 },
  'formulasMC_MupTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_YEAR.py\', branch_map="MupTup")' ,
                 },

  'formulasMC_MupTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_YEAR.py\', branch_map="MupTdo")' ,
                 },
  'formulasMC_METup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_YEAR.py\', branch_map="METup")' ,
                 },

  'formulasMC_METdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_YEAR.py\', branch_map="METdo")' ,
                 },
  'formulasMC_JESup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_YEAR.py\', branch_map="JESup")' ,
                 },

  'formulasMC_JESdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_YEAR.py\', branch_map="JESdo")' ,
                 },


  'formulasMC_FATJESup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_YEAR.py\', branch_map="FATJESup")' ,
                 },

  'formulasMC_FATJESdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_YEAR.py\', branch_map="FATJESdo")' ,
                 },
  
  'formulasMCLP19' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_2017LP19.py\')' ,
                 },

  'formulasMCnoSF' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MCnoSF_RPLME_YEAR.py\')' ,
                 },
   
  'formulasMC16tmp' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_16tmp.py\')' ,
                 },

  'formulasMCMH' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_MonoH.py\')' ,
                 },


  'formulasDATA' : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True   ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_DATA_RPLME_YEAR.py\')' ,
                 },
  'formulasDATALP19' : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True   ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_DATA_2017LP19.py\')' ,
                 },



  'formulasFAKE' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_FAKE_RPLME_YEAR.py\')' ,
                 },

  # 'formulasFAKE1l' : {
  #                 'isChain'    : False ,
  #                 'do4MC'      : True  ,
  #                 'do4Data'    : True  ,
  #                 'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
  #                 'declare'    : '',
  #                 'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_FAKE1l_RPLME_YEAR.py\')' ,
  #                },

  'formulasEMBED' : {
                  'isChain'    : False ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_EMBED_RPLME_YEAR.py\')' ,
                 },

## -------- DYMVA

  'DYMVA' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_v5_cfg.py\')' ,
                  'module'     : 'DYMVA()',
            } ,
   
  'DYMVA_ElepTup' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_ElepTup = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_v5_cfg.py\', branch_map="ElepTup")' ,
                  'module'     : 'DYMVA_ElepTup()',
            } ,

  'DYMVA_ElepTdo' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_ElepTdo = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_v5_cfg.py\', branch_map="ElepTdo")' ,
                  'module'     : 'DYMVA_ElepTdo()',
            } ,
  'DYMVA_MupTup' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_MupTup = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_v5_cfg.py\', branch_map="MupTup")' ,
                  'module'     : 'DYMVA_MupTup()',
            } ,

  'DYMVA_MupTdo' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_MupTdo = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_v5_cfg.py\', branch_map="MupTdo")' ,
                  'module'     : 'DYMVA_MupTdo()',
            } ,
  'DYMVA_METup' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_METup = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_v5_cfg.py\', branch_map="METup")' ,
                  'module'     : 'DYMVA_METup()',
            } ,

  'DYMVA_METdo' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_METdo = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_v5_cfg.py\', branch_map="METdo")' ,
                  'module'     : 'DYMVA_METdo()',
            } ,
  'DYMVA_JESup' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_JESup = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_v5_cfg.py\', branch_map="JESup")' ,
                  'module'     : 'DYMVA_JESup()',
            } ,

  'DYMVA_JESdo' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA_JESdo = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_v5_cfg.py\', branch_map="JESdo")' ,
                  'module'     : 'DYMVA_JESdo()',
            } ,

# 'DYMVA_v5' : {
#           #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
#                 'isChain'    : False ,
#                 'do4MC'      : True  ,
#                 'do4Data'    : True  ,
#                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
#                 'declare'    : 'DYMVA = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_v5_cfg.py\')' ,
#                 'module'     : 'DYMVA()',
#           } ,


# ------------------------------------ SYSTEMATICS ----------------------------------------------------------------

## ------- JES

  'JESBaseTestV8' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JECMaker' ,
                  'declare'    : 'JES = lambda : JECMaker(globalTag="Fall17_17Nov2017_V8_MC", types=["Total"], jetFlav="AK4PFchs")',
                  'module'     : 'JES()',
                  'onlySample' : [ 'WWTo2L2Nu' ] ,
               },

  'JESBase' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JECMaker' ,
                  'declare'    : 'JES = lambda : JECMaker(globalTag="Regrouped_RPLME_JESGT", types=["Total", "Absolute", "Absolute_RPLME_YEAR", "BBEC1", "BBEC1_RPLME_YEAR", "EC2", "EC2_RPLME_YEAR", "FlavorQCD", "HF", "HF_RPLME_YEAR", "RelativeBal", "RelativeSample_RPLME_YEAR"], jetFlav="AK4PFchs")',
                  'module'     : 'JES()',
               },

  'JESBaseTotal' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JECMaker' ,
                  'declare'    : 'JES = lambda : JECMaker(globalTag="RPLME_JESGT", types=["Total"], jetFlav="AK4PFchs")',
                  'module'     : 'JES()',
               },



  'FATJESBaseTotal' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JECMaker' ,
                  'declare'    : 'FATJES = lambda : JECMaker(globalTag="RPLME_JESGT", types=["Total"], jetFlav="AK8PFPuppi",jetCo="CleanFatJet")',
                  'module'     : 'FATJES()',
               },



  'do_JESup' : {  
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.PtCorrApplier', 
                  'declare'    : 'JESUp = lambda : PtCorrApplier(Coll="CleanJet", CorrSrc="jecUncertTotal", kind="Up", doMET=True, METobjects = ["MET","PuppiMET","RawMET"])', 
                  'module'     : 'JESUp()' 
               },

  'do_JESdo' : {  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.PtCorrApplier', 
                  'declare'    : 'JESDo = lambda : PtCorrApplier(Coll="CleanJet", CorrSrc="jecUncertTotal", kind="Do", doMET=True, METobjects = ["MET","PuppiMET","RawMET"])', 
                  'module'     : 'JESDo()' 
               },
  'do_JESup_suffix' : createJESvariation("Total", "Up"),
  'do_FATJESup_suffix' : createFATJESvariation("Total", "Up"),
#{  
#                  'isChain'    : False ,
#                  'do4MC'      : True  ,
#                  'do4Data'    : False  ,
#                  'import'     : 'LatinoAnalysis.NanoGardener.modules.PtCorrApplier', 
#                  'declare'    : 'JESUp = lambda : PtCorrApplier(Coll="CleanJet", CorrSrc="jecUncertTotal", kind="Up", doMET=True, METobjects = ["MET","PuppiMET","RawMET"], suffix="_JESup")', 
#                  'module'     : 'JESUp()' 
#               },

  'do_JESdo_suffix' : createJESvariation("Total", "Do"),
  'do_FATJESdo_suffix' : createFATJESvariation("Total", "Do"),
#{  'isChain'    : False ,
#                  'do4MC'      : True  ,
#                  'do4Data'    : False  ,
#                  'import'     : 'LatinoAnalysis.NanoGardener.modules.PtCorrApplier', 
#                  'declare'    : 'JESDo = lambda : PtCorrApplier(Coll="CleanJet", CorrSrc="jecUncertTotal", kind="Do", doMET=True, METobjects = ["MET","PuppiMET","RawMET"], suffix="_JESdo")', 
#                  'module'     : 'JESDo()' 
#               },
    
   'do_JESAbsoluteup_suffix' : createJESvariation("Absolute", "Up"), 
   'do_JESAbsolutedo_suffix' : createJESvariation("Absolute", "Do"), 
   'do_JESAbsolute_RPLME_YEARup_suffix' : createJESvariation("Absolute_RPLME_YEAR", "Up"), 
   'do_JESAbsolute_RPLME_YEARdo_suffix' : createJESvariation("Absolute_RPLME_YEAR", "Do"), 
   'do_JESBBEC1up_suffix' : createJESvariation("BBEC1", "Up"), 
   'do_JESBBEC1do_suffix' : createJESvariation("BBEC1", "Do"), 
   'do_JESBBEC1_RPLME_YEARup_suffix' : createJESvariation("BBEC1_RPLME_YEAR", "Up"), 
   'do_JESBBEC1_RPLME_YEARdo_suffix' : createJESvariation("BBEC1_RPLME_YEAR", "Do"), 
   'do_JESEC2up_suffix' : createJESvariation("EC2", "Up"), 
   'do_JESEC2do_suffix' : createJESvariation("EC2", "Do"), 
   'do_JESEC2_RPLME_YEARup_suffix' : createJESvariation("EC2_RPLME_YEAR", "Up"), 
   'do_JESEC2_RPLME_YEARdo_suffix' : createJESvariation("EC2_RPLME_YEAR", "Do"), 
   'do_JESFlavorQCDup_suffix' : createJESvariation("FlavorQCD", "Up"), 
   'do_JESFlavorQCDdo_suffix' : createJESvariation("FlavorQCD", "Do"), 
   'do_JESHFup_suffix' : createJESvariation("HF", "Up"), 
   'do_JESHFdo_suffix' : createJESvariation("HF", "Do"), 
   'do_JESHF_RPLME_YEARup_suffix' : createJESvariation("HF_RPLME_YEAR", "Up"), 
   'do_JESHF_RPLME_YEARdo_suffix' : createJESvariation("HF_RPLME_YEAR", "Do"), 
   'do_JESRelativeBalup_suffix' : createJESvariation("RelativeBal", "Up"), 
   'do_JESRelativeBaldo_suffix' : createJESvariation("RelativeBal", "Do"), 
   'do_JESRelativeSample_RPLME_YEARup_suffix' : createJESvariation("RelativeSample_RPLME_YEAR", "Up"), 
   'do_JESRelativeSample_RPLME_YEARdo_suffix' : createJESvariation("RelativeSample_RPLME_YEAR", "Do"), 





   # What about B-Tag weights ? They are done on top of the Jet Collection, not the CleanJet, so they don't catch th jet pT update !!!!

   'JESup' :   {  
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase','do_JESup','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasMC'],
               },


  'FATJESup_suffix_total' :{
    'isChain'    : True ,
    'do4MC'      : True  ,
    'do4Data'    : False  ,
    'subTargets' : ['FATJESBaseTotal']+
    createFATJESchain("Total","Up"),
    'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'

  } 
  ,

   'JESup_suffix_total' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBaseTotal'] +
                                  createJESchain("Total", "Up"),
                                  #createJESchain("Absolute", "Up") +
                                  #createJESchain("Absolute_RPLME_YEAR", "Up") +
                                  #createJESchain("BBEC1", "Up") +
                                  #createJESchain("BBEC1_RPLME_YEAR", "Up") +
                                  #createJESchain("EC2", "Up") +
                                  #createJESchain("EC2_RPLME_YEAR", "Up") +
                                  #createJESchain("FlavorQCD", "Up") +
                                  #createJESchain("HF", "Up") +
                                  #createJESchain("HF_RPLME_YEAR", "Up") +
                                  #createJESchain("RelativeBal", "Up") +
                                  #createJESchain("RelativeSample_RPLME_YEAR", "Up"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
                  #'subTargets' : ['JESBase','do_JESup_suffix','l2Kin_JESup', 'l3Kin_JESup', 'l4Kin_JESup','DYMVA_JESup','MonoHiggsMVA_JESup','formulasMC_JESup',
                  #               'do_JESAbsoluteup_suffix','do_JESAbsolutedo_suffix','do_JESAbsolute_RPLME_YEARup_suffix','do_JESAbsolute_RPLME_YEARdo_suffix','do_JESBBEC1up_suffix','do_JESBBEC1do_suffix','do_JESBBEC1_RPLME_YEARup_suffix','do_JESBBEC1_RPLME_YEARdo_suffix','do_JESEC2up_suffix','do_JESEC2do_suffix','do_JESEC2_RPLME_YEARup_suffix','do_JESEC2_RPLME_YEARdo_suffix','do_JESFlavorQCDup_suffix','do_JESFlavorQCDdo_suffix','do_JESHFup_suffix','do_JESHFdo_suffix','do_JESHF_RPLME_YEARup_suffix','do_JESHF_RPLME_YEARup_suffix','do_JESRelativeBaldo_suffix','do_JESRelativeBaldo_suffix','do_JESRelativeBal_RPLME_YEARup_suffix','do_JESRelativeBal_RPLME_YEARdo_suffix'],
               },


   'JESup_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] +
                                  createJESchain("Total", "Up") +
                                  createJESchain("Absolute", "Up") +
                                  createJESchain("Absolute_RPLME_YEAR", "Up") +
                                  createJESchain("BBEC1", "Up") +
                                  createJESchain("BBEC1_RPLME_YEAR", "Up") +
                                  createJESchain("EC2", "Up") +
                                  createJESchain("EC2_RPLME_YEAR", "Up") +
                                  createJESchain("FlavorQCD", "Up") +
                                  createJESchain("HF", "Up") +
                                  createJESchain("HF_RPLME_YEAR", "Up") +
                                  createJESchain("RelativeBal", "Up") +
                                  createJESchain("RelativeSample_RPLME_YEAR", "Up"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
                  #'subTargets' : ['JESBase','do_JESup_suffix','l2Kin_JESup', 'l3Kin_JESup', 'l4Kin_JESup','DYMVA_JESup','MonoHiggsMVA_JESup','formulasMC_JESup',
                  #               'do_JESAbsoluteup_suffix','do_JESAbsolutedo_suffix','do_JESAbsolute_RPLME_YEARup_suffix','do_JESAbsolute_RPLME_YEARdo_suffix','do_JESBBEC1up_suffix','do_JESBBEC1do_suffix','do_JESBBEC1_RPLME_YEARup_suffix','do_JESBBEC1_RPLME_YEARdo_suffix','do_JESEC2up_suffix','do_JESEC2do_suffix','do_JESEC2_RPLME_YEARup_suffix','do_JESEC2_RPLME_YEARdo_suffix','do_JESFlavorQCDup_suffix','do_JESFlavorQCDdo_suffix','do_JESHFup_suffix','do_JESHFdo_suffix','do_JESHF_RPLME_YEARup_suffix','do_JESHF_RPLME_YEARup_suffix','do_JESRelativeBaldo_suffix','do_JESRelativeBaldo_suffix','do_JESRelativeBal_RPLME_YEARup_suffix','do_JESRelativeBal_RPLME_YEARdo_suffix'],
               },

   'JESup_suffix_redoMVA' :   {  
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] + 
                                  createJESchain("Total", "Up") +
                                  createJESchain("Absolute", "Up") +
                                  createJESchain("Absolute_RPLME_YEAR", "Up") +
                                  createJESchain("BBEC1", "Up") +
                                  createJESchain("BBEC1_RPLME_YEAR", "Up") +
                                  createJESchain("EC2", "Up") +
                                  createJESchain("EC2_RPLME_YEAR", "Up") +
                                  createJESchain("FlavorQCD", "Up") +
                                  createJESchain("HF", "Up") +
                                  createJESchain("HF_RPLME_YEAR", "Up") +
                                  createJESchain("RelativeBal", "Up") +
                                  createJESchain("RelativeSample_RPLME_YEAR", "Up"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'                
                  #'subTargets' : ['JESBase','do_JESup_suffix','l2Kin_JESup', 'l3Kin_JESup', 'l4Kin_JESup','DYMVA_JESup','MonoHiggsMVA_JESup','formulasMC_JESup',
                  #               'do_JESAbsoluteup_suffix','do_JESAbsolutedo_suffix','do_JESAbsolute_RPLME_YEARup_suffix','do_JESAbsolute_RPLME_YEARdo_suffix','do_JESBBEC1up_suffix','do_JESBBEC1do_suffix','do_JESBBEC1_RPLME_YEARup_suffix','do_JESBBEC1_RPLME_YEARdo_suffix','do_JESEC2up_suffix','do_JESEC2do_suffix','do_JESEC2_RPLME_YEARup_suffix','do_JESEC2_RPLME_YEARdo_suffix','do_JESFlavorQCDup_suffix','do_JESFlavorQCDdo_suffix','do_JESHFup_suffix','do_JESHFdo_suffix','do_JESHF_RPLME_YEARup_suffix','do_JESHF_RPLME_YEARup_suffix','do_JESRelativeBaldo_suffix','do_JESRelativeBaldo_suffix','do_JESRelativeBal_RPLME_YEARup_suffix','do_JESRelativeBal_RPLME_YEARdo_suffix'],
               },

   'JESdo' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase','do_JESdo','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasMC'],
               },



  

   'JESdo_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] +
                                  createJESchain("Total", "Do") +
                                  createJESchain("Absolute", "Do") +
                                  createJESchain("Absolute_RPLME_YEAR", "Do") +
                                  createJESchain("BBEC1", "Do") +
                                  createJESchain("BBEC1_RPLME_YEAR", "Do") +
                                  createJESchain("EC2", "Do") +
                                  createJESchain("EC2_RPLME_YEAR", "Do") +
                                  createJESchain("FlavorQCD", "Do") +
                                  createJESchain("HF", "Do") +
                                  createJESchain("HF_RPLME_YEAR", "Do") +
                                  createJESchain("RelativeBal", "Do") +
                                  createJESchain("RelativeSample_RPLME_YEAR", "Do"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
                  #'subTargets' : ['JESBase','do_JESdo_suffix','l2Kin_JESdo', 'l3Kin_JESdo', 'l4Kin_JESdo','DYMVA_JESdo','MonoHiggsMVA_JESdo','formulasMC_JESdo'],
               },

   'FATJESdo_suffix_total' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['FATJESBaseTotal'] +
                                  createFATJESchain("Total", "Do"),
                                  
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
                  #'subTargets' : ['JESBase','do_JESdo_suffix','l2Kin_JESdo', 'l3Kin_JESdo', 'l4Kin_JESdo','DYMVA_JESdo','MonoHiggsMVA_JESdo','formulasMC_JESdo'],
               },

   'JESdo_suffix_total' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBaseTotal'] +
                                  createJESchain("Total", "Do"),
                                  #createJESchain("Absolute", "Do") +
                                  #createJESchain("Absolute_RPLME_YEAR", "Do") +
                                  #createJESchain("BBEC1", "Do") +
                                  #createJESchain("BBEC1_RPLME_YEAR", "Do") +
                                  #createJESchain("EC2", "Do") +
                                  #createJESchain("EC2_RPLME_YEAR", "Do") +
                                  #createJESchain("FlavorQCD", "Do") +
                                  #createJESchain("HF", "Do") +
                                  #createJESchain("HF_RPLME_YEAR", "Do") +
                                  #createJESchain("RelativeBal", "Do") +
                                  #createJESchain("RelativeSample_RPLME_YEAR", "Do"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
                  #'subTargets' : ['JESBase','do_JESdo_suffix','l2Kin_JESdo', 'l3Kin_JESdo', 'l4Kin_JESdo','DYMVA_JESdo','MonoHiggsMVA_JESdo','formulasMC_JESdo'],
               },


   'JESdo_suffix_redoMVA' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase'] +
                                  createJESchain("Total", "Do") +
                                  createJESchain("Absolute", "Do") +
                                  createJESchain("Absolute_RPLME_YEAR", "Do") +
                                  createJESchain("BBEC1", "Do") +
                                  createJESchain("BBEC1_RPLME_YEAR", "Do") +
                                  createJESchain("EC2", "Do") +
                                  createJESchain("EC2_RPLME_YEAR", "Do") +
                                  createJESchain("FlavorQCD", "Do") +
                                  createJESchain("HF", "Do") +
                                  createJESchain("HF_RPLME_YEAR", "Do") +
                                  createJESchain("RelativeBal", "Do") +
                                  createJESchain("RelativeSample_RPLME_YEAR", "Do"),
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'                
                  #'subTargets' : ['JESBase','do_JESdo_suffix','l2Kin_JESdo', 'l3Kin_JESdo', 'l4Kin_JESdo','DYMVA_JESdo','MonoHiggsMVA_JESdo','formulasMC_JESdo'],
               },


   'JESupLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase','do_JESup','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },

   'JESdoLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase','do_JESdo','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },


## ------- MET

  'do_METup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.MetUnclustered',
                  'declare'    : 'METup = lambda : MetUnclusteredTreeMaker(kind="Up",metCollections=["MET", "PuppiMET", "RawMET"])',
                  'module'     : 'METup()',
                },

  'do_METdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.MetUnclustered',
                  'declare'    : 'METDo = lambda : MetUnclusteredTreeMaker(kind="Dn",metCollections=["MET", "PuppiMET", "RawMET"])',
                  'module'     : 'METDo()',
                },
  'do_METup_suffix' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.MetUnclustered',
                  'declare'    : 'METup = lambda : MetUnclusteredTreeMaker(kind="Up",metCollections=["MET", "PuppiMET", "RawMET"], suffix="_METup")',
                  'module'     : 'METup()',
                },

  'do_METdo_suffix' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.MetUnclustered',
                  'declare'    : 'METDo = lambda : MetUnclusteredTreeMaker(kind="Dn",metCollections=["MET", "PuppiMET", "RawMET"], suffix="_METdo")',
                  'module'     : 'METDo()',
                },

   'METup' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_METup','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasMC'],
               },

   'METup_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  #'subTargets' : ['do_METup_suffix','l2Kin_METup', 'l3Kin_METup', 'l4Kin_METup','DYMVA_METup','MonoHiggsMVA_METup','formulasMC_METup'],
     'subTargets' : ['do_METup_suffix','formulasMC_METup'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },


   'METup_suffix_redoMVA' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_METup_suffix','l2Kin_METup', 'l3Kin_METup', 'l4Kin_METup','DYMVA_METup','MonoHiggsMVA_METup','formulasMC_METup'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

   'METdo' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_METdo','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasMC'],
               },

   'METdo_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  #'subTargets' : ['do_METdo_suffix','l2Kin_METdo', 'l3Kin_METdo', 'l4Kin_METdo','DYMVA_METdo','MonoHiggsMVA_METdo','formulasMC_METdo'],
     'subTargets' : ['do_METdo_suffix','formulasMC_METdo'],
     'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

   'METdo_suffix_redoMVA' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_METdo_suffix','l2Kin_METdo', 'l3Kin_METdo', 'l4Kin_METdo','DYMVA_METdo','MonoHiggsMVA_METdo','formulasMC_METdo'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

   'METupLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_METup','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },

   'METdoLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_METdo','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },

## ------- e-Scale

  'do_ElepTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'ElepTup = lambda : LeppTScalerTreeMaker(kind="Up", lepFlavor="ele", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"])',
                  'module'     : 'ElepTup()',
                },

  'do_ElepTup_suffix': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'ElepTup = lambda : LeppTScalerTreeMaker(kind="Up", lepFlavor="ele", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"], suffix="_ElepTup")',
                  'module'     : 'ElepTup()',
                },

  'do_ElepTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'ElepTdo = lambda : LeppTScalerTreeMaker(kind="Dn", lepFlavor="ele", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"])',
                  'module'     : 'ElepTdo()',
                },

  'do_ElepTdo_suffix' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'ElepTdo = lambda : LeppTScalerTreeMaker(kind="Dn", lepFlavor="ele", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"], suffix="_ElepTdo")',
                  'module'     : 'ElepTdo()',
                },

  'ElepTup' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_ElepTup','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasMC'],
               },

  'ElepTup_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  #'subTargets' : ['do_ElepTup_suffix', 'trigMCKeepRun_ElepTup', 'LeptonSF_ElepTup', 'l2Kin_ElepTup', 'l3Kin_ElepTup', 'l4Kin_ElepTup', 'DYMVA_ElepTup', 'MonoHiggsMVA_ElepTup', 'formulasMC_ElepTup'],
    'subTargets' : ['do_ElepTup_suffix', 'trigMCKeepRun_ElepTup', 'LeptonSF_ElepTup', 'formulasMC_ElepTup'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

  'ElepTup_suffix_redoMVA' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_ElepTup_suffix', 'trigMCKeepRun_ElepTup', 'LeptonSF_ElepTup', 'l2Kin_ElepTup', 'l3Kin_ElepTup', 'l4Kin_ElepTup', 'DYMVA_ElepTup', 'MonoHiggsMVA_ElepTup', 'formulasMC_ElepTup'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

  'ElepTdo' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_ElepTdo','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasMC'],
                },
 
  'ElepTdo_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  #'subTargets' : ['do_ElepTdo_suffix', 'trigMCKeepRun_ElepTdo', 'LeptonSF_ElepTdo', 'l2Kin_ElepTdo', 'l3Kin_ElepTdo', 'l4Kin_ElepTdo', 'DYMVA_ElepTdo', 'MonoHiggsMVA_ElepTdo', 'formulasMC_ElepTdo'],
    'subTargets' : ['do_ElepTdo_suffix', 'trigMCKeepRun_ElepTdo', 'LeptonSF_ElepTdo', 'formulasMC_ElepTdo'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },
 
  'ElepTdo_suffix_redoMVA' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_ElepTdo_suffix', 'trigMCKeepRun_ElepTdo', 'LeptonSF_ElepTdo', 'l2Kin_ElepTdo', 'l3Kin_ElepTdo', 'l4Kin_ElepTdo', 'DYMVA_ElepTdo', 'MonoHiggsMVA_ElepTdo', 'formulasMC_ElepTdo'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

  'ElepTupLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_ElepTup_ElepTdo','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },

  'ElepTdoLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_ElepTdo','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },

  'EmbElepTup' :   {
                  'isChain'    : True ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['do_ElepTup','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasEMBED'],
               },

  'EmbElepTdo' :   {
                  'isChain'    : True ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['do_ElepTdo','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasEMBED'],
               },

## ------- mu-Scale

  'do_MupTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'MupTup = lambda : LeppTScalerTreeMaker(kind="Up", lepFlavor="mu", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"])',
                  'module'     : 'MupTup()',
                },

                
  'do_MupTup_suffix' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'MupTup = lambda : LeppTScalerTreeMaker(kind="Up", lepFlavor="mu", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"], suffix="_MupTup")',
                  'module'     : 'MupTup()',
                },

  'do_MupTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'MupTup = lambda : LeppTScalerTreeMaker(kind="Dn", lepFlavor="mu", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"])',
                  'module'     : 'MupTup()',
                },

  'do_MupTdo_suffix' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'MupTdo = lambda : LeppTScalerTreeMaker(kind="Dn", lepFlavor="mu", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"], suffix="_MupTdo")',
                  'module'     : 'MupTdo()',
                },
  
  'MupTup' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_MupTup','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasMC'],
               },

  'MupTup_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  #'subTargets' : ['do_MupTup_suffix', 'trigMCKeepRun_MupTup', 'LeptonSF_MupTup', 'l2Kin_MupTup', 'l3Kin_MupTup', 'l4Kin_MupTup', 'DYMVA_MupTup', 'MonoHiggsMVA_MupTup', 'formulasMC_MupTup'],
    #'subTargets' : ['do_MupTup_suffix', 'trigMCKeepRun_MupTup', 'LeptonSF_MupTup', 'l2Kin_MupTup', 'l3Kin_MupTup', 'l4Kin_MupTup', 'formulasMC_MupTup'],
    'subTargets' : ['do_MupTup_suffix', 'trigMCKeepRun_MupTup', 'LeptonSF_MupTup', 'formulasMC_MupTup'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

  'MupTup_suffix_redoMVA' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_MupTup_suffix', 'trigMCKeepRun_MupTup', 'LeptonSF_MupTup', 'l2Kin_MupTup', 'l3Kin_MupTup', 'l4Kin_MupTup', 'DYMVA_MupTup', 'MonoHiggsMVA_MupTup', 'formulasMC_MupTup'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

  'MupTdo' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_MupTdo','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasMC'],
               },

  'MupTdo_suffix' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  #'subTargets' : ['do_MupTdo_suffix', 'trigMCKeepRun_MupTdo', 'LeptonSF_MupTdo', 'l2Kin_MupTdo', 'l3Kin_MupTdo', 'l4Kin_MupTdo', 'DYMVA_MupTdo', 'MonoHiggsMVA_MupTdo', 'formulasMC_MupTdo'],
    'subTargets' : ['do_MupTdo_suffix', 'trigMCKeepRun_MupTdo', 'LeptonSF_MupTdo', 'formulasMC_MupTdo'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },

  'MupTdo_suffix_redoMVA' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_MupTdo_suffix', 'trigMCKeepRun_MupTdo', 'LeptonSF_MupTdo', 'l2Kin_MupTdo', 'l3Kin_MupTdo', 'l4Kin_MupTdo', 'DYMVA_MupTdo', 'MonoHiggsMVA_MupTdo', 'formulasMC_MupTdo'],
                  'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
               },
  
  'MupTupLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_MupTup','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },

  'MupTdoLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_MupTdo','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },


  'EmbMupTup' :   {
                  'isChain'    : True ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['do_MupTup','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasEMBED'],
               },

  'EmbMupTdo' :   {
                  'isChain'    : True ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['do_MupTdo','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','DYMVA','MonoHiggsMVA','formulasEMBED'],
               },

#-------------------------  Fatjet mass scale

    'CleanFatJet_JESup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules
                  'declare'    : 'fatjetMaker_jesup = lambda : FatJetMaker( branch_prefix="jesTotalUp", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
                  'module'     : 'fatjetMaker_jesup()'
    },

     'CleanFatJet_JESdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules
                  'declare'    : 'fatjetMaker_jesdo = lambda : FatJetMaker( branch_prefix="jesTotalDown", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
                  'module'     : 'fatjetMaker_jesdo()'
    },

'CleanFatJet_JERup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules
                  'declare'    : 'fatjetMaker_jesup = lambda : FatJetMaker( branch_prefix="jerUp", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
                  'module'     : 'fatjetMaker_jerup()'
    },

     'CleanFatJet_JERdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules
                  'declare'    : 'fatjetMaker_jesdo = lambda : FatJetMaker( branch_prefix="jesTotalDown", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
                  'module'     : 'fatjetMaker_jerdo()'
    },

    'CleanFatJet_JMSup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules
                  'declare'    : 'fatjetMaker_jmsup = lambda : FatJetMaker( branch_prefix="jmsUp", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
                  'module'     : 'fatjetMaker_jmsup()'
    },

     'CleanFatJet_JMSdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules
                  'declare'    : 'fatjetMaker_jmsdo = lambda : FatJetMaker( branch_prefix="jerDown", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
                  'module'     : 'fatjetMaker_jmsdo()'
    },

    'CleanFatJet_JMRup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules
                  'declare'    : 'fatjetMaker_jmrup = lambda : FatJetMaker( branch_prefix="jmrUp", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
                  'module'     : 'fatjetMaker_jmrup()'
    },

     'CleanFatJet_JMRdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.FatJetMaker',
                  # The branch prefix needs to be used if the CleanFatJet module is run on top of CorrFatJet* modules
                  'declare'    : 'fatjetMaker_jmrdo = lambda : FatJetMaker( branch_prefix="jmrDown", jetid=0, minpt=200, maxeta=2.4, max_tau21=0.45, mass_range=[40, 250], over_lepR=0.8, over_jetR=0.8)',
                  'module'     : 'fatjetMaker_jmrdo()'
    },
  


    # chain of chains
    'systematics': {
        'isChain': True,
        'do4MC': True,
        'do4Data': False,
        'subTargets': ['JESup_suffix', 'JESdo_suffix', 'METup_suffix', 'METdo_suffix', 'ElepTup_suffix', 'ElepTdo_suffix', 'MupTup_suffix', 'MupTdo_suffix'],
        'outputbranchsel': os.getenv('CMSSW_BASE') + '/src/LatinoAnalysis/NanoGardener/python/data/keepsysts.txt'
    },

# ------------------------------------ SKIMS : CUTS ONLY ----------------------------------------------------------

  'TrgwSel'   : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'selection'  : '"((TriggerEffWeight_2l_u/TriggerEffWeight_2l)>10)"' ,
                  #'onlySample' : [ 'WWTo2L2Nu' ] ,
                 },

  'wwSel'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '"(mll>12 && ptll>30 && (MET_pt > 20 || PuppiMET_pt>20) && Alt$(Lepton_pt[0],0.)>20 && Alt$(Lepton_pt[1],0.)>10 && Alt$(Lepton_pt[2],0.)<10 && Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*13)"',
                  #'onlySample' : [ 'WWTo2L2Nu' ] ,
                 },

## ------- Fake Study:

  'fakeSel'    : {
                  'isChain'    : False ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'selection'  : '"((MET_pt < 20 || PuppiMET_pt < 20) && mtw1 < 20)"' ,
                 },


  'fakeSelKinMC'  : {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  , 
                  'selection'  : '"(MET_pt < 20 || PuppiMET_pt < 20)"' , 
                  'onlySample' : [
                                  #### DY
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3','DYJetsToLL_M-50-LO','DYJetsToLL_M-50-LO-ext1','DYJetsToLL_M-10to50-LO',
                                  'DYJetsToTT_MuEle_M-50','DYJetsToLL_M-50_ext2','DYJetsToLL_M-10to50-LO-ext1',
                                   # ... Low Mass HT
                                  'DYJetsToLL_M-4to50_HT-100to200',
                                  'DYJetsToLL_M-4to50_HT-100to200-ext1',
                                  'DYJetsToLL_M-4to50_HT-200to400',
                                  'DYJetsToLL_M-4to50_HT-200to400-ext1',
                                  'DYJetsToLL_M-4to50_HT-400to600',
                                  'DYJetsToLL_M-4to50_HT-400to600-ext1',
                                  'DYJetsToLL_M-4to50_HT-600toInf',
                                  'DYJetsToLL_M-4to50_HT-600toInf-ext1',
                                   # ... high Mass HT
                                  'DYJetsToLL_M-50_HT-100to200',
                                  'DYJetsToLL_M-50_HT-200to400',
                                  'DYJetsToLL_M-50_HT-400to600',
                                  'DYJetsToLL_M-50_HT-600to800',
                                  'DYJetsToLL_M-50_HT-800to1200',
                                  'DYJetsToLL_M-50_HT-1200to2500',
                                  'DYJetsToLL_M-50_HT-2500toInf',
 
                                  ####
                                  'WJetsToLNu-LO',
                                  'WJetsToLNu','WJetsToLNu_HT100_200','WJetsToLNu_HT200_400','WJetsToLNu_HT400_600','WJetsToLNu_HT600_800',
                                  'WJetsToLNu_HT800_1200','WJetsToLNu_HT1200_2500','WJetsToLNu_HT2500_inf',
                                  ####
                                  'QCD_Pt-15to20_EMEnriched', 'QCD_Pt-20to30_EMEnriched', 'QCD_Pt-30to50_EMEnriched', 'QCD_Pt-50to80_EMEnriched','QCD_Pt-50to80_EMEnriched_ext1',
                                  'QCD_Pt-20toInf_MuEnrichedPt15','QCD_Pt-30toInf_DoubleEMEnriched','QCD_Pt-15to20_MuEnrichedPt5',
                                  ####
                                  'QCD_Pt_15to20_bcToE','QCD_Pt_20to30_bcToE','QCD_Pt_30to80_bcToE','QCD_Pt_80to170_bcToE',
                                  'QCD_Pt_170to250_bcToE','QCD_Pt_250toInf_bcToE',
                                  ####
                                  'TT','TTJets','TTTo2L2Nu',
                                 ] ,               
                    'subTargets' : ['baseW','rochesterMC','trigMC','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMCnoSF'] ,
                 },



  'fakeSelMC'  : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  , 
                  'selection'  : '"((MET_pt < 20 || PuppiMET_pt < 20) && mtw1 < 20)"' , 
                  'onlySample' : [
                                  #### DY
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3','DYJetsToLL_M-50-LO','DYJetsToLL_M-50-LO-ext1','DYJetsToLL_M-10to50-LO',
                                  'DYJetsToTT_MuEle_M-50','DYJetsToLL_M-50_ext2','DYJetsToLL_M-10to50-LO-ext1',
                                   # ... Low Mass HT
                                  'DYJetsToLL_M-4to50_HT-100to200',
                                  'DYJetsToLL_M-4to50_HT-100to200-ext1',
                                  'DYJetsToLL_M-4to50_HT-200to400',
                                  'DYJetsToLL_M-4to50_HT-200to400-ext1',
                                  'DYJetsToLL_M-4to50_HT-400to600',
                                  'DYJetsToLL_M-4to50_HT-400to600-ext1',
                                  'DYJetsToLL_M-4to50_HT-600toInf',
                                  'DYJetsToLL_M-4to50_HT-600toInf-ext1',
                                   # ... high Mass HT
                                  'DYJetsToLL_M-50_HT-100to200',
                                  'DYJetsToLL_M-50_HT-200to400',
                                  'DYJetsToLL_M-50_HT-400to600',
                                  'DYJetsToLL_M-50_HT-600to800',
                                  'DYJetsToLL_M-50_HT-800to1200',
                                  'DYJetsToLL_M-50_HT-1200to2500',
                                  'DYJetsToLL_M-50_HT-2500toInf',
 
                                  ####
                                  'WJetsToLNu','WJetsToLNu_HT100_200','WJetsToLNu_HT200_400','WJetsToLNu_HT400_600','WJetsToLNu_HT600_800',
                                  'WJetsToLNu_HT800_1200','WJetsToLNu_HT1200_2500','WJetsToLNu_HT2500_inf',
                                  ####
                                  'QCD_Pt-15to20_EMEnriched', 'QCD_Pt-20to30_EMEnriched', 'QCD_Pt-30to50_EMEnriched', 'QCD_Pt-50to80_EMEnriched','QCD_Pt-50to80_EMEnriched_ext1',
                                  'QCD_Pt-20toInf_MuEnrichedPt15','QCD_Pt-30toInf_DoubleEMEnriched','QCD_Pt-15to20_MuEnrichedPt5',
                                  ####
                                  'QCD_Pt_15to20_bcToE','QCD_Pt_20to30_bcToE','QCD_Pt_30to80_bcToE','QCD_Pt_80to170_bcToE',
                                  'QCD_Pt_170to250_bcToE','QCD_Pt_250toInf_bcToE',
                                  ####
                                  'GJetsDR04_HT100To200', 'GJetsDR04_HT200To400', 'GJetsDR04_HT400To600', 'GJetsDR04_HT600ToInf', 'GJets_HT40To100', 'GJets_HT40To100-ext1',
                                  ####
                                  'TT','TTJets','TTTo2L2Nu',
                                  ###
                                  'GJetsDR04_HT40To100', 'GJetsDR04_HT100To200', 'GJetsDR04_HT200To400', 'GJetsDR04_HT400To600', 'GJetsDR04_HT600ToInf',
                                  'GJets_HT40To100-ext1',
                                 ] ,               
                 },

## ------- 2-Leptons: Loose / tightOR

#  'l2loose'   : {
#                  'isChain'    : False ,
#                  'do4MC'      : True  ,
#                  'do4Data'    : True  , 
#                  'selection'  : '"(nLepton>=2)"' , 
#                 },

# Run MVA after 2 lepton selection !
   'l2loose' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '"(nLepton>=2)"' ,
                  'subTargets' : ['DYMVA','MonoHiggsMVA','l3Kin'], 
                  'excludeSample' : LNuQQSamples
                },
 

#muWP='cut_Tight80x'
#eleWPlist = ['cut_WP_Tight80X','cut_WP_Tight80X_SS','mva_90p_Iso2016','mva_90p_Iso2016_SS']
  'l2tightOR2016' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_cut_WP_Tight80X[0] > 0.5        \
                                         || Lepton_isTightElectron_cut_WP_Tight80X_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016[0] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_cut_WP_Tight80X[1] > 0.5        \
                                         || Lepton_isTightElectron_cut_WP_Tight80X_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016[1] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[1] > 0.5             ) \
                                  "' ,
                 },

  'l2tightOR2016v5' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_cut_WP_Tight80X[0] > 0.5        \
                                         || Lepton_isTightElectron_cut_WP_Tight80X_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016[0] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_cut_WP_Tight80X[1] > 0.5        \
                                         || Lepton_isTightElectron_cut_WP_Tight80X_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016[1] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[1] > 0.5             ) \
                                  "' ,
                 },

  'l2tightOR2016v6' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_cut_WP_Tight80X[0] > 0.5        \
                                         || Lepton_isTightElectron_cut_WP_Tight80X_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016[0] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_cut_WP_Tight80X[1] > 0.5        \
                                         || Lepton_isTightElectron_cut_WP_Tight80X_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016[1] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[1] > 0.5             ) \
                                  "' ,
                 },


  'l2tightOR2017' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' , 
                 },

  'l2tightOR2017v4' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' ,
                 },

  'l2tightOR2017v5' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' ,
                 },

  'l2tightOR2017v6' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_cutFall17V1Iso_Tight[0] > 0.5        \
                                         || Lepton_isTightElectron_cutFall17V2Iso_Tight[0] > 0.5        \
                                         || Lepton_isTightElectron_cutFall17V1Iso_Tight_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_cutFall17V2Iso_Tight_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_cutFall17V1Iso_Tight[1] > 0.5        \
                                         || Lepton_isTightElectron_cutFall17V2Iso_Tight[1] > 0.5        \
                                         || Lepton_isTightElectron_cutFall17V1Iso_Tight_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_cutFall17V2Iso_Tight_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' ,
                 },


  'l2tightOR2018' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' ,
                 },

  'l2tightOR2018v4' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' ,
                 },

  'l2tightOR2018v5' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' ,
                 },


  'l2tightOR2018v6' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_cutFall17V1Iso_Tight[0] > 0.5        \
                                         || Lepton_isTightElectron_cutFall17V2Iso_Tight[0] > 0.5        \
                                         || Lepton_isTightElectron_cutFall17V1Iso_Tight_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_cutFall17V2Iso_Tight_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_cutFall17V1Iso_Tight[1] > 0.5        \
                                         || Lepton_isTightElectron_cutFall17V2Iso_Tight[1] > 0.5        \
                                         || Lepton_isTightElectron_cutFall17V1Iso_Tight_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_cutFall17V2Iso_Tight_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' ,
                 },

## ------- 1-Lepton: tightOR (For LNuQQ samples)

  'l1tightOR2016v5' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=1 && Lepton_pt[0]>18) \
                                    && (    Lepton_isTightElectron_cut_WP_Tight80X[0] > 0.5        \
                                         || Lepton_isTightElectron_cut_WP_Tight80X_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016[0] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[0] > 0.5             ) \
                                  "' ,
                 },

  'l1tightOR2016v6' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=1 && Lepton_pt[0]>18) \
                                    && (    Lepton_isTightElectron_cut_WP_Tight80X[0] > 0.5        \
                                         || Lepton_isTightElectron_cut_WP_Tight80X_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016[0] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[0] > 0.5             ) \
                                  "' ,
                 },

  'l1tightOR2017v5' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=1 && Lepton_pt[0]>18) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                  "' ,
                 },

  'l1tightOR2017v6' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=1 && Lepton_pt[0]>18) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_Tight[0] > 0.5       \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_Tight[0] > 0.5       \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_Tight_SS[0] > 0.5       \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_Tight_SS[0] > 0.5       \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                  "' ,
                 },

  'l1tightOR2018v5' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=1 && Lepton_pt[0]>18) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                  "' ,
                 },

  'l1tightOR2018v6' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=1 && Lepton_pt[0]>18) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_Tight[0] > 0.5       \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_Tight[0] > 0.5       \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_Tight_SS[0] > 0.5       \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_Tight_SS[0] > 0.5       \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                  "' ,
                 },


## ------- Analysis Skims:

  'trainDYMVA'   : {
                 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : True  ,
                 'selection'  : '"(mll>12 && Lepton_pt[0]>20 && Lepton_pt[1]>10 && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
                                   && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 && LepCut2l==1 \
                                   && ptll>30 && PuppiMET_pt > 20 && fabs(91.1876 - mll) > 15 \
                                   && ((Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)))"' ,
                 'onlySample' : [
                                 #### DY
                                 'DYJetsToLL_M-10to50-LO',
                                 'DYJetsToLL_M-50-LO-ext1',
                                 #### Higgs
                                 'GluGluHToWWTo2L2NuPowheg_M125_private','VBFHToWWTo2L2NuPowheg_M125_private',
                                ] ,
                 },

  ##################################################################
  ########### VBSjjlnu semileptonic analysis SKIM
  #################################################################

  'VBSjjlnu_pairing': {
      'isChain'    : False ,
      'do4MC'      : True  ,
      'do4Data'    : True  ,
      'import'     : 'LatinoAnalysis.NanoGardener.modules.VBSjjlnu_JetPairing',
      'declare'    : 'vbs_pairing = lambda : VBSjjlnu_JetPairing(year="RPLME_YEAR", mode="ALL", debug=False)',
      'module'     : 'vbs_pairing()'
  },


  'VBSjjlnu_kin': {
      'isChain'    : False ,
      'do4MC'      : True  ,
      'do4Data'    : True  ,
      'import'     : 'LatinoAnalysis.NanoGardener.modules.VBSjjlnu_kin',
      'declare'    : 'vbs_vars_maker = lambda : VBSjjlnu_kin(mode=["maxmjj","maxmjj_massWZ"], mjj_vbs_cut=250, deltaeta_vbs_cut=2, met="PuppiMET", debug=False)',
      'module'     : 'vbs_vars_maker()'
  },

  #### OLD SKIMS
  'VBSjjlnuSkim2017v3' : {
      'isChain'    : True ,
      'do4MC'      : True  ,
      'do4Data'    : True  ,
      'selection'  : '"nLepton>=1  && Lepton_pt[0]>30 \
                          && (  Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5 \
                             || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5 ) \
                        && Alt$(Lepton_pt[1],0)<=10 && Alt$(Lepton_isLoose[1],1)> 0.5 \
                         && (  Alt$(Lepton_isTightElectron_mvaFall17V1Iso_WP90[1], 0) < 0.5 \
                             && Alt$(Lepton_isTightMuon_cut_Tight_HWWW[1],0) < 0.5 )  \
                        "',  
      'subTargets': ['CleanFatJet', 'VBSjjlnu_pairing', 'VBSjjlnu_kin'],
      'onlySample' : vbsjjlnu_samples_bkg + vbsjjlnu_samples_signal + vbsjjlnu_samples_data2017
  },

  'VBSjjlnuSkim2017v3_fakesv2' : {
      'isChain'    : True ,
      'do4MC'      : True  ,
      'do4Data'    : True  ,
      'selection'  : '"nLepton>=1 && Lepton_pt[0]>30 \
                        && Alt$(Lepton_pt[1],0)<=10 && Alt$(Lepton_isLoose[1],1)> 0.5 \
                        && (  Alt$(Lepton_isTightElectron_mvaFall17V1Iso_WP90[1], 0) < 0.5 \
                             && Alt$(Lepton_isTightMuon_cut_Tight_HWWW[1],0) < 0.5 ) \
                        "',  
      'subTargets': ['fakeWstep1l','CleanFatJet', 'VBSjjlnu_pairing', 'VBSjjlnu_kin'],
      'onlySample' : vbsjjlnu_samples_data2017
  },
  #########################
  ### v4 chains

  'VBSjjlnuSkim2016v4' : {
      'isChain'    : True ,
      'do4MC'      : True  ,
      'do4Data'    : True  ,
      'selection'  : '"nLepton>=1  && Lepton_pt[0]>30 \
                          && (  Lepton_isTightElectron_mva_90p_Iso2016[0] > 0.5 \
                             || Lepton_isTightMuon_cut_Tight80x[0] > 0.5 ) \
                        && Alt$(Lepton_pt[1],0)<=10 && Alt$(Lepton_isLoose[1],1)> 0.5 \
                         && (  Alt$(Lepton_isTightElectron_mva_90p_Iso2016[1], 0) < 0.5 \
                             && Alt$(Lepton_isTightMuon_cut_Tight80x[1],0) < 0.5 )  \
                        "',  
      'subTargets': ['wNLOEWK','zNLOEWK','trigMC', 'CleanFatJet', 'CorrFatJetMass', 'VBSjjlnu_pairing', 'VBSjjlnu_kin'],
      'onlySample' : vbsjjlnu_samples_bkg + vbsjjlnu_samples_signal
  },

  'VBSjjlnuSkim2016v4_data' : {
      'isChain'    : True ,
      'do4MC'      : True  ,
      'do4Data'    : True  ,
      'selection'  : '"nLepton>=1  && Lepton_pt[0]>30 \
                        && Alt$(Lepton_pt[1],0)<=10 && Alt$(Lepton_isLoose[1],1)> 0.5 \
                         && (  Alt$(Lepton_isTightElectron_mva_90p_Iso2016[1], 0) < 0.5 \
                             && Alt$(Lepton_isTightMuon_cut_Tight80x[1],0) < 0.5 )  \
                        "',  
      'subTargets': ['fakeWstep1l','CleanFatJet', 'VBSjjlnu_pairing', 'VBSjjlnu_kin'],
      'onlySample' : vbsjjlnu_samples_data2016
  },

  'VBSjjlnuSkim2017v4' : {
      'isChain'    : True ,
      'do4MC'      : True  ,
      'do4Data'    : True  ,
      'selection'  : '"nLepton>=1  && Lepton_pt[0]>30 \
                          && (  Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5 \
                             || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5 ) \
                        && Alt$(Lepton_pt[1],0)<=10 && Alt$(Lepton_isLoose[1],1)> 0.5 \
                         && (  Alt$(Lepton_isTightElectron_mvaFall17V1Iso_WP90[1], 0) < 0.5 \
                             && Alt$(Lepton_isTightMuon_cut_Tight_HWWW[1],0) < 0.5 )  \
                        "',  
      'subTargets': ['wNLOEWK','zNLOEWK','trigMC', 'CleanFatJet', 'CorrFatJetMass', 'VBSjjlnu_pairing', 'VBSjjlnu_kin'],
      'onlySample' : vbsjjlnu_samples_bkg + vbsjjlnu_samples_signal + vbsjjlnu_samples_data2017
  },

  'VBSjjlnuSkim2017v4_fakes' : {
      'isChain'    : True ,
      'do4MC'      : False  ,
      'do4Data'    : True  ,
      'selection'  : '"nLepton>=1 && Lepton_pt[0]>30 \
                        && Alt$(Lepton_pt[1],0)<=10 && Alt$(Lepton_isLoose[1],1)> 0.5 \
                        && (  Alt$(Lepton_isTightElectron_mvaFall17V1Iso_WP90[1], 0) < 0.5 \
                             && Alt$(Lepton_isTightMuon_cut_Tight_HWWW[1],0) < 0.5 ) \
                        "',  
      'subTargets': ['fakeWstep1l','CleanFatJet', 'VBSjjlnu_pairing', 'VBSjjlnu_kin'],
      'onlySample' : vbsjjlnu_samples_data2017
  },

  'VBSjjlnuSkim2018v4' : {
      'isChain'    : True ,
      'do4MC'      : True  ,
      'do4Data'    : False  ,
      'selection'  : '"nLepton>=1  && Lepton_pt[0]>30 \
                          && (  Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5 \
                             || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5 ) \
                        && Alt$(Lepton_pt[1],0)<=10 && Alt$(Lepton_isLoose[1],1)> 0.5 \
                         && (  Alt$(Lepton_isTightElectron_mvaFall17V1Iso_WP90[1], 0) < 0.5 \
                             && Alt$(Lepton_isTightMuon_cut_Tight_HWWW[1],0) < 0.5 )  \
                        "',  
      'subTargets': ['wNLOEWK','zNLOEWK','trigMC', 'CleanFatJet', 'CorrFatJetMass', 'VBSjjlnu_pairing', "VBSjjlnu_kin"],
      'onlySample' : vbsjjlnu_samples_bkg + vbsjjlnu_samples_signal 
  },

  'VBSjjlnuSkim2018v4_data' : {
      'isChain'    : True ,
      'do4MC'      : False  ,
      'do4Data'    : True  ,
      'selection'  : '"nLepton>=1  && Lepton_pt[0]>30 \
                         && Alt$(Lepton_pt[1],0)<=10 && Alt$(Lepton_isLoose[1],1)> 0.5 \
                         && (  Alt$(Lepton_isTightElectron_mvaFall17V1Iso_WP90[1], 0) < 0.5 \
                             && Alt$(Lepton_isTightMuon_cut_Tight_HWWW[1],0) < 0.5 )  \
                        "',  
      'subTargets': ['fakeWstep1l','CleanFatJet', 'VBSjjlnu_pairing', "VBSjjlnu_kin"],
      'onlySample' : vbsjjlnu_samples_data2018
  },

  ############ New VBSjjlnu v5 skim and systematics
  ### News: 
  ### - rerun the NLOEWk modules
  ### - rerun trigMC to fix the trig efficiency systematic for electrons
  ### - rerun FatJet correction and cleaning


#  'VBSjjlnuSkim2016v5' : {
#      'isChain'    : True ,
#      'do4MC'      : True  ,
#      'do4Data'    : True  ,
#      'selection'  : vbsjjlnu_preselection_mc_2016,
#      'subTargets': ['wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK',
#                    'trigMC', 'CorrFatJetMC', 'CleanFatJet', 
#                    'VBSjjlnu_pairing', 'VBSjjlnu_kin'],
#      'onlySample' : vbsjjlnu_samples_bkg + vbsjjlnu_samples_signal
#  },
#
#  'VBSjjlnuSkim2016v5_data' : {
#      'isChain'    : True ,
#      'do4MC'      : True  ,
#      'do4Data'    : True  ,
#      'selection'  : vbsjjlnu_preselection_data_2016,  
#      'subTargets': ['fakeWstep1l','CorrFatJetData', 'CleanFatJet', 'VBSjjlnu_pairing', 'VBSjjlnu_kin'],
#      'onlySample' : vbsjjlnu_samples_data2016
#  },
#
#  'VBSjjlnuSkim2017v5' : {
#      'isChain'    : True ,
#      'do4MC'      : True  ,
#      'do4Data'    : True  ,
#      'selection'  : vbsjjlnu_preselection_mc_2017,
#      'subTargets': ['wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK',
#                    'trigMC', 'CorrFatJetMC', 'CleanFatJet', 
#                    'VBSjjlnu_pairing', 'VBSjjlnu_kin'],
#      'onlySample' : vbsjjlnu_samples_bkg + vbsjjlnu_samples_signal
#  },
#
#  'VBSjjlnuSkim2017v5_data' : {
#      'isChain'    : True ,
#      'do4MC'      : True  ,
#      'do4Data'    : True  ,
#      'selection'  : vbsjjlnu_preselection_data_2017,  
#      'subTargets': ['fakeWstep1l','CorrFatJetData', 'CleanFatJet', 'VBSjjlnu_pairing', 'VBSjjlnu_kin'],
#      'onlySample' : vbsjjlnu_samples_data2017
#  },
#
#  'VBSjjlnuSkim2018v5' : {
#      'isChain'    : True ,
#      'do4MC'      : True  ,
#      'do4Data'    : True  ,
#      'selection'  : vbsjjlnu_preselection_mc_2018,
#      'subTargets': ['wwNLOEWK','wzNLOEWK','zzNLOEWK','zNLOEWK','wNLOEWK',
#                    'trigMC', 'CorrFatJetMC', 'CleanFatJet', 
#                    'VBSjjlnu_pairing', 'VBSjjlnu_kin'],
#      'onlySample' : vbsjjlnu_samples_bkg + vbsjjlnu_samples_signal
#  },
#
#  'VBSjjlnuSkim2018v5_data' : {
#      'isChain'    : True ,
#      'do4MC'      : True  ,
#      'do4Data'    : True  ,
#      'selection'  : vbsjjlnu_preselection_data_2018,  
#      'subTargets': ['fakeWstep1l','CorrFatJetData', 'CleanFatJet', 'VBSjjlnu_pairing', 'VBSjjlnu_kin'],
#      'onlySample' : vbsjjlnu_samples_data2018
#  },
#
  #### Fatjet systematics are included at the bottom

# ------------------------------------ SPECIAL STEPS: HADD & UEPS -------------------------------------------------

## ------- HADD 

  'hadd'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'SizeMax'    : 5e9 ,
                 #'bigSamples' : ['DYJetsToLL_M-50','DY2JetsToLL','ZZTo2L2Q','DYJetsToLL_M-50-LO',
                 #                'DYJetsToLL_M-50-LO-ext1',
                 #                'WZTo2L2Q','TTToSemiLepton','TTToSemiLeptonic','TTTo2L2Nu_ext1','TTJetsDiLep-LO-ext1','TTTo2L2Nu',
                 #                'DYJetsToEE_Pow',
                 #                'DY1JetsToLL',
                 #                #'TTJets',
                 #               ],
               },

## ------- UEPS 
## ------- UEPS 

  'UEPS'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'onlySample' : [ 'TTToSemiLeptonic','TTTo2L2Nu','TTToSemiLeptonic_ext3','TTTo2L2Nu_ext3',
                                   'TT_TuneCUETP8M2T4_PSweights',
                                 ] ,
                  'cpMap' : {
                              'UEdo' : {
                                          'TTToSemiLeptonic_TuneCP5Down' : ['TTToSemiLeptonic','TTToSemiLeptonic_ext3'],
                                          'TTTo2L2Nu_TuneCP5Down' : ['TTTo2L2Nu','TTTo2L2Nu_ext3'],
                                          'TT_TuneCUETP8M2T4Down' : ['TT_TuneCUETP8M2T4_PSweights'],
                                       },
                              'UEup' : {
                                          'TTToSemiLeptonic_TuneCP5Up' : ['TTToSemiLeptonic','TTToSemiLeptonic_ext3'],
                                          'TTTo2L2Nu_TuneCP5Up' : ['TTTo2L2Nu','TTTo2L2Nu_ext3'],
                                          'TT_TuneCUETP8M2T4Up' : ['TT_TuneCUETP8M2T4_PSweights'],
                                       },
                              'HDAMPdo' : {
                                          'TTToSemiLeptonic_hdampDown' : ['TTToSemiLeptonic','TTToSemiLeptonic_ext3'],
                                          'TTTo2L2Nu_hdampDown' : ['TTTo2L2Nu','TTTo2L2Nu_ext3'],
                                          'TT_hdampDown' : ['TT_TuneCUETP8M2T4_PSweights'],
                                       },
                              'HDAMPup' : {
                                          'TTToSemiLeptonic_hdampUp' : ['TTToSemiLeptonic','TTToSemiLeptonic_ext3'],
                                          'TTTo2L2Nu_hdampUp' : ['TTTo2L2Nu','TTTo2L2Nu_ext3'],
                                          'TT_hdampUp' : ['TT_TuneCUETP8M2T4_PSweights'],
                                       },
                              'MTOPdo'  : {
                                          'TTToSemiLeptonic_mtopDown' : ['TTToSemiLeptonic','TTToSemiLeptonic_ext3'],
                                          'TTTo2L2Nu_mtopDown' : ['TTTo2L2Nu','TTTo2L2Nu_ext3'],
                                          'TT_mtopDown' : ['TT_TuneCUETP8M2T4_PSweights'],
                                       },
                              'MTOPup'  : {
                                          'TTToSemiLeptonic_mtopUp' : ['TTToSemiLeptonic','TTToSemiLeptonic_ext3'],
                                          'TTTo2L2Nu_mtopUp' : ['TTTo2L2Nu','TTTo2L2Nu_ext3'],
                                          'TT_mtopUp' : ['TT_TuneCUETP8M2T4_PSweights'],
                                       },
                            },
               },



}
Steps.update(addJESchainMembers())

### ADD systematics for VBSjjlnu analysis
#Steps.update(prepare_VBSjjlnu_syst("VBSjjlnuSkim2016v5",vbsjjlnu_preselection_mc_2016))
#Steps.update(prepare_VBSjjlnu_syst("VBSjjlnuSkim2017v5", vbsjjlnu_preselection_mc_2017))
#Steps.update(prepare_VBSjjlnu_syst("VBSjjlnuSkim2018v5", vbsjjlnu_preselection_mc_2018))
### ADD fatjet systematic for VBSjjlnu analysis
#Steps.update(prepare_VBSjjlnu_Fatjet_syst("VBSjjlnuSkim2016v5_fatjet", vbsjjlnu_preselection_mc_2016))
#Steps.update(prepare_VBSjjlnu_Fatjet_syst("VBSjjlnuSkim2017v5_fatjet", vbsjjlnu_preselection_mc_2017))
#Steps.update(prepare_VBSjjlnu_Fatjet_syst("VBSjjlnuSkim2018v5_fatjet", vbsjjlnu_preselection_mc_2018))
#
## Add fatjet systemtics for High Mass Semilep analysis

Steps.update(prepare_HMsemilep_Fatjet_syst("HMSemilep2016v6_fatjet"))
Steps.update(prepare_HMsemilep_Fatjet_syst("HMSemilep2017v6_fatjet"))
Steps.update(prepare_HMsemilep_Fatjet_syst("HMsemilep2018v6_fatjet"))


# Add syst steps for CHToCB
# kinFitTTSemiLep_jetMETSyst_Total
# kinFitTTSemiLep_jetMETSyst_uncorr
# kinFitTTSemiLep_jetMETSyst_corr
Steps.update(prepare_CHToCB_syst("kinFitTTSemiLep"))
