import os
def ApplyYearTag(path,Year):
    path_new=path+'_new'
    ftemplate=open(path,'r')
    fnew=open(path_new,'w')
    lines=ftemplate.readlines()
    for line in lines:
        line=line.replace('WPandCut2016','WPandCut'+Year)
        line=line.replace('samples_2016','samples_'+Year)
        line=line.replace('WPandCut2017','WPandCut'+Year)
        line=line.replace('samples_2017','samples_'+Year)
        line=line.replace('WPandCut2018','WPandCut'+Year)
        line=line.replace('samples_2018','samples_'+Year)
        fnew.write(line)
    os.system('mv '+path_new+' '+path)
    ftemplate.close()
    fnew.close()

def ChangeString(path,_from,_to):
    path_new=path+'_new'
    ftemplate=open(path,'r')
    fnew=open(path_new,'w')
    lines=ftemplate.readlines()
    for line in lines:
        line=line.replace(_from,_to)
        fnew.write(line)
    os.system('mv '+path_new+' '+path)
    ftemplate.close()
    fnew.close()
