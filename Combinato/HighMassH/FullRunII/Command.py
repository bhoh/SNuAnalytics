from Configuration import *
import os
from copy import deepcopy
#combineCards.py -S
import sys
sys.path.insert(0, "python_tool")
from ExportShellCondorSetup import Export

#${flv}_${boost}_${proc}0_${rg}_${YEAR}=Datacard_M${MX}/${flv}CH__${boost}${proc}__${rg}__${cutname}__MEKDTAG/${FINALVAR}/datacard.txt"
#workspace=os.getcwd()+'/../workspace/'
#print "workspace=",workspace
#os.system('mkdir -p '+workspace)

workspace=os.getcwd()+'/workspace/'
print "workspace=",workspace
os.system('mkdir -p '+workspace)



def PrintCommand():
    print "---Command---"
    print 'PrintCommand()'
    print "CpCards(Year)"
    print "CombineCardYear(Year)"
    print "MakeWorkSpace(Year)"
    print "GetAsymptoticLimit(Year)"
PrintCommand()
def CpCards(Year):
    print "----CpCard",Year
    Year=str(Year)
    cardpath=LoadCardPath()
    #path=cardpath[Year]
    print "cp",cardpath
    if os.path.isdir(workspace+'/'+Year+'/Datacards_'+Year):
        print 'Clear',workspace+'/'+Year+'/Datacards_'+Year
        os.system('rm -rf '+workspace+'/'+Year+'/Datacards_'+Year)
    os.system('mkdir -p '+workspace+'/'+Year)
    command='cp -r '+cardpath[Year]+' '+workspace+'/'+Year+'/Datacards_'+Year
    print command
    #print command
    os.system(command)

    print "----[END]CpCard",Year
def CombineCardCommand(Year,MX,BoostList=['Boosted','Resolved'],FlvList=['mu','ele']):
    FullRunII=False ##combine all 3yrs
    Year=str(Year)
    if Year=='3yr': FullRunII=True
    
    #config[Boosted][TOP][cuts/variable]
    config=LoadConfiguration()
    Years=[]
    if not FullRunII:
        Years=[Year]
    else:
        Years=['2016','2017','2018']
    ##--MassPoint
    List_MX_GGF=GetGGFMXList(Years[0])
    List_MX_VBF=GetVBFMXList(Years[0])

    
    List_MX_common=list(set(List_MX_GGF).intersection(List_MX_VBF))
    for yr in Years:
        List_MX_common=list(set(List_MX_common).intersection(GetGGFMXList(yr)))
        List_MX_common=list(set(List_MX_common).intersection(GetVBFMXList(yr)))
        #List_MX_GGF+=GetGGFMXList(yr)
        #List_MX_VBF+=GetVBFMXList(yr)
    
    validMX=True

    if not MX in List_MX_common:
        print MX,'is not in signal mass'
        validMX=False
    #List_MX=list(set(List_MX_GGF+List_MX_VBF))
    if not validMX:
        return
        

    MX=str(MX)
    


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

                for yr in Years:
                    if FullRunII:
                        cardpath='../'+yr+'/Datacards_'+yr+'/Datacard_M'+MX+'/'+cut+'/'+variable+'/datacard.txt'
                    else:
                        cardpath='Datacards_'+yr+'/Datacard_M'+MX+'/'+cut+'/'+variable+'/datacard.txt'
                
                    myarg=cut+'_'+yr+"="+cardpath
                    ARGUMENTS.append(myarg)

    ARGUMENT=" ".join(ARGUMENTS)
    workspace_year=workspace+'/'+Year
    #combinedcards_year=workspace+'/'+Year+'/CombinedCards'
    os.system('mkdir -p '+workspace_year)

    suffix=''
    if len(BoostList)==1:
        suffix+='_'+BoostList[0]
    if len(FlvList)==1:
        suffix+='_'+FlvList[0]
    command='combineCards.py -S '+ARGUMENT+'> combined_card_'+MX+suffix+'.txt'
    
    maindir=os.getcwd()
    os.chdir(workspace_year)
    os.system(command)
    os.chdir(maindir)
    #os.system('echo '+command+'> '+workspace_year+'/CombineCard'+Year+'.sh')
    return command
    #print command




