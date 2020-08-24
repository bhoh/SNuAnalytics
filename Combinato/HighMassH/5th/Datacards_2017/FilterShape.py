import datetime
begin_time = datetime.datetime.now()



BKG=[ 'DY', 'MultiV', 'top', 'Wjets','QCD_EM','QCD_MU','QCD_bcToE','qqWWqq','ggWW']

LIST_MX=[115,120,125,126,130,135,140,145,150,155,160,165,170,175,180,200,210,230,250,270,300,350,400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000,5000,]
SIG=[]


for MX in LIST_MX:

   SIG.append('vbfHWWlnuqq_M'+str(MX)+'_SBI')
   SIG.append('vbfHWWlnuqq_M'+str(MX)+'_S')
   SIG.append('ggHWWlnuqq_M'+str(MX)+'_SBI')
   SIG.append('ggHWWlnuqq_M'+str(MX)+'_S')



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
os.system('cp '+histofile+' '+histofile+'_backup')
dict_htemp={}
f=ROOT.TFile.Open(histofile,'UPDATE')
listfile=histofile.replace('.root','_list.txt')
fnew=open(listfile,'w')
print "---nominal---"
for proc in BKG+SIG:
   histopath='histo_'+proc
   #print histopath
   if histopath in ROOT.gDirectory.GetListOfKeys():
      thish=f.Get(histopath)
   #try:
      norm=thish.Integral()
      if norm <=0.:
         print histopath,'has negative'
         fnew.write(histopath+'\n')
         hnew=thish.Clone()
         Nbins= thish.GetNbinsX()
         for ibin in range(0,Nbins+1):
            y=thish.GetBinContent(ibin)
            yerr=thish.GetBinError(ibin)
            if y <=0:
               hnew.SetBinContent(ibin,0.0001)
               
            ##end of ibin
         ROOT.gDirectory.WriteObject(hnew,histopath)
         
   #except:
      #continue
print "-nuisance shape-"
for shape in ROOT.gDirectory.GetListOfKeys():
   for proc in BKG+SIG:
      shapepath=shape.GetName()
      if proc+'_' in shapepath and shapepath!="histo_"+proc:
         if 'qqWWqq' in proc : print shapepath
         #print shapepath
         fnew.write(histopath+'\n')
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
         if norm <= 0.:
            normshapepath=shapepath.split(proc)[0]+proc
            nomshape=f.Get(normshapepath)
            dict_htemp[shapepath]=nomshape.Clone()

            dict_htemp[shapepath].Scale(nomshape.Integral()/100000)
            dict_htemp[shapepath].SetName(shapepath)
            dict_htemp[shapepath].SetTitle(shapepath)
         ROOT.gDirectory.WriteObject(dict_htemp[shapepath],shapepath)


      
#ROOT.gDirectory.WriteObject(,'')
f.Close()
fnew.close()
print(datetime.datetime.now() - begin_time)
