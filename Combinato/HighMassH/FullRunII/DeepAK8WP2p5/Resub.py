import glob
import os
WORKDIR='WORKDIR__MakeWorSpace'

jidlist=glob.glob(WORKDIR+'/*/*.jid')

for jid in jidlist:
    jds=jid.replace('.jid','.jds')
    command='condor_submit '+jds+' > '+jid
    print command
    #os.system(command)
