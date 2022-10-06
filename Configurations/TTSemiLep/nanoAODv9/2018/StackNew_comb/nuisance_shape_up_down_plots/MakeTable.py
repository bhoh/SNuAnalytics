import ROOT
from ROOT import TLegend, TCanvas, TFile, TH1F, TPad, gPad, gStyle, kBlue, kGreen, kMagenta, kWhite, kBlack
import pandas as pd
import numpy as np


class MakeTable():

  def __init__(self):
    self.inputRootFile    = []
    self.inputRootFile_MC = []
    self.histoNominal     = []
    self.histo_up         = []
    self.histo_down       = []
    self.legendName       = []
    self.hNominal         = []
    self.hUp              = []
    self.hDo            = []
    self.nNominal         = []
    self.nUp              = []
    self.nDo              = []

    self.table            = {}
    self.table['sample'] = []
    self.table['nLepton'] = []
    self.table['region']  = []
    self.table['nuisance']= []
    self.table['nominal'] = []
    self.table['up']      = []
    self.table['down']    = []


  def addEntry(self, inputRootFile, inputRootFile_MC, histoNominal, histo_up, histo_down, legendName):
    self.inputRootFile    .append( inputRootFile )
    self.inputRootFile_MC .append( inputRootFile_MC )
    self.histoNominal     .append( histoNominal )
    self.histo_up         .append( histo_up )
    self.histo_down       .append( histo_down )
    self.legendName       .append( legendName )
    
    tfile = TFile (inputRootFile,"READ")

    self.hNominal.append( tfile.Get(histoNominal) )
    self.hUp     .append( tfile.Get(histo_up) )
    self.hDo     .append( tfile.Get(histo_down) )

    self.nNominal.append( self.hNominal[-1].Integral() )
    self.nUp     .append( self.hUp[-1].Integral() )
    self.nDo     .append( self.hDo[-1].Integral() )

  def makeTable(self):
    # sample, nLepton, region, nuisance, nominal, up, down

    sample     = self.histoNominal[-1].split('/')[-1]
    legendName = self.legendName[-1].split(',')
    nLepton = legendName[0]
    if len(legendName)==3:
      if "2b" in legendName[1]:
        region = "CR1"
      else:
        region = "SR"
    else:
      region = "CR2"

    nuisance = legendName[2] if len(legendName)==3 else legendName[1]
    nuisance = nuisance.split(' ')[-1].replace(' ','')

    self.table['sample']   .append( sample   )
    self.table['nLepton']  .append( nLepton  )
    self.table['region']   .append( region   )
    self.table['nuisance'] .append( nuisance )
    self.table['nominal']  .append( int(self.nNominal[-1]) )
    self.table['up']   .append( int(self.nUp[-1]) )
    self.table['down'] .append( int(self.nDo[-1]) )

  def saveTable(self,suffix):
    df = pd.DataFrame.from_dict(self.table)
    # change columns order
    df = df[['sample', 'nLepton','region','nuisance','nominal', 'up', 'down']]
    df.to_csv("out_nuis_table_{}.txt".format(suffix), index=False)


    df2 = df.groupby(by=['sample', 'nuisance', 'region']).sum()
    # up/down after sumup
    df2['up (%)']   = (100 * df2['up']/df2['nominal'] -100.).round(1)
    df2['down (%)'] = (100 * df2['down']/df2['nominal'] -100.).round(1)

    # up/down before sumup
    df['up (%)']   = (100 * df['up']/df['nominal'] -100.).round(1)
    df['down (%)'] = (100 * df['down']/df['nominal'] -100.).round(1)

    df_min = df.groupby(by=['sample', 'nuisance', 'region']).min()
    df_max = df.groupby(by=['sample', 'nuisance', 'region']).max()
    df2['min. (%)'] =  df_min[['up (%)','down (%)']].min(axis=1)
    df2['max (%)']  =  df_max[['up (%)','down (%)']].max(axis=1)
    df2['range']    = df2['min. (%)'].apply(str) + ' - ' + df2['max (%)'].apply(str) + ' %'

    df2.to_csv("out_nuis_table2_{}.txt".format(suffix))
    df2.to_latex("out_nuis_table2_{}.tex".format(suffix))
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
      print(df2)

    #df[ df['nuisance'] == '' ]
    #nuisance group
    self.groupNuisance(df)

    df3 = df.groupby(by=['sample', 'nuisance_group', 'region']).sum()
    df3 = df3.drop(columns=['up (%)', 'down (%)'])
    df_min = df.groupby(by=['sample', 'nuisance_group', 'region']).min()
    df_max = df.groupby(by=['sample', 'nuisance_group', 'region']).max()
    df3['min. (%)'] =  df_min[['up (%)','down (%)']].min(axis=1)
    df3['max (%)']  =  df_max[['up (%)','down (%)']].max(axis=1)
    df3['range']    = df3['min. (%)'].apply(str) + ' - ' + df3['max (%)'].apply(str) + ' %'

    df3.to_csv("out_nuis_table3_{}.txt".format(suffix))
    df3.to_latex("out_nuis_table3_{}.tex".format(suffix))
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
      print(df3)


  def groupNuisance(self, df):

    df['nuisance_group'] = ''

    df.loc[ df['nuisance'] == 'PU'                , 'nuisance_group'] = 'pu_syst'
    df.loc[ df['nuisance'] == 'LHEPdfWeight'      , 'nuisance_group'] = 'theory_syst'
    df.loc[ df['nuisance'] == 'QCDscale_tt'       , 'nuisance_group'] = 'theory_syst'
    df.loc[ df['nuisance'] == 'ttbar_fsr'         , 'nuisance_group'] = 'theory_syst'
    df.loc[ df['nuisance'] == 'ttbar_isr'         , 'nuisance_group'] = 'theory_syst'
    df.loc[ df['nuisance'] == 'btag_cferr1'       , 'nuisance_group'] = 'btag_syst'
    df.loc[ df['nuisance'] == 'btag_cferr2'       , 'nuisance_group'] = 'btag_syst'
    df.loc[ df['nuisance'] == 'btag_hf'           , 'nuisance_group'] = 'btag_syst'
    df.loc[ df['nuisance'] == 'btag_hfstats1_2018', 'nuisance_group'] = 'btag_syst'
    df.loc[ df['nuisance'] == 'btag_hfstats2_2018', 'nuisance_group'] = 'btag_syst'
    df.loc[ df['nuisance'] == 'btag_lf'           , 'nuisance_group'] = 'btag_syst'
    df.loc[ df['nuisance'] == 'btag_lfstats1_2018', 'nuisance_group'] = 'btag_syst'
    df.loc[ df['nuisance'] == 'btag_lfstats2_2018', 'nuisance_group'] = 'btag_syst'
    df.loc[ df['nuisance'] == 'eff_ele'           , 'nuisance_group'] = 'lepton_syst'
    df.loc[ df['nuisance'] == 'eff_muon'          , 'nuisance_group'] = 'lepton_syst'
    df.loc[ df['nuisance'] == 'eff_prefiring_2018', 'nuisance_group'] = 'lepton_syst'
    df.loc[ df['nuisance'] == 'jer0_2018'         , 'nuisance_group'] = 'jetmet_syst'
    df.loc[ df['nuisance'] == 'jer1_2018'         , 'nuisance_group'] = 'jetmet_syst'
    df.loc[ df['nuisance'] == 'jesFlavorQCD'      , 'nuisance_group'] = 'jetmet_syst'
    df.loc[ df['nuisance'] == 'jesTotalNoFlavor'  , 'nuisance_group'] = 'jetmet_syst'
    df.loc[ df['nuisance'] == 'unclustEn_2018'    , 'nuisance_group'] = 'jetmet_syst'
    df.loc[ df['nuisance'] == 'HEMIssue'          , 'nuisance_group'] = 'jetmet_syst'
    df.loc[ df['nuisance'] == 'TuneCP5'           , 'nuisance_group'] = 'tt_syst' 
    df.loc[ df['nuisance'] == 'hdamp'             , 'nuisance_group'] = 'tt_syst'
    df.loc[ df['nuisance'] == 'mtop'              , 'nuisance_group'] = 'tt_syst'
    df.loc[ df['nuisance'] == 'Top_pTreweight'    , 'nuisance_group'] = 'tt_syst'



#def MakeTable(inputRootFile, inputRootFile_MC, histoNominal, histo_up, histo_down, legendName):
#
#  tfile = TFile (inputRootFile,"READ")
#
#  hNominal = tfile.Get(histoNominal)
#
#  hUp = tfile.Get(histo_up)
#  hDo = tfile.Get(histo_down)
#
#  nNominal = hNominal.Integral()
#  nUp      = hUp.Integral()
#  nDo      = hDo.Integral()
#
#  # histo Nominal; Up(%); Down(%)
#  out_string = "{}: {}, {}, {}\n".format(legendName, nNominal, (nUp/nNominal-1), (nDo/nNominal-1))
#  print(out_string)
#  with open("out_nuis_table.txt", "a") as f:
#    f.write(out_string)
