import ROOT
from ROOT import TFile, TTree
from array import array
import os
import random

from variables import Variables

random.seed(1234)

xrd_base = 'root://cms-xrdr.private.lo:2094//xrd/store/user/bhoh/Latino/HWWNano/'
prod_2016HIPM   = 'Summer20UL16_106x_nAODv9_HIPM_Full2016v9/CHToCBLepton2016v9__CHToCBJetMETCorr2016v9__kinFitTTSemiLepV5__mvaTreeCHToCB/'
prod_2016noHIPM = 'Summer20UL16_106x_nAODv9_noHIPM_Full2016v9/CHToCBLepton2016v9__CHToCBJetMETCorr2016v9__kinFitTTSemiLepV5__mvaTreeCHToCB/'
prod_2017       = 'Summer20UL17_106x_nAODv9_Full2017v9/CHToCBLepton2017v9__CHToCBJetMETCorr2017v9__kinFitTTSemiLepV5__mvaTreeCHToCB/'
prod_2018       = 'Summer20UL18_106x_nAODv9_Full2018v9/CHToCBLepton2018v9__CHToCBJetMETCorr2018v9__kinFitTTSemiLepV5__mvaTreeCHToCB/'

mass_list = ['075', '080', '085', '090', '100', '110', '120', '130', '140', '150', '160' ]
#XXX
#mass_list = ['080', '085', '090', '100', '110', '120', '130', '140', '150', '160' ]

file_names = {}
file_names[('2016HIPM','TTLJ_powheg')]   = [ xrd_base + prod_2016HIPM   + "nanoLatino_TTToSemiLeptonic__part*.root" ]
file_names[('2016noHIPM','TTLJ_powheg')] = [ xrd_base + prod_2016noHIPM + "nanoLatino_TTToSemiLeptonic__part*.root" ]
file_names[('2017','TTLJ_powheg')]       = [ xrd_base + prod_2017       + "nanoLatino_TTToSemiLeptonic__part*.root" ]
file_names[('2018','TTLJ_powheg')]       = [ xrd_base + prod_2018       + "nanoLatino_TTToSemiLeptonic__part*.root" ]

for mass in mass_list:
  sample_name = "CHToCB_M" + mass
  file_names[('2016HIPM',sample_name)]   = [ xrd_base + prod_2016HIPM   + "nanoLatino_{SAMPLE}__part*.root".format(SAMPLE=sample_name) ]
  file_names[('2016noHIPM',sample_name)] = [ xrd_base + prod_2016noHIPM + "nanoLatino_{SAMPLE}__part*.root".format(SAMPLE=sample_name) ]
  file_names[('2017',sample_name)]       = [ xrd_base + prod_2017       + "nanoLatino_{SAMPLE}__part*.root".format(SAMPLE=sample_name) ]
  file_names[('2018',sample_name)]       = [ xrd_base + prod_2018       + "nanoLatino_{SAMPLE}__part*.root".format(SAMPLE=sample_name) ]


max_events = {
  #
  ('2016HIPM','TTLJ_powheg') : 3000000,
  ('2016HIPM','CHToCB_M075') : 300000,
  ('2016HIPM','CHToCB_M080') : 300000,
  ('2016HIPM','CHToCB_M085') : 300000,
  ('2016HIPM','CHToCB_M090') : 300000,
  ('2016HIPM','CHToCB_M100') : 300000,
  ('2016HIPM','CHToCB_M110') : 300000,
  ('2016HIPM','CHToCB_M120') : 300000,
  ('2016HIPM','CHToCB_M130') : 300000,
  ('2016HIPM','CHToCB_M140') : 300000,
  ('2016HIPM','CHToCB_M150') : 300000,
  ('2016HIPM','CHToCB_M160') : 300000,

  #
  ('2016noHIPM','TTLJ_powheg') : 3000000,
  ('2016noHIPM','CHToCB_M075') : 300000,
  ('2016noHIPM','CHToCB_M080') : 300000,
  ('2016noHIPM','CHToCB_M085') : 300000,
  ('2016noHIPM','CHToCB_M090') : 300000,
  ('2016noHIPM','CHToCB_M100') : 300000,
  ('2016noHIPM','CHToCB_M110') : 300000,
  ('2016noHIPM','CHToCB_M120') : 300000,
  ('2016noHIPM','CHToCB_M130') : 300000,
  ('2016noHIPM','CHToCB_M140') : 300000,
  ('2016noHIPM','CHToCB_M150') : 300000,
  ('2016noHIPM','CHToCB_M160') : 300000,
  #
  ('2017','TTLJ_powheg') : 3000000,
  ('2017','CHToCB_M075') : 300000,
  ('2017','CHToCB_M080') : 300000,
  ('2017','CHToCB_M085') : 300000,
  ('2017','CHToCB_M090') : 300000,
  ('2017','CHToCB_M100') : 300000,
  ('2017','CHToCB_M110') : 300000,
  ('2017','CHToCB_M120') : 300000,
  ('2017','CHToCB_M130') : 300000,
  ('2017','CHToCB_M140') : 300000,
  ('2017','CHToCB_M150') : 300000,
  ('2017','CHToCB_M160') : 300000,
  #
  ('2018','TTLJ_powheg') : 3000000,
  ('2018','CHToCB_M075') : 300000,
  ('2018','CHToCB_M080') : 300000,
  ('2018','CHToCB_M085') : 300000,
  ('2018','CHToCB_M090') : 300000,
  ('2018','CHToCB_M100') : 300000,
  ('2018','CHToCB_M110') : 300000,
  ('2018','CHToCB_M120') : 300000,
  ('2018','CHToCB_M130') : 300000,
  ('2018','CHToCB_M140') : 300000,
  ('2018','CHToCB_M150') : 300000,
  ('2018','CHToCB_M160') : 300000,
     
}

