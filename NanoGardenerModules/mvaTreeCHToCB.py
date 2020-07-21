import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

from ROOT import TLorentzVector
from itertools import combinations
from operator import itemgetter, attrgetter
from math import cosh, sqrt


## functions 
def nearest_top_mass_pair(vectors):
    ''' Returns the pair of vectors with invariant mass nearest to 
    the given mass '''
    l = []
    for i ,j, k  in combinations(range(len(vectors)),3):
      l.append(([i,j,k], abs(172.5 - (vectors[i]+vectors[j]+vectors[k]).M() )))
    l = sorted(l, key=itemgetter(1))
    return l[0][0]
##


##
# this module is to add variables for MVA training to skim tree.
##
class mvaTreeCHToCB(Module):
    def __init__(self):
        self.sortkey = lambda x: x.pt
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        #self.out.branch("",             "I")
        self.out.branch("csv_jet0", "F")
        self.out.branch("csv_jet1", "F")
        self.out.branch("csv_jet2", "F")

        self.out.branch("jet_vector0", "F")
        self.out.branch("jet_vector1", "F")
        self.out.branch("jet_vector2", "F")

        self.out.branch("dijet_deltaR0", "F")
        self.out.branch("dijet_deltaR1", "F")

        self.out.branch("hadronic_top_mass", "F")


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        # select jets
        self.Jet_coll       = Collection(event, 'CleanJet')

        #XXX set pt eta cut by years
        good_jets, good_jets_idx = self.get_jets_vectors(etacut, ptcut)

        # return if not more than 4 jets
        if len(good_jets) < 4:
          return True

        # select jet pair, find nearest top mass jet pair
        nearest_top_mass_pair_jetIdx = nearest_top_mass_pair(good_jets)

        # sort this jet pair in leading csv ordering
        nearest_top_mass_pair_jetIdx.sort(key=lambda idx: self.Jet_coll[good_jets_idx[idx]].btagDeepB, reverse=True)

        # make variables
        if not len(nearest_top_mass_pair_jetIdx) == 3:
          raise RuntimeError("len(nearest_top_mass_pair_jetIdx) is not 3")
        # nearest_top_mass_pair_jetIdx contains index of good_jets
        # good_jets_idx[<index of good_jets>] is index of self.Jet_coll corresponding to index of good_jets
        idx0, idx1, idx2 = [ good_jets_idx[idx] for idx in nearest_top_mass_pair_jetIdx ]

        csv_jet0 = self.Jet_coll[idx0].btagDeepB #leading csv
        csv_jet1 = self.Jet_coll[idx1].btagDeepB #2nd leading csv
        csv_jet2 = self.Jet_coll[idx2].btagDeepB #smallest csv

        jet_vector0 = good_jets[nearest_top_mass_pair_jetIdx[0]]
        jet_vector1 = good_jets[nearest_top_mass_pair_jetIdx[1]]
        jet_vector2 = good_jets[nearest_top_mass_pair_jetIdx[2]]

        dijet_deltaR0     = jet_vector2.DeltaR(jet_vector0)
        dijet_deltaR1     = jet_vector2.DeltaR(jet_vector1)
        hadronic_top_mass = ( jet_vector0 + jet_vector1 + jet_vector2 ).M()

        self.out.fillBranch("csv_jet0_mvaCHToCB", csv_jet0)
        self.out.fillBranch("csv_jet1_mvaCHToCB", csv_jet1)
        self.out.fillBranch("csv_jet2_mvaCHToCB", csv_jet2)

        self.out.fillBranch("jet_vector0_mvaCHToCB", jet_vector0)
        self.out.fillBranch("jet_vector1_mvaCHToCB", jet_vector1)
        self.out.fillBranch("jet_vector2_mvaCHToCB", jet_vector2)

        self.out.fillBranch("dijet_deltaR0_mvaCHToCB", dijet_deltaR0)
        self.out.fillBranch("dijet_deltaR1_mvaCHToCB", dijet_deltaR1)
        self.out.fillBranch("hadronic_top_mass_mvaCHToCB", hadronic_top_mass)

        return True


    def get_jets_vectors(self, etacut, ptcut):
        '''
        Returns a list of 4-momenta for jets
                                                                                                                    
        Inserted here an eta interval and pt range cut to avoid using the jets in a specified region for 
        tagging. 
        '''
        jets = []
        coll_ids = []
        for ijnf in range(len(self.Jet_coll)):
          jetindex = self.Jet_coll[ijnf].jetIdx
          # index in the original Jet collection
          rawjetid = self.Jet_coll[jetindex].jetIdx
          pt, eta, phi, mass = self.Jet_coll[jetindex].pt, \
                      self.Jet_coll[jetindex].eta,\
                      self.Jet_coll[jetindex].phi, \
                      self.rawJet_coll[rawjetid].mass
                                                                                                                  
          passetacut = True
          if abs(eta) >= etacut or pt <= ptcut: 
            passetacut = False
            if self.debug: 
              print "Jet index: ", jetindex, " CUT > pt:", pt ," eta:", eta, " phi:", phi, " mass:", mass
          if not passetacut : continue
          
          p = pt * cosh(eta)
          en = sqrt(p**2 + mass**2)
          vec = TLorentzVector()
          vec.SetPtEtaPhiE(pt, eta, phi, en)
          # check if different from the previous one
          if self.debug:
              print "Jet index: ", jetindex, "> pt:", pt ," eta:", eta, " phi:", phi, " mass:", mass
          jets.append(vec)
          coll_ids.append(jetindex)
        return jets, coll_ids
