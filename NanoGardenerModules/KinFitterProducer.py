#
#
#     |  |  |    |  / _)          
#     |  |  |    ' /   |  __ \    
#     | ___ __|  . \   |  |   |   
#    _|    _|   _|\_\ _| _|  _|   
#                                                                                     
#
#



import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger import collectionMerger
from LatinoAnalysis.NanoGardener.framework.BranchMapping import mappedOutputTree, mappedEvent


import os.path



class KinFitterProducer(Module):
    def __init__(self, branch_map=''):

        # change this part into correct path structure... 
        cmssw_base = os.getenv('CMSSW_BASE')
        ROOT.gSystem.AddIncludePath('-I'+cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/include/')
        ROOT.gSystem.AddIncludePath('-I'+cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src/')
        MacroList = ['TFitConstraintEp.C',
                     'TFitConstraintM.C',
                     'TFitConstraintM2Gaus.C',
                     'TFitConstraintMGaus.C',
                     'TFitParticleCart.C',
                     'TFitParticleECart.C',
                     'TFitParticleEMomDev.C',
                     'TFitParticleEScaledMomDev.C',
                     'TFitParticleESpher.C',
                     'TFitParticleEt.C',
                     'TFitParticleEtEtaPhi.C',
                     'TFitParticleEtPhi.C',
                     'TFitParticleEtThetaPhi.C',
                     'TFitParticleMCCart.C',
                     'TFitParticleMCMomDev.C',
                     'TFitParticleMCPInvSpher.C',
                     'TFitParticleMCSpher.C',
                     'TFitParticleMomDev.C',
                     'TFitParticlePt.C',
                     'TFitParticlePxPy.C',
                     'TFitParticlePz.C',
                     'TFitParticleSpher.C',
                    ]
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src/TAbsFitConstraint.C+g')
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src/TAbsFitParticle.C+g')
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src/TKinFitter.C+g')
            for macro in MacroList:
              ROOT.gROOT.LoadMacro(cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src/%s+g' % macro)
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src/TSCorrection+g')
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src/TKinFitterDriver+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src/TAbsFitConstraint.C++g')
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src/TAbsFitParticle.C++g')
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src/TKinFitter.C++g')
            for macro in MacroList:
              ROOT.gROOT.LoadMacro(cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src/%s++g' % macro)
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src/TSCorrection++g')
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src/TKinFitterDriver++g')

        self._branch_map = branch_map  
      
    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = mappedOutputTree(wrappedOutputTree, mapname=self._branch_map)
        self.newbranches = [
            'initial_dijet_M',
            'corrected_dijet_M',
            'fitted_dijet_M',
            'best_chi2',
            'fitter_status',
          ]
        
        for nameBranches in self.newbranches :
          self.out.branch(nameBranches  ,  "F");

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        event = mappedEvent(event, mapname=self._branch_map)
        #muons = Collection(event, "Muon")
        #electrons = Collection(event, "Electron")

        # order in pt the collection merging muons and electrons
        # lepMerger must be already called
        leptons = Collection(event, "Lepton")

        #leptons = electrons
        nLep = len(leptons)
        
        
        lep_pt      = ROOT.std.vector(float)(0)
        lep_eta     = ROOT.std.vector(float)(0)
        lep_phi     = ROOT.std.vector(float)(0)
        
        for lep in leptons :
          lep_pt. push_back(lep.pt)
          lep_eta.push_back(lep.eta)
          lep_phi.push_back(lep.phi)
          
        Jet   = Collection(event, "CleanJet")
        #auxiliary jet collection to access the mass
        OrigJet   = Collection(event, "Jet")

        nJet = len(Jet)

        jet_pt     = ROOT.std.vector(float)(0)
        jet_eta    = ROOT.std.vector(float)(0)
        jet_phi    = ROOT.std.vector(float)(0)
        jet_mass   = ROOT.std.vector(float)(0)

        for jet in Jet :
          jet_pt. push_back(jet.pt)
          jet_eta.push_back(jet.eta)
          jet_phi.push_back(jet.phi)
          jet_mass.push_back(OrigJet[jet.jetIdx].mass)

        MET_phi   = event.PuppiMET_phi
        MET_pt    = event.PuppiMET_pt
        
            
        #for nameBranches in self.newbranches :
        #  self.out.fillBranch(nameBranches  ,  getattr(ZWW, nameBranches)());


        return True






