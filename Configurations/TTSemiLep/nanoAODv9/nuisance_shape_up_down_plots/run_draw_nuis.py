#!/usr/bin/python
import os
import argparse
import ROOT

mergeMC = False
makePlot = True
makeTable = True

parser = argparse.ArgumentParser(description='year')
parser.add_argument('--year', dest='year', action='store', default='')

opt = parser.parse_args()


nuisances_2016 = ['TuneCP5', 'hdamp', 'mtop', 'jesTotalNoFlavor', 'jesFlavorQCD', 'Top_pTreweight']\
 + [ 'btag_' + shift + '_2016' if 'stats' in shift else 'btag_' + shift for shift in ['lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2'] ]\
 + [ 'eff_ele', 'eff_muon', 'eff_prefiring_2016']\
 + ['jer0_2016', 'jer1_2016', 'unclustEn_2016', 'HEMIssue']\
 + ['PU', 'ttbar_isr', 'ttbar_fsr', 'QCDscale_tt', 'LHEPdfWeight']
nuisances_2017 = ['TuneCP5', 'hdamp', 'mtop', 'jesTotalNoFlavor', 'jesFlavorQCD', 'Top_pTreweight']\
 + [ 'btag_' + shift + '_2017' if 'stats' in shift else 'btag_' + shift for shift in ['lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2'] ]\
 + [ 'eff_ele', 'eff_muon', 'eff_prefiring_2017']\
 + ['jer0_2017', 'jer1_2017', 'unclustEn_2017', 'HEMIssue']\
 + ['PU', 'ttbar_isr', 'ttbar_fsr', 'QCDscale_tt', 'LHEPdfWeight']
nuisances_2018 = ['TuneCP5', 'hdamp', 'mtop', 'jesTotalNoFlavor', 'jesFlavorQCD', 'Top_pTreweight']\
 + [ 'btag_' + shift + '_2018' if 'stats' in shift else 'btag_' + shift for shift in ['lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2'] ]\
 + [ 'eff_ele', 'eff_muon', 'eff_prefiring_2018']\
 + ['jer0_2018', 'jer1_2018', 'unclustEn_2018', 'HEMIssue']\
 + ['PU', 'ttbar_isr', 'ttbar_fsr', 'QCDscale_tt', 'LHEPdfWeight']

if opt.year == "2016HIPM":
  inputFile='/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv9/2016HIPM/StackNew_comb/rootFile_2016HIPM_SKIM9_final/PDF/results_unc.root'
  nuisances = nuisances_2016
elif opt.year == "2016noHIPM":
  inputFile='/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv9/2016noHIPM/StackNew_comb/rootFile_2016noHIPM_SKIM9_final/PDF/results_unc.root'
  nuisances = nuisances_2016
elif opt.year == "2017":
  inputFile='/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv9/2017/StackNew_comb/rootFile_2017_SKIM9_final/PDF/results_unc.root'
  nuisances = nuisances_2017
elif opt.year == "2018":
  inputFile='/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv9/2018/StackNew_comb/rootFile_2018_SKIM9_final/PDF/results_unc.root'
  nuisances = nuisances_2018
else:
  print("not supported year option: {}".format(opt.year))




