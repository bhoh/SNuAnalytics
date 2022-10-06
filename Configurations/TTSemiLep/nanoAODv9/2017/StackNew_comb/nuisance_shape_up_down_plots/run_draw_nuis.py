#!/usr/bin/python
import os
import ROOT

os.system('mkdir -p plots_Mjj/cc_sng_4j_muCH_2b/fitted_dijet_M')
os.system('mkdir -p plots_Mjj/cc_sng_4j_eleCH_2b/fitted_dijet_M')
os.system('mkdir -p plots_Mjj/cc_sng_4j_muCH_3b/fitted_dijet_M_down_type_jet_b_tagged')
os.system('mkdir -p plots_Mjj/cc_sng_4j_eleCH_3b/fitted_dijet_M_down_type_jet_b_tagged')

os.system('mkdir -p plots_disc/cc_dbl_4j_ee/3_4rd_leading_b_disc')
os.system('mkdir -p plots_disc/cc_dbl_4j_em/3_4rd_leading_b_disc')
os.system('mkdir -p plots_disc/cc_dbl_4j_me/3_4rd_leading_b_disc')
os.system('mkdir -p plots_disc/cc_dbl_4j_mm/3_4rd_leading_b_disc')

os.system('mkdir -p plots_Mjj/log_cc_sng_4j_muCH_2b/fitted_dijet_M')
os.system('mkdir -p plots_Mjj/log_cc_sng_4j_eleCH_2b/fitted_dijet_M')
os.system('mkdir -p plots_Mjj/log_cc_sng_4j_muCH_3b/fitted_dijet_M_down_type_jet_b_tagged')
os.system('mkdir -p plots_Mjj/log_cc_sng_4j_eleCH_3b/fitted_dijet_M_down_type_jet_b_tagged')


os.system('mkdir -p plots_disc/log_cc_dbl_4j_ee/3_4rd_leading_b_disc')
os.system('mkdir -p plots_disc/log_cc_dbl_4j_em/3_4rd_leading_b_disc')
os.system('mkdir -p plots_disc/log_cc_dbl_4j_me/3_4rd_leading_b_disc')
os.system('mkdir -p plots_disc/log_cc_dbl_4j_mm/3_4rd_leading_b_disc')

