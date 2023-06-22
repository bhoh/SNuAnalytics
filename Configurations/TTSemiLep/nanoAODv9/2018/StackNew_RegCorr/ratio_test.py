import ROOT
import numpy as np
import root_numpy as rnp
from array import array

f1  = ROOT.TFile("rootFile_2018_SKIM9_RegCorr/hadd.root", "READ")
f2 = ROOT.TFile("../StackNew_comb/rootFile_2018_SKIM9_final/hadd.root", "READ")


def testKS(h1, h2):
  d = h1.KolmogorovTest(h2, "D")
  return d

def addHist(sample_list, base_dir):
  h = None
  
  # different root file by base_dir
  if '###final:' in base_dir:
      f = f2
  else:
      f = f1

  for name in sample_list:
      histName = base_dir.split(":")[-1] + '/' + name
      if h == None:
          h = f.Get(histName).Clone()
      else:
          h.Add(f.Get(histName))
  return h



def drawGraph(canvas, x_name, legend1, legend2, legend3, ratio1, ratio2, ratio3, histo1, histo2, histo3):
  canvas.Clear()
  canvas.SetGrid()
  n1, n2, n3 = 0, 0, 0
  x1, x2, x3, y1, y2, y3 = array( 'd' ), array( 'd' ), array( 'd' ), array( 'd' ), array( 'd' ), array( 'd' )
  for i in range( len(ratio1) ):
    if ratio1[i] > 0:
      n1 += 1
      x1.append( histo1.GetXaxis().GetBinCenter(i+1) )
      y1.append( ratio1[i] )
  
  for i in range( len(ratio2) ):
    if ratio2[i] > 0:
      n2 += 1
      x2.append( histo2.GetXaxis().GetBinCenter(i+1) )
      y2.append( ratio2[i] )

  # include third graph
  if (ratio3 is not None) and (histo3 is not None):
    for i in range( len(ratio3) ):
      if ratio3[i] > 0:
        n3 += 1
        x3.append( histo3.GetXaxis().GetBinCenter(i+1) )
        y3.append( ratio3[i] )

 
  gr1 = ROOT.TGraph( n1, x1, y1 )
  gr1.SetLineColor( ROOT.kRed )
  gr1.SetLineWidth( 4 )
  gr1.SetMarkerColor( ROOT.kBlack )
  gr1.SetMarkerStyle( 21 )
  gr1.SetMarkerSize( 0 )
  gr1.SetTitle( '' )
  gr1.GetXaxis().SetTitle( x_name )
  gr1.GetYaxis().SetTitle( 'Data / MC' )
  gr1.GetHistogram().SetMaximum(2.5)
  gr1.GetHistogram().SetMinimum(0.5)
  gr1.Draw( 'ACP' )
  
  gr2 = ROOT.TGraph( n2, x2, y2 )
  gr2.SetLineColor( ROOT.kBlue )
  gr2.SetLineWidth( 4 )
  gr2.SetMarkerColor( ROOT.kBlack )
  gr2.SetMarkerStyle( 21 )
  gr2.SetMarkerSize( 0 )
  gr2.Draw( 'CP' )

  # include third graph
  if (ratio3 is not None) and (histo3 is not None):
    gr3 = ROOT.TGraph( n3, x3, y3 )
    gr3.SetLineColor( ROOT.kGreen )
    gr3.SetLineWidth( 4 )
    gr3.SetMarkerColor( ROOT.kBlack )
    gr3.SetMarkerStyle( 21 )
    gr3.SetMarkerSize( 0 )
    gr3.Draw( 'CP' )

  # stat error band
  hRef = histo1.Clone()
  hRef.SetFillColor(12)
  hRef.SetFillStyle(3004)
  for iBin in range(hRef.GetNbinsX()):
      error1   = histo1.GetBinError(iBin+1)
      content1 = histo1.GetBinContent(iBin+1)
      error2   = histo2.GetBinError(iBin+1)
      content2 = histo2.GetBinContent(iBin+1)

      SR = lambda x,y: (x**2 + y**2)**(0.5)
      error = SR(error1/content1 if content1 > 0 else 0, error2/content2 if content2 > 0 else 0)
      print(error)
      hRef.SetBinError(iBin+1,   error)
      hRef.SetBinContent(iBin+1, 1.)
  hRef.Draw("E2 same")

  legend = ROOT.TLegend(0.50,0.65,0.9,0.9)
  legend.AddEntry(gr1, legend1, "lp")
  legend.AddEntry(gr2, legend2, "lp")
  # include third graph
  if (ratio3 is not None) and (histo3 is not None):
    legend.AddEntry(gr3, legend3, "lp")
  legend.AddEntry(hRef, "Stat. error", "f")

  legend.Draw("same")

  # TCanvas.Update() draws the frame, after which one can change it
  canvas.Update()
  canvas.GetFrame().SetBorderSize( 12 )
  canvas.Modified()
  canvas.Update()
  canvas.Print("bc_corr_ratio_test_2018.pdf")


