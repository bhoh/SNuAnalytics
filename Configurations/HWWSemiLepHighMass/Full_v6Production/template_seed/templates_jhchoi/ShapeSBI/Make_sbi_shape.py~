TurnOff=False
import ROOT
import optparse
import os
import sys
import glob
sys.path.insert(0, "MassPoints")
from List_MX import *
sys.path.insert(1, "python_tool/latino/")
from List_MX_VBF import *

from HistoParser import HistoParser


class dummy():##dummy
    def __init__(self):
       self.variablesFile=''
       self.cutsFile=''
       self.nuisancesFile=''
       self.samplesFile=''
opt=dummy()
if TurnOff: 
    os.system('python TurnOffCombinedSamples.py WPandCut2016.py CombineMultiV')
    os.system('python TurnOffCombinedSamples.py WPandCut2016.py CombineH125')
    os.system('python TurnOffCombinedSamples.py WPandCut2016.py CombineWjets')
    os.system('python TurnOffCombinedSamples.py WPandCut2016.py Combine_ggWW')
    os.system('python TurnOffCombinedSamples.py WPandCut2016.py Combine_qqWWqq')
    os.system('python TurnOffCombinedSamples.py WPandCut2016.py CombineSBI')



def MakeSampleList(rootfiledir,inputlist):
    SampleList={}
    for i in inputlist:
        
        SampleList[i]=[]
    return SampleList
    
def HaddFiles(rootfiledir,inputlist,outputname):

    #alias='_'.join(inputlist)
    alias=outputname
    SampleList=MakeSampleList(rootfiledir,inputlist)
    

    TotalList=[]
    for p in SampleList:
        flist=glob.glob(rootfiledir+'/*_'+p+'.*root')
        SampleList[p]+=flist
        TotalList+=flist

        #print flist

    ##--Hadd
    tempdir=rootfiledir+'/_temp_'+alias+'/'
    os.system('mkdir -p '+tempdir)
    HaddedFile=tempdir+'/'+'plots_'+alias+'.root'
    OutputFile=rootfiledir+'/plots_'+alias+'.root'
    HaddInputs=' '.join(TotalList)
    os.system('hadd -f '+HaddedFile+' '+HaddInputs)


def MakeSUM(cuts,variables,samples,nuisances,rootfiledir,inputlist,outputname,nuisance='',var=''):
    alias=outputname
    SampleList=MakeSampleList(rootfiledir,inputlist)

    tempdir=rootfiledir+'/_temp_'+alias+'/'
    HaddedFile=tempdir+'/'+'plots_'+alias+'.root'
    OutputFile=rootfiledir+'/plots_'+alias+'.root'

    samplename=outputname
    ##---Make ggWW shape
    this_dict={#QCDscale

        samplename:{
            'cuts':sorted(cuts),
            'variables':sorted(variables),
            #'FileName':histofile,
            #'samples':[samplename+'_'+samplename+'V'+str(i)+'Var' for i in range(0,len(nuisances[samplename]['samples'][samplename]))]
        }
    }
    this_dict[samplename]['FileName']=HaddedFile
    HaddedHistoName="histo_"+alias #+"_"+nuisanceName

    if nuisance=='':
        this_dict[samplename]['samples']=sorted(SampleList) ##histos to read
        HaddedHistoName="histo_"+samplename ##save name
    else:
        this_dict[samplename]['samples']=[]
        nuisanceName=nuisances[nuisance]['name']
        for s in sorted(SampleList):
            if s in sorted(nuisances[nuisance]['samples']):
                this_dict[samplename]['samples'].append(s+'_'+nuisanceName+var)
        HaddedHistoName="histo_"+samplename+'_'+nuisanceName+var
        #HaddedHistoName="histo_"+samplename+var
    #print "this_dict[samplename]['samples']",this_dict[samplename]['samples']
    if len(this_dict[samplename]['samples'])==0 :
        return False
    histoana=HistoParser(this_dict)
    
    #histoana.MakeWeightedAvgShape(HaddedHistoName)

    ##--Save the Shape
    #self.mydict[gr]['histo'][cut][variable]['WeightedAvg']
    f=ROOT.TFile.Open(OutputFile,'Update')
    for cut in sorted(cuts):
        for var in sorted(variables):
            f.mkdir(cut+'/'+var)
            f.cd(cut+'/'+var)
            print "Store Shape on",cut+'/'+var+"/"+HaddedHistoName
            histoana.mydict[samplename]['histo'][cut][var]['Sum'].SetTitle(HaddedHistoName)
            histoana.mydict[samplename]['histo'][cut][var]['Sum'].SetName(HaddedHistoName)
            ROOT.gDirectory.WriteObject(histoana.mydict[samplename]['histo'][cut][var]['Sum'],HaddedHistoName)
            #print "Store Shape on",cut+'/'+var+"/histo_"+samplename+'_'+nuisanceName+'Down'
            #ROOT.gDirectory.WriteObject(histoana.mydict[samplename]['histo'][cut][var]['envelopDown'],"histo_"+samplename+'_'+nuisanceName+'Down')
            
    f.Close()
    print "[output]=",OutputFile