#if __name__ == '__main__':
def CombineCardYear(Year,doCopy=False):
    FullRunII=False ##combine all 3yrs
    Year=str(Year)
    if Year=='3yr': FullRunII=True
    Years=[]
    if not FullRunII:
        Years=[Year]
    else:
        Years=['2016','2017','2018']
    ##--MassPoint
    List_MX_GGF=GetGGFMXList(Years[0])
    List_MX_VBF=GetVBFMXList(Years[0])


    List_MX_common=list(set(List_MX_GGF).intersection(List_MX_VBF))
    for yr in Years:
        List_MX_common=list(set(List_MX_common).intersection(GetGGFMXList(yr)))
        List_MX_common=list(set(List_MX_common).intersection(GetVBFMXList(yr)))
        #List_MX_GGF+=GetGGFMXList(yr)

    #print 
    #Year=2016


    if doCopy:CpCards(Year)

    for MX in List_MX_common:
        print "Year=",Year,"MX=",MX
        CombineCardCommand(Year,MX,['Boosted','Resolved'],['mu','ele'])
        CombineCardCommand(Year,MX,['Boosted'],['mu','ele'])
        CombineCardCommand(Year,MX,['Resolved'],['mu','ele'])

def GetMakeWorkSpaceCommand(Year,MX,BoostList,FlvList):
    #print "<GetMakeWorkSpaceCommand>"
    workspace_year=workspace+'/'+Year
    #text2workspace.py $1 -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalar:XWW$2 -o M$2.root &> logs/make_workspace_M$2.log&
    #text2workspace.py $1 -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalar:XWW$2 -o M${2}_NoI.root --PO KillInterference &> logs/make_workspace_M${2}_NoI.log&

    command_list=[]

    MX=str(MX)
    #print MX,BoostList

    suffix=''
    if len(BoostList)==1:
        suffix+='_'+BoostList[0]
    if len(FlvList)==1:
        suffix+='_'+FlvList[0]

    if 'Boosted' in BoostList:
        if int(MX) < 200: 
            print "[!!!]MX below 200, and Boosted reion included, pass",MX
            return False
    workspace_year=workspace+'/'+Year
    workspace_files_path=workspace_year+'/WorkSpaceFiles'
    cardpath=workspace_year+'/combined_card_'+MX+suffix+'.txt'
    ##---workspace
    #os.chdir(combinedcards_year)
    os.system('mkdir -p '+workspace_files_path)

    command='text2workspace.py '+cardpath+' -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalar:XWW'+MX+' -o '+workspace_files_path+'/M'+MX+suffix+'.root'
    #print command
    #os.system(command)
    command_list.append(command)
    command='text2workspace.py '+cardpath+' -P HiggsAnalysis.CombinedLimit.HiggsCombinePhysicsModel.HighMassScalar.HighMassScalar:XWW'+MX+' -o '+workspace_files_path+'/M'+MX+suffix+'_NoI.root --PO KillInterference'
    #print command
    #os.system(command)
    command_list.append(command)
    
    return command_list

