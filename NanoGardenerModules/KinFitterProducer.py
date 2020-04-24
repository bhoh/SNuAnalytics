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
        self.newbranches_F = [
            'initial_dijet_M',
            'initial_dijet_M_high',
            'corrected_dijet_M',
            'corrected_dijet_M_high',
            'fitted_dijet_M',
            'fitted_dijet_M_high',
            'hadronic_top_M',
            'hadronic_top_pt',
            'leptonic_top_M',
            'leptonic_W_M',
            'best_chi2',
            'fitter_status',
            'hadronic_top_b_jet_pull',
            'w_ch_up_type_jet_pull',
            'w_ch_down_type_jet_pull',
          ]
        self.newbranches_I = [
            'nbtagsCleanJet',
            'down_type_jet_b_tagged',
            'hadronic_top_b_jet_idx',
            'leptonic_top_b_jet_idx',
            'w_ch_up_type_jet_idx',
            'w_ch_down_type_jet_idx'
          ]
        for nameBranches in self.newbranches_F :
          self.out.branch(nameBranches  ,  "F");
        for nameBranches in self.newbranches_I:
          self.out.branch(nameBranches ,  "I");

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

        jets            = ROOT.std.vector(ROOT.TLorentzVector)(0)
        jetPtResolution = ROOT.std.vector(float)(0)
        btag_csv_vector     = ROOT.std.vector(ROOT.Double)(0)

        nbtags = 0
        njets  = 0
        #print("jets")
        for jet in Jet :
          if OrigJet[jet.jetIdx].pt_nom <= 30 or abs(jet.eta)>=2.5:
            continue
          njets += 1
          tmp_jet = ROOT.TLorentzVector()
          tmp_jet.SetPtEtaPhiM(OrigJet[jet.jetIdx].pt_nom, jet.eta, jet.phi, OrigJet[jet.jetIdx].mass)
          jets.push_back(tmp_jet)
          tmp_jet.SetPtEtaPhiM(jet.pt, jet.eta, jet.phi, OrigJet[jet.jetIdx].mass)
          jetPtResolution_ = self.getJetPtResolution(tmp_jet, event.fixedGridRhoFastjetAll)
          jetPtResolution.push_back(jetPtResolution_)
          btag_csv_vector.push_back(OrigJet[jet.jetIdx].btagDeepB)
          if OrigJet[jet.jetIdx].btagDeepB > self._DeepB_WP_M:
            nbtags += 1
        
        MET = ROOT.TLorentzVector()
        MET.SetPtEtaPhiM(event.PuppiMET_pt, 0., event.PuppiMET_phi, 0.)
        #print("MET")
        #print(event.PuppiMET_pt,"   ",event.PuppiMET_phi)

        METShiftX =event.MET_MetUnclustEnUpDeltaX
        METShiftY =event.MET_MetUnclustEnUpDeltaY
        
        fitter = ROOT.TKinFitterDriver(int(self._Year))
        fitter.SetAllObjects(jets, btag_csv_vector, self._DeepB_WP_M, lepton, MET)
        fitter.SetJetPtResolution(jetPtResolution)
        fitter.SetMETShift(METShiftX, METShiftY)
        #fitter.FindBestChi2Fit()
        fitter.FindMaxPtHadTopFit(False,True,True)

        variables = {}
        variables['initial_dijet_M']         = fitter.GetBestInitialDijetMass()
        variables['initial_dijet_M_high']    = fitter.GetBestInitialDijetMass_high()
        variables['corrected_dijet_M']       = fitter.GetBestCorrectedDijetMass()
        variables['corrected_dijet_M_high']  = fitter.GetBestCorrectedDijetMass_high()
        variables['fitted_dijet_M']          = fitter.GetBestFittedDijetMass()
        variables['fitted_dijet_M_high']     = fitter.GetBestFittedDijetMass_high()
        variables['best_chi2']               = fitter.GetBestChi2()
        variables['fitter_status']           = fitter.GetBestStatus()
        variables['down_type_jet_b_tagged']  = fitter.GetBestDownTypeJetBTagged()
        variables['hadronic_top_b_jet_idx']  = fitter.GetBestHadronicTopBJetIdx()
        variables['leptonic_top_b_jet_idx']  = fitter.GetBestLeptonicTopBJetIdx()
        variables['w_ch_up_type_jet_idx']    = fitter.GetBestHadronicWCHUpTypeJetIdx()
        variables['w_ch_down_type_jet_idx']  = fitter.GetBestHadronicWCHDownTypeJetIdx()
         
        variables['hadronic_top_b_jet_pull'] = fitter.GetBestHadronicTopBJetPull()
        variables['w_ch_up_type_jet_pull']   = fitter.GetBestHadronicWCHUptypeJetIdxPull()
        variables['w_ch_down_type_jet_pull'] = fitter.GetBestHadronicWCHDowntypeJetIdxPull()

        variables['hadronic_top_M']          = fitter.GetBestHadronicTopMass()
        variables['hadronic_top_pt']          = fitter.GetBestHadronicTopPt()
        variables['leptonic_top_M']          = fitter.GetBestLeptonicTopMass()
        variables['leptonic_W_M']            = fitter.GetBestLeptonicWMass()

        variables["nbtagsCleanJet"] = nbtags

        for nameBranches in self.newbranches_F:
          self.out.fillBranch(nameBranches  ,  variables[nameBranches]);
        for nameBranches in self.newbranches_I:
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
