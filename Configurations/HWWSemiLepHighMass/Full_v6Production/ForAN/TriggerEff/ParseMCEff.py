import ROOT
import os



def ParseShapeOutput(Year,histopath,processes,eleEtaBins,elePtBins):
    #histopath='2016/NotSCrootFile_2016TriggerEff/hadd.root'
    
    #processes=['DY','Wjets0j','Wjets1j','Wjets2j']
    lep='ele'
    #elePtBins=[0., 30., 35., 36.,37.,38.,40.,42.,45.,50.,65.,70.,80.,100.,200.,]
    #eleEtaBins=[-2.5, -2.1, -1.570, -1.440, -0.800, 0., 0.800, 1.440, 1.570, 2.100, 2.500]


    ##--Read
    myfile=ROOT.TFile.Open(histopath)
    
    Eff={}
    

    
    for ieta in range(0,len(eleEtaBins)-1):        
        
        for ipt in range(0,len(elePtBins)-1):
            etalow=eleEtaBins[ieta]
            etahigh=eleEtaBins[ieta+1]
            
            ptlow=elePtBins[ipt]
            pthigh=elePtBins[ipt+1]
            
            
            if not etalow in Eff : Eff[etalow]={}
            if not ptlow in Eff[etalow] : Eff[etalow][ptlow]={}
            #Eff[etalow][ptlow]===>return eff
            

            
    for ieta in range(0,len(eleEtaBins)-1):
        for ipt in range(0,len(elePtBins)-1):
            
            h=ROOT.TH1D()
            
            
            etalow=eleEtaBins[ieta]
            etahigh=eleEtaBins[ieta+1]
            
            ptlow=elePtBins[ipt]
            pthigh=elePtBins[ipt+1]
            
            
            for iproc in range(0,len(processes)):
                process=processes[iproc]
                cutname=lep+'CH'+'__'+'elePtBin'+str(ipt)+'__'+'eleEtaBin'+str(ieta)
                variable=lep+'TrigMatch'
                histoname='histo_'+process        
                htemp=myfile.Get(cutname+'/'+variable+'/'+histoname)
                #print cutname+'/'+variable+'/'+histoname
                if iproc==0:
                    h=htemp.Clone()
                else:
                    h.Add(htemp)

            #effMC=h.GetMean()
            Pass=h.GetBinContent(2)
            PassErr=h.GetBinError(2)
            Fail=h.GetBinContent(1)
            
            eff=Pass/(Pass+Fail)
            err=PassErr/(Pass+Fail)
            
            #print effMC
            #print etalow,etahigh,ptlow,pthigh,eff,err
            
            Eff[etalow][ptlow]['eff']=eff
            Eff[etalow][ptlow]['errlow']=err
            Eff[etalow][ptlow]['errhigh']=err
    ##--SaveOutput
    
    #Year=2016
    
    os.system('mkdir -p EffOutput/')
    outputname='EffOutput/'+str(Year)+'__'.join(processes)+'.py'
    f=open(outputname,'w')
    f.write('TrigEffMC='+str(Eff))
    f.close()



if __name__ == '__main__':
    ##--


    
    #Year=2016
    #histopath='2016/NotSCrootFile_2016TriggerEff/hadd.root'
    #histopath='2016/rootFile_2016TriggerEff/hadd.root'
    dict_MC={
        '2016':{
            'histopath':'2016/rootFile_2016TriggerEff/hadd.root',
            'elePtBins':[0., 25., 26.,27.,29.,31.,34., 37.,40.,50.,100.],
            'eleEtaBins':[-2.5, -2.1, -1.570, -1.440, -0.800, 0., 0.800, 1.440, 1.570, 2.100, 2.500],
            },
        '2017':{
            'histopath':'2017/rootFile_2017TriggerEff/hadd.root',
            'elePtBins':[0., 30., 35., 36.,37.,38.,40.,42.,45.,50.,65.,70.,80.,100.,200.,],
            'eleEtaBins':[-2.5, -2.1, -1.570, -1.440, -0.800, 0., 0.800, 1.440, 1.570, 2.100, 2.500],
        },
        '2018':{
            'histopath':'2018/rootFile_2018TriggerEff/hadd.root',
            'elePtBins':[0., 30.,32.,33.,34., 35., 36.,37.,38.,40.,42.,45.,50., 60., 100., 200.,],
            'eleEtaBins':[-2.5, -2.1, -1.570, -1.440, -0.800, 0., 0.800, 1.440, 1.570, 2.100, 2.500],
        },
    }
    processes=['DY','Wjets0j','Wjets1j','Wjets2j']
    for Year in dict_MC:
        print Year
        histopath=dict_MC[Year]['histopath']
        elePtBins=dict_MC[Year]['elePtBins']
        eleEtaBins=dict_MC[Year]['eleEtaBins']
        if not os.path.isfile(histopath) : continue
        ParseShapeOutput(Year,histopath,processes,eleEtaBins,elePtBins)
    
