import sys
import os
sys.path.insert(0,os.getcwd()+'/../')
sys.path.insert(0,os.getcwd()+'/../python_tool')
from Command import *


Years=[2016,2017,2018]
##--EachYear
for Year in Years:
    continue
    CpCards(Year)
    CombineCardYear(Year)
    MakeWorkSpace(Year)
    continue
    GetAsymptoticLimit(Year)
##FullRunII
#3yr
CombineCardYear('3yr')
MakeWorkSpace('3yr')
