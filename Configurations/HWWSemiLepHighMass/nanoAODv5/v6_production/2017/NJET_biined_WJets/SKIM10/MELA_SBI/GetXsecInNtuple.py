import ROOT
ROOT.gROOT.SetBatch(True)

def GetXsecInNtuple(path):
    myfile=ROOT.TFile.Open(path)
    mytree=myfile.Get("Events")
    mytree.Draw("Xsec")
    htemp = ROOT.gPad.GetPrimitive("htemp");
    myxsec=htemp.GetMean()
    myfile.Close()
    del htemp
    return float(myxsec)



if __name__ == '__main__':
    #A=GetXsecInNtuple('/xrootd_user/jhchoi/xrootd/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSkimJHv6_7/nanoLatino_DYJetsToLL_M-50__part0.root')
    #print A
    from LatinoAnalysis.Tools.commonTools import *
    xrootdPath = 'root://cms-xrdr.private.lo:2094'
    treeBaseDir = "/xrootd/store/user/jhchoi/Latino/HWWNano/"
    ##--Set Campaign and Step--##
    CAMPAIGN='Fall2017_102X_nAODv5_Full2017v6'
    STEP="MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__BWReweight__HMFull_jhchoi10_nom"
    directory=treeBaseDir+CAMPAIGN+'/'+STEP
    samples={}
    from XsecPowheg import XSEC as XsecPowheg
    List_MX=[140,200,400,700,900,2000]
    for MX in List_MX:
        samples['ggHWWlnuqq_M'+str(MX)] = { 'name'  :getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_')}
        powheg=float(XsecPowheg[str(MX)])
        latino=float(GetXsecInNtuple(samples['ggHWWlnuqq_M'+str(MX)]['name'][0].replace("###","")))
        #XsecPowheg
        #print "---",MX,"---" 
        #print 'powheg,latino,po/la = ',powheg,latino,float(powheg/latino)
        print MX,':',float(powheg/latino),','
