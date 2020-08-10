SUBMIT=True
#SUBMIT=False
import optparse
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

def ExportMakeEnvelopShape_a_sample(samplename,nuisacneName,cuts,variables,histofile,nuisances,outputdirpath):
   print "[MakeEnvelopShape_a_sample]"
   print "samplename",samplename
   print "nuisacneName",nuisacneName
   print "len(cuts)",len(cuts)
   print "len(variables)",len(variables)
   print "histofile",histofile
   print "len(nuisances)",len(nuisances)
   print "outputdirpath",outputdirpath
   jobname=histofile.split('/')[-1].replace('.root','')
   print jobname
   this_dict={#QCDscale
      samplename:{
         'cuts':sorted(cuts),
         'variables':sorted(variables),
         'FileName':histofile,
         'samples':[samplename+'_'+nuisacneName+'V'+str(i)+'Var' for i in range(0,len(nuisances[nuisacneName]['samples'][samplename]))]
      },
   }
   ##Export dictionary
   #WORKDIR= outputdirpath+"/Calc_"+nuisacneName+"/WORKDIR_"+nuisacneName+"_"+samplename+'/'##define working directory
   WORKDIR= outputdirpath+"/Calc_"+nuisacneName+"/WORKDIR_"+nuisacneName+"_"+jobname+'/'##define working directory
   os.system("mkdir -p "+WORKDIR)
   f=open(WORKDIR+'/run.py','w')
   f.write('import os\n')
   f.write('import sys\n')
   f.write('import ROOT\n')
   f.write('sys.path.insert(0, "'+os.getcwd()+'/python_tool/latino/")\n')
   f.write('from HistoParser import HistoParser\n')
   f.write('os.chdir("'+os.getcwd()+'")\n')
   f.write("this_dict="+str(this_dict)+'\n')
   f.write("nuisacneName='"+nuisacneName+"'\n")
   f.write("samplename='"+samplename+"'\n")
   f.write("histofile='"+histofile+"'\n")
   f.write("outputdirpath='"+outputdirpath+"'\n")
   f.write("cuts="+str(cuts)+'\n')
   f.write("variables="+str(variables)+'\n')
   f.write('''
import datetime
begin_time = datetime.datetime.now()
histoana=HistoParser(this_dict)
histoana.MakeEnvelopShape("histo_"+samplename+'_'+nuisacneName)
   
#f=ROOT.TFile.Open(outputdirpath+"/"+jobname+'_'+nuisacneName+'.root','UPDATE')
f=ROOT.TFile.Open(histofile,'UPDATE')
for cut in sorted(cuts):
   for var in sorted(variables):
    #f.mkdir(cut+'/'+var)
    f.cd(cut+'/'+var)
    print "Store Shape on",cut+'/'+var+"/histo_"+samplename+'_'+nuisacneName+'Up'
    ROOT.gDirectory.WriteObject(histoana.mydict[samplename]['histo'][cut][var]['envelopUp'],"histo_"+samplename+'_'+nuisacneName+'Up')
    print "Store Shape on",cut+'/'+var+"/histo_"+samplename+'_'+nuisacneName+'Down'
    ROOT.gDirectory.WriteObject(histoana.mydict[samplename]['histo'][cut][var]['envelopDown'],"histo_"+samplename+'_'+nuisacneName+'Down')
         
f.Close()
print(datetime.datetime.now() - begin_time)

   ''')
   ##--ExEfile
   f=open(WORKDIR+'/run.sh','w')
   lines=[]

   lines.append("#!/bin/bash")
   lines.append("export VO_CMS_SW_DIR="+os.getenv("VO_CMS_SW_DIR"))
   lines.append("export SCRAM_ARCH="+os.getenv("SCRAM_ARCH"))
   lines.append("source $VO_CMS_SW_DIR/cmsset_default.sh")
   lines.append("cd "+os.getenv("CMSSW_BASE"))
   lines.append("eval `scramv1 ru -sh`")
   lines.append('cd '+os.getcwd()+'/'+WORKDIR)
   lines.append('python run.py')
   for line in lines:
      f.write(line+'\n')
   f.close()
   os.system('chmod u+x '+WORKDIR+'/run.sh')
   ##--Jdsfile
   f=open(WORKDIR+'/run.jds','w')
   lines=[]
   lines.append('executable = '+os.getcwd()+'/'+WORKDIR+'/run.sh')
   lines.append('universe = vanilla')
   lines.append('output = '+os.getcwd()+'/'+WORKDIR+'/run.out')
   lines.append('error = '+os.getcwd()+'/'+WORKDIR+'/run.err')
   lines.append('log = '+os.getcwd()+'/'+WORKDIR+'/run.log')
   lines.append('request_cpus = 1')
   lines.append('accounting_group=group_cms')
   lines.append('JobBatchName='+jobname+'_'+nuisacneName)
   #lines.append('request_memory = '+str(int(self.memory))+' MB \n')
   lines.append('queue')
   for line in lines:
      f.write(line+'\n')
   f.close()
   if SUBMIT:
      command='condor_submit '+WORKDIR+'/run.jds > '+WORKDIR+'run.jid'
      print command
      os.system(command)

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


def RunInteractive():
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
   samplesFile=samplesFile.replace('.py','_dummy.py')
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
   idx=0
   total=len(nuisances[nuisacneName]['samples'])
   for samplename in nuisances[nuisacneName]['samples']:
      #plots_2017_Boosted_SKIM10_HMVar10_Fullvar_GGF_SB_ALL_Wjets0j
      print idx,'/',total
      print "--",samplename,"--"
      #histofiles=glob.glob(outputDir+'/plots_'+tag+'_ALL_'+samplename+'.*root')
      #for histofile in histofiles:
      MakeEnvelopShape_a_sample(samplename,nuisacneName,cuts,variables,histofile,nuisances)
      idx+=1

if __name__ == '__main__':
   usage = 'usage: %prog [options]'
   parser = optparse.OptionParser(usage)
   parser.add_option("-c","--conf",   dest="conf", help="configuration file's name")
   parser.add_option("-f","--histofile",   dest="histofile", help="histofile's name")
   parser.add_option("-n","--nuisacneName",   dest="nuisacneName", help="nuisacneName, for example QCDscale")
   parser.add_option("-s","--samplename",   dest="samplename", help="samplename")
   (options, args) = parser.parse_args()
   
   conf=options.conf
   histofile=options.histofile
   nuisacneName=options.nuisacneName
   samplename=options.samplename
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
   samplesFile=samplesFile.replace('.py','_dummy.py')
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
   ##--Run
   MakeEnvelopShape_a_sample(samplename,nuisacneName,cuts,variables,histofile,nuisances)
   #histofile=outputDir+'/'+histofile
   #os.system("mkdir -p "+outputDir+'/'+nuisacneName+'/')
   #idx=0
   #total=len(nuisances[nuisacneName]['samples'])
   #for samplename in nuisances[nuisacneName]['samples']:
   #   print idx,'/',total
   #   #print "--",samplename,"--"
   #   #ExportMakeEnvelopShape_a_sample(samplename,nuisacneName,cuts,variables,histofile,nuisances,outputDir+'/'+nuisacneName)

   #   histofiles=glob.glob(outputDir+'/plots_'+tag+'_ALL_'+samplename+'.*root')
   #   for histofile in histofiles:                                                                                                            
   #      ExportMakeEnvelopShape_a_sample(samplename,nuisacneName,cuts,variables,histofile,nuisances,outputDir+'/'+nuisacneName)
   #   idx+=1






print(datetime.datetime.now() - begin_time)