nameNominal=[
  'sng_4j_muCH_2b/fitted_dijet_M/histo_MC',
  'sng_4j_eleCH_2b/fitted_dijet_M/histo_MC',
  'sng_4j_muCH_3b/fitted_dijet_M_high_down_type_jet_b_tagged/histo_MC',
  'sng_4j_eleCH_3b/fitted_dijet_M_high_down_type_jet_b_tagged/histo_MC',
  'sng_4j_muCH_3b/fitted_dijet_M_down_type_jet_b_tagged_DNN_Low_failMVA/histo_MC',
  'sng_4j_eleCH_3b/fitted_dijet_M_down_type_jet_b_tagged_DNN_Low_failMVA/histo_MC',
  'sng_4j_muCH_3b/fitted_dijet_M_high_down_type_jet_b_tagged_DNN_High_failMVA/histo_MC',
  'sng_4j_eleCH_3b/fitted_dijet_M_high_down_type_jet_b_tagged_DNN_High_failMVA/histo_MC',
  'sng_4j_muCH_3b/fitted_dijet_M_down_type_jet_b_tagged_DNN_Low_passMVA/histo_MC',
  'sng_4j_eleCH_3b/fitted_dijet_M_down_type_jet_b_tagged_DNN_Low_passMVA/histo_MC',
  'sng_4j_muCH_3b/fitted_dijet_M_high_down_type_jet_b_tagged_DNN_High_passMVA/histo_MC',
  'sng_4j_eleCH_3b/fitted_dijet_M_high_down_type_jet_b_tagged_DNN_High_passMVA/histo_MC',
  #'sng_4j_muCH_3b/fitted_dijet_M_down_type_jet_b_tagged_DNN_Low/histo_MC',
  #'sng_4j_eleCH_3b/fitted_dijet_M_down_type_jet_b_tagged_DNN_Low/histo_MC',
  #'sng_4j_muCH_3b/fitted_dijet_M_high_down_type_jet_b_tagged_DNN_High/histo_MC',
  #'sng_4j_eleCH_3b/fitted_dijet_M_high_down_type_jet_b_tagged_DNN_High/histo_MC',
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

nameMC= map(lambda x: x.split('/')[0], nameNominal)


legendName=[]
for name in nameNominal:
  if 'sng_4j_eleCH_2b' in name:
    outLegendName = '1e, 2b, '
  elif 'sng_4j_muCH_2b' in name:
    outLegendName = '1#mu, 2b, '
  elif 'sng_4j_eleORmuCH_2b' in name:
    outLegendName = '1l, 2b,'
  elif 'sng_4j_eleCH_3b' in name:
    outLegendName = '1e, #geq3b, '
  elif 'sng_4j_muCH_3b' in name:
    outLegendName = '1#mu, #geq3b, '
  elif 'sng_4j_eleORmuCH_3b' in name:
    outLegendName = '1l, #geq3b, '
  elif 'dbl_4j_ee' in name:
    outLegendName = 'ee, '
  elif 'dbl_4j_em' in name:
    outLegendName = 'e#mu, '
  elif 'dbl_4j_me' in name:
    outLegendName = '#mu e, '
  elif 'dbl_4j_mm' in name:
    outLegendName = '#mu #mu, '
  elif 'dbl_4j_eeORmmORemORme' in name:
    outLegendName = '2l, '

  if 'histo_MC' in name:
    outLegendName += 'Bkgs.'
  elif 'histo_CHToCB' in name:
    for mass in signal_samples:
      if mass in name:
        outLegendName += mass.replace('CHToCB_', '')
        break
  legendName.append(outLegendName)

varName=[]
outputDirPlots=[]
drawYields=[]
for name in nameNominal:
  if 'sng_4j' in name:
    varName.append('#it{M_{jj}} [GeV]')
    outputDirPlots.append('plots_Mjj')
  else:
    varName.append('Bins')
    outputDirPlots.append('plots_disc')
  drawYields.append('0')

max_ratio=[]
for name in nameNominal:
  max_ratio.append(1.2)
#max_ratio=[None]*20


nameNominal    =  nameNominal     * len(nuisances)
nameMC         =  nameMC          * len(nuisances)
legendName     =  [ '{}, {}'.format(name, nuis) for nuis in nuisances for name in legendName ]
varName        =  varName         * len(nuisances)
outputDirPlots =  outputDirPlots  * len(nuisances)
drawYields     =  drawYields      * len(nuisances)
max_ratio      =  max_ratio       * len(nuisances)

mergedFile = 'hadd_merged_{}.root'.format(opt.year)

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
    DrawNuisances(mergedFile,mergedFile,nameNominal_,nameUp_,nameDown_,nameMC_,legendName_,varName_,outputDirPlots_,drawYields_,drawMC_,max_ratio_,opt.year)

  if makeTable:
    maketable.addEntry(mergedFile,mergedFile,nameNominal_,nameUp_,nameDown_,legendName_)
    maketable.makeTable()

if makeTable:
  maketable.saveTable("{}_ver1".format(opt.year))
