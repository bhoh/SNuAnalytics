import ROOT
import numpy as np

fName_noBtag = 'rootFile_2018_SKIM9_noBtagSF/hadd.root'
fName_Btag   = 'rootFile_2018_SKIM9_BtagSF/hadd.root'

f_noBtag = ROOT.TFile(fName_noBtag, "READ")
f_Btag   = ROOT.TFile(fName_Btag,   "READ")

varName  = 'nCleanJet25_2p4'
hName_1l = 'sng_4j_eleORmuCH/nCleanJet25_2p4/histo_TTLJ'
hName_2l = 'dbl_4j_eeORmmORemORme_offZ/nCleanJet25_2p4/histo_TTLL'


h_noBtag_1l = f_noBtag.Get(hName_1l)
h_noBtag_2l = f_noBtag.Get(hName_2l)
h_Btag_1l   = f_Btag.  Get(hName_1l)
h_Btag_2l   = f_Btag.  Get(hName_2l)

h_noBtag_1l.Divide(h_Btag_1l)
h_noBtag_2l.Divide(h_Btag_2l)

def printFormula(ratio, template):
    nBinsX = ratio.GetNbinsX()
    ratio_list = []
    ratio_err_list = []
    for i in range(nBinsX):
        binIdx = i+1
        ratio_list.append(ratio.GetBinContent(binIdx))
        ratio_err_list.append(ratio.GetBinError(binIdx))

    np_ratio     = np.array(ratio_list)
    np_ratio_err = np.array(ratio_err_list)

    np_ratio_up   = (np_ratio+np_ratio_err)/(np_ratio)
    np_ratio_down = (np_ratio-np_ratio_err)/(np_ratio)

    getFormula = lambda np_ratio: template.format(VAR=varName,
                                            r2=np_ratio[2],
                                            r3=np_ratio[3],
                                            r4=np_ratio[4],
                                            r5=np_ratio[5],
                                            r6=np_ratio[6],
                                            r7=np_ratio[7])

    formula      = getFormula(np_ratio)
    formula_up   = getFormula(np_ratio_up)
    formula_down = getFormula(np_ratio_down)

    #print("print ratio")
    #print(ratio_list)
    #print("print ratio err.")
    #print(ratio_err_list)
    print("print formula")
    print(formula)
    #print("print formula up")
    #print(formula_up)
    #print("print formula down")
    #print(formula_down)

    return ratio_list, ratio_err_list

template1 = "({VAR}<4)*(1.) + ({VAR}==4)*({r2}) + ({VAR}==5)*({r3}) + ({VAR}==6)*({r4}) + ({VAR}==7)*({r5}) + ({VAR}==8)*({r6}) + ({VAR}>=9)*({r7})"
template2 = "{r2:.4f} & {r3:.4f} & {r4:.4f} & {r5:.4f} & {r6:.4f} & {r7:.4f}"
print("################################ l1")
printFormula(h_noBtag_1l, template1)
printFormula(h_noBtag_1l, template2)
print("################################ l2")
printFormula(h_noBtag_2l, template1)
printFormula(h_noBtag_2l, template2)