def calcRatio(dir1, dir2, dir3, syst=None):
  samples_mc =  ["histo_TTLJ_jj", "histo_TTLJ_cc", "histo_TTLJ_bj", "histo_TTLJ_bb",]
  samples_mc += ["histo_TTLL_jj", "histo_TTLL_cc", "histo_TTLL_bj", "histo_TTLL_bb",]
  samples_mc += ["histo_ST", "histo_Wjets", "histo_DY", "histo_QCD", "histo_TTZjets", "histo_TTWjets", "histo_WW", "histo_WZ", "histo_ZZ", "histo_ttH"]
  
  if syst is not None:
    samples_mc1 = map(lambda hName: hName + "_" + syst[0] if not "histo_QCD" in hName else hName, samples_mc) if syst[0] is not None else samples_mc
    samples_mc2 = map(lambda hName: hName + "_" + syst[1] if not "histo_QCD" in hName else hName, samples_mc) if syst[1] is not None else samples_mc
    samples_mc3 = map(lambda hName: hName + "_" + syst[2] if not "histo_QCD" in hName else hName, samples_mc) if syst[2] is not None else samples_mc
  else:
    samples_mc1 = samples_mc
    samples_mc2 = samples_mc
    samples_mc3 = samples_mc
  print(samples_mc1)
  print(samples_mc2)
  print(samples_mc3)

  samples_data = ["histo_DATA"]
  h1 = addHist(samples_mc1, dir1)
  # flip dir1 and dir2 if there's 'jes' or 'noSmear'
  h2 = addHist(samples_data, dir2 if 'jes' in dir1 else dir2 if 'noSmear' in dir1 else dir1)
  h3 = addHist(samples_mc2, dir2)
  # flip dir2 and dir1 if there's 'jes' or 'noSmear'
  h4 = addHist(samples_data, dir1 if 'jes' in dir2 else dir1 if 'noSmear' in dir2 else dir2)
  if dir3 is not None:
    h5 = addHist(samples_mc3, dir3)
    # flip dir3 and dir2 if there's 'jes' or 'noSmear'
    h6 = addHist(samples_data, dir1 if 'jes' in dir3 else dir1 if 'noSmear' in dir3 else dir3)
  
  #ratio
  ratio1 = rnp.hist2array(h2, copy=False) / rnp.hist2array(h1, copy=False)
  ratio2 = rnp.hist2array(h4, copy=False) / rnp.hist2array(h3, copy=False)
  if dir3 is not None:
    ratio3 = rnp.hist2array(h6, copy=False) / rnp.hist2array(h5, copy=False)
  
  
  #print(ratio1)
  #print(ratio2)
  if dir3 is not None:
    #print(ratio3)
    pass

  if dir3 is not None:
    out = (ratio1, ratio2, ratio3, h1, h3, h5)
  else:
    out = (ratio1, ratio2, None, h1, h3, None)

  return out


