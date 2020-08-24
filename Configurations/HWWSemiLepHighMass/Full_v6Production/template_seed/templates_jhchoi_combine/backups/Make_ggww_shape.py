import ROOT
import optparse
import os
import sys
import glob
sys.path.insert(0, "MassPoints")
from List_MX import *
sys.path.insert(1, "python_tool/latino/")
from HistoParser import HistoParser


class dummy():##dummy
    def __init__(self):
       self.variablesFile=''
       self.cutsFile=''
       self.nuisancesFile=''
       self.samplesFile=''
opt=dummy()




def MakeAVG_ggWW(cuts,variables,samples,nuisances,rootfiledir,nuisanceName=''):
    SampleList={}
    for MX in List_MX:
        MX=str(MX)
        SampleList['ggHWWlnuqq_M'+MX+'_B']=[]
    #print sorted(SampleList)
    #rootfiledir='rootFile_2017_SigBkgEfficiency_addVBF_Boosted_HMFull_V11_cprime1.0BRnew0.0_DeepAK8WP0p5MD_dMchi2Resolution_SR/'

    TotalList=[]
    for p in SampleList:
        flist=glob.glob(rootfiledir+'/*_'+p+'.*root')
        SampleList[p]+=flist
        TotalList+=flist

        #print flist

    ##--Hadd
    tempdir=rootfiledir+'/_temp_ggWW/'
    os.system('mkdir -p '+tempdir)
    HaddedFile=tempdir+'/'+'plots_ggWW_avg.root'
    OutputFile=rootfiledir+'/plots_ggWW_avg.root'
    HaddInputs=' '.join(TotalList)
    os.system('hadd -f '+HaddedFile+' '+HaddInputs)

    samplename='ggWW'
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
    HaddedHistoName="histo_ggWW_"+nuisanceName

    if nuisanceName=='':
        this_dict[samplename]['samples']=sorted(SampleList)
        HaddedHistoName="histo_"+samplename
    #print "this_dict[samplename]['samples']",this_dict[samplename]['samples']
    histoana=HistoParser(this_dict)
    
    histoana.MakeWeightedAvgShape(HaddedHistoName)

    ##--Save the Shape
    #self.mydict[gr]['histo'][cut][variable]['WeightedAvg']
    f=ROOT.TFile.Open(OutputFile,'RECREATE')
    for cut in sorted(cuts):
        for var in sorted(variables):
            f.mkdir(cut+'/'+var)
            f.cd(cut+'/'+var)
            print "Store Shape on",cut+'/'+var+"/"+HaddedHistoName
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
   #parser.add_option("-f","--histofile",   dest="histofile", help="histofile's name")
   #parser.add_option("-n","--nuisanceName",   dest="nuisanceName", help="nuisanceName, for example QCDscale")

   (options, args) = parser.parse_args()

   conf=options.conf

   samples,variables,cuts,nuisances,rootfiledir=LoadConfiguration(conf)
   ##For nominal
   MakeAVG_ggWW(cuts,variables,samples,nuisances,rootfiledir)
   
   
   ##--For shape nuisances
   NuisanceList=[]
   for nuisance in nuisances:
       if nuisances[nuisance]['type']=='shape':
           NuisanceList.append(nuisance)
    
   for nuisance in NuisanceList:
       print '[',nuisance,']'
       for _var in ['Up','Down']:
           print _var
           MakeAVG_ggWW(cuts,variables,samples,nuisances,rootfiledir,nuisance+_var)

    





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
