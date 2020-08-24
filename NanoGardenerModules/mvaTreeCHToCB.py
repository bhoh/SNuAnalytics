import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

from ROOT import TLorentzVector
from itertools import combinations
from operator import itemgetter, attrgetter
from math import cosh, sqrt











##


##
# this module is to add variables for MVA training to skim tree.
##
class mvaTreeCHToCB(Module):
    def __init__(self, Year):
        self.Year = Year
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("nbtags_had_top_mvaCHToCB",             "I")
        self.out.branch("nbtags_event_mvaCHToCB",             "I")

        self.out.branch("csv_jet0_mvaCHToCB", "F")
        self.out.branch("csv_jet1_mvaCHToCB", "F")
        self.out.branch("csv_jet2_mvaCHToCB", "F")

        #self.out.branch("jet_vector0_mvaCHToCB", "F")
        #self.out.branch("jet_vector1_mvaCHToCB", "F")
        #self.out.branch("jet_vector2_mvaCHToCB", "F")

        self.out.branch("dijet_deltaR0_mvaCHToCB", "F")
        self.out.branch("dijet_deltaR1_mvaCHToCB", "F")
        self.out.branch("Hplus_b_deltaR0_mvaCHToCB", "F")
        self.out.branch("Hplus_b_deltaR1_mvaCHToCB", "F")
        self.out.branch("bb_deltaR", "F")

        self.out.branch("dijet_ptD0_mvaCHToCB", "F")
        self.out.branch("dijet_ptD1_mvaCHToCB", "F")

        self.out.branch("had_top_pt_scalar_sum", "F")
        self.out.branch("mbb", "F")
        self.out.branch("mcb0", "F")
        self.out.branch("mcb1", "F")
        self.out.branch("hadronic_top_mass_mvaCHToCB", "F")


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        # select jets
        self.Jet_coll       = Collection(event, 'CleanJet')
        self.rawJet_coll    = Collection(event, 'Jet')

        #XXX set pt eta cut by years
        ptcut = 30.
        if int(self.Year) == 2016:
          absetacut = 2.4
          self.csvcut    = 0.6321
        elif int(self.Year) == 2017:
          absetacut = 2.5
          self.csvcut    = 0.4941
        else:
          absetacut = 2.5
          self.csvcut    = 0.4184

        good_jets, good_jets_idx = self.get_jets_vectors(absetacut, ptcut)

        # return if not more than 4 jets
        if len(good_jets) < 4:
          return True

        self.nbtags_event = sum([ csv > self.csvcut for csv in [ self.rawJet_coll[idx].btagDeepB for idx in good_jets_idx ]])

        if self.nbtags_event < 2:
          return True


        #
        # 1) select jet from top
        #    - to use before run kinFitter module
        #      -> select nearest top mass pair and maximum top pt pair
        #    - to use after run kinFitter module
        #      -> retrive variable from skimed tree to find top candidate jet pair
        #
        #

        #
        #
        #
        #
        #
        #
        #

        # if proper variables(index of jet candidate, b-tagging status) exist in skimed Tree,
        #use that variables for making variables
        if self.exist_variables_in_skimTree(event): # is there any smater way?
          down_type_jet_b_tagged_nom = event.down_type_jet_b_tagged_nom
          hadronic_top_b_jet_idx_nom = event.hadronic_top_b_jet_idx_nom
          leptonic_top_b_jet_idx_nom = event.leptonic_top_b_jet_idx_nom
          w_ch_up_type_jet_idx_nom   = event.w_ch_up_type_jet_idx_nom
          w_ch_down_type_jet_idx_nom = event.w_ch_down_type_jet_idx_nom

          hadronic_top_b_jet_pull_nom = event.hadronic_top_b_jet_pull_nom
          w_ch_up_type_jet_pull_nom   = event.w_ch_up_type_jet_pull_nom  
          w_ch_down_type_jet_pull_nom = event.w_ch_down_type_jet_pull_nom
          
          if not (hadronic_top_b_jet_idx_nom >= 0 and\
                  hadronic_top_b_jet_idx_nom >= 0 and\
                  w_ch_up_type_jet_idx_nom   >= 0 and\
                  w_ch_down_type_jet_idx_nom >= 0
                 ):
            return True

          had_top_jets_idx = [
                            hadronic_top_b_jet_idx_nom,
                            w_ch_up_type_jet_idx_nom,  
                            w_ch_down_type_jet_idx_nom,
                          ]

          # find index of element in good_jets_idx
          try:
            good_jets_idx_mask = [
                                   good_jets_idx.index(idx) for idx in had_top_jets_idx
                                 ]
          except IndexError:
            raise RuntimeWarning('index is not found in good_jets_idx')
            return True

          
          # copy good_jets using good_jets_idx_mask
          good_jets_         = [ 
                                 good_jets[idx] for idx in good_jets_idx_mask
                               ]
          # copy also good_jets_idx
          good_jets_idx_     = [
                                 good_jets_idx[idx] for idx in good_jets_idx_mask
                               ]

          # override good_jets, good_jets_idx.
          good_jets, good_jets_idx = good_jets_, good_jets_idx_
          
          
          nearest_top_mass_pair_jetIdx = [0,1,2] # good_jets contain only 3 had top candidate
          self.nbtags_had_top = sum([ csv > self.csvcut for csv in [ self.rawJet_coll[idx].btagDeepB for idx in good_jets_idx]])



          pull_cut = True
          if pull_cut:
            if not (abs(hadronic_top_b_jet_pull_nom)<2 and\
                    abs(w_ch_up_type_jet_pull_nom  )<2 and\
                    abs(w_ch_down_type_jet_pull_nom)<2\
                   ):
              return True


        # otherwise, find jet pairs
        else:
          # select jet pair, find nearest top mass jet pair
          nearest_top_mass_pair_jetIdx = self.nearest_top_mass_pair(good_jets, good_jets_idx)
          maximum_top_pt_pair_jetIdx = self.maximum_top_pt_pair(good_jets, good_jets_idx)

          if not (nearest_top_mass_pair_jetIdx == maximum_top_pt_pair_jetIdx):
            return True

        # sort this jet pair in leading csv ordering
        nearest_top_mass_pair_jetIdx.sort(key=lambda idx: self.rawJet_coll[good_jets_idx[idx]].btagDeepB, reverse=True)

        #
        #
        #
        #
        #
        #
        #

        # make variables
        if not len(nearest_top_mass_pair_jetIdx) == 3:
          raise RuntimeError("len(nearest_top_mass_pair_jetIdx) is not 3")
        # nearest_top_mass_pair_jetIdx contains index of good_jets
        # good_jets_idx[<index of good_jets>] is index of self.Jet_coll corresponding to index of good_jets
        idx0, idx1, idx2 = [ good_jets_idx[idx] for idx in nearest_top_mass_pair_jetIdx ]

        csv_jet0 = self.rawJet_coll[idx0].btagDeepB #leading csv
        csv_jet1 = self.rawJet_coll[idx1].btagDeepB #2nd leading csv
        csv_jet2 = self.rawJet_coll[idx2].btagDeepB #smallest csv

        #
        nbtags_had_top = self.nbtags_had_top
        #
        #

        jet_vector0 = good_jets[nearest_top_mass_pair_jetIdx[0]]
        jet_vector1 = good_jets[nearest_top_mass_pair_jetIdx[1]]
        jet_vector2 = good_jets[nearest_top_mass_pair_jetIdx[2]]

        jet_pt0 = jet_vector0.Pt()
        jet_pt1 = jet_vector1.Pt()
        jet_pt2 = jet_vector2.Pt()

        # jet_vector2 is 3rd leading csv jet
        # consider this jet as a jet comming from c
        # dijet_deltaR0/1 variables are deltaR between c jet and b jet comming from H+
        # 0,1 are labeled in pT order
        dijet_deltaR0     = jet_vector2.DeltaR(jet_vector0 if jet_pt0 >= jet_pt1 else jet_vector1)
        dijet_deltaR1     = jet_vector2.DeltaR(jet_vector1 if jet_pt0 >= jet_pt1 else jet_vector0 )
        Hplus_b_deltaR0   = jet_vector0.DeltaR(jet_vector1+jet_vector2) if jet_pt0 < jet_pt1 else jet_vector1.DeltaR(jet_vector0+jet_vector2)
        Hplus_b_deltaR1   = jet_vector1.DeltaR(jet_vector0+jet_vector2) if jet_pt0 < jet_pt1 else jet_vector0.DeltaR(jet_vector1+jet_vector2)

        bb_deltaR         = jet_vector0.DeltaR(jet_vector1)
        dijet_ptD0        = dijet_deltaR0
        dijet_ptD0        *= (jet_vector2+jet_vector0).Pt() if jet_pt0 >= jet_pt1 else (jet_vector2+jet_vector1).Pt()
        dijet_ptD1        = dijet_deltaR1
        dijet_ptD1        *= (jet_vector2+jet_vector1).Pt() if jet_pt0 >= jet_pt1 else (jet_vector2+jet_vector0).Pt()


        had_top_pt_scalar_sum = jet_pt0 + jet_pt1 + jet_pt2
        mbb  = ( jet_vector0 + jet_vector1 ).M()
        mcb0 = ( jet_vector2 + jet_vector1 ).M() if jet_pt0 < jet_pt1 else ( jet_vector2 + jet_vector0 ).M()
        mcb1 = ( jet_vector2 + jet_vector0 ).M() if jet_pt0 < jet_pt1 else ( jet_vector2 + jet_vector1 ).M()
        hadronic_top_mass = ( jet_vector0 + jet_vector1 + jet_vector2 ).M()

        self.out.fillBranch("nbtags_had_top_mvaCHToCB", nbtags_had_top)
        self.out.fillBranch("nbtags_event_mvaCHToCB", self.nbtags_event)

        self.out.fillBranch("csv_jet0_mvaCHToCB", csv_jet0)
        self.out.fillBranch("csv_jet1_mvaCHToCB", csv_jet1)
        self.out.fillBranch("csv_jet2_mvaCHToCB", csv_jet2)

        #self.out.fillBranch("jet_vector0_mvaCHToCB", jet_vector0)
        #self.out.fillBranch("jet_vector1_mvaCHToCB", jet_vector1)
        #self.out.fillBranch("jet_vector2_mvaCHToCB", jet_vector2)

        self.out.fillBranch("dijet_deltaR0_mvaCHToCB", dijet_deltaR0)
        self.out.fillBranch("dijet_deltaR1_mvaCHToCB", dijet_deltaR1)
        self.out.fillBranch("Hplus_b_deltaR0_mvaCHToCB", Hplus_b_deltaR0)
        self.out.fillBranch("Hplus_b_deltaR1_mvaCHToCB", Hplus_b_deltaR1)
        self.out.fillBranch("bb_deltaR", bb_deltaR)
        self.out.fillBranch("dijet_ptD0_mvaCHToCB", dijet_ptD0)
        self.out.fillBranch("dijet_ptD1_mvaCHToCB", dijet_ptD1)

        self.out.fillBranch("had_top_pt_scalar_sum", had_top_pt_scalar_sum)
        self.out.fillBranch("mbb", mbb)
        self.out.fillBranch("mcb0", mcb0)
        self.out.fillBranch("mcb1", mcb1)
        self.out.fillBranch("hadronic_top_mass_mvaCHToCB", hadronic_top_mass)

        return True


    def get_jets_vectors(self, absetacut, ptcut):
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
          pt, eta, phi, mass = self.Jet_coll[ijnf].pt, \
                      self.Jet_coll[ijnf].eta,\
                      self.Jet_coll[ijnf].phi, \
                      self.rawJet_coll[jetindex].mass
                                                                                                                  
          passabsetacut = True
          if abs(eta) >= absetacut or pt <= ptcut: 
            passabsetacut = False
            #if self.debug: 
            #  print "Jet index: ", jetindex, " CUT > pt:", pt ," eta:", eta, " phi:", phi, " mass:", mass
          if not passabsetacut : continue
          
          p = pt * cosh(eta)
          en = sqrt(p**2 + mass**2)
          vec = TLorentzVector()
          vec.SetPtEtaPhiE(pt, eta, phi, en)
          # check if different from the previous one
          #if self.debug:
          #    print "Jet index: ", jetindex, "> pt:", pt ," eta:", eta, " phi:", phi, " mass:", mass
          jets.append(vec)
          coll_ids.append(jetindex)
        return jets, coll_ids


    def exist_variables_in_skimTree(self, event):
        # check if variables exist in skimed tree
        # which kinFitTTSemiLep module produce
        # 
        # 'down_type_jet_b_tagged_nom'
        # 'hadronic_top_b_jet_idx_nom'
        # 'leptonic_top_b_jet_idx_nom'
        # 'w_ch_up_type_jet_idx_nom'
        # 'w_ch_down_type_jet_idx_nom'
        #
        # these variables return index of Jet assigned as top candidate
        #
        #
        return hasattr(event,'down_type_jet_b_tagged_nom') and\
               hasattr(event,'hadronic_top_b_jet_idx_nom') and\
               hasattr(event,'leptonic_top_b_jet_idx_nom') and\
               hasattr(event,'w_ch_up_type_jet_idx_nom') and\
               hasattr(event,'w_ch_down_type_jet_idx_nom') and\
               hasattr(event,'hadronic_top_b_jet_pull_nom') and\
               hasattr(event,'w_ch_up_type_jet_pull_nom') and\
               hasattr(event,'w_ch_down_type_jet_pull_nom')


    def nearest_top_mass_pair(self, vectors, idxs):
        ''' Returns the pair of vectors with invariant mass nearest to 
        the given mass '''
        l = []
        for i ,j, k  in combinations(range(len(vectors)),3):
          nbtags_had_top = sum([ csv > self.csvcut for csv in [ self.rawJet_coll[idxs[i]].btagDeepB, self.rawJet_coll[idxs[j]].btagDeepB, self.rawJet_coll[idxs[k]].btagDeepB ]])
          # if there's no btagged jets in hadronic top, assign large number
          # in the 2 btagged event, 1 b tagged jet is allowed in had top
          # in the >=3 btagged event, more than 2 b tagged jet are allowed in had top
          l.append(([i,j,k], abs(172.5 - (vectors[i]+vectors[j]+vectors[k]).M() ) if (self.nbtags_event==2 and nbtags_had_top == 1) or (self.nbtags_event>=3 and nbtags_had_top >= 2) else 9999999999, nbtags_had_top ))
        l = sorted(l, key=itemgetter(1))
        self.nbtags_had_top = l[0][2] #store number of b-tagged jet in hadronic top
        return l[0][0]

    def maximum_top_pt_pair(self, vectors, idxs):
        ''' Returns the pair of vectors with invariant mass nearest to 
        the given mass '''
        l = []
        for i ,j, k  in combinations(range(len(vectors)),3):
          nbtags_had_top = sum([ csv > self.csvcut for csv in [ self.rawJet_coll[idxs[i]].btagDeepB, self.rawJet_coll[idxs[j]].btagDeepB, self.rawJet_coll[idxs[k]].btagDeepB ]])
          # if there's no btagged jets in hadronic top, assign large number
          # in the 2 btagged event, 1 b tagged jet is allowed in had top
          # in the >=3 btagged event, more than 2 b tagged jet are allowed in had top
          #XXX require top mass window
          l.append(([i,j,k], (vectors[i]+vectors[j]+vectors[k]).Pt() if ((self.nbtags_event==2 and nbtags_had_top == 1) or (self.nbtags_event>=3 and nbtags_had_top >= 2)) and 100 < (vectors[i]+vectors[j]+vectors[k]).M() < 240 else -9999999999, nbtags_had_top ))
        l = sorted(l, key=itemgetter(1), reverse=True)
        self.nbtags_had_top = l[0][2] #store number of b-tagged jet in hadronic top
        return l[0][0]
