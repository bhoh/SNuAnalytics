#plot.py
#cuts_Boosted.py
import os
import sys
#ListProc=['GGF','VBF']
ListRegion=['TOP','SB','SR']
ListFlavor=['ele','mu','muele']
boosted=sys.argv[1]

print "[SpanPlotCut]",boosted

def ReplaceStringInFile(path,_from,_to):
    f=open(path,'r')
    fnew=open(path+'new','w')
    
    lines=f.readlines()
    
    for line in lines:
        if _from in line:
            line=line.replace(_from,_to)
        fnew.write(line)
    f.close()
    fnew.close()
    os.system('mv '+path+'new '+path)
    #os.system('rm '+path+'new')




#for proc in ListProc:
#for rg in ListRegion:
#    os.system('cp configuration_'+boosted+'.py '+'configuration_'+boosted+'_'+rg+'.py')
#    
#    for flv in ListFlavor:
#        os.system('cp cuts_'+boosted+'.py '+'cuts_'+boosted+'_'+rg+'_'+flv+'.py')
#    path='configuration_'+boosted+'_'+rg+'.py'
#    #ReplaceStringInFile(path,'__THIS_PROC__',proc)
#    ReplaceStringInFile(path,'__THIS_REGION__',rg)
