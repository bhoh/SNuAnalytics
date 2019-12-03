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


inF = TakeFileHisto('plots2500_Int_2017.root')

#################
# H + I(with H)   
#################
# GenBoosted
# GenResolved
# GenPass

cnvs = ROOT.TCanvas( 'tcanvas', 'distro',800,600)
cnvs.cd()

histoName="GenPass/GenRecH_m2500/histo_ggHWW_2500M"
histo2500_ggHWW = inF.getHisto(histoName)

histoName="GenPass/GenRecH_m2500/histo_ggHWW_I_h_2500M"
histo2500_ggHWW_I_h = inF.getHisto(histoName)

histoName="GenPass/GenRecH_m2500/histo_ggHWW_I_B_2500M"
histo2500_ggHWW_I_B = inF.getHisto(histoName)

histoName="GenPass/GenRecH_m2500/histo_ggHWW_I_2500M"
histo2500_ggHWW_I = inF.getHisto(histoName)


histo2500_ggHWW.SetLineWidth(2)
histo2500_ggHWW.SetLineColor(ROOT.kBlack)
histo2500_ggHWW_I.SetLineColor(ROOT.kGreen)
histo2500_ggHWW_I_h.SetLineColor(ROOT.kRed)
histo2500_ggHWW_I_B.SetLineColor(ROOT.kBlue)
histo2500_ggHWW.SetMaximum(12500)
histo2500_ggHWW.SetMinimum(-300)

histo2500_ggHWW.SetXTitle("m(lnjj) (GeV)");
histo2500_ggHWW.GetXaxis().SetTitleSize(0.035);
histo2500_ggHWW.GetXaxis().SetLabelSize(0.03);
histo2500_ggHWW.GetXaxis().SetTitleOffset(1.3);

histo2500_ggHWW.Draw('h')
histo2500_ggHWW_I_h.Draw('hsame')
histo2500_ggHWW_I_B.Draw('hsame')
histo2500_ggHWW_I.Draw('hsame')

leg= ROOT.TLegend(0.7,0.7,0.9,0.9);
leg.SetFillColor(0);
leg.SetBorderSize(0);
#leg.SetTextFont(8);
leg.AddEntry(histo2500_ggHWW,  "ggH(2500)WW","f");
leg.AddEntry(histo2500_ggHWW_I_h, "ggI_Hh","f");
leg.AddEntry(histo2500_ggHWW_I_B, "ggI_HB","f");
leg.AddEntry(histo2500_ggHWW_I,"ggI_HB+Hh","f");
leg.Draw("same")

cnvs.SaveAs("GenPassH2500HaIHhB.png")
cnvs.SaveAs("GenPassH2500HaIHhB.pdf")

