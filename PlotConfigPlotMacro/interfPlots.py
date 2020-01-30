#!/usr/bin/env python


import os, sys
import glob
#sys.path.insert(0,'./')
import ROOT
#import logging
#import argparse
from collections import OrderedDict

import tdrStyle as tdrStyle
from T800Tools  import *


#ROOT.gROOT.SetBatch()
tdrStyle.setTDRStyle()


inF = TakeFileHisto('~/Latino/CMSSW10215pch2/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/Cor_config/nanoAODv4v5_2017/Interference/rootFile_Int_2017/plots_Int_2017.root')

#################
# H + I(with H)   
#################
# GenBoosted
# GenResolved
# GenPass

cnvs = ROOT.TCanvas( 'tcanvas', 'distro',800,600)
cnvs.cd()

histoName="GenResolved/GenRecH_m900/histo_ggHWW_900M"
histo900_ggHWW = inF.getHisto(histoName)

histoName="GenResolved/GenRecH_m900/histo_ggHWW_I_h_900M"
histo900_ggHWW_I_h = inF.getHisto(histoName)

histoName="GenResolved/GenRecH_m900/histo_ggHWW_I_B_900M"
histo900_ggHWW_I_B = inF.getHisto(histoName)

histoName="GenResolved/GenRecH_m900/histo_ggHWW_I_900M"
histo900_ggHWW_I = inF.getHisto(histoName)


histo900_ggHWW.SetLineWidth(2)
histo900_ggHWW.SetLineColor(ROOT.kBlack)
histo900_ggHWW_I.SetLineColor(ROOT.kGreen)
histo900_ggHWW_I_h.SetLineColor(ROOT.kRed)
histo900_ggHWW_I_B.SetLineColor(ROOT.kBlue)
histo900_ggHWW.SetMaximum(50)
histo900_ggHWW.SetMinimum(-40)

histo900_ggHWW.SetXTitle("m(lnjj) (GeV)");
histo900_ggHWW.GetXaxis().SetTitleSize(0.035);
histo900_ggHWW.GetXaxis().SetLabelSize(0.03);
histo900_ggHWW.GetXaxis().SetTitleOffset(1.3);

histo900_ggHWW.Draw('h')
histo900_ggHWW_I_h.Draw('hsame')
histo900_ggHWW_I_B.Draw('hsame')
histo900_ggHWW_I.Draw('hsame')

leg= ROOT.TLegend(0.7,0.7,0.9,0.9);
leg.SetFillColor(0);
leg.SetBorderSize(0);
#leg.SetTextFont(8);
leg.AddEntry(histo900_ggHWW,  "ggH(900)WW","f");
leg.AddEntry(histo900_ggHWW_I_h, "ggI_Hh","f");
leg.AddEntry(histo900_ggHWW_I_B, "ggI_HB","f");
leg.AddEntry(histo900_ggHWW_I,"ggI_HB+Hh","f");
leg.Draw("same")

cnvs.SaveAs("plots/GenResolvedH900HaIHhB.png")
cnvs.SaveAs("plots/GenResolvedH900HaIHhB.pdf")

