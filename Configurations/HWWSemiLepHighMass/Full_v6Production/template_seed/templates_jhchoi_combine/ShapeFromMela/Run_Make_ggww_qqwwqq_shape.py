submit=True
import glob
import sys
import os
sys.path.insert(0, "python_tool/")

from ExportShellCondorSetup import Export

sys.path.insert(1, os.getcwd())
from WPandCut2016 import *
##


##---Before start, check PDF/QCDscale jobs

list_qcdscalejob=glob.glob('WORKDIR__QCDscaleAccept/*/*/*.jid ')
list_pdfjob=glob.glob('WORKDIR__WORKDIR__pdfAccept/*/*/*.jid ')
nqcd=len(list_qcdscalejob)
npdf=len(list_pdfjob)

if nqcd+npdf!=0:
    print "[!!!]PDF,QCDscale job not finished, stop run MELA bkg shape"
    exit()
else:
    print "[PDF,QCDscale] no remaining jobs"


#python Make_ggww_qqwwqq_shape.py --c configuration_Boosted_SR.py --p ggww
#Export(WORKDIR,command,jobname,submit,ncpu)

#REGION_LIST=['SR','SB','TOP']
BOOST_LIST=['Boosted','Resolved']
PROC_LIST=['ggWW','qqWWqq']

##---block for change region list
<__REGION_LIST__>



if Year!="2016":
    print "Year=",Year
    PROC_LIST=['ggWW']

for reg in REGION_LIST:
    for bst in BOOST_LIST:
        for proc in PROC_LIST:
            command_list=[
                'cd '+os.getcwd(),
                'python ShapeFromMela/Make_ggww_qqwwqq_shape.py --c configuration_'+bst+'_'+reg+'.py --p '+proc
            ]
            command='&&'.join(command_list)


            WORKDIR='WORKDIR_ShapeFromMELA/WORKDIR__Make_'+proc+'_'+bst+'_'+reg
            jobname='Make_'+proc+'_'+bst+'_'+reg+'_'+Year

            ncpu=1
            print WORKDIR
            Export(WORKDIR,command,jobname,submit,ncpu)
