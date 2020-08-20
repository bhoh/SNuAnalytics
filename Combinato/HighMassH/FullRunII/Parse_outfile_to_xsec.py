##--
import os 
def ExportLimit(path,result):
    dirpath=path.split('/')[-2]
    if not os.path.isdir(dirpath):os.system('mkdir -p '+dirpath)
        
    f=open(path,'w')
    f.write('XWW='+str(result))
    f.close()

def GetLimit(Method,outfile):
    #print "<GetLimit>"
    #print outfile
    
    f= open(outfile,'r')
    lines=f.readlines()
    doRead=False
    
    obs=0
    exp2p5=0
    exp16=0
    exp50=0
    exp84=0
    exp97p5=0

    for line in lines:
        #print line
        if 'AsymptoticLimits ( CLs )' in line:
            doRead=True
            continue
        if line.replace(' ','')=='\n': continue ##pass empty line
        if doRead:
            
            value=line.split()[-1]
            if 'Observed Limit' in line:
                obs=value
            elif 'Expected  2.5%' in line:
                exp2p5=value
            elif 'Expected 16.0%' in line:
                exp16=value
            elif 'Expected 50.0%' in line:
                exp50=value
            elif 'Expected 84.0%' in line:
                exp84=value
            elif 'Expected 97.5%' in line:
                exp97p5=value
    f.close()
    return obs,exp2p5,exp16,exp50,exp84,exp97p5


##--
def ExportLimitByfvbf(fvbf,interference=True):
    import glob
    Method='AsymptoticLimit'
    #fvbf='ggfonly'
    # -- AsymptoticLimits ( CLs ) --
    #Observed Limit: sigma < 0.3919
    #Expected  2.5%: sigma < 0.2055
    #Expected 16.0%: sigma < 0.2786
    #Expected 50.0%: sigma < 0.3926
    #Expected 84.0%: sigma < 0.5506
    #Expected 97.5%: sigma < 0.7390
    
    #outputdir='WORKDIR__'+Method+'__ggfonly'
    outputdir='WORKDIR__'+Method+'__'+fvbf
    
    #massdir='AsymptoticLimit__ggfonly__ALLchannel__commbine__300__2016'
    #massdir=Method+'__'+fvbf+'__ALLchannel__commbine__300__2016'
    
    massdirs=glob.glob(outputdir+'/'+Method+'__'+fvbf+'*/')
    
    
    Result={}
    BestLimit={}    
    

    suffix=''
    for massdir in massdirs:
        if interference:
            if 'NoI' in massdir : 
                continue 
        else:
            suffix='_NoI'
            if not 'NoI' in massdir :
                continue
                
        #massdir='AsymptoticLimit__ggfonly__ALLchannel__commbine__300__2016'
        infos=massdir.split('/')[-2].split('__')
        ch=infos[2]
        bst=infos[3] ##Boosted OR Resolved
        mass=int(infos[4].replace('_NoI',''))
        year=infos[5]
        #print infos
        outfile=massdir+'/*.out'
        outfile=glob.glob(outfile)[0]
        #print outfile
        obs,exp2p5,exp16,exp50,exp84,exp97p5 = GetLimit(Method,outfile)
        if not mass in Result: Result[mass]={}
        if not ch in Result[mass]: Result[mass][ch]={}
        if not bst in Result[mass][ch]: Result[mass][ch][bst]={}
        if not year in Result[mass][ch][bst]: Result[mass][ch][bst][year]={}
        Result[mass][ch][bst][year]['obs']=float(obs)
        Result[mass][ch][bst][year]['exp2p5']=float(exp2p5)
        Result[mass][ch][bst][year]['exp16']=float(exp16)
        Result[mass][ch][bst][year]['exp50']=float(exp50)
        Result[mass][ch][bst][year]['exp84']=float(exp84)
        Result[mass][ch][bst][year]['exp97p5']=float(exp97p5)
        #print obs,exp2p5,exp16,exp50,exp84,exp97p5
        
        
    ##---Take Best 50% expected Limit

        
    for mass in Result:
        #print mass
        limit=9999999999
        #mass=int(mass)
        for ch in Result[mass]:
            for bst in Result[mass][ch]:
                for year in Result[mass][ch][bst]:
                    #limits.append(Result[mass][ch][bst][year]['exp50'])
                    if float(Result[mass][ch][bst][year]['exp50']) < limit and float(Result[mass][ch][bst][year]['exp50'])!=0:
                        if not mass in BestLimit: BestLimit[mass]={}
                            
                        BestLimit[mass]['obs']=Result[mass][ch][bst][year]['obs']
                        BestLimit[mass]['exp2p5']=Result[mass][ch][bst][year]['exp2p5']
                        BestLimit[mass]['exp16']=Result[mass][ch][bst][year]['exp16']
                        BestLimit[mass]['exp50']=Result[mass][ch][bst][year]['exp50']
                        BestLimit[mass]['exp84']=Result[mass][ch][bst][year]['exp84']
                        BestLimit[mass]['exp97p5']=Result[mass][ch][bst][year]['exp97p5']
                        limit=float(Result[mass][ch][bst][year]['exp50'])
                            

    

    #print BestLimit
    
    ExportLimit('BestLimit/'+Method+'__'+fvbf+suffix+'.py',BestLimit)
    ExportLimit('Limit/'+Method+'__'+fvbf+suffix+'.py',Result)

if __name__ == '__main__':
    fvbf_list=['floating','0.5','ggfonly','vbfonly']
    for fvbf in fvbf_list:
        ExportLimitByfvbf(fvbf,True) ## fvbfcase,interference on
        ExportLimitByfvbf(fvbf,False)
