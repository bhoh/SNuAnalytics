from LatinoAnalysis.Tools.HiggsXSection  import *
HiggsXS = HiggsXSection()


import sys
sys.path.insert(0, "MassPoints")
from List_MX import *
from List_MX_VBF import *


##--xsec of signals


for MX in List_MX:
    print '--',MX,'--'
    print HiggsXS.GetHiggsProdXS('YR4','13TeV','ggH',int(MX),'bsm')
    print HiggsXS.GetHiggsProdXS('YR4','13TeV','vbfH',int(MX),'bsm')

    