def SkimTree(outFileName, fileList, nMax, formula, year_label=None, mass_label=None, n_samples_by_mass=None):

  formula = formula.replace('import','').replace('__','')

  outFile = TFile(outFileName,"RECREATE")
  fChain  = ROOT.TChain("Events")
  for file_ in fileList:
    fChain.Add(file_)

  
  fChain.SetBranchStatus("*",0)

  mvaVars = Variables()
  mvaVars.include_dijet_pt = True
  mvaVars_dict = mvaVars.getVariables()
  for varKey in mvaVars_dict:
    if ":=" in mvaVars_dict[varKey]['definition']:
      continue
    fChain.SetBranchStatus(mvaVars_dict[varKey]['definition'],1)

  fChain.SetBranchStatus("EventNum_mvaCHToCB",1)
  fChain.SetBranchStatus("fitted_dijet_M_nom",1)
  fChain.SetBranchStatus("fitted_dijet_M_high_nom",1)
  fChain.SetBranchStatus("nbtags_event_mvaCHToCB_nom",1)
  fChain.SetBranchStatus("nbtags_had_top_mvaCHToCB_nom",1)
  fChain.SetBranchStatus("Lepton_genmatched",1)
  fChain.SetBranchStatus("Lepton_pt",1)
  fChain.SetBranchStatus("Lepton_pdgId",1)
  fChain.SetBranchStatus("Lepton_eta",1)
  fChain.SetBranchStatus("PuppiMET_pt",1)
  fChain.SetBranchStatus("XSWeight",1)
  fChain.SetBranchStatus("status_nom",1)
  fChain.SetBranchStatus("btagSF",1)
  fChain.SetBranchStatus("genTtbarId",1)
  #fChain.SetBranchStatus("matched_4jet_matched",1)

  #block1 = fChain.CopyTree("EventNum_mvaCHToCB%100 >= 50")
  #block2 = fChain.CopyTree("EventNum_mvaCHToCB%100 <  50")

  tmp_tree = fChain.CopyTree("status_nom==0 && nbtags_event_mvaCHToCB_nom>=3 && nbtags_had_top_mvaCHToCB_nom>=2 && Lepton_genmatched[0]>0.5 && Lepton_pt[0] > 30. && ((abs(Lepton_pdgId[0])==11 && ( abs(Lepton_eta[0])<2.5 )) || (abs(Lepton_pdgId[0])==13 && ( abs(Lepton_eta[0])<2.4 )))")
  #tmp_tree = fChain.CopyTree("status_nom==0 && nbtags_event_mvaCHToCB_nom>=3 && nbtags_had_top_mvaCHToCB_nom>=1")
  #tmp_tree = fChain.CopyTree("matched_4jet_matched && status_nom==0")
  #tmp_tree = fChain.CopyTree("nbtags_event_mvaCHToCB_nom>=3 && status_nom==0")
  outTree  = tmp_tree.CloneTree(0)


  # add sample mass_label
  if mass_label!=None:
    v_mass_label = array('f', [mass_label])
    outTree.Branch("mass_label",v_mass_label,"mass_label/F")

  if n_samples_by_mass!=None:
    mass_labels = []
    for key in n_samples_by_mass:
        n_sample = n_samples_by_mass[key]
        mass_labels.extend([float(key)]*n_sample)
    v_mass_label = array('f', [-1.])
    outTree.Branch("mass_label",v_mass_label,"mass_label/F")

  # add year_label
  if year_label!=None:
    v_year_label = array('f', [year_label])
    outTree.Branch("year_label",v_year_label,"year_label/F")
  
  nEntries = tmp_tree.GetEntries()

  entries = list(range(nEntries))
  #if 'CHToCB' in outFileName:
  #  for _ in range(10):
  #    random.shuffle(entries)
  print("entries: %d"%len(entries))
  print(entries[:100])

  if nEntries > nMax:
    entries = entries[:nMax]

  if n_samples_by_mass!=None:
    while len(mass_labels) <= len(entries):
        mass_labels = mass_labels * 2
    random.shuffle(mass_labels)

  for i in entries:
  #for i in range(nEntries):

    flag = eval(formula)
    if not flag:
      continue

    #get entry and fill
    tmp_tree.GetEntry(i)
    if n_samples_by_mass!=None:
        v_mass_label[0] = mass_labels[i]
    outTree.Fill()
    #print(10*i+j, tmp_tree.EventNum_mvaCHToCB)
    #print(10*(i+1)+j, tmp_tree.EventNum_mvaCHToCB)



  outFile.cd()
  outTree.AutoSave()
  #outTree.Write()
  outFile.Close()


