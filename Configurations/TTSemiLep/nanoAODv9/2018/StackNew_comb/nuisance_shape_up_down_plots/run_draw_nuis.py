#!/usr/bin/python
import os
import ROOT

mergeMC = True
makePlot = True
makeTable = True

os.system('mkdir -p plots_Mjj/cc_sng_4j_muCH_2b/fitted_dijet_M')
os.system('mkdir -p plots_Mjj/cc_sng_4j_eleCH_2b/fitted_dijet_M')
os.system('mkdir -p plots_Mjj/cc_sng_4j_muCH_3b/fitted_dijet_M_high_down_type_jet_b_tagged')
os.system('mkdir -p plots_Mjj/cc_sng_4j_eleCH_3b/fitted_dijet_M_high_down_type_jet_b_tagged')

os.system('mkdir -p plots_disc/cc_dbl_4j_ee/3_4rd_leading_b_disc')
os.system('mkdir -p plots_disc/cc_dbl_4j_em/3_4rd_leading_b_disc')
os.system('mkdir -p plots_disc/cc_dbl_4j_me/3_4rd_leading_b_disc')
os.system('mkdir -p plots_disc/cc_dbl_4j_mm/3_4rd_leading_b_disc')

os.system('mkdir -p plots_Mjj/log_cc_sng_4j_muCH_2b/fitted_dijet_M')
os.system('mkdir -p plots_Mjj/log_cc_sng_4j_eleCH_2b/fitted_dijet_M')
os.system('mkdir -p plots_Mjj/log_cc_sng_4j_muCH_3b/fitted_dijet_M_high_down_type_jet_b_tagged')
os.system('mkdir -p plots_Mjj/log_cc_sng_4j_eleCH_3b/fitted_dijet_M_high_down_type_jet_b_tagged')


os.system('mkdir -p plots_disc/log_cc_dbl_4j_ee/3_4rd_leading_b_disc')
os.system('mkdir -p plots_disc/log_cc_dbl_4j_em/3_4rd_leading_b_disc')
os.system('mkdir -p plots_disc/log_cc_dbl_4j_me/3_4rd_leading_b_disc')
os.system('mkdir -p plots_disc/log_cc_dbl_4j_mm/3_4rd_leading_b_disc')

inputFile='/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv9/2018/StackNew_comb/rootFile_2018_SKIM9_final/PDF/results_unc.root'
inputFile_MC='/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv9/2018/StackNew_comb/rootFile_2018_SKIM9_final/PDF/results_unc.root'


nuisances = ['TuneCP5', 'hdamp', 'mtop', 'jesTotalNoFlavor', 'jesFlavorQCD', 'Top_pTreweight']\
 + [ 'btag_' + shift + '_2018' if 'stats' in shift else 'btag_' + shift for shift in ['lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2'] ]\
 + [ 'eff_ele', 'eff_muon', 'eff_prefiring_2018']\
 + ['jer0_2018', 'jer1_2018', 'unclustEn_2018', 'HEMIssue']\
 + ['PU', 'ttbar_isr', 'ttbar_fsr', 'QCDscale_tt', 'LHEPdfWeight']




nameNominal=[
  'sng_4j_muCH_2b/fitted_dijet_M/histo_MC',
  'sng_4j_eleCH_2b/fitted_dijet_M/histo_MC',
  'sng_4j_muCH_3b/fitted_dijet_M_high_down_type_jet_b_tagged/histo_MC',
  'sng_4j_eleCH_3b/fitted_dijet_M_high_down_type_jet_b_tagged/histo_MC',
  'dbl_4j_ee/3_4rd_leading_b_disc/histo_MC',
  'dbl_4j_em/3_4rd_leading_b_disc/histo_MC',
  'dbl_4j_me/3_4rd_leading_b_disc/histo_MC',
  'dbl_4j_mm/3_4rd_leading_b_disc/histo_MC',
]


nameNominal_signal = []
signal_samples = ['CHToCB_M075','CHToCB_M080','CHToCB_M085','CHToCB_M090','CHToCB_M100','CHToCB_M110','CHToCB_M120','CHToCB_M130','CHToCB_M140','CHToCB_M150','CHToCB_M160',]
#signal_samples = []
for signal_sample in signal_samples:
  nameNominal_signal.extend( [ name.replace('histo_MC','histo_{}'.format(signal_sample)) for name in nameNominal ] )

nameNominal.extend(nameNominal_signal)


