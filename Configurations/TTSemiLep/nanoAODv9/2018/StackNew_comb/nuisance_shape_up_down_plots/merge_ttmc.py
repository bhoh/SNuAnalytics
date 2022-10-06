#!/usr/bin/python



def MergeTTMC(input_f,output_f,histo_dir, histo_dir_alt):

  samples = [
      'TTLJ_jj','TTLJ_bj','TTLJ_bb','TTLJ_cc',
      'TTLL_jj','TTLL_bj','TTLL_bb','TTLL_cc',
      'ST', 'Wjets', 'DY', 'QCD', 'WW', 'WZ', 'ZZ',
      'TTZjets', 'TTWjets', 'ttH',
      ]
  
  # input dir ex) sng_4j_muCH_2b/fitted_dijet_M/histo_TT
  # input histo_dir
  
  histoName = histo_dir.split('/')[-1]
  #histoName_alt = histo_dir_alt.split('/')[-1]
  #merge TTMC
  histo_dir_list = [ histo_dir.replace('histo_MC', 'histo_' + sample) for sample in samples if not 'CHToCB' in sample ]
  histo_dir_list_alt = [ histo_dir_alt.replace('histo_MC', 'histo_' + sample) for sample in samples  if not 'CHToCB' in sample ]

  def getHist(histo_dir_pair):
    histo_dir     = histo_dir_pair[0]
    histo_dir_alt = histo_dir_pair[1]
    hist = input_f.Get(histo_dir)
    if not hist:
      hist = input_f.Get(histo_dir_alt)
      print('use alt histos: ', histo_dir_pair)
    return hist

  histo_list     = map(getHist, zip(histo_dir_list, histo_dir_list_alt))
  
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

def CopyHisto(input_f,output_f,histo_dir, histo_dir_alt):

  
  # input dir ex) sng_4j_muCH_2b/fitted_dijet_M/histo_TT
  # input histo_dir
  
  histoName = histo_dir.split('/')[-1]
  #histoName_alt = histo_dir_alt.split('/')[-1]
  #merge TTMC
  histo_dir_list = [ histo_dir ]
  histo_dir_list_alt = [ histo_dir_alt ]

  def getHist(histo_dir_pair):
    histo_dir     = histo_dir_pair[0]
    histo_dir_alt = histo_dir_pair[1]
    hist = input_f.Get(histo_dir)
    if not hist:
      hist = input_f.Get(histo_dir_alt)
      print('use alt histos: ', histo_dir_pair)
    return hist

  histo_list     = map(getHist, zip(histo_dir_list, histo_dir_list_alt))
  
  out_histo = histo_list[0].Clone(histoName)
  print('merge_signal, histoName: ' + histoName)
  for histo in histo_list[1:]:
    out_histo.Add(histo)
  
  output_f.cd()
  outdir = '/'.join(histo_dir.split('/')[:-1])
  print('merge_signal, outdir: ' + outdir)
  if not output_f.GetDirectory(outdir):
    output_f.mkdir(outdir)
  output_f.cd(outdir)
  out_histo.Write()


