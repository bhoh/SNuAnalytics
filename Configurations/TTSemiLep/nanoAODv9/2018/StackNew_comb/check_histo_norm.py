import ROOT
#plots_2018_SKIM7_mva_ALL_TTLJ.0.root
for i in range(94):
    name = 'rootFile_2018_SKIM7_mva/plots_2018_SKIM7_mva_ALL_TTLJ.%d.root'%i
    f = ROOT.TFile(name,"READ")
    if f.IsOpen():
        h   = f.Get('sng_4j_eleORmuCH_2b/fitted_dijet_M/histo_TTLJ_jj')
        hUp = f.Get('sng_4j_eleORmuCH_2b/fitted_dijet_M/histo_TTLJ_jj_jer_2018Up')
        hDo = f.Get('sng_4j_eleORmuCH_2b/fitted_dijet_M/histo_TTLJ_jj_jer_2018Down')

        print(i, h.Integral(), hUp.Integral(), hDo.Integral())
        #print(h.Integral())
    else:
        pass
    f.Close()
