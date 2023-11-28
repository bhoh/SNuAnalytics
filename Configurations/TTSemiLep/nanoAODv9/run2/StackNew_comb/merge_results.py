import ROOT


#f_out        = ROOT.TFile("results_run2_PostFit_b.root", "RECREATE")
#f_out        = ROOT.TFile("results_run2_PreFit_Low.root", "UPDATE")
#f_out        = ROOT.TFile("results_run2_PreFit_High.root", "UPDATE")

#f_2016HIPM   = ROOT.TFile("results_2016HIPM_PostFit_b.root", "READ")
#f_2016noHIPM = ROOT.TFile("results_2016noHIPM_PostFit_b.root", "READ")
#f_2017       = ROOT.TFile("results_2017_PostFit_b.root", "READ")
#f_2018       = ROOT.TFile("results_2018_PostFit_b.root", "READ")
#
#f_list = [f_2016HIPM, f_2016noHIPM, f_2017, f_2018]






### PATH
# "sng_4j_eleCH_2b"
# "sng_4j_muCH_2b"
# "dbl_4j_ee"
# "dbl_4j_em"
# "dbl_4j_me"
# "dbl_4j_mm"
# 
### VARIABLE
# 
# "DNN_Low_mass"
# "DNN_High_mass"
# "3_4rd_leading_b_disc"
# 
### MERGE
# "DATA"
# "TT+jj"
# "TT+cc"
# "TT+bb"
# "Others"
# "ST"
# "QCD"


def merge(files, channels, variable, samples):
  h_outlist = []
  for sample in samples:
    h_out = None
    for file_ in files:
      for channel in channels:
        h_in = file_.Get(channel + "/" + variable + "/histo_" + sample)
        if h_out == None:
          h_out = h_in.Clone()
        else:
          h_out.Add(h_in)
    h_outlist.append(h_out)
  return h_outlist

def save(fout, dir_name, hist_list):
  if fout.Get(dir_name):
    pass
  else:
    fout.mkdir(dir_name)

  fout.cd(dir_name)
  for hist in hist_list:
    hist.Write(hist.GetName())
  

if __name__ == '__main__':

  with_mass = False

  if with_mass:
    #f_out        = ROOT.TFile("results_run2_PostFit_b_High_mass.root", "UPDATE")
    f_out        = ROOT.TFile("results_run2_PreFit_High_mass.root", "UPDATE")
    f_list = [f_out]
    h_list = merge(f_list, ['sng_4j_eleCH_2b', 'sng_4j_muCH_2b'], 'DNN_High_mass', ['DATA', 'TT+jj', 'TT+cc', 'TT+bb', 'ST', 'QCD', 'Others'])
    save(f_out, 'sng_4j_eleORmuCH_2b/DNN_High_mass', h_list)
    h_list = merge(f_list, ['dbl_4j_ee','dbl_4j_mm','dbl_4j_em','dbl_4j_me'], '3_4rd_leading_b_disc', ['DATA', 'TT+jj', 'TT+cc', 'TT+bb', 'ST',  'Others'])
    save(f_out, 'dbl_4j_eeORmmORemORme_offZ/3_4rd_leading_b_disc', h_list)
    #
    #
    #f_out        = ROOT.TFile("results_run2_PostFit_b_Low_mass.root", "UPDATE")
    f_out        = ROOT.TFile("results_run2_PreFit_Low_mass.root", "UPDATE")
    f_list = [f_out]
    h_list = merge(f_list, ['sng_4j_eleCH_2b', 'sng_4j_muCH_2b'], 'DNN_Low_mass', ['DATA', 'TT+jj', 'TT+cc', 'TT+bb', 'ST', 'QCD', 'Others'])
    save(f_out, 'sng_4j_eleORmuCH_2b/DNN_Low_mass', h_list)
    h_list = merge(f_list, ['dbl_4j_ee','dbl_4j_mm','dbl_4j_em','dbl_4j_me'], '3_4rd_leading_b_disc', ['DATA', 'TT+jj', 'TT+cc', 'TT+bb', 'ST',  'Others'])
    save(f_out, 'dbl_4j_eeORmmORemORme_offZ/3_4rd_leading_b_disc', h_list)
  else:
    #f_out        = ROOT.TFile("results_run2_PostFit_b_High.root", "UPDATE")
    f_out        = ROOT.TFile("results_run2_PreFit_High.root", "UPDATE")
    f_list = [f_out]
    h_list = merge(f_list, ['sng_4j_eleCH_2b', 'sng_4j_muCH_2b'], 'DNN_High', ['DATA', 'TT+jj', 'TT+cc', 'TT+bb', 'ST', 'QCD', 'Others'])
    save(f_out, 'sng_4j_eleORmuCH_2b/DNN_High', h_list)
    h_list = merge(f_list, ['dbl_4j_ee','dbl_4j_mm','dbl_4j_em','dbl_4j_me'], '3_4rd_leading_b_disc', ['DATA', 'TT+jj', 'TT+cc', 'TT+bb', 'ST',  'Others'])
    save(f_out, 'dbl_4j_eeORmmORemORme_offZ/3_4rd_leading_b_disc', h_list)
    #
    #
    #f_out        = ROOT.TFile("results_run2_PostFit_b_Low.root", "UPDATE")
    f_out        = ROOT.TFile("results_run2_PreFit_Low.root", "UPDATE")
    f_list = [f_out]
    h_list = merge(f_list, ['sng_4j_eleCH_2b', 'sng_4j_muCH_2b'], 'DNN_Low', ['DATA', 'TT+jj', 'TT+cc', 'TT+bb', 'ST', 'QCD', 'Others'])
    save(f_out, 'sng_4j_eleORmuCH_2b/DNN_Low', h_list)
    h_list = merge(f_list, ['dbl_4j_ee','dbl_4j_mm','dbl_4j_em','dbl_4j_me'], '3_4rd_leading_b_disc', ['DATA', 'TT+jj', 'TT+cc', 'TT+bb', 'ST',  'Others'])
    save(f_out, 'dbl_4j_eeORmmORemORme_offZ/3_4rd_leading_b_disc', h_list)




