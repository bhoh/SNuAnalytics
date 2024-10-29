import ROOT
import os, tarfile, tempfile, shutil
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

from ROOT import TLorentzVector
from itertools import combinations
from operator import itemgetter, attrgetter
from math import cosh, sqrt
import random


##
LARGE_NUM=9999999999

##
# this module is to add variables for MVA training to skim tree.
##
class mvaTreeCHToCB(Module):
    def __init__(self, cmssw, syst_suffix='nom', isSmear=False, genMatched=False):
        random.seed(12345)
        #self._lowerBjetPt = lowerBjetPt
        self._lowerBjetPt = False
        self._genMatched = genMatched
        self.isSmear = isSmear 
        self.cmssw = cmssw

        if '2016' in cmssw:
          self.Year = 2016
        if '2017' in cmssw:
          self.Year = 2017
        if '2018' in cmssw:
          self.Year = 2018

        if '2016v9HIPM' in cmssw:
          self.year_label = 0
        elif '2016v9noHIPM' in cmssw:
          self.year_label = 1
        elif '2017' in cmssw:
          self.year_label = 2
        elif '2018' in cmssw:
          self.year_label = 3
        else:
          raise Exception("no cmssw: {}".format(cmssw))

        self._syst_suffix = syst_suffix
        self._isDeltaR = True # use delta R variables instead of delta Eta and Phi
        self._include_DeltaEtaPhi = True
        # read jet energy resolution (JER) and JER scale factors and uncertainties
        # (the txt files were downloaded from https://github.com/cms-jet/JRDatabase/tree/master/textFiles/ )
        # Text files are now tarred so must extract first
        #
        if self.isSmear:
          if int(Year) == 2016:
            jerInputFileName_eta = "Summer16_25nsV1_MC_EtaResolution_AK4PFchs.txt"
            jerInputFileName_phi = "Summer16_25nsV1_MC_PhiResolution_AK4PFchs.txt"
            jerInputFileName     = "Summer16_25nsV1_MC_PtResolution_AK4PFchs.txt"
            jerUncertaintyInputFileName = "Summer16_25nsV1_MC_SF_AK4PFchs.txt"
          elif int(Year) == 2017:
            jerInputFileName_eta = "Fall17_V3_MC_EtaResolution_AK4PFchs.txt"
            jerInputFileName_phi = "Fall17_V3_MC_PhiResolution_AK4PFchs.txt"
            jerInputFileName     = "Fall17_V3_MC_PtResolution_AK4PFchs.txt"
            jerUncertaintyInputFileName = "Fall17_V3_MC_SF_AK4PFchs.txt"
          elif int(Year) == 2018:
            jerInputFileName_eta = "Autumn18_V7_MC_EtaResolution_AK4PFchs.txt"
            jerInputFileName_phi = "Autumn18_V7_MC_PhiResolution_AK4PFchs.txt"
            jerInputFileName     = "Autumn18_V7_MC_PtResolution_AK4PFchs.txt"
            jerUncertaintyInputFileName = "Autumn18_V7_MC_SF_AK4PFchs.txt"
          #
          self.jerInputArchivePath = os.environ['CMSSW_BASE'] + "/src/PhysicsTools/NanoAODTools/data/jme/"
          self.jerTag = jerInputFileName[:jerInputFileName.find('_MC_')+len('_MC')]
          self.jerArchive = tarfile.open(self.jerInputArchivePath+self.jerTag+".tgz", "r:gz")
          self.jerInputFilePath = tempfile.mkdtemp()
          self.jerArchive.extractall(self.jerInputFilePath)
          self.jerInputFileName_eta = jerInputFileName_eta
          self.jerInputFileName_phi = jerInputFileName_phi
          self.jerInputFileName     = jerInputFileName
          self.jerUncertaintyInputFileName = jerUncertaintyInputFileName
          
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
        if self.isSmear:
          print("Loading jet energy resolutions (JER) from file '%s'" % os.path.join(self.jerInputFilePath, self.jerInputFileName))
          self.jer = {}
          self.jer['Pt']  = ROOT.PyJetResolutionWrapper(os.path.join(self.jerInputFilePath, self.jerInputFileName))
          self.jer['Eta'] = ROOT.PyJetResolutionWrapper(os.path.join(self.jerInputFilePath, self.jerInputFileName_eta))
          self.jer['Phi'] = ROOT.PyJetResolutionWrapper(os.path.join(self.jerInputFilePath, self.jerInputFileName_phi))
          print("Loading JER scale factors and uncertainties from file '%s'" % os.path.join(self.jerInputFilePath, self.jerUncertaintyInputFileName))
          self.jerSF_and_Uncertainty = ROOT.PyJetResolutionScaleFactorWrapper(os.path.join(self.jerInputFilePath, self.jerUncertaintyInputFileName))

    def endJob(self):
        if self.isSmear:
          shutil.rmtree(self.jerInputFilePath)

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("nbtags_had_top_mvaCHToCB_%s"%self._syst_suffix,             "I")
        self.out.branch("nbtags_event_mvaCHToCB_%s"%self._syst_suffix,             "I")

        self.out.branch("csv_jet0_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("csv_jet1_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("csv_jet2_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("csv_jet3_mvaCHToCB_%s"%self._syst_suffix, "F")

        self.out.branch("CvB_jet0_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("CvB_jet1_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("CvB_jet2_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("CvB_jet3_mvaCHToCB_%s"%self._syst_suffix, "F")

        self.out.branch("CvL_jet0_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("CvL_jet1_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("CvL_jet2_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("CvL_jet3_mvaCHToCB_%s"%self._syst_suffix, "F")

        self.out.branch("avg_csv_had_top_%s"%self._syst_suffix, "F")
        self.out.branch("second_moment_csv_jet0_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("second_moment_csv_jet1_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("second_moment_csv_jet2_mvaCHToCB_%s"%self._syst_suffix, "F")

        #self.out.branch("jet_vector0_mvaCHToCB", "F")
        #self.out.branch("jet_vector1_mvaCHToCB", "F")
        #self.out.branch("jet_vector2_mvaCHToCB", "F")

        self.out.branch("jet_pt0_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("jet_pt1_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("jet_pt2_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("jet_pt3_mvaCHToCB_%s"%self._syst_suffix, "F")
        #self.out.branch("jet_eta0_mvaCHToCB_%s"%self._syst_suffix, "F")
        #self.out.branch("jet_eta1_mvaCHToCB_%s"%self._syst_suffix, "F")
        #self.out.branch("jet_eta2_mvaCHToCB_%s"%self._syst_suffix, "F")
        #self.out.branch("jet_eta3_mvaCHToCB_%s"%self._syst_suffix, "F")
        #self.out.branch("jet_phi0_mvaCHToCB_%s"%self._syst_suffix, "F")
        #self.out.branch("jet_phi1_mvaCHToCB_%s"%self._syst_suffix, "F")
        #self.out.branch("jet_phi2_mvaCHToCB_%s"%self._syst_suffix, "F")
        #self.out.branch("jet_phi3_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("dijet_pt0_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("dijet_pt1_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("dijet_gamma0_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("dijet_gamma1_mvaCHToCB_%s"%self._syst_suffix, "F")


        if self._isDeltaR:
          self.out.branch("dijet_deltaR0_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("dijet_deltaR1_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("dijet_deltaR2_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("dijet_deltaR3_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("dijet_deltaR4_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("dijet_deltaR5_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("Hplus_b_deltaR0_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("Hplus_b_deltaR1_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("Hplus_b_deltaR2_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("Hplus_b_deltaR3_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("Hplus_b_deltaR4_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("Hplus_b_deltaR5_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("bb_deltaR0_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("bb_deltaR1_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("bb_deltaR2_mvaCHToCB_%s"%self._syst_suffix, "F")

          #self.out.branch("dijet_ptD0_mvaCHToCB_%s"%self._syst_suffix, "F")
          #self.out.branch("dijet_ptD1_mvaCHToCB_%s"%self._syst_suffix, "F")


          self.out.branch("lj_deltaR0_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("lj_deltaR1_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("lj_deltaR2_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("lj_deltaR3_mvaCHToCB_%s"%self._syst_suffix, "F")

        if self._include_DeltaEtaPhi:
          #delta Eta
          self.out.branch("dijet_deltaEta0_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("dijet_deltaEta1_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("dijet_deltaEta2_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("dijet_deltaEta3_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("dijet_deltaEta4_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("dijet_deltaEta5_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("Hplus_b_deltaEta0_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("Hplus_b_deltaEta1_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("Hplus_b_deltaEta2_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("Hplus_b_deltaEta3_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("Hplus_b_deltaEta4_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("Hplus_b_deltaEta5_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("bb_deltaEta0_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("bb_deltaEta1_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("bb_deltaEta2_mvaCHToCB_%s"%self._syst_suffix, "F")

          #self.out.branch("dijet_ptD0_mvaCHToCB_%s"%self._syst_suffix, "F")
          #self.out.branch("dijet_ptD1_mvaCHToCB_%s"%self._syst_suffix, "F")


          self.out.branch("lj_deltaEta0_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("lj_deltaEta1_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("lj_deltaEta2_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("lj_deltaEta3_mvaCHToCB_%s"%self._syst_suffix, "F")

          #delta Phi
          self.out.branch("dijet_deltaPhi0_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("dijet_deltaPhi1_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("dijet_deltaPhi2_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("dijet_deltaPhi3_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("dijet_deltaPhi4_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("dijet_deltaPhi5_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("Hplus_b_deltaPhi0_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("Hplus_b_deltaPhi1_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("Hplus_b_deltaPhi2_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("Hplus_b_deltaPhi3_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("Hplus_b_deltaPhi4_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("Hplus_b_deltaPhi5_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("bb_deltaPhi0_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("bb_deltaPhi1_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("bb_deltaPhi2_mvaCHToCB_%s"%self._syst_suffix, "F")

          #self.out.branch("dijet_ptD0_mvaCHToCB_%s"%self._syst_suffix, "F")
          #self.out.branch("dijet_ptD1_mvaCHToCB_%s"%self._syst_suffix, "F")


          self.out.branch("lj_deltaPhi0_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("lj_deltaPhi1_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("lj_deltaPhi2_mvaCHToCB_%s"%self._syst_suffix, "F")
          self.out.branch("lj_deltaPhi3_mvaCHToCB_%s"%self._syst_suffix, "F")

        self.out.branch("min_deltaR_bb_event_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("min_deltaR_jj_event_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("had_top_pt_scalar_sum_mvaCHToCB_%s"%self._syst_suffix, "F")

        self.out.branch("HT_btagged_L_%s"%self._syst_suffix, "F")
        self.out.branch("HT_btagged_M_%s"%self._syst_suffix, "F")
        self.out.branch("HT_btagged_T_%s"%self._syst_suffix, "F")
        self.out.branch("HT_not_btagged_L_%s"%self._syst_suffix, "F")
        self.out.branch("HT_not_btagged_M_%s"%self._syst_suffix, "F")
        self.out.branch("HT_not_btagged_T_%s"%self._syst_suffix, "F")
        self.out.branch("mbb_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("mcb0_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("mcb1_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("hadronic_top_mass_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("hadronic_top_gamma_mvaCHToCB_%s"%self._syst_suffix, "F")
        self.out.branch("year_label", "F")
        
        if self._syst_suffix == 'nom':
          self.out.branch("EventNum_mvaCHToCB", "I")
          self.out.branch("btagSF", "F")


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        self.eventNum = random.randint(0,99)
        if not self.isSmear:
          return_ = self.analyze_once(event)
        else:
          nSmear = 1
          for i in range(nSmear):
            self.i_Smear = i
            return_ = self.analyze_once(event)
            if i<nSmear - 1:
              self.out.fill()
            if not return_:
              break
          
        return return_

    def analyze_once(self,event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        # select jets
        self.Jet_coll       = Collection(event, 'CleanJet')
        self.rawJet_coll    = Collection(event, 'Jet')
        #if hasattr(event, 'Lepton'):
        #  self.Lepton         = Collection(event, 'Lepton')
        #else:
        #  #XXX dumy
        #  self.Lepton = self.Jet_coll
        self.Lepton         = Collection(event, 'Lepton')

        #XXX set pt eta cut by years
        ptcut = 25.
        if self.cmssw == "Full2016v9HIPM":
          absetacut = 2.4
          self.csvcut_L    = 0.0480
          self.csvcut_M    = 0.2489
          self.csvcut_T    = 0.6377
        elif self.cmssw == "Full2016v9noHIPM":
          absetacut = 2.4
          self.csvcut_L    = 0.0508
          self.csvcut_M    = 0.2598
          self.csvcut_T    = 0.6502
        elif self.cmssw == "Full2017v9":
          absetacut = 2.4
          self.csvcut_L    = 0.0532
          self.csvcut_M    = 0.3040
          self.csvcut_T    = 0.7476
        else:
          absetacut = 2.4
          self.csvcut_L    = 0.0490
          self.csvcut_M    = 0.2783
          self.csvcut_T    = 0.7100
        if self.isSmear:
          good_jets, good_jets_idx = self.get_jets_vectors(absetacut, ptcut, event.fixedGridRhoFastjetAll)
        else:
          good_jets, good_jets_idx = self.get_jets_vectors(absetacut, ptcut, 0)

        # return if not more than 4 jets
        if len(good_jets) < 4:
          return True



        # get minimum deltaR b-tagged pair among all possible b-jet combination
        min_deltaR_bb_event = self.min_deltaR_bb(good_jets, good_jets_idx)
        min_deltaR_jj_event = self.min_deltaR_jj(good_jets, good_jets_idx)



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
          if self._genMatched:
            hadronic_top_b_jet_idx_nom = getattr(event, "had_top_b_matched_jet_idx"        )
            leptonic_top_b_jet_idx_nom = getattr(event, "lep_top_b_matched_jet_idx"        )
            w_ch_up_type_jet_idx_nom   = getattr(event, "had_top_up_type_matched_jet_idx"  )
            w_ch_down_type_jet_idx_nom = getattr(event, "had_top_down_type_matched_jet_idx")
          else:
            hadronic_top_b_jet_idx_nom = getattr(event, 'hadronic_top_b_jet_idx_%s'%self._syst_suffix)
            leptonic_top_b_jet_idx_nom = getattr(event, 'leptonic_top_b_jet_idx_%s'%self._syst_suffix)
            w_ch_up_type_jet_idx_nom   = getattr(event, 'w_ch_up_type_jet_idx_%s'%self._syst_suffix)
            w_ch_down_type_jet_idx_nom = getattr(event, 'w_ch_down_type_jet_idx_%s'%self._syst_suffix)

            hadronic_top_b_jet_pull_nom = getattr(event, 'hadronic_top_b_jet_pull_%s'%self._syst_suffix)
            w_ch_up_type_jet_pull_nom   = getattr(event, 'w_ch_up_type_jet_pull_%s'%self._syst_suffix)
            w_ch_down_type_jet_pull_nom = getattr(event, 'w_ch_down_type_jet_pull_%s'%self._syst_suffix)
            
          self.nbtags_event = getattr(event,'nbtagsCleanJet_{}'.format(self._syst_suffix))


          if not (hadronic_top_b_jet_idx_nom >= 0 and\
                  leptonic_top_b_jet_idx_nom >= 0 and\
                  w_ch_up_type_jet_idx_nom   >= 0 and\
                  w_ch_down_type_jet_idx_nom >= 0
                 ):
            return True

          had_top_jets_idx = [
                            w_ch_up_type_jet_idx_nom,  
                            w_ch_down_type_jet_idx_nom,
                            hadronic_top_b_jet_idx_nom,
                          ]

          leptonic_top_jets_idx = [ leptonic_top_b_jet_idx_nom
                  ]

          # find index of element in good_jets_idx
          try:
            good_jets_idx_mask = [
                                   good_jets_idx.index(idx) for idx in had_top_jets_idx
                                 ]
            leptonic_top_jets_idx_mask = good_jets_idx.index(leptonic_top_jets_idx[0])
          except ValueError:
            if self._genMatched:
              return True
            else:
              raise RuntimeWarning('index is not found in good_jets_idx')

          
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
          self.nbtags_had_top =  2 if getattr(event,'down_type_jet_b_tagged_{}'.format(self._syst_suffix))>0.5 else 1

          # pt sum of hadronic top jets
          HT_btagged_L, HT_not_btagged_L = self.get_HT_btagged(good_jets_idx, self.csvcut_L)
          HT_btagged_M, HT_not_btagged_M = self.get_HT_btagged(good_jets_idx, self.csvcut_M)
          HT_btagged_T, HT_not_btagged_T = self.get_HT_btagged(good_jets_idx, self.csvcut_T)


          pull_cut = False
          if pull_cut:
            if not (abs(hadronic_top_b_jet_pull_nom)<2 and\
                    abs(w_ch_up_type_jet_pull_nom  )<2 and\
                    abs(w_ch_down_type_jet_pull_nom)<2\
                   ):
              return True


        # otherwise, find jet pairs
        else:
          return True

        # sort this jet pair in leading csv ordering
        # not sorted in csv order, it increase ambiguity in b jet order in H+ Mar21, 2023
        #nearest_top_mass_pair_jetIdx.sort(key=lambda idx: self.rawJet_coll[good_jets_idx[idx]].btagDeepFlavB, reverse=True)

        if self.nbtags_event < 2:
          return True
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

        csv_jet0 = self.rawJet_coll[idx0].btagDeepFlavB #leading csv
        csv_jet1 = self.rawJet_coll[idx1].btagDeepFlavB #2nd leading csv
        csv_jet2 = self.rawJet_coll[idx2].btagDeepFlavB #smallest csv
        csv_jet3 = self.rawJet_coll[leptonic_top_jets_idx[0]].btagDeepFlavB #leptonic csv

        if csv_jet2 < self.csvcut_M:
            print("csv_jet2 < self.csvcut_M")
        if csv_jet3 < self.csvcut_M:
            print("csv_jet3 < self.csvcut_M")

        CvB_jet0 = self.rawJet_coll[idx0].btagDeepFlavCvB #leading csv
        CvB_jet1 = self.rawJet_coll[idx1].btagDeepFlavCvB #2nd leading csv
        CvB_jet2 = self.rawJet_coll[idx2].btagDeepFlavCvB #smallest csv
        CvB_jet3 = self.rawJet_coll[leptonic_top_jets_idx[0]].btagDeepFlavCvB #leptonic csv

        CvL_jet0 = self.rawJet_coll[idx0].btagDeepFlavCvL #leading csv
        CvL_jet1 = self.rawJet_coll[idx1].btagDeepFlavCvL #2nd leading csv
        CvL_jet2 = self.rawJet_coll[idx2].btagDeepFlavCvL #smallest csv
        CvL_jet3 = self.rawJet_coll[leptonic_top_jets_idx[0]].btagDeepFlavCvL #leptonic csv

        avg_csv_had_top     = (csv_jet0+csv_jet1+csv_jet2)/3
        second_moment_csv_jet0 = (csv_jet0-avg_csv_had_top)*(csv_jet0-avg_csv_had_top)
        second_moment_csv_jet1 = (csv_jet1-avg_csv_had_top)*(csv_jet1-avg_csv_had_top)
        second_moment_csv_jet2 = (csv_jet2-avg_csv_had_top)*(csv_jet2-avg_csv_had_top)

        #
        nbtags_had_top = self.nbtags_had_top
        #
        #

        jet_vector0 = self.get_jet_vector(idx0) #good_jets[nearest_top_mass_pair_jetIdx[0]] # H+ c
        jet_vector1 = self.get_jet_vector(idx1) #good_jets[nearest_top_mass_pair_jetIdx[1]] # H+ b
        jet_vector2 = self.get_jet_vector(idx2) #good_jets[nearest_top_mass_pair_jetIdx[2]] # top b
        jet_vector3 = self.get_jet_vector(leptonic_top_jets_idx[0])#good_leptonic_top_jet  #leptonic_top_jets_idx
        
        #is_high_mass_fitter = (jet_pt1 < jet_pt2) and (jet_pt1 < jet_pt0)

        jet_pt0 = jet_vector0.Pt() * self.rawJet_coll[idx0].cRegCorr #XXX 24.04.10, bug fix: cRegRes -> cRegCorr
        jet_pt1 = jet_vector1.Pt() * self.rawJet_coll[idx1].bRegCorr
        jet_pt2 = jet_vector2.Pt() * self.rawJet_coll[idx2].bRegCorr
        jet_pt3 = jet_vector3.Pt() * self.rawJet_coll[leptonic_top_jets_idx[0]].bRegCorr
        jet_eta0 = jet_vector0.Eta()
        jet_eta1 = jet_vector1.Eta()
        jet_eta2 = jet_vector2.Eta()
        jet_eta3 = jet_vector3.Eta()
        jet_phi0 = jet_vector0.Phi()
        jet_phi1 = jet_vector1.Phi()
        jet_phi2 = jet_vector2.Phi()
        jet_phi3 = jet_vector3.Phi()

        dijet_pt0 = (jet_vector0 + jet_vector1).Pt()
        dijet_pt1 = (jet_vector0 + jet_vector2).Pt()
        dijet_E0  = (jet_vector0 + jet_vector1).E()
        dijet_E1  = (jet_vector0 + jet_vector2).E()
        dijet_M0  = (jet_vector0 + jet_vector1).M()
        dijet_M1  = (jet_vector0 + jet_vector2).M()
        dijet_gamma0 = dijet_E0 / dijet_M0
        dijet_gamma1 = dijet_E1 / dijet_M1

        lepton_vector = TLorentzVector()
        lepton_vector.SetPtEtaPhiM(self.Lepton[0].pt, self.Lepton[0].eta, self.Lepton[0].phi, 0.)

        # jet_vector2 is 3rd leading csv jet
        # consider this jet as a jet comming from c
        # dijet_deltaR0/1 variables are deltaR between c jet and b jet comming from H+
        # 0,1 are labeled in pT order
        #
        #
        dijet_deltaR0     = jet_vector0.DeltaR(jet_vector1)
        dijet_deltaR1     = jet_vector0.DeltaR(jet_vector2)
        # flip with jet_pt2 and jet_pt3 
        dijet_deltaR2     = jet_vector0.DeltaR(jet_vector1)
        dijet_deltaR3     = jet_vector0.DeltaR(jet_vector3)
        # flip with jet_pt1 and jet_pt3
        dijet_deltaR4     = jet_vector0.DeltaR(jet_vector3)
        dijet_deltaR5     = jet_vector0.DeltaR(jet_vector2)
        Hplus_b_deltaR0   = jet_vector2.DeltaR(jet_vector0+jet_vector1)
        Hplus_b_deltaR1   = jet_vector1.DeltaR(jet_vector0+jet_vector2)
        # flip with jet_pt2 and jet_pt3 
        Hplus_b_deltaR2   = jet_vector3.DeltaR(jet_vector0+jet_vector1)
        Hplus_b_deltaR3   = jet_vector1.DeltaR(jet_vector0+jet_vector3)
        # flip with jet_pt1 and jet_pt3
        Hplus_b_deltaR4   = jet_vector2.DeltaR(jet_vector0+jet_vector3)
        Hplus_b_deltaR5   = jet_vector3.DeltaR(jet_vector0+jet_vector2)

        bb_deltaR0         = jet_vector1.DeltaR(jet_vector2)
        # flip with jet_pt2 and jet_pt3 
        bb_deltaR1         = jet_vector1.DeltaR(jet_vector3)
        # flip with jet_pt1 and jet_pt3
        bb_deltaR2         = jet_vector3.DeltaR(jet_vector2)

        lj_deltaR0        = lepton_vector.DeltaR(jet_vector0)
        lj_deltaR1        = lepton_vector.DeltaR(jet_vector1)
        lj_deltaR2        = lepton_vector.DeltaR(jet_vector2)
        lj_deltaR3        = lepton_vector.DeltaR(jet_vector3)

        # delta Eta
        DeltaEta = lambda vec_1, vec_2: abs(vec_1.Eta() - vec_2.Eta())

        dijet_deltaEta0     = DeltaEta(jet_vector0,jet_vector1)
        dijet_deltaEta1     = DeltaEta(jet_vector0,jet_vector2)
        # flip with jet_pt2 and jet_pt3 
        dijet_deltaEta2     = DeltaEta(jet_vector0,jet_vector1)
        dijet_deltaEta3     = DeltaEta(jet_vector0,jet_vector3)
        # flip with jet_pt1 and jet_pt3
        dijet_deltaEta4     = DeltaEta(jet_vector0,jet_vector3)
        dijet_deltaEta5     = DeltaEta(jet_vector0,jet_vector2)
        Hplus_b_deltaEta0   = DeltaEta(jet_vector2,jet_vector0+jet_vector1)
        Hplus_b_deltaEta1   = DeltaEta(jet_vector1,jet_vector0+jet_vector2)
        # flip with jet_pt2 and jet_pt3 
        Hplus_b_deltaEta2   = DeltaEta(jet_vector3,jet_vector0+jet_vector1)
        Hplus_b_deltaEta3   = DeltaEta(jet_vector1,jet_vector0+jet_vector3)
        # flip with jet_pt1 and jet_pt3
        Hplus_b_deltaEta4   = DeltaEta(jet_vector2,jet_vector0+jet_vector3)
        Hplus_b_deltaEta5   = DeltaEta(jet_vector3,jet_vector0+jet_vector2)

        bb_deltaEta0         = DeltaEta(jet_vector1,jet_vector2)
        # flip with jet_pt2 and jet_pt3 
        bb_deltaEta1         = DeltaEta(jet_vector1,jet_vector3)
        # flip with jet_pt1 and jet_pt3
        bb_deltaEta2         = DeltaEta(jet_vector3,jet_vector2)

        #dijet_ptD0        = dijet_deltaEta0
        #dijet_ptD0        *= (jet_vector2+jet_vector0).Pt() if jet_pt0 >= jet_pt1 else (jet_vector2+jet_vector1).Pt()
        #dijet_ptD1        = dijet_deltaEta1
        #dijet_ptD1        *= (jet_vector2+jet_vector1).Pt() if jet_pt0 >= jet_pt1 else (jet_vector2+jet_vector0).Pt()

        lj_deltaEta0        = DeltaEta(lepton_vector,jet_vector0)
        lj_deltaEta1        = DeltaEta(lepton_vector,jet_vector1)
        lj_deltaEta2        = DeltaEta(lepton_vector,jet_vector2)
        lj_deltaEta3        = DeltaEta(lepton_vector,jet_vector3)

        # delta phi
        dijet_deltaPhi0     = jet_vector0.DeltaPhi(jet_vector1)
        dijet_deltaPhi1     = jet_vector0.DeltaPhi(jet_vector2)
        # flip with jet_pt2 and jet_pt3 
        dijet_deltaPhi2     = jet_vector0.DeltaPhi(jet_vector1)
        dijet_deltaPhi3     = jet_vector0.DeltaPhi(jet_vector3)
        # flip with jet_pt1 and jet_pt3
        dijet_deltaPhi4     = jet_vector0.DeltaPhi(jet_vector3)
        dijet_deltaPhi5     = jet_vector0.DeltaPhi(jet_vector2)
        Hplus_b_deltaPhi0   = jet_vector2.DeltaPhi(jet_vector0+jet_vector1)
        Hplus_b_deltaPhi1   = jet_vector1.DeltaPhi(jet_vector0+jet_vector2)
        # flip with jet_pt2 and jet_pt3 
        Hplus_b_deltaPhi2   = jet_vector3.DeltaPhi(jet_vector0+jet_vector1)
        Hplus_b_deltaPhi3   = jet_vector1.DeltaPhi(jet_vector0+jet_vector3)
        # flip with jet_pt1 and jet_pt3
        Hplus_b_deltaPhi4   = jet_vector2.DeltaPhi(jet_vector0+jet_vector3)
        Hplus_b_deltaPhi5   = jet_vector3.DeltaPhi(jet_vector0+jet_vector2)

        bb_deltaPhi0         = jet_vector1.DeltaPhi(jet_vector2)
        # flip with jet_pt2 and jet_pt3 
        bb_deltaPhi1         = jet_vector1.DeltaPhi(jet_vector3)
        # flip with jet_pt1 and jet_pt3
        bb_deltaPhi2         = jet_vector3.DeltaPhi(jet_vector2)

        #dijet_ptD0        = dijet_deltaPhi0
        #dijet_ptD0        *= (jet_vector2+jet_vector0).Pt() if jet_pt0 >= jet_pt1 else (jet_vector2+jet_vector1).Pt()
        #dijet_ptD1        = dijet_deltaPhi1
        #dijet_ptD1        *= (jet_vector2+jet_vector1).Pt() if jet_pt0 >= jet_pt1 else (jet_vector2+jet_vector0).Pt()

        lj_deltaPhi0        = lepton_vector.DeltaPhi(jet_vector0)
        lj_deltaPhi1        = lepton_vector.DeltaPhi(jet_vector1)
        lj_deltaPhi2        = lepton_vector.DeltaPhi(jet_vector2)
        lj_deltaPhi3        = lepton_vector.DeltaPhi(jet_vector3)







        had_top_pt_scalar_sum = jet_pt0 + jet_pt1 + jet_pt2
        mbb  = ( jet_vector1 + jet_vector2 ).M()
        mcb0 = ( jet_vector0 + jet_vector1 ).M()
        mcb1 = ( jet_vector0 + jet_vector2 ).M()
        
        hadronic_top_mass = ( jet_vector0 + jet_vector1 + jet_vector2 ).M()
        hadronic_top_E = ( jet_vector0 + jet_vector1 + jet_vector2 ).E()
        hadronic_top_gamma = hadronic_top_E / hadronic_top_mass

        #btag SF
        btagSF = 1.
        if hasattr(self.rawJet_coll[0], "btagSF_deepjet_shape"):
          for jet in self.Jet_coll:
            if jet.pt < 25. or abs(jet.eta) > 2.4:
              continue
            btagSF *= self.rawJet_coll[jet.jetIdx].btagSF_deepjet_shape

        self.out.fillBranch("nbtags_had_top_mvaCHToCB_%s"%self._syst_suffix, nbtags_had_top)
        self.out.fillBranch("nbtags_event_mvaCHToCB_%s"%self._syst_suffix, self.nbtags_event)

        self.out.fillBranch("csv_jet0_mvaCHToCB_%s"%self._syst_suffix, csv_jet0)
        self.out.fillBranch("csv_jet1_mvaCHToCB_%s"%self._syst_suffix, csv_jet1)
        self.out.fillBranch("csv_jet2_mvaCHToCB_%s"%self._syst_suffix, csv_jet2)
        self.out.fillBranch("csv_jet3_mvaCHToCB_%s"%self._syst_suffix, csv_jet3)

        self.out.fillBranch("CvB_jet0_mvaCHToCB_%s"%self._syst_suffix, CvB_jet0)
        self.out.fillBranch("CvB_jet1_mvaCHToCB_%s"%self._syst_suffix, CvB_jet1)
        self.out.fillBranch("CvB_jet2_mvaCHToCB_%s"%self._syst_suffix, CvB_jet2)
        self.out.fillBranch("CvB_jet3_mvaCHToCB_%s"%self._syst_suffix, CvB_jet3)

        self.out.fillBranch("CvL_jet0_mvaCHToCB_%s"%self._syst_suffix, CvL_jet0)
        self.out.fillBranch("CvL_jet1_mvaCHToCB_%s"%self._syst_suffix, CvL_jet1)
        self.out.fillBranch("CvL_jet2_mvaCHToCB_%s"%self._syst_suffix, CvL_jet2)
        self.out.fillBranch("CvL_jet3_mvaCHToCB_%s"%self._syst_suffix, CvL_jet3)

        self.out.fillBranch("avg_csv_had_top_%s"%self._syst_suffix, avg_csv_had_top)
        self.out.fillBranch("second_moment_csv_jet0_mvaCHToCB_%s"%self._syst_suffix, second_moment_csv_jet0)
        self.out.fillBranch("second_moment_csv_jet1_mvaCHToCB_%s"%self._syst_suffix, second_moment_csv_jet1)
        self.out.fillBranch("second_moment_csv_jet2_mvaCHToCB_%s"%self._syst_suffix, second_moment_csv_jet2)

        #self.out.fillBranch("jet_vector0_mvaCHToCB", jet_vector0)
        #self.out.fillBranch("jet_vector1_mvaCHToCB", jet_vector1)
        #self.out.fillBranch("jet_vector2_mvaCHToCB", jet_vector2)
        self.out.fillBranch("jet_pt0_mvaCHToCB_%s"%self._syst_suffix, jet_pt0)
        self.out.fillBranch("jet_pt1_mvaCHToCB_%s"%self._syst_suffix, jet_pt1)
        self.out.fillBranch("jet_pt2_mvaCHToCB_%s"%self._syst_suffix, jet_pt2)
        self.out.fillBranch("jet_pt3_mvaCHToCB_%s"%self._syst_suffix, jet_pt3)
        #self.out.fillBranch("jet_eta0_mvaCHToCB_%s"%self._syst_suffix, jet_eta0)
        #self.out.fillBranch("jet_eta1_mvaCHToCB_%s"%self._syst_suffix, jet_eta1)
        #self.out.fillBranch("jet_eta2_mvaCHToCB_%s"%self._syst_suffix, jet_eta2)
        #self.out.fillBranch("jet_eta3_mvaCHToCB_%s"%self._syst_suffix, jet_eta3)
        #self.out.fillBranch("jet_phi0_mvaCHToCB_%s"%self._syst_suffix, jet_phi0)
        #self.out.fillBranch("jet_phi1_mvaCHToCB_%s"%self._syst_suffix, jet_phi1)
        #self.out.fillBranch("jet_phi2_mvaCHToCB_%s"%self._syst_suffix, jet_phi2)
        #self.out.fillBranch("jet_phi3_mvaCHToCB_%s"%self._syst_suffix, jet_phi3)
        self.out.fillBranch("dijet_pt0_mvaCHToCB_%s"%self._syst_suffix, dijet_pt0)
        self.out.fillBranch("dijet_pt1_mvaCHToCB_%s"%self._syst_suffix, dijet_pt1)
        self.out.fillBranch("dijet_gamma0_mvaCHToCB_%s"%self._syst_suffix, dijet_gamma0)
        self.out.fillBranch("dijet_gamma1_mvaCHToCB_%s"%self._syst_suffix, dijet_gamma1)

        if self._isDeltaR:
          self.out.fillBranch("dijet_deltaR0_mvaCHToCB_%s"%self._syst_suffix, dijet_deltaR0)
          self.out.fillBranch("dijet_deltaR1_mvaCHToCB_%s"%self._syst_suffix, dijet_deltaR1)
          self.out.fillBranch("dijet_deltaR2_mvaCHToCB_%s"%self._syst_suffix, dijet_deltaR2)
          self.out.fillBranch("dijet_deltaR3_mvaCHToCB_%s"%self._syst_suffix, dijet_deltaR3)
          self.out.fillBranch("dijet_deltaR4_mvaCHToCB_%s"%self._syst_suffix, dijet_deltaR4)
          self.out.fillBranch("dijet_deltaR5_mvaCHToCB_%s"%self._syst_suffix, dijet_deltaR5)
          self.out.fillBranch("Hplus_b_deltaR0_mvaCHToCB_%s"%self._syst_suffix, Hplus_b_deltaR0)
          self.out.fillBranch("Hplus_b_deltaR1_mvaCHToCB_%s"%self._syst_suffix, Hplus_b_deltaR1)
          self.out.fillBranch("Hplus_b_deltaR2_mvaCHToCB_%s"%self._syst_suffix, Hplus_b_deltaR2)
          self.out.fillBranch("Hplus_b_deltaR3_mvaCHToCB_%s"%self._syst_suffix, Hplus_b_deltaR3)
          self.out.fillBranch("Hplus_b_deltaR4_mvaCHToCB_%s"%self._syst_suffix, Hplus_b_deltaR4)
          self.out.fillBranch("Hplus_b_deltaR5_mvaCHToCB_%s"%self._syst_suffix, Hplus_b_deltaR5)
          self.out.fillBranch("bb_deltaR0_mvaCHToCB_%s"%self._syst_suffix, bb_deltaR0)
          self.out.fillBranch("bb_deltaR1_mvaCHToCB_%s"%self._syst_suffix, bb_deltaR1)
          self.out.fillBranch("bb_deltaR2_mvaCHToCB_%s"%self._syst_suffix, bb_deltaR2)

          #self.out.fillBranch("dijet_ptD0_mvaCHToCB_%s"%self._syst_suffix, dijet_ptD0)
          #self.out.fillBranch("dijet_ptD1_mvaCHToCB_%s"%self._syst_suffix, dijet_ptD1)

          self.out.fillBranch("lj_deltaR0_mvaCHToCB_%s"%self._syst_suffix, lj_deltaR0)
          self.out.fillBranch("lj_deltaR1_mvaCHToCB_%s"%self._syst_suffix, lj_deltaR1)
          self.out.fillBranch("lj_deltaR2_mvaCHToCB_%s"%self._syst_suffix, lj_deltaR2)
          self.out.fillBranch("lj_deltaR3_mvaCHToCB_%s"%self._syst_suffix, lj_deltaR3)


        if self._include_DeltaEtaPhi:
          # delta Eta
          self.out.fillBranch("dijet_deltaEta0_mvaCHToCB_%s"%self._syst_suffix, dijet_deltaEta0)
          self.out.fillBranch("dijet_deltaEta1_mvaCHToCB_%s"%self._syst_suffix, dijet_deltaEta1)
          self.out.fillBranch("dijet_deltaEta2_mvaCHToCB_%s"%self._syst_suffix, dijet_deltaEta2)
          self.out.fillBranch("dijet_deltaEta3_mvaCHToCB_%s"%self._syst_suffix, dijet_deltaEta3)
          self.out.fillBranch("dijet_deltaEta4_mvaCHToCB_%s"%self._syst_suffix, dijet_deltaEta4)
          self.out.fillBranch("dijet_deltaEta5_mvaCHToCB_%s"%self._syst_suffix, dijet_deltaEta5)
          self.out.fillBranch("Hplus_b_deltaEta0_mvaCHToCB_%s"%self._syst_suffix, Hplus_b_deltaEta0)
          self.out.fillBranch("Hplus_b_deltaEta1_mvaCHToCB_%s"%self._syst_suffix, Hplus_b_deltaEta1)
          self.out.fillBranch("Hplus_b_deltaEta2_mvaCHToCB_%s"%self._syst_suffix, Hplus_b_deltaEta2)
          self.out.fillBranch("Hplus_b_deltaEta3_mvaCHToCB_%s"%self._syst_suffix, Hplus_b_deltaEta3)
          self.out.fillBranch("Hplus_b_deltaEta4_mvaCHToCB_%s"%self._syst_suffix, Hplus_b_deltaEta4)
          self.out.fillBranch("Hplus_b_deltaEta5_mvaCHToCB_%s"%self._syst_suffix, Hplus_b_deltaEta5)
          self.out.fillBranch("bb_deltaEta0_mvaCHToCB_%s"%self._syst_suffix, bb_deltaEta0)
          self.out.fillBranch("bb_deltaEta1_mvaCHToCB_%s"%self._syst_suffix, bb_deltaEta1)
          self.out.fillBranch("bb_deltaEta2_mvaCHToCB_%s"%self._syst_suffix, bb_deltaEta2)

          #self.out.fillBranch("dijet_ptD0_mvaCHToCB_%s"%self._syst_suffix, dijet_ptD0)
          #self.out.fillBranch("dijet_ptD1_mvaCHToCB_%s"%self._syst_suffix, dijet_ptD1)

          self.out.fillBranch("lj_deltaEta0_mvaCHToCB_%s"%self._syst_suffix, lj_deltaEta0)
          self.out.fillBranch("lj_deltaEta1_mvaCHToCB_%s"%self._syst_suffix, lj_deltaEta1)
          self.out.fillBranch("lj_deltaEta2_mvaCHToCB_%s"%self._syst_suffix, lj_deltaEta2)
          self.out.fillBranch("lj_deltaEta3_mvaCHToCB_%s"%self._syst_suffix, lj_deltaEta3)

          # delta Phi
          self.out.fillBranch("dijet_deltaPhi0_mvaCHToCB_%s"%self._syst_suffix, dijet_deltaPhi0)
          self.out.fillBranch("dijet_deltaPhi1_mvaCHToCB_%s"%self._syst_suffix, dijet_deltaPhi1)
          self.out.fillBranch("dijet_deltaPhi2_mvaCHToCB_%s"%self._syst_suffix, dijet_deltaPhi2)
          self.out.fillBranch("dijet_deltaPhi3_mvaCHToCB_%s"%self._syst_suffix, dijet_deltaPhi3)
          self.out.fillBranch("dijet_deltaPhi4_mvaCHToCB_%s"%self._syst_suffix, dijet_deltaPhi4)
          self.out.fillBranch("dijet_deltaPhi5_mvaCHToCB_%s"%self._syst_suffix, dijet_deltaPhi5)
          self.out.fillBranch("Hplus_b_deltaPhi0_mvaCHToCB_%s"%self._syst_suffix, Hplus_b_deltaPhi0)
          self.out.fillBranch("Hplus_b_deltaPhi1_mvaCHToCB_%s"%self._syst_suffix, Hplus_b_deltaPhi1)
          self.out.fillBranch("Hplus_b_deltaPhi2_mvaCHToCB_%s"%self._syst_suffix, Hplus_b_deltaPhi2)
          self.out.fillBranch("Hplus_b_deltaPhi3_mvaCHToCB_%s"%self._syst_suffix, Hplus_b_deltaPhi3)
          self.out.fillBranch("Hplus_b_deltaPhi4_mvaCHToCB_%s"%self._syst_suffix, Hplus_b_deltaPhi4)
          self.out.fillBranch("Hplus_b_deltaPhi5_mvaCHToCB_%s"%self._syst_suffix, Hplus_b_deltaPhi5)
          self.out.fillBranch("bb_deltaPhi0_mvaCHToCB_%s"%self._syst_suffix, bb_deltaPhi0)
          self.out.fillBranch("bb_deltaPhi1_mvaCHToCB_%s"%self._syst_suffix, bb_deltaPhi1)
          self.out.fillBranch("bb_deltaPhi2_mvaCHToCB_%s"%self._syst_suffix, bb_deltaPhi2)

          #self.out.fillBranch("dijet_ptD0_mvaCHToCB_%s"%self._syst_suffix, dijet_ptD0)
          #self.out.fillBranch("dijet_ptD1_mvaCHToCB_%s"%self._syst_suffix, dijet_ptD1)

          self.out.fillBranch("lj_deltaPhi0_mvaCHToCB_%s"%self._syst_suffix, lj_deltaPhi0)
          self.out.fillBranch("lj_deltaPhi1_mvaCHToCB_%s"%self._syst_suffix, lj_deltaPhi1)
          self.out.fillBranch("lj_deltaPhi2_mvaCHToCB_%s"%self._syst_suffix, lj_deltaPhi2)
          self.out.fillBranch("lj_deltaPhi3_mvaCHToCB_%s"%self._syst_suffix, lj_deltaPhi3)


        self.out.fillBranch("min_deltaR_bb_event_mvaCHToCB_%s"%self._syst_suffix, min_deltaR_bb_event)
        self.out.fillBranch("min_deltaR_jj_event_mvaCHToCB_%s"%self._syst_suffix, min_deltaR_jj_event)

        self.out.fillBranch("had_top_pt_scalar_sum_mvaCHToCB_%s"%self._syst_suffix, had_top_pt_scalar_sum)

        self.out.fillBranch("HT_btagged_L_%s"%self._syst_suffix, HT_btagged_L)
        self.out.fillBranch("HT_btagged_M_%s"%self._syst_suffix, HT_btagged_M)
        self.out.fillBranch("HT_btagged_T_%s"%self._syst_suffix, HT_btagged_T)
        self.out.fillBranch("HT_not_btagged_L_%s"%self._syst_suffix, HT_not_btagged_L)
        self.out.fillBranch("HT_not_btagged_M_%s"%self._syst_suffix, HT_not_btagged_M)
        self.out.fillBranch("HT_not_btagged_T_%s"%self._syst_suffix, HT_not_btagged_T)
        self.out.fillBranch("mbb_mvaCHToCB_%s"%self._syst_suffix, mbb)
        self.out.fillBranch("mcb0_mvaCHToCB_%s"%self._syst_suffix, mcb0)
        self.out.fillBranch("mcb1_mvaCHToCB_%s"%self._syst_suffix, mcb1)
        self.out.fillBranch("hadronic_top_mass_mvaCHToCB_%s"  % self._syst_suffix, hadronic_top_mass)
        self.out.fillBranch("hadronic_top_gamma_mvaCHToCB_%s" % self._syst_suffix, hadronic_top_gamma)
        self.out.fillBranch("year_label", self.year_label)
        if self._syst_suffix == 'nom':
          self.out.fillBranch("EventNum_mvaCHToCB", self.eventNum)
          self.out.fillBranch("btagSF", btagSF)

        return True



    def findJetPtSystAttr(self,object_,suffix_):
        if "unclustEn" in self._syst_suffix:
          syst_suffix = "{}_nom".format(suffix_)
        elif "RegCorr" in self._syst_suffix:
          syst_suffix = "{}_nom".format(suffix_)
        elif "RegRes" in self._syst_suffix:
          syst_suffix = "{}_nom".format(suffix_)
        else:
          syst_suffix = "{}_{}".format(suffix_, self._syst_suffix)
        return getattr(object_,syst_suffix)




    def get_jet_vector(self, idx):
        pt, eta, phi, mass = self.findJetPtSystAttr(self.rawJet_coll[idx],"pt"), self.rawJet_coll[idx].eta, self.rawJet_coll[idx].phi, self.findJetPtSystAttr(self.rawJet_coll[idx], "mass")
        #
        vec = TLorentzVector()
        vec.SetPtEtaPhiM(pt, eta, phi, mass)
        return vec


    def get_jets_vectors(self, absetacut, ptcut, rho):
        '''
        Returns a list of 4-momenta for jets
                                                                                                                    
        Inserted here an eta interval and pt range cut to avoid using the jets in a specified region for 
        tagging. 
        '''
        jets = []
        coll_idx = []
        for ijnf in range(len(self.Jet_coll)):
          jetindex = self.Jet_coll[ijnf].jetIdx
          # index in the original Jet collection

          pt, eta, phi, mass = self.findJetPtSystAttr(self.rawJet_coll[self.Jet_coll[ijnf].jetIdx], "pt"),\
                      self.Jet_coll[ijnf].eta,\
                      self.Jet_coll[ijnf].phi,\
                      self.findJetPtSystAttr(self.rawJet_coll[self.Jet_coll[ijnf].jetIdx], "mass")

          csv, puId_M = self.rawJet_coll[jetindex].btagDeepFlavB , self.rawJet_coll[jetindex].puId
                                                                                                                  
          passabsetacut = True
          if abs(eta) >= absetacut or pt <= ptcut: 
            passabsetacut = False
          if pt > 25 and pt<=30:
            pass
            #if not self._lowerBjetPt:
            #  passabsetacut = False
            #if not (puId_M & (1<<1)):
            #  passabsetacut = False
            #if csv <= self.csvcut_M:
            #  passabsetacut = False
          #if self.debug: 
          #  print "Jet index: ", jetindex, " CUT > pt:", pt ," eta:", eta, " phi:", phi, " mass:", mass
          if not passabsetacut : continue
          
          

          p = pt * cosh(eta)
          en = sqrt(p**2 + mass**2)
          vec = TLorentzVector()
          vec.SetPtEtaPhiE(pt, eta, phi, en)
          # smear resolution
          if self.isSmear:
            # do not smear at first iteration for smearing
            if not self.i_Smear == 0:
              jetPtResolution_, jetEtaResolution_, jetPhiResolution_ = self.getJetPtResolution(vec, rho)

              # generate random number
              rand = [random.gauss(0,1), random.gauss(0,1), random.gauss(0,1)]
              # truncate random normal
              rand = [ rand_ if rand_ > -2. else -2  for rand_ in rand  ]
              rand = [ rand_ if rand_ <  2. else  2. for rand_ in rand  ]
              var = [jetPtResolution_*rand[0], jetEtaResolution_*rand[1], jetPhiResolution_*rand[2]]
              vec.SetPtEtaPhiE(pt*(1+var[0]), eta*(1+var[1]), phi*(1+var[2]), en)
          # check if different from the previous one
          #if self.debug:
          #print "Jet index: ", jetindex, "> pt:", pt, "> pt_res:", pt*(1+var[0]), " eta:", eta, " eta_res:", eta*(1+var[1]), " phi:", phi, " phi_res:", phi*(1+var[2])," mass:", mass
          jets.append(vec)
          coll_idx.append(jetindex)
        return jets, coll_idx


    def exist_variables_in_skimTree(self, event):
        # check if variables exist in skimed tree
        # which kinFitTTSemiLep module produce
        # 
        # 'hadronic_top_b_jet_idx_nom'
        # 'leptonic_top_b_jet_idx_nom'
        # 'w_ch_up_type_jet_idx_nom'
        # 'w_ch_down_type_jet_idx_nom'
        #
        # these variables return index of Jet assigned as top candidate
        #
        #
        if self._genMatched:
          return hasattr(event,"had_top_b_matched_jet_idx"        ) and\
                 hasattr(event,"lep_top_b_matched_jet_idx"        ) and\
                 hasattr(event,"had_top_up_type_matched_jet_idx"  ) and\
                 hasattr(event,"had_top_down_type_matched_jet_idx")
        else:
          return hasattr(event,'hadronic_top_b_jet_idx_%s'%self._syst_suffix) and\
                 hasattr(event,'leptonic_top_b_jet_idx_%s'%self._syst_suffix) and\
                 hasattr(event,'w_ch_up_type_jet_idx_%s'%self._syst_suffix) and\
                 hasattr(event,'w_ch_down_type_jet_idx_%s'%self._syst_suffix) and\
                 hasattr(event,'hadronic_top_b_jet_pull_%s'%self._syst_suffix) and\
                 hasattr(event,'w_ch_up_type_jet_pull_%s'%self._syst_suffix) and\
                 hasattr(event,'w_ch_down_type_jet_pull_%s'%self._syst_suffix)


    def nearest_top_mass_pair(self, vectors, idxs):
        ''' Returns the pair of vectors with invariant mass nearest to 
        the given mass '''
        l = []
        for i ,j, k  in combinations(range(len(vectors)),3):
          #XXX need improvement : seperated module for calculating nbtags
          nbtags_had_top = sum([ csv > self.csvcut_M for csv in [ self.rawJet_coll[idxs[i]].btagDeepFlavB, self.rawJet_coll[idxs[j]].btagDeepFlavB, self.rawJet_coll[idxs[k]].btagDeepFlavB ]])
          # if there's no btagged jets in hadronic top, assign large number
          # in the 2 btagged event, 1 b tagged jet is allowed in had top
          # in the >=3 btagged event, more than 2 b tagged jet are allowed in had top
          l.append(([i,j,k], abs(172.5 - (vectors[i]+vectors[j]+vectors[k]).M() ) if (self.nbtags_event==2 and nbtags_had_top == 1) or (self.nbtags_event>=3 and nbtags_had_top >= 2) else LARGE_NUM, nbtags_had_top ))
        l = sorted(l, key=itemgetter(1))
        self.nbtags_had_top = l[0][2] #store number of b-tagged jet in hadronic top
        return l[0][0]

    def maximum_top_pt_pair(self, vectors, idxs):
        ''' Returns the pair of vectors with maximum pt of its 4-vector sum'''
        l = []
        for i ,j, k  in combinations(range(len(vectors)),3):
          #XXX need improvement : seperated module for calculating nbtags
          nbtags_had_top = sum([ csv > self.csvcut_M for csv in [ self.rawJet_coll[idxs[i]].btagDeepFlavB, self.rawJet_coll[idxs[j]].btagDeepFlavB, self.rawJet_coll[idxs[k]].btagDeepFlavB ]])
          # if there's no btagged jets in hadronic top, assign large number
          # in the 2 btagged event, 1 b tagged jet is allowed in had top
          # in the >=3 btagged event, more than 2 b tagged jet are allowed in had top
          #XXX require top mass window
          l.append(([i,j,k], (vectors[i]+vectors[j]+vectors[k]).Pt() if ((self.nbtags_event==2 and nbtags_had_top == 1) or (self.nbtags_event>=3 and nbtags_had_top >= 2)) and 100 < (vectors[i]+vectors[j]+vectors[k]).M() < 240 else -LARGE_NUM, nbtags_had_top ))
        l = sorted(l, key=itemgetter(1), reverse=True)
        self.nbtags_had_top = l[0][2] #store number of b-tagged jet in hadronic top
        return l[0][0]

    def min_deltaR_bb(self, vectors, idxs):
        l = []
        for i ,j in combinations(range(len(vectors)),2):
          is_bb = sum([ csv > self.csvcut_M for csv in [ self.rawJet_coll[idxs[i]].btagDeepFlavB, self.rawJet_coll[idxs[j]].btagDeepFlavB]]) == 2
          l.append(([i,j], vectors[i].DeltaR(vectors[j]) if is_bb else LARGE_NUM ))
        l = sorted(l, key=itemgetter(1))
        return l[0][1]

    def min_deltaR_jj(self, vectors, idxs):
        l = []
        for i ,j in combinations(range(len(vectors)),2):
          is_jj = sum([ csv <= self.csvcut_M for csv in [ self.rawJet_coll[idxs[i]].btagDeepFlavB, self.rawJet_coll[idxs[j]].btagDeepFlavB]]) == 2
          l.append(([i,j], vectors[i].DeltaR(vectors[j]) if is_jj else LARGE_NUM ))
        l = sorted(l, key=itemgetter(1))
        return l[0][1] if not l[0][1] == LARGE_NUM else -1

    def min_deltaPhi_bb(self, vectors, idxs):
        l = []
        for i ,j in combinations(range(len(vectors)),2):
          is_bb = sum([ csv > self.csvcut_M for csv in [ self.rawJet_coll[idxs[i]].btagDeepFlavB, self.rawJet_coll[idxs[j]].btagDeepFlavB]]) == 2
          l.append(([i,j], vectors[i].DeltaPhi(vectors[j]) if is_bb else LARGE_NUM ))
        l = sorted(l, key=itemgetter(1))
        return l[0][1]

    def min_deltaPhi_jj(self, vectors, idxs):
        l = []
        for i ,j in combinations(range(len(vectors)),2):
          is_jj = sum([ csv <= self.csvcut_M for csv in [ self.rawJet_coll[idxs[i]].btagDeepFlavB, self.rawJet_coll[idxs[j]].btagDeepFlavB]]) == 2
          l.append(([i,j], vectors[i].DeltaPhi(vectors[j]) if is_jj else -1 ))
        l = sorted(l, key=itemgetter(1))
        return l[0][1]
    def get_HT_btagged(self, idxs, csvcut):
        is_btagged       = [ csv > csvcut for csv in [ self.rawJet_coll[idx].btagDeepFlavB for idx in idxs ]]
        idxs_btagged     = [ idxs[i] for i, is_tagged in enumerate(is_btagged) if is_tagged is True  ]
        idxs_not_btagged = [ idxs[i] for i, is_tagged in enumerate(is_btagged) if is_tagged is False ]

        HT_btagged     = sum( [ self.findJetPtSystAttr( self.rawJet_coll[idx], "pt" ) for idx in idxs_btagged if self.findJetPtSystAttr( self.rawJet_coll[idx], "pt" )>0 ] )
        HT_not_btagged = sum( [ self.findJetPtSystAttr( self.rawJet_coll[idx], "pt" ) for idx in idxs_not_btagged if self.findJetPtSystAttr( self.rawJet_coll[idx], "pt" )>0 ] )
        return HT_btagged, HT_not_btagged

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
        jet_pt_resolution = self.jer['Pt'].getResolution(self.params_resolution)
        jet_eta_resolution = self.jer['Eta'].getResolution(self.params_resolution)
        jet_phi_resolution = self.jer['Phi'].getResolution(self.params_resolution)
        self.params_sf_and_uncertainty.setJetEta(jet.Eta())
        self.params_sf_and_uncertainty.setJetPt(jet.Pt())
        jet_pt_resolution_SF = self.jerSF_and_Uncertainty.getScaleFactor(self.params_sf_and_uncertainty, 0) # 0 for nominal

        # debug
        #print_msg = "MC jer : {0:.4f} \t\t   MC jer SF : {1:.4f}".format(jet_pt_resolution,jet_pt_resolution_SF)
        #print(print_msg)
        return jet_pt_resolution*jet_pt_resolution_SF, jet_eta_resolution, jet_phi_resolution