inputFile='/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv7/2017/StackNew_comb/rootFile_2017_SKIM7_final/hadd.root'
inputFile_MC='/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv7/2017/StackNew_comb/rootFile_2017_SKIM7_final/hadd.root'
nameNominal=[
  'sng_4j_muCH_2b/fitted_dijet_M/histo_TT',
  'sng_4j_eleCH_2b/fitted_dijet_M/histo_TT',
  'sng_4j_muCH_3b/fitted_dijet_M_down_type_jet_b_tagged/histo_TT',
  'sng_4j_eleCH_3b/fitted_dijet_M_down_type_jet_b_tagged/histo_TT',
  'dbl_4j_ee/3_4rd_leading_b_disc/histo_TT',
  'dbl_4j_em/3_4rd_leading_b_disc/histo_TT',
  'dbl_4j_me/3_4rd_leading_b_disc/histo_TT',
  'dbl_4j_mm/3_4rd_leading_b_disc/histo_TT',

  'sng_4j_muCH_2b/fitted_dijet_M/histo_TT',
  'sng_4j_eleCH_2b/fitted_dijet_M/histo_TT',
  'sng_4j_muCH_3b/fitted_dijet_M_down_type_jet_b_tagged/histo_TT',
  'sng_4j_eleCH_3b/fitted_dijet_M_down_type_jet_b_tagged/histo_TT',
  'dbl_4j_ee/3_4rd_leading_b_disc/histo_TT',
  'dbl_4j_em/3_4rd_leading_b_disc/histo_TT',
  'dbl_4j_me/3_4rd_leading_b_disc/histo_TT',
  'dbl_4j_mm/3_4rd_leading_b_disc/histo_TT',

  'sng_4j_muCH_2b/fitted_dijet_M/histo_TT',
  'sng_4j_eleCH_2b/fitted_dijet_M/histo_TT',
  'sng_4j_muCH_3b/fitted_dijet_M_down_type_jet_b_tagged/histo_TT',
  'sng_4j_eleCH_3b/fitted_dijet_M_down_type_jet_b_tagged/histo_TT',
  'dbl_4j_ee/3_4rd_leading_b_disc/histo_TT',
  'dbl_4j_em/3_4rd_leading_b_disc/histo_TT',
  'dbl_4j_me/3_4rd_leading_b_disc/histo_TT',
  'dbl_4j_mm/3_4rd_leading_b_disc/histo_TT',

]
nameUp=[
  'sng_4j_muCH_2b/fitted_dijet_M/histo_TT_TuneCP5Up',
  'sng_4j_eleCH_2b/fitted_dijet_M/histo_TT_TuneCP5Up',
  'sng_4j_muCH_3b/fitted_dijet_M_down_type_jet_b_tagged/histo_TT_TuneCP5Up',
  'sng_4j_eleCH_3b/fitted_dijet_M_down_type_jet_b_tagged/histo_TT_TuneCP5Up',
  'dbl_4j_ee/3_4rd_leading_b_disc/histo_TT_TuneCP5Up',
  'dbl_4j_em/3_4rd_leading_b_disc/histo_TT_TuneCP5Up',
  'dbl_4j_me/3_4rd_leading_b_disc/histo_TT_TuneCP5Up',
  'dbl_4j_mm/3_4rd_leading_b_disc/histo_TT_TuneCP5Up',

  'sng_4j_muCH_2b/fitted_dijet_M/histo_TT_hdampUp',
  'sng_4j_eleCH_2b/fitted_dijet_M/histo_TT_hdampUp',
  'sng_4j_muCH_3b/fitted_dijet_M_down_type_jet_b_tagged/histo_TT_hdampUp',
  'sng_4j_eleCH_3b/fitted_dijet_M_down_type_jet_b_tagged/histo_TT_hdampUp',
  'dbl_4j_ee/3_4rd_leading_b_disc/histo_TT_hdampUp',
  'dbl_4j_em/3_4rd_leading_b_disc/histo_TT_hdampUp',
  'dbl_4j_me/3_4rd_leading_b_disc/histo_TT_hdampUp',
  'dbl_4j_mm/3_4rd_leading_b_disc/histo_TT_hdampUp',

  'sng_4j_muCH_2b/fitted_dijet_M/histo_TT_mtop_weightUp',
  'sng_4j_eleCH_2b/fitted_dijet_M/histo_TT_mtop_weightUp',
  'sng_4j_muCH_3b/fitted_dijet_M_down_type_jet_b_tagged/histo_TT_mtop_weightUp',
  'sng_4j_eleCH_3b/fitted_dijet_M_down_type_jet_b_tagged/histo_TT_mtop_weightUp',
  'dbl_4j_ee/3_4rd_leading_b_disc/histo_TT_mtop_weightUp',
  'dbl_4j_em/3_4rd_leading_b_disc/histo_TT_mtop_weightUp',
  'dbl_4j_me/3_4rd_leading_b_disc/histo_TT_mtop_weightUp',
  'dbl_4j_mm/3_4rd_leading_b_disc/histo_TT_mtop_weightUp',


]
nameDown=[
  'sng_4j_muCH_2b/fitted_dijet_M/histo_TT_TuneCP5Down',
  'sng_4j_eleCH_2b/fitted_dijet_M/histo_TT_TuneCP5Down',
  'sng_4j_muCH_3b/fitted_dijet_M_down_type_jet_b_tagged/histo_TT_TuneCP5Down',
  'sng_4j_eleCH_3b/fitted_dijet_M_down_type_jet_b_tagged/histo_TT_TuneCP5Down',
  'dbl_4j_ee/3_4rd_leading_b_disc/histo_TT_TuneCP5Down',
  'dbl_4j_em/3_4rd_leading_b_disc/histo_TT_TuneCP5Down',
  'dbl_4j_me/3_4rd_leading_b_disc/histo_TT_TuneCP5Down',
  'dbl_4j_mm/3_4rd_leading_b_disc/histo_TT_TuneCP5Down',

  'sng_4j_muCH_2b/fitted_dijet_M/histo_TT_hdampDown',
  'sng_4j_eleCH_2b/fitted_dijet_M/histo_TT_hdampDown',
  'sng_4j_muCH_3b/fitted_dijet_M_down_type_jet_b_tagged/histo_TT_hdampDown',
  'sng_4j_eleCH_3b/fitted_dijet_M_down_type_jet_b_tagged/histo_TT_hdampDown',
  'dbl_4j_ee/3_4rd_leading_b_disc/histo_TT_hdampDown',
  'dbl_4j_em/3_4rd_leading_b_disc/histo_TT_hdampDown',
  'dbl_4j_me/3_4rd_leading_b_disc/histo_TT_hdampDown',
  'dbl_4j_mm/3_4rd_leading_b_disc/histo_TT_hdampDown',

  'sng_4j_muCH_2b/fitted_dijet_M/histo_TT_mtop_weightDown',
  'sng_4j_eleCH_2b/fitted_dijet_M/histo_TT_mtop_weightDown',
  'sng_4j_muCH_3b/fitted_dijet_M_down_type_jet_b_tagged/histo_TT_mtop_weightDown',
  'sng_4j_eleCH_3b/fitted_dijet_M_down_type_jet_b_tagged/histo_TT_mtop_weightDown',
  'dbl_4j_ee/3_4rd_leading_b_disc/histo_TT_mtop_weightDown',
  'dbl_4j_em/3_4rd_leading_b_disc/histo_TT_mtop_weightDown',
  'dbl_4j_me/3_4rd_leading_b_disc/histo_TT_mtop_weightDown',
  'dbl_4j_mm/3_4rd_leading_b_disc/histo_TT_mtop_weightDown',


]
nameMC=[
  'sng_4j_muCH_2b',
  'sng_4j_eleCH_2b',
  'sng_4j_muCH_3b',
  'sng_4j_eleCH_3b',
  'dbl_4j_ee',
  'dbl_4j_em',
  'dbl_4j_me',
  'dbl_4j_mm',

  'sng_4j_muCH_2b',
  'sng_4j_eleCH_2b',
  'sng_4j_muCH_3b',
  'sng_4j_eleCH_3b',
  'dbl_4j_ee',
  'dbl_4j_em',
  'dbl_4j_me',
  'dbl_4j_mm',

  'sng_4j_muCH_2b',
  'sng_4j_eleCH_2b',
  'sng_4j_muCH_3b',
  'sng_4j_eleCH_3b',
  'dbl_4j_ee',
  'dbl_4j_em',
  'dbl_4j_me',
  'dbl_4j_mm',

]
legendName=[
  '1#mu, 2b, TT TuneCP5',
  '1e, 2b, TT TuneCP5',
  '1#mu, #geq3b, TT TuneCP5',
  '1e, #geq3b, TT TuneCP5',
  'ee, TT TuneCP5',
  'e#mu, TT TuneCP5',
  '#mue, TT TuneCP5',
  '#mu#mu, TT TuneCP5',

  '1#mu, 2b, TT hdamp',
  '1e, 2b, TT hdamp',
  '1#mu, #geq3b, TT hdamp',
  '1e, #geq3b, TT hdamp',
  'ee, TT hdamp',
  'e#mu, TT hdamp',
  '#mue, TT hdamp',
  '#mu#mu, TT hdamp',

  '1#mu, 2b, TT mtop',
  '1e, 2b, TT mtop',
  '1#mu, #geq3b, TT mtop',
  '1e, #geq3b, TT mtop',
  'ee, TT mtop',
  'e#mu, TT mtop',
  '#mue, TT mtop',
  '#mu#mu, TT mtop',


]
varName=[
  '#it{M_{jj}} [GeV]',
  '#it{M_{jj}} [GeV]',
  '#it{M_{jj}} [GeV]',
  '#it{M_{jj}} [GeV]',
  'Bins',
  'Bins',
  'Bins',
  'Bins',

  '#it{M_{jj}} [GeV]',
  '#it{M_{jj}} [GeV]',
  '#it{M_{jj}} [GeV]',
  '#it{M_{jj}} [GeV]',
  'Bins',
  'Bins',
  'Bins',
  'Bins',

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

  'plots_Mjj',
  'plots_Mjj',
  'plots_Mjj',
  'plots_Mjj',
  'plots_disc',
  'plots_disc',
  'plots_disc',
  'plots_disc',

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

  '0',
  '0',
  '0',
  '0',
  '0',
  '0',
  '0',
  '0',

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
  1.1,        
  1.1,        
  1.2,        
  1.2,        
  3.0,        
  1.8,        
  2.5,        
  1.8,        

  1.1,        
  1.1,        
  1.2,        
  1.2,        
  3.0,        
  1.8,        
  2.5,        
  1.8,        

  1.1,        
  1.1,        
  1.2,        
  1.2,        
  3.0,        
  1.8,        
  2.5,        
  1.8,        



]

input_f  = ROOT.TFile(inputFile)
mergedFile = 'hadd_merged.root'
output_f = ROOT.TFile(mergedFile,'RECREATE')
from merge_ttmc import MergeTTMC

for histo_dir in nameNominal + nameUp + nameDown:
  print('merge histo: ' + histo_dir)
  MergeTTMC(input_f,output_f,histo_dir)

input_f.Close()
output_f.Close()




# python
from DrawNuisances import DrawNuisances

ROOT.gROOT.SetBatch(True)

args = zip(nameNominal,nameUp,nameDown,nameMC,legendName,varName,outputDirPlots,drawYields,max_ratio)
drawMC_='0'
for nameNominal_,nameUp_,nameDown_,nameMC_,legendName_,varName_,outputDirPlots_,drawYields_,max_ratio_ in args:
  print(nameNominal_,nameUp_,nameDown_,nameMC_,legendName_,varName_,outputDirPlots_,drawYields_)
  DrawNuisances(mergedFile,mergedFile,nameNominal_,nameUp_,nameDown_,nameMC_,legendName_,varName_,outputDirPlots_,drawYields_,drawMC_,max_ratio_)
