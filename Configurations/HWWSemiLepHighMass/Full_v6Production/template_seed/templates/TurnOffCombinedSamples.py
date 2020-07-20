##TurnOffCombinedSamples.py
import sys
#print sys.argv[1]
filename=sys.argv[1]
flag=sys.argv[2]

f=open(filename,'r')
fnew=open(filename+'_new','w')
lines=f.readlines()


#FLAGDICT={'CombineMultiV':False,'CombineH125':False}
#FLAGLIST=['CombineMultiV','CombineH125']
for line in lines:

    #if flag in line and 'True' in line:
    #print line.replace(' ','')
    if flag+'=True' in line.replace(' ',''):
        print flag,'= True',', turn off'
        line=line.replace('True','False')
            
    fnew.write(line)
f.close()
fnew.close()
import os
os.system('mv '+filename+'_new '+filename)





