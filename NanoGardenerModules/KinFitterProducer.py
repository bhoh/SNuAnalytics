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
import math, os, tarfile, tempfile, shutil
import numpy as np
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import matchObjectCollection, matchObjectCollectionMultiple
#from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger import collectionMerger
from LatinoAnalysis.NanoGardener.framework.BranchMapping import mappedOutputTree, mappedEvent

import os.path



class KinFitterProducer(Module):
    def __init__(self, Year, branch_map=''):

        # change this part into correct path structure... 

        self._Year = Year
        cmssw_base = os.getenv('CMSSW_BASE')
        ROOT.gSystem.AddIncludePath('-I'+cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/include/')
        ROOT.gSystem.AddIncludePath('-I'+cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src/')
        self._MacroList = [
                     'TAbsFitConstraint.C',
                     'TAbsFitParticle.C',
                     'TFitConstraintEp.C',
                     'TFitConstraintM.C',
                     'TFitConstraintM2Gaus.C',
                     'TFitConstraintMGaus.C',
                     #'TFitParticleCart.C',
                     #'TFitParticleECart.C',
                     #'TFitParticleEMomDev.C',
                     #'TFitParticleEScaledMomDev.C',
                     #'TFitParticleESpher.C',
                     'TFitParticleEt.C',
                     'TFitParticleEtEtaPhi.C',
                     'TFitParticleEtPhi.C',
                     #'TFitParticleEtThetaPhi.C',
                     #'TFitParticleMCCart.C',
                     #'TFitParticleMCMomDev.C',
                     #'TFitParticleMCPInvSpher.C',
                     #'TFitParticleMCSpher.C',
                     #'TFitParticleMomDev.C',
                     'TFitParticlePt.C',
                     'TFitParticlePxPy.C',
                     'TFitParticlePz.C',
                     #'TFitParticleSpher.C',
                     'TKinFitter.C',
                     'TSCorrection.C',
                     'TKinFitterDriver.C'
                    ]

        for macro in self._MacroList:
          try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src/%s+g' % macro)
          except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src/%s++g' % macro)

        self._branch_map = branch_map
        #
        if int(Year) == 2016:
          self._DeepB_WP_M = 0.6321
        elif int(Year) == 2017:
          self._DeepB_WP_M = 0.4941
        elif int(Year) == 2018:
          self._DeepB_WP_M = 0.4184

        # read jet energy resolution (JER) and JER scale factors and uncertainties
        # (the txt files were downloaded from https://github.com/cms-jet/JRDatabase/tree/master/textFiles/ )
        # Text files are now tarred so must extract first
        #

        if int(Year) == 2016:
          jerInputFileName = "Summer16_25nsV1_DATA_PtResolution_AK4PFchs.txt"
        elif int(Year) == 2017:
          jerInputFileName = "Fall17_V3_DATA_PtResolution_AK4PFchs.txt"
        elif int(Year) == 2018:
          jerInputFileName = "Autumn18_V7_DATA_PtResolution_AK4PFchs.txt"
        #
        self.jerInputArchivePath = os.environ['CMSSW_BASE'] + "/src/PhysicsTools/NanoAODTools/data/jme/"
        self.jerTag = jerInputFileName[:jerInputFileName.find('_DATA_')+len('_DATA')]
        self.jerArchive = tarfile.open(self.jerInputArchivePath+self.jerTag+".tgz", "r:gz")
        self.jerInputFilePath = tempfile.mkdtemp()
        self.jerArchive.extractall(self.jerInputFilePath)
        self.jerInputFileName = jerInputFileName
        
        #self.jmr_vals = jmr_vals
        
        self.params_sf_and_uncertainty = ROOT.PyJetParametersWrapper()
        self.params_resolution = ROOT.PyJetParametersWrapper()
        
        # load libraries for accessing JER scale factors and uncertainties from txt files
        for library in [ "libCondFormatsJetMETObjects", "libPhysicsToolsNanoAODTools" ]:
            if library not in ROOT.gSystem.GetLibraries():
                print("Load Library '%s'" % library.replace("lib", ""))
                ROOT.gSystem.Load(library)

      
    def beginJob(self):
        # initialize JER scale factors and uncertainties
        # (cf. PhysicsTools/PatUtils/interface/SmearedJetProducerT.h )
        print("Loading jet energy resolutions (JER) from file '%s'" % os.path.join(self.jerInputFilePath, self.jerInputFileName))
        self.jer = ROOT.PyJetResolutionWrapper(os.path.join(self.jerInputFilePath, self.jerInputFileName))


    def endJob(self):
        shutil.rmtree(self.jerInputFilePath)

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
        #print("lepton")
        nLep = len(leptons)
        lepton = ROOT.TLorentzVector()
        lepton.SetPtEtaPhiM(leptons[0].pt, leptons[0].eta, leptons[0].phi, 0.)
        #print(leptons[0].pt,"   ",leptons[0].eta,"    ",leptons[0].phi)
        
        #
        Jet   = Collection(event, "CleanJet")
        #auxiliary jet collection to access the mass
        OrigJet   = Collection(event, "Jet")

        nJet = len(Jet)
        if nJet < 4:
          return False

        jets            = ROOT.std.vector(ROOT.TLorentzVector)(0)
        #jetPtResolution = ROOT.std.vector(float)(0)
        btag_vector     = ROOT.std.vector(bool)(0)

        nbtags = 0
        njets  = 0
        #print("jets")
        for jet in Jet :
          if jet.pt <= 30 or abs(jet.eta)>=2.4:
            continue
          njets += 1
          tmp_jet = ROOT.TLorentzVector()
          tmp_jet.SetPtEtaPhiM(jet.pt, jet.eta, jet.phi, OrigJet[jet.jetIdx].mass)
          jets.push_back(tmp_jet)
          jetPtResolution_ = self.getJetPtResolution(tmp_jet, event.fixedGridRhoFastjetAll)
          print("jetPtResolution :", jetPtResolution_)
          #jetPtResolution.push_back(self.)
          #print(jet.pt,"   ",jet.eta,"    ",jet.phi)
          if OrigJet[jet.jetIdx].btagDeepB > self._DeepB_WP_M:
            btag_vector.push_back(True)
            nbtags += 1
          else:
            btag_vector.push_back(False)

        if njets < 4 or nbtags < 2:
          return False
        
        MET = ROOT.TLorentzVector()
        MET.SetPtEtaPhiM(event.MET_pt, 0., event.MET_phi, 0.)
        #print("MET")
        #print(event.PuppiMET_pt,"   ",event.PuppiMET_phi)

        METShiftX =event.MET_MetUnclustEnUpDeltaX
        METShiftY =event.MET_MetUnclustEnUpDeltaY
        
        fitter = ROOT.TKinFitterDriver(int(self._Year))
        fitter.SetAllObjects(jets, btag_vector, lepton, MET)
        fitter.SetMETShift(METShiftX, METShiftY)
        fitter.FindBestChi2Fit()

        variables = {}
        variables['initial_dijet_M']   = fitter.GetBestInitialDijetMass()
        variables['corrected_dijet_M'] = fitter.GetBestCorrectedDijetMass()
        variables['fitted_dijet_M']    = fitter.GetBestFittedDijetMass()
        variables['best_chi2']         = fitter.GetBestChi2()
        variables['fitter_status']     = fitter.GetBestStatus()

        for nameBranches in self.newbranches :
          self.out.fillBranch(nameBranches  ,  variables[nameBranches]);

        return True


    def getJetPtResolution(self, jetIn, rho):
        if hasattr( jetIn, "p4"):
          jet = jetIn.p4()
        else:
          jet = jetIn

        if not (jet.Perp() > 0.):
            print("WARNING: jet pT = %1.1f !!" % jet.Perp())
            return ( jet.Perp(), jet.Perp(), jet.Perp() )

        self.params_resolution.setJetPt(jet.Perp())
        self.params_resolution.setJetEta(jet.Eta())
        self.params_resolution.setRho(rho)
        jet_pt_resolution = self.jer.getResolution(self.params_resolution)
        return jet_pt_resolution