def MakeWorkSpace(Year):
    Year=str(Year)
    ncpu=1
    submit=True


    FullRunII=False ##combine all 3yrs
    Year=str(Year)
    if Year=='3yr': FullRunII=True

    Years=[]
    if not FullRunII:
        Years=[Year]
    else:
        Years=['2016','2017','2018']
    ##--MassPoint
    List_MX_GGF=GetGGFMXList(Years[0])
    List_MX_VBF=GetVBFMXList(Years[0])


    List_MX_common=list(set(List_MX_GGF).intersection(List_MX_VBF))
    for yr in Years:
        List_MX_common=list(set(List_MX_common).intersection(GetGGFMXList(yr)))
        List_MX_common=list(set(List_MX_common).intersection(GetVBFMXList(yr)))
        #List_MX_GGF+=GetGGFMXList(yr)                                                                                                                                                                      
        #List_MX_VBF+=GetVBFMXList(yr)                                                                                                                                                                      


    ##---combine all channels---##
    for MX in List_MX_common:
        #MX=str(MX)
        #print "Year=",Year,"MX=",MX
        jobname='workspace__ALLchannel__combine__'+str(MX)+"__"+Year
        WORKDIR='WORKDIR__MakeWorSpace/'+jobname
        commands=GetMakeWorkSpaceCommand(Year,MX,['Boosted','Resolved'],['mu','ele'])
        if not commands:continue
        commands.insert(0, 'cd '+os.getcwd())
        command='&&'.join(commands)
        Export(WORKDIR,command,jobname,submit,ncpu)

    ##---only Boosted
    for MX in List_MX_common:

        jobname='workspace__Boosted__combine__'+str(MX)+'__'+Year
        WORKDIR='WORKDIR__MakeWorSpace/'+jobname
        commands=GetMakeWorkSpaceCommand(Year,MX,['Boosted'],['mu','ele'])
        if not commands:continue
        command='&&'.join(commands)
        Export(WORKDIR,command,jobname,submit,ncpu)        

    ##---only Resolved
    for MX in List_MX_common:

        jobname='workspace__Resolved__combine__'+str(MX)+'__'+Year
        WORKDIR='WORKDIR__MakeWorSpace/'+jobname
        commands=GetMakeWorkSpaceCommand(Year,MX,['Resolved'],['mu','ele'])
        if not commands:continue
        command='&&'.join(commands)
        Export(WORKDIR,command,jobname,submit,ncpu)


def GetAsymptoticLimitCommand(Year,MX,BoostList,FlvList,fvbf,interference):
    #fvbf= floating,vbfonly,ggfonly,0.5
    print '<GetAsymptoticLimitCommand>'
    MX=str(MX)
    suffix=''
    if len(BoostList)==1:
        suffix+='_'+BoostList[0]
    if len(FlvList)==1:
        suffix+='_'+FlvList[0]

    if 'Boosted' in BoostList:
        if int(MX) < 200:
            print "[!!!]MX below 200, and Boosted reion included, pass",MX
            return False

    workspace_year=workspace+'/'+Year
    workspace_files_path=workspace_year+'/WorkSpaceFiles/'

    #maindir=os.getcwd()
    #os.chdir(workspace_year)
    workspacefile=workspace_files_path+'/M'+MX+suffix+'.root'
    if not interference:
        workspacefile=workspace_files_path+'/M'+MX+suffix+'_NoI.root'
    if fvbf=='floating': 
        command='combine -M AsymptoticLimits -d '+workspacefile+' --trackParameters fvbf -t -1 -m '+str(MX)+' -s 5'
    if fvbf=='vbfonly': 
        command='combine -M AsymptoticLimits -d '+workspacefile+' --setParameters fvbf=1 --freezeParameters fvbf -t -1 -m '+str(MX)+' -s 6'
    if fvbf=='ggfonly': 
        command='combine -M AsymptoticLimits -d '+workspacefile+' --setParameters fvbf=0 --freezeParameters fvbf  -t -1 -m '+str(MX)+' -s 5'
    if fvbf=='0.5': 
        command='combine -M AsymptoticLimits -d '+workspacefile+' --setParameters fvbf=0.5 --freezeParameters fvbf  -t -1 -m '+str(MX)+' -s 5'
    return command

    #os.chdir(maindir)
