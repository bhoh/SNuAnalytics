# LatinoAnalysis/NanoGardener/python/modules 

import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import math
import numpy
import re
import os
from math import sqrt

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

Wmass=80.4
MaxLimit =  99999.
MinLimit = -1.

Masses = [400, 1500]

class HMlnjjVarsClass_Dev(Module):
    def __init__(self, year, METtype='PuppiMET', doSkim=False, doHardSkim=False):

        self.cmssw_base = os.getenv('CMSSW_BASE')
        cmssw_arch = os.getenv('SCRAM_ARCH')

        self._MET_4v        = ROOT.TLorentzVector()
        self._MET_big4v     = ROOT.TLorentzVector()
        self._lepton_4v     = ROOT.TLorentzVector()
        self._Wlep_4v       = ROOT.TLorentzVector()
        self._Wlep_big4v    = ROOT.TLorentzVector()
        self._FinalFatJet_4v= ROOT.TLorentzVector()
        self._Whad_j1_4v    = ROOT.TLorentzVector()
        self._Whad_j2_4v    = ROOT.TLorentzVector()
        self._Whad_4v       = ROOT.TLorentzVector()
	self._lnJ_4v        = ROOT.TLorentzVector()
	# TODO  let's think the usage of this MET_Z solution
	self._lnJ_big4v     = ROOT.TLorentzVector()
	self._lnjj_4v       = ROOT.TLorentzVector()
	self._lnjj_big4v    = ROOT.TLorentzVector()
	self._VBFBoost_jet1_4v       = ROOT.TLorentzVector()
	self._VBFBoost_jet2_4v       = ROOT.TLorentzVector()

        self.doSkim = doSkim
        self.METtype = METtype

        ##--How to select primary fatjet
        self._FatSel_cfjidx={}
        self._FatSel_cfjidx['mindM']=-1 ## FatJet_mass ~ mindM
        self._FatSel_cfjidx['mxPT']=-1 ## largest mxPT
       
        self._subJet1_4v = ROOT.TLorentzVector()
        self._subJet2_4v = ROOT.TLorentzVector()
        #####################################
	# Cuts
        #####################################
	self.Wmass_CRlow  = 40
	self.Wmass_CRhigh = 250
	self.Wmass_SRlow  = 65
	self.Wmass_SRhigh = 105 

        self.METcut_Boost = 40.
        self.METcut_Resol = 30.
	self.cut_lnjj_Mt  = 60
	self.cut_Wlep_Mt  = 50 # resolve only

	self.cut_fjet_eta = 2.4
	self.cut_fjet_pt  = 200
	self.cut_jet_eta  = 2.4
	self.cut_jet_pt   = 30
	self.cut_bjet_pt  = 20
	self.cut_bjet_eta = 2.5

	self.cut_VBFjet_pt = 30
	self.cut_VBFjet_eta= 4.7 
	self.cut_VBF_dEta  = 3.5
	self.cut_VBF_mjj   = 500

	self.cut_minPtWOverMlnJ  = 0.4
	self.cut_minPtWOverMlnjj = 0.35

        ###---Year dependent cut----##
        print "@@Year->",year
        self.year=year
        # b-tag WP && tau21 (Wtag)
        self.bWP=0.2217 ##2016legacy
        self.tau21WP= 0.4 ##2016 legacy
        self.min_fatjetid = 1
        if '2016' in str(self.year): 
            self.bWP=0.2217   ##https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation2016Legacy
            self.tau21WP=0.4  ##2016 scale factors and corrections
            self.min_fatjetid = 1
        elif '2017' in str(self.year): 
            self.bWP=0.1522    ##https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
            self.tau21WP=0.45  ##https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetWtagging#tau21_0_45
            self.min_fatjetid = 2
        elif '2018' in str(self.year):
            self.bWP=0.1241    ##https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation102X
            self.tau21WP=0.45  ##https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetWtagging#tau21_0_45_HP_0_45_tau21_0_75_LP
            self.min_fatjetid = 4 
        # Tau21 cut (High purity)

        # MELA 
        # Directory ZZMatrixElement: https://github.com/cms-analysis/HiggsAnalysis-ZZMatrixElement.git / https://twiki.cern.ch/twiki/bin/view/CMS/MELAProject
        # Directory MelaAnalytics: https://github.com/usarica/MelaAnalytics.git
        ROOT.gSystem.AddIncludePath("-I"+self.cmssw_base+"/interface/")
        ROOT.gSystem.AddIncludePath("-I"+self.cmssw_base+"/src/")
        ROOT.gSystem.Load("libZZMatrixElementMELA.so")
        ROOT.gSystem.Load("libMelaAnalyticsCandidateLOCaster.so")
        ROOT.gSystem.Load(self.cmssw_base+"/src/ZZMatrixElement/MELA/data/"+cmssw_arch+"/libmcfm_706.so")
        try:
            ROOT.gROOT.LoadMacro(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/melaHighMassKDwCalc.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/melaHighMassKDwCalc.C++g')

        self.MakeMassVsGamma()

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.debug = False
	if self.debug:
	  self.evtMyNum = 0

	# ME
	# Mass dependent later maybe, let's go with already observed processes
	for mass in Masses:
	 self.MEbranches = [
	     'meP' + str(mass) + '_BstVBF_vbf_S',
	     'meP' + str(mass) + '_BstVBF_vbf_B',
	     'meP' + str(mass) + '_BstVBF_ggf_S',
	     'meP' + str(mass) + '_BstVBF_ggf_B',
	     'meP' + str(mass) + '_BstNoT_vbf_S',
	     'meP' + str(mass) + '_BstNoT_vbf_B',
	     'meP' + str(mass) + '_BstNoT_ggf_S',
	     'meP' + str(mass) + '_BstNoT_ggf_B',
	     'meP' + str(mass) + '_ResVBF_vbf_S',
	     'meP' + str(mass) + '_ResVBF_vbf_B',
	     'meP' + str(mass) + '_ResVBF_ggf_S',
	     'meP' + str(mass) + '_ResVBF_ggf_B',
	     'meP' + str(mass) + '_ResNoT_vbf_S',
	     'meP' + str(mass) + '_ResNoT_vbf_B',
	     'meP' + str(mass) + '_ResNoT_ggf_S',
	     'meP' + str(mass) + '_ResNoT_ggf_B'
	     ]
	 for brName in self.MEbranches:
	   self.out.branch(brName, "F")
	#self.MEbranches = [
	#    'meP_Boost_vbf_Sg',
	#    'meP_Boost_ggf_Sg',
	#    'meP_Resol_vbf_Sg',
	#    'meP_Resol_ggf_Sg',
	#    'meP_Boost_vbf_Bg',
	#    'meP_Boost_ggf_Bg',
	#    'meP_Resol_vbf_Bg',
	#    'meP_Resol_ggf_Bg'
	#    ]
	for brName in self.MEbranches:
	  self.out.branch(brName, "F")

        # TODO high mass sample dependent mass and gamma
	#massH = 400
        #gsmH = self.g.GetBinContent(self.g.FindBin(massH))
        #self.mela = ROOT.MelaHighMassKDwCalc(13, massH, gsmH )
        self.mela = ROOT.MelaHighMassKDwCalc(13, 125, 0.00407 )

        # Wlep
        for var in ['pt','eta','phi','mass','Mt']:
            self.out.branch("Wlep_"+var  , "F")
        self.out.branch(self.METtype+'_pz1', "F")
        self.out.branch(self.METtype+'_pz2', "F")
        

        ##---Boost Region kinematics
        self.out.branch("isBoost","O")
        self.out.branch("isBoostSR","O")
        self.out.branch("WtagFatjet_cfjidx","I",lenVar='nWtagFatjet')
        for var in ['pt','eta','phi','mass','tau21']:
            self.out.branch("WtagFatjet_"+var,"F",lenVar='nWtagFatjet')
        self.out.branch("FinalFatJet_mindM_cfjidx","I")
        self.out.branch("FinalFatJet_mxPT_cfjidx","I")
        
        for sel in self._FatSel_cfjidx:
            self.out.branch('lnJ_pt_'+sel,"F")
            self.out.branch('lnJ_mass_'+sel,"F")
            self.out.branch('minPtWOverMlnJ_'+sel,"F")
            self.out.branch('maxPtWOverMlnJ_'+sel,"F")
            self.out.branch('dR_l_F_'+sel,"F")
            self.out.branch('dR_Wlep_F_'+sel,"F")
            self.out.branch('dPhi_l_F_'+sel,"F")
            self.out.branch('dPhi_Wlep_F'+sel,"F")
        
        self.out.branch('BJetBoost_cjidx','I',lenVar='nBJetBoost')
        self.out.branch('BJetBoostVBF_cjidx','I',lenVar='nBJetBoostVBF')

        self.out.branch('isVBF_Boost','O')
        self.out.branch('VBFjjBoost_mjj','F')
        self.out.branch('VBFjjBoost_dEta','F')
        self.out.branch('max_mjj_Boost','F')

        ##---Resol Region kinemaics
        self.out.branch('isResol',"O")
        self.out.branch('isResolSR',"O")
        for var in ['pt','eta','phi','mass','Mt']:
            self.out.branch('Whad_'+var,'F')
        
        self.out.branch('Whad_cjidx1','I')
        self.out.branch('Whad_cjidx2','I')
        self.out.branch('BJetResol_cjidx','I',lenVar='nBJetResol')
        self.out.branch('BJetResolVBF_cjidx','I',lenVar='nBJetResolVBF')
        self.out.branch('isVBF_Resol','O')
        self.out.branch('VBFjjResol_dEta','F')
        self.out.branch('VBFjjResol_mjj','F')
        self.out.branch('VBFjjResol_dEta','F')
        self.out.branch('max_mjj_Resol','F')

        self.out.branch('lnjj_pt', 'F')
        self.out.branch('lnjj_mass', 'F')
        self.out.branch('lnjj_Mt', 'F')
        self.out.branch('minPtWOverMlnjj','F')
        self.out.branch('maxPtWOverMlnjj','F')
        self.out.branch('dR_l_Whad','F')
        self.out.branch('dR_Wlep_Whad','F')
        self.out.branch('dPhi_l_Whad','F')
        self.out.branch('dPhi_Wlep_Whad','F')

        
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def initReaders(self,tree): # this function gets the pointers to Value and ArrayReaders and sets them in the C++ worker class
        pass


    def analyze(self, event):
        if self.debug:
          self.evtMyNum = self.evtMyNum +1
	#if self.evtMyNum not in [945,947]: return True
        """process event, return True (go to next module) or False (fail, go to next event)"""
	# Wlep ############################3
        self._lepton_4v.SetPtEtaPhiM(0,0,0,0)
        self._MET_4v.SetPtEtaPhiM(0,0,0,0)
        self._MET_big4v.SetPtEtaPhiM(0,0,0,0)
	self._Wlep_4v.SetPtEtaPhiM(0,0,0,0)
	self._Wlep_big4v.SetPtEtaPhiM(0,0,0,0)
	self._Wlep_Mt = MinLimit


	self._VBFBoost_jet1_4v.SetPtEtaPhiM(0,0,0,0)
	self._VBFBoost_jet2_4v.SetPtEtaPhiM(0,0,0,0)
        # Boost ########################
        self._isBoost=False
        self._isBoostSB=False
        self._isBoostSR=False
        self._Wfatjet_mindM_cfjidx=-1 ##select fatjet whose mass is closest to MW
        self._Wfatjet_mxPT_cfjidx=-1 ## select fatjet whose pt is largest one
        self._FinalFatJet_4v.SetPtEtaPhiM(0,0,0,0)
        self._subJet1_4v.SetPtEtaPhiM(0,0,0,0)
        self._subJet2_4v.SetPtEtaPhiM(0,0,0,0)
        self._Wfatjet_cfjidx_list=[]
        self._Wfatjet_pt_list=[]
        self._Wfatjet_eta_list=[]
        self._Wfatjet_phi_list=[]
        self._Wfatjet_mass_list=[]
        self._Wfatjet_tau21_list=[]
        self._BJetBoost_cjidx=[]
        self._BJetBoostVBF_cjidx=[]
        self._isVBF_Boost=False
        self._VBFjjBoost_dEta = MinLimit
        self._VBFjjBoost_mjj  = MinLimit
        self._VBFjjBoost_cjidx1=-1
        self._VBFjjBoost_cjidx2=-1
        self._max_mjj_Boost=-1.
        self._FatSel_cfjidx['mindM']=-1 ## FatJet_mass ~ mindM
        self._FatSel_cfjidx['mxPT']=-1## largest mxPT
        self._lnJ_4v.SetPtEtaPhiM(0,0,0,0)
        self._lnJ_big4v.SetPtEtaPhiM(0,0,0,0)
        
	# Resol #########################3
        self._isResol = False
        self._isResolSR = False
        self._isResolSB = False
        self._Whad_j1_4v.SetPtEtaPhiM(0,0,0,0)
        self._Whad_j2_4v.SetPtEtaPhiM(0,0,0,0)
        self._Whad_4v.SetPtEtaPhiM(0,0,0,0)
        self._Whad_cjidx1=-1
        self._Whad_cjidx2=-1
        self._BJetResol_cjidx=[]
        self._BJetResolVBF_cjidx=[]
        self._isVBF_Resol=False
        self._VBFjjResol_dEta= MinLimit
        self._VBFjjResol_mjj = MinLimit
        self._VBFjjResol_cjidx1=-1
        self._VBFjjResol_cjidx2=-1
        self._max_mjj_Resol = -1.
	self._minPtWOverMlnjj = MinLimit
	self._maxPtWOverMlnjj = MinLimit
        self._lnjj_4v.SetPtEtaPhiM(0,0,0,0)
        self._lnjj_big4v.SetPtEtaPhiM(0,0,0,0)
	self._lnjj_pt   = MinLimit
	self._lnjj_mass = MinLimit
	self._lnjj_Mt   = MinLimit

	self._dR_l_Whad = -1
	self._dR_Wlep_Whad = -1
	self._dPhil_Whad = -1
	self._dPhiWlep_Whad = -1


        ##--End of initialization

        
        ##--Get object collections--##
        self._Lepton = Object(event, 'Lepton', index=0)
        self._CleanFatJet_col = Collection(event, 'CleanFatJet')
        self._FatJet_col = Collection(event, 'FatJet')
        self._CleanJet_col = Collection(event, 'CleanJet')
        self._CleanJetNotFat_col = Collection(event, 'CleanJetNotFat')
        self._Jet_col = Collection(event,"Jet")
        self._SubJet_col = Collection(event,"SubJet")

        ##---MET
        self._MET = Object(event, self.METtype)
        self._MET_pt = self._MET.pt
        self._MET_phi = self._MET.phi
	self._MET_pz1 = -1
	self._MET_pz2 = -1
	self._MET_pz  = 0
	self._MET_bigZ  = 0
	#self._MET_4v.SetPtEtaPhiM(self._MET_pt, 0, self._MET_phi, 0.) at Wlep
        
        

        #<<<<<<<Boost>>>>>>>#
        
        ##---Step.1.Set Wlep
        #print "Start WlepMaker"
        self.WlepMaker()  #self._Wlep_4v , self._MET_pz1, self._MET_pz2
        #print "End WlepMaker"
        ##set           self._Wlep_4v
        
        
        
        ##---Step.2 Get Wtagger fatjet
        
        self.FindWtaggerFatJet() ##Fill self._Wfatjet_cfjidx_list
        ##-> Fill        cleanfatjet index     to       self._Wfatjet_cfjidx_list=[]
        ##-> set         self._Wfatjet_mindM_cfjidx -> select FatJet whose Msoftdrop is closest to MW
        ##-> set         self._Wfatjet_mxPT_cfjidx -> select FatJet whose mxPT is the largest one
	##-> set	self._isBoost after WfatJet selection

        #---Two kinds of choice for FatJets 
        ##self._Wfatjet_mindM_idx
        ##self._Wfatjet_mxPT_idx
        
	self.CookLnJ() #cut for minPtWOverMlnJ, MET 
	# giving lnJ_4v, FinalFatJet_4v
	# isBoostSB, isBoostSR

        ##End of fatjet selection choice
       
        ##---Step.4 VBF Boost
        self.VBF_Boost()
        ##Set values of 
        ##->self._isVBF_Boost
	## variables for the maximum mjj
        ##->self._VBFjjBoost_dEta
        ##->self._VBFjjBoost_mjj
        ##->self._VBFjjBoost_cjidx1
        ##->self._VBFjjBoost_cjidx2
        #print "End of Boost"

        ##--- should be after VBF_Boost for BJetBoostVBF_cjidx
        self.GetBJetsBoost()
        ##->Set self._BJetBoost_cjidx
        ##->Set self._BJetBoostVBF_cjidx


        ##--Fill Branch for object ##
        ###-->Wfatjet_idx_list/Wfatjet_mindM_cfjidx//Wfatjet_mxPT_cfjidx/
        ###-->_isBoost, Wlep momentum, solution 1,2/ _VBFjjBoost_dEta, _VBFjjBoost_mjj,_BJetBoost_cjidx,_max_mjj_Boost
        ##---Check whether they are initialized at the starting of this analyze loop function
        #<<<<< End of Boost
        #print "fillBranchBoost end"
        
        #<<<<<<<Resol>>>>>>>#
        
        ##Step.1 Get hadronic W using ak4 jet pair, choosing min(Wmass -Mjj)
        self.WhadMaker()
        ##set      self._Whad_4v
        ##set      self._Whad_cjidx1
        ##set      self._Whad_cjidx2
        ##set      self._isResol
	self.CookLnjj()
	#cut for minPtWOverMlnJ, MET 
        # isResolSB, isResolSR

        ##Step.2 Get Btag
        ##set      self._BJetResol_cjidx
        

        ##Step.3 VBF_Resol
        self.VBF_Resol()
        ##set      self._isVBF_Resol
	# variables for maximum mjj
        ##set      self._VBFjjResol_mjj
        ##set      self._VBFjjResol_dEta
        ##set      self._VBFjjResol_cjidx1
        ##set      self._VBFjjResol_cjidx2
        ##set      self._VBFjjResol_mjj

        ##--- should be after VBF_Boost for BJetResolVBF_cjidx
        self.GetBJetsResol()

	self.CookME()
   
        ##Fill branch ####
	self.FillBranch()

        #print "self._isBoost",self._isBoost
        #print "self._isResol",self._isResol
        
        ##<<<<End of Resol


	########################
	# Event Save Decision
	########################

        if (not self._isBoost) and (not self._isResol) and self.doSkim: return False

        #if event.event % 10000 ==1 :##To flush memory of ttree
	#  self.out._tree.AutoSave()
	#self.out._tree.AutoSave("FlushBaskets")

        return True




    def FillBranch(self):

        ##---Wlep
        #print "fillBranchBoost"
        self.out.fillBranch('Wlep_pt',self._Wlep_4v.Pt())
        self.out.fillBranch('Wlep_eta',self._Wlep_4v.Eta())
        self.out.fillBranch('Wlep_phi',self._Wlep_4v.Phi())
        self.out.fillBranch('Wlep_mass',self._Wlep_4v.M())
        self.out.fillBranch('Wlep_Mt'  ,self._Wlep_Mt)
        self.out.fillBranch(self.METtype+'_pz1',self._MET_pz1) ##MET_pz = pz1+-sqrt(pz2)
        self.out.fillBranch(self.METtype+'_pz2',self._MET_pz2)
        

        self.out.fillBranch('isBoost'  ,self._isBoost)
        self.out.fillBranch('isBoostSR',self._isBoostSR)
        self.out.fillBranch('WtagFatjet_cfjidx',self._Wfatjet_cfjidx_list)
        self.out.fillBranch('WtagFatjet_pt',self._Wfatjet_pt_list)
        self.out.fillBranch('WtagFatjet_eta',self._Wfatjet_eta_list)
        self.out.fillBranch('WtagFatjet_phi',self._Wfatjet_phi_list)
        self.out.fillBranch('WtagFatjet_mass',self._Wfatjet_mass_list)
        self.out.fillBranch('WtagFatjet_tau21',self._Wfatjet_tau21_list)

        ## choice for final fatjet
        self.out.fillBranch('FinalFatJet_mindM_cfjidx',self._Wfatjet_mindM_cfjidx)
        self.out.fillBranch('FinalFatJet_mxPT_cfjidx',self._Wfatjet_mxPT_cfjidx)


        ##---Btagged Jet
        self.out.fillBranch('BJetBoost_cjidx', self._BJetBoost_cjidx)
        self.out.fillBranch('BJetBoostVBF_cjidx', self._BJetBoostVBF_cjidx)
        ##---VBF Boost
        self.out.fillBranch('isVBF_Boost', self._isVBF_Boost)

        self.out.fillBranch('VBFjjBoost_mjj', self._VBFjjBoost_mjj)
        self.out.fillBranch('VBFjjBoost_dEta', self._VBFjjBoost_dEta)

        self.out.fillBranch('max_mjj_Boost', self._max_mjj_Boost)
        self.out.fillBranch('isResol',self._isResol)
        self.out.fillBranch('isResolSR',self._isResolSR)

        ##Hadronic W
        self.out.fillBranch('Whad_pt',   self._Whad_4v.Pt())
        self.out.fillBranch('Whad_eta',  self._Whad_4v.Eta())
        self.out.fillBranch('Whad_phi',  self._Whad_4v.Phi())
        self.out.fillBranch('Whad_mass', self._Whad_4v.M())
        self.out.fillBranch('Whad_Mt',   self._Whad_4v.Mt())

        self.out.fillBranch('Whad_cjidx1', self._Whad_cjidx1)
        self.out.fillBranch('Whad_cjidx2', self._Whad_cjidx2)
        self.out.fillBranch('BJetResol_cjidx', self._BJetResol_cjidx)
        self.out.fillBranch('BJetResolVBF_cjidx', self._BJetResolVBF_cjidx)

        ###VBF
        self.out.fillBranch('isVBF_Resol',     self._isVBF_Resol)
        self.out.fillBranch('VBFjjResol_dEta', self._VBFjjResol_dEta)
        self.out.fillBranch('VBFjjResol_mjj',  self._VBFjjResol_mjj)
        self.out.fillBranch('VBFjjResol_dEta', self._VBFjjResol_dEta)
        self.out.fillBranch('max_mjj_Resol',   self._max_mjj_Resol)

        
        self.out.fillBranch('lnjj_pt',   self._lnjj_pt)
        self.out.fillBranch('lnjj_mass', self._lnjj_mass)
        self.out.fillBranch('lnjj_Mt',   self._lnjj_Mt)
        self.out.fillBranch('minPtWOverMlnjj',self._minPtWOverMlnjj)
        self.out.fillBranch('maxPtWOverMlnjj',self._maxPtWOverMlnjj)
        self.out.fillBranch('dR_l_Whad',     self._dR_l_Whad)
        self.out.fillBranch('dR_Wlep_Whad',  self._dR_Wlep_Whad)
        self.out.fillBranch('dPhi_l_Whad',   self._dPhil_Whad)
        self.out.fillBranch('dPhi_Wlep_Whad',self._dPhiWlep_Whad)









        #print "End of fllbranch"




    def CookME(self):
	# particle ids
	lepId = self._Lepton.pdgId
	if lepId > 0:
	  neutId = -lepId -1
	  WlepId   = 24
	  WhadId = -24
	else :
	  neutId = -lepId + 1
	  WlepId   = -24
	  WhadId = 24
	#print "lep, neut", lepId, neutId

        #Boost_h_ids = ROOT.vector('int')()
        #Boost_h_4Vs = ROOT.vector('TLorentzVector')()

        #Boost_h_ids.push_back(int(25)) 
	#Boost_h_4Vs.push_back(self._lnJ_4v)

        Boost_hDa_ids = ROOT.vector('int')()
        Boost_hDa_4Vs = ROOT.vector('TLorentzVector')()

        Boost_hDa_ids.push_back(int(WlepId)) 
	Boost_hDa_4Vs.push_back(self._Wlep_4v)
        Boost_hDa_ids.push_back(int(WhadId)) 
	Boost_hDa_4Vs.push_back(self._FinalFatJet_4v)

	Boost_WWda_ids = ROOT.vector('int')()
	Boost_WWda_4Vs = ROOT.vector('TLorentzVector')()

	Boost_WWda_ids.push_back(int(lepId))
	Boost_WWda_4Vs.push_back(self._lepton_4v)

	Boost_WWda_ids.push_back(int(neutId))
	Boost_WWda_4Vs.push_back(self._MET_4v)

	Boost_WWda_ids.push_back(int(0))
	Boost_WWda_4Vs.push_back(self._subJet1_4v)

	Boost_WWda_ids.push_back(int(0))
	Boost_WWda_4Vs.push_back(self._subJet2_4v)

	Res_hDa_ids = ROOT.vector('int')()
	Res_hDa_4Vs = ROOT.vector('TLorentzVector')()
	Res_hDa_ids.push_back(int(WlepId))
	Res_hDa_4Vs.push_back(self._Wlep_4v)
	Res_hDa_ids.push_back(int(WhadId))
	Res_hDa_4Vs.push_back(self._Whad_4v)

	Res_WWda_ids = ROOT.vector('int')()
	Res_WWda_4Vs = ROOT.vector('TLorentzVector')()

	Res_WWda_ids.push_back(int(lepId))
	Res_WWda_4Vs.push_back(self._lepton_4v)

	Res_WWda_ids.push_back(int(neutId))
	Res_WWda_4Vs.push_back(self._MET_4v)

	Res_WWda_ids.push_back(int(0))
	Res_WWda_4Vs.push_back(self._Whad_j1_4v)

	Res_WWda_ids.push_back(int(0))
	Res_WWda_4Vs.push_back(self._Whad_j2_4v)


        for mH in Masses:
          gsm = self.g.GetBinContent(self.g.FindBin(mH))
	  self.mela.setMelaHiggsMassWidth(mH, gsm)
	  # variable initialization
          P_BstVBF_vbf_S = -1
          P_BstVBF_vbf_B = -1
          P_BstVBF_ggf_S = -1
          P_BstVBF_ggf_B = -1

          P_BstNoT_vbf_S = -1
          P_BstNoT_vbf_B = -1
          P_BstNoT_ggf_S = -1
          P_BstNoT_ggf_B = -1

          P_ResVBF_vbf_S = -1
          P_ResVBF_vbf_B = -1
          P_ResVBF_ggf_S = -1
          P_ResVBF_ggf_B = -1

          P_ResNoT_vbf_S = -1
          P_ResNoT_vbf_B = -1
          P_ResNoT_ggf_S = -1
          P_ResNoT_ggf_B = -1

	  if self.debug:
	    print "Probability for mass",mH

          allCut_BoostSR_VBF = [
              self._isBoostSR and self._isVBF_Boost and len(self._BJetBoostVBF_cjidx) ==0
              ]
          allCut_BoostSR_NonVBF = [
              self._isBoostSR and not self._isVBF_Boost and len(self._BJetBoost_cjidx) ==0
              ]
          allCut_ResolSR_VBF = [
              self._isResolSR and  self._isVBF_Resol and len(self._BJetResolVBF_cjidx) ==0
              ]
          allCut_ResolSR_NonVBF = [
              self._isResolSR and  not self._isVBF_Resol and len(self._BJetResol_cjidx) ==0
              ]
          if all( allCut_BoostSR_VBF ) :###### BstVBF #################
	    pass
	    #if self.debug:
	    #  print "allCut_BoostSR_VBF begin"
	    #  print self.evtMyNum

	    #VBF_associate_ids = ROOT.vector('int')()
	    #VBF_associate_4Vs = ROOT.vector('TLorentzVector')() 
	    #
	    #VBF_associate_ids.push_back(int(0))
	    #VBF_associate_4Vs.push_back(self._VBFBoost_jet1_4v)
	    #VBF_associate_ids.push_back(int(0))
	    #VBF_associate_4Vs.push_back(self._VBFBoost_jet2_4v)
	  
	    #self.mela.setCandidateDecayMode(ROOT.TVar.CandidateDecay_WW)

	    #if self.debug:
	    #  print "BstVBF tag: VBF meP calculation" 
	    #self.mela.setupDaughtersNoMom(
	    #    True,
	    #    Boost_WWda_ids, Boost_WWda_4Vs,
	    #    VBF_associate_ids, VBF_associate_4Vs,
	    #    False )
	    #self.mela.setCurrentCandidateFromIndex(int(0))
	    #P_BstVBF_vbf_S = self.mela.computeDecP(ROOT.TVar.HSMHiggs, ROOT.TVar.MCFM, False)
	    #P_BstVBF_vbf_B = self.mela.computeDecP(ROOT.TVar.bkgWW,    ROOT.TVar.MCFM, True)

            #if self.debug:
	    #  print "ggF prob. calculation"
	    #self.mela.setupDaughtersNoMom(
	    #    False,
	    #    Boost_WWda_ids, Boost_WWda_4Vs,
	    #    VBF_associate_ids, VBF_associate_4Vs,
	    #    False )
	    #self.mela.setCurrentCandidateFromIndex(int(0))
	    ## TVar.CandidateDecay_Stable case: h->WW, ProdP : just 0 
	    ## TVar.CandidateDecay_Stable case: h->WW, DecP :  not supported
	    ## TVar.CandidateDecay_WW     case: h->WW, DecP :  not supported
	    ## TVar.CandidateDecay_WW     case: h->WW, ProdP : not supported
	    #P_BstVBF_ggf_S = self.mela.computeDecP(ROOT.TVar.HSMHiggs, ROOT.TVar.MCFM, False)
	    #P_BstVBF_ggf_B = self.mela.computeDecP(ROOT.TVar.bkgWW,    ROOT.TVar.MCFM, True)
	    #if self.debug:
	    #  print "allCut_BoostSR_VBF ------------------"
	    #  print self.evtMyNum
	    #  print 'P_BstVBF_vbf_S',P_BstVBF_vbf_S,'P_BstVBF_vbf_B',P_BstVBF_vbf_B,'P_BstVBF_ggf_S',P_BstVBF_ggf_S,'P_BstVBF_ggf_B',P_BstVBF_ggf_B
	  elif all( allCut_BoostSR_NonVBF ): ############## BstNoT ############
	    if self.debug:
	      print "allCut_BoostSR_NoVBF begin"
	    NoVBF_associate_ids = ROOT.vector('int')()
	    NoVBF_associate_4Vs = ROOT.vector('TLorentzVector')()
            tmp_4V = ROOT.TLorentzVector()
	    for i_noFat in range(0, self._CleanJetNotFat_col._len):
              cj_idx=self._CleanJetNotFat_col[i_noFat].jetIdx
	      pt, eta, phi, mass = self.CleanJet_PtEtaPhiM(cj_idx)
	      if pt < self.cut_jet_pt: continue
              if abs(eta) > self.cut_jet_eta : continue
	      tmp_4V.SetPtEtaPhiM(pt, eta, phi, mass)
	      NoVBF_associate_ids.push_back( int(0) )
	      NoVBF_associate_4Vs.push_back( tmp_4V )
            if self.debug:
	      print "check VBF prob."
	    self.mela.setCandidateDecayMode(ROOT.TVar.CandidateDecay_Stable)
	    self.mela.setupDaughtersNoMom(
	        True,
	        Boost_hDa_ids, Boost_hDa_4Vs,
	        NoVBF_associate_ids, NoVBF_associate_4Vs,
	        False )
	    self.mela.setCurrentCandidateFromIndex(int(0))
	    P_BstNoT_vbf_S = self.mela.computeProdP(ROOT.TVar.HSMHiggs, ROOT.TVar.JHUGen, False)
	    P_BstNoT_vbf_B = self.mela.computeProdP(ROOT.TVar.bkgWW,    ROOT.TVar.JHUGen, True)
	    if self.debug:
	      print "check ggf prob."
	    self.mela.setCandidateDecayMode(ROOT.TVar.CandidateDecay_WW)
	    self.mela.setupDaughtersNoMom(
	        False,
	        Boost_WWda_ids, Boost_WWda_4Vs,
	        NoVBF_associate_ids, NoVBF_associate_4Vs,
	        False )
	    self.mela.setCurrentCandidateFromIndex(int(0))
	    # TVar.CandidateDecay_Stable case: h->WW, ProdP : just 0 
	    # TVar.CandidateDecay_Stable case: h->WW, DecP :  not supported
	    # TVar.CandidateDecay_WW     case: h->WW, DecP :  not supported
	    # TVar.CandidateDecay_WW     case: h->WW, ProdP : not supported
	    #mePgg = self.mela.computeProdP(ROOT.TVar.HSMHiggs, ROOT.TVar.JHUGen, True)
	    P_BstNoT_ggf_S = self.mela.computeDecP(ROOT.TVar.HSMHiggs, ROOT.TVar.MCFM, False)
	    P_BstNoT_ggf_B = self.mela.computeDecP(ROOT.TVar.bkgWW,    ROOT.TVar.MCFM, True)
	    if self.debug:
	      print "NoVBF boost prob ==========================================="
	      print self.evtMyNum
	      print "P_BstNoT_vbf_S",P_BstNoT_vbf_S,"P_BstNoT_vbf_B",P_BstNoT_vbf_B,"P_BstNoT_ggf_S",P_BstNoT_ggf_S,"P_BstNoT_ggf_B",P_BstNoT_ggf_B

	  elif all( allCut_ResolSR_VBF ): ############ Resol  VBF #############
	    pass
	    #if self.debug:
	    #  print "allCut_ResolSR_VBF begin"
	    #ResVbf_as_ids = ROOT.vector('int')()
	    #ResVbf_as_4Vs = ROOT.vector('TLorentzVector')()

	    #tmp_4V = self.CleanJet_4V(self._VBFjjResol_cjidx1)
	    #ResVbf_as_ids.push_back(int(0))
	    #ResVbf_as_4Vs.push_back(tmp_4V)
	    #tmp_4V = self.CleanJet_4V(self._VBFjjResol_cjidx2)
	    #ResVbf_as_ids.push_back(int(0))
	    #ResVbf_as_4Vs.push_back(tmp_4V)

	    #self.mela.setCandidateDecayMode(ROOT.TVar.CandidateDecay_WW)
            #
	    #if self.debug:
	    #  print "Resol vbf meP"
	    #self.mela.setupDaughtersNoMom(
	    #    True,
	    #    Res_WWda_ids, Res_WWda_4Vs,
	    #    ResVbf_as_ids, ResVbf_as_4Vs,
	    #    False )
	    #self.mela.setCurrentCandidateFromIndex(int(0))
	    #P_ResVBF_vbf_S = self.mela.computeDecP(ROOT.TVar.HSMHiggs, ROOT.TVar.MCFM, False)
	    #P_ResVBF_vbf_B = self.mela.computeDecP(ROOT.TVar.bkgWW,    ROOT.TVar.MCFM, True)
	    #if self.debug:
	    #  print "Resol ggf meP"
	    #self.mela.setupDaughtersNoMom(
	    #    False,
	    #    Res_WWda_ids, Res_WWda_4Vs,
	    #    ResVbf_as_ids, ResVbf_as_4Vs,
	    #    False )
	    #self.mela.setCurrentCandidateFromIndex(int(0))
	    #P_ResVBF_ggf_S = self.mela.computeDecP(ROOT.TVar.HSMHiggs, ROOT.TVar.MCFM, False)
	    #P_ResVBF_ggf_B = self.mela.computeDecP(ROOT.TVar.bkgWW,    ROOT.TVar.MCFM, True)
	    #if self.debug:
	    #  print "ResolVBF  ==========================================="
	    #  print self.evtMyNum
	    #  print "P_ResVBF_vbf_S",P_ResVBF_vbf_S,"P_ResVBF_vbf_B",P_ResVBF_vbf_B,"P_ResVBF_ggf_S",P_ResVBF_ggf_S,"P_ResVBF_ggf_B",P_ResVBF_ggf_B

	  elif all( allCut_ResolSR_NonVBF ): ############ Resol NonVBF ################
	    if self.debug:
	      print "allCut_ResolSR_NoT begin"
	    ResNoVbf_as_ids = ROOT.vector('int')()
	    ResNoVbf_as_4Vs = ROOT.vector('TLorentzVector')()
            tmp_4V = ROOT.TLorentzVector()
	    for i_cj in range(0, self._CleanJet_col._len):
	      if i_cj in [self._Whad_cjidx1, self._Whad_cjidx2 ]: continue
	      tmp_4V = self.CleanJet_4V(i_cj)
	      if tmp_4V.Pt()  < self.cut_jet_pt: continue
	      if abs(tmp_4V.Eta()) < self.cut_jet_pt: continue
	      ResNoVbf_as_ids.push_back( int(0) )
	      ResNoVbf_as_4Vs.push_back( tmp_4V )
            if self.debug:
	      print "meP vbf"
	    self.mela.setCandidateDecayMode(ROOT.TVar.CandidateDecay_Stable)
	    self.mela.setupDaughtersNoMom(
	        True,
	        Res_hDa_ids, Res_hDa_4Vs,
	        ResNoVbf_as_ids, ResNoVbf_as_4Vs,
	        False )
	    self.mela.setCurrentCandidateFromIndex(int(0))
	    # VBF can not use ProdDecP  with JHUGen, JHUGen possible for vbf prod, and ggHWW
	    P_ResNoT_vbf_S = self.mela.computeProdP(ROOT.TVar.HSMHiggs, ROOT.TVar.JHUGen, False)
	    P_ResNoT_vbf_B = self.mela.computeProdP(ROOT.TVar.bkgWW,    ROOT.TVar.JHUGen, True)
           
	    if self.debug:
	      print "meP ggf"
	    self.mela.setCandidateDecayMode(ROOT.TVar.CandidateDecay_WW)
	    self.mela.setupDaughtersNoMom(
	        False,
	        Res_WWda_ids, Res_WWda_4Vs,
	        ResNoVbf_as_ids, ResNoVbf_as_4Vs,
	        False )
	    self.mela.setCurrentCandidateFromIndex(int(0))
	    P_ResNoT_ggf_S = self.mela.computeDecP(ROOT.TVar.HSMHiggs, ROOT.TVar.MCFM, False)
	    P_ResNoT_ggf_B = self.mela.computeDecP(ROOT.TVar.bkgWW,    ROOT.TVar.MCFM, True)
	    if self.debug:
	      print "Resol NoVBF prob ==========================================="
	      print self.evtMyNum
	      print "P_ResNoT_vbf_S", P_ResNoT_vbf_S,"P_ResNoT_vbf_B",P_ResNoT_vbf_B,"P_ResNoT_ggf_S",P_ResNoT_ggf_S,"P_ResNoT_ggf_B",P_ResNoT_ggf_B

	  else: pass

          self.out.fillBranch('meP'+ str(mH) + '_BstVBF_vbf_S',   P_BstVBF_vbf_S)
          self.out.fillBranch('meP'+ str(mH) + '_BstVBF_vbf_B',   P_BstVBF_vbf_B)
          self.out.fillBranch('meP'+ str(mH) + '_BstVBF_ggf_S',   P_BstVBF_ggf_S)
          self.out.fillBranch('meP'+ str(mH) + '_BstVBF_ggf_B',   P_BstVBF_ggf_B)

          self.out.fillBranch('meP'+ str(mH) + '_BstNoT_vbf_S',   P_BstNoT_vbf_S)
          self.out.fillBranch('meP'+ str(mH) + '_BstNoT_vbf_B',   P_BstNoT_vbf_B)
          self.out.fillBranch('meP'+ str(mH) + '_BstNoT_ggf_S',   P_BstNoT_ggf_S)
          self.out.fillBranch('meP'+ str(mH) + '_BstNoT_ggf_B',   P_BstNoT_ggf_B)

          self.out.fillBranch('meP'+ str(mH) + '_ResVBF_vbf_S',   P_ResVBF_vbf_S)
          self.out.fillBranch('meP'+ str(mH) + '_ResVBF_vbf_B',   P_ResVBF_vbf_B)
          self.out.fillBranch('meP'+ str(mH) + '_ResVBF_ggf_S',   P_ResVBF_ggf_S)
          self.out.fillBranch('meP'+ str(mH) + '_ResVBF_ggf_B',   P_ResVBF_ggf_B)

          self.out.fillBranch('meP'+ str(mH) + '_ResNoT_vbf_S',   P_ResNoT_vbf_S)
          self.out.fillBranch('meP'+ str(mH) + '_ResNoT_vbf_B',   P_ResNoT_vbf_B)
          self.out.fillBranch('meP'+ str(mH) + '_ResNoT_ggf_S',   P_ResNoT_ggf_S)
          self.out.fillBranch('meP'+ str(mH) + '_ResNoT_ggf_B',   P_ResNoT_ggf_B)

              #daughter_coll = ROOT.SimpleParticleCollection_t()
            #accociated_coll = ROOT.SimpleParticleCollection_t()
            #daughter = ROOT.SimpleParticle_t(25, self._lnJ_4v)
            #associated1 = ROOT.SimpleParticle_t(0, self._VBFBoost_jet1_4v)
            #associated2 = ROOT.SimpleParticle_t(0, self._VBFBoost_jet2_4v)
            #daughter_coll.push_back(daughter)
            #associated_coll.push_back(associated1)
            #associated_coll.push_back(associated2)



    def getDeltaR(self, phi1, eta1, phi2, eta2):
        dphi = phi1 - phi2
        if dphi > ROOT.TMath.Pi(): dphi -= 2*ROOT.TMath.Pi()
        if dphi < -ROOT.TMath.Pi(): dphi += 2*ROOT.TMath.Pi()
        deta = eta1 - eta2
        deltaR = sqrt((deta*deta) + (dphi*dphi))
        return deltaR
    def InvMassCalc(self, pt0, eta0, phi0, mass0, pt1, eta1, phi1, mass1):
        v0 = ROOT.TLorentzVector()
        v1 = ROOT.TLorentzVector()
        v0.SetPtEtaPhiM(pt0, eta0, phi0, mass0)
        v1.SetPtEtaPhiM(pt1, eta1, phi1, mass1)
        InvM01 = (v0 + v1).M()
        return InvM01
    def WlepMetPzCalc(self, leptE, leptPt, leptPz, leptPhi, metPt, metPhi,  ):
        mu = ((Wmass)**2)/2 + leptPt * metPt * math.cos(metPhi-leptPhi)
        ## metPz solution = metPz_1 +-sqrt(metPz_2)
        metPz_1      = mu * leptPz/(leptPt**2)
        metPz_2_pow2 = metPz_1**2 - ( (leptE*metPt)**2 - mu**2 )/(leptPt**2)
        metPz=0
        ##--complex number case
        if metPz_2_pow2 < 0:
            metPz = metPz_1
        ##--real solution    
        else:
            sol1 = metPz_1 + math.sqrt(metPz_2_pow2)
            sol2 = metPz_1 - math.sqrt(metPz_2_pow2)
            if math.fabs(sol1) < math.fabs(sol2):
                metPz = sol1
            else:
                metPz = sol2

        return metPz
 


    def WlepMaker(self):
        lepton_pt  = self._Lepton.pt
        lepton_eta = self._Lepton.eta
        lepton_phi = self._Lepton.phi
        lepton_pz  = lepton_pt*math.sinh(lepton_eta)
        lepton_E   = lepton_pt*math.cosh(lepton_eta)
        self._lepton_4v.SetPtEtaPhiM(lepton_pt,lepton_eta,lepton_phi,0)

        met_pt  = self._MET_pt
        met_phi = self._MET_phi
        #print 'Wmass=',type(Wmass)
        #print 'lepton_pt=',type(lepton_pt)
        #print 'lepton_phi=',type(lepton_pt)
        #print 'met_pt=',type(met_pt)
        #print 'met_phi=',type(met_phi)
        mu = (Wmass*Wmass)/2 + lepton_pt*met_pt*math.cos(met_phi-lepton_phi)
        self._MET_pz1 = mu*lepton_pz/pow(lepton_pt,2)
        self._MET_pz2 = (  mu*lepton_pz/(lepton_pt**2)  )**2 - ( (lepton_E*met_pt)**2 - mu**2 )/(lepton_pt**2)

        #met_pz solution = met_pz_1 +-sqrt(met_pz_2)

        ##complex case
        if self._MET_pz2 < 0:
            self._MET_pz = self._MET_pz1
        else:
            sol1 = self._MET_pz1 + math.sqrt(self._MET_pz2)
            sol2 = self._MET_pz1 - math.sqrt(self._MET_pz2)
            if abs(sol1) < abs(sol2):
                self._MET_pz = sol1
                self._MET_bigZ = sol2
            else:
                self._MET_pz = sol2
                self._MET_bigZ = sol1

        met_px   =  met_pt*math.cos(met_phi)
        met_py   =  met_pt*math.sin(met_phi)
        met_E    =  math.sqrt(self._MET_pz**2 + met_pt**2)
        met_bigE =  math.sqrt(self._MET_bigZ**2 + met_pt**2)
        self._MET_4v.SetPxPyPzE(met_px, met_py, self._MET_pz ,met_E)
        self._MET_big4v.SetPxPyPzE(met_px, met_py, self._MET_bigZ ,met_bigE)

        wlep_px    = lepton_pt*math.cos(lepton_phi) + met_pt*math.cos(met_phi)
        wlep_py    = lepton_pt*math.sin(lepton_phi) + met_pt*math.sin(met_phi)
        wlep_pz    = lepton_pz + self._MET_pz
        wlep_bigPz = lepton_pz + self._MET_bigZ
        wlep_E     = lepton_E  + math.sqrt(self._MET_pz**2   + met_pt**2)
        wlep_bigE  = lepton_E  + math.sqrt(self._MET_bigZ**2 + met_pt**2)
        self._Wlep_4v.SetPxPyPzE(   wlep_px,wlep_py,wlep_pz,   wlep_E)
	# TODO use this big4v for the event test, which could enhence the mH resolution
        self._Wlep_big4v.SetPxPyPzE(wlep_px,wlep_py,wlep_bigPz,wlep_bigE)

        self._Wlep_Mt = math.sqrt(2*lepton_pt*met_pt*(1-math.cos(lepton_phi - met_phi ) ) )
        

    def FindWtaggerFatJet(self):
        ##self._CleanFatJet
        self._Wfatjet_cfjidx_list=[]
        self._Wfatjet_pt_list=[]
        self._Wfatjet_eta_list=[]
        self._Wfatjet_phi_list=[]
        self._Wfatjet_mass_list=[]
        self._Wfatjet_mindM_cfjidx=-1
        self._Wfatjet_mxPT_cfjidx=-1
        
        min_dM = MaxLimit
        max_pt = MinLimit
        N=self._CleanFatJet_col._len
        for i_fj in range(0,N):
            pt,eta,phi,mass=self.CleanFatJet_PtEtaPhiM(i_fj)
            tau21=self._CleanFatJet_col[i_fj].tau21
            cfatjet_jetIdx=self._CleanFatJet_col[i_fj].jetIdx
            fatjetid = self._FatJet_col[cfatjet_jetIdx].jetId

            if mass < self.Wmass_CRlow : continue
            if mass > self.Wmass_CRhigh : continue
            if tau21 > self.tau21WP : continue
            if abs(eta) > self.cut_fjet_eta : continue
            if pt < self.cut_fjet_pt : continue
            if fatjetid < self.min_fatjetid : continue
            self._Wfatjet_cfjidx_list.append(i_fj)
            self._Wfatjet_pt_list.append(pt)
            self._Wfatjet_eta_list.append(eta)
            self._Wfatjet_phi_list.append(phi)
            self._Wfatjet_mass_list.append(mass)
            self._Wfatjet_tau21_list.append(tau21)
            ##PT ordering
            if pt > max_pt :
	      max_pt = pt
	      self._Wfatjet_mxPT_cfjidx = i_fj

            tmp_dM = abs(Wmass - mass)
            if tmp_dM < min_dM :
	      min_dM = tmp_dM
	      self._Wfatjet_mindM_cfjidx = i_fj
	if min_dM  < MaxLimit: self._isBoost = True
        
    def GetBJetsBoost(self):
        ##->Set self._BJetBoost_cjidx
        #self._CleanJetNotFat_col
        bWP=self.bWP
        N = self._CleanJetNotFat_col._len
        for i_cj in range(0,N): ##-- i_cj = idx of self._CleanJetNotFat_col
            cj_idx=self._CleanJetNotFat_col[i_cj].jetIdx
            pt=self._CleanJet_col[cj_idx].pt
            eta=self._CleanJet_col[cj_idx].eta
            jet_idx=self._CleanJet_col[cj_idx].jetIdx
            bAlgo=self._Jet_col[jet_idx].btagDeepB
            if bAlgo < bWP:continue
            if pt < 20 :continue
            if abs(eta) > 2.5:continue
            self._BJetBoost_cjidx.append(cj_idx) ## fill index of CleanJet 
	    if self._isVBF_Boost:
	      if cj_idx not in [ self._VBFjjBoost_cjidx1, self._VBFjjBoost_cjidx2]:
		self._BJetBoostVBF_cjidx.append(cj_idx)

    def GetBJetsResol(self):
        ##->Set self._BJetResol_cjidx
        #self._CleanJet_col
        bWP=self.bWP
        N=self._CleanJet_col._len
        for i_cj in range(0,N):
            if i_cj == self._Whad_cjidx1 : continue
            if i_cj == self._Whad_cjidx2 : continue
            
            pt   = self._CleanJet_col[i_cj].pt
            eta  = self._CleanJet_col[i_cj].eta
            j_idx= self._CleanJet_col[i_cj].jetIdx ##Jet Object index
            bAlgo= self._Jet_col[j_idx].btagDeepB
            if bAlgo < bWP:continue
            if pt < self.cut_bjet_pt  :continue
            if abs(eta) > self.cut_bjet_eta:continue
            self._BJetResol_cjidx.append(i_cj) ## fill index of CleanJet
	    if self._isVBF_Resol:
	      if i_cj not in [self._VBFjjResol_cjidx1, self._VBFjjResol_cjidx2]:
		self._BJetResolVBF_cjidx.append(i_cj)
            



    def VBF_Boost(self):
        N=self._CleanJetNotFat_col._len
        if N < 2 :
            #print "NCleanJet < 2"
            self._isVBF_Boost = False
            return
        
        for i_cj in range(0,N):
            cjidx1 = self._CleanJetNotFat_col[i_cj].jetIdx ##index of CleanJet
            pt1,eta1,phi1,mass1 = self.CleanJet_PtEtaPhiM(cjidx1)
            if pt1 < self.cut_VBFjet_pt : continue
            if abs(eta1) > self.cut_VBFjet_eta : continue
            
            for j_cj in range(0,N):
                if j_cj <= i_cj : continue ##aviod doubly checked or the same one
                cjidx2 = self._CleanJetNotFat_col[j_cj].jetIdx ##index of CleanJet
                pt2,eta2,phi2,mass2 = self.CleanJet_PtEtaPhiM(cjidx2)
                if pt2 < self.cut_VBFjet_pt: continue
                if abs(eta2) > self.cut_VBFjet_eta : continue

                ##Set momentum##
                #print "Boost forward pair, "
                this_dEta=abs(eta1-eta2)
                this_mjj = self.InvMassCalc(pt1,eta1,phi1,mass1,pt2,eta2,phi2,mass2)
                #print "this_dEta=",this_dEta
                #print "this_mjj=",this_mjj
		# Select the biggest mjj as VBFjj
                if (this_dEta > self.cut_VBF_dEta) and (this_mjj > self._VBFjjBoost_mjj) : 
                    self._VBFjjBoost_dEta = this_dEta
                    self._VBFjjBoost_mjj = this_mjj
                    self._VBFjjBoost_cjidx1 = cjidx1
                    self._VBFjjBoost_cjidx2 = cjidx2
                    self._VBFBoost_jet1_4v.SetPtEtaPhiM(pt1, eta1, phi1, mass1)
                    self._VBFBoost_jet2_4v.SetPtEtaPhiM(pt2, eta2, phi2, mass2)
		# the biggest mjj for either VBF or non-VBF
                if this_mjj > self._max_mjj_Boost:
                    self._max_mjj_Boost = this_mjj

        ##--End of jet pair loop
        if self._VBFjjBoost_mjj > self.cut_VBF_mjj : self._isVBF_Boost = True

    def VBF_Resol(self):
        if not self._isResol:
            self._isVBF_Resol = False
	    return
        #N = self._CleanJetNotFat_col._len bug?
        N=self._CleanJet_col._len
        #if N < 2 : ## could it be 4 ? bug?
        if N < 4 : 
            self._isVBF_Resol = False
            return

        for i_cj in range(0,N):
	    if i_cj in [self._Whad_cjidx1, self._Whad_cjidx2]:
	      #print "cjet id", i_cj,"is in",self._Whad_cjidx1, self._Whad_cjidx2
	      continue 
            pt1,eta1,phi1,mass1 = self.CleanJet_PtEtaPhiM(i_cj)
            if pt1 < self.cut_VBFjet_pt : continue
            if abs(eta1) > self.cut_VBFjet_eta : continue

            for j_cj in range(0,N):
                if j_cj <= i_cj : continue ##doubly checked or the same one
	        if j_cj in [self._Whad_cjidx1, self._Whad_cjidx2]: continue
                
                pt2,eta2,phi2,mass2 = self.CleanJet_PtEtaPhiM(j_cj)
                if pt2 < self.cut_VBFjet_pt: continue
                if abs(eta2) > self.cut_VBFjet_eta : continue

                ##Set momentum##

                this_dEta=abs(eta1-eta2)
                this_mjj = self.InvMassCalc(pt1,eta1,phi1,mass1,pt2,eta2,phi2,mass2)
                if (this_dEta > self.cut_VBF_dEta) and (this_mjj > self._VBFjjResol_mjj) :
                    self._VBFjjResol_dEta = this_dEta
                    self._VBFjjResol_mjj = this_mjj
                    self._VBFjjResol_cjidx1 = i_cj
                    self._VBFjjResol_cjidx2 = j_cj
                if this_mjj > self._max_mjj_Resol:
                    self._max_mjj_Resol = this_mjj

        ##--End of jet pair loop
        if self._VBFjjResol_mjj > self.cut_VBF_mjj : self._isVBF_Resol = True


    def WhadMaker(self):
        N = self._CleanJet_col._len
        dM = MaxLimit
        Whad_mass = MinLimit
        v1=ROOT.TLorentzVector()
        v2=ROOT.TLorentzVector()
        for i_cj in range(0,N):
            pt1,eta1,phi1,mass1 = self.CleanJet_PtEtaPhiM(i_cj)
            if pt1 < self.cut_jet_pt : continue
            if abs(eta1) > self.cut_jet_eta : continue 
            for j_cj in range(0,N):
                if j_cj <= i_cj : continue
                pt2,eta2,phi2,mass2 = self.CleanJet_PtEtaPhiM(j_cj)
                if pt2 < self.cut_jet_pt  : continue
                if abs(eta2) > self.cut_jet_eta : continue
                v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
                v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2)
                
                this_M=(v1+v2).M()
                this_dM=abs(Wmass-this_M)
                if this_dM < dM:
                    dM = this_dM
                    self._Whad_cjidx1 = i_cj
                    self._Whad_cjidx2 = j_cj
                    self._Whad_4v = v1+v2
		    self._Whad_j1_4v = v1
		    self._Whad_j2_4v = v2
        if dM < MaxLimit:
	  self._isResol = True
          ##DeltaR, DeltaPhi between l - Whad OR Wlep - Whad
          self._dR_l_Whad      = self._Whad_4v.DeltaR(self._lepton_4v)
          self._dR_Wlep_Whad   = self._Whad_4v.DeltaR(self._Wlep_4v)
          self._dPhil_Whad     = self._Whad_4v.DeltaPhi(self._lepton_4v)
          self._dPhiWlep_Whad  = self._Whad_4v.DeltaPhi(self._Wlep_4v)

        if self._Whad_cjidx1 < 0 :
	  self._isResol   = False #for safty
        if self._Whad_cjidx2 < 0 :
	  self._isResol   = False #for safty
 
    def CookLnJ(self):
        if not self._isBoost: return
        self._FatSel_cfjidx['mindM'] = self._Wfatjet_mindM_cfjidx
        self._FatSel_cfjidx['mxPT']  = self._Wfatjet_mxPT_cfjidx

        tmp_FatJet_4v= ROOT.TLorentzVector()

        for sel in self._FatSel_cfjidx:# loop twice for mindM and mxPT
            cfatjet_idx=self._FatSel_cfjidx[sel]
            if cfatjet_idx >= 0:
                
                WfatPt, WfatEta, WfatPhi, WfatMass = self.CleanFatJet_PtEtaPhiM(cfatjet_idx)
                tmp_FatJet_4v.SetPtEtaPhiM(WfatPt,WfatEta,WfatPhi,WfatMass) ##FatJet vector
                H_4v    = self._Wlep_4v    + tmp_FatJet_4v ## sum Wlep + Whad
                H_big4v = self._Wlep_big4v + tmp_FatJet_4v ## sum Wlep + Whad
                lnJ_pt=H_4v.Pt()
                lnJ_mass=H_4v.M()
                ##--additional cut
                minPtWOverMlnJ = min(self._Wlep_4v.Pt(), tmp_FatJet_4v.Pt())/lnJ_mass
                maxPtWOverMlnJ = max(self._Wlep_4v.Pt(), tmp_FatJet_4v.Pt())/lnJ_mass
                ##DeltaR, DeltaPhi between l - Fat OR Wlep - Fat
                
                dR_l_F    = tmp_FatJet_4v.DeltaR(self._lepton_4v)
                dR_Wlep_F = tmp_FatJet_4v.DeltaR(self._Wlep_4v)
                
                dPhi_l_F    = tmp_FatJet_4v.DeltaPhi(self._lepton_4v)
                dPhi_Wlep_F = tmp_FatJet_4v.DeltaPhi(self._Wlep_4v)
		########################
		#### Event Catagory ####
		########################
		if sel == "mindM":
		  #print "mindM case"
                  fatjetIdx=self._CleanFatJet_col[cfatjet_idx].jetIdx
                  subJetI1 = self._FatJet_col[fatjetIdx].subJetIdx1
                  subJetI2 = self._FatJet_col[fatjetIdx].subJetIdx2
		  self._subJet1_4v = self.SubJet_4V(subJetI1)
		  self._subJet2_4v = self.SubJet_4V(subJetI2)
		  fatjetAgain_4V = self._subJet1_4v + self._subJet2_4v
		  #print "fatjetAgain"
		  #print fatjetAgain_4V.Pt(), fatjetAgain_4V.Eta(), fatjetAgain_4V.Phi(), fatjetAgain_4V.M()
		  #print WfatPt, WfatEta, WfatPhi, WfatMass
		  #print self._FatJet_col[fatjetIdx].pt, self._FatJet_col[fatjetIdx].eta, self._FatJet_col[fatjetIdx].phi, self._FatJet_col[fatjetIdx].mass

                  self._lnJ_4v    = H_4v
		  # TODO
                  self._lnJ_big4v = H_big4v
		  self._FinalFatJet_4v = tmp_FatJet_4v
	          cut_Boost_Base  = [ \
		      self._MET_pt    > self.METcut_Boost and \
		      minPtWOverMlnJ > self.cut_minPtWOverMlnJ ]
		  cut_Boost_SB = [ \
		      WfatMass < self.Wmass_CRhigh and \
		      WfatMass > self.Wmass_CRlow]
		  cut_Boost_SR = [ \
		      WfatMass < self.Wmass_SRhigh and \
		      WfatMass > self.Wmass_SRlow]
		  if all(cut_Boost_Base) and all(cut_Boost_SB):
                    self._isBoostSB = True
		  if all(cut_Boost_Base) and all(cut_Boost_SR):
                    self._isBoostSR = True
            else:
                lnJ_pt =  MinLimit
                lnJ_mass= MinLimit
                minPtWOverMlnJ = MinLimit
                maxPtWOverMlnJ = MinLimit
                dR_l_F    = MinLimit
                dR_Wlep_F = MinLimit
                dR_l_F    = MinLimit
                dR_Wlep_F = MinLimit

            # All cases should be filled even with default values
            self.out.fillBranch('lnJ_pt_'+sel, lnJ_pt)
            self.out.fillBranch('lnJ_mass_'+sel, lnJ_mass)
            self.out.fillBranch('minPtWOverMlnJ_'+sel, minPtWOverMlnJ)##additional cut
            self.out.fillBranch('maxPtWOverMlnJ_'+sel, maxPtWOverMlnJ)
            self.out.fillBranch('dR_l_F_'+sel, dR_l_F)
            self.out.fillBranch('dR_Wlep_F_'+sel, dR_Wlep_F)
            self.out.fillBranch('dPhi_l_F_'+sel, dR_l_F)
            self.out.fillBranch('dPhi_Wlep_F'+sel, dR_Wlep_F)


    def CookLnjj(self):
        if not self._isResol : return
        self._lnjj_4v    = self._Wlep_4v    + self._Whad_4v
	# TODO
        self._lnjj_big4v = self._Wlep_big4v + self._Whad_4v
        self._lnjj_pt   = self._lnjj_4v.Pt()
        self._lnjj_mass = self._lnjj_4v.M()
        self._minPtWOverMlnjj = min(self._Wlep_4v.Pt(), self._Whad_4v.Pt())/self._lnjj_mass
        self._maxPtWOverMlnjj = max(self._Wlep_4v.Pt(), self._Whad_4v.Pt())/self._lnjj_mass

        Ljj_4v = self._lepton_4v + self._Whad_4v
	Ljj_pt = Ljj_4v.Pt()
	self._lnjj_Mt = math.sqrt(2.* Ljj_pt*self._MET_pt * (1. - math.cos( Ljj_4v.DeltaPhi(self._MET_4v)) ))

        Whad_mass     = self._Whad_4v.M()

	#print "Mts", self._lnjj_Mt, self._Wlep_Mt

	cut_Resol_Base = [ 
	    self._MET_pt          > self.METcut_Resol and  
	    self._minPtWOverMlnjj > self.cut_minPtWOverMlnjj and
	    self._lnjj_Mt         > self.cut_lnjj_Mt  and
	    self._Wlep_Mt         > self.cut_Wlep_Mt
	    ]
	cut_Resol_SB = [ \
	    Whad_mass > self.Wmass_CRlow and \
	    Whad_mass < self.Wmass_CRhigh ]
	cut_Resol_SR = [ \
	    Whad_mass > self.Wmass_SRlow and \
	    Whad_mass < self.Wmass_SRhigh ]
	if all(cut_Resol_Base) and all(cut_Resol_SB):
          self._isResolSB = True
	if all(cut_Resol_Base) and all(cut_Resol_SR):
          self._isResolSR = True



    def CleanJet_PtEtaPhiM(self,cjidx):
        pt=self._CleanJet_col[cjidx].pt
        eta=self._CleanJet_col[cjidx].eta
        phi=self._CleanJet_col[cjidx].phi
        jidx=self._CleanJet_col[cjidx].jetIdx
        mass=self._Jet_col[jidx].mass
        return pt,eta,phi,mass

    def CleanJet_4V(self,cjidx):
        pt=self._CleanJet_col[cjidx].pt
        eta=self._CleanJet_col[cjidx].eta
        phi=self._CleanJet_col[cjidx].phi
        jidx=self._CleanJet_col[cjidx].jetIdx
        mass=self._Jet_col[jidx].mass
        tmp_4V = ROOT.TLorentzVector()
	tmp_4V.SetPtEtaPhiM(pt, eta, phi, mass)
        return tmp_4V

    def CleanFatJet_PtEtaPhiM(self,cfjidx):
        pt=self._CleanFatJet_col[cfjidx].pt
        eta=self._CleanFatJet_col[cfjidx].eta
        phi=self._CleanFatJet_col[cfjidx].phi
        mass=self._CleanFatJet_col[cfjidx].mass
        
        return pt,eta,phi,mass

    def Jet_4V(self,jidx):
        pt  = self._Jet_col[jidx].pt
        eta = self._Jet_col[jidx].eta
        phi = self._Jet_col[jidx].phi
        mass= self._Jet_col[jidx].mass
        tmp_4V = ROOT.TLorentzVector()
	tmp_4V.SetPtEtaPhiM(pt, eta, phi, mass)
        return tmp_4V

    def SubJet_4V(self,jidx):
        pt  = self._SubJet_col[jidx].pt
        eta = self._SubJet_col[jidx].eta
        phi = self._SubJet_col[jidx].phi
        mass= self._SubJet_col[jidx].mass
        tmp_4V = ROOT.TLorentzVector()
	tmp_4V.SetPtEtaPhiM(pt, eta, phi, mass)
        return tmp_4V

    def MakeMassVsGamma(self):
        # Non-CPS values from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR2014 for up to 1000 GeV
        Hmass = [80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0,
                 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0,
                 100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 109.0,
                 110.0, 110.5, 111.0, 111.5, 112.0, 112.5, 113.0, 113.5, 114.0, 114.5,
                 115.0, 115.5, 116.0, 116.5, 117.0, 117.5, 118.0, 118.5, 119.0, 119.5,

                 120.0, 120.1, 120.2, 120.3, 120.4, 120.5, 120.6, 120.7, 120.8, 120.9,
                 121.0, 121.1, 121.2, 121.3, 121.4, 121.5, 121.6, 121.7, 121.8, 121.9,
                 122.0, 122.1, 122.2, 122.3, 122.4, 122.5, 122.6, 122.7, 122.8, 122.9,
                 123.0, 123.1, 123.2, 123.3, 123.4, 123.5, 123.6, 123.7, 123.8, 123.9,
                 124.0, 124.1, 124.2, 124.3, 124.4, 124.5, 124.6, 124.7, 124.8, 124.9,

                 125.0, 125.1, 125.2, 125.3, 125.4, 125.5, 125.6, 125.7, 125.8, 125.9,
                 126.0, 126.1, 126.2, 126.3, 126.4, 126.5, 126.6, 126.7, 126.8, 126.9,
                 127.0, 127.1, 127.2, 127.3, 127.4, 127.5, 127.6, 127.7, 127.8, 127.9,
                 128.0, 128.1, 128.2, 128.3, 128.4, 128.5, 128.6, 128.7, 128.8, 128.9,
                 129.0, 129.1, 129.2, 129.3, 129.4, 129.5, 129.6, 129.7, 129.8, 129.9,

                 130.0, 130.5, 131.0, 131.5, 132.0, 132.5, 133.0, 133.5, 134.0, 134.5,
                 135.0, 135.5, 136.0, 136.5, 137.0, 137.5, 138.0, 138.5, 139.0, 139.5,
                 140.0, 140.5, 141.0, 141.5, 142.0, 142.5, 143.0, 143.5, 144.0, 144.5,
                 145.0, 145.5, 146.0, 146.5, 147.0, 147.5, 148.0, 148.5, 149.0, 149.5,
                 150.0, 152.0, 154.0, 156.0, 158.0, 160.0, 162.0, 164.0, 165.0, 166.0,

                 168.0, 170.0, 172.0, 174.0, 175.0, 176.0, 178.0, 180.0, 182.0, 184.0,
                 185.0, 186.0, 188.0, 190.0, 192.0, 194.0, 195.0, 196.0, 198.0, 200.0,
                 202.0, 204.0, 206.0, 208.0, 210.0, 212.0, 214.0, 216.0, 218.0, 220.0,
                 222.0, 224.0, 226.0, 228.0, 230.0, 232.0, 234.0, 236.0, 238.0, 240.0,
                 242.0, 244.0, 246.0, 248.0, 250.0, 252.0, 254.0, 256.0, 258.0, 260.0,

                 262.0, 264.0, 266.0, 268.0, 270.0, 272.0, 274.0, 276.0, 278.0, 280.0,
                 282.0, 284.0, 286.0, 288.0, 290.0, 292.0, 294.0, 296.0, 298.0, 300.0,
                 305.0, 310.0, 315.0, 320.0, 325.0, 330.0, 335.0, 340.0, 345.0, 350.0,
                 360.0, 370.0, 380.0, 390.0, 400.0, 420.0, 440.0, 450.0, 460.0, 480.0,
                 500.0, 520.0, 540.0, 550.0, 560.0, 580.0, 600.0, 620.0, 640.0, 650.0,

                 660.0, 680.0, 700.0, 720.0, 740.0, 750.0, 760.0, 780.0, 800.0, 820.0,
                 840.0, 850.0, 860.0, 880.0, 900.0, 920.0, 940.0, 950.0, 960.0, 980.0,
                 1000.0, 1050.0, 1100.0, 1150.0, 1200.0, 1250.0, 1300.0, 1350.0, 1400.0, 1450.0,
                 1500.0, 1550.0, 1600.0, 1650.0, 1700.0, 1750.0, 1800.0, 1850.0, 1900.0, 1950.0,
                 2000.0, 2050.0, 2100.0, 2150.0, 2200.0, 2250.0, 2300.0, 2350.0, 2400.0, 2450.0,

                 2500.0, 2550.0, 2600.0, 2650.0, 2700.0, 2750.0, 2800.0, 2850.0, 2900.0, 2950.0,
                 3000.0, 3050.0, 3100.0, 3150.0, 3200.0, 3250.0, 3300.0, 3350.0, 3400.0, 3450.0,
                 3500.0, 3550.0, 3600.0, 3650.0, 3700.0, 3750.0, 3800.0, 3850.0, 3900.0, 3950.0,
                 4000.0, 4050.0, 4100.0, 4150.0, 4200.0, 4250.0, 4300.0, 4350.0, 4400.0, 4450.0,
                 4500.0, 4550.0, 4600.0, 4650.0, 4700.0, 4750.0, 4800.0, 4850.0, 4900.0, 4950.0, 5000.0]

        Hwidth = [0.00199, 0.00201, 0.00204, 0.00206, 0.00208, 0.00211, 0.00213, 0.00215, 0.00218, 0.0022,
                  0.00222, 0.00225, 0.00227, 0.0023, 0.00232, 0.00235, 0.00237, 0.0024, 0.00243, 0.00246,
                  0.00248, 0.00251, 0.00254, 0.00258, 0.00261, 0.00264, 0.00268, 0.00272, 0.00276, 0.0028,
                  0.00285, 0.00287, 0.00289, 0.00292, 0.00295, 0.00297, 0.003, 0.00303, 0.00306, 0.00309,
                  0.00312, 0.00315, 0.00319, 0.00322, 0.00326, 0.0033, 0.00333, 0.00338, 0.00342, 0.00346,

                  0.00351, 0.00352, 0.00352, 0.00353, 0.00354, 0.00355, 0.00356, 0.00357, 0.00358, 0.00359,
                  0.0036, 0.00361, 0.00362, 0.00363, 0.00364, 0.00365, 0.00366, 0.00367, 0.00368, 0.00369,
                  0.00371, 0.00372, 0.00373, 0.00374, 0.00375, 0.00376, 0.00377, 0.00378, 0.00379, 0.00381,
                  0.00382, 0.00383, 0.00384, 0.00385, 0.00386, 0.00388, 0.00389, 0.0039, 0.00391, 0.00393,
                  0.00394, 0.00395, 0.00396, 0.00398, 0.00399, 0.004, 0.00402, 0.00403, 0.00404, 0.00406,

                  0.00407, 0.00408, 0.0041, 0.00411, 0.00412, 0.00414, 0.00415, 0.00417, 0.00418, 0.0042,
                  0.00421, 0.00423, 0.00424, 0.00426, 0.00427, 0.00429, 0.0043, 0.00432, 0.00433, 0.00435,
                  0.00436, 0.00438, 0.0044, 0.00441, 0.00443, 0.00445, 0.00446, 0.00448, 0.0045, 0.00451,
                  0.00453, 0.00455, 0.00457, 0.00458, 0.0046, 0.00462, 0.00464, 0.00465, 0.00467, 0.00469,
                  0.00471, 0.00473, 0.00475, 0.00477, 0.00479, 0.00481, 0.00483, 0.00485, 0.00487, 0.00489,

                  0.00491, 0.00501, 0.00512, 0.00523, 0.00535, 0.00548, 0.0056, 0.00574, 0.00588, 0.00603,
                  0.00618, 0.00634, 0.00651, 0.00669, 0.00687, 0.00706, 0.00726, 0.00747, 0.0077, 0.00793,
                  0.00817, 0.00843, 0.0087, 0.00898, 0.00928, 0.00959, 0.00992, 0.0103, 0.0106, 0.011,
                  0.0114, 0.0119, 0.0123, 0.0128, 0.0133, 0.0139, 0.0145, 0.0151, 0.0158, 0.0165,
                  0.0173, 0.0211, 0.0266, 0.0351, 0.0502, 0.0831, 0.147, 0.215, 0.246, 0.276,

                  0.33, 0.38, 0.429, 0.477, 0.501, 0.525, 0.575, 0.631, 0.7, 0.788,
                  0.832, 0.876, 0.96, 1.04, 1.12, 1.2, 1.24, 1.28, 1.35, 1.43,
                  1.51, 1.59, 1.68, 1.76, 1.85, 1.93, 2.02, 2.12, 2.21, 2.31,
                  2.40, 2.50, 2.61, 2.71, 2.82, 2.93, 3.04, 3.16, 3.27, 3.40,
                  3.52, 3.64, 3.77, 3.91, 4.04, 4.18, 4.32, 4.46, 4.61, 4.76,

                  4.91, 5.07, 5.23, 5.39, 5.55, 5.72, 5.89, 6.07, 6.25, 6.43,
                  6.61, 6.80, 6.99, 7.19, 7.39, 7.59, 7.79, 8.00, 8.22, 8.43,
                  8.99, 9.57, 10.20, 10.80, 11.40, 12.10, 12.80, 13.50, 14.20, 15.20,
                  17.60, 20.20, 23.10, 26.10, 29.20, 35.90, 43.00, 46.80, 50.80, 59.10,
                  68.00, 77.50, 87.70, 93.00, 98.60, 110.00, 123.00, 136.00, 150.00, 158.00,

                  165.00, 182.00, 199.00, 217.00, 237.00, 247.00, 258.00, 280.00, 304.00, 330.00,
                  357.00, 371.00, 386.00, 416.00, 449.00, 484.00, 521.00, 540.00, 560.00, 602.00,
                  647.00, 525, 550, 575, 600, 625, 650, 675, 700, 725,
                  750, 775, 800, 825, 850, 875, 900, 925, 950, 975,
                  1000, 1025, 1050, 1075, 1100, 1125, 1150, 1175, 1200, 1225,

                  1250, 1275, 1300, 1325, 1350, 1375, 1400, 1425, 1450, 1475,
                  1500, 1525, 1550, 1575, 1600, 1625, 1650, 1675, 1700, 1725,
                  1750, 1775, 1800, 1825, 1850, 1875, 1900, 1925, 1950, 1975,
                  2000, 2025, 2050, 2075, 2100, 2125, 2150, 2175, 2200, 2225,
                  2250, 2275, 2300, 2325, 2350, 2375, 2400, 2425, 2450, 2475, 2500]

        # CPS values from https://github.com/latinos/LatinoAnalysis/blob/master/Gardener/python/variables/pwhg_cpHTO_reweight.f
        HmassCPS = [80.0, 82.0, 84.0, 86.0, 88.0, 90.0, 92.0, 94.0, 96.0, 98.0,
                    100.0, 102.0, 104.0, 106.0, 108.0, 110.0, 112.0, 114.0, 116.0, 118.0,
                    120.0, 122.0, 124.0, 125.0, 126.0, 128.0, 130.0, 132.0, 134.0, 136.0,
                    138.0, 140.0, 142.0, 144.0, 146.0, 148.0, 150.0, 152.0, 154.0, 156.0,
                    158.0, 160.0, 162.0, 164.0, 166.0, 168.0, 170.0, 172.0, 174.0, 176.0,

                    178.0, 180.0, 182.0, 184.0, 186.0, 188.0, 190.0, 192.0, 194.0, 196.0,
                    198.0, 200.0, 202.0, 204.0, 206.0, 208.0, 210.0, 212.0, 214.0, 216.0,
                    218.0, 220.0, 222.0, 224.0, 226.0, 228.0, 230.0, 232.0, 234.0, 236.0,
                    238.0, 240.0, 242.0, 244.0, 246.0, 248.0, 250.0, 252.0, 254.0, 256.0,
                    258.0, 260.0, 262.0, 264.0, 266.0, 268.0, 270.0, 272.0, 274.0, 276.0,

                    278.0, 280.0, 282.0, 284.0, 286.0, 288.0, 290.0, 292.0, 294.0, 296.0,
                    298.0, 300.0, 305.0, 310.0, 315.0, 320.0, 325.0, 330.0, 335.0, 340.0,
                    345.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 420.0, 440.0, 450.0,
                    460.0, 480.0, 500.0, 520.0, 540.0, 550.0, 560.0, 580.0, 600.0, 620.0,
                    640.0, 650.0, 660.0, 680.0, 700.0, 720.0, 740.0, 750.0, 760.0, 780.0,

                    800.0, 820.0, 840.0, 850.0, 860.0, 880.0, 900.0, 920.0, 940.0, 950.0,
                    960.0, 980.0, 1000.0, 1050.0, 1100.0, 1150.0, 1200.0, 1250.0, 1300.0, 1350.0,
                    1400.0, 1450.0, 1500.0, 1550.0, 1600.0, 1650.0, 1700.0, 1750.0, 1800.0, 1850.0,
                    1900.0, 1950.0, 2000.0, 2050.0, 2100.0, 2150.0, 2200.0, 2250.0, 2300.0, 2350.0,
                    2400.0, 2450.0, 2500.0, 2550.0, 2600.0, 2650.0, 2700.0, 2750.0, 2800.0, 2850.0,

                    2900.0, 2950.0, 3000.0, 3050.0, 3100.0, 3150.0, 3200.0, 3250.0, 3300.0, 3350.0,
                    3400.0, 3450.0, 3500.0, 3550.0, 3600.0, 3650.0, 3700.0, 3750.0, 3800.0, 3850.0,
                    3900.0, 3950.0, 4000.0, 4050.0, 4100.0, 4150.0, 4200.0, 4250.0, 4300.0, 4350.0,
                    4400.0, 4450.0, 4500.0, 4550.0, 4600.0, 4650.0, 4700.0, 4750.0, 4800.0, 4850.0, 4900.0, 4950.0, 5000.0]

        HwidthCPS = [0.00202, 0.00205, 0.00208, 0.00212, 0.00216, 0.00220, 0.00225, 0.00229, 0.00235, 0.00240,
                     0.00246, 0.00252, 0.00259, 0.00266, 0.00273, 0.00282, 0.00292, 0.00303, 0.00316, 0.00330,
                     0.00347, 0.00367, 0.00390, 0.00403, 0.00417, 0.00449, 0.00487, 0.00532, 0.00584, 0.00646,
                     0.00721, 0.00812, 0.00924, 0.0106, 0.0123, 0.0144, 0.0173, 0.0214, 0.0268, 0.0342,
                     0.0493, 0.0828, 0.141, 0.211, 0.276, 0.330, 0.379, 0.427, 0.475, 0.521,

                     0.570, 0.629, 0.702, 0.786, 0.870, 0.953, 1.03, 1.12, 1.19, 1.27,
                     1.35, 1.42, 1.5, 1.57, 1.65, 1.73, 1.81, 1.89, 1.97, 2.05,
                     2.14, 2.23, 2.32, 2.41, 2.5, 2.6, 2.7, 2.8, 2.9, 3.01,
                     3.12, 3.24, 3.36, 3.48, 3.61, 3.74, 3.87, 4.0, 4.13, 4.27,
                     4.42, 4.56, 4.71, 4.86, 5.01, 5.17, 5.33, 5.5, 5.66, 5.83,

                     6.01, 6.18, 6.36, 6.55, 6.73, 6.92, 7.12, 7.31, 7.51, 7.72,
                     7.93, 8.14, 8.68, 9.25, 9.83, 10.45, 11.08, 11.74, 12.43, 13.14,
                     13.88, 14.89, 17.08, 19.31, 21.63, 24.06, 26.6, 32.03, 37.94, 41.08,
                     44.35, 51.27, 58.7, 66.67, 75.16, 79.62, 84.2, 93.79, 103.93, 114.63,
                     125.88, 131.72, 137.69, 150.06, 162.97, 176.43, 190.43, 197.63, 204.96, 220.01,

                     235.57, 251.63, 268.17, 276.62, 285.18, 302.65, 320.55, 338.88, 357.62, 367.14,
                     376.75, 396.26, 416.12, 467.24, 520.26, 574.94, 631.07, 688.46, 746.93, 806.33,
                     866.54, 927.43, 988.91, 1050.9, 1113.3, 1176.1, 1239.2, 1302.5, 1366.1, 1429.9,
                     1493.9, 1558.0, 1622.2, 1686.6, 1751.0, 1815.5, 1880.2, 1944.8, 2009.6, 2074.4,
                     2139.2, 2204.1, 2269.1, 2334.0, 2399.1, 2464.1, 2529.2, 2594.4, 2659.6, 2724.8,

                     2790.1, 2855.4, 2920.7, 2986.1, 3051.7, 3117.4, 3183.1, 3248.9, 3314.7, 3380.5,
                     3446.4, 3512.3, 3578.3, 3644.4, 3710.5, 3776.6, 3831.6, 3883.5, 3935.3, 3987.2,
                     4039.0, 4090.8, 4142.6, 4194.3, 4246.1, 4297.9, 4349.7, 4401.5, 4453.3, 4505.0,
                     4547.8, 4599.5, 4651.2, 4702.8, 4754.5, 4806.2, 4857.9, 4909.6, 4961.2, 5012.9, 5064.6, 5116.3, 5168.0]

        #g_graph = ROOT.TGraph(len(Hmass), numpy.array(Hmass), numpy.array(Hwidth))
        #gCPS_graph = ROOT.TGraph(len(HmassCPS), numpy.array(HmassCPS), numpy.array(HwidthCPS))

        self.g = ROOT.TH1D("g","SM Higgs width",len(Hmass)-1,numpy.array(Hmass))
        self.gCPS = ROOT.TH1D("gCPS","SM Higgs width CPS",len(HmassCPS)-1,numpy.array(HmassCPS))
        for k,v in enumerate(Hwidth):
          self.g.SetBinContent(k+1,v)

        for k,v in enumerate(HwidthCPS):
          self.gCPS.SetBinContent(k+1,v)

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed                    
HMlnjjVars_Dev = lambda : HMlnjjVarsClass_Dev()

