#include "TLegend.h"
#include "TCanvas.h"
#include "TFile.h"
#include "TH1F.h"
#include "TStyle.h"
#include "TPad.h"
import os
import ROOT
from ROOT import TLegend, TCanvas, TFile, TH1F, TPad, gPad, gStyle, kBlue, kGreen, kMagenta, kWhite, kBlack
import numpy as np


def DrawNuisances(inputRootFile, inputRootFile_MC, histoNominal, histo_up, histo_down, histoMC, legendName, varName, outputDirPlots = "./", drawYields = "0", drawMC = "0", custom_max_ratio=None, year=''):
  
  gStyle.SetOptStat(0)
  
  gStyle.SetPadTopMargin(0.21)

  import LatinoAnalysis.ShapeAnalysis.tdrStyle as tdrStyle
  tdrStyle.setTDRStyle()
  ROOT.TGaxis.SetExponentOffset(-0.06, 0.00,"y")
  
  cc = TCanvas("cc","",800,600)
  
  tfile = TFile (inputRootFile,"READ")
 
  hNominal = tfile.Get(histoNominal)
  #debug
  if not hNominal:
    print(histoNominal)

  hNominal.SetTitle("")
  hUp = tfile.Get(histo_up)
  hDo = tfile.Get(histo_down)
  if drawMC == "1":
    tfile_MC = TFile (inputRootFile_MC,"READ")
    hNominal_MC = tfile_MC.Get(histoMC)
 
  hNominal.SetLineColor(kBlue)
  hNominal.SetLineWidth(5)
 
  hUp.SetLineColor(kGreen+2)
  hUp.SetLineWidth(5)
  hUp.SetLineStyle(3)
  
  hDo.SetLineColor(kMagenta)
  hDo.SetLineWidth(5)
  hDo.SetLineStyle(2)

  if drawMC == "1":
    hNominal_MC.SetLineColorAlpha(kBlack, 0.5)
    hNominal_MC.SetLineWidth(5)
    hNominal_MC.SetLineStyle(2)
  
  ymax = hNominal.GetMaximum()
  if hUp.GetMaximum() > ymax:
    ymax = hUp.GetMaximum()
  if hDo.GetMaximum() > ymax:
    ymax = hDo.GetMaximum()

  if drawMC == "1":
    if hNominal_MC.GetMaximum() > ymax:
      ymax = hNominal_MC.GetMaximum()
  ymax *= 1.2
 
  hNominal.GetYaxis().SetRangeUser(0,ymax*1.2)
  hNominal.GetYaxis().SetTitle("Events")
  hNominal.GetYaxis().SetTitleOffset(1.2)
  hNominal.GetYaxis().SetTitleSize(0.05)


  #BHO
  hNominal.GetXaxis().SetLabelSize(0.)
 
  hNominal.Draw("e histo")
  hUp.Draw("histo same")
  hDo.Draw("histo same")
  if drawMC == "1":
    hNominal_MC.Draw("histo same")
  
  leg = TLegend(0.4,0.70,0.95,0.85)
  #leg = TLegend(0.65,0.15)
  leg.SetTextFont(42)
  leg.SetLineColor(0)
  leg.SetShadowColor(0)
  leg.SetBorderSize(0)
  leg.SetFillColor(kWhite)
  if drawYields == "1":
    legString = ""
    legString = "%s: %4.2f"%(histoNominal, hNominal.Integral())
    leg.AddEntry(hNominal,legString,"l")
    legString = "%s: %4.2f (%4.2f %%)"%(histo_up, hUp.Integral(), 100 * (hUp.Integral() - hNominal.Integral()) / hNominal.Integral())
    leg.AddEntry(hUp,legString,"l")
    legString = "%s: %4.2f (%4.2f %%)"%(histo_down, hDo.Integral(), 100 * (hDo.Integral() - hNominal.Integral()) / hNominal.Integral())
    leg.AddEntry(hDo,legString,"l")

    if drawMC == "1":
      legString = "%s: %4.2f (%4.2f %%)"%(histoMC, hNominal_MC.Integral(), 100 * (hNominal_MC.Integral() - hNominal.Integral()) / hNominal.Integral())
      leg.AddEntry(hNominal_MC,legString,"l")
  
  else:
    legString = ""
    legString = "%s, nominal"%(legendName)
    leg.AddEntry(hNominal,legString,"l")
    legString = "%s, up"%(legendName)
    leg.AddEntry(hUp,legString,"l")
    legString = "%s, down"%(legendName)
    leg.AddEntry(hDo,legString,"l")

    if drawMC == "1":
      legString = "%s, nominal"%(legendName)
      leg.AddEntry(hNominal_MC,legString,"l")
  
 
  leg.Draw()
  
  gPad.SetGrid()
  
  
  #---- ratio plot
  ccRatio = TCanvas("ccRatio","",800,600)
  hReferenceRatio = hNominal.Clone("Reference")
  hReferenceRatio.SetMaximum(1.1)
  hReferenceRatio.SetMinimum(0.9)
  #hReferenceRatio.SetLineColor(kBlue)
  hReferenceRatio.SetLineWidth(0)
  hRatioCenter = hNominal.Clone("Center")
  
  for iBin in range(hReferenceRatio.GetNbinsX()):
 #   if (1./hReferenceRatio.GetBinContent(iBin+1) != 0) hReferenceRatio.SetBinError  (iBin+1, 1./hReferenceRatio.GetBinContent(iBin+1) * hReferenceRatio.GetBinError(iBin+1))
   hReferenceRatio.SetBinError(iBin+1, 0.)
   hReferenceRatio.SetBinContent(iBin+1, 1.)
   hRatioCenter.SetBinError(iBin+1, 0.)
   hRatioCenter.SetBinContent(iBin+1, 1.)
  
  hRatioUp = hUp.Clone("Up")
  hRatioDo = hDo.Clone("Do")

  if drawMC == "1":
    hRatioMC = hNominal_MC.Clone("MC")
  
  max_ratio = 1.5
  ratios = []
  for iBin in range(hReferenceRatio.GetNbinsX()):
    ratio = 1
    den = hNominal.GetBinContent(iBin+1)
    den_error = hNominal.GetBinError(iBin+1)
    if den != 0:
      ratio = hRatioUp.GetBinContent(iBin+1) / den
    hRatioUp.SetBinContent(iBin+1, ratio)
    if den != 0 and hRatioUp.GetBinContent(iBin+1):
      ratio_error = ratio * ( den_error**2 / den**2 + hRatioUp.GetBinError(iBin+1)**2 / hUp.GetBinContent(iBin+1)**2 )**(0.5)
    else:
      ratio_error = 0.0
    hRatioUp.SetBinError(iBin+1, 0.0)
    #print("debug: ", ratio_error)
    hReferenceRatio.SetBinError(iBin+1, ratio_error)
 #    if (den != 0) hRatioUp.SetBinError  (iBin+1, 1./den * hRatioUp.GetBinError(iBin+1))
    ratios.append(ratio)
  hRatioUp.SetLineColor(kGreen+2)
  hRatioUp.SetLineWidth(5)
  
  for iBin in range(hReferenceRatio.GetNbinsX()):
    ratio = 1
    den = hNominal.GetBinContent(iBin+1)
    den_error = hNominal.GetBinError(iBin+1)
    if (den != 0):
      ratio = hRatioDo.GetBinContent(iBin+1) / den
    
    hRatioDo.SetBinContent(iBin+1, ratio)
    if den != 0 and hRatioDo.GetBinContent(iBin+1) != 0:
      ratio_error = ratio * ( den_error**2 / den**2 + hRatioDo.GetBinError(iBin+1)**2 / hDo.GetBinContent(iBin+1)**2 )**(0.5)
    else:
      ratio_error = 0.0
    #print("debug: ", ratio_error)
    hRatioDo.SetBinError(iBin+1, 0.0)
    if ratio_error > hReferenceRatio.GetBinError(iBin+1):
      hReferenceRatio.SetBinError(iBin+1, ratio_error)
    #    if (den != 0) hRatioDo.SetBinError  (iBin+1, 1./den * hRatioDo.GetBinError(iBin+1))
    ratios.append(ratio)
  hRatioDo.SetLineColor(kMagenta)
  hRatioDo.SetLineWidth(5)
  
  if drawMC == "1":
    for iBin in range(hReferenceRatio.GetNbinsX()):
      ratio = 1
      den = hNominal.GetBinContent(iBin+1)
      if (den != 0):
        ratio = hRatioMC.GetBinContent(iBin+1) / den
      
      hRatioMC.SetBinContent(iBin+1, ratio)
      hRatioMC.SetBinError(iBin+1, 0.)
      #    if (den != 0) hRatioMC.SetBinError  (iBin+1, 1./den * hRatioMC.GetBinError(iBin+1))
      if max_ratio < ratio:
        max_ratio = ratio
    hRatioMC.SetLineColor(kBlack)
    hRatioMC.SetLineWidth(5)
  
  hRatioCenter.SetLineColor(kBlue)
  hRatioCenter.SetLineWidth(5)

  hReferenceRatio.Draw()
  hRatioCenter.Draw("same")
  hRatioUp.Draw("same")
  hRatioDo.Draw("same")
  if drawMC == "1":
    hRatioMC.Draw("same")

  leg.Draw() 
  gPad.SetGrid()
  
  
  name = ""
  # name = Form ("%s/cratio_%s.png", outputDirPlots, histo_up)
  # ccRatio.SaveAs( name.Data() )
  # name = Form ("%s/cc_%s.png", outputDirPlots, histo_up)
  # cc.SaveAs( name.Data() )
 
  ccFull = TCanvas("ccFull","",800,800)
  pad1   = TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
  pad2   = TPad("pad2", "pad2", 0, 0.0, 1, 0.3)
 
  pad1.SetTopMargin(0.1)
  pad1.SetBottomMargin(0.02)
  pad1.SetFrameFillStyle(4000)
  pad1.Draw()
 
  pad2.SetTopMargin(0.05)
  pad2.SetBottomMargin(0.35)
  pad2.Draw()
 
  pad1.cd()
  
  hNominal.Draw("histo e")
  hUp.Draw("histo same")
  hDo.Draw("histo same")
  if drawMC == "1":
    hNominal_MC.Draw("histo e same")
 
  leg.Draw() 
  gPad.SetGrid()
 
  pad2.cd()
 
  hReferenceRatio.Draw()

  max_ratio = np.quantile(np.array([ abs(1-ratio) for ratio in ratios ]), 0.90)
  rounded_max_ratio = int( 100. * (1+ max(2.0*max_ratio, 0.02) ) ) / 100.
  if custom_max_ratio == None:
    max_ratio_ = rounded_max_ratio
    min_ratio_ = 1./rounded_max_ratio
  else:
    max_ratio_ = custom_max_ratio
    min_ratio_ = 1./custom_max_ratio
    
  hReferenceRatio.GetYaxis().SetRangeUser(min_ratio_, max_ratio_)
  hReferenceRatio.GetYaxis().SetNdivisions(5)
  #BHO
  hReferenceRatio.GetYaxis().SetLabelSize(0.08)
  hReferenceRatio.GetYaxis().SetTitleOffset(0.6)
  hReferenceRatio.GetYaxis().SetTitleSize(0.1)
  hReferenceRatio.GetYaxis().SetTitle("Ratio")
  hReferenceRatio.GetXaxis().SetLabelSize(0.08)
  hReferenceRatio.GetXaxis().SetTitle(varName)
  hReferenceRatio.GetXaxis().SetTitleSize(0.1)
  hReferenceRatio.GetXaxis().SetTitleOffset(1)
  hReferenceRatio.SetFillColor(12)
  hReferenceRatio.SetFillStyle(3004)
  hReferenceRatio.Draw("E2")

  hRatioCenter.Draw("same")
  hRatioUp.Draw("same")
  hRatioDo.Draw("same")
  if drawMC == "1":
    hRatioMC.Draw("same")

  leg_ratio = TLegend(0.55,0.82,0.70,0.92)
  #leg_ratio = TLegend(0.15,0.10)
  leg_ratio.SetTextFont(42)
  #leg_ratio.SetLineColor(0)
  #leg_ratio.SetShadowColor(0)
  leg_ratio.SetBorderSize(1)
  leg_ratio.SetFillColor(kWhite)
  leg_ratio.AddEntry(hReferenceRatio,"Stat. unc.","f")
  leg_ratio.Draw()

  gPad.SetGrid()

  import CMS_lumi as CMS_lumi

  CMS_lumi.lumi_13TeV = 'L = 59.74/fb'
  #CMS_lumi.lumi_13TeV = 'L = 137.2/fb'
  CMS_lumi.sqrtS = '#sqrt{s} = 13 TeV'
  CMS_lumi.extraText = " simulation"
  CMS_lumi.writeExtraText = 1
  #CMS_lumi.lumiTextOffset = 0.4
  #CMS_lumi.cmsTextOffset  = 0.3

  #CMS_lumi.extraOverCmsTextSize = 0.96
  #CMS_lumi.cmsTextSize      = 0.75
  CMS_lumi.relPosX = 0.12
  #CMS_lumi.relPosX = 0.12
  CMS_lumi.CMS_lumi(pad1, 4, 0)



  out_file_name   = '/'.join([year, histo_up.replace("Up","")])
  out_folder_name = '/'.join(out_file_name.split('/')[:-1])

  if not os.path.exists(out_folder_name):
    os.makedirs(out_folder_name)

  name = "%s.png"%(out_file_name)
  ccFull.SaveAs( name )
  name = "%s.pdf"%(out_file_name)
  ccFull.SaveAs( name )
  name = "%s.root"%(out_file_name)
  ccFull.SaveAs( name )
 
  hNominal.GetYaxis().SetRangeUser(0.01,ymax*10.)
  pad1.SetLogy()  
 
  name = "%s_log.png"%(out_file_name)
  ccFull.SaveAs( name )
  name = "%s_log.pdf"%(out_file_name)
  ccFull.SaveAs( name )
  name = "%s_log.root"%(out_file_name)
  ccFull.SaveAs( name )





