import ROOT
#GetListOfBranches ()
#nosys/nanoLatino_ZZZ__part2.root
#sys/nanoLatino_ZZZ__part2.root

def CheckAlreadyHadd(dir1,dir2,filename):

    AlreadyHadd=False
    
    #commonName='nanoLatino_ZZZ__part2.root'
    commonName=filename
    
    #f1="nosys/"+commonName
    #f2="sys/"+commonName

    f1=dir1+"/"+commonName
    f2=dir2+"/"+commonName
    
    tf1=ROOT.TFile.Open(f1,'READ')
    tf2=ROOT.TFile.Open(f2,'READ')
    
    ttree1=tf1.Get("Events")
    ttree2=tf2.Get("Events")
    
    brlist1=ttree1.GetListOfBranches ()
    brlist2=ttree2.GetListOfBranches ()
    
    for br1 in brlist1:
        #print br1.GetName()
        name1=br1.GetName()
        for br2 in brlist2:
            name2=br2.GetName()
            if name1==name2:##if they have the common name
                if not name1.startswith('n'):  ##length values is in common, if it is not a length value but common
                    AlreadyHadd=True
                    tf1.Close()
                    tf2.Close()
                    return AlreadyHadd
                
                    
    tf1.Close()
    tf2.Close()
    return AlreadyHadd



if __name__ == '__main__':
    
    #dir1="nosys"
    dir1="sys"
    dir2="sys"
    filename="nanoLatino_ZZZ__part2.root"
    AlreadyHadd=CheckAlreadyHadd(dir1,dir2,filename)
    print "AlreadyHadd=",AlreadyHadd
