import ROOT

fCombineNameLow ='/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/diffNuisances/fitDiagnostics75.root'
fCombineNameHigh='/cms_scratch/bhoh/toys/fitDiagnosticsPostFit150.root'

fName_2018       = '../../2018/StackNew_comb/rootFile_2018_SKIM9_final/PDF/results_unc.root'
fName_2017       = '../../2017/StackNew_comb/rootFile_2017_SKIM9_final/PDF/results_unc.root'
fName_2016noHIPM = '../../2016noHIPM/StackNew_comb/rootFile_2016noHIPM_SKIM9_final/PDF/results_unc.root'
fName_2016HIPM   = '../../2016HIPM/StackNew_comb/rootFile_2016HIPM_SKIM9_final/PDF/results_unc.root'

fCombineLow = ROOT.TFile(fCombineNameLow, "READ")
fCombineHigh = ROOT.TFile(fCombineNameHigh, "READ")

f_2018       = ROOT.TFile(fName_2018      , 'READ')
f_2017       = ROOT.TFile(fName_2017      , 'READ')
f_2016noHIPM = ROOT.TFile(fName_2016noHIPM, 'READ')
f_2016HIPM   = ROOT.TFile(fName_2016HIPM  , 'READ')


def getDATA(f_, cutName, varName):
  h_DATA = f_.Get("{VAR1}/{VAR2}/histo_DATA".format(VAR1=cutName, VAR2=varName))
  return h_DATA

def getDATAs(fList, cutName, varName):
  h_DATA = None
  for f_ in fList:
    if h_DATA == None:
      h_DATA = f_.Get("{VAR1}/{VAR2}/histo_DATA".format(VAR1=cutName, VAR2=varName))
    else:
      tmp_h_DATA = f_.Get("{VAR1}/{VAR2}/histo_DATA".format(VAR1=cutName, VAR2=varName))
      h_DATA.Add(tmp_h_DATA)
  return h_DATA

def getPreFitMC(f_, era, cutName, sampleName):
  h_MC = f_.Get("shapes_prefit/{VAR1}__{VAR2}/{VAR3}".format(VAR1=era, VAR2=cutName, VAR3=sampleName))
  return h_MC

def getPreFitMCs(f_, eras, cutName, sampleName):
  h_MC = None
  for era in eras:
    if h_MC == None:
      h_MC = f_.Get("shapes_prefit/{VAR1}__{VAR2}/{VAR3}".format(VAR1=era, VAR2=cutName, VAR3=sampleName))
    else:
      tmp_h_MC = f_.Get("shapes_prefit/{VAR1}__{VAR2}/{VAR3}".format(VAR1=era, VAR2=cutName, VAR3=sampleName))
      h_MC.Add(tmp_h_MC)
  return h_MC


def changeMCbins(h_MC, h_DATA):
  h_MC_new = h_DATA.Clone("histo_" + h_MC.GetName())

  for i in range(h_MC_new.GetNbinsX()):
    iBin = i + 1
    bin_content = h_MC.GetBinContent(iBin)
    bin_error   = h_MC.GetBinError(iBin)

    h_MC_new.SetBinContent(iBin, bin_content)
    h_MC_new.SetBinError(iBin,   bin_error)

  return h_MC_new


def saveHistos(fOut, cutName, varName, hNames, histos):
  pathName = '{CUT}/{VAR}'.format(CUT=cutName, VAR=varName)
  if fOut.Get(pathName):
    pass
  else:
    fOut.mkdir(pathName)
  
  fOut.cd(pathName)

  if len(hNames) != len(histos):
    raise RuntimeError("Inside of the saveHistos:  len(hNames) != len(histos)")
  for i_name, hName in enumerate(hNames):
    histo = histos[i_name]
    print("{}/{}: {}".format(pathName, hName, histo.Integral()))
    histo.Write(hName)
    
