submit=True

import sys
import os
sys.path.insert(0, "python_tool/")
from ExportShellCondorSetup import Export

sys.path.insert(1, "MassPoints")
from List_MX import *
sys.path.insert(1, "python_tool/latino/")
from List_MX_VBF import *



##
os.system('python TurnOffCombinedSamples.py WPandCut2016.py CombineMultiV')
os.system('python TurnOffCombinedSamples.py WPandCut2016.py CombineH125')
os.system('python TurnOffCombinedSamples.py WPandCut2016.py CombineWjets')
os.system('python TurnOffCombinedSamples.py WPandCut2016.py Combine_ggWW')
os.system('python TurnOffCombinedSamples.py WPandCut2016.py Combine_qqWWqq')
os.system('python TurnOffCombinedSamples.py WPandCut2016.py CombineSBI')


'''
   parser = optparse.OptionParser(usage)
   parser.add_option("-c","--conf",   dest="conf", help="configuration file's name")
   parser.add_option("-i","--inputlist",   dest="inputlist", help="inputlist")
   parser.add_option("-o","--outputname",   dest="outputname", help="outputname")

'''




REGION_LIST=['SR','SB','TOP']
BOOST_LIST=['Boosted','Resolved']
#PROC_LIST=['ggww','qqwwqq']
List_MX=[900]
List_MX_VBF=[900]
for reg in REGION_LIST:
    for bst in BOOST_LIST:
        ##--ggf
        for MX in List_MX:
            MX=str(MX)
            samplelist=[
                'ggWW',
                'ggHWWlnuqq_M125',
                'ggHWWlnuqq_M'+MX+'_SI'
            ]
            samplelist=','.join(samplelist)
            outputname='ggHWWlnuqq_M'+MX+'_SBI'
            command_list=[
                'cd '+os.getcwd(),
                'python ShapeSBI/Make_sbi_shape.py --c configuration_'+bst+'_'+reg+'.py --i '+samplelist+' -o '+outputname 
            ]
            command='&&'.join(command_list)
            
            
            WORKDIR='WORKDIR_SBI/WORKDIR__Make_'+outputname+'_'+bst+'_'+reg
            jobname='Make_'+outputname+'_'+bst+'_'+reg
            
            ncpu=1
            print WORKDIR
            Export(WORKDIR,command,jobname,submit,ncpu)
        

        ##--vbf
        for MX in List_MX_VBF:
            MX=str(MX)
            samplelist=[
                'qqWWqq',
                'vbfHWWlnuqq_M125',
                'vbfHWWlnuqq_M'+MX+'_SI'
            ]
            samplelist=','.join(samplelist)
            outputname='vbfHWWlnuqq_M'+MX+'_SBI'
            command_list=[
                'cd '+os.getcwd(),
                'python ShapeSBI/Make_sbi_shape.py --c configuration_'+bst+'_'+reg+'.py --i '+samplelist+' -o '+outputname 
            ]
            command='&&'.join(command_list)
            
            
            WORKDIR='WORKDIR_SBI/WORKDIR__Make_'+outputname+'_'+bst+'_'+reg
            jobname='Make_'+outputname+'_'+bst+'_'+reg
            
            ncpu=1
            print WORKDIR
            Export(WORKDIR,command,jobname,submit,ncpu)
            
