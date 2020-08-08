submit=True

import sys
import os
sys.path.insert(0, "python_tool/")
from ExportShellCondorSetup import Export

##
os.system('python TurnOffCombinedSamples.py WPandCut2016.py CombineMultiV')
os.system('python TurnOffCombinedSamples.py WPandCut2016.py CombineH125')
os.system('python TurnOffCombinedSamples.py WPandCut2016.py CombineWjets')
os.system('python TurnOffCombinedSamples.py WPandCut2016.py Combine_ggWW')
os.system('python TurnOffCombinedSamples.py WPandCut2016.py Combine_qqWWqq')
os.system('python TurnOffCombinedSamples.py WPandCut2016.py CombineSBI')



#python Make_ggww_qqwwqq_shape.py --c configuration_Boosted_SR.py --p ggww
#Export(WORKDIR,command,jobname,submit,ncpu)

REGION_LIST=['SR','SB','TOP']
BOOST_LIST=['Boosted','Resolved']
PROC_LIST=['ggWW','qqWWqq']

for reg in REGION_LIST:
    for bst in BOOST_LIST:
        for proc in PROC_LIST:
            command_list=[
                'cd '+os.getcwd(),
                'python ShapeFromMela/Make_ggww_qqwwqq_shape.py --c configuration_'+bst+'_'+reg+'.py --p '+proc
            ]
            command='&&'.join(command_list)


            WORKDIR='WORKDIR_ShapeFromMELA/WORKDIR__Make_'+proc+'_'+bst+'_'+reg
            jobname='Make_'+proc+'_'+bst+'_'+reg

            ncpu=1
            print WORKDIR
            Export(WORKDIR,command,jobname,submit,ncpu)
