import ROOT
import math
if __name__ == '__main__':
    #sig_MEKD_Bst_C_0.1_M1500;1
    finput='RESULT_Boost/ele/ggf_signal_M1500/ROC_Obj_MEKD_Bst_C_0.1_M1500.root'
    f=ROOT.TFile.Open(finput)
    hsig=f.Get("sig_MEKD_Bst_C_0.1_M1500")
    hbkg=f.Get("bkg_MEKD_Bst_C_0.1_M1500")
    
    max_significance=-1
    cut=-1
    Nbins=hbkg.GetNbinsX()
    print "Nbins",Nbins
    for i in range(0,Nbins+1):

        #weight=hbkg.GetBinContent(i)
        bkgpass=hbkg.Integral(i,Nbins)
        sigpass=hsig.Integral(i,Nbins)
        score=hbkg.GetBinLowEdge(i)
        significance=0
        if bkgpass+sigpass>0:
            significance=sigpass/math.sqrt(bkgpass+sigpass)
        else:
            significance=0
        #print 'bkgpass,sigpass,score,significance=',bkgpass,sigpass,score,significance
        if significance > max_significance:
            max_significance = significance
            cut=score
        #if weight<0:weight=0

        #weight=hsig.GetBinContent(i)
        #score=hsig.GetBinCenter(i)
        #if weight<0:weight=0
    print 'cut,max_significance=',cut,max_significance
        




def my1st():
    ginput=''
    gname=''
    Integral_bkg=100
    Integral_sig=1
    f=ROOT.TFile.Open(ginput)
    gr=f.Get("MEKD_Bst_C_0.000003_M1500")
    n=gr.GetN()

    max_significance=-1
    sig_max=-1
    bkg_max=-1
    for i in range(n):
        bkg=(1-GetPointX(i))*Integral_bkg
        sig=(GetPointY(i))*Integral_sig
        significance=sig/math.sqrt(sig+bkg)
        if significance>max_significance:
            max_significance=significance
            sig_max=sig
            bkg_max=bkg



