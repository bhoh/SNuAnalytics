import ROOT
import sys


fitGaus1 = ROOT.TF1("gaus1","gaus",60,100)
fitGaus2 = ROOT.TF1("gaus2","gaus",60,100)


#mass = "080"
mass     = str( sys.argv[1] )
variable = str( sys.argv[2] )
histo_min = str( sys.argv[3] )
histo_max = str( sys.argv[4] )

if mass not in ["075", "080", "085", "090", "100", "110", "120", "130", "140", "150", "160"]:
  raise Exception("{MASS} is not in the list".format(MASS=mass))

fIn = "/xrootd/store/user/bhoh/Latino/HWWNano/Summer20UL16_106x_nAODv9_HIPM_Full2016v9/CHToCBLepton2016v9__CHToCBJetMETCorr2016v9__kinFitTTSemiLepV5__mvaTreeCHToCB/nanoLatino_CHToCB_M{MASS}__part*.root".format(MASS=mass)
#fIn = "/xrootd/store/user/bhoh/Latino/HWWNano/Summer20UL16_106x_nAODv9_noHIPM_Full2016v9/CHToCBLepton2016v9__CHToCBJetMETCorr2016v9__kinFitTTSemiLepV5__mvaTreeCHToCB/nanoLatino_CHToCB_M{MASS}__part*.root".format(MASS=mass)
#fIn = "/xrootd/store/user/bhoh/Latino/HWWNano/Summer20UL18_106x_nAODv9_Full2018v9/CHToCBLepton2018v9__CHToCBJetMETCorr2018v9__kinFitTTSemiLepV5__mvaTreeCHToCB/nanoLatino_CHToCB_M{MASS}__part*.root".format(MASS=mass)
#fIn = "/xrootd/store/user/bhoh/Latino/HWWNano/Summer20UL18_106x_nAODv9_Full2018v9/CHToCBLepton2018v9__CHToCBJetMETCorr2018v9__kinFitTTSemiLepV5__mvaTreeCHToCB/nanoLatino_CHToCB_M{MASS}__part*.root".format(MASS=mass)


#"root://cms-xrdr.private.lo:2094///xrd/store/user/bhoh/Latino/HWWNano//Summer20UL18_106x_nAODv9_Full2018v9/CHToCBLepton2018v9__CHToCBJetMETCorr2018v9__kinFitTTSemiLepV5__mvaTreeCHToCB//nanoLatino_CHToCB_M150__part0.root"

fChain = ROOT.TChain("Events")

fChain.Add(fIn)


ROOT.gStyle.SetOptStat(0)

import LatinoAnalysis.ShapeAnalysis.tdrStyle as tdrStyle
tdrStyle.setTDRStyle()
ROOT.TGaxis.SetExponentOffset(-0.06, 0.00,"y")

cc = ROOT.TCanvas("cc","",800,600)
pad1   = ROOT.TPad("pad1", "pad1", 0, 0, 1.0, 1.0)
ROOT.gPad.SetGrid()
pad1.SetTopMargin(0.11)
pad1.SetBottomMargin(0.125)
pad1.SetFrameFillStyle(4000)
pad1.Draw()

pad1.cd()


fChain.Draw("{VAR}>>h1(50,{MIN},{MAX})".format(VAR=variable,MIN=histo_min,MAX=histo_max),"({VAR}>0)*XSWeight".format(VAR=variable))
fChain.Draw("{VAR}_flavCorr>>h2(50,{MIN},{MAX})".format(VAR=variable,MIN=histo_min,MAX=histo_max),"({VAR}>0)*XSWeight".format(VAR=variable))
#
h1 = ROOT.gROOT.FindObject("h1")
h2 = ROOT.gROOT.FindObject("h2")
#
h1.SetLineColor(ROOT.kBlue)
h2.SetLineColor(ROOT.kRed)
#

h1.GetYaxis().SetTitle("a.u.")
if "top_mass" in variable:
  h1.GetXaxis().SetTitle("#it{M_{jjj}}")
  h1.GetYaxis().SetTitle("Events")