nameUp=[]
for nuisance in nuisances:
  nameUp.extend( [ name + '_' + nuisance + 'Up' for name in nameNominal ] )

nameDown=[]
for nuisance in nuisances:
  nameDown.extend( [ name + '_' + nuisance + 'Down' for name in nameNominal ] )

nameMC=[
  'sng_4j_muCH_2b',
  'sng_4j_eleCH_2b',
  'sng_4j_muCH_3b',
  'sng_4j_eleCH_3b',
  'dbl_4j_ee',
  'dbl_4j_em',
  'dbl_4j_me',
  'dbl_4j_mm',
]


legendName=[]
for nuisance in nuisances:
  for signal_sample in ['Bkgs.'] + signal_samples:
    tmp_legend = [
      '1#mu, 2b, Bkgs.',
      '1e, 2b, Bkgs.',
      '1#mu, #geq3b, Bkgs.',
      '1e, #geq3b, Bkgs.',
      'ee, Bkgs.',
      'e#mu, Bkgs.',
      '#mue, Bkgs.',
      '#mu#mu, Bkgs.',
            ]
    mass = signal_sample.replace('CHToCB_', '')
    legendName.extend( map(lambda s: s.replace('Bkgs.', mass) + ' ' + nuisance, tmp_legend) )


varName=[
  '#it{M_{jj}} [GeV]',
  '#it{M_{jj}} [GeV]',
  '#it{M_{jj}} [GeV]',
  '#it{M_{jj}} [GeV]',
  'Bins',
  'Bins',
  'Bins',
  'Bins',
]
outputDirPlots=[
  'plots_Mjj',
  'plots_Mjj',
  'plots_Mjj',
  'plots_Mjj',
  'plots_disc',
  'plots_disc',
  'plots_disc',
  'plots_disc',
]
drawYields=[
  '0',
  '0',
  '0',
  '0',
  '0',
  '0',
  '0',
  '0',
]

max_ratio=[
  1.2,        
  1.2,        
  1.2,        
  1.2,        
  2.0,        
  2.0,        
  2.0,        
  2.0,

]
max_ratio=[None]*8


nameNominal    =  nameNominal    * len(nuisances)
nameMC         =  nameMC         * (len(signal_samples)+1) * len(nuisances)
varName        =  varName        * (len(signal_samples)+1) * len(nuisances)
outputDirPlots =  outputDirPlots * (len(signal_samples)+1) * len(nuisances)
drawYields     =  drawYields     * (len(signal_samples)+1) * len(nuisances)
max_ratio      =  max_ratio      * (len(signal_samples)+1) * len(nuisances)

mergedFile = 'hadd_merged.root'

if mergeMC:
  from merge_ttmc import * 

  input_f  = ROOT.TFile(inputFile)
  output_f = ROOT.TFile(mergedFile,'RECREATE')

  namePair = zip(nameNominal[:],nameNominal[:]) + zip(nameUp[:],nameNominal[:]) + zip(nameDown[:],nameNominal[:])

  for histo_dir, histo_dir_alt in namePair:
    print('merge histo: ' + histo_dir)

    if not 'histo_CHToCB_M' in histo_dir:
      MergeTTMC(input_f,output_f,histo_dir, histo_dir_alt)
    else:
      CopyHisto(input_f,output_f,histo_dir, histo_dir_alt)

  input_f.Close()
  output_f.Close()




# python
from DrawNuisances import DrawNuisances
from MakeTable import MakeTable

ROOT.gROOT.SetBatch(True)

args = zip(nameNominal,nameUp,nameDown,nameMC,legendName,varName,outputDirPlots,drawYields,max_ratio)
drawMC_='0'
if makeTable:
  maketable = MakeTable()
for nameNominal_,nameUp_,nameDown_,nameMC_,legendName_,varName_,outputDirPlots_,drawYields_,max_ratio_ in args:
  print(nameNominal_,nameUp_,nameDown_,nameMC_,legendName_,varName_,outputDirPlots_,drawYields_)
  if makePlot:
    DrawNuisances(mergedFile,mergedFile,nameNominal_,nameUp_,nameDown_,nameMC_,legendName_,varName_,outputDirPlots_,drawYields_,drawMC_,max_ratio_)

  if makeTable:
    maketable.addEntry(mergedFile,mergedFile,nameNominal_,nameUp_,nameDown_,legendName_)
    maketable.makeTable()

if makeTable:
  maketable.saveTable("ver1")
