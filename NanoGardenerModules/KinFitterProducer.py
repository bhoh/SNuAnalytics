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
import sys



class KinFitterProducer(Module):
    def __init__(self, cmssw, syst_suffix='nom', lowerBjetPt=False, noRegCorr=False,branch_map=''):

        # change this part into correct path structure... 

        if '2016' in cmssw:
          self._Year = 2016
        if '2017' in cmssw:
          self._Year = 2017
        if '2018' in cmssw:
          self._Year = 2018

        self._syst_suffix = syst_suffix
        self._lowerBjetPt = lowerBjetPt
        self._noRegCorr   = noRegCorr
        cmssw_base = os.getenv('CMSSW_BASE')
        

        self._branch_map = branch_map
        self.cmssw = cmssw
        #
        if self.cmssw == "Full2016v9HIPM":
            self._DeepFlavB_WP_M   = 0.2598
        elif self.cmssw == "Full2016v9noHIPM":
            self._DeepFlavB_WP_M   = 0.2489
        elif self.cmssw == "Full2017v9":
            self._DeepFlavB_WP_M   = 0.3040
        elif self.cmssw == "Full2018v9":
            self._DeepFlavB_WP_M   = 0.2783
        else:
            raise RuntimeError("no cmssw configuration: " + self.cmssw)

        self._jet_abseta_cut = 2.4

        # read jet energy resolution (JER) and JER scale factors and uncertainties
        # (the txt files were downloaded from https://github.com/cms-jet/JRDatabase/tree/master/textFiles/ )
        # Text files are now tarred so must extract first
        #
        jerTagsMC = {
            'Full2016v7': 'Summer16_25nsV1_MC',
            'Full2017v7': 'Fall17_V3_MC',
            'Full2018v7': 'Autumn18_V7b_MC',
            'Full2016v9HIPM': 'Summer20UL16APV_JRV3_MC',
            'Full2016v9noHIPM': 'Summer20UL16_JRV3_MC',
            'Full2017v9': 'Summer19UL17_JRV2_MC',
            'Full2018v9': 'Summer19UL18_JRV2_MC',
        }

        jerTagMC = jerTagsMC[self.cmssw]
        jerInputFileName_pt  = jerTagMC + "_PtResolution_AK4PFchs.txt"
        jerInputFileName_eta = jerTagMC + "_EtaResolution_AK4PFchs.txt"
        jerInputFileName_phi = jerTagMC + "_PhiResolution_AK4PFchs.txt"
        jerUncertaintyInputFileName = jerTagMC + "_SF_AK4PFchs.txt"

        #
        self.jerInputArchivePath = os.environ['CMSSW_BASE'] + "/src/PhysicsTools/NanoAODTools/data/jme/"
        self.jerTag = jerInputFileName_pt[:jerInputFileName_pt.find('_MC_')+len('_MC')]
        self.jerArchive = tarfile.open(self.jerInputArchivePath+self.jerTag+".tgz", "r:gz")
        self.jerInputFilePath = tempfile.mkdtemp()
        self.jerArchive.extractall(self.jerInputFilePath)
        self.jerInputFileName_pt  = jerInputFileName_pt 
        self.jerInputFileName_eta = jerInputFileName_eta
        self.jerInputFileName_phi = jerInputFileName_phi
        self.jerUncertaintyInputFileName = jerUncertaintyInputFileName
        
        #self.jmr_vals = jmr_vals
        
        self.params_sf_and_uncertainty = ROOT.PyJetParametersWrapper()
        self.params_resolution = ROOT.PyJetParametersWrapper()


        # load libraries for kinematic fitter 
        # load libraries for accessing JER scale factors and uncertainties from txt files
        for library in [ "libCondFormatsJetMETObjects", "libPhysicsToolsNanoAODTools", "libPhysicsToolsKinFitter" ]:
            if library not in ROOT.gSystem.GetLibraries():
                print("Load Library '%s'" % library.replace("lib", ""))
                ROOT.gSystem.Load(library)

        ROOT.gSystem.AddIncludePath('-I'+cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/include/')
        ROOT.gSystem.AddIncludePath('-I'+cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src/')
        self._MacroList = [
                     #'TAbsFitConstraint.C',
                     #'TAbsFitParticle.C',
                     #'TFitConstraintEp.C',
                     #'TFitConstraintM.C',
                     #'TFitConstraintM2Gaus.C',
                     #'TFitConstraintMGaus.C',
                     ##'TFitParticleCart.C',
                     ##'TFitParticleECart.C',
                     ##'TFitParticleEMomDev.C',
                     ##'TFitParticleEScaledMomDev.C',
                     ##'TFitParticleESpher.C',
                     #'TFitParticleEt.C',
                     #'TFitParticleEtEtaPhi.C',
                     #'TFitParticleEtPhi.C',
                     ##'TFitParticleEtThetaPhi.C',
                     #'TFitParticleMCCart.C',
                     ##'TFitParticleMCMomDev.C',
                     ##'TFitParticleMCPInvSpher.C',
                     ##'TFitParticleMCSpher.C',
                     ##'TFitParticleMomDev.C',
                      'TFitParticlePt.C',
                      'TFitParticlePxPy.C',
                     #'TFitParticlePz.C',
                     ##'TFitParticleSpher.C',
                     #'TKinFitter.C',
                      'TSCorrection.C',
                     ##'TKinFitterDriver.C'
                      'TKinFitterDriver.C'
                    ]

        for macro in self._MacroList:
          #ROOT.gROOT.ProcessLineSync('.L '+cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src/%s+g' % macro)
          # original code lines, but it cause
          # fatal error in python 
          #Error in `python': double free or corruption
          try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src/%s+' % macro)
          except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/SNuAnalytics/NanoGardenerModules/KinematicFitter/src/%s++' % macro)


      
    def beginJob(self):
        # initialize JER scale factors and uncertainties
        # (cf. PhysicsTools/PatUtils/interface/SmearedJetProducerT.h )
        print("Loading jet energy resolutions (JER) from file '%s'" % os.path.join(self.jerInputFilePath, self.jerInputFileName_pt ))
        #print("Loading jet energy resolutions (JER) from file '%s'" % os.path.join(self.jerInputFilePath, self.jerInputFileName_eta))
        #print("Loading jet energy resolutions (JER) from file '%s'" % os.path.join(self.jerInputFilePath, self.jerInputFileName_phi))
        self.jer_pt  = ROOT.PyJetResolutionWrapper(os.path.join(self.jerInputFilePath, self.jerInputFileName_pt ))
        #self.jer_eta = ROOT.PyJetResolutionWrapper(os.path.join(self.jerInputFilePath, self.jerInputFileName_eta))
        #self.jer_phi = ROOT.PyJetResolutionWrapper(os.path.join(self.jerInputFilePath, self.jerInputFileName_phi))
        print("Loading JER scale factors and uncertainties from file '%s'" % os.path.join(self.jerInputFilePath, self.jerUncertaintyInputFileName))
        self.jerSF_and_Uncertainty = ROOT.PyJetResolutionScaleFactorWrapper(os.path.join(self.jerInputFilePath, self.jerUncertaintyInputFileName))


    def endJob(self):
        shutil.rmtree(self.jerInputFilePath)

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = mappedOutputTree(wrappedOutputTree, mapname=self._branch_map)
        self.newbranches_F = [
            'initial_dijet_M_{}'.format(self._syst_suffix),
            'initial_dijet_M_high_{}'.format(self._syst_suffix),
            'fitted_dijet_M_{}'.format(self._syst_suffix),
            'fitted_dijet_M_high_{}'.format(self._syst_suffix),
            'hadronic_top_M_{}'.format(self._syst_suffix),
            'hadronic_top_pt_{}'.format(self._syst_suffix),
            'leptonic_top_M_{}'.format(self._syst_suffix),
            'leptonic_W_M_{}'.format(self._syst_suffix),
            'initial_MET_{}'.format(self._syst_suffix),
            'fitted_MET_{}'.format(self._syst_suffix),
            'chi2_{}'.format(self._syst_suffix),
            #'lambda_{}'.format(self._syst_suffix),
            'hadronic_top_b_jet_pull_{}'.format(self._syst_suffix),
            'leptonic_top_b_jet_pull_{}'.format(self._syst_suffix),
            'w_ch_up_type_jet_pull_{}'.format(self._syst_suffix),
            'w_ch_down_type_jet_pull_{}'.format(self._syst_suffix),
            #'fitted_hadronic_top_b_jet_pull_{}'.format(self._syst_suffix),
            #'fitted_leptonic_top_b_jet_pull_{}'.format(self._syst_suffix),
            #'fitted_w_ch_up_type_jet_pull_{}'.format(self._syst_suffix),
            #'fitted_w_ch_down_type_jet_pull_{}'.format(self._syst_suffix),
            #'hadronic_top_mass_F_{}'.format(self._syst_suffix),
            #'leptonic_top_mass_F_{}'.format(self._syst_suffix),
            #'leptonic_w_mass_F_{}'.format(self._syst_suffix),
            #'init_pX_{}'.format(self._syst_suffix),
            #'init_pY_{}'.format(self._syst_suffix),
            #'fitted_pX_{}'.format(self._syst_suffix),
            #'fitted_pY_{}'.format(self._syst_suffix),
            'MET_CHToCB_pt_{}'.format(self._syst_suffix),
            'MET_CHToCB_phi_{}'.format(self._syst_suffix),
          ]
        self.newbranches_I = [
            'nbtagsCleanJet_{}'.format(self._syst_suffix),
            'status_{}'.format(self._syst_suffix),
            'down_type_jet_b_tagged_{}'.format(self._syst_suffix),
            'hadronic_top_b_jet_idx_{}'.format(self._syst_suffix),
            'leptonic_top_b_jet_idx_{}'.format(self._syst_suffix),
            'w_ch_up_type_jet_idx_{}'.format(self._syst_suffix),
            'w_ch_down_type_jet_idx_{}'.format(self._syst_suffix)
          ]
        for nameBranches in self.newbranches_F :
          self.out.branch(nameBranches  ,  "F");
        for nameBranches in self.newbranches_I:
          self.out.branch(nameBranches ,  "I");


        self._fLDroot = ROOT.TFile("/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv9/2018/StackNew_comb/signal_study/Likelihood.root","READ")
        self._had_top_mass_LD = self._fLDroot.Get("likelihood_ratio_had_top_mass_flavCorr_SM")
        self._lep_top_mass_LD = self._fLDroot.Get("likelihood_ratio_lep_top_mass_flavCorr_SM")
        self._mbl_LD          = self._fLDroot.Get("likelihood_ratio_mbl_flavCorr_SM")



    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        # top mass 171.77 \pm 0.38 GeV
        # https://cms.cern/news/cms-collaboration-measures-mass-top-quark-unparalleled-accuracy
        self._fitter = ROOT.TKinFitterDriver(int(self._Year), ROOT.Double(172.5))
        self._fitter.Set_had_top_mass_LD(self._had_top_mass_LD)
        self._fitter.Set_lep_top_mass_LD(self._lep_top_mass_LD)
        self._fitter.Set_mbl_LD(self._mbl_LD)
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
        orig_jets_idx   = ROOT.std.vector(int)(0) # to store orig jet idx to see which jets are selected
        jetPtResolution = ROOT.std.vector(ROOT.Double)(0)
        jetPtBregCorr   = ROOT.std.vector(ROOT.Double)(0)
        jetPtBregRes    = ROOT.std.vector(ROOT.Double)(0)
        jetPtCregCorr   = ROOT.std.vector(ROOT.Double)(0)
        jetPtCregRes    = ROOT.std.vector(ROOT.Double)(0)
        #jetEtaResolution = ROOT.std.vector(ROOT.Double)(0)
        #jetPhiResolution = ROOT.std.vector(ROOT.Double)(0)
        btag_csv_vector = ROOT.std.vector(ROOT.Double)(0)
        genJetPt        = ROOT.std.vector(ROOT.Double)(0)

        nbtags = 0
        njets  = 0

        #print("jets")
        for jet in Jet :
          # jet_pt syst branch should exist in skim
          jet_pt   = self.findJetPtSystAttr(OrigJet[jet.jetIdx], "pt")
          jet_mass   = self.findJetPtSystAttr(OrigJet[jet.jetIdx], "mass")
          jet_csv  = OrigJet[jet.jetIdx].btagDeepFlavB
          #jet_puId_M = OrigJet[jet.jetIdx].puId
          if jet_pt <= 25. or abs(jet.eta)>=self._jet_abseta_cut:
            continue
          if jet_pt > 25. and jet_pt<=30:
            #if not self._lowerBjetPt:
            #  continue
            #if not (jet_puId_M & (1<<1)):
            #  continue
            #if jet_csv <= self._DeepFlavB_WP_M:
            #  continue
            pass
          njets += 1
          # b taggging
          isBtaged = jet_csv > self._DeepFlavB_WP_M
          if isBtaged:
            nbtags += 1
          tmp_jet = ROOT.TLorentzVector()
          tmp_jet.SetPtEtaPhiM(jet_pt, jet.eta, jet.phi, jet_mass)
          if lepton.DeltaR(tmp_jet) < 0.3:
            print("Debug!!!!!: lepton.DeltaR(tmp_jet) < 0.3")
            continue
          btag_csv_vector.push_back(jet_csv)
          jets.push_back(tmp_jet)
          orig_jets_idx.push_back(jet.jetIdx)
          #tmp_jet.SetPtEtaPhiM(jet.pt, jet.eta, jet.phi, OrigJet[jet.jetIdx].mass) #XXX 24.04.10, bug fix: commented out
          # set jet resolution
          jetPtResolution_, jetEtaResolution_, jetPhiResolution_ = self.getJetPtResolution(tmp_jet, event.fixedGridRhoFastjetAll)
          if self._noRegCorr == False:
            # sigma = 1.482 * IQR
            jetPtBregCorr_ = OrigJet[jet.jetIdx].bRegCorr
            jetPtBregRes_  = 1.482 * OrigJet[jet.jetIdx].bRegRes
            jetPtCregCorr_ = OrigJet[jet.jetIdx].cRegCorr
            jetPtCregRes_  = 1.482 * OrigJet[jet.jetIdx].cRegRes
          else:
            jetPtBregCorr_ = 1.
            jetPtBregRes_  = jetPtResolution_
            jetPtCregCorr_ = 1.
            jetPtCregRes_  = jetPtResolution_


          # 3% of jet pT is assigned as conservative uncertainties.
          if "RegCorr" in self._syst_suffix:
            if   "bRegCorrUp" in self._syst_suffix:
              jetPtBregCorr_ += 0.03
            elif "bRegCorrDown" in self._syst_suffix:
              jetPtBregCorr_ -= 0.03 if jetPtBregCorr_ > 0.03 else 0
            elif "cRegCorrUp" in self._syst_suffix:
              jetPtCregCorr_ += 0.03
            elif "cRegCorrDown" in self._syst_suffix:
              jetPtCregCorr_ -= 0.03 if jetPtCregCorr_ > 0.03 else 0

          elif "RegRes" in self._syst_suffix:
            if   "bRegResUp" in self._syst_suffix:
              jetPtBregRes_  += 0.1
            elif "bRegResDown" in self._syst_suffix:
              jetPtBregRes_  -= 0.1 if jetPtBregRes_ > 0.1 else 0
            elif "cRegResUp" in self._syst_suffix:
              jetPtCregRes_  += 0.1
            elif "cRegResDown" in self._syst_suffix:
              jetPtCregRes_  -= 0.1 if jetPtCregRes_ > 0.1 else 0

          jetPtResolution.push_back(jetPtResolution_)
          jetPtBregCorr.push_back(jetPtBregCorr_)
          jetPtBregRes .push_back(jetPtBregRes_ )
          jetPtCregCorr.push_back(jetPtCregCorr_)
          jetPtCregRes .push_back(jetPtCregRes_ )
          #jetEtaResolution.push_back(jetEtaResolution_)
          #jetPhiResolution.push_back(jetPhiResolution_)

        

        # propagate MET by syst suffix
        # jet_pt syst branch should exist in skim
        MET_CHToCB = ROOT.TLorentzVector()
        origMET = Object(event, "PuppiMET")

        MET_CHToCB_pt, MET_CHToCB_phi = self.propagateToMET(OrigJet,Jet,origMET)
        MET_CHToCB_pt, MET_CHToCB_phi = self.UnclShift(MET_CHToCB_pt,MET_CHToCB_phi,event)
        MET_CHToCB.SetPtEtaPhiM(MET_CHToCB_pt, 0., MET_CHToCB_phi, 0.)
        #print("MET_CHToCB")
        #print(event.PuppiMET_pt,"   ",event.PuppiMET_phi)

        METShiftX =event.MET_MetUnclustEnUpDeltaX
        METShiftY =event.MET_MetUnclustEnUpDeltaY
        
        self._fitter.SetAllObjects(jets, btag_csv_vector, self._DeepFlavB_WP_M, lepton, MET_CHToCB)
        self._fitter.SetJetPtResolution(jetPtResolution)
        self._fitter.SetJetBregCorr(jetPtBregCorr)
        self._fitter.SetJetBregRes (jetPtBregRes)
        self._fitter.SetJetCregCorr(jetPtCregCorr)
        self._fitter.SetJetCregRes (jetPtCregRes)
        #self._fitter.SetJetEtaResolution(jetEtaResolution)
        #self._fitter.SetJetPhiResolution(jetPhiResolution)
        self._fitter.SetMETShift(METShiftX, METShiftY)
        #self._fitter.FindBestChi2Fit()
        self._fitter.FindBestLDFit()
        #self._fitter.FindBestSelTopFit(False,True,True) #old. closest leptonic top, closet had. top, max. had. top
        #void TKinFitterDriver::FindBestSelTopFit(bool IsMaxHadTopPt, bool IsClosestHadTopM, bool IsMaxLepTopPt, bool IsClosestLepTopM){
        #self._fitter.FindBestSelTopFit(True,True,False,True,False)

        variables = {}

        # retrive ResultContainer vector from fitter
        fit_results = self._fitter.GetResults()
        # if there's a no eligible result, put -1
        if fit_results.size() > 0:
          for nameBranches in self.newbranches_F + self.newbranches_I:
            if 'nbtagsCleanJet' in nameBranches: # skip variable not retrived from fitter
              continue
            elif 'MET_CHToCB' in nameBranches: # skip variable not retrived from fitter
              continue
            else:
              nameBranches_no_suffix = nameBranches[:-len(self._syst_suffix)][:-1]
              if 'jet_idx' not in nameBranches:
                variables[nameBranches] = getattr(fit_results.at(0),nameBranches_no_suffix)
              else:
                # convert jet index inside the fitter to index in Jet collection
                variables[nameBranches] = self.findOrigJetIdx(getattr(fit_results.at(0),nameBranches_no_suffix), orig_jets_idx)
                if "leptonic_top_b_jet_idx" in nameBranches:
                  tmp_csv = OrigJet[variables[nameBranches]].btagDeepFlavB
                  if tmp_csv < self._DeepFlavB_WP_M:
                    print("tmp_csv < self._DeepFlavB_WP_M")

        else:
          for nameBranches in self.newbranches_F + self.newbranches_I:
            if 'nbtagsCleanJet' in nameBranches: # skip variable not retrived from fitter
              continue
            elif 'MET_CHToCB' in nameBranches: # skip variable not retrived from fitter
              continue
            variables[nameBranches] = -1


        variables['nbtagsCleanJet_{}'.format(self._syst_suffix)] = nbtags

        variables['MET_CHToCB_pt_{}'.format(self._syst_suffix)]  = MET_CHToCB_pt
        variables['MET_CHToCB_phi_{}'.format(self._syst_suffix)] = MET_CHToCB_phi

        for nameBranches in self.newbranches_F + self.newbranches_I:
          #if "hadronic_top_b_jet_pull" in nameBranches:
          #  print(nameBranches, variables[nameBranches])
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
        jet_pt_resolution  = self.jer_pt.getResolution(self.params_resolution)
        jet_eta_resolution = 1. #self.jer_eta.getResolution(self.params_resolution)
        jet_phi_resolution = 1. #self.jer_phi.getResolution(self.params_resolution)
        self.params_sf_and_uncertainty.setJetEta(jet.Eta())
        self.params_sf_and_uncertainty.setJetPt(jet.Pt())
        jet_pt_resolution_SF = self.jerSF_and_Uncertainty.getScaleFactor(self.params_sf_and_uncertainty, 0) # 0 for nominal

        # debug
        #print_msg = "MC jer : {0:.4f} \t\t   MC jer SF : {1:.4f}".format(jet_pt_resolution,jet_pt_resolution_SF)
        #print(print_msg)
        return jet_pt_resolution*jet_pt_resolution_SF, jet_eta_resolution, jet_phi_resolution

    def findOrigJetIdx(self,fitter_jet_idx, orig_jets_idx):
        # convert 'jet index inside fitter' to 'jet index in OrigJets(Jet_ in nanoAOD)'
        #if fitter_jet_idx<0:
        #  return fitter_jet_idx
        #else:
        #  return orig_jets_idx[fitter_jet_idx]
        return orig_jets_idx[fitter_jet_idx]


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


    def propagateToMET(self,Jet,CleanJet,origMET):
        #### MET_px = -sum( particle_px ) 
        ######MET_px_new = -sum(particle_px_new) = -sum( particle_px - particle_px + particle_px_new  )
        ######## = MET_px -sum(particle_px_new - particle_px)
        ###     => MET_px_new = MET_px - sum( dpx )
        JetPxSum_old, JetPySum_old = self.GetJetPxPySum(Jet,CleanJet,False)
        JetPxSum_new, JetPySum_new = self.GetJetPxPySum(Jet,CleanJet,True)

        if self._syst_suffix == 'nom':
          if JetPxSum_old != JetPxSum_new or JetPySum_old != JetPySum_new:
            raise Exception('something wrong in propagateToMET')
        
        dpx = JetPxSum_new - JetPxSum_old
        dpy = JetPySum_new - JetPySum_old


        origMET_pt = origMET.pt
        origMET_phi = origMET.phi
        origMET_px = origMET_pt*math.cos(origMET_phi)
        origMET_py = origMET_pt*math.sin(origMET_phi)

        newMET_px = origMET_px - dpx
        newMET_py = origMET_py - dpy
        newMET_pt = math.sqrt(newMET_px**2 + newMET_py**2)
        newMET_phi = math.atan2(newMET_py,newMET_px)

        return newMET_pt, newMET_phi


    def GetJetPxPySum(self,Jet,CleanJet,syst):
        JetPxSum = 0.
        JetPySum = 0.
        for jet in CleanJet: #propagate CleanJet to MET
          if syst==False:
            pt = Jet[jet.jetIdx].pt_nom #jet pt with JER smearing
          else:
            pt = self.findJetPtSystAttr(Jet[jet.jetIdx],"pt") # for nominal syst, propagate Jet_pt_nom
          phi=jet.phi
          JetPxSum+=pt*math.cos(phi)
          JetPySum+=pt*math.sin(phi)

        return JetPxSum, JetPySum

    def UnclShift(self,met_pt,met_phi,event_):
        if "unclustEn" not in self._syst_suffix:
          return met_pt, met_phi
        elif "unclustEnUp" in self._syst_suffix:
          met_pt_shift  = event_.PuppiMET_ptUnclusteredUp
          met_phi_shift = event_.PuppiMET_phiUnclusteredUp
        elif "unclustEnDown" in self._syst_suffix:
          met_pt_shift  = event_.PuppiMET_ptUnclusteredDown
          met_phi_shift = event_.PuppiMET_phiUnclusteredDown

        return met_pt_shift, met_phi_shift
        
        

