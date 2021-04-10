import ROOT
import os
import copy

inFileName  = '../rootFile_2016_SKIM7_final/PDF/results_unc.root'
outFileName = 'hadd_data_driven.root'
abcdFileName = 'ABCD_data_driven_shape.root'

from ABCD_data_driven_shape import input_dict

# copy original root file
os.system('cp %s %s'%(inFileName, outFileName))
outFile  = ROOT.TFile(outFileName,"UPDATE")
abcdFile = ROOT.TFile(abcdFileName,"READ")

input_dict['qcd_envelop_btagUp']   = copy.deepcopy(input_dict[''])
input_dict['qcd_envelop_btagDown'] =  copy.deepcopy(input_dict[''])
input_dict['qcd_envelop_tt_hfUp']   = copy.deepcopy(input_dict[''])
input_dict['qcd_envelop_tt_hfDown'] =  copy.deepcopy(input_dict[''])

for tag_key, tag in input_dict.iteritems():
  for ch, var_dict in tag['chennels'].iteritems():
    for var in var_dict:
      new_histo_suffix = tag_key
      if tag_key == '':
        abcd_hist_path      = '%s/%s/%s'%(ch,var,'histo_QCD_data_driven')
      elif 'iso' in tag_key:
        ch_ = ch.replace('sng_4j_D_','').replace('eleCH','e').replace('muCH','m').replace('_2b','').replace('_3b','')
        new_histo_suffix = 'iso_%s%s'%(ch_,tag_key.replace('isoVar',''))
        abcd_hist_path      = '%s/%s/%s'%(ch,var,'histo_QCD_data_driven_' + new_histo_suffix)
      elif 'binning' in tag_key:
        ch_ = ch.replace('sng_4j_D_','').replace('eleCH','e').replace('muCH','m')
        year = '2016'
        new_histo_suffix = 'binning_%s_%s%s'%(ch_,year,tag_key.replace('binningVar',''))
        abcd_hist_path      = '%s/%s/%s'%(ch,var,'histo_QCD_data_driven_' + new_histo_suffix)
      else:
        abcd_hist_path      = '%s/%s/%s'%(ch,var,'histo_QCD_data_driven_' + new_histo_suffix)
      abcd_hist      = abcdFile.Get(abcd_hist_path)
      target_hist_path = '%s/%s'%(ch.replace('_D_','_'),var)
      outFile.cd(target_hist_path)
      if tag_key == '':
        cloned_hist = abcd_hist.Clone('histo_QCD_data_driven')
      else:
        cloned_hist = abcd_hist.Clone('histo_QCD_data_driven_' + new_histo_suffix)
      if tag_key == '':
        cloned_hist.Write('histo_QCD_EM',ROOT.TObject.kOverwrite)
        cloned_hist.Scale(0.)
        cloned_hist.Write('histo_QCD_bcToE',ROOT.TObject.kOverwrite)
        cloned_hist.Write('histo_QCD_MU',ROOT.TObject.kOverwrite)
      else:
        cloned_hist.Write('histo_QCD_EM_' + new_histo_suffix,ROOT.TObject.kOverwrite)
        cloned_hist.Scale(0.)
        cloned_hist.Write('histo_QCD_bcToE_' + new_histo_suffix,ROOT.TObject.kOverwrite)
        cloned_hist.Write('histo_QCD_MU_' + new_histo_suffix,ROOT.TObject.kOverwrite)





