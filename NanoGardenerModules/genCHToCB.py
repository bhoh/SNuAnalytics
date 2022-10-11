import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import deltaR, closest, matchObjectCollection, matchObjectCollectionMultiple

import random
random.seed(10)

def toLorentzVector(idx, Jets_):

    jet = Jets_[idx]
    jet_vector = ROOT.TLorentzVector()
    #
    if hasattr(jet, "pt_nom"):
      jet_vector.SetPtEtaPhiM(jet.pt_nom,jet.eta,jet.phi,jet.mass)
    else:
      jet_vector.SetPtEtaPhiM(jet.pt,jet.eta,jet.phi,jet.mass)

    return jet_vector

def toLorentzVector_flavCorr(idx, Jets_, flav):
    jet = Jets_[idx]
    jet_vector = ROOT.TLorentzVector()

    if hasattr(jet, "pt_nom"):
      if flav == "b":
        flavCorr = jet.bRegCorr
      elif flav == "c":
        flavCorr = jet.cRegCorr
      else:
        raise Exception("toLorentzVector_flavCorr unsupported flavour")
      jet_vector.SetPtEtaPhiM(jet.pt_nom * flavCorr,jet.eta,jet.phi,jet.mass)
    else:
      jet_vector.SetPtEtaPhiM(jet.pt,jet.eta,jet.phi,jet.mass)

    return jet_vector



def toLorentzVector1(idx, Leptons_):

    lepton = Leptons_[idx]
    lepton_vector = ROOT.TLorentzVector()
    #
    lepton_vector.SetPtEtaPhiM(lepton.pt,lepton.eta,lepton.phi,0.)

    return lepton_vector

def toLorentzVector2(MET_pt_, MET_phi_):

    met_vector = ROOT.TLorentzVector()
    #
    met_vector.SetPtEtaPhiM(MET_pt_, 0., MET_phi_, 0.)

    return met_vector

