import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict


class BinByBinJERMaker(Module):
    def __init__(self, jetType = "AK8PFPuppi", noGroom = False, jer_bin_list = [ 0, 1 ] ):
      if "AK4" in jetType : 
        self.jetBranchName = "Jet"
      elif "AK8" in jetType :
        self.jetBranchName = "FatJet"
        self.doGroomed = not noGroom
      else:
        raise ValueError("ERROR: Invalid jet type = '%s'!" % jetType)
      self.lenVar = "n" + self.jetBranchName

      self.jer_bin_list = jer_bin_list

    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.itree = inputTree
        
        #new branch
        for shift in [ "Up", "Down" ]:
          for binIdx in self.jer_bin_list:
            self.out.branch("%s_pt_jer%s%s" % (self.jetBranchName, binIdx, shift), "F", lenVar=self.lenVar)
            self.out.branch("%s_mass_jer%s%s" % (self.jetBranchName, binIdx, shift), "F", lenVar=self.lenVar)
            if self.doGroomed:
              self.out.branch("%s_msoftdrop_jer%s%s" % (self.jetBranchName, binIdx, shift), "F", lenVar=self.lenVar)
              self.out.branch("%s_msoftdrop_tau21DDT_jer%s%s" % (self.jetBranchName, binIdx, shift), "F", lenVar=self.lenVar)
              

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        jets  = Collection(event, self.jetBranchName)

        OutBranchs = {}
        for shift in [ "Up", "Down" ]:
          for binIdx in self.jer_bin_list:
            OutBranchs["%s_pt_jer%s%s" % (self.jetBranchName, binIdx, shift)]   = []
            OutBranchs["%s_mass_jer%s%s" % (self.jetBranchName, binIdx, shift)] = []
            if self.doGroomed:
              OutBranchs["%s_msoftdrop_jer%s%s" % (self.jetBranchName, binIdx, shift)]          = []
              OutBranchs["%s_msoftdrop_tau21DDT_jer%s%s" % (self.jetBranchName, binIdx, shift)] = []


        for jet in jets:
          eta = jet['eta']
          pt  = jet['pt']
          jerSystBinIdx = self.GetJERSystBin(eta, pt)
          #
          for shift in [ "Up", "Down" ]:
            for binIdx in self.jer_bin_list:
              if binIdx == jerSystBinIdx:
                pt_jer   = jet['pt_jer%s'%shift]
                mass_jer = jet['mass_jer%s'%shift]
                if self.doGroomed:
                  msoftdrop_jer          = jet['msoftdrop_jer%s'%shift]
                  msoftdrop_tau21DDT_jer = jet['msoftdrop_tau21DDT_jer%s'%shift]
              else:
                pt_jer   = jet['pt_nom']
                mass_jer = jet['mass_nom']
                if self.doGroomed:
                  msoftdrop_jer          = jet['msoftdrop_nom']
                  msoftdrop_tau21DDT_jer = jet['msoftdrop_tau21DDT_nom']

              OutBranchs["%s_pt_jer%s%s" % (self.jetBranchName, binIdx, shift)].append(pt_jer)
              OutBranchs["%s_mass_jer%s%s" % (self.jetBranchName, binIdx, shift)].append(mass_jer)
              if self.doGroomed:
                OutBranchs["%s_msoftdrop_jer%s%s" % (self.jetBranchName, binIdx, shift)].append(msoftdrop_jer)
                OutBranchs["%s_msoftdrop_tau21DDT_jer%s%s" % (self.jetBranchName, binIdx, shift)].append(msoftdrop_tau21DDT_jer)

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
            jerSystBinIdx = -1
            print(" [WARNING] GetJERSystBin : eta range out of bound, eta : %.2f"%eta)

        return jerSystBinIdx

