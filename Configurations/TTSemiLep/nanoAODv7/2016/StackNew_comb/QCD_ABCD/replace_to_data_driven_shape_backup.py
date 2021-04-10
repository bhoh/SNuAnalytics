import ROOT
import os
import copy

inFileName  = '../rootFile_2016_SKIM7/PDF/results_unc.root'
outFileName = 'hadd_data_driven.root'
abcdFileName = 'ABCD_data_driven_shape.root'

from ABCD_data_driven_shape import input_dict

# copy original root file
os.system('cp %s %s'%(inFileName, outFileName))
outFile  = ROOT.TFile(outFileName,"UPDATE")
abcdFile = ROOT.TFile(abcdFileName,"READ")

input_dict['qcd_envelopUp']   = copy.deepcopy(input_dict[''])
input_dict['qcd_envelopDown'] =  copy.deepcopy(input_dict[''])

for tag_key, tag in input_dict.iteritems():
  for ch, var_dict in tag['chennels'].iteritems():
    for var in var_dict:
      #XXX  
      if 'btag_' in tag_key and 'CMS_' not in tag_key:
        tag_key = 'CMS_' + tag_key
      if tag_key == '':
        abcd_hist_path      = '%s/%s/%s'%(ch,var,'histo_QCD_data_driven')
      else:
        abcd_hist_path      = '%s/%s/%s'%(ch,var,'histo_QCD_data_driven_' + tag_key)
      abcd_hist      = abcdFile.Get(abcd_hist_path)
      if not abcd_hist:
        print(ch, var, tag_key)
        raise Exception('exception')
      target_hist_path = '%s/%s'%(ch.replace('_D_','_'),var)
      outFile.cd(target_hist_path)
      if tag_key == '':
        cloned_hist = abcd_hist.Clone('histo_QCD_data_driven')
      else:
        cloned_hist = abcd_hist.Clone('histo_QCD_data_driven_' + tag_key)
      if tag_key == '':
        cloned_hist.Write('histo_QCD_EM',ROOT.TObject.kOverwrite)
        cloned_hist.Scale(0.)
        cloned_hist.Write('histo_QCD_bcToE',ROOT.TObject.kOverwrite)
        cloned_hist.Write('histo_QCD_MU',ROOT.TObject.kOverwrite)
      else:
        cloned_hist.Write('histo_QCD_EM_' + tag_key,ROOT.TObject.kOverwrite)
        cloned_hist.Scale(0.)
        cloned_hist.Write('histo_QCD_bcToE_' + tag_key,ROOT.TObject.kOverwrite)
        cloned_hist.Write('histo_QCD_MU_' + tag_key,ROOT.TObject.kOverwrite)