else:
  h1.GetXaxis().SetTitle("#it{M_{jj}}")
  h1.GetYaxis().SetTitle("Events")

yMax = h2.GetMaximum()
yMax = yMax if yMax > h1.GetMaximum() else h1.GetMaximum()
h1.GetYaxis().SetRangeUser(0, yMax * 1.2)
h2.GetYaxis().SetRangeUser(0, yMax * 1.2)

fitGaus1.SetLineColor(ROOT.kBlue)
fitGaus2.SetLineColor(ROOT.kRed)



# set fit range

h2.Fit("gaus2","","",h2.GetMean()-2*h2.GetRMS(), h2.GetMean()+2*h2.GetRMS())
h1.Fit("gaus1","","",h1.GetMean()-2*h1.GetRMS(), h1.GetMean()+2*h1.GetRMS())

gausParams1 = fitGaus1.GetParameters()
gausParams2 = fitGaus2.GetParameters()

fitRange1 = (gausParams1[1] - 2.0*gausParams1[2], gausParams1[1] + 2.0*gausParams1[2])
fitRange2 = (gausParams2[1] - 2.0*gausParams2[2], gausParams2[1] + 2.0*gausParams2[2])

h2.Fit("gaus2","","",fitRange2[0],fitRange2[1])
h1.Fit("gaus1","","",fitRange1[0],fitRange1[1])

gausParams1 = fitGaus1.GetParameters()
gausParams2 = fitGaus2.GetParameters()
fitRange3 = (gausParams1[1] - 1.5*gausParams1[2], gausParams1[1] + 1.5*gausParams1[2])
fitRange4 = (gausParams2[1] - 1.5*gausParams2[2], gausParams2[1] + 1.5*gausParams2[2])
h2.Fit("gaus2","","",fitRange4[0],fitRange4[1])
h1.Fit("gaus1","","",fitRange3[0],fitRange3[1])

##########

# TLatex to display fit results (mean, sigma)
gausParams1 = fitGaus1.GetParameters()
gausParams2 = fitGaus2.GetParameters()

pt = ROOT.TPaveText(0.20,0.60,0.20,0.83,"NBNDC")
ptptr = pt.AddText("Before correction")
ptptr.SetTextColor(ROOT.kBlue)
ptptr.SetTextSize(0.038)
ptptr.SetTextAlign(11)
ptptr = pt.AddText("Mean:  %.1f" % gausParams1[1] )
ptptr.SetTextColor(ROOT.kBlue)
ptptr.SetTextSize(0.038)
ptptr.SetTextAlign(11)
ptptr = pt.AddText("Sigma: %.1f" % gausParams1[2] )
ptptr.SetTextColor(ROOT.kBlue)
ptptr.SetTextSize(0.038)
ptptr.SetTextAlign(11)

ptptr = pt.AddText("After correction")
ptptr.SetTextColor(ROOT.kRed)
ptptr.SetTextSize(0.038)
ptptr.SetTextAlign(11)
ptptr = pt.AddText("Mean:  %.1f" % gausParams2[1] )
ptptr.SetTextColor(ROOT.kRed)
ptptr.SetTextSize(0.038)
ptptr.SetTextAlign(11)
ptptr = pt.AddText("Sigma: %.1f" % gausParams2[2] )
ptptr.SetTextColor(ROOT.kRed)
ptptr.SetTextSize(0.038)
ptptr.SetTextAlign(11)

pt.Draw("same")

##########

ROOT.gStyle.SetOptFit(0000)
h2.Draw("same")
h1.Draw("same")

import CMS_lumi as CMS_lumi
                                      
CMS_lumi.lumi_13TeV = ''
#CMS_lumi.lumi_13TeV = 'L = 137.2/fb'
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
CMS_lumi.CMS_lumi(pad1, 4, 0)

cc.Update()

cc.SaveAs("signalBcorr_{VAR}_M{MASS}.png".format(VAR=variable, MASS=mass))