def saveHistos_CHToCB(fOut, fCombine, cutName, varName):
  h_DATA   = getDATAs([f_2018, f_2017, f_2016noHIPM, f_2016HIPM], cutName, varName)
  h_Others = changeMCbins( getPreFitMCs(fCombine, ['Y2018', 'Y2017', 'Y2016noHIPM', 'Y2016HIPM'], cutName, 'Others'), h_DATA)
  h_ST     = changeMCbins( getPreFitMCs(fCombine, ['Y2018', 'Y2017', 'Y2016noHIPM', 'Y2016HIPM'], cutName,     'ST'), h_DATA)
  h_TTjj   = changeMCbins( getPreFitMCs(fCombine, ['Y2018', 'Y2017', 'Y2016noHIPM', 'Y2016HIPM'], cutName,  'TT+jj'), h_DATA)
  h_TTcc   = changeMCbins( getPreFitMCs(fCombine, ['Y2018', 'Y2017', 'Y2016noHIPM', 'Y2016HIPM'], cutName,  'TT+cc'), h_DATA)
  h_TTbb   = changeMCbins( getPreFitMCs(fCombine, ['Y2018', 'Y2017', 'Y2016noHIPM', 'Y2016HIPM'], cutName,  'TT+bb'), h_DATA)

  if "sng_4j" in cutName:
    h_QCD    = changeMCbins( getPreFitMCs(fCombine, ['Y2018', 'Y2017', 'Y2016noHIPM', 'Y2016HIPM'], cutName,    'QCD'), h_DATA)
    hNames = ["histo_DATA", "histo_QCD", "histo_Others", "histo_ST", "histo_TT+jj", "histo_TT+cc", "histo_TT+bb"]
    histos = [h_DATA, h_QCD, h_Others, h_ST, h_TTjj, h_TTcc, h_TTbb]
  else:
    hNames = ["histo_DATA", "histo_Others", "histo_ST", "histo_TT+jj", "histo_TT+cc", "histo_TT+bb"]
    histos = [h_DATA, h_Others, h_ST, h_TTjj, h_TTcc, h_TTbb]
    

  saveHistos(fOut, cutName, varName, hNames, histos)


def mergeHistos(histos):
  out_histo = None
  for histo in histos:
    if out_histo == None:
      out_histo = histo.Clone(histo.GetName() + "_merged")
    else:
      out_histo.Add(histo)

  return out_histo



if __name__ == '__main__':
  # !! SAVE !!
  fOutLow = ROOT.TFile("results_run2_PreFit_Low.root", "RECREATE")
  fOutHigh = ROOT.TFile("results_run2_PreFit_High.root", "RECREATE")
  #
  saveHistos_CHToCB(fOutLow, fCombineLow, "sng_4j_eleCH_2b", "DNN_Low_mass")
  saveHistos_CHToCB(fOutLow, fCombineLow, "sng_4j_muCH_2b",  "DNN_Low_mass")
  saveHistos_CHToCB(fOutHigh, fCombineHigh, "sng_4j_eleCH_2b", "DNN_High_mass")
  saveHistos_CHToCB(fOutHigh, fCombineHigh, "sng_4j_muCH_2b",  "DNN_High_mass")

  saveHistos_CHToCB(fOutLow, fCombineLow, "dbl_4j_ee", "3_4rd_leading_b_disc")
  saveHistos_CHToCB(fOutLow, fCombineLow, "dbl_4j_em", "3_4rd_leading_b_disc")
  saveHistos_CHToCB(fOutLow, fCombineLow, "dbl_4j_me", "3_4rd_leading_b_disc")
  saveHistos_CHToCB(fOutLow, fCombineLow, "dbl_4j_mm", "3_4rd_leading_b_disc")

  saveHistos_CHToCB(fOutHigh, fCombineLow, "dbl_4j_ee", "3_4rd_leading_b_disc")
  saveHistos_CHToCB(fOutHigh, fCombineLow, "dbl_4j_em", "3_4rd_leading_b_disc")
  saveHistos_CHToCB(fOutHigh, fCombineLow, "dbl_4j_me", "3_4rd_leading_b_disc")
  saveHistos_CHToCB(fOutHigh, fCombineLow, "dbl_4j_mm", "3_4rd_leading_b_disc")

  #saveMergedHistos_CHToCB(fOut, ["sng_4j_eleCH_2b", "sng_4j_muCH_2b"], "DNN_Low_mass",  "sng_4j_eleORmuCH_2b")
  #saveMergedHistos_CHToCB(fOut, ["sng_4j_eleCH_2b", "sng_4j_muCH_2b"], "DNN_High_mass", "sng_4j_eleORmuCH_2b")
  #saveMergedHistos_CHToCB(fOut, ["dbl_4j_ee", "dbl_4j_em", "dbl_4j_me", "dbl_4j_mm"], "3_4rd_leading_b_disc", "dbl_4j_eeORmmORemORme_offZ")
  

