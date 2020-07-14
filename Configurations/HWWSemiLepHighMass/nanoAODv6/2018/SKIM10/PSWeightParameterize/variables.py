isFinal=False
#isFinal=True
print "isFinal=",isFinal
import os
import sys
sys.path.append(os.getcwd())


#-----Variable Deinition-----#
from WPandCut2018 import *


#------End of Variable Definition-----#
#variables={}

variables['Event'] = {
    'name' : '1',
    'range':(1,0,2),
    'xaxis':'1',
    'fold': 0
}


#     PSWeightISR[s]=["PSWeight[0]","PSWeight[1]"]
#     PSWeightFSR[s]=["PSWeight[2]","PSWeight[3]"]


variables['PSWeight[0]'] = {
    'name' : 'PSWeight[0]',
    'range':(200,0,2),
    'xaxis':'PSWeight[0]',
    'fold': 3
}

variables['PSWeight[1]'] = {
    'name' : 'PSWeight[1]',
    'range':(200,0,2),
    'xaxis':'PSWeight[1]',
    'fold': 3
}

variables['PSWeight[2]'] = {
    'name' : 'PSWeight[2]',
    'range':(200,0,2),
    'xaxis':'PSWeight[2]',
    'fold': 3
}

variables['PSWeight[3]'] = {
    'name' : 'PSWeight[3]',
    'range':(200,0,2),
    'xaxis':'PSWeight[3]',
    'fold': 3
}









print "len(variables)=",len(variables)