class genCHToCB(Module):
    def __init__(self, cmssw):

        if '2016' in cmssw:
          self.Year = 2016
        if '2017' in cmssw:
          self.Year = 2017
        if '2018' in cmssw:
          self.Year = 2018

        self.cmssw = cmssw


        self.sortkey = lambda x: x.pt


        #XXX set pt eta cut by years
        self.ptcut = 25.
        if self.cmssw == "Full2016v9HIPM":
          self.absetacut = 2.4
          self._DeepFlavB_WP_M   = 0.2598
        elif self.cmssw == "Full2016v9noHIPM":
          self.absetacut = 2.4
          self._DeepFlavB_WP_M   = 0.2489
        elif self.cmssw == "Full2017v9":
          self.absetacut = 2.4
          self._DeepFlavB_WP_M   = 0.3040
        elif self.cmssw == "Full2018v9":
          self.absetacut = 2.4
          self._DeepFlavB_WP_M   = 0.2783
        else:
          raise RuntimeError("no cmssw configuration: " + self.cmssw)

    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("top_b_matched_jet_idx",             "I")
        self.out.branch("anti_top_b_matched_jet_idx",        "I")
        self.out.branch("had_top_down_type_matched_jet_idx", "I")
        self.out.branch("had_top_up_type_matched_jet_idx", "I")
        self.out.branch("had_top_b_matched_jet_idx", "I")
        self.out.branch("lep_top_b_matched_jet_idx", "I")
        self.out.branch("matched_dijet_mass", "F")
        self.out.branch("matched_dijet_mass_flavCorr", "F")
        self.out.branch("matched_dijet_pt", "F")
        self.out.branch("matched_dijet_deltaR", "F")
        self.out.branch("matched_dijet_ptD", "F")
        self.out.branch("matched_had_top_mass", "F")
        self.out.branch("matched_had_top_mass_flavCorr", "F")
        self.out.branch("matched_had_top_pt", "F")
        self.out.branch("matched_w_ch_b_deltaR", "F")
        self.out.branch("matched_had_top_b_deltaR", "F")
        self.out.branch("matched_lep_top_mass", "F")
        self.out.branch("matched_lep_top_mass_flavCorr", "F")
        self.out.branch("matched_mbl", "F")
        self.out.branch("matched_mbl_flavCorr", "F")
        self.out.branch("matched_tt_dphi", "F")
        self.out.branch("matched_had_top_sign", "I")
        self.out.branch("matched_4jet_matched", "I")

        self.out.branch("gen_dijet_mass", "F")
        self.out.branch("gen_had_top_mass", "F")
        self.out.branch("gen_had_top_b_lep_top_b_deltaR", "F")
        self.out.branch("gen_had_top_pt", "F")
        self.out.branch("gen_w_ch_b_deltaR", "F")
        self.out.branch("gen_had_top_b_deltaR", "F")

        self.out.branch("had_top_down_type_matched_genjet_idx", "I")
        self.out.branch("had_top_up_type_matched_genjet_idx", "I")
        self.out.branch("had_top_b_matched_genjet_idx", "I")
        self.out.branch("lep_top_b_matched_genjet_idx", "I")

        self.out.branch("rand_dijet_mass", "F")
        self.out.branch("rand_dijet_mass_flavCorr", "F")
        self.out.branch("rand_dijet_pt", "F")
        self.out.branch("rand_dijet_pt_flavCorr", "F")
        self.out.branch("rand_dijet_deltaR", "F")
        self.out.branch("rand_dijet_ptD", "F")
        self.out.branch("rand_had_top_mass", "F")
        self.out.branch("rand_had_top_mass_flavCorr", "F")
        self.out.branch("rand_had_top_pt", "F")
        self.out.branch("rand_lep_top_mass", "F")
        self.out.branch("rand_lep_top_mass_flavCorr", "F")
        self.out.branch("rand_mbl", "F")
        self.out.branch("rand_mbl_flavCorr", "F")
        self.out.branch("rand_tt_dphi", "F")
        self.out.branch("had_top_down_type_random_jet_idx", "I")
        self.out.branch("had_top_up_type_random_jet_idx", "I")
        self.out.branch("had_top_b_random_jet_idx", "I")
        self.out.branch("lep_top_b_random_jet_idx", "I")


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        genParticles = Collection(event, "GenPart")        #jet matching
        CleanJets = Collection(event, "CleanJet")
        Jets = Collection(event, "Jet")
        GenJets = Collection(event,"GenJet")
        Leptons = Collection(event, "Lepton")
        MET_pt  = event.PuppiMET_pt
        MET_phi = event.PuppiMET_phi


        # 1) find top / anti-top
        #print("debug flag 1")
        top_idx = -1
        anti_top_idx = -1
        for idx, particle in enumerate(genParticles):
          pdgId_ = particle.pdgId
          statusFlags_ = particle.statusFlags
          if pdgId_==6 and statusFlags_>>13 & 1: # last copy
            top_idx = idx
            #print("found a top idx : %s"%top_idx)
          elif pdgId_==-6 and statusFlags_>>13 & 1: # last copy
            anti_top_idx = idx
            #print("found a anti-top idx : %s"%anti_top_idx)

          # after find top and anti-top, break the loop
          if top_idx>=0 and anti_top_idx>=0:
            #print("found top pair, break the loop")
            break

        #print("debug flag 2")
        #XXX exception if we don't find ttbar pair
        if top_idx == -1 or anti_top_idx == -1:
          self.fillEmptyBranch()
          return True

        # 2) find W+ and W-
        #print("debug flag 3")
        w_plus_idx = -1
        w_minus_idx = -1

        # find w from top ancestor 
        for idx, particle in enumerate(genParticles):
          if (particle.pdgId==24 or particle.pdgId==37) and particle.statusFlags>>13 & 1: # last copy
            is_top_offspring_w = self.findAncester(idx,genParticles,top_idx,[6])
            if is_top_offspring_w:
              w_plus_idx = idx
              #print("found w+ : %s"%w_plus_idx)
          elif (particle.pdgId==-24 or particle.pdgId==-37) and particle.statusFlags>>13 & 1: # last copy
            is_anti_top_offspring_w = self.findAncester(idx,genParticles,anti_top_idx,[-6])
            if is_anti_top_offspring_w:
              w_minus_idx = idx
              #print("found w- : %s"%w_minus_idx)

          # after found w+,w-, break the loop
          if w_plus_idx>=0 and w_minus_idx>=0:
            #print("found W pair, break the loop")
            break

        #print("debug flag 4")
        #XXX exception if we don't find one of W
        if w_plus_idx == -1 or w_minus_idx == -1:
          self.fillEmptyBranch()
          return True
        
        #print("debug flag 5")
        top_b_idx = -1
        anti_top_b_idx = -1
        had_top_up_type_jet_idx = -1
        had_top_down_type_jet_idx = -1
        lep_top_lepton_idx = -1
        lep_top_neutrino = -1
        matched_had_top_sign = -10

        # 3) find ancestor
        ###
        for idx, particle in enumerate(genParticles):
          if abs(particle.pdgId)==5 and particle.statusFlags>>13 & 1 and particle.statusFlags>>8 & 1:
            #XXX check if
            #if self.findAncester(idx,genParticles,top_idx,[6],[-24,-37]):
            if self.findAncester(idx,genParticles,top_idx,[6],[24,37]):
              top_b_idx = idx
              #print("found top b : %s"%top_b_idx)
            #XXX check if
            #elif self.findAncester(idx,genParticles,anti_top_idx,[-6],[24,37]):
            elif self.findAncester(idx,genParticles,anti_top_idx,[-6],[-24,-37]):
              anti_top_b_idx = idx
              #print("found anti-top b : %s"%anti_top_b_idx)
            elif self.findAncester(idx,genParticles,w_plus_idx,[24,37]): 
              had_top_down_type_jet_idx = idx
              #print("found down type jet from w+ : %s"%had_top_down_type_jet_idx)
            elif self.findAncester(idx,genParticles,w_minus_idx,[-24,-37]):
              had_top_down_type_jet_idx = idx
              #print("found down type jet from w- : %s"%had_top_down_type_jet_idx)
          elif (abs(particle.pdgId) in [1,3] ) and particle.statusFlags>>13 & 1 and particle.statusFlags>>8 & 1: # d, s
            if self.findAncester(idx,genParticles,w_plus_idx,[24,37]):
              had_top_down_type_jet_idx = idx
              #print("found down type jet from w+ : %s"%had_top_down_type_jet_idx)
            elif self.findAncester(idx,genParticles,w_minus_idx,[-24,-37]):
              had_top_down_type_jet_idx = idx
              #print("found down type jet from w- : %s"%had_top_down_type_jet_idx)
          elif (abs(particle.pdgId) in [2,4] ) and particle.statusFlags>>13 & 1 and particle.statusFlags>>8 & 1: # u, c
            if self.findAncester(idx,genParticles,w_plus_idx,[24,37]):
              had_top_up_type_jet_idx = idx
              #print("found up type jet from w+ : %s"%had_top_up_type_jet_idx)
            elif self.findAncester(idx,genParticles,w_minus_idx,[-24,-37]):
              had_top_up_type_jet_idx = idx
              #print("found up type jet from w- : %s"%had_top_up_type_jet_idx)
          elif ( (abs(particle.pdgId)==11 or abs(particle.pdgId)==12) and particle.status == 1) and particle.statusFlags>>8 & 1:
            if self.findAncester(idx,genParticles,w_plus_idx,[24,37]):
              lep_top_lepton_idx = idx
              matched_had_top_sign = -1
              #print("matched_had_top_sign : %s"%matched_had_top_sign)
            elif self.findAncester(idx,genParticles,w_minus_idx,[-24,-37]):
              lep_top_lepton_idx = idx
              matched_had_top_sign = 1
              #print("matched_had_top_sign : %s"%matched_had_top_sign)
          elif (abs(particle.pdgId)==12 or abs(particle.pdgId)==14) and particle.status == 1  and particle.statusFlags>>8 & 1: 
            if self.findAncester(idx,genParticles,w_plus_idx,[24,37]):
              lep_top_neutrino = idx
            elif self.findAncester(idx,genParticles,w_minus_idx,[-24,-37]):
              lep_top_neutrino = idx

        #filter functions
        #FIXME match reco jet and gen jet -> remove jet from PU
        #jetSelFcn      = lambda jet, Jets__: (Jets__[jet.jetIdx].genJetIdx >= 0) and (abs(jet.eta)<self.absetacut) and (jet.pt>self.ptcut)
        isRealJet      = lambda jet: closest(jet, GenJets)[1] < 0.2
        jetSelFcn      = lambda jet, Jets__: isRealJet(jet)
        isBPartonJet   = lambda jet, Jets__: Jets__[jet.jetIdx].partonFlavour == 5
        isAntiBPartonJet   = lambda jet, Jets__: Jets__[jet.jetIdx].partonFlavour == -5
        jetBtagMFcn    = lambda jet, Jets__: (Jets__[jet.jetIdx].btagDeepFlavB > self._DeepFlavB_WP_M)
        #filtered jets
        RealJets             = self.filterJets(CleanJets, Jets, jetSelFcn)
        RealJets_BParton     = self.filterJets(RealJets, Jets, isBPartonJet)
        RealJets_AntiBParton     = self.filterJets(RealJets, Jets, isAntiBPartonJet)
        GenJets_BParton      = filter(lambda jet: jet.partonFlavour == 5, GenJets)
        GenJets_AntiBParton      = filter(lambda jet: jet.partonFlavour == -5, GenJets)
        #
        #matched jet index list parton - genjet
        top_b_matched_list             = self.genJetMatching(top_b_idx,                 genParticles, GenJets)
        anti_top_b_matched_list        = self.genJetMatching(anti_top_b_idx,            genParticles, GenJets)
        had_top_down_type_matched_list = self.genJetMatching(had_top_down_type_jet_idx, genParticles, GenJets)
        had_top_up_type_matched_list   = self.genJetMatching(had_top_up_type_jet_idx,   genParticles, GenJets)

        top_b_matched_genjet_idx             = top_b_matched_list[0]             if len(top_b_matched_list)==1 else -1
        anti_top_b_matched_genjet_idx        = anti_top_b_matched_list[0]        if len(anti_top_b_matched_list)==1 else -1
        had_top_down_type_matched_genjet_idx = had_top_down_type_matched_list[0] if len(had_top_down_type_matched_list)==1 else -1
        had_top_up_type_matched_genjet_idx   = had_top_up_type_matched_list[0]   if len(had_top_up_type_matched_list)==1 else -1

        # ambiguity matching case
        matched_genjet_list = [top_b_matched_genjet_idx, anti_top_b_matched_genjet_idx, had_top_down_type_matched_genjet_idx, had_top_up_type_matched_genjet_idx]
        matched_genjet_list = [ idx for idx in matched_genjet_list if not idx < 0 ]
        if not len(matched_genjet_list) == len(set(matched_genjet_list)):
          top_b_matched_genjet_idx             = -1
          anti_top_b_matched_genjet_idx        = -1
          had_top_down_type_matched_genjet_idx = -1
          had_top_up_type_matched_genjet_idx   = -1

        #matched jet index list genjet - recojet
        top_b_matched_list             = self.jetMatching(top_b_matched_genjet_idx            , GenJets,     RealJets)
        anti_top_b_matched_list        = self.jetMatching(anti_top_b_matched_genjet_idx       , GenJets, RealJets)
        had_top_down_type_matched_list = self.jetMatching(had_top_down_type_matched_genjet_idx, GenJets, RealJets)
        had_top_up_type_matched_list   = self.jetMatching(had_top_up_type_matched_genjet_idx  , GenJets, RealJets)

        top_b_matched_jet_idx             = top_b_matched_list[0]             if len(top_b_matched_list)==1 else -1
        anti_top_b_matched_jet_idx        = anti_top_b_matched_list[0]        if len(anti_top_b_matched_list)==1 else -1    
        had_top_down_type_matched_jet_idx = had_top_down_type_matched_list[0] if len(had_top_down_type_matched_list)==1 else -1
        had_top_up_type_matched_jet_idx   = had_top_up_type_matched_list[0]   if len(had_top_up_type_matched_list)==1 else -1

        # if a jet index not satisfy a selection criteria, assign -1
        checkAcceptence = lambda jet_idx:  jet_idx if jet_idx>=0 and Jets[jet_idx].pt_nom > 15. and abs(Jets[jet_idx].eta)<2.4 else -1
        top_b_matched_jet_idx             = checkAcceptence( top_b_matched_jet_idx            )
        anti_top_b_matched_jet_idx        = checkAcceptence( anti_top_b_matched_jet_idx       ) 
        had_top_down_type_matched_jet_idx = checkAcceptence( had_top_down_type_matched_jet_idx) 
        had_top_up_type_matched_jet_idx   = checkAcceptence( had_top_up_type_matched_jet_idx  ) 


        matched_dijet_mass, matched_dijet_mass_flavCorr, matched_dijet_pt, matched_dijet_pt_flavCorr, matched_dijet_deltaR, matched_dijet_ptD = self.getDijetMassPtDeltaRptD(had_top_down_type_matched_jet_idx,had_top_up_type_matched_jet_idx,Jets)
        gen_dijet_mass, _, _, _, _, _ = self.getDijetMassPtDeltaRptD(had_top_down_type_matched_genjet_idx,had_top_up_type_matched_genjet_idx,GenJets)
        if matched_had_top_sign==-10:
          had_top_b_idx = -1
          lep_top_b_idx = -1
          had_top_b_genjet_idx = -1
          lep_top_b_genjet_idx = -1
        else:
          if matched_had_top_sign==-1:
            had_top_b_idx = anti_top_b_matched_jet_idx
            lep_top_b_idx = top_b_matched_jet_idx
            had_top_b_genjet_idx = anti_top_b_matched_genjet_idx
            lep_top_b_genjet_idx = top_b_matched_genjet_idx
          else:
            had_top_b_idx = top_b_matched_jet_idx
            lep_top_b_idx = anti_top_b_matched_jet_idx
            had_top_b_genjet_idx = top_b_matched_genjet_idx
            lep_top_b_genjet_idx = anti_top_b_matched_genjet_idx


        matched_had_top_mass, matched_had_top_pt, matched_had_top_mass_flavCorr, matched_w_ch_b_deltaR, matched_had_top_b_deltaR  = self.getHadTopKin(had_top_down_type_matched_jet_idx,had_top_up_type_matched_jet_idx,had_top_b_idx,Jets)

        matched_lep_top_mass, matched_lep_top_mass_flavCorr, matched_mbl, matched_mbl_flavCorr = self.getLepTopMassMbl(lep_top_b_idx, Jets, Leptons, MET_pt, MET_phi)
        matched_tt_dphi               = self.getTTdPhi()

        gen_had_top_mass, gen_had_top_pt, _, gen_w_ch_b_deltaR, gen_had_top_b_deltaR = self.getHadTopKin(had_top_down_type_matched_genjet_idx,had_top_up_type_matched_genjet_idx,had_top_b_genjet_idx,GenJets)
        gen_had_top_b_lep_top_b_deltaR = deltaR(GenJets[had_top_b_genjet_idx], GenJets[lep_top_b_genjet_idx]) if had_top_b_genjet_idx>=0 and lep_top_b_genjet_idx>=0 else -1

        CleanJets_selected = filter(lambda jet: Jets[jet.jetIdx].pt_nom > 15. and abs(jet.eta)<2.4, CleanJets)
        CleanJets_selected_btaged = self.filterJets(CleanJets_selected, Jets, jetBtagMFcn)
        #sort in pT order
        CleanJets_selected.sort(key=lambda jet: Jets[jet.jetIdx].pt_nom, reverse=True)
        CleanJets_selected = CleanJets_selected[:6] #upto leading 6 jets
        matched_four_idxs = [had_top_down_type_matched_jet_idx, had_top_up_type_matched_jet_idx, had_top_b_idx, lep_top_b_idx]
        random_jet_idxs = self.randomAssignment(CleanJets_selected, CleanJets_selected_btaged, matched_four_idxs)
        had_top_down_type_random_jet_idx, had_top_up_type_random_jet_idx, had_top_b_random_jet_idx, lep_top_b_random_jet_idx = random_jet_idxs

        rand_dijet_mass, rand_dijet_mass_flavCorr, rand_dijet_pt, rand_dijet_pt_flavCorr, rand_dijet_deltaR, rand_dijet_ptD = self.getDijetMassPtDeltaRptD(had_top_down_type_random_jet_idx,had_top_up_type_random_jet_idx,Jets)
        rand_had_top_mass, rand_had_top_pt, rand_had_top_mass_flavCorr, _, _ = self.getHadTopKin(had_top_down_type_random_jet_idx,had_top_up_type_random_jet_idx,had_top_b_random_jet_idx,Jets)
        rand_lep_top_mass, rand_lep_top_mass_flavCorr, rand_mbl, rand_mbl_flavCorr = self.getLepTopMassMbl(lep_top_b_random_jet_idx, Jets, Leptons, MET_pt, MET_phi)
        rand_tt_dphi                = self.getTTdPhi()


        #check if there 4 jet matched with parton with no ambiguity
        is_4jet_matched = -1
        if top_b_matched_jet_idx!=-1 and\
           anti_top_b_matched_jet_idx!=-1 and\
           had_top_down_type_matched_jet_idx!=-1 and\
           had_top_up_type_matched_jet_idx!=-1:
          if top_b_matched_jet_idx != anti_top_b_matched_jet_idx and\
             top_b_matched_jet_idx != had_top_down_type_matched_jet_idx and\
             top_b_matched_jet_idx != had_top_up_type_matched_jet_idx:
            if anti_top_b_matched_jet_idx != had_top_down_type_matched_jet_idx and\
               anti_top_b_matched_jet_idx != had_top_up_type_matched_jet_idx:
              if had_top_down_type_matched_jet_idx != had_top_up_type_matched_jet_idx:
                is_4jet_matched = 1

        self.out.fillBranch("top_b_matched_jet_idx",             top_b_matched_jet_idx            )  
        self.out.fillBranch("anti_top_b_matched_jet_idx",        anti_top_b_matched_jet_idx       )  
        self.out.fillBranch("had_top_down_type_matched_jet_idx", had_top_down_type_matched_jet_idx)  
        self.out.fillBranch("had_top_up_type_matched_jet_idx",   had_top_up_type_matched_jet_idx  )  
        self.out.fillBranch("had_top_b_matched_jet_idx",         had_top_b_idx )
        self.out.fillBranch("lep_top_b_matched_jet_idx",         lep_top_b_idx )
        self.out.fillBranch("matched_dijet_mass", matched_dijet_mass)
        self.out.fillBranch("matched_dijet_mass_flavCorr", matched_dijet_mass_flavCorr)
        self.out.fillBranch("matched_dijet_pt", matched_dijet_pt)
        self.out.fillBranch("matched_dijet_deltaR", matched_dijet_deltaR)
        self.out.fillBranch("matched_dijet_ptD", matched_dijet_ptD)
        self.out.fillBranch("matched_had_top_mass", matched_had_top_mass)
        self.out.fillBranch("matched_had_top_mass_flavCorr", matched_had_top_mass_flavCorr)
        self.out.fillBranch("matched_had_top_pt", matched_had_top_pt)
        self.out.fillBranch("matched_w_ch_b_deltaR",    matched_w_ch_b_deltaR  )
        self.out.fillBranch("matched_had_top_b_deltaR", matched_had_top_b_deltaR)
        self.out.fillBranch("matched_lep_top_mass", matched_lep_top_mass)
        self.out.fillBranch("matched_lep_top_mass_flavCorr", matched_lep_top_mass_flavCorr)
        self.out.fillBranch("matched_mbl", matched_mbl)
        self.out.fillBranch("matched_mbl_flavCorr", matched_mbl_flavCorr)
        self.out.fillBranch("matched_tt_dphi", matched_tt_dphi)
        self.out.fillBranch("matched_had_top_sign", matched_had_top_sign)
        self.out.fillBranch("matched_4jet_matched", is_4jet_matched)

        self.out.fillBranch("gen_dijet_mass",   gen_dijet_mass)
        self.out.fillBranch("gen_had_top_mass", gen_had_top_mass)
        self.out.fillBranch("gen_had_top_b_lep_top_b_deltaR", gen_had_top_b_lep_top_b_deltaR)
        self.out.fillBranch("gen_had_top_pt", gen_had_top_pt)
        self.out.fillBranch("gen_w_ch_b_deltaR",    gen_w_ch_b_deltaR  )
        self.out.fillBranch("gen_had_top_b_deltaR", gen_had_top_b_deltaR)

        self.out.fillBranch("had_top_down_type_matched_genjet_idx", had_top_down_type_matched_genjet_idx)  
        self.out.fillBranch("had_top_up_type_matched_genjet_idx",   had_top_up_type_matched_genjet_idx  )  
        self.out.fillBranch("had_top_b_matched_genjet_idx",         had_top_b_genjet_idx )
        self.out.fillBranch("lep_top_b_matched_genjet_idx",         lep_top_b_genjet_idx )

        self.out.fillBranch("rand_dijet_mass",   rand_dijet_mass)
        self.out.fillBranch("rand_dijet_mass_flavCorr",   rand_dijet_mass_flavCorr)
        self.out.fillBranch("rand_dijet_pt",     rand_dijet_pt)
        self.out.fillBranch("rand_dijet_pt_flavCorr",     rand_dijet_pt_flavCorr)
        self.out.fillBranch("rand_dijet_deltaR", rand_dijet_deltaR)
        self.out.fillBranch("rand_dijet_ptD",    rand_dijet_ptD)
        self.out.fillBranch("rand_had_top_mass", rand_had_top_mass)
        self.out.fillBranch("rand_had_top_mass_flavCorr", rand_had_top_mass_flavCorr)
        self.out.fillBranch("rand_had_top_pt",   rand_had_top_pt)
        self.out.fillBranch("rand_lep_top_mass", rand_lep_top_mass)
        self.out.fillBranch("rand_lep_top_mass_flavCorr", rand_lep_top_mass_flavCorr)
        self.out.fillBranch("rand_mbl",          rand_mbl)
        self.out.fillBranch("rand_mbl_flavCorr", rand_mbl_flavCorr)
        self.out.fillBranch("rand_tt_dphi",      rand_tt_dphi)
        self.out.fillBranch("had_top_down_type_random_jet_idx", had_top_down_type_random_jet_idx)
        self.out.fillBranch("had_top_up_type_random_jet_idx",   had_top_up_type_random_jet_idx)
        self.out.fillBranch("had_top_b_random_jet_idx",         had_top_b_random_jet_idx)
        self.out.fillBranch("lep_top_b_random_jet_idx",         lep_top_b_random_jet_idx)
            
        return True

    def fillEmptyBranch(self):
        self.out.fillBranch("top_b_matched_jet_idx",            -1 )  
        self.out.fillBranch("anti_top_b_matched_jet_idx",       -1 )  
        self.out.fillBranch("had_top_down_type_matched_jet_idx",-1 )  
        self.out.fillBranch("had_top_up_type_matched_jet_idx",  -1 )  
        self.out.fillBranch("had_top_b_matched_jet_idx", -1)
        self.out.fillBranch("lep_top_b_matched_jet_idx", -1)
        self.out.fillBranch("matched_dijet_mass", -1)
        self.out.fillBranch("matched_dijet_mass_flavCorr", -1)
        self.out.fillBranch("matched_dijet_pt", -1)
        self.out.fillBranch("matched_dijet_deltaR", -1)
        self.out.fillBranch("matched_dijet_ptD", -1)
        self.out.fillBranch("matched_had_top_mass", -1)
        self.out.fillBranch("matched_had_top_mass_flavCorr", -1)
        self.out.fillBranch("matched_had_top_pt", -1)
        self.out.fillBranch("matched_w_ch_b_deltaR", -1)
        self.out.fillBranch("matched_had_top_b_deltaR", -1)
        self.out.fillBranch("matched_lep_top_mass", -1)
        self.out.fillBranch("matched_lep_top_mass_flavCorr", -1)
        self.out.fillBranch("matched_mbl", -1)
        self.out.fillBranch("matched_mbl_flavCorr", -1)
        self.out.fillBranch("matched_tt_dphi", -1)
        self.out.fillBranch("matched_had_top_sign", -1)
        self.out.fillBranch("matched_4jet_matched", -1)

        self.out.fillBranch("gen_dijet_mass",   -1)
        self.out.fillBranch("gen_had_top_mass", -1)
        self.out.fillBranch("gen_had_top_b_lep_top_b_deltaR", -1)
        self.out.fillBranch("gen_had_top_pt", -1)
        self.out.fillBranch("gen_w_ch_b_deltaR", -1)
        self.out.fillBranch("gen_had_top_b_deltaR", -1)

        self.out.fillBranch("had_top_down_type_matched_genjet_idx", -1)
        self.out.fillBranch("had_top_up_type_matched_genjet_idx",   -1)
        self.out.fillBranch("had_top_b_matched_genjet_idx",         -1)
        self.out.fillBranch("lep_top_b_matched_genjet_idx",         -1)

        self.out.fillBranch("rand_dijet_mass",   -1)
        self.out.fillBranch("rand_dijet_mass_flavCorr", -1)
        self.out.fillBranch("rand_dijet_pt",     -1)
        self.out.fillBranch("rand_dijet_pt_flavCorr",     -1)
        self.out.fillBranch("rand_dijet_deltaR", -1)
        self.out.fillBranch("rand_dijet_ptD",    -1)
        self.out.fillBranch("rand_had_top_mass", -1)
        self.out.fillBranch("rand_had_top_mass_flavCorr", -1)
        self.out.fillBranch("rand_had_top_pt",   -1)
        self.out.fillBranch("rand_lep_top_mass", -1)
        self.out.fillBranch("rand_lep_top_mass_flavCorr", -1)
        self.out.fillBranch("rand_mbl",          -1)
        self.out.fillBranch("rand_mbl_flavCorr",          -1)
        self.out.fillBranch("rand_tt_dphi",      -1)
        self.out.fillBranch("had_top_down_type_random_jet_idx",  -1)
        self.out.fillBranch("had_top_up_type_random_jet_idx",    -1)
        self.out.fillBranch("had_top_b_random_jet_idx",          -1)
        self.out.fillBranch("lep_top_b_random_jet_idx",          -1)


    def findAncester(self, offspring_Idx, genPart, ancester_Idx, ancester_pdgId, not_from_ancester_pdgId=[]):
        idx = offspring_Idx
        mother_idx = idx #initialize
        out = False
        while mother_idx>0:
          mother_idx = genPart[idx].genPartIdxMother
          idx = mother_idx # update idx
          
          if idx<0: # to avoid negative index
            break
          elif genPart[idx].pdgId in not_from_ancester_pdgId: # to avoid some pdgId
            out = False
            break
          elif idx == ancester_Idx:
            if genPart[idx].pdgId in ancester_pdgId:
              out = True
              break
            else:
              out = False
              break
          else:
            pass

        return out

    def filterJets(self, CleanJets_, Jets_, filterFcn):

        CleanJets = [ jet for jet in CleanJets_ if filterFcn(jet, Jets_) ]
        return CleanJets

    def genJetMatching(self, genIdx, genParticle, GenJets_):
        if genIdx<0:
          return []


        matched_idx=[]
        # find the closest jet matched within 0.4 and parton pT more than 20 GeV
        matched_jet, min_deltaR, n_presel = self.closest(genParticle[genIdx], GenJets_, lambda x,y: deltaR(x,y)<0.4)
        if matched_jet == None:
          return []
        if not n_presel == 1:
          return []
        
        for i, jet in enumerate(GenJets_):
          if deltaR(jet, matched_jet) == 0:
            matched_idx.append(i)
      
        return matched_idx

    def jetMatching(self, genIdx, genParticle, CleanJets_):
        if genIdx<0:
          return []


        matched_idx=[]
        # find the closest jet matched within 0.4 and whose pT is not greater than 30%.
        matched_jet, min_deltaR, n_presel = self.closest(genParticle[genIdx], CleanJets_, lambda x,y: deltaR(x,y)<0.2)
        if matched_jet == None:
          return []
        if not n_presel == 1:
          return []
        
        for jet in CleanJets_:
          if deltaR(jet, matched_jet) == 0:
            matched_idx.append(jet.jetIdx)

      
        return matched_idx

    def getDijetMassPtDeltaRptD(self,idx1,idx2,Jets_):
        is_2jet_matched = True
        if idx1<0 or idx2<0:
          is_2jet_matched = False

        if is_2jet_matched:
          jet_vector1 = toLorentzVector(idx1, Jets_)
          jet_vector2 = toLorentzVector(idx2, Jets_)
          jet_vector1_flavCorr = toLorentzVector_flavCorr(idx1, Jets_, "b")
          jet_vector2_flavCorr = toLorentzVector_flavCorr(idx2, Jets_, "c")

          dijet_vector = jet_vector1+jet_vector2
          dijet_mass = dijet_vector.M()
          dijet_pt   = dijet_vector.Pt()
          dijet_deltaR = jet_vector1.DeltaR(jet_vector2)
          dijet_ptD = dijet_pt*dijet_deltaR


          dijet_vector_flavCorr = jet_vector1_flavCorr+jet_vector2_flavCorr
          dijet_pt_flavCorr = dijet_vector_flavCorr.Pt()
          dijet_mass_flavCorr = dijet_vector_flavCorr.M()
        else:
          dijet_mass   = -1
          dijet_pt     = -1
          dijet_pt_flavCorr     = -1
          dijet_mass_flavCorr = -1 
          dijet_deltaR = -1
          dijet_ptD    = -1

        return dijet_mass, dijet_mass_flavCorr, dijet_pt, dijet_pt_flavCorr, dijet_deltaR, dijet_ptD

    def getHadTopKin(self,idx1,idx2,idx3,Jets_):
        is_3jet_matched = True
        if idx1<0 or idx2<0 or idx3<0:
          is_3jet_matched = False

        if is_3jet_matched:
          jet_vector1 = toLorentzVector(idx1, Jets_)
          jet_vector2 = toLorentzVector(idx2, Jets_)
          jet_vector3 = toLorentzVector(idx3, Jets_)
          jet_vector1_flavCorr = toLorentzVector_flavCorr(idx1, Jets_, "b")
          jet_vector2_flavCorr = toLorentzVector_flavCorr(idx2, Jets_, "c")
          jet_vector3_flavCorr = toLorentzVector_flavCorr(idx3, Jets_, "b")
          

          w_ch    = jet_vector1 + jet_vector2
          had_top = w_ch + jet_vector3
          self.had_top = had_top
          had_top_mass, had_top_pt = had_top.M(), had_top.Pt()
          w_ch_b_deltaR    = w_ch.DeltaR(jet_vector3)
          had_top_b_deltaR = had_top.DeltaR(jet_vector3)

          had_top_flavCorr = jet_vector1_flavCorr+jet_vector2_flavCorr+jet_vector3_flavCorr
          had_top_mass_flavCorr = had_top_flavCorr.M()
        else:
          self.had_top = None
          had_top_mass, had_top_pt = -1, -1
          had_top_mass_flavCorr = -1
          w_ch_b_deltaR, had_top_b_deltaR = -1, -1
        return had_top_mass, had_top_pt, had_top_mass_flavCorr, w_ch_b_deltaR, had_top_b_deltaR

    def getLepTopMassMbl(self,idx1,Jets_,Lepton_,MET_pt_, MET_phi_):
        if idx1<0:
          lep_top_mass, lep_top_mass_flavCorr, Mbl, Mbl_flavCorr = -1, -1, -1, -1
          self.lep_top = None
        else:
          jet_vector1 = toLorentzVector(idx1, Jets_)
          jet_vector1_flavCorr = toLorentzVector_flavCorr(idx1, Jets_, "b")
          lep_vector  = toLorentzVector1(0, Lepton_)
          MET_vector  = toLorentzVector2(MET_pt_, MET_phi_)

          mbl          = jet_vector1 + lep_vector
          mbl_flavCorr = jet_vector1_flavCorr + lep_vector
          lep_top          = mbl + MET_vector
          lep_top_flavCorr = mbl_flavCorr + MET_vector
          self.lep_top = lep_top

          lep_top_mass, lep_top_mass_flavCorr, Mbl, Mbl_flavCorr = lep_top.M(), lep_top_flavCorr.M(), mbl.M(), mbl_flavCorr.M()

        return lep_top_mass, lep_top_mass_flavCorr, Mbl, Mbl_flavCorr

    def getTTdPhi(self):
        if self.had_top == None:
          tt_dphi = -1
        elif self.lep_top == None:
          tt_dphi = -1
        else:
          tt_dphi = self.had_top.DeltaPhi(self.lep_top)
        return tt_dphi



    def randomAssignment(self, CleanJets_, CleanJets_btaged_, trueIdxs):
        num_sets = 4
        CleanJets_idxs = map(lambda jet: jet.jetIdx, CleanJets_)
        CleanJets_btaged_idxs = map(lambda jet: jet.jetIdx, CleanJets_btaged_)

        if num_sets > len(CleanJets_idxs):
          return [-1,-1,-1,-1]

        # no >=2 b jets in selected jets
        if (set(CleanJets_idxs) & set(CleanJets_btaged_idxs) ) < 2:
          return [-1,-1,-1,-1]

        # sample again if this is same as true assignment
        # [had_top_down_type_matched_jet_idx, had_top_up_type_matched_jet_idx, had_top_b_idx, lep_top_b_idx]

        resample = True
        nIter    = 0
        maxIter  = 5000
        while resample:
          # sample jets randomly
          random_jets = random.sample(CleanJets_idxs, num_sets)
          nIter      += 1
          resample    = False

          if nIter >= maxIter:
            break

          if sorted(random_jets[:2]) == sorted(trueIdxs[:2]):
            resample = True
          if sorted(random_jets[:3]) == sorted(trueIdxs[:3]):
            resample = True
          if random_jets[3] == trueIdxs[3]:
            resample = True
          if random_jets[2] not in CleanJets_btaged_idxs:
            resample = True
          if random_jets[3] not in CleanJets_btaged_idxs:
            resample = True

        return random_jets

    def closest(self,obj,collection,presel=lambda x,y: True):
      ret = None; drMin = 999; n_presel = 0;
      for x in collection:
        if not presel(obj,x): continue
        n_presel += 1
        dr = deltaR(obj,x)
        if dr < drMin:
          ret = x; drMin = dr
      return ret, drMin, n_presel


