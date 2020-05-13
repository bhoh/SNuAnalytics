import ROOT
import math, os, tarfile, tempfile, shutil
import numpy as np
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import matchObjectCollection, matchObjectCollectionMultiple
#from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger import collectionMerger
from LatinoAnalysis.NanoGardener.framework.BranchMapping import mappedOutputTree, mappedEvent

from LatinoAnalysis.NanoGardener.modules.KinFitterProducer import KinFitterProducer

import os.path

class GenKinFitterProducer(KinFitterProducer):

    def __init__(self, Year, branch_map=''):
        super(GenKinFitterProducer,self).__init__(Year,branch_map)


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
          ]
        for nameBranches in self.newbranches_F :
          self.out.branch(nameBranches  ,  "F");
        for nameBranches in self.newbranches_I:
          self.out.branch(nameBranches ,  "I");


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

        nbtags = 0
        njets  = 0
        #print("jets")

        had_top_b_matched_jet_idx         =  event.top_b_matched_jet_idx if event.gen_had_top_sign>0 else event.anti_top_b_matched_jet_idx
        had_top_up_type_matched_jet_idx   = event.had_top_up_type_matched_jet_idx  
        had_top_down_type_matched_jet_idx = event.had_top_down_type_matched_jet_idx

        #check if indexs are negative
        negative_idx = False
        if had_top_b_matched_jet_idx<0 or\
           had_top_up_type_matched_jet_idx<0 or\
           had_top_down_type_matched_jet_idx<0:
          negative_idx = True

        fitter = ROOT.TKinFitterDriver(int(self._Year))
        # do not run fitter if there're more than one negative index.
        if negative_idx:
          pass
        else:
          # make a tlorentzvector for matched jet idx
          had_top_b_matched_jet             = self.getJetVector(OrigJet, had_top_b_matched_jet_idx)
          had_top_up_type_matched_jet   = self.getJetVector(OrigJet, had_top_up_type_matched_jet_idx)
          had_top_down_type_matched_jet = self.getJetVector(OrigJet, had_top_down_type_matched_jet_idx)

          # jet pt resolution for matched jet idx
          fixedGridRhoFastjetAll = event.fixedGridRhoFastjetAll
          had_top_b_matched_jet_resolution             = self.getJetPtResolution(had_top_b_matched_jet, fixedGridRhoFastjetAll)
          had_top_up_type_matched_jet_resolution   = self.getJetPtResolution(had_top_up_type_matched_jet,  fixedGridRhoFastjetAll)
          had_top_down_type_matched_jet_resolution = self.getJetPtResolution(had_top_down_type_matched_jet,fixedGridRhoFastjetAll)

       
          MET = ROOT.TLorentzVector()
          MET.SetPtEtaPhiM(event.PuppiMET_pt, 0., event.PuppiMET_phi, 0.)

          fitter.SetHadronicTopBJets(had_top_b_matched_jet,      had_top_b_matched_jet_resolution)
          fitter.SetWCHUpTypeJets(had_top_down_type_matched_jet, had_top_up_type_matched_jet_resolution)
          fitter.SetWCHDownTypeJets(had_top_up_type_matched_jet, had_top_down_type_matched_jet_resolution)
          fitter.SetLepton(lepton)
          fitter.SetNeutrinoSmallerPz(MET)
          fitter.FitCurrentPermutation()

        variables = {}
        variables['initial_dijet_M']         = fitter.GetBestInitialDijetMass()
        variables['initial_dijet_M_high']    = fitter.GetBestInitialDijetMass_high()
        variables['corrected_dijet_M']       = fitter.GetBestCorrectedDijetMass()
        variables['corrected_dijet_M_high']  = fitter.GetBestCorrectedDijetMass_high()
        variables['fitted_dijet_M']          = fitter.GetBestFittedDijetMass()
        variables['fitted_dijet_M_high']     = fitter.GetBestFittedDijetMass_high()
        variables['best_chi2']               = fitter.GetBestChi2()
        variables['fitter_status']           = fitter.GetBestStatus()
         
        variables['hadronic_top_b_jet_pull'] = fitter.GetBestHadronicTopBJetPull()
        variables['w_ch_up_type_jet_pull']   = fitter.GetBestHadronicWCHUptypeJetIdxPull()
        variables['w_ch_down_type_jet_pull'] = fitter.GetBestHadronicWCHDowntypeJetIdxPull()

        variables['hadronic_top_M']          = fitter.GetBestHadronicTopMass()
        variables['hadronic_top_pt']          = fitter.GetBestHadronicTopPt()
        variables['leptonic_top_M']          = fitter.GetBestLeptonicTopMass()
        variables['leptonic_W_M']            = fitter.GetBestLeptonicWMass()

        for nameBranches in self.newbranches_F:
          self.out.fillBranch(nameBranches  ,  variables[nameBranches]);
        for nameBranches in self.newbranches_I:
          self.out.fillBranch(nameBranches  ,  variables[nameBranches]);

        return True

   
    def getJetVector(self,Jets,idx):
        jet_vector = ROOT.TLorentzVector()
        negative_idx = False
        if idx<0:
          negative_idx = True
        if negative_idx:
          jet_vector.SetPtEtaPhiM(0., 0., 0., 0.)
        else:
          jet = Jets[idx]
          jet_vector.SetPtEtaPhiM(jet.pt_nom, jet.eta, jet.phi, jet.mass)
        return jet_vector
