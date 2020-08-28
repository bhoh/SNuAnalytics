submit=True

import sys
import os
import glob
sys.path.insert(0, "python_tool/")

from ExportShellCondorSetup import Export


sys.path.insert(1, os.getcwd())
from WPandCut2016 import *





REGION_LIST=['SR','SB','TOP']
#REGION_LIST=['TOP']
BOOST_LIST=['Boosted','Resolved']
#BOOST_LIST=['Boosted']


for reg in REGION_LIST:
    for bst in BOOST_LIST:
        rootfiles=glob.glob('rootFile*'+bst+'*'+reg+'*/plot*.root')
        #print rootfiles

        for rf in rootfiles: 
            if '_SI' in rf : continue ####pass S+I shape
            command_list=[
                'cd '+os.getcwd(),
                'python ScriptFilterShape/FilterShape.py -f '+rf
            ]
            command='&&'.join(command_list)
            
            
            #WORKDIR='WORKDIR_FilterShape/WORKDIR__FilterShape_'+'_'+bst+'_'+reg+'/'+rf.replace('.root','')
            WORKDIR='WORKDIR_FilterShape/WORKDIR__FilterShape_'+'_'+rf.replace('.root','')
            jobname='FilterShape'+'_'+bst+'_'+reg+'_'+Year
            ndone=len(glob.glob(WORKDIR+'/*.done'))
            if ndone>0:continue
            ncpu=1
            print WORKDIR
            Export(WORKDIR,command,jobname,submit,ncpu)

