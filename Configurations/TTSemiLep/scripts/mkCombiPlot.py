#!/usr/bin/env python


import os, sys
import numpy as np
sys.path.insert(0,'./')
import ROOT
import logging
import argparse
from collections import OrderedDict

input_files = {
  '8tev' : OrderedDict({
      90  : '/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/combine_8tev/res_Comb_8TeV_90_syst.out',
      100 : '/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/combine_8tev/res_Comb_8TeV_100_syst.out',
      110 : '/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/combine_8tev/res_Comb_8TeV_110_syst.out',
      120 : '/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/combine_8tev/res_Comb_8TeV_120_syst.out',
      130 : '/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/combine_8tev/res_Comb_8TeV_130_syst.out',
      140 : '/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/combine_8tev/res_Comb_8TeV_140_syst.out',
      150 : '/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/combine_8tev/res_Comb_8TeV_150_syst.out',
  }),
  'not_flip' : OrderedDict({
      75  : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M/mkCombine__Asym_fitted_dijet_M__ALL__075.out',
      80  : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M/mkCombine__Asym_fitted_dijet_M__ALL__080.out',
      85  : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M/mkCombine__Asym_fitted_dijet_M__ALL__085.out',
      90  : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M/mkCombine__Asym_fitted_dijet_M__ALL__090.out',
      100 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M/mkCombine__Asym_fitted_dijet_M__ALL__100.out',
      110 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M/mkCombine__Asym_fitted_dijet_M__ALL__110.out',
      120 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M/mkCombine__Asym_fitted_dijet_M__ALL__120.out',
      130 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M/mkCombine__Asym_fitted_dijet_M__ALL__130.out',
      140 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M/mkCombine__Asym_fitted_dijet_M__ALL__140.out',
      150 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M/mkCombine__Asym_fitted_dijet_M__ALL__150.out',
      160 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M/mkCombine__Asym_fitted_dijet_M__ALL__160.out',
  }),
   'standard' : OrderedDict({
      75  : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M/mkCombine__Asym_fitted_dijet_M__ALL__075.out',
      80  : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M/mkCombine__Asym_fitted_dijet_M__ALL__080.out',
      85  : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M/mkCombine__Asym_fitted_dijet_M__ALL__085.out',
      90  : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M/mkCombine__Asym_fitted_dijet_M__ALL__090.out',
      100 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M/mkCombine__Asym_fitted_dijet_M__ALL__100.out',
      110 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M/mkCombine__Asym_fitted_dijet_M__ALL__110.out',
      120 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M/mkCombine__Asym_fitted_dijet_M__ALL__120.out',
      130 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high/mkCombine__Asym_fitted_dijet_M_high__ALL__130.out',
      140 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high/mkCombine__Asym_fitted_dijet_M_high__ALL__140.out',
      150 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high/mkCombine__Asym_fitted_dijet_M_high__ALL__150.out',
      160 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high/mkCombine__Asym_fitted_dijet_M_high__ALL__160.out',
  }), 
  'flip_all' : OrderedDict({
      75  : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high/mkCombine__Asym_fitted_dijet_M_high__ALL__075.out',
      80  : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high/mkCombine__Asym_fitted_dijet_M_high__ALL__080.out',
      85  : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high/mkCombine__Asym_fitted_dijet_M_high__ALL__085.out',
      90  : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high/mkCombine__Asym_fitted_dijet_M_high__ALL__090.out',
      100 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high/mkCombine__Asym_fitted_dijet_M_high__ALL__100.out',
      110 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high/mkCombine__Asym_fitted_dijet_M_high__ALL__110.out',
      120 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high/mkCombine__Asym_fitted_dijet_M_high__ALL__120.out',
      130 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high/mkCombine__Asym_fitted_dijet_M_high__ALL__130.out',
      140 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high/mkCombine__Asym_fitted_dijet_M_high__ALL__140.out',
      150 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high/mkCombine__Asym_fitted_dijet_M_high__ALL__150.out',
      160 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high/mkCombine__Asym_fitted_dijet_M_high__ALL__160.out',
  }),       
  'BDT' : OrderedDict({
      75  : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_BDT_Low/mkCombine__Asym_fitted_dijet_M_BDT_Low__ALL__075.out',
      80  : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_BDT_Low/mkCombine__Asym_fitted_dijet_M_BDT_Low__ALL__080.out',
      85  : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_BDT_Low/mkCombine__Asym_fitted_dijet_M_BDT_Low__ALL__085.out',
      90  : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_BDT_Low/mkCombine__Asym_fitted_dijet_M_BDT_Low__ALL__090.out',
      100 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_BDT_Low/mkCombine__Asym_fitted_dijet_M_BDT_Low__ALL__100.out',
      110 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_BDT_Low/mkCombine__Asym_fitted_dijet_M_BDT_Low__ALL__110.out',
      120 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_BDT_Low/mkCombine__Asym_fitted_dijet_M_BDT_Low__ALL__120.out',
      130 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high_BDT_High/mkCombine__Asym_fitted_dijet_M_high_BDT_High__ALL__130.out',
      140 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high_BDT_High/mkCombine__Asym_fitted_dijet_M_high_BDT_High__ALL__140.out',
      150 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high_BDT_High/mkCombine__Asym_fitted_dijet_M_high_BDT_High__ALL__150.out',
      160 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high_BDT_High/mkCombine__Asym_fitted_dijet_M_high_BDT_High__ALL__160.out',
  }),  
  'DNN' : OrderedDict({
      75  : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_DNN_Low/mkCombine__Asym_fitted_dijet_M_DNN_Low__ALL__075.out',
      80  : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_DNN_Low/mkCombine__Asym_fitted_dijet_M_DNN_Low__ALL__080.out',
      85  : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_DNN_Low/mkCombine__Asym_fitted_dijet_M_DNN_Low__ALL__085.out',
      90  : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_DNN_Low/mkCombine__Asym_fitted_dijet_M_DNN_Low__ALL__090.out',
      100 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_DNN_Low/mkCombine__Asym_fitted_dijet_M_DNN_Low__ALL__100.out',
      110 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_DNN_Low/mkCombine__Asym_fitted_dijet_M_DNN_Low__ALL__110.out',
      120 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_DNN_Low/mkCombine__Asym_fitted_dijet_M_DNN_Low__ALL__120.out',
      130 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high_DNN_High/mkCombine__Asym_fitted_dijet_M_high_DNN_High__ALL__130.out',
      140 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high_DNN_High/mkCombine__Asym_fitted_dijet_M_high_DNN_High__ALL__140.out',
      150 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high_DNN_High/mkCombine__Asym_fitted_dijet_M_high_DNN_High__ALL__150.out',
      160 : '/cms/ldap_home/bhoh/latinos/jobs/mkCombine__Asym_fitted_dijet_M_high_DNN_High/mkCombine__Asym_fitted_dijet_M_high_DNN_High__ALL__160.out',
  }),
}



