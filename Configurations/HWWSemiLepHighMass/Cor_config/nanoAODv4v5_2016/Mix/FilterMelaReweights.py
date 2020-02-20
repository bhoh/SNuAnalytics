import ROOT
from math import sqrt
from LatinoAnalysis.Tools.commonTools import *


def GetMinMaxCut(filelist,model,mode,nsigma=2):
    ROOT.gROOT.SetBatch(True)
    
    Sum=0
    Sum2=0
    Nentry=0
    print "===="+model+mode+"====="
    for f in filelist:
        if '###' in f:
            f=f.replace("###","")
        myfile=ROOT.TFile.Open(f,"read")
        mytree=myfile.Get("Events")
        
        mytree.Draw(model+mode)
        htemp=ROOT.gPad.GetPrimitive("htemp")
        
        #print 'MEAN=',htemp.GetMean()
        #print 'DEV =',htemp.GetStdDev()
        #print "Integrals=", htemp.Integral()
        #print "GetEntries=",htemp.GetEntries()
        Sum+=htemp.GetMean()*htemp.GetEntries()
        Sum2+=(htemp.GetStdDev()*htemp.GetStdDev()+htemp.GetMean()*htemp.GetMean())*htemp.GetEntries()
        Nentry+=htemp.GetEntries()
        myfile.Close()
    #print "Total MEAN=",Sum/Nentry
    #print "Total DEV=",sqrt((Sum2/Nentry)-(Sum/Nentry)*(Sum/Nentry))
    #print "GetEntries=",Nentry
    Mean=Sum/Nentry
    dev=sqrt((Sum2/Nentry)-(Sum/Nentry)*(Sum/Nentry))
    return Mean-nsigma*dev, Mean+nsigma*dev

