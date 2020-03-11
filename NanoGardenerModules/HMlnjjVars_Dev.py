import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os
from math import sqrt

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

Wmass=80.4

class HMlnjjVarsClass_Dev(Module):
    def __init__(self,year,METtype='PuppiMET,',doSkim=False,doHardSkim=False):

        self._Wlep_4v=ROOT.TLorentzVector()
        self._lepton_4v=ROOT.TLorentzVector()
        self._FinalFatJet_4v=ROOT.TLorentzVector()##declare tlorenzvector objects when start of 
        self._Whad_4v = ROOT.TLorentzVector()
        '''
        ##---Leptonic W---##
        self._Wlep_4v=ROOT.TLorentzVector()
        self._Wlep_METpz1=-1.
        self._Wlep_METpz2=-1. ##METpz solution ==pz1+-sqrt(pz2)



        ##---Boost Region---## Tag a AK8Jet with largest pT. 
        self._FinalFatJet_4v=ROOT.TLorentzVector()
        self._FinalFatJet_cfjidx=-1
        self._BJetBoost_cjidx=[]
        self._VBFjjBoost_dEta=-999.
        self._VBFjjBoost_mjj=-999.
        self._VBFjjBoost_cjdix1=-1
        self._VBFjjBoost_cjdix2=-1

        ##---Resol Region---##
        self._Whad_4v=ROOT.TLorentzVector()
        self._Whad_cjidx1=-1
        self._Whad_cjidx2=-1
        self._BJetResol_cjidx=[]
        self._VBFjjResol_dEta=-999.
        self._VBFjjResol_mjj=-999.
        self._VBFjjResol_cjidx1=-999.
        self._VBFjjResol_cjidx2=-999.
        '''
        self.doSkim = doSkim
        self.METtype = METtype

        ##--How to select primary fatjet
        self.cfjidx_FatSel={}
        self.cfjidx_FatSel['mindM']=-1 ## FatJet_mass ~ mindM
        self.cfjidx_FatSel['mxPT']=-1 ## largest mxPT
       
        #####################################
	# Cuts
        #####################################
	self.Wmass_CRlow  = 40
	self.Wmass_CRhigh = 250
	self.Wmass_SRlow  = 65
	self.Wmass_SRhigh = 105 

        self.METcut_Boost=40.
        self.METcut_Resol=30.

	self.cut_fjet_eta = 2.4
	self.cut_fjet_pt  = 200
	self.cut_jet_eta  = 2.4
	self.cut_jet_pt   = 30
	self.cut_bjet_pt   = 20
	self.cut_bjet_eta  = 2.5
	self.cut_VBFjet_pt = 30
	self.cut_VBFjet_eta= 4.7 
	self.cut_VBF_mjj= 500
	self.cut_minPtWOverMlnJ  = 0.4
	self.cut_minPtWOverMlnjj = 0.35

	self.cut_VBF_dEta = 3.5
	self.cut_VBF_mjj  = 500
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




    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree

        ##---Boost Region kinematics
        for var in ['pt','eta','phi','mass']:
            self.out.branch("Wlep_"+var  , "F")
        self.out.branch(self.METtype+'_pz1', "F")
        self.out.branch(self.METtype+'_pz2', "F")
        

        self.out.branch("isBoost","O")
        self.out.branch("WtagFatjet_cfjidx","I",lenVar='nWtagFatjet')
        for var in ['pt','eta','phi','mass','tau21']:
            self.out.branch("WtagFatjet_"+var,"F",lenVar='nWtagFatjet')
        self.out.branch("FinalFatJet_mindM_cfjidx","I")
        self.out.branch("FinalFatJet_mxPT_cfjidx","I")
        

        for sel in self.cfjidx_FatSel:
            self.out.branch('lnJ_pt_'+sel,"F")
            self.out.branch('lnJ_mass_'+sel,"F")
            self.out.branch('minPtWOverMlnJ_'+sel,"F")
            self.out.branch('maxPtWOverMlnJ_'+sel,"F")
            self.out.branch('dR_l_F_'+sel,"F")
            self.out.branch('dR_Wlep_F_'+sel,"F")
            self.out.branch('dPhi_l_F_'+sel,"F")
            self.out.branch('dPhi_Wlep_F'+sel,"F")
        
        self.out.branch('BJetBoost_cjidx','I',lenVar='nBJetBoost')

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
        """process event, return True (go to next module) or False (fail, go to next event)"""
	# initialize
        self._lepton_4v.SetPtEtaPhiM(0,0,0,0)
	self._Wlep_4v.SetPtEtaPhiM(0,0,0,0)
	self._Wlep_METpz1=-1
	self._Wlep_METpz2=-1
	
        self._isBoost=False
        self._isBoostSR=False
        self.Wfatjet_mindM_cfjidx=-1 ##select fatjet whose mass is closest to MW
        self.Wfatjet_mxPT_cfjidx=-1 ## select fatjet whose pt is largest one
        self.Wfatjet_idx_list=[]
        self.Wfatjet_pt_list=[]
        self.Wfatjet_eta_list=[]
        self.Wfatjet_phi_list=[]
        self.Wfatjet_mass_list=[]
        self.Wfatjet_tau21_list=[]
        self._BJetBoost_cjidx=[]
        self._isVBF_Boost=False
        self._VBFjjBoost_dEta=-999.
        self._VBFjjBoost_mjj=-999.
        self._VBFjjBoost_cjidx1=-1
        self._VBFjjBoost_cjidx2=-1
        self._max_mjj_Boost=-1.

        self.cfjidx_FatSel['mindM']=-1 ## FatJet_mass ~ mindM
        self.cfjidx_FatSel['mxPT']=-1## largest mxPT

        self._isResol = False
        self._isResolSR = False
        self._Whad_4v.SetPtEtaPhiM(0,0,0,0)
        self._Whad_cjidx1=-1
        self._Whad_cjidx2=-1
        self._BJetResol_cjidx=[]
        self._isVBF_Resol=False
        self._VBFjjResol_dEta=-999.
        self._VBFjjResol_mjj=-999.
        self._VBFjjResol_cjidx1=-1
        self._VBFjjResol_cjidx2=-1
        self._max_mjj_Resol = -1. 
        ##--End of initialization

        
        ##--Get object collections--##
        self.Lepton = Object(event, 'Lepton', index=0)
        self.CleanFatJet_col = Collection(event, 'CleanFatJet')
        self.FatJet_col = Collection(event, 'FatJet')
        self.CleanJet_col = Collection(event, 'CleanJet')
        self.CleanJetNotFat_col = Collection(event, 'CleanJetNotFat')
        self.Jet_col = Collection(event,"Jet")

        ##---MET
        self.MET = Object(event, self.METtype)
        self.MET_pt = self.MET.pt
        self.MET_phi = self.MET.phi
        #self.MET=ROOT.TLorentzVector()
        #self.MET.SetPtEtaPhiM(self.MET_pt, 0., self.MET_phi, 0.)
        
        

        #<<<<<<<Boost>>>>>>>#
        
        ##---Step.1.Set Wlep
        #print "Start WlepMaker"
        self.WlepMaker()  #self._Wlep_4v , self._Wlep_METpz1, self._Wlep_METpz2
        #print "End WlepMaker"
        ##set           self._Wlep_4v
        
        
        
        ##---Step.2 Get Wtagger fatjet
        
        self.FindWtaggerFatJet() ##Fill self.Wfatjet_idx_list
        ##-> Fill        cleanfatjet index     to       self.Wfatjet_idx_list=[]
        ##-> set         self.Wfatjet_mindM_idx -> select FatJet whose Msoftdrop is closest to MW
        ##-> set         self.Wfatjet_mxPT_idx -> select FatJet whose mxPT is the largest one

        #---Two kinds of choice for FatJets 
        ##self.Wfatjet_mindM_idx
        ##self.Wfatjet_mxPT_idx

        ################# 
        # Cook for lnJ ##
        ################# 
        self.cfjidx_FatSel['mindM']=self.Wfatjet_mindM_cfjidx
        self.cfjidx_FatSel['mxPT']=self.Wfatjet_mxPT_cfjidx

        for sel in self.cfjidx_FatSel:# loop twice for mindM and mxPT
            cfatjet_idx=self.cfjidx_FatSel[sel]
            if cfatjet_idx >= 0:
                
                WfatPt, WfatEta, WfatPhi, WfatMass = self.CleanFatJet_PtEtaPhiM(cfatjet_idx)
                self._FinalFatJet_4v.SetPtEtaPhiM(WfatPt,WfatEta,WfatPhi,WfatMass) ##FatJet vector
                H_4v=self._Wlep_4v + self._FinalFatJet_4v ## sum Wlep + Whad
                lnJ_pt=H_4v.Pt()
                lnJ_mass=H_4v.M()
                ##--additional cut
                minPtWOverMlnJ = min(self._Wlep_4v.Pt(), self._FinalFatJet_4v.Pt())/lnJ_mass
                maxPtWOverMlnJ = max(self._Wlep_4v.Pt(), self._FinalFatJet_4v.Pt())/lnJ_mass
                ##DeltaR, DeltaPhi between l - Fat OR Wlep - Fat
                
                dR_l_F=self._FinalFatJet_4v.DeltaR(self._lepton_4v)
                dR_Wlep_F=self._FinalFatJet_4v.DeltaR(self._Wlep_4v)
                
                dPhi_l_F=self._FinalFatJet_4v.DeltaPhi(self._lepton_4v)
                dPhi_Wlep_F=self._FinalFatJet_4v.DeltaPhi(self._Wlep_4v)
		########################
		#### Event Catagory ####
		########################
		if sel == "mindM":
		  #print "mindM case"
	          cut_Boost_Base  = [ \
		      self.MET_pt    > self.METcut_Boost and \
		      minPtWOverMlnJ > self.cut_minPtWOverMlnJ]
		  cut_Boost_CR = [ \
		      WfatMass < self.Wmass_CRhigh and \
		      WfatMass > self.Wmass_CRlow]
		  cut_Boost_SR = [ \
		      WfatMass < self.Wmass_SRhigh and \
		      WfatMass > self.Wmass_SRlow]
		  if all(cut_Boost_Base) and all(cut_Boost_CR):
                    self._isBoost = True
		  if all(cut_Boost_Base) and all(cut_Boost_SR):
                    self._isBoostSR = True
            else:
                lnJ_pt = -999.
                lnJ_mass= 999.
                minPtWOverMlnJ=-999.
                maxPtWOverMlnJ=-999.
                dR_l_F = -999.
                dR_Wlep_F = -999.
                dR_l_F = -999.
                dR_Wlep_F = -999.

            self.out.fillBranch('lnJ_pt_'+sel, lnJ_pt)
            self.out.fillBranch('lnJ_mass_'+sel, lnJ_mass)
            self.out.fillBranch('minPtWOverMlnJ_'+sel, minPtWOverMlnJ)##additional cut
            self.out.fillBranch('maxPtWOverMlnJ_'+sel, maxPtWOverMlnJ)
            self.out.fillBranch('dR_l_F_'+sel, dR_l_F)
            self.out.fillBranch('dR_Wlep_F_'+sel, dR_Wlep_F)
            self.out.fillBranch('dPhi_l_F_'+sel, dR_l_F)
            self.out.fillBranch('dPhi_Wlep_F'+sel, dR_Wlep_F)
            
        ##End of fatjet selection choice
       

        ##---Step.3 Btag in Boost region
        self.GetBJetsBoost()
        ##->Set self._BJetBoost_cjidx


        ##---Step.4 VBF Boost
        self.VBF_Boost()
        ##Set values of 
        ##->self._isVBF_Boost
        ##->self._VBFjjBoost_dEta
        ##->self._VBFjjBoost_mjj
        ##->self._VBFjjBoost_cjidx1
        ##->self._VBFjjBoost_cjidx2
        #print "End of Boost"


        ##--Fill Branch for object ##
        ###-->Wfatjet_idx_list/Wfatjet_mindM_cfjidx//Wfatjet_mxPT_cfjidx/
        ###-->_isBoost, Wlep momentum, solution 1,2/ _VBFjjBoost_dEta, _VBFjjBoost_mjj,_BJetBoost_cjidx,_max_mjj_Boost
        ##---Check whether they are initialized at the starting of this analyze loop function
        
        ##---Wlep
        #print "fillBranchBoost"
        self.out.fillBranch('Wlep_pt',self._Wlep_4v.Pt())
        self.out.fillBranch('Wlep_eta',self._Wlep_4v.Eta())
        self.out.fillBranch('Wlep_phi',self._Wlep_4v.Phi())
        self.out.fillBranch('Wlep_mass',self._Wlep_4v.M())
        #self.out.fillBranch(self.METtype+'_pz1',self._Wlep_METpz1) ##MET_pz = pz1+-sqrt(pz2)
        #self.out.fillBranch(self.METtype+'_pz2',self._Wlep_METpz2)
        

        self.out.fillBranch('isBoost'  ,self._isBoost)
        self.out.fillBranch('isBoostSR',self._isBoostSR)
        self.out.fillBranch('WtagFatjet_cfjidx',self.Wfatjet_idx_list)
        self.out.fillBranch('WtagFatjet_pt',self.Wfatjet_pt_list)
        self.out.fillBranch('WtagFatjet_eta',self.Wfatjet_eta_list)
        self.out.fillBranch('WtagFatjet_phi',self.Wfatjet_phi_list)
        self.out.fillBranch('WtagFatjet_mass',self.Wfatjet_mass_list)
        self.out.fillBranch('WtagFatjet_tau21',self.Wfatjet_tau21_list)



        ## choice for final fatjet
        self.out.fillBranch('FinalFatJet_mindM_cfjidx',self.Wfatjet_mindM_cfjidx)
        self.out.fillBranch('FinalFatJet_mxPT_cfjidx',self.Wfatjet_mxPT_cfjidx)


        
        
        ##---Btagged Jet
        self.out.fillBranch('BJetBoost_cjidx', self._BJetBoost_cjidx)
        ##---VBF Boost
        self.out.fillBranch('isVBF_Boost', self._isVBF_Boost)
        self.out.fillBranch('VBFjjBoost_mjj', self._VBFjjBoost_mjj)
        self.out.fillBranch('VBFjjBoost_dEta', self._VBFjjBoost_dEta)
        self.out.fillBranch('max_mjj_Boost', self._max_mjj_Boost)

        #<<<<< End of Boost
        #print "fillBranchBoost end"
        
        #<<<<<<<Resol>>>>>>>#
        #print "if not boosted"
        

        ##Step.1 Get hadronic W using ak4 jet pair, choosing min(Wmass -Mjj)
        self.WhadMaker()
        ##set      self._Whad_4v
        ##set      self._Whad_cjidx1
        ##set      self._Whad_cjidx2
        ##set      self._isResol
            
        ##Step.2 Get Btag
        self.GetBJetsResol()
        ##set      self._BJetResol_cjidx
        

        ##Step.3 VBF_Resol
        self.VBF_Resol()
        ##set      self._VBFjjResol_mjj
        ##set      self._VBFjjResol_dEta
        ##set      self._VBFjjResol_cjidx1
        ##set      self._VBFjjResol_cjidx2
        ##set      self._isVBF_Resol
        ##set      self._VBFjjResol_mjj
            
        #print "fill resolved"

        ##Fill branch
        self.out.fillBranch('isResol',self._isResol)
        self.out.fillBranch('isResolSR',self._isResolSR)

        ##Hadronic W
        self.out.fillBranch('Whad_pt', self._Whad_4v.Pt())
        self.out.fillBranch('Whad_eta', self._Whad_4v.Eta())
        self.out.fillBranch('Whad_phi', self._Whad_4v.Phi())
        self.out.fillBranch('Whad_mass', self._Whad_4v.M())
        self.out.fillBranch('Whad_Mt', self._Whad_4v.Mt())

        self.out.fillBranch('Whad_cjidx1', self._Whad_cjidx1)
        self.out.fillBranch('Whad_cjidx2', self._Whad_cjidx2)
        self.out.fillBranch('BJetResol_cjidx', self._BJetResol_cjidx)

        ###VBF
        self.out.fillBranch('isVBF_Resol', self._isVBF_Resol)
        self.out.fillBranch('VBFjjResol_dEta', self._VBFjjResol_dEta)
        self.out.fillBranch('VBFjjResol_mjj', self._VBFjjResol_mjj)
        self.out.fillBranch('VBFjjResol_dEta', self._VBFjjResol_dEta)
        self.out.fillBranch('max_mjj_Resol', self._max_mjj_Resol)

        ##Hlnjj
        H_4v=self._Wlep_4v + self._Whad_4v
        lnjj_pt = H_4v.Pt()
        lnjj_mass = H_4v.M()
        lnjj_Mt=H_4v.Mt()
        
        minPtWOverMlnjj = min(self._Wlep_4v.Pt(), self._Whad_4v.Pt())/lnjj_mass
        maxPtWOverMlnjj = max(self._Wlep_4v.Pt(), self._Whad_4v.Pt())/lnjj_mass
        ##DeltaR, DeltaPhi between l - Whad OR Wlep - Whad
        dR_l_Whad=self._Whad_4v.DeltaR(self._lepton_4v)
        dR_Wlep_Whad=self._Whad_4v.DeltaR(self._Wlep_4v)
        dPhi_l_Whad=self._Whad_4v.DeltaPhi(self._lepton_4v)
        dPhi_Wlep_Whad=self._Whad_4v.DeltaPhi(self._Wlep_4v)
        self.out.fillBranch('lnjj_pt', lnjj_pt)
        self.out.fillBranch('lnjj_mass', lnjj_mass)
        self.out.fillBranch('lnjj_Mt', lnjj_Mt)
        self.out.fillBranch('minPtWOverMlnjj',minPtWOverMlnjj)
        self.out.fillBranch('maxPtWOverMlnjj',maxPtWOverMlnjj)
        self.out.fillBranch('dR_l_Whad',dR_l_Whad)
        self.out.fillBranch('dR_Wlep_Whad',dR_Wlep_Whad)
        self.out.fillBranch('dPhi_l_Whad',dPhi_l_Whad)
        self.out.fillBranch('dPhi_Wlep_Whad',dPhi_Wlep_Whad)




        #print "End of fllbranch"


        #print "self._isBoost",self._isBoost
        #print "self._isResol",self._isResol
        
        ##<<<<End of Resol

        if (not self._isBoost) and (not self._isResol) and self.doSkim: return False

        
        


        return True



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
        lepton_pt=self.Lepton.pt
        lepton_eta=self.Lepton.eta
        lepton_phi=self.Lepton.phi
        lepton_pz = lepton_pt*math.sinh(lepton_eta)
        lepton_E = lepton_pt*math.cosh(lepton_eta)
        self._lepton_4v=ROOT.TLorentzVector()
        self._lepton_4v.SetPtEtaPhiM(lepton_pt,lepton_eta,lepton_phi,0)
        met_pt=self.MET_pt
        met_phi=self.MET_phi
        #print 'Wmass=',type(Wmass)
        #print 'lepton_pt=',type(lepton_pt)
        #print 'lepton_phi=',type(lepton_pt)
        #print 'met_pt=',type(met_pt)
        #print 'met_phi=',type(met_phi)
        mu = (Wmass*Wmass)/2 + lepton_pt*met_pt*math.cos(met_phi-lepton_phi)
        met_pz_1 = mu*lepton_pz/pow(lepton_pt,2)
        met_pz_2 = (  mu*lepton_pz/(lepton_pt**2)  )**2 - ( (lepton_E*met_pt)**2 - mu**2 )/(lepton_pt**2)

        #met_pz solution = met_pz_1 +-sqrt(met_pz_2)

        ##complex case
        if met_pz_2 < 0:
            met_pz = met_pz_1
        else:
            sol1 = met_pz_1+math.sqrt(met_pz_2)
            sol2 = met_pz_1-math.sqrt(met_pz_2)
            if abs(sol1) < abs(sol2):
                met_pz = sol1
            else:
                met_pz = sol2

        wlep_px = lepton_pt*math.cos(lepton_phi) + met_pt*math.cos(met_phi)
        wlep_py = lepton_pt*math.sin(lepton_phi) + met_pt*math.sin(met_phi)
        wlep_pz = lepton_pz + met_pz
        wlep_E  = lepton_E  + math.sqrt(met_pz**2 + met_pt**2)
        self._Wlep_4v.SetPxPyPzE(wlep_px,wlep_py,wlep_pz,wlep_E)
        


    def FindWtaggerFatJet(self):
        ##self.CleanFatJet
        self.Wfatjet_idx_list=[]
        self.Wfatjet_pt_list=[]
        self.Wfatjet_eta_list=[]
        self.Wfatjet_phi_list=[]
        self.Wfatjet_mass_list=[]
        self.Wfatjet_mindM_cfjidx=-1
        self.Wfatjet_mxPT_cfjidx=-1
        
        min_dM=999999.
        max_pt=-999999.
        N=self.CleanFatJet_col._len
        for i_fj in range(0,N):
            pt,eta,phi,mass=self.CleanFatJet_PtEtaPhiM(i_fj)
            tau21=self.CleanFatJet_col[i_fj].tau21
            cfatjet_jetIdx=self.CleanFatJet_col[i_fj].jetIdx
            fatjetid = self.FatJet_col[cfatjet_jetIdx].jetId
            if mass < self.Wmass_CRlow : continue
            if mass > self.Wmass_CRhigh : continue
            if tau21 > self.tau21WP : continue
            if abs(eta) > self.cut_fjet_eta : continue
            if pt < self.cut_fjet_pt : continue
            if fatjetid < self.min_fatjetid : continue
            self.Wfatjet_idx_list.append(i_fj)
            self.Wfatjet_pt_list.append(pt)
            self.Wfatjet_eta_list.append(eta)
            self.Wfatjet_phi_list.append(phi)
            self.Wfatjet_mass_list.append(mass)
            self.Wfatjet_tau21_list.append(tau21)
            ##PT ordering
            if pt > max_pt :
	      max_pt = pt
	      self.Wfatjet_mxPT_cfjdx = i_fj
            tmp_dM = abs(Wmass - mass)
            if tmp_dM < min_dM :
	      min_dM = tmp_dM
	      self.Wfatjet_mindM_cfjidx = i_fj
        
    def GetBJetsBoost(self):
        ##->Set self._BJetBoost_cjidx
        #self.CleanJetNotFat_col
        bWP=self.bWP
        N=self.CleanJetNotFat_col._len
        for i_cj in range(0,N): ##-- i_cj = idx of self.CleanJetNotFat_col
            cj_idx=self.CleanJetNotFat_col[i_cj].jetIdx
            pt=self.CleanJet_col[cj_idx].pt
            eta=self.CleanJet_col[cj_idx].eta
            j_idx=self.CleanJet_col[cj_idx].jetIdx
            bAlgo=self.Jet_col[j_idx].btagDeepB
            if bAlgo < bWP:continue
            if pt < 20 :continue
            if abs(eta) > 2.5:continue
            self._BJetBoost_cjidx.append(cj_idx) ## fill index of CleanJet 
    def GetBJetsResol(self):
        ##->Set self._BJetResol_cjidx
        #self.CleanJet_col
        bWP=self.bWP
        N=self.CleanJet_col._len
        for i_cj in range(0,N):
            if i_cj == self._Whad_cjidx1 : continue
            if i_cj == self._Whad_cjidx2 : continue
            
            pt   = self.CleanJet_col[i_cj].pt
            eta  = self.CleanJet_col[i_cj].eta
            j_idx= self.CleanJet_col[i_cj].jetIdx ##Jet Object index
            bAlgo= self.Jet_col[j_idx].btagDeepB
            if bAlgo < bWP:continue
            if pt < self.cut_bjet_pt  :continue
            if abs(eta) > self.cut_bjet_eta:continue
            self._BJetResol_cjidx.append(i_cj) ## fill index of CleanJet
            



    def VBF_Boost(self):
        N=self.CleanJetNotFat_col._len
        if N < 2 :
            #print "NCleanJet < 2"
            self._isVBF_Boost = False
            return
        
        #max_mjj=-9999.
        for i_cj in range(0,N):
            cjidx1 = self.CleanJetNotFat_col[i_cj].jetIdx ##index of CleanJet
            pt1,eta1,phi1,mass1 = self.CleanJet_PtEtaPhiM(cjidx1)
            if pt1 < self.cut_VBFjet_pt : continue
            if abs(eta1) > self.cut_VBFjet_eta : continue
            
            for j_cj in range(0,N):
                if j_cj <= i_cj : continue ##aviod doubly checked or the same one
                cjidx2 = self.CleanJetNotFat_col[j_cj].jetIdx ##index of CleanJet
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
                if (this_dEta > 3.5) and (this_mjj > self._VBFjjBoost_mjj) : 
                    self._VBFjjBoost_dEta = this_dEta
                    self._VBFjjBoost_mjj = this_mjj
                    self._VBFjjBoost_cjidx1 = cjidx1
                    self._VBFjjBoost_cjidx2 = cjidx2
		# the biggest mjj for VBF or not
                if this_mjj > self._max_mjj_Boost:
                    self._max_mjj_Boost = this_mjj

        ##--End of jet pair loop
        if self._VBFjjBoost_mjj > self.cut_minPtWOverMlnjj : self._isVBF_Boost = True

    def VBF_Resol(self):
        if not self._isResol:
            self._isVBF_Resol = False
	    return
        #N = self.CleanJetNotFat_col._len bug?
        N=self.CleanJet_col._len
        #if N < 2 : ## could it be 4 ? bug?
        if N < 4 : 
            self._isVBF_Resol = False
            return

        #max_mjj=-9999.
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
                if (this_dEta > 3.5) and (this_mjj > self._VBFjjResol_mjj) :
                    self._VBFjjResol_dEta = this_dEta
                    self._VBFjjResol_mjj = this_mjj
                    self._VBFjjResol_cjidx1 = i_cj
                    self._VBFjjResol_cjidx2 = j_cj
                if this_mjj > self._max_mjj_Resol:
                    self._max_mjj_Resol = this_mjj

        ##--End of jet pair loop
        if self._VBFjjResol_mjj > self.cut_VBF_mjj : self._isVBF_Resol = True


    def WhadMaker(self):
        N=self.CleanJet_col._len
        dM=99999.
        Whad_mass=-9999.
        for i_cj in range(0,N):
            pt1,eta1,phi1,mass1 = self.CleanJet_PtEtaPhiM(i_cj)
            if pt1 < self.cut_jet_pt : continue
            if abs(eta1) > self.cut_jet_eta : continue 
            for j_cj in range(0,N):
                if j_cj <= i_cj : continue
                pt2,eta2,phi2,mass2 = self.CleanJet_PtEtaPhiM(j_cj)
                if pt2 < self.cut_jet_pt  : continue
                if abs(eta2) > self.cut_jet_eta : continue
                v1=ROOT.TLorentzVector()
                v2=ROOT.TLorentzVector()
                v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
                v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2)
                
                this_M=(v1+v2).M()
                this_dM=abs(Wmass-this_M)
                if this_dM < dM:
                    dM = this_dM
                    self._Whad_cjidx1 = i_cj
                    self._Whad_cjidx2 = j_cj
                    self._Whad_4v = v1+v2
        Whad_mass=self._Whad_4v.M()
        if Whad_mass > self.Wmass_CRlow and Whad_mass < self.Wmass_CRhigh : self._isResol = True
        if Whad_mass > self.Wmass_SRlow and Whad_mass < self.Wmass_SRhigh : self._isResolSR = True
        if self._Whad_cjidx1 < 0 :
	  self._isResol   = False #for safty
	  self._isResolSR = False #for safty
        if self._Whad_cjidx2 < 0 :
	  self._isResol   = False #for safty
	  self._isResolSR = False #for safty




    def CleanJet_PtEtaPhiM(self,cjidx):
        pt=self.CleanJet_col[cjidx].pt
        eta=self.CleanJet_col[cjidx].eta
        phi=self.CleanJet_col[cjidx].phi
        jidx=self.CleanJet_col[cjidx].jetIdx
        mass=self.Jet_col[jidx].mass
        return pt,eta,phi,mass

    def CleanFatJet_PtEtaPhiM(self,cfjidx):
        pt=self.CleanFatJet_col[cfjidx].pt
        eta=self.CleanFatJet_col[cfjidx].eta
        phi=self.CleanFatJet_col[cfjidx].phi
        mass=self.CleanFatJet_col[cfjidx].mass
        
        return pt,eta,phi,mass

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed                    
HMlnjjVars_Dev = lambda : HMlnjjVarsClass_Dev()

