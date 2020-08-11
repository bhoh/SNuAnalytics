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



def MakeSampleList(rootfiledir,prod):
    prefix=''
    alias=''
    if prod=='ggWW':
        prefix='ggHWWlnuqq'
        List_Mass=List_MX
    elif prod=='qqWWqq':
        prefix='vbfHWWlnuqq'
        List_Mass=List_MX_VBF
    alias=prod
    SampleList={}

    for MX in List_Mass:
        if MX < 300:continue
        if MX > 900 : continue
        MX=str(MX)
        SampleList[prefix+'_M'+MX+'_B']=[]
    return SampleList
    
def HaddFiles(rootfiledir,prod):

    alias=prod
    SampleList=MakeSampleList(rootfiledir,prod)
    

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


def MakeAVG(cuts,variables,samples,nuisances,rootfiledir,prod,nuisance='',var=''):
    alias=prod
    SampleList=MakeSampleList(rootfiledir,prod)

    tempdir=rootfiledir+'/_temp_'+alias+'/'
    HaddedFile=tempdir+'/'+'plots_'+alias+'.root'
    OutputFile=rootfiledir+'/plots_'+alias+'.root'

    samplename=alias
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
    
    histoana.MakeWeightedAvgShape(HaddedHistoName)

    ##--Save the Shape
    #self.mydict[gr]['histo'][cut][variable]['WeightedAvg']
    f=ROOT.TFile.Open(OutputFile,'Update')
    for cut in sorted(cuts):
        for var in sorted(variables):
            f.mkdir(cut+'/'+var)
            f.cd(cut+'/'+var)
            print "Store Shape on",cut+'/'+var+"/"+HaddedHistoName
            histoana.mydict[samplename]['histo'][cut][var]['WeightedAvg'].SetTitle(HaddedHistoName)
            histoana.mydict[samplename]['histo'][cut][var]['WeightedAvg'].SetName(HaddedHistoName)
            if histoana.mydict[samplename]['histo'][cut][var]['WeightedAvg'].Integral()<=0:
                histoana.mydict[samplename]['histo'][cut][var]['WeightedAvg'].SetEntries(0)
            ROOT.gDirectory.WriteObject(histoana.mydict[samplename]['histo'][cut][var]['WeightedAvg'],HaddedHistoName)
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
   parser.add_option("-p","--prod",   dest="prod", help="ggWW or qqWWqq")
   #parser.add_option("-f","--histofile",   dest="histofile", help="histofile's name")
   #parser.add_option("-n","--nuisanceName",   dest="nuisanceName", help="nuisanceName, for example QCDscale")

   (options, args) = parser.parse_args()

   conf=options.conf
   prod=options.prod
   if prod!='ggWW' and prod!='qqWWqq':
       print "!!!!Please --p ggWW OR qqWWqq"
       exit()

   samples,variables,cuts,nuisances,rootfiledir=LoadConfiguration(conf)
   ##For nominal
   #MakeAVG_ggWW(cuts,variables,samples,nuisances,rootfiledir)
   

   ##--Hadd
   HaddFiles(rootfiledir,prod)


   MakeAVG(cuts,variables,samples,nuisances,rootfiledir,prod)
   
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
