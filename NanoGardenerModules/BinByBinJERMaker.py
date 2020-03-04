import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict


class BinByBinJERMaker(Module):
    def __init__(self, jetType = "AK8PFPuppi"):
      if "AK4" in jetType : 
        self.jetBranchName = "Jet"
      elif "AK8" in jetType :
        self.jetBranchName = "FatJet"
      else:
        raise ValueError("ERROR: Invalid jet type = '%s'!" % jetType)
      self.lenVar = "n" + self.jetBranchName

    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.itree = inputTree
        
        #new branch
        for shift in [ "Up", "Down" ]:
          for binIdx in [ "0", "1", "2", "3", "4", "5" ]:
          self.out.branch("%s_pt_jer%s%s" % (self.jetBranchName, binIdx, shift), "F", lenVar=self.lenVar)
          self.out.branch("%s_mass_jer%s%s" % (self.jetBranchName, binIdx, shift), "F", lenVar=self.lenVar)
          #TODO: msoftdrop jer

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        #jets  = Collection(event, self.jetBranchName)
        jets_pt  = Collection(event, self.jetBranchName+"_pt")
        #jets_pt  = Collection(event, self.jetBranchName+"_pt")
        jets_eta = Collection(event, self.jetBranchName+"_eta")
        jets_mass  = Collection(event, self.jetBranchName+"_mass")

        #jets_pt_nom = Collection(event, self.jetBranchName+"_pt_nom")
        #jets_pt_jerUp = Collection(event, self.jetBranchName+"_pt_jerUp")
        #jets_pt_jerDown = Collection(event, self.jetBranchName+"_pt_jerDown")
        #jets_mass_nom = Collection(event, self.jetBranchName+"_mass_nom")
        #jets_mass_jerUp = Collection(event, self.jetBranchName+"_mass_jerUp")
        #jets_mass_jerDown = Collection(event, self.jetBranchName+"_mass_jerDown")

        for shift in [ "Up", "Down" ]:
          for binIdx in [ "0", "1", "2", "3", "4", "5" ]:
            OutBranchs["%s_pt_jer%s%s" % (self.jetBranchName, binIdx, shift)]   = []
            OutBranchs["%s_mass_jer%s%s" % (self.jetBranchName, binIdx, shift)] = []

        for iJet in range(jets_pt._len):
          eta = jets_eta[iJet]['']
          pt  = jets_pt[iJet]['']
          jerSystBinIdx = self.GetJERSystBin(eta, pt)
          #
          for shift in [ "Up", "Down" ]:
            for binIdx in [ "0", "1", "2", "3", "4", "5" ]:
              if int(binIdx) == jerSystBinIdx:
                pt_jer   = jets_pt[iJet]['jer%s'%shift]
                mass_jer = jets_mass[iJet]['jer%s'%shift]
              else:
                pt_jer   = jets_pt[iJet]['nom']
                mass_jer = jets_mass[iJet]['nom']
              OutBranchs["%s_pt_jer%s%s" % (self.jetBranchName, binIdx, shift)].append(pt_jer)
              OutBranchs["%s_mass_jer%s%s" % (self.jetBranchName, binIdx, shift)].append(mass_jer)

        for OutBranchName, OutBranch in OutBranchs.iteritems():
          self.out.fillBranch(OutBranchName, OutBranch)

        return True


    def GetJERSystBin(self, eta, pt):
        # https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetResolution#Run2_JER_uncertainty_correlation
        # - in region |eta| < 1.93 use one pT bin: (0,Inf) 
        # - in region 1.93 < |eta| < 2.5 use one pT bin: (0,Inf) 
        # - in region 2.5 < |eta| < 3 use two pT bins: (0,50) and (50,Inf) 
        # - in region 3 < |eta| < 5 use two pT bins: (0,50) and (50,Inf)

        absEta = abs(eta)

        if absEta < 1.93:
          jerSystBinIdx = 0
        elif 1.93 < absEta < 2.50:
          jerSystBinIdx = 1
        elif 2.50 < absEta < 3.00:
          if pt < 50:
            jerSystBinIdx = 2
          else:
            jerSystBinIdx = 3
        elif 3.00 < absEta < 5.00:
          if pt < 50:
            jerSystBinIdx = 4
          else:
            jerSystBinIdx = 5
        else:
          raise ValueError("GetJERSystBin : eta range out of bound")

        return jerSystBinIdx

