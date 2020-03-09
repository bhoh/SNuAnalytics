import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import math, re

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict


class BTagReshapeNormProducer(Module):
    def __init__(self):
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.systs_shape_norm = []
        for syst in [ 'jes',
                      'lf', 'hf',
                      'hfstats1', 'hfstats2',
                      'lfstats1', 'lfstats2',
                      'cferr1', 'cferr2' ]:
            self.systs_shape_norm.append("up_%s" % syst)
            self.systs_shape_norm.append("down_%s" % syst)
        self.central_and_systs_shape_norm = [ "central" ]
        self.central_and_systs_shape_norm.extend(self.systs_shape_norm)
        self.branchNames_central_and_systs_shape_norm={}
        for central_or_syst in self.central_and_systs_shape_norm:
            if central_or_syst == "central":
                self.branchNames_central_and_systs_shape_norm[central_or_syst] = "btagReshapeNorm"
            else:
                self.branchNames_central_and_systs_shape_norm[central_or_syst] = "btagReshapeNorm_%s" % central_or_syst
            self.out.branch(self.branchNames_central_and_systs_shape_norm[central_or_syst],'F')     

                
    
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        for central_or_syst in self.central_and_systs_shape_norm:
          weight = 1.
          for i in range(event.nCleanJet):
            #print event.nCleanJet , event.nJet , i , event.CleanJet_jetIdx[i]
            #weight = weight*event.Jet_btagSF_shape[event.CleanJet_jetIdx[i]]
            idx = event.CleanJet_jetIdx[i]
            jet_flav = event.Jet_hadronFlavour[idx]
            jet_pt = event.Jet_pt[idx]
            jet_eta = event.Jet_eta[idx]
            btagReshapeNorm = self.GetBTagReshapeNorm(jet_flav, jet_pt, jet_eta, central_or_syst)
            weight *= btagReshapeNorm
          
          self.out.fillBranch(self.branchNames_central_and_systs_shape_norm[central_or_syst], weight)   

        return True

    def GetBTagReshapeNorm(self, flav, pt, eta, central_or_syst):
        ######
        # place holder
        # read normalization weight from external root file
        ######
        
        return 1.


    def GetBtvPOGbinning(self, flav, pt, eta):

        absEta = abs(eta)

        if pt < 20:
          raise ValueError("GetBtvPOGbinning : pt range out of bound, pt : %.2f" % pt )
        if absEta >= 2.5: # 2.4 / 2.5/ 2.5 ( 2016 / 2017 / 2018 )
          raise ValueError("GetBtvPOGbinning : absEta range out of bound, absEta : %.2f" % absEta )

        if flav==5:
          if pt < 30:
            outBinIdx = 0
          elif pt < 50:
            outBinIdx = 1
          elif pt < 70:
            outBinIdx = 2
          elif pt < 100:
            outBinIdx = 3
          else:
            outBinIdx = 4
        elif flav==4:
            outBinIdx = 0
        elif flav==0:
          if pt < 30:
            if absEta < 0.8:
              outBinIdx = 0
            elif absEta < 1.6:
              outBinIdx = 1
            elif absEta < 2.5: # 2.4 / 2.5/ 2.5 ( 2016 / 2017 / 2018 )
              outBinIdx = 2
          elif pt < 40:
            if absEta < 0.8:
              outBinIdx = 3
            elif absEta < 1.6:
              outBinIdx = 4
            elif absEta < 2.5: # 2.4 / 2.5/ 2.5 ( 2016 / 2017 / 2018 )
              outBinIdx = 5
          elif pt < 60:
            if absEta < 0.8:
              outBinIdx = 6
            elif absEta < 1.6:
              outBinIdx = 7
            elif absEta < 2.5: # 2.4 / 2.5/ 2.5 ( 2016 / 2017 / 2018 )
              outBinIdx = 8
          else:
            if absEta < 0.8:
              outBinIdx = 9
            elif absEta < 1.6:
              outBinIdx = 10
            elif absEta < 2.5: # 2.4 / 2.5/ 2.5 ( 2016 / 2017 / 2018 )
              outBinIdx = 11

        else:
            raise ValueError("GetBtvPOGbinning : hadronFlavour of %d is not supported"%flav)

        return outBinIdx
