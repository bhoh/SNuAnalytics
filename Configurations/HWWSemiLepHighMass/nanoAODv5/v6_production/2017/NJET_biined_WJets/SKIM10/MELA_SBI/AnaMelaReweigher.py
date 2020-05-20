import sys
sys.path.append('python_tool/latino')

from HistoParser import HistoParser
import ROOT
mydict={
    'gr1':{
        'cuts':['1'],
        'variables':['LHE_ptWW','LHE_mWW','GEN_mH','GEN_ptH'],
        'FileName':'rootFile_2017_Boosted_SKIM10_HMVar10_MELASBI/hadd.root',
        'samples':['ggHWWlnuqq_M'+str(M)+'_B' for M in [200,400,700,900,2000]]
    }
}
print mydict['gr1']['samples']

test=HistoParser(mydict)
c=ROOT.TCanvas()
test.mydict['gr1']['histo']['1']['LHE_ptWW']['ggHWWlnuqq_M200_B'].Draw()
c.SaveAs('test.png')
