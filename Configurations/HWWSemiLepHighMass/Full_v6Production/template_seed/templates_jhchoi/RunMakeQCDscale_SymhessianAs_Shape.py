submit=True
resub=False

import os
import sys
#if sys.args[1]:
if sys.argv[1]=="resub":
    print "[resub]"
    resub=True
elif sys.argv[1]=="sub":
    print "[submit]"
    submit=True
elif sys.argv[1]=='dry':
    print "[dryrun]"
    submit=False
else:
    exit()



import glob
print "[Turn off flags]"
os.system('python TurnOffCombinedSamples.py WPandCut2016.py CombineMultiV')
os.system('python TurnOffCombinedSamples.py WPandCut2016.py CombineH125')
os.system('python TurnOffCombinedSamples.py WPandCut2016.py CombineWjets')
os.system('python TurnOffCombinedSamples.py WPandCut2016.py Combine_ggWW')
os.system('python TurnOffCombinedSamples.py WPandCut2016.py Combine_qqWWqq')
os.system('python TurnOffCombinedSamples.py WPandCut2016.py CombineSBI')

print "[done]"


##---Module For batchjob
sys.path.insert(0, "python_tool/")
from ExportShellCondorSetup import Export 
#def Export(WORKDIR,command,jobname,submit,ncpu):

##--Predefined functions--##

def SubmitMakeEnvelopShape(nuisance,s,bst,reg):
    configuration='configuration_'+bst+'_'+reg+'.py'
    #nuisance='QCDscaleAccept'
    filelist=glob.glob('rootFile*_*'+bst+'*_*'+reg+'*/*'+s+'.*root')
    command='cd '+os.getcwd()+'&&'
    for f in filelist:
        command+='python MakeEnvelopShape.py -c '+configuration+' -n '+nuisance+' -s '+s+' -f '+f+'&&'
    command+="echo '--'"
    print command
    
    WORKDIR="WORKDIR__"+nuisance+'/'+bst+'_'+reg+'/'+s
    jobname=nuisance+'/'+bst+'_'+reg+'/'+s
    
    ncpu=1
    Export(WORKDIR,command,jobname,submit,ncpu)

def SubmitMakeSymhessianAsShape(nuisance,s,bst,reg):
    configuration='configuration_'+bst+'_'+reg+'.py'
    #nuisance='QCDscaleAccept'
    filelist=glob.glob('rootFile*_*'+bst+'*_*'+reg+'*/*_'+s+'.*root')
    command='cd '+os.getcwd()+';'
    for f in filelist:
        command+='python MakeSymhessianAsShape.py -c '+configuration+' -n '+nuisance+' -s '+s+' -f '+f+';'
    print command
    
    WORKDIR="WORKDIR__"+nuisance+'/'+bst+'_'+reg+'/'+s
    jobname=nuisance+'/'+bst+'_'+reg+'/'+s
    
    ncpu=1
    Export(WORKDIR,command,jobname,submit,ncpu)
    


CONFIG_LIST=[]
BST_LIST=['Boosted','Resolved']
REGION_LIST=['TOP','SB','SR']

#python python_tool/ExportShellCondorSetup.py -c "$command" -d "Run_mkDatacards/Resolved_M${MX}_${flv}_${rg}/" -n "Run_mkDatacards_M${MX}_${flv}_${rg}_Resolved" -s

def getjid(jidpath):
    if not os.path.isfile(jidpath):##if no jidpath
        return False
    f=open(jidpath,'r')
    #1 job(s) submitted to cluster 5834730
    print jidpath
    line=f.readlines()[1]
    print line
    jid=line.split('to cluster')[-1].replace(' ','').replace('.','').replace('\n','')
    jid=int(jid)
    f.close()
    return jid

def isTerminated(jid,logpath):
    if not os.path.isfile(logpath):##if no logpath
        return False
    f=open(logpath,'r')
    lines=f.readlines()
    isEnded=False
    for line in lines:
        if 'terminated' in line and str(jid) in line:isEnded=True
    f.close()

    return isEnded


def Submit():
    ##Read QCDscale/nuisance_QCDscale.py
    handle=open('QCDscale/nuisance_QCDscale.py','r')
    exec(handle)
    handle.close()
    for n in nMember_sample:
        for s in nMember_sample[n]:
            ##s='top'
            for bst in BST_LIST:
                for reg in REGION_LIST:

                    nuisance='QCDscaleAccept'
                    SubmitMakeEnvelopShape(nuisance,s,bst,reg)
    handle=open('PDF/nuisance_pdf.py','r')
    exec(handle)
    handle.close()
    for n in nMember_sample:
        for s in nMember_sample[n]:
        ##s='top'
            for bst in BST_LIST:
                for reg in REGION_LIST:
                    
                    
                    nuisance='pdfAccept'
                    SubmitMakeSymhessianAsShape(nuisance,s,bst,reg)
def Resub():
    shlist=[]
    nuisancelist=['QCDscaleAccept','pdfAccept']
    for nuisance in nuisancelist:
    #nuisance='QCDscaleAccept'

        shlist+=glob.glob('WORKDIR__'+nuisance+'/*/*/run.sh')
    
    ntotal=len(shlist)
    nresub=0
    for sh in shlist:
        jobname=sh.split('.sh')[-2]
        donename=jobname+'.done'
        if os.path.isfile(donename):continue ##success
        jidname=jobname+'.jid'
        jid=getjid(jidname)
        logname=jobname+'.log'
        if not isTerminated(jid,logname):continue ## still running

        jdsname=jobname+'.jds'
        command='condor_submit '+jdsname+' &> '+jidname
        print command
        os.system(command)
        nresub+=1
    print "[ResubJobs]",nresub,'/',ntotal
    #nuisance='pdfAccept'
    
if __name__ == '__main__':
    
    if resub:
        Resub()
        
    else:
        Submit()
