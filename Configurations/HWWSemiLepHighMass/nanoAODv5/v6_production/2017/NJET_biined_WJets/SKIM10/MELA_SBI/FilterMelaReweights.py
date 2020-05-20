import ROOT
from math import sqrt
from LatinoAnalysis.Tools.commonTools import *


def GetMinMaxCut(filelist,model,mode,nsigma=2):
    #Root.gROOT.SetBatch(True)
    
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

##--get cuts for multiple modes
def GetMinMaxCuts(filelist,model,modes=['','_I','_B','_H','_I_HB'],nsigma=2):
    ROOT.gROOT.SetBatch(True)
    
    mydict={}
    for mode in modes:
        mydict[mode]={}
        mydict[mode]['Sum']=0
        mydict[mode]['Sum2']=0
        mydict[mode]['Nentry']=0
        mydict[mode]['Mean']=0
        mydict[mode]['dev']=0
        mydict[mode]['min']=0
        mydict[mode]['max']=0
        
    mydict['Nveto']=0
    mydict['Npass']=0
    mydict['cut']='1'
        #Sum=0
        #Sum2=0
        #Nentry=0

    for f in filelist:
        if '###' in f:
            f=f.replace("###","")
        myfile=ROOT.TFile.Open(f,"read")
        mytree=myfile.Get("Events")
        for mode in modes:
            #print "===="+model+mode+"====="
            mytree.Draw(model+mode)
            #print "after draw"
            htemp=ROOT.gPad.GetPrimitive("htemp")
        
            #print 'MEAN=',htemp.GetMean()
            #print 'DEV =',htemp.GetStdDev()
            #print "Integrals=", htemp.Integral()
            #print "GetEntries=",htemp.GetEntries()
            mydict[mode]['Sum']+=htemp.GetMean()*htemp.GetEntries()
            mydict[mode]['Sum2']+=(htemp.GetStdDev()*htemp.GetStdDev()+htemp.GetMean()*htemp.GetMean())*htemp.GetEntries()
            mydict[mode]['Nentry']+=htemp.GetEntries()
        

        myfile.Close()
        #print "Total MEAN=",Sum/Nentry
        #print "Total DEV=",sqrt((Sum2/Nentry)-(Sum/Nentry)*(Sum/Nentry))
        #print "GetEntries=",Nentry
    for mode in modes:
        mydict[mode]['Mean']=mydict[mode]['Sum']/mydict[mode]['Nentry']
        mydict[mode]['dev']=sqrt((mydict[mode]['Sum2']/mydict[mode]['Nentry'])-(mydict[mode]['Sum']/mydict[mode]['Nentry'])*(mydict[mode]['Sum']/mydict[mode]['Nentry']))
        mydict[mode]['min']=mydict[mode]['Mean']-nsigma*mydict[mode]['dev']
        mydict[mode]['max']=mydict[mode]['Mean']+nsigma*mydict[mode]['dev']

    for mode in modes:
        mydict['cut']+='&&('+model+mode+'<='+str(mydict[mode]['max'])+')&&('+model+mode+'>='+str(mydict[mode]['min'])+')'

    mydict['cut']="("+mydict['cut']+')'
    for f in filelist:
        if '###' in f:
            f=f.replace("###","")
        myfile=ROOT.TFile.Open(f,"read")
        mytree=myfile.Get("Events")
        cut='0'
        for mode in modes:
            #print "===="+model+mode+"====="
            #mytree.Draw(model+mode, model+mode+'>'+str(mydict[mode]['max'])+'||'+model+mode+'<'+str(mydict[mode]['min']))
            cut+='||('+model+mode+'>'+str(mydict[mode]['max'])+')||('+model+mode+'<'+str(mydict[mode]['min'])+')'
        #print cut
        mytree.Draw('abs('+model+mode+')',cut)
        #print "after draw"
            
        htemp=ROOT.gPad.GetPrimitive("htemp")
        #print "veto's mean=",htemp.GetMean()
        try:
            #print "veto's mean=",htemp.GetMean()
            mydict['Nveto']+=htemp.GetEntries()
        except AttributeError:
            #print "veto's mean=0"
            mydict['Nveto']+=0

        cut='1'
        for mode in modes:
            cut+='&&('+model+mode+'<='+str(mydict[mode]['max'])+')&&('+model+mode+'>='+str(mydict[mode]['min'])+')'
        mytree.Draw('1',cut)
        htemp=ROOT.gPad.GetPrimitive("htemp")
        try:
            mydict['Npass']+=htemp.GetEntries()
        except AttributeError:
            mydict['Npass']+=0
        

    return mydict

#def GetStatement(filelist,model,modes=['','_I','_B','_H','_HB'],nsigma=2):
#    dict_min_max=GetMinMaxCuts(filelist,model,modes,nsigma)
    


if __name__ == '__main__':
    SITE=os.uname()[1]
    xrootdPath = 'root://cms-xrdr.private.lo:2094'
    treeBaseDir = "/xrootd/store/user/jhchoi/Latino/HWWNano/"
    
    CAMPAIGN='Fall2017_102X_nAODv5_Full2017v6'
    STEP="MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__BWReweight__HMFull_jhchoi10_nom__HMLHEAna"

    directory=treeBaseDir+CAMPAIGN+'/'+STEP
    import sys
    sys.path.insert(0, "MassPoints")
    from List_MX import *
    from List_MX_VBF import *

    model="cprime1.0BRnew0.0"


    for MX in List_MX:
        print MX
        MELA_cuts=GetMinMaxCuts(getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),model)
        cut=MELA_cuts['cut']
        print cut

    '''
    MX=4000
    mode='_I'
    thisdict=GetMinMaxCuts(getSampleFiles(directory,'GluGluHToWWToLNuQQ_M'+str(MX),False,'nanoLatino_'),'MSSModel',['','_I','_B','_I_HB','_H'])
    vlist=['Mean','Nentry','dev','min','max']
    #,'Nveto','Npass']
    print mode
    for v in vlist:
        print v,thisdict[mode][v]
    print 'Nveto=',thisdict['Nveto']
    print 'Npass=',thisdict['Npass']
    print 'cut=',thisdict['cut']
    '''
