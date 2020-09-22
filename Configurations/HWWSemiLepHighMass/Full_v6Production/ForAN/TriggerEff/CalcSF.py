import ROOT



def CalcSF(EffDataPy,EffMCPy):
    #EffMCPy='EffOutput/2017DY__Wjets0j__Wjets1j__Wjets2j.py'
    
    #EffDataPy='EffOutput/2017B__Data.py'


    #exec('from '+EffMCPy+' import Eff as EffMC')
    #exec('from '+EffDataPy+' import Eff as EffData')
    
    ##--Read 
    fMC=open(EffMCPy,'r')
    exec(fMC)
    fMC.close()
    
    fData=open(EffDataPy,'r')
    exec(fData)
    fData.close()
    
    
    ptbins=[]
    etabins=[]
    for eta in TrigEffMC:
        for pt in TrigEffMC[eta]:
            ptbins.append(pt)
            etabins.append(eta)

    ptbins=sorted(list(set(ptbins)))
    etabins=sorted(list(set(etabins)))
    
    
    TrigSF={}
    
    for eta in etabins:
        print 'eta=',eta
        for pt in ptbins:
            if not eta in TrigSF:TrigSF[eta]={}
            if not pt in TrigSF[eta] : TrigSF[eta][pt]={}
            #TrigEffData[eta][pt]
            
            MCnom=TrigEffMC[eta][pt]['eff']
            MCup=MCnom+TrigEffMC[eta][pt]['errhigh']
            MCdown=MCnom-TrigEffMC[eta][pt]['errlow']
            
            Datanom=TrigEffData[eta][pt]['eff']
            Dataup=Datanom+TrigEffData[eta][pt]['errhigh']
            Datadown=Datanom-TrigEffData[eta][pt]['errlow']
        
        
            SF=Datanom/MCnom
            SFhigh=Dataup/MCdown
            SFlow=Datadown/MCup
            
            TrigSF[eta][pt]['SF']=SF
            TrigSF[eta][pt]['SFhigh']=SFhigh
            TrigSF[eta][pt]['SFlow']=SFlow
            
            
            print pt,'|',SF,SFlow,SFhigh


if __name__ == '__main__':
    

    EffMCPy='EffOutput/2017DY__Wjets0j__Wjets1j__Wjets2j.py'

    EffDataPy='EffOutput/2017F__Data.py'
    CalcSF(EffDataPy,EffMCPy)