def LoadConfiguration(conf):

   #histofile=options.histofile
   #nuisanceName=options.nuisanceName
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

   return samples,variables,cuts,nuisances,outputDir

if __name__ == '__main__':
   usage = 'usage: %prog [options]'
   parser = optparse.OptionParser(usage)
   parser.add_option("-c","--conf",   dest="conf", help="configuration file's name")
   parser.add_option("-i","--inputlist",   dest="inputlist", help="inputlist")
   parser.add_option("-o","--outputname",   dest="outputname", help="outputname")
   #parser.add_option("-f","--histofile",   dest="histofile", help="histofile's name")
   #parser.add_option("-n","--nuisanceName",   dest="nuisanceName", help="nuisanceName, for example QCDscale")

   (options, args) = parser.parse_args()

   conf=options.conf
   inputlist=options.inputlist
   inputlist=inputlist.split(',')
   outputname=options.outputname
   #if prod!='ggww' and prod!='qqwwqq':
   #    print "!!!!Please --p ggww OR qqwwqq"
   #    exit()

   samples,variables,cuts,nuisances,rootfiledir=LoadConfiguration(conf)
   ##For nominal
   #MakeAVG_ggWW(cuts,variables,samples,nuisances,rootfiledir)
   

   ##--Hadd
   HaddFiles(rootfiledir,inputlist,outputname)


   MakeSUM(cuts,variables,samples,nuisances,rootfiledir,inputlist,outputname)
   
   #--SampleList
   #SampleList=MakeSampleList(rootfiledir,prod)
   ##--For shape nuisances
   NuisanceList=[]
   for nuisance in nuisances:
       if nuisances[nuisance]['type']=='shape':
           NuisanceList.append(nuisance)
    
   for nuisance in NuisanceList:
       print '[',nuisance,']'
       for _var in ['Up','Down']:
           print _var
           MakeAVG(cuts,variables,samples,nuisances,rootfiledir,prod,nuisance,_var)

    





'''
(python python_tool/latino/CombineShapesToAvg.py -c configuration_Boosted.py -f ${ggWWfile} -s ${PROCINPUT} -n ggWW -o;cp ${ggWWfile}_ggWW ${rootfiledir}/plot_ggWW.root)&> logs/Make_ggww_shape_Boosted.log&


#--Resolved
listR=(
ggHWWlnuqq_M300_B
ggHWWlnuqq_M350_B
ggHWWlnuqq_M400_B
ggHWWlnuqq_M450_B
ggHWWlnuqq_M500_B
ggHWWlnuqq_M550_B
ggHWWlnuqq_M600_B
ggHWWlnuqq_M125
)
rootfiledir=`ls -d rootFile*Resol*/`
echo ${rootfiledir}
##hadd_above process files
haddlist=""
for p in ${listR[@]};do
    thisfile=`ls ${rootfiledir}/hadddir_${p}/hadd_${p}.root`
    echo $thisfile
    haddlist=$haddlist" $thisfile"
done
echo $haddlist
mkdir -p ${rootfiledir}/ggWW/
ggWWfile=${rootfiledir}/ggWW/plots_ggWW.root
echo $ggWWfile
echo "hadd -f ${ggWWfile} ${haddlist}"
hadd -f ${ggWWfile} ${haddlist}

PROCINPUT=""
for PROC in ${listR[@]};do
    PROCINPUT="${PROCINPUT},${PROC}"
done
PROCINPUT=${PROCINPUT#,}

(python python_tool/latino/CombineShapesToAvg.py -c configuration_Resolved.py -f ${ggWWfile} -s ${PROCINPUT} -n ggWW -o;cp ${ggWWfile}_ggWW ${rootfiledir}/plot_ggWW.root)&> logs/Make_ggww_shape_Resolved.log&


'''
