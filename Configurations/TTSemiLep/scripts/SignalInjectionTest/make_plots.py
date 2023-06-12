import ROOT

ROOT.gStyle.SetOptStat(0)

import LatinoAnalysis.ShapeAnalysis.tdrStyle as tdrStyle
tdrStyle.setTDRStyle()
ROOT.TGaxis.SetExponentOffset(-0.06, 0.00,"y")

import CMS_lumi as CMS_lumi
                                      
CMS_lumi.lumi_13TeV = ''
CMS_lumi.lumi_13TeV = 'L = 137.6/fb'
CMS_lumi.sqrtS = '#sqrt{s} = 13 TeV'
CMS_lumi.extraText = " simulation"
CMS_lumi.writeExtraText = 1
#CMS_lumi.lumiTextOffset = 0.4
#CMS_lumi.cmsTextOffset  = 0.3
                                      
#CMS_lumi.extraOverCmsTextSize = 0.96
CMS_lumi.cmsTextSize      = CMS_lumi.cmsTextSize  * 0.75
CMS_lumi.lumiTextSize     = CMS_lumi.lumiTextSize * 0.75
CMS_lumi.relPosX = 0.12
#CMS_lumi.relPosX = 0.12

def getTrees(BR, mass):
  fChain = ROOT.TChain("tree_fit_sb")
  for seed in range(50):
    fileName = '/cms_scratch/bhoh/toys/fitDiagnostics{MASS}_{BR}_{SEED}.root'.format(BR=BR, MASS=mass, SEED=seed)
    fChain.Add(fileName)
  return fChain

def drawPlot(cc, ttree, BR, BR_inj, mass):
  pad1   = ROOT.TPad("pad1", "pad1", 0, 0, 1.0, 1.0)
  ROOT.gPad.SetGrid()
  pad1.SetTopMargin(0.11)
  pad1.SetBottomMargin(0.125)
  pad1.SetFrameFillStyle(4000)
  pad1.Draw()
  
  pad1.cd()

  t.Draw("(BR-{BR_INJ})/(((BR-{BR_INJ})>=0)*BRHiErr+((BR-{BR_INJ})<0)*BRLoErr)>>h(50,-10,10),fit_status==0".format(BR_INJ=BR_inj))
  h = ROOT.gROOT.FindObject("h")
  h.SetLineColor(ROOT.kBlack)
  h.GetXaxis().SetTitle("(BR_{fit}-BR_{inj})/BR_{err}")
  h.GetXaxis().SetTitleSize(0.035)
  h.GetXaxis().SetTitleOffset(1.5)
  h.GetYaxis().SetTitle("Number of toys")
  fitGaus = ROOT.TF1("gaus","gaus",-10,10)
  fitGaus.SetLineColor(ROOT.kBlue)
  fitGaus.SetLineWidth(3)
  h.Fit("gaus","","",-10, 10)
  gausParams      = fitGaus.GetParameters()
  gausParamErrors = fitGaus.GetParErrors()

  pt = ROOT.TPaveText(0.20,0.55,0.20,0.83,"NBNDC")
  if BR == "0":
    ptptr = pt.AddText("m_{{H+}} = {MASS} GeV".format(MASS=mass))
  else:
    ptptr = pt.AddText("m_{{H+}} = {MASS} GeV, {BR} CL_{{s}}".format(MASS=mass, BR=BR.replace("sigma","#sigma")))
  ptptr.SetTextColor(ROOT.kBlack)
  ptptr.SetTextSize(0.038)
  ptptr.SetTextAlign(11)
  if BR == "0":
    ptptr = pt.AddText("BR_{{inj}} = {BR}".format(BR=BR.replace("1sigma","#sigma")))
  else:
    ptptr = pt.AddText("BR_{{inj}} = {BR_INJ:.3g}".format(BR_INJ=float(BR_inj)))
  ptptr.SetTextColor(ROOT.kBlack)
  ptptr.SetTextSize(0.038)
  ptptr.SetTextAlign(11)

  ptptr = pt.AddText("Mean (hist.): %.2f"%(h.GetMean()))
  ptptr.SetTextColor(ROOT.kBlack)
  ptptr.SetTextSize(0.038)
  ptptr.SetTextAlign(11)
  ptptr = pt.AddText("Mean (fit.): %.2f #pm %.2f"%(gausParams[1],gausParamErrors[1]))
  ptptr.SetTextColor(ROOT.kBlue)
  ptptr.SetTextSize(0.038)
  ptptr.SetTextAlign(11)
  ptptr = pt.AddText("Sigma (hist.): %.2f"%(h.GetRMS()))
  ptptr.SetTextColor(ROOT.kBlack)
  ptptr.SetTextSize(0.038)
  ptptr.SetTextAlign(11)
  ptptr = pt.AddText("Sigma (fit.): %.2f #pm %.2f"%(gausParams[2],gausParamErrors[2]))
  ptptr.SetTextColor(ROOT.kBlue)
  ptptr.SetTextSize(0.038)
  ptptr.SetTextAlign(11)


  pt.Draw("same")

  ROOT.gStyle.SetOptFit(0000)
  h.Draw("same")

  CMS_lumi.CMS_lumi(pad1, 4, 0)
  
  cc.Update()
  cc.SaveAs("SignalInjection_test_mH{MASS}_BR{BR}.png".format(MASS=mass,BR=BR))
  cc.Print("SignalInjection_test.pdf")
  cc.Clear()

def getAsymResult(BR, mass):
  fname = "/cms_scratch/bhoh/toys/higgsCombineTest.AsymptoticLimits.mH{MASS}.root".format(MASS=mass)
  f     = ROOT.TFile(fname, "READ")
  t     = f.Get("limit")

  out_BR = None
  if BR == '0':
    out_BR = BR
  elif BR == '-1sigma':
    t.GetEntry(1)
    out_BR = t.limit
  elif BR == 'median':
    t.GetEntry(2)
    out_BR = t.limit
  elif BR == '1sigma':
    t.GetEntry(3)
    out_BR = t.limit
  elif BR == '0.01':
    out_BR = BR
  return str(out_BR)



cc = ROOT.TCanvas("cc","",800,600)
cc.Print("SignalInjection_test.pdf[")
for mass in ['75', '80', '85', '90', '100', '110', '120', '130', '140', '150', '160']:
  for BR in ['0','-1sigma','median','1sigma']:
#for mass in ['75']:
#  for BR in ['0','-1sigma','median','1sigma']:
#  for BR in ['0',]:
    t = getTrees(BR, mass)
    BR_inj = getAsymResult(BR, mass)
    drawPlot(cc,t, BR, BR_inj, mass)
cc.Print("SignalInjection_test.pdf]")
