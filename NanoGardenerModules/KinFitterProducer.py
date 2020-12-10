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
    def __init__(self, Year, syst_suffix='nom', branch_map=''):

        # change this part into correct path structure... 

        self._Year = Year
        self._syst_suffix = syst_suffix
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
          self._jet_abseta_cut = 2.4
        elif int(Year) == 2017:
          self._DeepB_WP_M = 0.4941
          self._jet_abseta_cut = 2.5
        elif int(Year) == 2018:
          self._DeepB_WP_M = 0.4184
          self._jet_abseta_cut = 2.5

        # read jet energy resolution (JER) and JER scale factors and uncertainties
        # (the txt files were downloaded from https://github.com/cms-jet/JRDatabase/tree/master/textFiles/ )
        # Text files are now tarred so must extract first
        #

        if int(Year) == 2016:
          jerInputFileName = "Summer16_25nsV1_MC_PtResolution_AK4PFchs.txt"
          jerUncertaintyInputFileName = "Summer16_25nsV1_MC_SF_AK4PFchs.txt"
        elif int(Year) == 2017:
          jerInputFileName = "Fall17_V3_MC_PtResolution_AK4PFchs.txt"
          jerUncertaintyInputFileName = "Fall17_V3_MC_SF_AK4PFchs.txt"
        elif int(Year) == 2018:
          jerInputFileName = "Autumn18_V7_MC_PtResolution_AK4PFchs.txt"
          jerUncertaintyInputFileName = "Autumn18_V7_MC_SF_AK4PFchs.txt"
        #
        self.jerInputArchivePath = os.environ['CMSSW_BASE'] + "/src/PhysicsTools/NanoAODTools/data/jme/"
        self.jerTag = jerInputFileName[:jerInputFileName.find('_MC_')+len('_MC')]
        self.jerArchive = tarfile.open(self.jerInputArchivePath+self.jerTag+".tgz", "r:gz")
        self.jerInputFilePath = tempfile.mkdtemp()
        self.jerArchive.extractall(self.jerInputFilePath)
        self.jerInputFileName = jerInputFileName
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
        print("Loading jet energy resolutions (JER) from file '%s'" % os.path.join(self.jerInputFilePath, self.jerInputFileName))
        self.jer = ROOT.PyJetResolutionWrapper(os.path.join(self.jerInputFilePath, self.jerInputFileName))
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
            'fitted_dijet_M_new1_{}'.format(self._syst_suffix),
            'fitted_dijet_M_new2_{}'.format(self._syst_suffix),
            'hadronic_top_M_{}'.format(self._syst_suffix),
            'hadronic_top_pt_{}'.format(self._syst_suffix),
            'leptonic_top_M_{}'.format(self._syst_suffix),
            'leptonic_W_M_{}'.format(self._syst_suffix),
            'chi2_{}'.format(self._syst_suffix),
            'lambda_{}'.format(self._syst_suffix),
            'hadronic_top_b_jet_pull_{}'.format(self._syst_suffix),
            'leptonic_top_b_jet_pull_{}'.format(self._syst_suffix),
            'w_ch_up_type_jet_pull_{}'.format(self._syst_suffix),
            'w_ch_down_type_jet_pull_{}'.format(self._syst_suffix),
            'hadronic_top_mass_F_{}'.format(self._syst_suffix),
            'leptonic_top_mass_F_{}'.format(self._syst_suffix),
            'leptonic_w_mass_F_{}'.format(self._syst_suffix),
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
        orig_jets_idx   = ROOT.std.vector(int)(0) # to store orig jet idx to see which jets are selected
        jetPtResolution = ROOT.std.vector(float)(0)
        btag_csv_vector     = ROOT.std.vector(ROOT.Double)(0)

        nbtags = 0
        njets  = 0

        #print("jets")
        for jet in Jet :
          # jet_pt syst branch should exist in skim
          jet_pt = self.findJetPtSystAttr(OrigJet[jet.jetIdx])
          if jet_pt <= 20. or abs(jet.eta)>=self._jet_abseta_cut:
            continue
          njets += 1
          tmp_jet = ROOT.TLorentzVector()
          tmp_jet.SetPtEtaPhiM(jet_pt, jet.eta, jet.phi, OrigJet[jet.jetIdx].mass)
          jets.push_back(tmp_jet)
          orig_jets_idx.push_back(jet.jetIdx)
          tmp_jet.SetPtEtaPhiM(jet.pt, jet.eta, jet.phi, OrigJet[jet.jetIdx].mass)
          # set jet resolution
          jetPtResolution_ = self.getJetPtResolution(tmp_jet, event.fixedGridRhoFastjetAll)
          jetPtResolution.push_back(jetPtResolution_)
          btag_csv_vector.push_back(OrigJet[jet.jetIdx].btagDeepB)
          # b taggging
          if OrigJet[jet.jetIdx].btagDeepB > self._DeepB_WP_M:
            nbtags += 1
        


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
        
        fitter = ROOT.TKinFitterDriver(int(self._Year))
        fitter.SetAllObjects(jets, btag_csv_vector, self._DeepB_WP_M, lepton, MET_CHToCB)
        fitter.SetJetPtResolution(jetPtResolution)
        fitter.SetMETShift(METShiftX, METShiftY)
        fitter.FindBestChi2Fit()
        #fitter.FindBestSelTopFit(False,True,True) #old. closest leptonic top, closet had. top, max. had. top
        #void TKinFitterDriver::FindBestSelTopFit(bool IsMaxHadTopPt, bool IsClosestHadTopM, bool IsMaxLepTopPt, bool IsClosestLepTopM){
        #fitter.FindBestSelTopFit(True,True,False,True,False)

        variables = {}

        # retrive ResultContainer vector from fitter
        fit_results = fitter.GetResults()
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
        else:
          for nameBranches in self.newbranches_F + self.newbranches_I:
            if 'nbtagsCleanJet' in nameBranches: # skip variable not retrived from fitter
              continue
            elif 'MET_CHToCB' in nameBranches: # skip variable not retrived from fitter
              continue
            variables[nameBranches] = -1

        #variables['initial_dijet_M_{}'.format(self._syst_suffix)]         = fitter.GetBestInitialDijetMass()
        #variables['initial_dijet_M_high_{}'.format(self._syst_suffix)]    = fitter.GetBestInitialDijetMass_high()
        #variables['corrected_dijet_M_{}'.format(self._syst_suffix)]       = fitter.GetBestCorrectedDijetMass()
        #variables['corrected_dijet_M_high_{}'.format(self._syst_suffix)]  = fitter.GetBestCorrectedDijetMass_high()
        #variables['fitted_dijet_M_{}'.format(self._syst_suffix)]          = fitter.GetBestFittedDijetMass()
        #variables['fitted_dijet_M_high_{}'.format(self._syst_suffix)]     = fitter.GetBestFittedDijetMass_high()
        #variables['best_chi2_{}'.format(self._syst_suffix)]               = fitter.GetBestChi2()
        #variables['lambda_{}'.format(self._syst_suffix)]                  = fitter.GetBestLambda()
        #variables['fitter_status_{}'.format(self._syst_suffix)]           = fitter.GetBestStatus()
        #variables['down_type_jet_b_tagged_{}'.format(self._syst_suffix)]  = fitter.GetBestDownTypeJetBTagged()
        ## these idx variables should be calculated again and this will become a OrigJet idx
        #variables['hadronic_top_b_jet_idx_{}'.format(self._syst_suffix)]  = self.findOrigJetIdx(fitter.GetBestHadronicTopBJetIdx(), orig_jets_idx)
        #variables['leptonic_top_b_jet_idx_{}'.format(self._syst_suffix)]  = self.findOrigJetIdx(fitter.GetBestLeptonicTopBJetIdx(), orig_jets_idx)
        #variables['w_ch_up_type_jet_idx_{}'.format(self._syst_suffix)]    = self.findOrigJetIdx(fitter.GetBestHadronicWCHUpTypeJetIdx(), orig_jets_idx)
        #variables['w_ch_down_type_jet_idx_{}'.format(self._syst_suffix)]  = self.findOrigJetIdx(fitter.GetBestHadronicWCHDownTypeJetIdx(), orig_jets_idx)
        # 
        #variables['hadronic_top_b_jet_pull_{}'.format(self._syst_suffix)] = fitter.GetBestHadronicTopBJetPull()
        #variables['leptonic_top_b_jet_pull_{}'.format(self._syst_suffix)] = fitter.GetBestLeptonicTopBJetPull()
        #variables['w_ch_up_type_jet_pull_{}'.format(self._syst_suffix)]   = fitter.GetBestHadronicWCHUptypeJetIdxPull()
        #variables['w_ch_down_type_jet_pull_{}'.format(self._syst_suffix)] = fitter.GetBestHadronicWCHDowntypeJetIdxPull()

        #fit_results = fitter.GetResults()
        #if fit_results.size() > 0:
        #  variables['hadronic_top_mass_F_{}'.format(self._syst_suffix)]     = fit_results.at(0).hadronic_top_mass_F
        #  variables['leptonic_top_mass_F_{}'.format(self._syst_suffix)]     = fit_results.at(0).leptonic_top_mass_F
        #  variables['leptonic_w_mass_F_{}'.format(self._syst_suffix)]       = fit_results.at(0).leptonic_w_mass_F
        #else:
        #  variables['hadronic_top_mass_F_{}'.format(self._syst_suffix)]     = -1.
        #  variables['leptonic_top_mass_F_{}'.format(self._syst_suffix)]     = -1.
        #  variables['leptonic_w_mass_F_{}'.format(self._syst_suffix)]       = -1.

        #variables['hadronic_top_M_{}'.format(self._syst_suffix)]          = fitter.GetBestHadronicTopMass()
        #variables['hadronic_top_pt_{}'.format(self._syst_suffix)]         = fitter.GetBestHadronicTopPt()
        #variables['leptonic_top_M_{}'.format(self._syst_suffix)]          = fitter.GetBestLeptonicTopMass()
        #variables['leptonic_W_M_{}'.format(self._syst_suffix)]            = fitter.GetBestLeptonicWMass()

        variables['nbtagsCleanJet_{}'.format(self._syst_suffix)] = nbtags

        variables['MET_CHToCB_pt_{}'.format(self._syst_suffix)]  = MET_CHToCB_pt
        variables['MET_CHToCB_phi_{}'.format(self._syst_suffix)] = MET_CHToCB_phi

        for nameBranches in self.newbranches_F + self.newbranches_I:
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
        self.params_sf_and_uncertainty.setJetEta(jet.Eta())
        self.params_sf_and_uncertainty.setJetPt(jet.Pt())
        jet_pt_resolution_SF = self.jerSF_and_Uncertainty.getScaleFactor(self.params_sf_and_uncertainty, 0) # 0 for nominal

        # debug
        #print_msg = "MC jer : {0:.4f} \t\t   MC jer SF : {1:.4f}".format(jet_pt_resolution,jet_pt_resolution_SF)
        #print(print_msg)
        return jet_pt_resolution*jet_pt_resolution_SF

    def findOrigJetIdx(self,fitter_jet_idx, orig_jets_idx):
        # convert 'jet index inside fitter' to 'jet index in OrigJets(Jet_ in nanoAOD)'
        if fitter_jet_idx<0:
          return fitter_jet_idx
        else:
          return orig_jets_idx[fitter_jet_idx]


    def findJetPtSystAttr(self,object_):
        if "unclustEn" in self._syst_suffix:
          syst_suffix = "pt_nom"
        else:
          syst_suffix = "pt_{}".format(self._syst_suffix)
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
            pt = self.findJetPtSystAttr(Jet[jet.jetIdx]) # for nominal syst, propagate Jet_pt_nom
          phi=jet.phi
          JetPxSum+=pt*math.cos(phi)
          JetPySum+=pt*math.sin(phi)

        return JetPxSum, JetPySum

    def UnclShift(self,met_pt,met_phi,event_):
        if "unclustEn" not in self._syst_suffix:
          return met_pt, met_phi
        elif "unclustEnUp" in self._syst_suffix:
          METShiftX =event_.MET_MetUnclustEnUpDeltaX
          METShiftY =event_.MET_MetUnclustEnUpDeltaY
        elif "unclustEnDown" in self._syst_suffix:
          METShiftX =-(event_.MET_MetUnclustEnUpDeltaX)
          METShiftY =-(event_.MET_MetUnclustEnUpDeltaY)
        met_px = met_pt*math.cos(met_phi) + METShiftX
        met_py = met_pt*math.sin(met_phi) + METShiftY

        new_met_pt = math.sqrt(met_px**2 + met_py**2)
        new_met_phi = math.atan2(met_py,met_px)

        return new_met_pt, new_met_phi
        
        

