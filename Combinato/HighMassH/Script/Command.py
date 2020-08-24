from Configuration import *
import os
#combineCards.py -S

#${flv}_${boost}_${proc}0_${rg}_${YEAR}=Datacard_M${MX}/${flv}CH__${boost}${proc}__${rg}__${cutname}__MEKDTAG/${FINALVAR}/datacard.txt"
workspace=os.getcwd()+'/workspace/'
os.system('mkdir -p '+workspace)

UseCardDirect=False

def CpCards(Year):
    Year=str(Year)
    cardpath=LoadCardPath()
    #path=cardpath[Year]
    if os.path.isdir(workspace+'/Datacards_'+Year):
        os.system('rm -rf '+workspace+'/'+Year+'/Datacards_'+Year)
    os.system('cp -r '+cardpath[Year]+' '+workspace+'/'+Year+'/Datacards_'+Year)

        
def CombineCardCommand(Year,MX,BoostList=['Boosted','Resolved'],FlvList=['mu','ele']):
    Year=str(Year)
    #config[Boosted][TOP][cuts/variable]
    config=LoadConfiguration()
    ##--MassPoint
    List_MX_GGF=GetGGFMXList(Year)
    List_MX_VBF=GetVBFMXList(Year)

    validMX=True

    if not MX in List_MX_GGF:
        print MX,'is not in GGF signal mass'
        validMX=False
    if not MX in List_MX_VBF:
        print MX,'is not in VBF signal mass'
        validMX=False
    #List_MX=list(set(List_MX_GGF+List_MX_VBF))
    if not validMX:
        exit()
        

    MX=str(MX)
    
    ##--Use card direct
    if UseCardDirect:
        cardpath=LoadCardPath()
        cardpath_this_yr=cardpath[Year]

    ARGUMENTS=[]
    
    #for bst in config:
    for bst in BoostList:
        for rg in config[bst]:
            cuts=config[bst][rg]['cuts']
            variable=config[bst][rg]['variable']

            for cut in cuts:
                #for MX in List_MX:
                doCombine=False

                ##--check lepton ch
                for flv in FlvList:
                    if not flv+'CH' in cut: doCombine=True 
                if not doCombine: continue


                cardpath='Datacards_'+Year+'/Datacard_M'+MX+'/'+cut+'/'+variable+'/datacard.txt'
                if UseCardDirect:
                    cardpath=cardpath_this_yr+'/Datacard_M'+MX+'/'+cut+'/'+variable+'/datacard.txt'
                myarg=cut+'_'+Year+"="+cardpath
                ARGUMENTS.append(myarg)

    ARGUMENT=" ".join(ARGUMENTS)
    workspace_year=workspace+'/'+Year
    os.system('mkdir -p '+workspace_year)
    suffix=''
    if len(BoostList)==1:
        suffix+='_'+BoostList[0]
    if len(FlvList)==1:
        suffix+='_'+FlvList[0]
    command='combineCards.py -S '+ARGUMENT+'> '+workspace_year+'/combined_card_'+MX+suffix+'.txt'
    
    maindir=os.getcwd()
    os.chdir(workspace_year)
    os.system(command)
    os.chdir(maindir)
    #os.system('echo '+command+'> '+workspace_year+'/CombineCard'+Year+'.sh')
    return command
    #print command


if __name__ == '__main__':
    Year=2016
    CpCards(Year)
    CombineCardCommand(Year,900,['Boosted'],['mu'])
