from LatinoAnalysis.Tools.HiggsXSection  import *
HiggsXS = HiggsXSection()

import sys
sys.path.insert(0, "MassPoints")
from List_MX import *
from List_MX_VBF import *

#BR=HiggsXS.GetHiggsBR('YR4','1H_WW',int(MX),,'bsm') ##   def GetHiggsBR(self,YRversion,decay,mh,model='sm'):
#'YR4','13TeV','vbfH',int(MX),'bsm'
print "BR={}"
for MX in sorted(list(set(List_MX+List_MX_VBF))):
    BR=HiggsXS.GetHiggsBR('YR4','H_WW',int(MX),'bsm') ##   def GetHiggsBR(self,YRversion,decay,mh,model='sm'):
    print 'BR[',MX,']=','[',BR,']'
