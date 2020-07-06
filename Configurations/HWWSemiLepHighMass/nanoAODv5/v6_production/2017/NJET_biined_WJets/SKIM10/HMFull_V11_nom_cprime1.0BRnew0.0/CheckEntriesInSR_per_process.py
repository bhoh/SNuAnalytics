import ROOT
import sys
sys.path.insert(0, "kfactor")
from NormToPowheg import *
from kfactor import *
import argparse
import glob
import os

parser = argparse.ArgumentParser()
parser.add_argument("-c", dest='cutname')
#parser.add_argument("-f", dest='histofile')
parser.add_argument("-p", dest='processname')
parser.add_argument("-d", dest='directorypath')
parser.add_argument("-v", dest='variablename')
parser.add_argument("-n", dest='nevent')
#parser.add_argument("-s", dest='samples')
args=parser.parse_args()

cutname=args.cutname
processname=args.processname
directorypath=args.directorypath ## dir path where histofiles
variable=args.variablename
nevent=args.nevent ##nentries threshold
#samples=args.samples
#samplelist=samples.split(',')





#sys.path.insert(0, "MassPoints")
#from List_MX import *
#from List_MX_VBF import *

#'ggHWWlnuqq_M'+str(MX)+'_S'
#'vbfHWWlnuqq_M'+str(MX)+'_S'
#samplelist=[]
#for MX in List_MX:
#    samplelist.append('ggHWWlnuqq_M'+str(MX)+'_B')
#    #histo_ggHWWlnuqq_M115_S

#ggHWWlnuqq_M150_B

print "--check files of ",processname,'--'
histofiles=glob.glob(directorypath+'/plot*'+processname+'.*root')
print histofiles

print "---haddfiles---"
workdir=directorypath+'/hadddir_'+processname
os.system('mkdir -p '+workdir)
haddfile=workdir+'/hadd_'+processname+'.root'
hadd='hadd -f '+haddfile+' '+" ".join(histofiles)
print hadd
os.system(hadd)

#for histofile in histofiles:
myfile=ROOT.TFile.Open(haddfile)
print cutname+'/'+variable
#selected=[]

path=cutname+'/'+variable+'/histo_'+processname
htemp=myfile.Get(path)
N=htemp.GetEntries()
integral=htemp.Integral()
if N > int(nevent):
#if True:
    MX=-1
    #normfactor=0
    if 'ggHWWlnuqq_M' in processname:
        MX=processname.replace('ggHWWlnuqq_M','').replace('_B','')
        #normfactor=float(NormToPowheg['ggHWWlnuqq_M'+MX])/float(kfactor['ggHWWlnuqq_M'+MX])
    elif 'vbfHWWlnuqq_M' in processname:
        MX=processname.replace('vbfHWWlnuqq_M','').replace('_B','')
        #normfactor=float(NormToPowheg['vbfHWWlnuqq_M'+MX])/float(kfactor['vbfHWWlnuqq_M'+MX])
    print MX,'Entries=',N,'integral',integral
    f=open(workdir+'/info.txt','w')
    f.write(str(MX)+' Entries='+str(N)+' integral='+str(integral)+'\n')
    f.close()
myfile.Close()


'''

myfile=ROOT.TFile.Open(histofile)

print cutname+'/'+variable

selected=[]

for s in samplelist:
path=cutname+'/'+variable+'/histo_'+s
#print path
htemp=myfile.Get(cutname+'/'+variable+'/histo_'+s)
N=htemp.GetEntries()
integral=htemp.Integral()
    if N > int(nevent):
#print s,N
MX=s.replace('ggHWWlnuqq_M','').replace('_B','')
normfactor=float(NormToPowheg['ggHWWlnuqq_M'+MX])/float(kfactor['ggHWWlnuqq_M'+MX])
print s.replace('ggHWWlnuqq_M','').replace('_B',''),'Entries=',N,'integral=',integral,'normfactor=',normfactor
selected.append(s)
myfile.Close()

for s in selected:
print s
'''
