#!/usr/bin/env python


import os, sys
sys.path.insert(0,'./')
import ROOT
import logging
import argparse
from collections import OrderedDict

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
    Nmass = len(masses)
    print "Nmass", Nmass
    values =dict( (i, []) for i in range(7) ) #mass, obs, expp2, expp1, exp, expm1, expm2 7 items
    for mass in masses:
      # res_M090Y2017Mu2b3bEl2b3b.out

      fileName= 'combine/statonly_stepping_200522/res_M' + str(mass).zfill(3) +  'Y2016muCH4j2b__4j3b__eleCH4j2b__4j3b__Y2017muCH4j2b__4j3b__eleCH4j2b__4j3b__Y2018muCH4j2b__HEMveto4j3b__HEMvetoeleCH4j2b__HEMveto4j3b__HEMveto.AsymptoticLimits.mH%d.out'%(mass)
      #fileName= 'combine/res_M' + str(mass).zfill(3) + 'Y2017Mu2bEl2b.out'
      print fileName
      f = open(fileName,"r")
      fL = f.readlines()
      values[0].append(mass)
      row = 1
      for x in fL:
        if ': BR <' in x:
          # Observed Limit: BR < 0.3334
          print float(x.split("BR <")[-1])
          values[row].append( float(x.split("BR <")[-1]) )
          row +=1

   
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
      tgr_cls_obs.SetPoint(i,values[0][i], values[1][i])
      tgr_cls_exp.SetPoint(i,values[0][i], values[4][i])
      tgr_cls_exp_pm1.SetPoint(i,values[0][i], values[4][i])
      tgr_cls_exp_pm2.SetPoint(i,values[0][i], values[4][i])

      tgr_cls_exp_pm1.SetPointError(i, 0, 0, values[4][i]-values[3][i], values[5][i]-values[4][i])
      tgr_cls_exp_pm2.SetPointError(i, 0, 0, values[4][i]-values[2][i], values[6][i]-values[4][i])

    frame = ROOT.TH2F("frame","",12,50.0,170.0,10,0,0.008);
    frame.SetYTitle("Limit on B(t #rightarrow H^{+}b) with B(H^{+}#rightarrow c#bar{b}) = 1");
    frame.GetYaxis().SetTitleSize(0.035);
    frame.GetYaxis().SetLabelSize(0.03);
    frame.GetYaxis().SetTitleOffset(1.5);
    frame.SetXTitle("m_{H^{+}} (GeV)");
    frame.GetXaxis().SetTitleSize(0.035);
    frame.GetXaxis().SetLabelSize(0.03);
    frame.GetXaxis().SetTitleOffset(1.5);
    #tgr_cls_exp_pm2.GetHistogram().SetYTitle("Limit on B(t #rightarrow H^{+}b) with B(H^{+}#rightarrow c#bar{b}) = 1");
    frame.Draw()
    tgr_cls_exp_pm2.Draw("3 same")
    #tgr_cls_exp_pm2.Draw("a3 same")
    tgr_cls_exp_pm1.Draw("3 same")
    tgr_cls_exp.Draw("l same")
    tgr_cls_obs.Draw("pl same")

    leg= ROOT.TLegend(0.65,0.65,0.9,0.84);
    leg.SetFillColor(0);
    leg.SetBorderSize(0);
    #leg.SetTextFont(40);
    leg.AddEntry(tgr_cls_obs,     "Observed Limit","l");
    leg.AddEntry(tgr_cls_exp,     "Expected Limit","l");
    leg.AddEntry(tgr_cls_exp_pm1, "Expected #pm 1#sigma","f");
    leg.AddEntry(tgr_cls_exp_pm2, "Expected #pm 2#sigma","f");
    leg.Draw("same")

    import CMS_lumi as CMS_lumi

    CMS_lumi.lumi_13TeV = 'L = 137.2/fb'
    CMS_lumi.sqrtS = '#sqrt{s} = 13 TeV'
    CMS_lumi.extraText = "work in progress"

    #CMS_lumi.extraOverCmsTextSize = 0.96
    #CMS_lumi.cmsTextSize      = 0.75
    CMS_lumi.relPosX = 0.1
    #CMS_lumi.relPosX = 0.12
    CMS_lumi.CMS_lumi(tcanvas, 4, 0)

    tcanvas.SaveAs("limits.png")





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
  tag=''
  for flag in Userflags:
    if IsFirstFlag:
      tag = flag
    else:
      tag += '_'+flag 
  print tag
  
  com = CombiPlot()
  masses = [75,80,85,90,100,110,120,130,140,150]
  com.mkAsymptoticPlot(masses)

  
  
  #factory.makePlot(opt.inputFile,opt.outputDirPlots, variables, cuts, samples, plot, nuisances, legend, groupPlot)
  
  print 'Now closing......, Bye!'
