import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class genCHToCB(Module):
    def __init__(self):
        self.sortkey = lambda x: x.pt
        pass
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
        self.out.branch("gen_dijet_mass", "F")
        self.out.branch("gen_dijet_pt", "F")
        self.out.branch("gen_dijet_deltaR", "F")
        self.out.branch("gen_dijet_ptD", "F")
        self.out.branch("gen_had_top_mass", "F")
        self.out.branch("gen_had_top_pt", "F")
        self.out.branch("gen_had_top_sign", "I")
        self.out.branch("gen_4jet_matched", "I")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        genParticles = Collection(event, "GenPart")


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
        gen_had_top_sign = -10

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
          elif ( (abs(particle.pdgId)==11 or abs(particle.pdgId)==13) and particle.status == 1) and particle.statusFlags>>8 & 1:
            if self.findAncester(idx,genParticles,w_plus_idx,[24,37]):
              lep_top_lepton_idx = idx
              gen_had_top_sign = -1
              #print("gen_had_top_sign : %s"%gen_had_top_sign)
            elif self.findAncester(idx,genParticles,w_minus_idx,[-24,-37]):
              lep_top_lepton_idx = idx
              gen_had_top_sign = 1
              #print("gen_had_top_sign : %s"%gen_had_top_sign)
          elif (abs(particle.pdgId)==12 or abs(particle.pdgId)==14) and particle.status == 1  and particle.statusFlags>>8 & 1: 
            if self.findAncester(idx,genParticles,w_plus_idx,[24,37]):
              lep_top_neutrino = idx
            elif self.findAncester(idx,genParticles,w_minus_idx,[-24,-37]):
              lep_top_neutrino = idx

        #jet matching
        CleanJets = Collection(event, "CleanJet")
        Jets = Collection(event, "Jet")
        top_b_matched_list             = self.jetMatching(top_b_idx,genParticles,CleanJets,Jets)
        anti_top_b_matched_list        = self.jetMatching(anti_top_b_idx,genParticles,CleanJets,Jets)
        had_top_down_type_matched_list = self.jetMatching(had_top_down_type_jet_idx,genParticles,CleanJets,Jets)
        had_top_up_type_matched_list   = self.jetMatching(had_top_up_type_jet_idx,genParticles,CleanJets,Jets)

        top_b_matched_jet_idx             = top_b_matched_list[0]             if len(top_b_matched_list)==1 else -1
        anti_top_b_matched_jet_idx        = anti_top_b_matched_list[0]        if len(anti_top_b_matched_list)==1 else -1    
        had_top_down_type_matched_jet_idx = had_top_down_type_matched_list[0] if len(had_top_down_type_matched_list)==1 else -1
        had_top_up_type_matched_jet_idx   = had_top_up_type_matched_list[0]   if len(had_top_up_type_matched_list)==1 else -1

        gen_dijet_mass, gen_dijet_pt, gen_dijet_deltaR, gen_dijet_ptD = self.getDijetMassPtDeltaRptD(had_top_down_type_matched_jet_idx,had_top_up_type_matched_jet_idx,Jets)
        if gen_had_top_sign==-10:
          had_top_b_idx = -1
        else:
          if gen_had_top_sign==-1:
            had_top_b_idx = anti_top_b_matched_jet_idx
          else:
            had_top_b_idx = top_b_matched_jet_idx

        gen_had_top_mass, gen_had_top_pt = self.getHadTopMassPt(had_top_down_type_matched_jet_idx,had_top_up_type_matched_jet_idx,had_top_b_idx,Jets)

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
        self.out.fillBranch("gen_dijet_mass", gen_dijet_mass)
        self.out.fillBranch("gen_dijet_pt", gen_dijet_pt)
        self.out.fillBranch("gen_dijet_deltaR", gen_dijet_deltaR)
        self.out.fillBranch("gen_dijet_ptD", gen_dijet_ptD)
        self.out.fillBranch("gen_had_top_mass", gen_had_top_mass)
        self.out.fillBranch("gen_had_top_pt", gen_had_top_pt)
        self.out.fillBranch("gen_had_top_sign", gen_had_top_sign)
        self.out.fillBranch("gen_4jet_matched", is_4jet_matched)
            
        return True

    def fillEmptyBranch(self):
        self.out.fillBranch("top_b_matched_jet_idx",            -1 )  
        self.out.fillBranch("anti_top_b_matched_jet_idx",       -1 )  
        self.out.fillBranch("had_top_down_type_matched_jet_idx",-1 )  
        self.out.fillBranch("had_top_up_type_matched_jet_idx",  -1 )  
        self.out.fillBranch("gen_dijet_mass", -1)
        self.out.fillBranch("gen_dijet_pt", -1)
        self.out.fillBranch("gen_dijet_deltaR", -1)
        self.out.fillBranch("gen_dijet_ptD", -1)
        self.out.fillBranch("gen_had_top_mass", -1)
        self.out.fillBranch("gen_had_top_pt", -1)
        self.out.fillBranch("gen_had_top_sign", -1)
        self.out.fillBranch("gen_4jet_matched", -1)


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
  
    def jetMatching(self,genIdx,genParticle,CleanJet_,Jet_):
        if genIdx<0:
          return []

        gen_eta = genParticle[genIdx].eta
        gen_phi = genParticle[genIdx].phi
        matched_idx=[]
        for jet in CleanJet_:
          jet_pt = Jet_[jet.jetIdx].pt_nom
          jet_eta = jet.eta
          jet_phi = jet.phi
          if abs(jet_eta) >= 2.5 or jet_pt <=30.:
            continue

          is_matched = ((gen_eta-jet_eta)*(gen_eta-jet_eta)+(gen_phi-jet_phi)*(gen_phi-jet_phi))<(0.4*0.4)
          is_real_jet = Jet_[jet.jetIdx].genJetIdx != -1
          if is_matched and is_real_jet:
            matched_idx.append(jet.jetIdx)
      
        return matched_idx

    def getDijetMassPtDeltaRptD(self,idx1,idx2,Jet_):
        is_2jet_matched = True
        if idx1<0 or idx2<0:
          is_2jet_matched = False

        if is_2jet_matched:
          jet1 = Jet_[idx1]
          jet2 = Jet_[idx2]
          jet_vector1 = ROOT.TLorentzVector()
          jet_vector2 = ROOT.TLorentzVector()
          #
          jet_vector1.SetPtEtaPhiM(jet1.pt_nom,jet1.eta,jet1.phi,jet1.mass)
          jet_vector2.SetPtEtaPhiM(jet2.pt_nom,jet2.eta,jet2.phi,jet2.mass)

          dijet_vector = jet_vector1+jet_vector2
          dijet_mass = dijet_vector.M()
          dijet_pt   = dijet_vector.Pt()
          dijet_deltaR = jet_vector1.DeltaR(jet_vector2)
          dijet_ptD = dijet_pt*dijet_deltaR
        else:
          dijet_mass   = -1
          dijet_pt     = -1
          dijet_deltaR = -1
          dijet_ptD    = -1

        return dijet_mass, dijet_pt, dijet_deltaR, dijet_ptD

    def getHadTopMassPt(self,idx1,idx2,idx3,Jet_):
        is_3jet_matched = True
        if idx1<0 or idx2<0 or idx3<0:
          is_3jet_matched = False

        if is_3jet_matched:
          jet1 = Jet_[idx1]
          jet2 = Jet_[idx2]
          jet3 = Jet_[idx3]
          jet_vector1 = ROOT.TLorentzVector()
          jet_vector2 = ROOT.TLorentzVector()
          jet_vector3 = ROOT.TLorentzVector()
          #
          jet_vector1.SetPtEtaPhiM(jet1.pt_nom,jet1.eta,jet1.phi,jet1.mass)
          jet_vector2.SetPtEtaPhiM(jet2.pt_nom,jet2.eta,jet2.phi,jet2.mass)
          jet_vector3.SetPtEtaPhiM(jet3.pt_nom,jet3.eta,jet3.phi,jet3.mass)

          had_top = jet_vector1+jet_vector2+jet_vector3
          had_top_mass, had_top_pt = had_top.M(), had_top.Pt()
        else:
          had_top_mass, had_top_pt = -1, -1
        return had_top_mass, had_top_pt