class CombiPlot:
  def __init__(self):
    self._tag = ''


  def defineStyle(self):

    import tdrStyle as tdrStyle
    tdrStyle.setTDRStyle()

    ROOT.TGaxis.SetExponentOffset(-0.08, 0.00,"y")

  def mkAsymptoticPlot(self,masses):
    self.defineStyle()
    isCLsb = False
    self._values = {}
    for tag_key, file_dict in input_files.iteritems():
      self._values[tag_key] =dict( (i, []) for i in range(7) ) #mass, obs, expp2, expp1, exp, expm1, expm2 7 items
      for mass, fileName in iter(sorted(file_dict.iteritems())):
        print fileName
        f = open(fileName,"r")
        fL = f.readlines()
        self._values[tag_key][0].append(mass)
        row = 1
        for x in fL:
          if ': BR <' in x:
            # Observed Limit: BR < 0.3334
            print float(x.split("BR <")[-1])
            self._values[tag_key][row].append( float(x.split("BR <")[-1]) )
            row +=1
      Nmass=len(file_dict.keys())
      self.drawExpObsLimits(tag_key, Nmass)
    expAll = [('8tev','8 TeV',ROOT.kBlack),('not_flip','not flip',ROOT.kGreen),('flip_all','flip',ROOT.kYellow),('BDT','BDT',ROOT.kBlue),('DNN','DNN',ROOT.kRed)] #(<tag_key>,<label>,<color>)

    Nmass = len(masses)
    print "Nmass", Nmass
    self.drawExpLimitsAll(expAll)

  def drawExpObsLimits(self,tag_key,Nmass):
   
    tcanvas = ROOT.TCanvas( 'tcanvas', 'distro',800,600)
    tcanvas.cd()
    # Making tgraphs for each items
    tgr_cls_obs     = ROOT.TGraph(Nmass)
    tgr_cls_exp     = ROOT.TGraph(Nmass)
    tgr_cls_exp_pm1 = ROOT.TGraphAsymmErrors(Nmass)
    tgr_cls_exp_pm2 = ROOT.TGraphAsymmErrors(Nmass)
    tgr_cls_obs.SetLineWidth(2)
    tgr_cls_exp.SetLineWidth(4)
    tgr_cls_exp_pm1.SetLineWidth(2)
    tgr_cls_exp_pm2.SetLineWidth(2)


    tgr_cls_exp.SetLineColor(ROOT.kRed)
    tgr_cls_exp_pm1.SetLineColor(ROOT.kGreen)
    tgr_cls_exp_pm2.SetLineColor(ROOT.kYellow)
    tgr_cls_exp_pm1.SetFillColor(ROOT.kGreen)
    tgr_cls_exp_pm2.SetFillColor(ROOT.kYellow)

    for i in range(Nmass):
      tgr_cls_obs.SetPoint(i,self._values[tag_key][0][i], self._values[tag_key][1][i])
      tgr_cls_exp.SetPoint(i,self._values[tag_key][0][i], self._values[tag_key][4][i])
      tgr_cls_exp_pm1.SetPoint(i,self._values[tag_key][0][i], self._values[tag_key][4][i])
      tgr_cls_exp_pm2.SetPoint(i,self._values[tag_key][0][i], self._values[tag_key][4][i])

      tgr_cls_exp_pm1.SetPointError(i, 0, 0, self._values[tag_key][4][i]-self._values[tag_key][3][i], self._values[tag_key][5][i]-self._values[tag_key][4][i])
      tgr_cls_exp_pm2.SetPointError(i, 0, 0, self._values[tag_key][4][i]-self._values[tag_key][2][i], self._values[tag_key][6][i]-self._values[tag_key][4][i])

    #frame = ROOT.TH2F("frame","",12,50.0,170.0,10,0.0001,0.1);
    frame = ROOT.TH2F("frame","",13,np.array([60.,70.,75.,80.,85.,90.,100.,110.,120.,130.,140.,150.,160.,170.]),10,np.array([0.0001,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1]));
    frame.SetYTitle("95% CL upper limit on B(t #rightarrow H^{+}b) with B(H^{+}#rightarrow c#bar{b}) = 1");
    frame.GetYaxis().SetTitleSize(0.035);
    frame.GetYaxis().SetLabelSize(0.03);
    frame.GetYaxis().SetTitleOffset(1.5);
    frame.SetXTitle("m_{H^{+}} (GeV)");
    frame.GetXaxis().SetTitleSize(0.035);
    frame.GetXaxis().SetLabelSize(0.03);
    frame.GetXaxis().SetTitleOffset(1.5);
    frame.GetXaxis().SetNdivisions(14);
    #tgr_cls_exp_pm2.GetHistogram().SetYTitle("Limit on B(t #rightarrow H^{+}b) with B(H^{+}#rightarrow c#bar{b}) = 1");
    frame.Draw()

    #TLine grid for 75 85 GeV
    l = ROOT.TLine()
    l.SetLineStyle(3)
    ymin = tcanvas.GetUymin()
    #ymax = tcanvas.GetUymax()
    ymax = 0.1
    l.DrawLine(75,ymin,75,ymax)
    l.DrawLine(85,ymin,85,ymax)

    tgr_cls_exp_pm2.Draw("3 same")
    #tgr_cls_exp_pm2.Draw("a3 same")
    tgr_cls_exp_pm1.Draw("3 same")
    tgr_cls_exp.Draw("l same")
    #tgr_cls_obs.Draw("pl same")

    leg= ROOT.TLegend(0.35,0.75,0.6,0.94);
    leg.SetFillColor(0);
    leg.SetBorderSize(0);
    #leg.SetTextFont(40);
    #leg.AddEntry(tgr_cls_obs,    "Observed","l");
    leg.AddEntry(tgr_cls_exp,     "Median expected","l");
    leg.AddEntry(tgr_cls_exp_pm1, "68% expected","f");
    leg.AddEntry(tgr_cls_exp_pm2, "95% expected","f");
    leg.Draw("same")

    import CMS_lumi as CMS_lumi

    #CMS_lumi.lumi_13TeV = 'L = 58.8/fb'
    CMS_lumi.lumi_13TeV = 'L = 137.2/fb'
    CMS_lumi.sqrtS = '#sqrt{s} = 13 TeV'
    CMS_lumi.extraText = "preliminary"

    #CMS_lumi.extraOverCmsTextSize = 0.96
    #CMS_lumi.cmsTextSize      = 0.75
    CMS_lumi.relPosX = 0.1
    #CMS_lumi.relPosX = 0.12
    CMS_lumi.CMS_lumi(tcanvas, 4, 0)


    tcanvas.SetGrid()
    tcanvas.SetLogy()
    tcanvas.SaveAs("limits_%s.png"%tag_key)

  def drawExpLimitsAll(self, exp_all_list):

    tcanvas = ROOT.TCanvas( 'tcanvas', 'distro',800,600)
    tcanvas.SetGrid()
    tcanvas.SetLogy()
    tcanvas.cd()
    # Making tgraphs for each items
    tgr_cls_exp = {}
    for tag_key, _, color in exp_all_list:
      Nmass = len(input_files[tag_key].keys())
      tgr_cls_exp[tag_key]     = ROOT.TGraph(Nmass)
      tgr_cls_exp[tag_key].SetLineWidth(4)


      tgr_cls_exp[tag_key].SetLineColor(color)

      for i in range(Nmass):
        tgr_cls_exp[tag_key].SetPoint(i,self._values[tag_key][0][i], self._values[tag_key][4][i])


    #frame = ROOT.TH2F("frame","",12,50.0,170.0,10,0.0001,0.1);
    frame = ROOT.TH2F("frame","",13,np.array([60.,70.,75.,80.,85.,90.,100.,110.,120.,130.,140.,150.,160.,170.]),10,np.array([0.0001,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1]));
    frame.SetYTitle("95% CL upper limit on B(t #rightarrow H^{+}b) with B(H^{+}#rightarrow c#bar{b}) = 1");
    frame.GetYaxis().SetTitleSize(0.035);
    frame.GetYaxis().SetLabelSize(0.03);
    frame.GetYaxis().SetTitleOffset(1.5);
    frame.SetXTitle("m_{H^{+}} (GeV)");
    frame.GetXaxis().SetTitleSize(0.035);
    frame.GetXaxis().SetLabelSize(0.03);
    frame.GetXaxis().SetTitleOffset(1.5);
    frame.GetXaxis().SetNdivisions(14);
    #tgr_cls_exp_pm2.GetHistogram().SetYTitle("Limit on B(t #rightarrow H^{+}b) with B(H^{+}#rightarrow c#bar{b}) = 1");
    frame.Draw()

    #TLine grid for 75 85 GeV
    l = ROOT.TLine()
    l.SetLineStyle(3)
    ymin = tcanvas.GetUymin()
    #ymax = tcanvas.GetUymax()
    ymax = 0.1
    l.DrawLine(75,ymin,75,ymax)
    l.DrawLine(85,ymin,85,ymax)

    for tag_key, _, _ in exp_all_list:
      tgr_cls_exp[tag_key].Draw("l same")

    leg= ROOT.TLegend(0.35,0.75,0.6,0.94);
    leg.SetFillColor(0);
    leg.SetBorderSize(0);
    #leg.SetTextFont(40);
    #leg.AddEntry(tgr_cls_obs,     "Observed Limit","l");
    for tag_key, label, _ in exp_all_list:
      leg.AddEntry(tgr_cls_exp[tag_key],     "Median expected, %s"%label,"l");
    leg.Draw("same")

    import CMS_lumi as CMS_lumi

    #CMS_lumi.lumi_13TeV = 'L = 58.8/fb'
    CMS_lumi.lumi_13TeV = 'L = 137.2/fb'
    CMS_lumi.sqrtS = '#sqrt{s} = 13 TeV'
    CMS_lumi.extraText = "preliminary"

    #CMS_lumi.extraOverCmsTextSize = 0.96
    #CMS_lumi.cmsTextSize      = 0.75
    CMS_lumi.relPosX = 0.1
    #CMS_lumi.relPosX = 0.12
    CMS_lumi.CMS_lumi(tcanvas, 4, 0)

    tcanvas.SaveAs("limits_expAll.png")



