import ROOT
import sys


f = ROOT.TFile("Likelihood.root","UPDATE")

mass = "080"
mass = str( sys.argv[1] )
variable1 = str( sys.argv[2] )
variable2 = str( sys.argv[3] )
#histogram range by mass
histo_min = str( sys.argv[4] )
histo_max = str( sys.argv[5] )
#mass = "120"

if mass not in ["SM", "075", "080", "085", "090", "100", "110", "120", "130", "140", "150", "160"]:
  raise Exception("{MASS} is not in the list".format(MASS=mass))

if mass == "SM":
  fIn = "/xrootd/store/user/bhoh/Latino/HWWNano/Summer20UL18_106x_nAODv9_Full2018v9/CHToCBLepton2018v9__CHToCBJetMETCorr2018v9__kinFitTTSemiLepV5__mvaTreeCHToCB/nanoLatino_TTToSemiLeptonic__part1*.root"
  fIn = "/xrootd/store/user/bhoh/Latino/HWWNano/Summer20UL17_106x_nAODv9_Full2017v9/CHToCBLepton2017v9__CHToCBJetMETCorr2017v9__kinFitTTSemiLepV5__mvaTreeCHToCB/nanoLatino_TTToSemiLeptonic__part1*.root"
else:
  fIn = "/xrootd/store/user/bhoh/Latino/HWWNano/Summer20UL18_106x_nAODv9_Full2018v9/CHToCBLepton2018v9__CHToCBJetMETCorr2018v9__kinFitTTSemiLepV5__mvaTreeCHToCB/nanoLatino_CHToCB_M{MASS}__part*.root".format(MASS=mass)
  fIn = "/xrootd/store/user/bhoh/Latino/HWWNano/Summer20UL17_106x_nAODv9_Full2017v9/CHToCBLepton2017v9__CHToCBJetMETCorr2017v9__kinFitTTSemiLepV5__mvaTreeCHToCB/nanoLatino_CHToCB_M{MASS}__part*.root".format(MASS=mass)


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


#XXX previous
#fChain.Draw("gen_tt_dphi>>h1(50,{MIN},{MAX})".format(MIN=histo_min,MAX=histo_max),"(gen_tt_dphi>0)*XSWeight")
#fChain.Draw("rand_tt_dphi>>h2(50,{MIN},{MAX})".format(MIN=histo_min,MAX=histo_max),"(rand_tt_dphi>0)*XSWeight")

# histogram for plotting
fChain.Draw("TMath::Min(TMath::Max({VAR},{MIN}+0.01),{MAX}-0.01)>>h1(50,{MIN},{MAX})".format(VAR=variable1,MIN=histo_min,MAX=histo_max),"({VAR}>0)*XSWeight".format(VAR=variable1))
fChain.Draw("TMath::Min(TMath::Max({VAR},{MIN}+0.01),{MAX}-0.01)>>h2(50,{MIN},{MAX})".format(VAR=variable2,MIN=histo_min,MAX=histo_max),"({VAR}>0)*XSWeight".format(VAR=variable2))


#
h1 = ROOT.gROOT.FindObject("h1")
h2 = ROOT.gROOT.FindObject("h2")
#
n1 = h1.Integral()
n2 = h2.Integral()
#
h1.Scale(1/n1)
h2.Scale(1/n2)

#
h1.SetLineColor(ROOT.kBlue)
h2.SetLineColor(ROOT.kRed)
#
h1.GetYaxis().SetTitle("a.u.")
if "top_mass" in variable1:
  h1.GetXaxis().SetTitle("#it{M_{jjj}}")
elif "mbl" in variable1:
  h1.GetXaxis().SetTitle("#it{M_{jl}}")
elif "dijet_mass" in variable1:
  h1.GetXaxis().SetTitle("#it{M_{jj}}")
elif "dijet_deltaR" in variable1:
  h1.GetXaxis().SetTitle("#DeltaR(j,j)")
else:
  h1.GetXaxis().SetTitle("#it{M_{jj}}")


yMax = h2.GetMaximum()
yMax = yMax if yMax > h1.GetMaximum() else h1.GetMaximum()
h1.GetYaxis().SetRangeUser(0, yMax * 1.2)
h2.GetYaxis().SetRangeUser(0, yMax * 1.2)

##########

ROOT.gStyle.SetOptFit(0000)
h1.Draw()
h2.Draw("same")

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

cc.SaveAs("signalKF_{VAR}_M{MASS}.png".format(VAR=variable1, MASS=mass))

f.cd()

h1.Sumw2()
h2.Sumw2()
h1.Write("{VAR}_{MASS}".format(VAR=variable1, MASS=mass))
h2.Write("{VAR}_{MASS}".format(VAR=variable2, MASS=mass))

h3 = h1.Clone("likelihood_ratio")
h4 = h1.Clone("likelihood_divide")
h4.Add(h2)
h3.Divide(h4)

h3.GetYaxis().SetRangeUser(0, 1)

h3.Write("likelihood_ratio_{VAR}_{MASS}".format(VAR=variable1.replace("matched_",""), MASS=mass))

