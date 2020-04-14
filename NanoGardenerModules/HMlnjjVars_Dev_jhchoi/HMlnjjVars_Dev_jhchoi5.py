##add Whad algorithm
####Jet rawfactor
import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os
from math import sqrt
import sys

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import matchObjectCollection, matchObjectCollectionMultiple
from LatinoAnalysis.NanoGardener.framework.BranchMapping import mappedOutputTree, mappedEvent


##--We can move this configurations to a cfg file after some tests--#
Wmass=80.4


MYALGO={
'dM':'',
'dMchi2rawF':'',
'dMchi2rawFqgl':'',
'dMchi2Resolution':'',
'dMchi2Resolutionqgl':'',
'HighPTjj':'', ##require jj pair making highest pt(jj)
'LowPTjj':'', ##require jj pair making lowest pt(jj)
}

class HMlnjjVarsClass_Dev_jhchoi(Module):
    def __init__(self,year,METtype='PuppiMET,',doSkim=False,doHardSkim=False):

        self._Wlep_4v=ROOT.TLorentzVector()
        self._lepton_4v=ROOT.TLorentzVector()
        self._FinalFatJet_4v=ROOT.TLorentzVector()##declare tlorenzvector objects when start of 
        
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
        

        ##--Init JetResolution--##
        self.init_JetResolution(year)

    def init_JetResolution(self,Year):
        print "--Initialize JetResolution reader---"
        cmssw_base = os.getenv('CMSSW_BASE')
        if int(Year) == 2016:
          jerInputFileName = "Summer16_25nsV1b_DATA_PtResolution_AK4PFchs.txt"
          jerInputFileSource="https://raw.githubusercontent.com/cms-jet/JRDatabase/master/textFiles/Summer16_25nsV1b_DATA/Summer16_25nsV1b_DATA_PtResolution_AK4PFchs.txt"
        elif int(Year) == 2017:
          jerInputFileName = "Fall17_V3b_DATA_PtResolution_AK4PFchs.txt"
          jerInputFileSource = "https://raw.githubusercontent.com/cms-jet/JRDatabase/master/textFiles/Fall17_V3b_DATA/Fall17_V3b_DATA_PtResolution_AK4PFchs.txt"
        elif int(Year) == 2018:
          jerInputFileName = "Autumn18_V7b_DATA_PtResolution_AK4PFchs.txt"
          jerInputFileSource = "https://raw.githubusercontent.com/cms-jet/JRDatabase/master/textFiles/Autumn18_V7b_DATA/Autumn18_V7b_DATA_PtResolution_AK4PFchs.txt"
        self.jerInputArchivePath = os.environ['CMSSW_BASE'] + "/src/PhysicsTools/NanoAODTools/data/jme/"
        if not os.path.isfile(self.jerInputArchivePath+'/'+jerInputFileName):
            print "Get JER source from ",jerInputFileSource
            os.system('wget '+jerInputFileSource+" -O "+self.jerInputArchivePath+'/'+jerInputFileName)
        self.jerInputFilePath = self.jerInputArchivePath
        self.jerInputFileName = jerInputFileName
        self.params_sf_and_uncertainty = ROOT.PyJetParametersWrapper()
        self.params_resolution = ROOT.PyJetParametersWrapper()
        for library in [ "libCondFormatsJetMETObjects", "libPhysicsToolsNanoAODTools" ]:
            if library not in ROOT.gSystem.GetLibraries():
                print("Load Library '%s'" % library.replace("lib", ""))
                ROOT.gSystem.Load(library)

    def beginJob(self):
        print("Loading jet energy resolutions (JER) from file '%s'" % os.path.join(self.jerInputFilePath, self.jerInputFileName))
        self.jer = ROOT.PyJetResolutionWrapper(os.path.join(self.jerInputFilePath,self.jerInputFileName))

        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree

        ##---Boosted Region kinematics
        for var in ['pt','eta','phi','mass','Mt']:
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
        self.out.branch('AddJetBoosted_cjidx','I',lenVar='nAddJetBoosted')

        self.out.branch('isVBF_Boosted','O')
        self.out.branch('VBFjjBoosted_mjj','F')
        self.out.branch('VBFjjBoosted_dEta','F')
        self.out.branch('max_mjj_Boosted','F')

        ##---Resolved Region kinemaics
        for algo in MYALGO:
            _algo='_'+algo
            self.out.branch('isResolved'+_algo,"O")
            for var in ['pt','eta','phi','mass','Mt','ScoreToLeast']:
                self.out.branch('Whad_'+var+_algo,'F')

            self.out.branch('Whad_cjidx1'+_algo,'I')
            self.out.branch('Whad_cjidx2'+_algo,'I')
            self.out.branch('BJetResolved_cjidx'+_algo,'I',lenVar='nBJetResolved'+_algo)
            self.out.branch('AddJetResolved_cjidx'+_algo,'I',lenVar='nAddJetResolved'+_algo)
            self.out.branch('isVBF_Resolved'+_algo,'O')
            self.out.branch('VBFjjResolved_dEta'+_algo,'F')
            self.out.branch('VBFjjResolved_mjj'+_algo,'F')
            self.out.branch('VBFjjResolved_dEta'+_algo,'F')
            self.out.branch('max_mjj_Resolved'+_algo,'F')

            self.out.branch('lnjj_pt'+_algo, 'F')
            self.out.branch('lnjj_mass'+_algo, 'F')
            self.out.branch('lnjj_Mt'+_algo, 'F')
            self.out.branch('minPtWOverMlnjj'+_algo,'F')
            self.out.branch('maxPtWOverMlnjj'+_algo,'F')
            self.out.branch('dR_l_Whad'+_algo,'F')
            self.out.branch('dR_Wlep_Whad'+_algo,'F')
            self.out.branch('dPhi_l_Whad'+_algo,'F')
            self.out.branch('dPhi_Wlep_Whad'+_algo,'F')



        
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
        self._AddJetBoosted_cjidx=[]
        self._isVBF_Boosted=False
        self._VBFjjBoosted_dEta=-999.
        self._VBFjjBoosted_mjj=-999.
        self._VBFjjBoosted_cjidx1=-1
        self._VBFjjBoosted_cjidx2=-1
        self._max_mjj_Boosted=-1.

        self.cfjidx_FatSel['MW']=-1 ## FatJet_mass ~ MW
        self.cfjidx_FatSel['PT']=-1## largest PT

        ##--Resolved--##
        self._isResolved = {}
        self._Whad_4v = {}
        self._Whad_ScoreToLeast = {}
        self._Whad_cjidx1={}
        self._Whad_cjidx2={}
        self._BJetResolved_cjidx={}
        self._AddJetResolved_cjidx={}
        self._isVBF_Resolved={}
        self._VBFjjResolved_dEta={}
        self._VBFjjResolved_mjj={}
        self._VBFjjResolved_cjidx1={}
        self._VBFjjResolved_cjidx2={}
        self._max_mjj_Resolved = {}
        for algo in MYALGO:
            self._isResolved[algo] = False
            self._Whad_4v[algo]=ROOT.TLorentzVector()
            self._Whad_4v[algo].SetPtEtaPhiM(0,0,0,0)
            self._Whad_ScoreToLeast[algo] = sys.float_info.max 

            self._Whad_cjidx1[algo]=-1
            self._Whad_cjidx2[algo]=-1
            self._BJetResolved_cjidx[algo]=[]
            self._AddJetResolved_cjidx[algo]=[]
            self._isVBF_Resolved[algo]=False
            self._VBFjjResolved_dEta[algo]=-999.
            self._VBFjjResolved_mjj[algo]=-999.
            self._VBFjjResolved_cjidx1[algo]=-1
            self._VBFjjResolved_cjidx2[algo]=-1
            self._max_mjj_Resolved[algo] = -1. 
        ##--End of initialization

        
        ##--Get object collections--##
        self.Lepton = Object(event, 'Lepton', index=0)
        self.CleanFatJet_col = Collection(event, 'CleanFatJet')
        self.FatJet_col = Collection(event, 'FatJet')
        self.CleanJet_col = Collection(event, 'CleanJet')
        self.CleanJetNotFat_col = Collection(event, 'CleanJetNotFat')
        self.Jet_col = Collection(event,"Jet")
        self.rho = event.fixedGridRhoFastjetAll##For deriving resulution 
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
        if (len(self._cfatjet_idx_list) > 0) and ( self.MET_pt > self.METcut_Boosted): 
            self._isBoosted=True
        
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
        self.out.fillBranch('Wlep_Mt',self._Wlep_Mt)
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
        self.out.fillBranch('AddJetBoosted_cjidx', self._AddJetBoosted_cjidx)
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
        for algo in MYALGO:
            _algo='_'+algo
            #self.WhadMaker()
            #self.WhadMakerMWrawFchi2()
            exec('self.WhadMaker("'+algo+'")')
            ##set      self._Whad_4v
            ##set      self._Whad_cjidx1
            ##set      self._Whad_cjidx2
            ##set      self._isResolved
            
            ##Step.2 Get Btag
            #self.GetBJetsResolved()
            exec('self.GetBJetsResolved("'+algo+'")')
            ##set      self._BJetResolved_cjidx
        

            ##Step.3 VBF_Resolved
            exec('self.VBF_Resolved("'+algo+'")')
            ##set      self._VBFjjResolved_mjj
            ##set      self._VBFjjResolved_dEta
            ##set      self._VBFjjResolved_cjidx1
            ##set      self._VBFjjResolved_cjidx2
            ##set      self._isVBF_Resolved
            ##set      self._VBFjjResolved_mjj
            
            #print "fill resolved"
            
            ##Fill branch
            self.out.fillBranch('isResolved'+_algo,self._isResolved[algo])

            ##Hadronic W
            self.out.fillBranch('Whad_pt'+_algo, self._Whad_4v[algo].Pt())
            self.out.fillBranch('Whad_eta'+_algo, self._Whad_4v[algo].Eta())
            self.out.fillBranch('Whad_phi'+_algo, self._Whad_4v[algo].Phi())
            self.out.fillBranch('Whad_mass'+_algo, self._Whad_4v[algo].M())
            self.out.fillBranch('Whad_Mt'+_algo, self._Whad_4v[algo].Mt())
            self.out.fillBranch('Whad_ScoreToLeast'+_algo, self._Whad_ScoreToLeast[algo])

            self.out.fillBranch('Whad_cjidx1'+_algo, self._Whad_cjidx1[algo])
            self.out.fillBranch('Whad_cjidx2'+_algo, self._Whad_cjidx2[algo])
            self.out.fillBranch('BJetResolved_cjidx'+_algo, self._BJetResolved_cjidx[algo])
            self.out.fillBranch('AddJetResolved_cjidx'+_algo, self._AddJetResolved_cjidx[algo])

            ###VBF
            self.out.fillBranch('isVBF_Resolved'+_algo, self._isVBF_Resolved[algo])
            self.out.fillBranch('VBFjjResolved_dEta'+_algo, self._VBFjjResolved_dEta[algo])
            self.out.fillBranch('VBFjjResolved_mjj'+_algo, self._VBFjjResolved_mjj[algo])
            self.out.fillBranch('VBFjjResolved_dEta'+_algo, self._VBFjjResolved_dEta[algo])
            self.out.fillBranch('max_mjj_Resolved'+_algo, self._max_mjj_Resolved[algo])

            ##Hlnjj
            H_4v=self._Wlep_4v + self._Whad_4v[algo]
            lnjj_pt = H_4v.Pt()
            lnjj_mass = H_4v.M()
            whad_pt = self._Whad_4v[algo].Pt()
            whad_mass = self._Whad_4v[algo].M()
            whad_Et = math.sqrt(whad_pt**2 + whad_mass**2)
            lnjj_Et = whad_Et+ self.Lepton.pt + self.MET_pt
            lnjj_px = whad_pt * math.cos(self._Whad_4v[algo].Phi()) + self.Lepton.pt*math.cos(self.Lepton.phi) + self.MET_pt*math.cos(self.MET_phi)
            lnjj_py = whad_pt * math.sin(self._Whad_4v[algo].Phi()) + self.Lepton.pt*math.sin(self.Lepton.phi) + self.MET_pt*math.sin(self.MET_phi)
            lnjj_pt = math.sqrt(lnjj_px**2 + lnjj_py**2)
            lnjj_Mt= 0
            try:
                lnjj_Mt = math.sqrt(lnjj_Et**2 - lnjj_pt**2)
            except ValueError:
                #print "lnjj_Et=",lnjj_Et
                #print "lnjj_pt=",lnjj_pt
                #print "whad_mass=",whad_mass
                #print "whad_pt=",whad_pt
                #print "whad_Et=",whad_Et
                lnjj_Mt=0
                
            minPtWOverMlnjj = min(self._Wlep_4v.Pt(), self._Whad_4v[algo].Pt())/lnjj_mass
            maxPtWOverMlnjj = max(self._Wlep_4v.Pt(), self._Whad_4v[algo].Pt())/lnjj_mass
            ##DeltaR, DeltaPhi between l - Whad OR Wlep - Whad
            dR_l_Whad=self._Whad_4v[algo].DeltaR(self._lepton_4v)
            dR_Wlep_Whad=self._Whad_4v[algo].DeltaR(self._Wlep_4v)
            dPhi_l_Whad=self._Whad_4v[algo].DeltaPhi(self._lepton_4v)
            dPhi_Wlep_Whad=self._Whad_4v[algo].DeltaPhi(self._Wlep_4v)
            self.out.fillBranch('lnjj_pt'+_algo, lnjj_pt)
            self.out.fillBranch('lnjj_mass'+_algo, lnjj_mass)
            self.out.fillBranch('lnjj_Mt'+_algo, lnjj_Mt)
            self.out.fillBranch('minPtWOverMlnjj'+_algo,minPtWOverMlnjj)
            self.out.fillBranch('maxPtWOverMlnjj'+_algo,maxPtWOverMlnjj)
            self.out.fillBranch('dR_l_Whad'+_algo,dR_l_Whad)
            self.out.fillBranch('dR_Wlep_Whad'+_algo,dR_Wlep_Whad)
            self.out.fillBranch('dPhi_l_Whad'+_algo,dPhi_l_Whad)
            self.out.fillBranch('dPhi_Wlep_Whad'+_algo,dPhi_Wlep_Whad)
            



            #print "End of fllbranch"


            #print "self._isBoosted",self._isBoosted
            #print "self._isResolved",self._isResolved
            
            ##<<<<End of Resolved


        if event.event % 10000 ==1 :##To flush memory of ttree
            print >> sys.stderr, "[jhchoi]AutoSave, #event=",event.event
            self.out._tree.AutoSave("FlushBaskets")


        if (not self._isBoosted) and (not any( self._isResolved.values())) and self.doSkim: return False

        
        


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
        self._Wlep_METpz1=met_pz_1
        self._Wlep_METpz2=met_pz_2

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
        
        ##-- Wlep Mt 
        self._Wlep_Mt=math.sqrt(2*lepton_pt*met_pt*(1-math.cos(lepton_phi - met_phi ) ) )


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
        if not self._isBoosted:
            return
        ##->Set self._BJetBoosted_cjidx
        #self.CleanJetNotFat_col
        bWP=self.bWP
        #N=len(self.CleanJetNotFat_col)
        N=len(self.CleanJet_col)
        ##jhchoi##
        #idx_list=[]
        #for i_cj in range(0,N): ##-- i_cj = idx of self.CleanJetNotFat_col
        #    cj_idx=self.CleanJetNotFat_col[i_cj].jetIdx
        #    idx_list.append(cj_idx)
        for i_cj in range(0,N): ##-- i_cj = idx of self.CleanJetNotFat_col
            #if self.CleanJetNotFat_col[i_cj].deltaR < 0 : continue
            #cj_idx=self.CleanJetNotFat_col[i_cj].jetIdx
            cj_idx=i_cj
            if self.IsAK4inAK8(cj_idx): continue
            #try:
            pt=self.CleanJet_col[cj_idx].pt
            eta=self.CleanJet_col[cj_idx].eta
            j_idx=self.CleanJet_col[cj_idx].jetIdx
            bAlgo=self.Jet_col[j_idx].btagDeepB

            
            if pt < 20 :continue
            if abs(eta) > 2.5:continue
            self._AddJetBoosted_cjidx.append(cj_idx) ## fill index of CleanJet 
            if bAlgo < bWP:continue
            self._BJetBoosted_cjidx.append(cj_idx) ## fill index of CleanJet
            #except IndexError:
            #    print "len(self.CleanFatJet_col)=",len(self.CleanFatJet_col)
            #    print "cj_idx=",cj_idx
            #    print "dR=",self.CleanJetNotFat_col[i_cj].deltaR
            #    #print idx_list
            #    print "N not fat=",N
            #    print "N cleanjet=",len(self.CleanJet_col)
    def GetBJetsResolved(self,algo_):
        algo=algo_
        ##->Set self._BJetResolved_cjidx
        #self.CleanJet_col
        bWP=self.bWP
        N=self.CleanJet_col._len
        for i_cj in range(0,N):
            if i_cj == self._Whad_cjidx1[algo] : continue
            if i_cj == self._Whad_cjidx2[algo] : continue
            
            pt=self.CleanJet_col[i_cj].pt
            eta=self.CleanJet_col[i_cj].eta
            j_idx=self.CleanJet_col[i_cj].jetIdx ##Jet Object index
            bAlgo=self.Jet_col[j_idx].btagDeepB
            
            if pt < 20 :continue
            if abs(eta) > 2.5:continue
            self._AddJetResolved_cjidx[algo].append(i_cj) ## fill index of CleanJet
            if bAlgo < bWP:continue
            self._BJetResolved_cjidx[algo].append(i_cj) ## fill index of CleanJet
            



    def VBF_Boosted(self):
        if not self._isBoosted:
            self._isVBF_Boosted = False
            return
        #N=self.CleanJetNotFat_col._len
        N=self.CleanJet_col._len
        if N < 2 :
            #print "NCleanJet < 2"
            self._isVBF_Boosted = False
            return
        
        #max_mjj=-9999.
        for i_cj in range(0,N):
            #if self.CleanJetNotFat_col[i_cj].deltaR < 0 : continue
            #cjidx1 = self.CleanJetNotFat_col[i_cj].jetIdx ##index of CleanJet
            cjidx1 = i_cj
            pt1,eta1,phi1,mass1 = self.CleanJet_PtEtaPhiM(cjidx1)
            if pt1 < 30 : continue
            if abs(eta1) > 4.7 : continue
            if self.IsAK4inAK8(cjidx1) : continue
            for j_cj in range(0,N):
                if j_cj <= i_cj : continue ##aviod doubly checked or the same one
                #if self.CleanJetNotFat_col[j_cj].deltaR < 0 : continue
                #cjidx2 = self.CleanJetNotFat_col[j_cj].jetIdx ##index of CleanJet
                cjidx2=j_cj
                if self.IsAK4inAK8(cjidx2) : continue
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

    def VBF_Resolved(self,algo_):
        algo=algo_
        N = self.CleanJet_col._len ##->change to CleanJetColl
        if N < 2 : ## could it be 4 ?
            self._isVBF_Resolved[algo] = False
            return
        #print "--pass Njet>=4"
        #max_mjj=-9999.
        for i_cj in range(0,N):
            ##->add not whad
            if i_cj == self._Whad_cjidx1[algo] : continue
            if i_cj == self._Whad_cjidx2[algo] : continue
            pt1,eta1,phi1,mass1 = self.CleanJet_PtEtaPhiM(i_cj)
            if pt1 < 30 : continue
            if abs(eta1) > 4.7 : continue

            for j_cj in range(0,N):
                if j_cj <= i_cj : continue ##doubly checked or the same one
                if j_cj == self._Whad_cjidx1[algo] : continue
                if j_cj == self._Whad_cjidx2[algo] : continue
                ##->add not whad
                pt2,eta2,phi2,mass2 = self.CleanJet_PtEtaPhiM(j_cj)
                if pt2 < 30: continue
                if abs(eta2) > 4.7 : continue
                #print "-pass whad jet idx- "
                ##Set momentum##

                this_dEta=abs(eta1-eta2)
                this_mjj = self.InvMassCalc(pt1,eta1,phi1,mass1,pt2,eta2,phi2,mass2)
                #print "this_mjj",this_mjj
                #print "this_dEta",this_dEta
                #print "self._VBFjjResolved_mjj",self._VBFjjResolved_mjj
                if (this_dEta > 3.5) and (this_mjj > self._VBFjjResolved_mjj[algo]) :
                    #print "=define values-"
                    
                    self._VBFjjResolved_dEta[algo] = this_dEta
                    self._VBFjjResolved_mjj[algo] = this_mjj
                    self._VBFjjResolved_cjidx1[algo] = i_cj
                    self._VBFjjResolved_cjidx2[algo] = j_cj
                if this_mjj > self._max_mjj_Resolved:
                    self._max_mjj_Resolved[algo] = this_mjj

        ##--End of jet pair loop
        if self._VBFjjResolved_mjj[algo] > 500. : self._isVBF_Resolved[algo] = True
        #print "_VBFjjResolved_mjj=",self._VBFjjResolved_mjj


    ##Jet Cleaning
    def IsAK4inAK8(self,cj_idx):
        pt1,eta1,phi1,mass1 = self.CleanJet_PtEtaPhiM(cj_idx)
        _v1 = ROOT.TLorentzVector()
        _v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
        for cfjidx in self._cfatjet_idx_list:
            pt2,eta2,phi2,mass2 = self.CleanFatJet_PtEtaPhiM(cfjidx)
            _v2 = ROOT.TLorentzVector()
            _v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2)
            dR=_v2.DeltaR(_v1)
            if dR < 0.8 : return True
        return False


    def WhadMaker(self,algo_):
        algo=algo_
        N=self.CleanJet_col._len
        ScoreToLeast=sys.float_info.max
        
        Whad_mass=-9999.
        for i_cj in range(0,N):
            pt1,eta1,phi1,mass1,rawFactor1 = self.CleanJet_PtEtaPhiMrawFactor(i_cj)
            if pt1 < 30. : continue
            if abs(eta1) > 2.4 : continue 
            for j_cj in range(0,N):
                if j_cj <= i_cj : continue
                pt2,eta2,phi2,mass2,rawFactor2 = self.CleanJet_PtEtaPhiMrawFactor(j_cj)
                if pt2 < 30. : continue
                if abs(eta2) > 2.4 : continue

                thisScore = sys.float_info.max
                if algo=="dM":
                    thisScore = self.CalcDM(pt1,eta1,phi1,mass1,\
                                       pt2,eta2,phi2,mass2)
                elif algo=="dMchi2rawF":
                    thisScore = self.CalcChi2rawFactor(pt1, eta1, phi1, mass1, rawFactor1,\
                                                  pt2, eta2, phi2, mass2, rawFactor2)
                elif algo=="dMchi2rawFqgl":
                    thisScore = self.CalcInvLikelihood(i_cj, j_cj)
                elif algo=="dMchi2Resolution":
                    thisScore = self.CalcChi2DMReolsution(i_cj, j_cj,self.rho)

                elif algo=="dMchi2Resolutionqgl":
                    thisScore = self.CalcChi2DMReolsutionQgl(i_cj, j_cj,self.rho)
                elif algo=="HighPTjj":
                    thisScore = self.CalcHighPTjj(i_cj, j_cj)
                elif algo=="LowPTjj":
                    thisScore = self.CalcLowPTjj(i_cj, j_cj)
                    
                ##Go to CalcAlgo

                #v1=ROOT.TLorentzVector()
                #v2=ROOT.TLorentzVector()
                #v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
                #v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2)                
                #this_M=(v1+v2).M()
                #this_dM=abs(Wmass-this_M)
                ##End of go to calcalgo

                if thisScore < ScoreToLeast:
                    ScoreToLeast = thisScore
                    v1=ROOT.TLorentzVector()
                    v2=ROOT.TLorentzVector()
                    v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
                    v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2)
                    self._Whad_cjidx1[algo] = i_cj
                    self._Whad_cjidx2[algo] = j_cj
                    self._Whad_4v[algo] = v1+v2
        Whad_mass=self._Whad_4v[algo].M()
        self._Whad_ScoreToLeast[algo] = ScoreToLeast
        if Whad_mass > 40 and Whad_mass < 250 : self._isResolved[algo] = True
        if ScoreToLeast==sys.float_info.max : self._isResolved[algo] = False ##for safety
        if self._Whad_cjidx1[algo] < 0 : self._isResolved[algo] = False #for safty
        if self._Whad_cjidx2[algo] < 0 : self._isResolved[algo] = False #for safty

    def CalcDM(self,\
               pt1, eta1, phi1, mass1,\
               pt2, eta2, phi2, mass2):


        v1=ROOT.TLorentzVector()
        v2=ROOT.TLorentzVector()
        v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
        v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2)
        this_M=(v1+v2).M()
        this_dM=abs(Wmass-this_M)
        return this_dM

    def CalcChi2rawFactor(self,\
                          pt1, eta1, phi1, mass1, rawFactor1,\
                          pt2, eta2, phi2, mass2, rawFactor2):
        v1=ROOT.TLorentzVector()
        v2=ROOT.TLorentzVector()
        v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
        v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2)
        v1before=ROOT.TLorentzVector()
        v2before=ROOT.TLorentzVector()
        v1before.SetPtEtaPhiM(pt1*(1-rawFactor1), eta1, phi1, mass1)
        v2before.SetPtEtaPhiM(pt2*(1-rawFactor2), eta2, phi2, mass2)
        this_M=(v1+v2).M()
        this_Mbefore=(v1before+v2before).M()
        this_dM=abs(Wmass-this_M)
        this_Msigma=abs(this_Mbefore-this_M)
        this_chi2= this_dM**2 / this_Msigma**2
        return this_chi2

    def CalcInvLikelihood(self,\
                          i_cj,\
                          j_cj):
        pt1,eta1,phi1,mass1,rawFactor1,qgl1 = self.CleanJet_PtEtaPhiMrawFactorQgl(i_cj)
        pt2,eta2,phi2,mass2,rawFactor2,qgl2 = self.CleanJet_PtEtaPhiMrawFactorQgl(j_cj)
        if qgl1 < 0 : return sys.float_info.max
        if qgl2 < 0 : return sys.float_info.max
        v1=ROOT.TLorentzVector()
        v2=ROOT.TLorentzVector()
        v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
        v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2)
        v1before=ROOT.TLorentzVector()
        v2before=ROOT.TLorentzVector()
        v1before.SetPtEtaPhiM(pt1*(1-rawFactor1), eta1, phi1, mass1)
        v2before.SetPtEtaPhiM(pt2*(1-rawFactor2), eta2, phi2, mass2)
        this_M=(v1+v2).M()
        this_Mbefore=(v1before+v2before).M()
        this_dM=abs(Wmass-this_M)
        this_Msigma=abs(this_Mbefore-this_M)
        this_chi2= this_dM**2 / this_Msigma**2
        ##Likelihood = 1/sqrt(sigma)*exp(-x**2/2)
        #let it -log(likelihood) ->MLL
        #print "this_Msigma=",this_Msigma
        #print "this_chi2=",this_chi2
        this_MLL = math.log(math.sqrt(this_Msigma))+this_chi2/2
        #print 'before=',this_MLL
        try:
            this_MLL += -1*math.log(qgl1*qgl2)
        except ValueError:
            this_MLL = sys.float_info.max
        #print 'after=',this_MLL
        return this_MLL

    def CalcChi2DMReolsution(self,i_cj, j_cj,rho):
        pt1,eta1,phi1,mass1 = self.CleanJet_PtEtaPhiM(i_cj)
        pt2,eta2,phi2,mass2 = self.CleanJet_PtEtaPhiM(j_cj)

        v1=ROOT.TLorentzVector()
        v2=ROOT.TLorentzVector()
        v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
        v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2)
        #rho=event.fixedGridRhoFastjetAll
        resol1= self.getJetPtResolution(v1,rho)
        resol2= self.getJetPtResolution(v2,rho)
        M=(v1+v2).M()
        ##--j1 up--##
        v1.SetPtEtaPhiM(pt1*(1+resol1), eta1, phi1, mass1 )
        M_j1up = (v1+v2).M()
        ##--j1 do--##
        v1.SetPtEtaPhiM(pt1*(1-resol1), eta1, phi1, mass1 )
        M_j1do = (v1+v2).M()
        ##--j2 up--##
        v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
        v2.SetPtEtaPhiM(pt2*(1+resol2),eta2,phi2,mass2)
        M_j2up = (v1+v2).M()
        ##--j2 do--##
        v2.SetPtEtaPhiM(pt2*(1+resol2),eta2,phi2,mass2)
        M_j2do = (v1+v2).M()
        sigma2=(M-M_j1up)**2 + (M-M_j1do)**2 +(M-M_j2up)**2 +(M-M_j2do)**2
        this_Chi2=(M-Wmass)**2/sigma2


        return this_Chi2



    def CalcChi2DMReolsutionQgl(self,i_cj, j_cj,rho):
        pt1,eta1,phi1,mass1,rawFactor1,qgl1 = self.CleanJet_PtEtaPhiMrawFactorQgl(i_cj)
        pt2,eta2,phi2,mass2,rawFactor2,qgl2 = self.CleanJet_PtEtaPhiMrawFactorQgl(j_cj)
        if qgl1 < 0 : return sys.float_info.max
        if qgl2 < 0 : return sys.float_info.max
        v1=ROOT.TLorentzVector()
        v2=ROOT.TLorentzVector()
        v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
        v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2)
        #rho=event.fixedGridRhoFastjetAll
        resol1= self.getJetPtResolution(v1,rho)
        resol2= self.getJetPtResolution(v2,rho)
        M=(v1+v2).M()
        ##--j1 up--##
        v1.SetPtEtaPhiM(pt1*(1+resol1), eta1, phi1, mass1 )
        M_j1up = (v1+v2).M()
        ##--j1 do--##
        v1.SetPtEtaPhiM(pt1*(1-resol1), eta1, phi1, mass1 )
        M_j1do = (v1+v2).M()
        ##--j2 up--##
        v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
        v2.SetPtEtaPhiM(pt2*(1+resol2),eta2,phi2,mass2)
        M_j2up = (v1+v2).M()
        ##--j2 do--##
        v2.SetPtEtaPhiM(pt2*(1+resol2),eta2,phi2,mass2)
        M_j2do = (v1+v2).M()
        sigma2=(M-M_j1up)**2 + (M-M_j1do)**2 +(M-M_j2up)**2 +(M-M_j2do)**2
        this_Msigma=math.sqrt(sigma2)
        this_chi2=(M-Wmass)**2/sigma2
        this_MLL = math.log(math.sqrt(this_Msigma))+this_chi2/2
        #print 'before=',this_MLL
        try:
            this_MLL += -1*math.log(qgl1*qgl2)
        except ValueError:
            this_MLL = sys.float_info.max
        #print 'after=',this_MLL
        return this_MLL


        #return this_Chi2

    def CalcHighPTjj(self, i_cj, j_cj):
        pt1,eta1,phi1,mass1 = self.CleanJet_PtEtaPhiM(i_cj)
        pt2,eta2,phi2,mass2 = self.CleanJet_PtEtaPhiM(j_cj)

        v1=ROOT.TLorentzVector()
        v2=ROOT.TLorentzVector()
        v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
        v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2)

        ptjj=(v1+v2).Pt()
        Mjj=(v1+v2).M()
        if Mjj <40 : return sys.float_info.max
        if Mjj >250 : return sys.float_info.max
        #print ptjj
        return -1*ptjj
    def CalcLowPTjj(self, i_cj, j_cj):
        pt1,eta1,phi1,mass1 = self.CleanJet_PtEtaPhiM(i_cj)
        pt2,eta2,phi2,mass2 = self.CleanJet_PtEtaPhiM(j_cj)

        v1=ROOT.TLorentzVector()
        v2=ROOT.TLorentzVector()
        v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
        v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2)

        ptjj=(v1+v2).Pt()
        Mjj=(v1+v2).M()
        if Mjj <40 : return sys.float_info.max
        if Mjj >250 : return sys.float_info.max
        #print ptjj
        return ptjj



    def WhadMakerdM(self):
        algo='dM'
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
                    self._Whad_cjidx1[algo] = i_cj
                    self._Whad_cjidx2[algo] = j_cj
                    self._Whad_4v[algo] = v1+v2
        Whad_mass=self._Whad_4v[algo].M()
        if Whad_mass > 40 and Whad_mass < 250 : self._isResolved[algo] = True
        if self._Whad_cjidx1[algo] < 0 : self._isResolved[algo] = False #for safty
        if self._Whad_cjidx2[algo] < 0 : self._isResolved[algo] = False #for safty

    def WhadMakerdMchi2rawF(self):
        algo='dMchi2rawF'
        N=self.CleanJet_col._len
        chi2=sys.float_info.max
        Whad_mass=-9999.
        for i_cj in range(0,N):
            pt1,eta1,phi1,mass1,rawFactor1 = self.CleanJet_PtEtaPhiMrawFactor(i_cj)
            if pt1 < 30. : continue
            if abs(eta1) > 2.4 : continue
            for j_cj in range(0,N):
                if j_cj <= i_cj : continue
                pt2,eta2,phi2,mass2,rawFactor2 = self.CleanJet_PtEtaPhiMrawFactor(j_cj)
                if pt2 < 30. : continue
                if abs(eta2) > 2.4 : continue
                v1=ROOT.TLorentzVector()
                v2=ROOT.TLorentzVector()
                v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
                v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2)
                v1before=ROOT.TLorentzVector()
                v2before=ROOT.TLorentzVector()
                v1before.SetPtEtaPhiM(pt1*(1-rawFactor1), eta1, phi1, mass1)
                v2before.SetPtEtaPhiM(pt2*(1-rawFactor2), eta2, phi2, mass2)
                this_M=(v1+v2).M()
                this_Mbefore=(v1before+v2before).M()
                this_dM=abs(Wmass-this_M)
                this_Msigma=abs(this_Mbefore-this_M)
                this_chi2= this_dM**2 / this_Msigma**2
                if this_chi2 < chi2:
                    chi2 = this_chi2

                    self._Whad_cjidx1[algo] = i_cj
                    self._Whad_cjidx2[algo] = j_cj
                    self._Whad_4v[algo] = v1+v2
        Whad_mass=self._Whad_4v[algo].M()
        if Whad_mass > 40 and Whad_mass < 250 : self._isResolved[algo] = True
        if self._Whad_cjidx1[algo] < 0 : self._isResolved[algo] = False #for safty
        if self._Whad_cjidx2[algo] < 0 : self._isResolved[algo] = False #for safty



    def CleanJet_PtEtaPhiM(self,cjidx):
        pt=self.CleanJet_col[cjidx].pt
        eta=self.CleanJet_col[cjidx].eta
        phi=self.CleanJet_col[cjidx].phi
        jidx=self.CleanJet_col[cjidx].jetIdx
        mass=self.Jet_col[jidx].mass
        return pt,eta,phi,mass

    def CleanJet_PtEtaPhiMrawFactor(self,cjidx):
        pt=self.CleanJet_col[cjidx].pt
        eta=self.CleanJet_col[cjidx].eta
        phi=self.CleanJet_col[cjidx].phi
        jidx=self.CleanJet_col[cjidx].jetIdx
        mass=self.Jet_col[jidx].mass
        rawFactor=self.Jet_col[jidx].rawFactor
        return pt,eta,phi,mass,rawFactor 

    def CleanJet_PtEtaPhiMrawFactorQgl(self,cjidx):
        pt=self.CleanJet_col[cjidx].pt
        eta=self.CleanJet_col[cjidx].eta
        phi=self.CleanJet_col[cjidx].phi
        jidx=self.CleanJet_col[cjidx].jetIdx
        mass=self.Jet_col[jidx].mass
        rawFactor=self.Jet_col[jidx].rawFactor
        qgl=self.Jet_col[jidx].qgl
        return pt,eta,phi,mass,rawFactor,qgl 

    def CleanFatJet_PtEtaPhiM(self,cfjidx):
        pt=self.CleanFatJet_col[cfjidx].pt
        eta=self.CleanFatJet_col[cfjidx].eta
        phi=self.CleanFatJet_col[cfjidx].phi
        mass=self.CleanFatJet_col[cfjidx].mass
        
        return pt,eta,phi,mass

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
        return jet_pt_resolution



# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed                    
HMlnjjVars_Dev_jhchoi = lambda : HMlnjjVarsClass_Dev_jhchoi()

