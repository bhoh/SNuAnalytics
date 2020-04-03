import ROOT
import os
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.TrigMaker_cfg import Trigger

class HEMweight(Module):

    def __init__(self, isData, dataYear, jetColl="CleanJet", cmssw = 'Full2016', seed=65539):
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
        
        self.doHEMweight = int(self.dataYear) == 2018
        self.HEMPtScale = self.doHEMweight and not self.isData

        if jetColl=="CleanJet":
            self.IsCleanJetColl=True

    def beginJob(self): 
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.initReaders(inputTree) # initReaders must be called in beginFile
        self.out = wrappedOutputTree

        if self.doHEMweight:
          self.out.branch('HEMweight', 'F')
          self.out.branch('RunPeriod_HEM', 'I')
        if self.HEMPtScale:
          #self.out.branch('HEM%sPtScale'%self.jetColl, 'F', lenVar='n'+self.jetColl)
            self.out.branch(self.jetColl+'_HEMPtScale', 'F', lenVar='n'+self.jetColl) ##fix to NanoAOD format
          # getattr(self,'HEM%sPtScale'%self.jetColl) is self.doHEMweight and not self.isData
          # so RunPeriod_HEM should be already created in "if self.doHEMweight:"

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
        self.lumiFrac12 = self.TriggerCfg[1]['lumi'] + self.TriggerCfg[2]['lumi']
        self.lumiFrac12 /= self.lumi
        for i in range(len(self.RunFrac)):
            self.RunFrac[i] /= self.lumi

       
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""


        if not self.doHEMweight:
          return True
          
        if self.IsCleanJetColl:
            self.orig_jet_coll = Collection(event, "Jet" )
        HEMweight_ = 1.
        HEMJetPtScale_ = [1. for _ in range(getattr(event,'n'+self.jetColl))]
        if self.isData:
          run = event.run
          run_period = next(i + 1 for i in range(len(self.RunRange)) if self.RunRange[i][0] <= run <=self.RunRange[i][1] )
          if run_period == 3 or run_period == 4:
            jet_coll = Collection(event, self.jetColl )
            if self._hasHEMJet(jet_coll):
              HEMweight_ = 0.
            else:
              pass
        else:
          x = self.random.Rndm()
          run_period = next(i + 1 for i in range(len(self.RunFrac)) if self.RunFrac[i] >= x)
          jet_coll = Collection(event, self.jetColl )
          if self._hasHEMJet(jet_coll):
            HEMweight_ = self.lumiFrac12
          else:
            pass
          if run_period == 3 or run_period == 4:
            HEMJetPtScale_ = self._scaleHEMJetPt(jet_coll)            
        if self.doHEMweight:
          self.out.fillBranch('HEMweight', HEMweight_)
          self.out.fillBranch('RunPeriod_HEM',run_period)
        if self.HEMPtScale:
          self.out.fillBranch(self.jetColl+'_HEMPtScale', HEMJetPtScale_)
          # getattr(self,'HEM%sPtScale'%self.jetColl) is self.doHEMweight and not self.isData
          # so RunPeriod_HEM should be already stored in "if self.doHEMweight:"
        
        

                    
        return True

    def _hasHEMJet(self, jet_coll_):
        hasHEMJet = False

        ##if cleanjet, get the corrected pt value
        
        for jet in jet_coll_:
          pt  = jet["pt"]
          #print "cleanejt_pt->",pt
          if self.IsCleanJetColl: 
              #print "[jhchoi] Get orig jet coll"
              pt = self.orig_jet_coll[jet["jetIdx"]]["pt_nom"]
              #print ">>pt=",pt
          eta = jet["eta"]
          phi = jet["phi"]
          if pt > 15. and -3.0 < eta < -1.3 and -1.57 < phi < -0.87:
            hasHEMJet = True
            break
        return hasHEMJet

    def _scaleHEMJetPt(self, jet_coll_):
        HEMJetPtScale = []
        
        for jet in jet_coll_:
          #print"cleanejt_pt->",pt

          if self.IsCleanJetColl:
              #print "[jhchoi] Get orig jet coll"
              pt = self.orig_jet_coll[jet["jetIdx"]]["pt_nom"]
              #print ">>pt=",pt
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
          else:
            HEMJetPtScale.append(1.)

        return HEMJetPtScale