def GetAsymptoticLimit(Year):
    '''
    combine -M AsymptoticLimits -d $workspacefile ${option} --trackParameters fvbf -t -1 -m ${MX} -s 5 &> Limits/AsymptoticLimits_$workspacefile.txt&
    combine -M AsymptoticLimits -d $workspacefile ${option} --setParameters fvbf=0 --freezeParameters fvbf -t -1 -m ${MX} -s 6 &> Limits/AsymptoticLimits_${workspacefile}_GGFOnly.txt&
    combine -M AsymptoticLimits -d $workspacefile ${option} --setParameters fvbf=1 --freezeParameters fvbf -t -1 -m ${MX} -s 7 &> Limits/AsymptoticLimits_${workspacefile}_VBFOnly.txt&
    combine -M AsymptoticLimits -d $workspacefile ${option} --setParameters fvbf=0.5 --freezeParameters fvbf -t -1 -m ${MX} -s 8 &> Limits/AsymptoticLimits_${workspacefile}_fvbf0p5.txt&

    '''
    Year=str(Year)
    ncpu=1
    submit=True
    FullRunII=False ##combine all 3yrs

    Year=str(Year)
    if Year=='3yr': FullRunII=True

    Years=[]
    if not FullRunII:
        Years=[Year]
    else:
        Years=['2016','2017','2018']
    ##--MassPoint
    List_MX_GGF=GetGGFMXList(Years[0])
    List_MX_VBF=GetVBFMXList(Years[0])


    List_MX_common=list(set(List_MX_GGF).intersection(List_MX_VBF))
    for yr in Years:
        List_MX_common=list(set(List_MX_common).intersection(GetGGFMXList(yr)))
        List_MX_common=list(set(List_MX_common).intersection(GetVBFMXList(yr)))


    fvbf_list=['floating','vbfonly','ggfonly','0.5']
    interference_list=[True,False]
    ##---combine all channels---##
    for MX in List_MX_common:

        #MX=str(MX)
        #print "Year=",Year,"MX=",MX
        #GetAsymptoticLimitCommand
        #GetAsymptoticLimitCommand(Year,MX,BoostList,FlvList,fvbf='floating')
        for fvbf in fvbf_list:
            for interference in interference_list:
                commands=[]
                jobname='AsymptoticLimit__'+fvbf+'__ALLchannel__combine__'+str(MX)+"__"+Year
                if not interference: jobname='AsymptoticLimit__'+fvbf+'__ALLchannel__combine__'+str(MX)+"_NoI__"+Year
                WORKDIR='WORKDIR__AsymptoticLimit__'+fvbf+'/'+jobname
                _command=GetAsymptoticLimitCommand(Year,MX,['Boosted','Resolved'],['mu','ele'],fvbf,interference)
                if not _command:continue
                #commands.append('cd '+os.getcwd())
                commands.append('cd '+os.getcwd()+'/'+WORKDIR) ##@jobsubmission dir
                commands.append(_command)
                command='&&'.join(commands)
                print command
                Export(WORKDIR,command,jobname,submit,ncpu)

    ##---only Boosted
    for MX in List_MX_common:

        for fvbf in fvbf_list:
            for interference in interference_list:
                commands=[]
                jobname='AsymptoticLimit__'+fvbf+'__Boosted__combine__'+str(MX)+"__"+Year
                if not interference: jobname='AsymptoticLimit__'+fvbf+'__Boosted__combine__'+str(MX)+"_NoI__"+Year
                WORKDIR='WORKDIR__AsymptoticLimit__'+fvbf+'/'+jobname
                _command=GetAsymptoticLimitCommand(Year,MX,['Boosted'],['mu','ele'],fvbf,interference)
                if not _command:continue
                commands.append('cd '+os.getcwd()+'/'+WORKDIR) ##@jobsubmission dir
                commands.append(_command)
                command='&&'.join(commands)
                print command
                Export(WORKDIR,command,jobname,submit,ncpu)



    ##---only Resolved
    for MX in List_MX_common:

        for fvbf in fvbf_list:
            for interference in interference_list:
                commands=[]
                jobname='AsymptoticLimit__'+fvbf+'__Resolved__combine__'+str(MX)+"__"+Year
                if not interference: jobname='AsymptoticLimit__'+fvbf+'__Resolved__combine__'+str(MX)+"_NoI__"+Year
                WORKDIR='WORKDIR__AsymptoticLimit__'+fvbf+'/'+jobname
                _command=GetAsymptoticLimitCommand(Year,MX,['Resolved'],['mu','ele'],fvbf,interference)
                if not _command:continue
                commands.append('cd '+os.getcwd()+'/'+WORKDIR) ##@jobsubmission dir
                commands.append(_command)
                command='&&'.join(commands)
                print command
                Export(WORKDIR,command,jobname,submit,ncpu)



    
if __name__ == '__main__':


    ##1)combine Card
    #CpCards(2016)
    #CombineCardYear(2016)
    #MakeWorkSpace(2016)
    print "from Command import *"
