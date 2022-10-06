#!/usr/bin/python



def MergeTTMC(input_f,output_f,histo_dir):

  samples = [
      'TTLJ_jj','TTLJ_bj','TTLJ_bb','TTLJ_cc',
      'TTLL_jj','TTLL_bj','TTLL_bb','TTLL_cc',
      ]
  
  # input dir ex) sng_4j_muCH_2b/fitted_dijet_M/histo_TT
  # input histo_dir
  
  histoName = histo_dir.split('/')[-1]
  histo_dir_list = [ histo_dir.replace('histo_TT', 'histo_' + sample) for sample in samples ] 
  histo_list     = [ input_f.Get(histo_dir) for histo_dir in histo_dir_list ]
  
  out_histo = histo_list[0].Clone(histoName)
  print('merge_ttmc, histoName: ' + histoName)
  for histo in histo_list[1:]:
    out_histo.Add(histo)
  
  output_f.cd()
  outdir = '/'.join(histo_dir.split('/')[:-1])
  print('merge_ttmc, outdir: ' + outdir)
  if not output_f.GetDirectory(outdir):
    output_f.mkdir(outdir)
  output_f.cd(outdir)
  out_histo.Write()


