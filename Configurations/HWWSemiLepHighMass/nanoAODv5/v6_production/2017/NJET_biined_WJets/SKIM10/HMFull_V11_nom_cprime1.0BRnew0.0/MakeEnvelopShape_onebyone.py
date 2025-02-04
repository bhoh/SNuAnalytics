import datetime
begin_time = datetime.datetime.now()

##---
class dummy():##dummy
   def __init__(self):
       self.variablesFile=''
       self.cutsFile=''
       self.nuisancesFile=''
       self.samplesFile=''
opt=dummy()
##---



from array import array
import ROOT
ROOT.gROOT.SetBatch(True)
import os
import sys
sys.path.insert(0, "python_tool/latino/")
sys.path.insert(0, os.getcwd())
import math
from HistoParser import HistoParser
'''
def MakeEnvelopShape(conf,histofile,nuisacneName):
   #conf='configuration_Boosted.py'
   #histofile='plots_2017_Boosted_SKIM10_HMVar10_Full_ALL_vbfHWWlnuqq_M1000_test.root'
   #nuisacneName='QCDscale'
   ##--declare--##
   variables={}
   cuts={}
   samples={}
   nuisances={}
   ##---Read configuration---##
   handle=open(conf,'r')
   exec(handle)
   handle.close()
   ##--Read SamplesFile--##
   handle=open(samplesFile,'r')
   exec(handle)
   handle.close()
   ##--Read variablesFile--##
   handle=open(variablesFile,'r')
   exec(handle)
   handle.close()
   ##--Read cutsFile--##
   handle=open(cutsFile,'r')
   exec(handle)
   handle.close()
   ##--Read NuisancesFile--##
   handle=open(nuisancesFile,'r')
   exec(handle)
   handle.close()
   ##---END--##
   #print nuisances['QCDscale']
   histofile=outputDir+'/'+histofile
   #nuisances['QCDscale']['samples']['vbfHWWlnuqq_M1000']
   for samplename in nuisances[nuisacneName]['samples']:
      print "--",samplename,"--"
      MakeEnvelopShape_a_sample(samplename,nuisacneName,cuts,variables,histofile,nuisances)
'''
def MakeEnvelopShape_a_sample(samplename,nuisacneName,cuts,variables,histofile,nuisances):
   print "[MakeEnvelopShape_a_sample]"
   print "samplename",samplename
   print "nuisacneName",nuisacneName
   print "len(cuts)",len(cuts)
   print "len(variables)",len(variables)
   print "histofile",histofile
   print "len(nuisances)",len(nuisances)
   this_dict={#QCDscale
      samplename:{
         'cuts':sorted(cuts),
         'variables':sorted(variables),
         'FileName':histofile,
         'samples':[samplename+'_'+nuisacneName+'V'+str(i)+'Var' for i in range(0,len(nuisances[nuisacneName]['samples'][samplename]))]
      },
   }
   histoana=HistoParser(this_dict)
   histoana.MakeEnvelopShape("histo_"+samplename+'_'+nuisacneName)
   
   f=ROOT.TFile.Open(histofile,'UPDATE')
   for cut in sorted(cuts):
      for var in sorted(variables):

         f.cd(cut+'/'+var)
         print "Store Shape on",cut+'/'+var+"/histo_"+samplename+'_'+nuisacneName+'Up'
         ROOT.gDirectory.WriteObject(histoana.mydict[samplename]['histo'][cut][var]['envelopUp'],"histo_"+samplename+'_'+nuisacneName+'Up')
         print "Store Shape on",cut+'/'+var+"/histo_"+samplename+'_'+nuisacneName+'Down'
         ROOT.gDirectory.WriteObject(histoana.mydict[samplename]['histo'][cut][var]['envelopDown'],"histo_"+samplename+'_'+nuisacneName+'Down')
         
   f.Close()
   #c.SaveAs("test.pdf")



if __name__ == '__main__':
   import optparse
   usage = 'usage: %prog [options]'
   parser = optparse.OptionParser(usage)
   parser.add_option("-c","--conf",   dest="conf", help="configuration file's name")
   parser.add_option("-f","--histofile",   dest="histofile", help="histofile's name")
   parser.add_option("-n","--nuisacneName",   dest="nuisacneName", help="nuisacneName, for example QCDscale")
   
   (options, args) = parser.parse_args()
   
   #conf='configuration_Boosted.py'
   #histofile='rootFile_2017_Boosted_SKIM10_HMVar10_Full/hadd.root'
   #histofile='hadd.root'
   #nuisacneName='QCDscale'
   conf=options.conf
   histofile=options.histofile
   nuisacneName=options.nuisacneName
   ##--declare--##
   variables={}
   cuts={}
   samples={}
   nuisances={}
   ##---Read configuration---##
   print '---Read configuration---',conf
   handle=open(conf,'r')
   exec(handle)
   handle.close()

   opt.samplesFile=samplesFile
   opt.variablesFile=variablesFile
   opt.cutsFile=cutsFile
   opt.nuisancesFile=nuisancesFile


   ##--Read SamplesFile--##
   print '--Read SamplesFile--',samplesFile
   handle=open(samplesFile,'r')
   exec(handle)
   handle.close()
   ##--Read variablesFile--##
   print '--Read variablesFile--',variablesFile
   handle=open(variablesFile,'r')
   exec(handle)
   handle.close()
   ##--Read cutsFile--##
   print '--Read cutsFile--',cutsFile
   handle=open(cutsFile,'r')
   exec(handle)
   handle.close()
   ##--Read NuisancesFile--##
   print '--Read NuisancesFile--',nuisancesFile
   handle=open(nuisancesFile,'r')
   exec(handle)
   handle.close()
   ##---END--##
   #print nuisances['QCDscale']
   histofile=outputDir+'/'+histofile
   #nuisances['QCDscale']['samples']['vbfHWWlnuqq_M1000']
   for samplename in nuisances[nuisacneName]['samples']:
      #plots_2017_Boosted_SKIM10_HMVar10_Fullvar_GGF_SB_ALL_Wjets0j
      print "--",samplename,"--"
      histofiles=glob.glob(outputDir+'/plots_'+tag+'_ALL_'+samplename+'.*root')
      for histofile in histofiles:
         MakeEnvelopShape_a_sample(samplename,nuisacneName,cuts,variables,histofile,nuisances)



'''


f=ROOT.TFile.Open(histofile,'UPDATE')
#f.ls()
#idx=0
for cut in sorted(cuts):
   #f.cd(cut)
   for var in sorted(variables):      
      #if idx==0:
      #   print "init dir"
      #   ROOT.gDirectory.pwd()
      #   print 'go to',cut,var
      #   f.cd(cut+'/'+var)
      #   print "--current dir--"
      #   ROOT.gDirectory.pwd()
      #   ROOT.gDirectory.WriteObject(histoana.mydict['bkg']['histo'][cut][var]['Sum'],'histo_PeudoData')
      #   ROOT.gDirectory.ls()

      f.cd(cut+'/'+var)
      #idx+=1
      #initdir=ROOT.gDirectory.CurrentDirectory()

      ROOT.gDirectory.WriteObject(histoana.mydict['bkg']['histo'][cut][var]['Sum'],'histo_PeudoData')
      #f.cd(initdir)
      #f.cd('../')
   #f.cd('../')
f.Close()
'''


print(datetime.datetime.now() - begin_time)
