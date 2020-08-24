import glob
import sys
import os
sys.path.insert(0, os.getcwd()+"/../")
from Parse_outfile_to_xsec import *
##---Parse condor out file
fvbf='floating'
Year='2016'
bst='Boosted' #Resolved/ALLchannel


WORKDIR='WORKDIR__AsymptoticLimit__'+fvbf

OUTPUTDIRS=glob.glob(WORKDIR+'/*')


#AsymptoticLimit__floating__Boosted__commbine__550__2016
#AsymptoticLimit__floating__Resolved__commbine__450_NoI__2016
for outdir in OUTPUTDIRS:
    f=open(outdir+'/run.out','r')
    lines=f.readlines()



            


