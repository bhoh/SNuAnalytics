import os
#yrlist=['2016','2017','2018']
#for yr in yrlist:
if os.path.exists('samples_2016.py'):
    fdummy=open('samples_2016_dummy.py','w')
    fdummy.write('samples={}\n')
    
    f=open('samples_2016.py','r')
    exec(f)
    for s in samples:
        fdummy.write('samples["'+s+'"]={}\n')
        
