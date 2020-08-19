import datetime
begin_time = datetime.datetime.now()
import sys
import os
sys.path.insert(0, "MassPoints")
from List_MX import *
from List_MX_VBF import *


import sys
sys.path.insert(1, os.getcwd()+"/../")
sys.path.insert(2, os.getcwd())
from WPandCut2016 import *
#List_MX_common=list(set(List_MX).intersection(List_MX_VBF))
#BKG=[ 'DY', 'top']+Wjets+MultiV+H125+qqWWqq+ggWW

#LIST_MX=[115,120,125,126,130,135,140,145,150,155,160,165,170,175,180,200,210,230,250,270,300,350,400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000,5000,]


from samples_2016_dummy import *
samples=sorted(samples)

SAMPLELIST=sorted(samples)

for s in SAMPLELIST:
   if '_SI' in s:
      SAMPLELIST.append(s.replace('_SI','_SBI'))



#for MX in List_MX_VBF:
#   SIG.append('vbfHWWlnuqq_M'+str(MX)+'_SBI')
#   SIG.append('vbfHWWlnuqq_M'+str(MX)+'_S')
#for MX in List_MX:
#   SIG.append('ggHWWlnuqq_M'+str(MX)+'_SBI')
#   SIG.append('ggHWWlnuqq_M'+str(MX)+'_S')



from array import array
import ROOT
ROOT.gROOT.SetBatch(True)
import sys
sys.path.insert(0, "python_tool/latino/")
import math


import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-f", dest='histofile')


args=parser.parse_args()


histofile=args.histofile
import os
print "histofile.split('/')=",histofile.split('/')
histodir="/".join(histofile.split('/')[:-1])
print "histodir=",histodir
histofilename=histofile.split('/')[-1]
backupdir=histodir+'/backup_rootFile'
backupfile=backupdir+'/'+histofilename
os.system('mkdir -p '+backupdir)

if not os.path.isfile(backupfile):
   os.system('cp '+histofile+' '+backupfile)
else:
   print "backup is already there"
   os.system('cp '+backupfile+' '+histofile)
dict_htemp={}
f=ROOT.TFile.Open(histofile,'UPDATE')


print "---nominal---"
#ntotal=len(BKG+SIG)
ntotal=len(SAMPLELIST)
idx=0
#for proc in BKG+SIG:
for proc in SAMPLELIST:
   idx+=1
   print idx,'/',ntotal,proc
   histopath='histo_'+proc
   #print histopath
   #keylist=ROOT.gDirectory.GetListOfKeys()
   cutlist=f.GetListOfKeys()
   #keylist=ROOT.gDirectory.GetList()
   
   for cut in cutlist:
      cutname=cut.GetName()
      #print "key=",key
      #print 'dirname=',dirname
      f.cd(cutname)
      variablelist=ROOT.gDirectory.GetListOfKeys()
      for variable in variablelist:
         variablename=variable.GetName()
         #print variablename
         f.cd(cutname+'/'+variablename)
         shapelist=ROOT.gDirectory.GetListOfKeys()
         #for shape in shapelist:
            #shapepath=cutname+'/'+variablename+'/'+shape
         #print 'shapelist'
         #print shapelist
         if histopath in shapelist: ##if nominal shape
            #print "find histopath ",histopath
            fullpath=cutname+'/'+variablename+'/'+histopath
            #print fullpath
            thish=f.Get(fullpath)
            #try:
            norm=thish.Integral()
            #print norm
            entries=thish.GetEntries()
            if norm ==0 and entries>0:
               print histopath,'zero norm, but has entries '
               print fullpath
               hnew=thish.Clone()
               Nbins= thish.GetNbinsX()
               for ibin in range(0,Nbins+1):
                  #y=thish.GetBinContent(ibin)
                  #yerr=thish.GetBinError(ibin)
                  #if y <=0:
                  hnew.SetBinContent(ibin,0.0)
                     
                  ##end of ibin
               hnew.SetEntries(0)
               ROOT.gDirectory.WriteObject(hnew,histopath)
            if norm < 0 and entries > 0:
               print histopath,'negative norm, but has entries '
               print fullpath
               hnew=thish.Clone()
               Nbins= thish.GetNbinsX()
               for ibin in range(0,Nbins+1):
                  y=thish.GetBinContent(ibin)
                  yerr=thish.GetBinError(ibin)
                  if y <0:
                     hnew.SetBinContent(ibin,0.0)
                     
                  ##end of ibin
               
               ROOT.gDirectory.WriteObject(hnew,histopath)
         for shape in shapelist: ##to find nuisance shape 
            shapename=shape.GetName() ## histo_Wjets01_fatsys_up e.g.
            #print shapename,"shapename"
            fullpath=cutname+'/'+variablename+'/'+shapename
            if histopath+'_' in shapename and histopath!=shapename: ##nuisance shape
               #fullpath=cutname+'/'+variablename+'/'+histopath
               #print fullpath
               thish=f.Get(fullpath)
               norm=thish.Integral()
               #print norm
               entries=thish.GetEntries()
               #if norm ==0 and entries>0:
               ##   print fullpath,'has entry but norm'
               #   hnew=thish.Clone()
               #   for ibin in range(0,Nbins+1):
               #      hnew.SetBinContent(ibin,0.0)
               #   hnew.SetEntries(0)
               #   ROOT.gDirectory.WriteObject(hnew,shapename)
               if norm <= 0 :##--take nominal
                  print fullpath,"has negative norm, sync to norminal shape"
                  normshapepath=cutname+'/'+variablename+'/'+histopath
                  print 'normshapepath=',normshapepath
                  nomshape=f.Get(normshapepath)
                  hnew=nomshape.Clone()
                  hnew.Scale(nomshape.Integral()/100000)
                  hnew.SetName(shapename)
                  hnew.SetTitle(shapename)
                  ROOT.gDirectory.WriteObject(hnew,shapename)
                  


   #except:
      #continue
'''
print "-nuisance shape-"
for shape in ROOT.gDirectory.GetListOfKeys():
   for proc in BKG+SIG:
      shapepath=shape.GetName()
      #print "shapepath=",shapepath
      #print "shape=",shape
      if proc in shapepath and shapepath!="histo_"+proc: ## systematic shape
         print shapepath
         thish = f.Get(shapepath)
         dict_htemp[shapepath]=thish.Clone()
         norm=thish.Integral()
         #Nbins= thish.GetNbinsX()
         #for ibin in range(0,Nbins+1):
         #   y=thish.GetBinContent(ibin)
         #   yerr=thish.GetBinError(ibin)
         #   if y <0:
         #      dict_htemp[shapepath].SetBinContent(ibin,0)
         #      ##end of ibin
         if norm <= 0:
            normshapepath=shapepath.split(proc)[0]+proc
            nomshape=f.Get(normshapepath)
            dict_htemp[shapepath]=nomshape.Clone()

            dict_htemp[shapepath].Scale(nomshape.Integral()/100000)
            dict_htemp[shapepath].SetName(shapepath)
            dict_htemp[shapepath].SetTitle(shapepath)
         ROOT.gDirectory.WriteObject(dict_htemp[shapepath],shapepath)
'''

      
#ROOT.gDirectory.WriteObject(,'')
f.Close()
print(datetime.datetime.now() - begin_time)