if __name__ == "__main__":
  baseDir_noRegCorr_had_top1 = "sng_4j_eleORmuCH_2b/hadronic_top_b_jet_bRegCorr/"
  baseDir_noRegCorr_had_top2 = "sng_4j_eleORmuCH_2b/hadronic_top_b_jet_noRegCorr/"
  baseDir_noRegCorr_lep_top1 = "sng_4j_eleORmuCH_2b/leptonic_top_b_jet_bRegCorr/"
  baseDir_noRegCorr_lep_top2 = "sng_4j_eleORmuCH_2b/leptonic_top_b_jet_noRegCorr/"
  baseDir_noRegCorr_Wc1 = "sng_4j_eleORmuCH_2b/W_c_jet_cRegCorr/"
  baseDir_noRegCorr_Wc2 = "sng_4j_eleORmuCH_2b/W_c_jet_noRegCorr/"
  
  baseDir_jesTotalNoFlavor_had_top1 = "sng_4j_eleORmuCH_2b/hadronic_top_b_jet_bRegCorr/"
  baseDir_jesTotalNoFlavor_had_top2 = "sng_4j_eleORmuCH_2b/hadronic_top_b_jet_jesTotalNoFlavorUp/"
  baseDir_jesTotalNoFlavor_had_top3 = "sng_4j_eleORmuCH_2b/hadronic_top_b_jet_jesTotalNoFlavorDown/"

  baseDir_jesTotalNoFlavor_lep_top1 = "sng_4j_eleORmuCH_2b/leptonic_top_b_jet_bRegCorr/"
  baseDir_jesTotalNoFlavor_lep_top2 = "sng_4j_eleORmuCH_2b/leptonic_top_b_jet_jesTotalNoFlavorUp/"
  baseDir_jesTotalNoFlavor_lep_top3 = "sng_4j_eleORmuCH_2b/leptonic_top_b_jet_jesTotalNoFlavorDown/"

  baseDir_jesTotalNoFlavor_Wc1 = "sng_4j_eleORmuCH_2b/W_c_jet_cRegCorr/"
  baseDir_jesTotalNoFlavor_Wc2 = "sng_4j_eleORmuCH_2b/W_c_jet_jesTotalNoFlavorUp/"
  baseDir_jesTotalNoFlavor_Wc3 = "sng_4j_eleORmuCH_2b/W_c_jet_jesTotalNoFlavorDown/"

  #baseDir2 = "sng_4j_eleORmuCH_2b/W_c_jet_jesFlavorQCDDown/"
  baseDir_jesFlavorQCD_had_top1 = "sng_4j_eleORmuCH_2b/hadronic_top_b_jet_bRegCorr/"
  baseDir_jesFlavorQCD_had_top2 = "sng_4j_eleORmuCH_2b/hadronic_top_b_jet_jesFlavorQCDUp/"
  baseDir_jesFlavorQCD_had_top3 = "sng_4j_eleORmuCH_2b/hadronic_top_b_jet_jesFlavorQCDDown/"

  baseDir_jesFlavorQCD_lep_top1 = "sng_4j_eleORmuCH_2b/leptonic_top_b_jet_bRegCorr/"
  baseDir_jesFlavorQCD_lep_top2 = "sng_4j_eleORmuCH_2b/leptonic_top_b_jet_jesFlavorQCDUp/"
  baseDir_jesFlavorQCD_lep_top3 = "sng_4j_eleORmuCH_2b/leptonic_top_b_jet_jesFlavorQCDDown/"

  baseDir_jesFlavorQCD_Wc1 = "sng_4j_eleORmuCH_2b/W_c_jet_cRegCorr/"
  baseDir_jesFlavorQCD_Wc2 = "sng_4j_eleORmuCH_2b/W_c_jet_jesFlavorQCDUp/"
  baseDir_jesFlavorQCD_Wc3 = "sng_4j_eleORmuCH_2b/W_c_jet_jesFlavorQCDDown/"

  baseDir_noRegCorr_1st_b_jet1 = "dbl_4j_eeORmmORemORme_offZ/1st_leading_jet_pt_bRegCorr/"
  baseDir_noRegCorr_1st_b_jet2 = "dbl_4j_eeORmmORemORme_offZ/1st_leading_jet_pt_noRegCorr/"

  baseDir_noRegCorr_2nd_b_jet1 = "dbl_4j_eeORmmORemORme_offZ/2nd_leading_jet_pt_bRegCorr/"
  baseDir_noRegCorr_2nd_b_jet2 = "dbl_4j_eeORmmORemORme_offZ/2nd_leading_jet_pt_noRegCorr/"

  baseDir_jesTotalNoFlavor_1st_b_jet1 = "dbl_4j_eeORmmORemORme_offZ/1st_leading_jet_pt_bRegCorr/"
  baseDir_jesTotalNoFlavor_1st_b_jet2 = "dbl_4j_eeORmmORemORme_offZ/1st_leading_jet_pt_jesTotalNoFlavorUp/"
  baseDir_jesTotalNoFlavor_1st_b_jet3 = "dbl_4j_eeORmmORemORme_offZ/1st_leading_jet_pt_jesTotalNoFlavorDown/"

  baseDir_jesTotalNoFlavor_2nd_b_jet1 = "dbl_4j_eeORmmORemORme_offZ/2nd_leading_jet_pt_bRegCorr/"
  baseDir_jesTotalNoFlavor_2nd_b_jet2 = "dbl_4j_eeORmmORemORme_offZ/2nd_leading_jet_pt_jesTotalNoFlavorUp/"
  baseDir_jesTotalNoFlavor_2nd_b_jet3 = "dbl_4j_eeORmmORemORme_offZ/2nd_leading_jet_pt_jesTotalNoFlavorDown/"

  baseDir_jesFlavorQCD_1st_b_jet1 = "dbl_4j_eeORmmORemORme_offZ/1st_leading_jet_pt_bRegCorr/"
  baseDir_jesFlavorQCD_1st_b_jet2 = "dbl_4j_eeORmmORemORme_offZ/1st_leading_jet_pt_jesFlavorQCDUp/"
  baseDir_jesFlavorQCD_1st_b_jet3 = "dbl_4j_eeORmmORemORme_offZ/1st_leading_jet_pt_jesFlavorQCDDown/"

  baseDir_jesFlavorQCD_2nd_b_jet1 = "dbl_4j_eeORmmORemORme_offZ/2nd_leading_jet_pt_bRegCorr/"
  baseDir_jesFlavorQCD_2nd_b_jet2 = "dbl_4j_eeORmmORemORme_offZ/2nd_leading_jet_pt_jesFlavorQCDUp/"
  baseDir_jesFlavorQCD_2nd_b_jet3 = "dbl_4j_eeORmmORemORme_offZ/2nd_leading_jet_pt_jesFlavorQCDDown/"

  baseDir_noRegCorr_noSmear_had_top1 = "sng_4j_eleORmuCH_2b/hadronic_top_b_jet_noRegCorr_noSmear/"
  baseDir_noRegCorr_noSmear_had_top2 = "sng_4j_eleORmuCH_2b/hadronic_top_b_jet_noRegCorr/"
  baseDir_noRegCorr_noSmear_lep_top1 = "sng_4j_eleORmuCH_2b/leptonic_top_b_jet_noRegCorr_noSmear/"
  baseDir_noRegCorr_noSmear_lep_top2 = "sng_4j_eleORmuCH_2b/leptonic_top_b_jet_noRegCorr/"
  baseDir_noRegCorr_noSmear_Wc1 = "sng_4j_eleORmuCH_2b/W_c_jet_noRegCorr_noSmear/"
  baseDir_noRegCorr_noSmear_Wc2 = "sng_4j_eleORmuCH_2b/W_c_jet_noRegCorr/"
  baseDir_noRegCorr_noSmear_1st_b_jet1 = "dbl_4j_eeORmmORemORme_offZ/1st_leading_jet_pt_noRegCorr_noSmear/"
  baseDir_noRegCorr_noSmear_1st_b_jet2 = "dbl_4j_eeORmmORemORme_offZ/1st_leading_jet_pt_noRegCorr/"
  baseDir_noRegCorr_noSmear_2nd_b_jet1 = "dbl_4j_eeORmmORemORme_offZ/2nd_leading_jet_pt_noRegCorr_noSmear/"
  baseDir_noRegCorr_noSmear_2nd_b_jet2 = "dbl_4j_eeORmmORemORme_offZ/2nd_leading_jet_pt_noRegCorr/"


  baseDir_RegCorr_noSmear_had_top1 = "sng_4j_eleORmuCH_2b/hadronic_top_b_jet_bRegCorr_noSmear/"
  baseDir_RegCorr_noSmear_had_top2 = "sng_4j_eleORmuCH_2b/hadronic_top_b_jet_bRegCorr/"
  baseDir_RegCorr_noSmear_lep_top1 = "sng_4j_eleORmuCH_2b/leptonic_top_b_jet_bRegCorr_noSmear/"
  baseDir_RegCorr_noSmear_lep_top2 = "sng_4j_eleORmuCH_2b/leptonic_top_b_jet_bRegCorr/"
  baseDir_RegCorr_noSmear_Wc1 = "sng_4j_eleORmuCH_2b/W_c_jet_cRegCorr_noSmear/"
  baseDir_RegCorr_noSmear_Wc2 = "sng_4j_eleORmuCH_2b/W_c_jet_cRegCorr/"
  baseDir_RegCorr_noSmear_1st_b_jet1 = "dbl_4j_eeORmmORemORme_offZ/1st_leading_jet_pt_bRegCorr_noSmear/"
  baseDir_RegCorr_noSmear_1st_b_jet2 = "dbl_4j_eeORmmORemORme_offZ/1st_leading_jet_pt_bRegCorr/"
  baseDir_RegCorr_noSmear_2nd_b_jet1 = "dbl_4j_eeORmmORemORme_offZ/2nd_leading_jet_pt_bRegCorr_noSmear/"
  baseDir_RegCorr_noSmear_2nd_b_jet2 = "dbl_4j_eeORmmORemORme_offZ/2nd_leading_jet_pt_bRegCorr/"

  baseDir_noRegCorr_fitted_dijet_M1 = "###final:sng_4j_eleORmuCH_2b/fitted_dijet_M/"
  baseDir_noRegCorr_fitted_dijet_M2 = "sng_4j_eleORmuCH_2b/fitted_dijet_M/"

  baseDir_jesTotalNoFlavor_fitted_dijet_M1 = "###final:sng_4j_eleORmuCH_2b/fitted_dijet_M/"
  baseDir_jesTotalNoFlavor_fitted_dijet_M2 = "###final:sng_4j_eleORmuCH_2b/fitted_dijet_M/"
  baseDir_jesTotalNoFlavor_fitted_dijet_M3 = "###final:sng_4j_eleORmuCH_2b/fitted_dijet_M/"

  baseDir_jesFlavorQCD_fitted_dijet_M1 = "###final:sng_4j_eleORmuCH_2b/fitted_dijet_M/"
  baseDir_jesFlavorQCD_fitted_dijet_M2 = "###final:sng_4j_eleORmuCH_2b/fitted_dijet_M/"
  baseDir_jesFlavorQCD_fitted_dijet_M3 = "###final:sng_4j_eleORmuCH_2b/fitted_dijet_M/"

  baseDir_jer_fitted_dijet_M1 = "###final:sng_4j_eleORmuCH_2b/fitted_dijet_M/"
  baseDir_jer_fitted_dijet_M2 = "###final:sng_4j_eleORmuCH_2b/fitted_dijet_M/"
  baseDir_jer_fitted_dijet_M3 = "###final:sng_4j_eleORmuCH_2b/fitted_dijet_M/"

  c1 = ROOT.TCanvas( 'c1', 'A Simple Graph Example', 200, 10, 700, 500 )
  
  c1.Print("bc_corr_ratio_test_2018.pdf[")
  drawGraph(c1, "hadronic top b p_{T}", "b corr.", "no b corr.", None, *calcRatio(baseDir_noRegCorr_had_top1, baseDir_noRegCorr_had_top2, None))
  drawGraph(c1,  "leptonic top b p_{T}","b corr.", "no b corr.", None, *calcRatio(baseDir_noRegCorr_lep_top1, baseDir_noRegCorr_lep_top2, None))
  drawGraph(c1, "W c p_{T}", "c corr.", "no c corr.", None, *calcRatio(baseDir_noRegCorr_Wc1, baseDir_noRegCorr_Wc2, None))
  ##
  drawGraph(c1, "hadronic top b p_{T}", "b corr.", "jesTotalNoFlavorUp", "jesTotalNoFlavorDown", *calcRatio(baseDir_jesTotalNoFlavor_had_top1, baseDir_jesTotalNoFlavor_had_top2, baseDir_jesTotalNoFlavor_had_top3))
  drawGraph(c1, "leptonic top b p_{T}","b corr.", "jesTotalNoFlavorUp", "jesTotalNoFlavorDown", *calcRatio(baseDir_jesTotalNoFlavor_lep_top1, baseDir_jesTotalNoFlavor_lep_top2, baseDir_jesTotalNoFlavor_lep_top3))
  drawGraph(c1, "W c p_{T}", "c corr.", "jesTotalNoFlavorUp", "jesTotalNoFlavorDown", *calcRatio(baseDir_jesTotalNoFlavor_Wc1, baseDir_jesTotalNoFlavor_Wc2, baseDir_jesTotalNoFlavor_Wc3))
  ##
  drawGraph(c1, "hadronic top b p_{T}", "b corr.", "jesFlavorQCDUp", "jesFlavorQCDDown", *calcRatio(baseDir_jesFlavorQCD_had_top1, baseDir_jesFlavorQCD_had_top2, baseDir_jesFlavorQCD_had_top3))
  drawGraph(c1, "leptonic top b p_{T}", "b corr.", "jesFlavorQCDUp", "jesFlavorQCDDown", *calcRatio(baseDir_jesFlavorQCD_lep_top1, baseDir_jesFlavorQCD_lep_top2, baseDir_jesFlavorQCD_lep_top3))
  drawGraph(c1, "W c p_{T}", "c corr.", "jesFlavorQCDUp", "jesFlavorQCDDown", *calcRatio(baseDir_jesFlavorQCD_Wc1, baseDir_jesFlavorQCD_Wc2, baseDir_jesFlavorQCD_Wc3))
  #

  drawGraph(c1, "1st leading b jet p_{T}", "b corr.", "no b corr.", None, *calcRatio(baseDir_noRegCorr_1st_b_jet1, baseDir_noRegCorr_1st_b_jet2, None))
  drawGraph(c1, "2nd leading b jet p_{T}", "b corr.", "no b corr.", None, *calcRatio(baseDir_noRegCorr_2nd_b_jet1, baseDir_noRegCorr_2nd_b_jet2, None))
  drawGraph(c1, "1st leading b jet p_{T}", "b corr.", "jesTotalNoFlavorUp", "jesTotalNoFlavorDown", *calcRatio(baseDir_jesTotalNoFlavor_1st_b_jet1, baseDir_jesTotalNoFlavor_1st_b_jet2, baseDir_jesTotalNoFlavor_1st_b_jet3))
  drawGraph(c1, "2nd leading b jet p_{T}", "b corr.", "jesTotalNoFlavorUp", "jesTotalNoFlavorDown", *calcRatio(baseDir_jesTotalNoFlavor_2nd_b_jet1, baseDir_jesTotalNoFlavor_2nd_b_jet2, baseDir_jesTotalNoFlavor_2nd_b_jet3))
  drawGraph(c1, "1st leading b jet p_{T}", "b corr.", "jesFlavorQCDUp", "jesFlavorQCDDown", *calcRatio(baseDir_jesFlavorQCD_1st_b_jet1, baseDir_jesFlavorQCD_1st_b_jet2, baseDir_jesFlavorQCD_1st_b_jet3))
  drawGraph(c1, "2nd leading b jet p_{T}", "b corr.", "jesFlavorQCDUp", "jesFlavorQCDDown", *calcRatio(baseDir_jesFlavorQCD_2nd_b_jet1, baseDir_jesFlavorQCD_2nd_b_jet2, baseDir_jesFlavorQCD_2nd_b_jet3))
  #
  drawGraph(c1, "hadronic top b p_{T}", "no corr., no smear.", "no corr.", None, *calcRatio(baseDir_noRegCorr_noSmear_had_top1, baseDir_noRegCorr_noSmear_had_top2, None))
  drawGraph(c1, "leptonic top b p_{T}", "no corr., no smear.", "no corr.", None, *calcRatio(baseDir_noRegCorr_noSmear_lep_top1, baseDir_noRegCorr_noSmear_lep_top2, None))
  drawGraph(c1, "W c p_{T}", "no corr., no smear.", "no corr.", None, *calcRatio(baseDir_noRegCorr_noSmear_Wc1, baseDir_noRegCorr_noSmear_Wc2, None))
  drawGraph(c1, "1st leading b jet p_{T}", "no corr., no smear", "no corr.", None, *calcRatio(baseDir_noRegCorr_noSmear_1st_b_jet1, baseDir_noRegCorr_noSmear_1st_b_jet2, None))
  drawGraph(c1, "2nd leading b jet p_{T}", "no corr., no smear", "no corr.", None, *calcRatio(baseDir_noRegCorr_noSmear_2nd_b_jet1, baseDir_noRegCorr_noSmear_2nd_b_jet2, None))

  drawGraph(c1, "hadronic top b p_{T}", "corr., no smear.", "corr., smear.", None, *calcRatio(baseDir_RegCorr_noSmear_had_top1, baseDir_RegCorr_noSmear_had_top2, None))
  drawGraph(c1, "leptonic top b p_{T}", "corr., no smear.", "corr., smear.", None, *calcRatio(baseDir_RegCorr_noSmear_lep_top1, baseDir_RegCorr_noSmear_lep_top2, None))
  drawGraph(c1, "W c p_{T}",  "corr., no smear.", "corr., smear.", None, *calcRatio(baseDir_RegCorr_noSmear_Wc1, baseDir_RegCorr_noSmear_Wc2, None))
  drawGraph(c1, "1st leading b jet p_{T}", "corr., no smear.", "corr., smear.", None, *calcRatio(baseDir_RegCorr_noSmear_1st_b_jet1, baseDir_RegCorr_noSmear_1st_b_jet2, None))
  drawGraph(c1, "2nd leading b jet p_{T}", "corr., no smear.", "corr., smear.", None, *calcRatio(baseDir_RegCorr_noSmear_2nd_b_jet1, baseDir_RegCorr_noSmear_2nd_b_jet2, None))
  #
  drawGraph(c1, "M_{jj}", "b corr.", "no b corr.", None, *calcRatio(baseDir_noRegCorr_fitted_dijet_M1, baseDir_noRegCorr_fitted_dijet_M2, None))
  drawGraph(c1, "M_{jj}", "b corr.", "jesTotalNoFlavorUp", "jesTotalNoFlavorDown", *calcRatio(baseDir_jesTotalNoFlavor_fitted_dijet_M1, baseDir_jesTotalNoFlavor_fitted_dijet_M2, baseDir_jesTotalNoFlavor_fitted_dijet_M3, [None, "jesTotalNoFlavorUp", "jesTotalNoFlavorDown"]))
  drawGraph(c1, "M_{jj}", "b corr.", "jesFlavorQCDUp", "jesFlavorQCDDown", *calcRatio(baseDir_jesFlavorQCD_fitted_dijet_M1, baseDir_jesFlavorQCD_fitted_dijet_M2, baseDir_jesFlavorQCD_fitted_dijet_M3, [None, "jesFlavorQCDUp", "jesFlavorQCDDown"]))
  drawGraph(c1, "M_{jj}", "b corr.", "jerUp", "jerDown", *calcRatio(baseDir_jer_fitted_dijet_M1, baseDir_jer_fitted_dijet_M2, baseDir_jer_fitted_dijet_M3, [None, "jer_2018Up", "jer_2018Down"]))
  #
  c1.Print("bc_corr_ratio_test_2018.pdf]")