def createDir():
    directory = "/cms_scratch/bhoh"
    if not os.path.exists(directory):
        os.makedirs(directory)

def nSamplesByMass(file_dict):
    out_dict = {}
    for key in file_names:
        year, sample  = key
        if 'CHToCB' not in sample:
            continue
        mass = sample.split("CHToCB_M")[-1]
        fileName      = "/cms_scratch/bhoh/mva_%s_%s.root"%(sample,year)
        tmp_f = TFile(fileName,"READ")
        tmp_tree = tmp_f.Get("Events")
        entries = tmp_tree.GetEntries()
        out_dict[mass] = entries
    return out_dict


def getYearLabel(year_):

  out_label = None

  if year_ == "2016HIPM":
    out_label = 0
  elif year_ == "2016noHIPM":
    out_label = 1
  elif year_ == "2017":
    out_label = 2
  elif year_ == "2018":
    out_label = 3

  return out_label


if __name__ == "__main__":
  createDir()
  for key in file_names:
    year, sample  = key
    outFileName      = "/cms_scratch/bhoh/mva_%s_%s.root"%(sample,year)
    outFileNameTrain = "/cms_scratch/bhoh/mva_%s_%s_Train.root"%(sample,year)
    outFileNameTest = "/cms_scratch/bhoh/mva_%s_%s_Test.root"%(sample,year)
    print(outFileNameTrain, file_names[key])
    print(outFileNameTest, file_names[key])
    nMax = max_events[key]
  
    #add signal sample label
    if 'CHToCB' in sample:
      mass = sample.split("CHToCB_M")[-1]
      SkimTree(outFileName, file_names[key], nMax, "1==1", getYearLabel(year), float(mass))
  
  for key in file_names:
    year, sample  = key
    outFileName      = "/cms_scratch/bhoh/mva_%s_%s.root"%(sample,year)
    outFileNameTrain = "/cms_scratch/bhoh/mva_%s_%s_Train.root"%(sample,year)
    outFileNameTest = "/cms_scratch/bhoh/mva_%s_%s_Test.root"%(sample,year)
    print(outFileNameTrain, file_names[key])
    print(outFileNameTest, file_names[key])
    nMax = max_events[key]
  
    #add bkg. sample label (randomized probabiltiy weighted by number events of each samples)
    if 'TTLJ_powheg' in sample:
      n_samples_by_mass = nSamplesByMass(file_names)
      SkimTree(outFileName, file_names[key], nMax, "1==1", getYearLabel(year), None, n_samples_by_mass)
  
  for key in file_names:
    year, sample  = key
    outFileName      = "/cms_scratch/bhoh/mva_%s_%s.root"%(sample,year)
    outFileNameTrain = "/cms_scratch/bhoh/mva_%s_%s_Train.root"%(sample,year)
    outFileNameTest = "/cms_scratch/bhoh/mva_%s_%s_Test.root"%(sample,year)
    print(outFileNameTrain, file_names[key])
    print(outFileNameTest, file_names[key])
    nMax = max_events[key]
  
  
    #divide into train and test and validation set
  
    SkimTree(outFileNameTrain, [outFileName], nMax, "(i % 10)>=3")
    SkimTree(outFileNameTest,  [outFileName], nMax, "(i % 10)<3")
