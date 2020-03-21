import ROOT
import numpy as np
import os

CMSSW     = os.environ["CMSSW_BASE"]
BASE_PATH = CMSSW + "/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv6/2018/SKIM5"

variables_BTag   = BASE_PATH + "/ReshapeNorm_BTagSF/variables.py"
variables_NoBTag = BASE_PATH + "/ReshapeNorm_NoBTagSF/variables.py"

rootfile_BTag   = BASE_PATH + "/rootFile_2018_ReshapeNorm_BTagSF/hadd.root"
rootfile_NoBTag = BASE_PATH + "/rootFile_2018_ReshapeNorm_NoBTagSF/hadd.root"

tfile_BTag   = ROOT.TFile(rootfile_BTag,  "READ")
tfile_NoBTag = ROOT.TFile(rootfile_NoBTag,"READ")

print("load TFile:\n%s"% tfile_BTag)
print("load TFile:\n%s"% tfile_NoBTag)


def GetHist(tfile,histName):
    outHist = tfile.Get(histName)
    if outHist == None:
        raise Exception("[Error] %s is not found"%(histName))
    return outHist

def GetRatio(hist_BTag, hist_NoBTag):
    try:
      ratio = hist_NoBTag.GetBinContent(2) / hist_BTag.GetBinContent(2)
    except ZeroDivisionError:
      ratio = 1.
    return ratio

def GetVariableKeys(variables_path):
    variables={}
    print("load variables from: %s"%variables_path)
    handle = open(variables_path)
    exec(handle)
    handle.close()
    return variables.keys()

def WriteRatio(key_list, ratio_list):
    def binParser(key_list, flavour, variable):
        print("parse binning: %s    %s"%(flavour,variable))
        #filter key_list
        # ex) key : udsg_pt60toINF_abseta0.8to1.6
        key_list_ = [key for key in key_list if flavour == key.split("_")[0]]
        out_bin_list = []
        for key_ in key_list_:
          token = key_.split('_')
          bin_range = next(ele.replace(variable,'').split('to') for ele in token if variable in ele)
          if not len(bin_range)==2:
            raise RuntimeError("binParger :  len of bin_range[0] is %d"%len(bin_range[0]))
          bin_start = float(bin_range[0])
          bin_end   = float(bin_range[1].replace("INF","1000"))
          #append to out list
          out_bin_list += [bin_start] if bin_start not in out_bin_list else []
          out_bin_list += [bin_end]   if bin_end not in out_bin_list else []

        out_bin_list.sort()
        print("out_bining :")
        print(out_bin_list)
        return out_bin_list

    def getBinIdx(key,variable,variable_bin):
        token = key.split('_')
        variable_range = next(ele.replace(variable,'') for ele in token if variable in ele)
        # estimate bin center
        variable_center = sum([ float(ele.replace('INF',"1000")) for ele in variable_range.split('to')])/2.
        # estimate bin index
        variable_bin_idx = -1
        for i, value in enumerate(variable_bin):
          if value > variable_center:
            variable_bin_idx = i
            break
        if variable_bin_idx == -1:
            raise Exception("getBinIdx : bin idx coudln't found")
        return variable_bin_idx

    pt_bin={}
    pt_bin["b"]    = binParser(key_list,"b","pt")
    pt_bin["udsg"] = binParser(key_list,"udsg","pt")
    abseta_bin={}
    abseta_bin["b"]    = binParser(key_list,"b","abseta")
    abseta_bin["udsg"] = binParser(key_list,"udsg","abseta")

    ratio_hist={}
    #print(np.asarray(pt_bin["b"]))
    #print(np.asarray(abseta_bin["b"]))
    ratio_hist["b"] = ROOT.TH2D("b","b",len(pt_bin["b"])-1,np.asarray(pt_bin["b"]),len(abseta_bin["b"])-1,np.asarray(abseta_bin["b"]))
    ratio_hist["udsg"] = ROOT.TH2D("udsg","udsg",len(pt_bin["udsg"])-1,np.asarray(pt_bin["udsg"]),len(abseta_bin["udsg"])-1,np.asarray(abseta_bin["udsg"]))

    for i, key in enumerate(key_list):
      flavour = key.split("_")[0]
      pt_bin_idx = getBinIdx(key,"pt",pt_bin[flavour])
      abseta_bin_idx = getBinIdx(key,"abseta",abseta_bin[flavour])
      ratio = ratio_list[i]
      ratio_hist[flavour].SetBinContent(pt_bin_idx, abseta_bin_idx, ratio)

    for key in ratio_hist:
      ratio_hist[key].Write()
    
    return

# test GetVariableKeys
#print(GetVariableKeys(variables_BTag))
#print(GetVariableKeys(variables_NoBTag))

ratio_list=[]
key_list=[]
for key in GetVariableKeys(variables_BTag):
  if key=="Event":
      continue

  #rootFile_2018_ReshapeNorm_BTagSF
  #rootFile_2018_ReshapeNorm_NoBTagSF
  #"Lep__Top" + key + "histo_top"
  histName = "Lep__Top/%s/histo_top"%key
  # test GetHist
  #print(GetHist(tfile_BTag, histName))
  #print(GetHist(tfile_NoBTag, histName))
  # test GetRatio
  #print(GetRatio(GetHist(tfile_BTag, histName),GetHist(tfile_NoBTag, histName)))
  ratio = GetRatio(GetHist(tfile_BTag, histName),GetHist(tfile_NoBTag, histName))
  ratio_list.append(ratio)
  key_list.append(key)

out_rootfile = ROOT.TFile("BTagReshapeNorm.root","RECREATE")
out_rootfile.cd()
WriteRatio(key_list,ratio_list)
out_rootfile.Close()