if __name__ == "__main__":

  print '''
  -----------------------------------------------------------------------------------------
                                                           
    _____  _       _     __  __       _               _    _       _           _           
   |  __ \| |     | |   |  \/  |     | |             | |  | |     | |         | |          
   | |__) | | ___ | |_  | \  / | __ _| | _____ _ __  | |__| | __ _| |__   __ _| |__   __ _ 
   |  ___/| |/ _ \| __| | |\/| |/ _` | |/ / _ \ '__| |  __  |/ _` | '_ \ / _` | '_ \ / _` |
   | |    | | (_) | |_  | |  | | (_| |   <  __/ |    | |  | | (_| | | | | (_| | | | | (_| |
   |_|    |_|\___/ \__| |_|  |_|\__,_|_|\_\___|_|    |_|  |_|\__,_|_| |_|\__,_|_| |_|\__,_|
  	                                                                                          
  -----------------------------------------------------------------------------------------
  
  '''
  
  
  parser = argparse.ArgumentParser(description='JudgementDay')
  parser.add_argument('--userflags', dest='Userflags', default="test")
  parser.add_argument('--debug', dest='debug', default=0, type=int)
  parser.add_argument('--scaleToPlot'    , dest='scaleToPlot'    , help='scale of maxY to maxHistoY'                 , default=2.0  ,    type=float   )
  parser.add_argument('--minLogC'        , dest='minLogC'        , help='min Y in log plots'                         , default=0.01  ,    type=float   )
  parser.add_argument('--maxLogC'        , dest='maxLogC'        , help='max Y in log plots'                         , default=100   ,    type=float   )
  parser.add_argument('--minLogCratio'   , dest='minLogCratio'   , help='min Y in log ratio plots'                   , default=0.001 ,    type=float   )
  parser.add_argument('--maxLogCratio'   , dest='maxLogCratio'   , help='max Y in log ratio plots'                   , default=10    ,    type=float   )
  parser.add_argument('--maxLinearScale' , dest='maxLinearScale' , help='scale factor for max Y in linear plots (1.45 magic number as default)'     , default=1.45   ,    type=float   )
  parser.add_argument('--outputDirPlots' , dest='outputDirPlots' , help='output directory'                           , default='./')
  											  
  parser.add_argument('--postFit', dest='postFit', help='Plot sum of post-fit backgrounds, and the data/post-fit ratio.' , default='n') 
  
  
  
  ROOT.gROOT.SetBatch()
  
  opt = parser.parse_args()
  
  
  print ""
  print "              outputDirPlots =", opt.outputDirPlots
  print "                 scaleToPlot =", opt.scaleToPlot
  print "                     minLogC =", opt.minLogC
  print "                     maxLogC =", opt.maxLogC
  print "                minLogCratio =", opt.minLogCratio
  print "                maxLogCratio =", opt.maxLogCratio
  print "                    postFit  =", opt.postFit
  print ""
  
  opt.scaleToPlot = float(opt.scaleToPlot)
  opt.minLogC = float(opt.minLogC)
  opt.maxLogC = float(opt.maxLogC)
  
  opt.minLogCratio = float(opt.minLogCratio)
  opt.maxLogCratio = float(opt.maxLogCratio)
  
  if not opt.debug:
    pass
  elif opt.debug == 2:
    print 'Logging level set to DEBUG (%d)' % opt.debug
    logging.basicConfig( level=logging.DEBUG )
  elif opt.debug == 1:
    print 'Logging level set to INFO (%d)' % opt.debug
    logging.basicConfig( level=logging.INFO )
  
  Userflags = []
  if opt.Userflags != "":
    Userflags = (opt.Userflags).split(',')
  
  IsFirstFlag = True
  #tag=''
  #for flag in Userflags:
  #  if IsFirstFlag:
  #    tag = flag
  #  else:
  #    tag += '_'+flag 
  #print tag
  
  com = CombiPlot()
  masses = [75,80,85,90,100,110,120,130,140,150,160]
  com.mkAsymptoticPlot(masses)

  
  
  #factory.makePlot(opt.inputFile,opt.outputDirPlots, variables, cuts, samples, plot, nuisances, legend, groupPlot)
  
  print 'Now closing......, Bye!'
