import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os
from math import sqrt

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

Wmass=80.4

class HMlnjjVarsClass_Dev_jhchoi(Module):
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



        ##---Boosted Region---## Tag a AK8Jet with largest pT. 
        self._FinalFatJet_4v=ROOT.TLorentzVector()
        self._FinalFatJet_cfjidx=-1
        self._BJetBoosted_cjidx=[]
        self._VBFjjBoosted_dEta=-999.
        self._VBFjjBoosted_mjj=-999.
        self._VBFjjBoosted_cjdix1=-1
        self._VBFjjBoosted_cjdix2=-1

        ##---Resolved Region---##
        self._Whad_4v=ROOT.TLorentzVector()
        self._Whad_cjidx1=-1
        self._Whad_cjidx2=-1
        self._BJetResolved_cjidx=[]
        self._VBFjjResolved_dEta=-999.
        self._VBFjjResolved_mjj=-999.
        self._VBFjjResolved_cjidx1=-999.
        self._VBFjjResolved_cjidx2=-999.
        '''
        self.doSkim = doSkim
        self.METtype = METtype
        self.METcut_Boosted=40.
        self.METcut_Resolved=30.

        ##--How to select primary fatjet
        self.cfjidx_FatSel={}
        self.cfjidx_FatSel['MW']=-1 ## FatJet_mass ~ MW
        self.cfjidx_FatSel['PT']=-1 ## largest PT

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

        ##---Boosted Region kinematics
        for var in ['pt','eta','phi','mass']:
            self.out.branch("Wlep_"+var  , "F")
        self.out.branch(self.METtype+'_pz1', "F")
        self.out.branch(self.METtype+'_pz2', "F")
        

        self.out.branch("isBoosted","O")
        self.out.branch("WtaggerFatjet_cfjidx","I",lenVar='nWtaggerFatjet')
        for var in ['pt','eta','phi','mass','tau21']:
            self.out.branch("WtaggerFatjet_"+var,"F",lenVar='nWtaggerFatjet')
        self.out.branch("FinalFatJet_MW_cfjidx","I")
        self.out.branch("FinalFatJet_PT_cfjidx","I")
        

        for sel in self.cfjidx_FatSel:
            self.out.branch('lnJ_pt_'+sel,"F")
            self.out.branch('lnJ_mass_'+sel,"F")
            self.out.branch('minPtWOverMlnJ_'+sel,"F")
            self.out.branch('maxPtWOverMlnJ_'+sel,"F")
            self.out.branch('dR_l_F_'+sel,"F")
            self.out.branch('dR_Wlep_F_'+sel,"F")
            self.out.branch('dPhi_l_F_'+sel,"F")
            self.out.branch('dPhi_Wlep_F'+sel,"F")
        
        self.out.branch('BJetBoosted_cjidx','I',lenVar='nBJetBoosted')

        self.out.branch('isVBF_Boosted','O')
        self.out.branch('VBFjjBoosted_mjj','F')
        self.out.branch('VBFjjBoosted_dEta','F')
        self.out.branch('max_mjj_Boosted','F')

        ##---Resolved Region kinemaics
        self.out.branch('isResolved',"O")
        for var in ['pt','eta','phi','mass','Mt']:
            self.out.branch('Whad_'+var,'F')
        
        self.out.branch('Whad_cjidx1','I')
        self.out.branch('Whad_cjidx2','I')
        self.out.branch('BJetResolved_cjidx','I',lenVar='nBJetResolved_cjidx')
        self.out.branch('isVBF_Resolved','O')
        self.out.branch('VBFjjResolved_dEta','F')
        self.out.branch('VBFjjResolved_mjj','F')
        self.out.branch('VBFjjResolved_dEta','F')
        self.out.branch('max_mjj_Resolved','F')

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
	
        self._isBoosted=False
        self._cfatjet_MW_idx=-1 ##select fatjet whose mass is closest to MW
        self._cfatjet_PT_idx=-1 ## select fatjet whose pt is largest one
        self._cfatjet_idx_list=[]
        self._cfatjet_pt_list=[]
        self._cfatjet_eta_list=[]
        self._cfatjet_phi_list=[]
        self._cfatjet_mass_list=[]
        self._cfatjet_tau21_list=[]
        self._BJetBoosted_cjidx=[]
        self._isVBF_Boosted=False
        self._VBFjjBoosted_dEta=-999.
        self._VBFjjBoosted_mjj=-999.
        self._VBFjjBoosted_cjidx1=-1
        self._VBFjjBoosted_cjidx2=-1
        self._max_mjj_Boosted=-1.

        self.cfjidx_FatSel['MW']=-1 ## FatJet_mass ~ MW
        self.cfjidx_FatSel['PT']=-1## largest PT


        self._isResolved = False
        self._Whad_4v.SetPtEtaPhiM(0,0,0,0)
        self._Whad_cjidx1=-1
        self._Whad_cjidx2=-1
        self._BJetResolved_cjidx=[]
        self._isVBF_Resolved=False
        self._VBFjjResolved_dEta=-999.
        self._VBFjjResolved_mjj=-999.
        self._VBFjjResolved_cjidx1=-1
        self._VBFjjResolved_cjidx2=-1
        self._max_mjj_Resolved = -1. 
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
        
        

        #<<<<<<<Boosted>>>>>>>#
        
        ##---Step.1.Set Wlep
        #print "Start WlepMaker"
        self.WlepMaker()  #self._Wlep_4v , self._Wlep_METpz1, self._Wlep_METpz2
        #print "End WlepMaker"
        ##set           self._Wlep_4v
        
        
        
        ##---Step.2 Get Wtagger fatjet
        
        self.FindWtaggerFatJet() ##Fill self._cfatjet_idx_list
        ##-> Fill        cleanfatjet index     to       self._cfatjet_idx_list=[]
        ##-> set         self._cfatjet_MW_idx -> select FatJet whose Msoftdrop is closest to MW
        ##-> set         self._cfatjet_PT_idx -> select FatJet whose PT is the largest one
        
        
        ##---Step.3 Btag in Boosted region
        self.GetBJetsBoosted()
        ##->Set self._BJetBoosted_cjidx


        ##---Step.4 VBF Boosted
        self.VBF_Boosted()
        ##Set values of 
        ##->self._isVBF_Boosted
        ##->self._VBFjjBoosted_dEta
        ##->self._VBFjjBoosted_mjj
        ##->self._VBFjjBoosted_cjidx1
        ##->self._VBFjjBoosted_cjidx2
        #print "End of Boosted"
        ##---Now Objects for Boosted Region are defined
        if (len(self._cfatjet_idx_list) > 0) and ( self.MET_pt > self.METcut_Boosted): 
            self._isBoosted=True


        ##--Fill Branch for object ##
        ###-->_cfatjet_idx_list/_cfatjet_MW_idx//_cfatjet_PT_idx/
        ###-->_isBoosted, Wlep momentum, solution 1,2/ _VBFjjBoosted_dEta, _VBFjjBoosted_mjj,_BJetBoosted_cjidx,_max_mjj_Boosted
        ##---Check whether they are initialized at the starting of this analyze loop function
        
        ##---Wlep
        #print "fillBranchBoosted"
        self.out.fillBranch( 'Wlep_pt',self._Wlep_4v.Pt())
        self.out.fillBranch( 'Wlep_eta',self._Wlep_4v.Eta())
        self.out.fillBranch('Wlep_phi',self._Wlep_4v.Phi())
        self.out.fillBranch('Wlep_mass',self._Wlep_4v.M())
        self.out.fillBranch(self.METtype+'_pz1',self._Wlep_METpz1) ##MET_pz = pz1+-sqrt(pz2)
        self.out.fillBranch(self.METtype+'_pz2',self._Wlep_METpz2)
        

        self.out.fillBranch('isBoosted',self._isBoosted)
        self.out.fillBranch('WtaggerFatjet_cfjidx',self._cfatjet_idx_list)
        self.out.fillBranch('WtaggerFatjet_pt',self._cfatjet_pt_list)
        self.out.fillBranch('WtaggerFatjet_eta',self._cfatjet_eta_list)
        self.out.fillBranch('WtaggerFatjet_phi',self._cfatjet_phi_list)
        self.out.fillBranch('WtaggerFatjet_mass',self._cfatjet_mass_list)
        self.out.fillBranch('WtaggerFatjet_tau21',self._cfatjet_tau21_list)



        ## choice for final fatjet
        self.out.fillBranch('FinalFatJet_MW_cfjidx',self._cfatjet_MW_idx)
        self.out.fillBranch('FinalFatJet_PT_cfjidx',self._cfatjet_PT_idx)


        
        #---Two kinds of choice for FatJets 
        ##self._cfatjet_MW_idx
        ##self._cfatjet_PT_idx
        
        self.cfjidx_FatSel['MW']=self._cfatjet_MW_idx
        self.cfjidx_FatSel['PT']=self._cfatjet_PT_idx


        for sel in self.cfjidx_FatSel:
            cfatjet_idx=self.cfjidx_FatSel[sel]
            if cfatjet_idx >= 0:
                
                pt, eta, phi, mass = self.CleanFatJet_PtEtaPhiM(cfatjet_idx)
                self._FinalFatJet_4v.SetPtEtaPhiM(pt,eta,phi,mass) ##FatJet vector
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
        
        ##---Btagged Jet
        self.out.fillBranch('BJetBoosted_cjidx', self._BJetBoosted_cjidx)
        ##---VBF Boosted
        self.out.fillBranch('isVBF_Boosted', self._isVBF_Boosted)
        self.out.fillBranch('VBFjjBoosted_mjj', self._VBFjjBoosted_mjj)
        self.out.fillBranch('VBFjjBoosted_dEta', self._VBFjjBoosted_dEta)
        self.out.fillBranch('max_mjj_Boosted', self._max_mjj_Boosted)

        #<<<<< End of Boosted
        #print "fillBranchBoosted end"
        
        #<<<<<<<Resolved>>>>>>>#
        #print "if not boosted"
        

        ##Step.1 Get hadronic W using ak4 jet pair
        self.WhadMaker()
        ##set      self._Whad_4v
        ##set      self._Whad_cjidx1
        ##set      self._Whad_cjidx2
        ##set      self._isResolved
            
        ##Step.2 Get Btag
        self.GetBJetsResolved()
        ##set      self._BJetResolved_cjidx
        

        ##Step.3 VBF_Resolved
        self.VBF_Resolved()
        ##set      self._VBFjjResolved_mjj
        ##set      self._VBFjjResolved_dEta
        ##set      self._VBFjjResolved_cjidx1
        ##set      self._VBFjjResolved_cjidx2
        ##set      self._isVBF_Resolved
        ##set      self._VBFjjResolved_mjj
            
        #print "fill resolved"

        ##Fill branch
        self.out.fillBranch('isResolved',self._isResolved)

        ##Hadronic W
        self.out.fillBranch('Whad_pt', self._Whad_4v.Pt())
        self.out.fillBranch('Whad_eta', self._Whad_4v.Eta())
        self.out.fillBranch('Whad_phi', self._Whad_4v.Phi())
        self.out.fillBranch('Whad_mass', self._Whad_4v.M())
        self.out.fillBranch('Whad_Mt', self._Whad_4v.Mt())

        self.out.fillBranch('Whad_cjidx1', self._Whad_cjidx1)
        self.out.fillBranch('Whad_cjidx2', self._Whad_cjidx2)
        self.out.fillBranch('BJetResolved_cjidx', self._BJetResolved_cjidx)

        ###VBF
        self.out.fillBranch('isVBF_Resolved', self._isVBF_Resolved)
        self.out.fillBranch('VBFjjResolved_dEta', self._VBFjjResolved_dEta)
        self.out.fillBranch('VBFjjResolved_mjj', self._VBFjjResolved_mjj)
        self.out.fillBranch('VBFjjResolved_dEta', self._VBFjjResolved_dEta)
        self.out.fillBranch('max_mjj_Resolved', self._max_mjj_Resolved)

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


        #print "self._isBoosted",self._isBoosted
        #print "self._isResolved",self._isResolved
        
        ##<<<<End of Resolved

        if (not self._isBoosted) and (not self._isResolved) and self.doSkim: return False

        
        


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
        self._cfatjet_idx_list=[]
        self._cfatjet_pt_list=[]
        self._cfatjet_eta_list=[]
        self._cfatjet_phi_list=[]
        self._cfatjet_mass_list=[]
        self._cfatjet_MW_idx=-1
        self._cfatjet_PT_idx=-1
        
        min_dM=999999.
        max_pt=-999999.
        N=self.CleanFatJet_col._len
        for i_fj in range(0,N):
            pt,eta,phi,mass=self.CleanFatJet_PtEtaPhiM(i_fj)
            tau21=self.CleanFatJet_col[i_fj].tau21
            cfatjet_jetIdx=self.CleanFatJet_col[i_fj].jetIdx
            fatjetid = self.FatJet_col[cfatjet_jetIdx].jetId
            if mass < 40 : continue
            if mass > 250 : continue
            if tau21 > self.tau21WP : continue
            if abs(eta) > 2.4 : continue
            if pt < 200 : continue
            if fatjetid < self.min_fatjetid : continue
            self._cfatjet_idx_list.append(i_fj)
            self._cfatjet_pt_list.append(pt)
            self._cfatjet_eta_list.append(eta)
            self._cfatjet_phi_list.append(phi)
            self._cfatjet_mass_list.append(mass)
            self._cfatjet_tau21_list.append(tau21)
            ##PT ordering
            if pt > max_pt : self._cfatjet_PT_idx = i_fj
            if abs(Wmass - mass) < min_dM : self._cfatjet_MW_idx = i_fj
        
    def GetBJetsBoosted(self):
        ##->Set self._BJetBoosted_cjidx
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
            self._BJetBoosted_cjidx.append(cj_idx) ## fill index of CleanJet 
    def GetBJetsResolved(self):
        ##->Set self._BJetResolved_cjidx
        #self.CleanJet_col
        bWP=self.bWP
        N=self.CleanJet_col._len
        for i_cj in range(0,N):
            if i_cj == self._Whad_cjidx1 : continue
            if i_cj == self._Whad_cjidx2 : continue
            
            pt=self.CleanJet_col[i_cj].pt
            eta=self.CleanJet_col[i_cj].eta
            j_idx=self.CleanJet_col[i_cj].jetIdx ##Jet Object index
            bAlgo=self.Jet_col[j_idx].btagDeepB
            if bAlgo < bWP:continue
            if pt < 20 :continue
            if abs(eta) > 2.5:continue
            self._BJetResolved_cjidx.append(i_cj) ## fill index of CleanJet
            



    def VBF_Boosted(self):
        N=self.CleanJetNotFat_col._len
        if N < 2 :
            #print "NCleanJet < 2"
            self._isVBF_Boosted = False
            return
        
        #max_mjj=-9999.
        for i_cj in range(0,N):
            cjidx1 = self.CleanJetNotFat_col[i_cj].jetIdx ##index of CleanJet
            pt1,eta1,phi1,mass1 = self.CleanJet_PtEtaPhiM(cjidx1)
            if pt1 < 30 : continue
            if abs(eta1) > 4.7 : continue
            
            for j_cj in range(0,N):
                if j_cj <= i_cj : continue ##aviod doubly checked or the same one
                cjidx2 = self.CleanJetNotFat_col[j_cj].jetIdx ##index of CleanJet
                pt2,eta2,phi2,mass2 = self.CleanJet_PtEtaPhiM(cjidx2)
                if pt2 < 30: continue
                if abs(eta2) > 4.7 : continue

                ##Set momentum##
                #print "Boosted forward pair, "
                this_dEta=abs(eta1-eta2)
                this_mjj = self.InvMassCalc(pt1,eta1,phi1,mass1,pt2,eta2,phi2,mass2)
                #print "this_dEta=",this_dEta
                #print "this_mjj=",this_mjj
                if (this_dEta > 3.5) and (this_mjj > self._VBFjjBoosted_mjj) : 
                    self._VBFjjBoosted_dEta = this_dEta
                    self._VBFjjBoosted_mjj = this_mjj
                    self._VBFjjBoosted_cjidx1 = cjidx1
                    self._VBFjjBoosted_cjidx2 = cjidx2
                if this_mjj > self._max_mjj_Boosted:
                    self._max_mjj_Boosted = this_mjj

        ##--End of jet pair loop
        if self._VBFjjBoosted_mjj > 500. : self._isVBF_Boosted = True

    def VBF_Resolved(self):
        N = self.CleanJetNotFat_col._len
        if N < 2 : ## could it be 4 ?
            self._isVBF_Resolved = False
            return

        #max_mjj=-9999.
        for i_cj in range(0,N):
            
            pt1,eta1,phi1,mass1 = self.CleanJet_PtEtaPhiM(i_cj)
            if pt1 < 30 : continue
            if abs(eta1) > 4.7 : continue

            for j_cj in range(0,N):
                if j_cj <= i_cj : continue ##doubly checked or the same one
                
                pt2,eta2,phi2,mass2 = self.CleanJet_PtEtaPhiM(j_cj)
                if pt2 < 30: continue
                if abs(eta2) > 4.7 : continue

                ##Set momentum##

                this_dEta=abs(eta1-eta2)
                this_mjj = self.InvMassCalc(pt1,eta1,phi1,mass1,pt2,eta2,phi2,mass2)
                if (this_dEta > 3.5) and (this_mjj > self._VBFjjResolved_mjj) :
                    self._VBFjjResolved_dEta = this_dEta
                    self._VBFjjResolved_mjj = this_mjj
                    self._VBFjjResolved_cjidx1 = i_cj
                    self._VBFjjResolved_cjidx2 = j_cj
                if this_mjj > self._max_mjj_Resolved:
                    self._max_mjj_Resolved = this_mjj

        ##--End of jet pair loop
        if self._VBFjjResolved_mjj > 500. : self._isVBF_Resolved = True


    def WhadMaker(self):
        N=self.CleanJet_col._len
        dM=99999.
        Whad_mass=-9999.
        for i_cj in range(0,N):
            pt1,eta1,phi1,mass1 = self.CleanJet_PtEtaPhiM(i_cj)
            if pt1 < 30. : continue
            if abs(eta1) > 2.4 : continue 
            for j_cj in range(0,N):
                if j_cj <= i_cj : continue
                pt2,eta2,phi2,mass2 = self.CleanJet_PtEtaPhiM(j_cj)
                if pt2 < 30. : continue
                if abs(eta2) > 2.4 : continue
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
        if Whad_mass > 40 and Whad_mass < 250 : self._isResolved = True
        if self._Whad_cjidx1 < 0 : self._isResolved = False #for safty
        if self._Whad_cjidx2 < 0 : self._isResolved = False #for safty




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
HMlnjjVars_Dev_jhchoi = lambda : HMlnjjVarsClass_Dev_jhchoi()

