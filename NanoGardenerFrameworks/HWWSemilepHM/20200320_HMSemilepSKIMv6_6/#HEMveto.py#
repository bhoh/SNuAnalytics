import ROOT
import os
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.TrigMaker_cfg import Trigger

class HEMveto(Module):
    #ref: https://hypernews.cern.ch/HyperNews/CMS/get/JetMET/1995/2.html
    #ref: https://hypernews.cern.ch/HyperNews/CMS/get/JetMET/2000.html

    def __init__(self, isData, dataYear, jetColl="CleanJet", cmssw = 'Full2016', seed=65539):
        print "isData=",isData
        print "dataYear=",dataYear
        #self.TriggerCfg = Trigger[cmssw] #2018 period range not available
        #ref : https://twiki.cern.ch/twiki/bin/view/CMS/PdmV2018Analysis
        self.TriggerCfg = {
                            1 : {'begin':315252 , 'end':316995, 'lumi':13.48},
                            2 : {'begin':317080 , 'end':319310, 'lumi':6.785},
                            3 : {'begin':319337 , 'end':320065, 'lumi':6.612},
                            4 : {'begin':320673 , 'end':325175, 'lumi':31.95},
                          }
        self.random = ROOT.TRandom3(seed)
        self.isData = isData
        self.dataYear   = dataYear
        self.jetColl = jetColl

    def beginJob(self): 
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.initReaders(inputTree) # initReaders must be called in beginFile
        self.out = wrappedOutputTree
        
        self.out.branch('HEMveto', 'F')
        if not self.isData and int(self.dataYear) == 2018:
          self.out.branch('HEM%sPtScale'%self.jetColl, 'F', lenVar='n'+self.jetColl)

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def initReaders(self,tree): # this function gets the pointers to Value and ArrayReaders and sets them in the C++ worker class
        self.RunRange = []
        self.RunFrac = []
        self.lumi = 0.
        for RunCfg in self.TriggerCfg.itervalues():
            self.lumi += RunCfg['lumi']
            self.RunFrac.append(self.lumi)
            self.RunRange.append((RunCfg['begin'],RunCfg['end']))
        
        for i in range(len(self.RunFrac)):
            self.RunFrac[i] /= self.lumi

       
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        HEMveto_ = 1
        HEMJetPtScale_ = [1. for _ in range(getattr(event,'n'+self.jetColl))]
        if not int(self.dataYear) == 2018:
          pass
        else:
          if self.isData:
            run = event.run
            run_period = next(i + 1 for i in range(len(self.RunRange)) if self.RunRange[i][0] <= run <=self.RunRange[i][1] )
          else:
            x = self.random.Rndm()
            run_period = next(i + 1 for i in range(len(self.RunFrac)) if self.RunFrac[i] >= x)

          if run_period == 3 or run_period == 4:
            jet_coll = Collection(event, self.jetColl )
            if self._hasHEMJet(jet_coll):
              HEMveto_ = 0
            else:
              pass

            if not self.isData:
              HEMJetPtScale_ = self._scaleHEMJetPt(jet_coll)

        self.out.fillBranch('HEMveto', HEMveto_)
        if not self.isData and int(self.dataYear) == 2018:
          self.out.fillBranch('HEM%sPtScale'%self.jetColl, HEMJetPtScale_)

        return True


    def _hasHEMJet(self, jet_coll_):
        hasHEMJet = False
        for jet in jet_coll_:
          pt  = jet["pt"]
          eta = jet["eta"]
          phi = jet["phi"]
          if pt > 15. and -3.0 < eta < -1.3 and -1.57 < phi < -0.87:
            hasHEMJet = True
            break
        return hasHEMJet

    def _scaleHEMJetPt(self, jet_coll_):
        HEMJetPtScale = []
        for jet in jet_coll_:
          pt  = jet["pt"]
          eta = jet["eta"]
          phi = jet["phi"]
          if pt > 15. and -1.57 < phi < -0.87:
            if -2.5 < eta < -1.3:
              HEMJetPtScale.append(0.8) # scale down 20% 
            elif -3.0 < eta <= -2.5:
              HEMJetPtScale.append(0.65) # scale down 35%
          else:
            HEMJetPtScale.append(1.)

        return HEMJetPtScale
