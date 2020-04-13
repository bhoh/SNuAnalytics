# LatinoAnalysis/NanoGardener/python/modules 

import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import math
import numpy
import re
import os
import sys
from math import sqrt

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

from LatinoAnalysis.NanoGardener.data.HMlnjjVars_Dev_jhchoi_cfg import HMlnjjVarsCuts,MELAcfg
from LatinoAnalysis.NanoGardener.data.Wtagger_cfg import WJID,FATJETCUTS


Wmass=80.4
MaxLimit =  sys.float_info.max
MinLimit = -1.



class HMlnjjVarsClass_Dev(Module):
    def __init__(self, year, METtype='PuppiMET',fjsysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown'],jetsysvars='all',pairalgos=['dMchi2Resolution','dM'],jsyssources="all", doSkim=False):
        year=str(year)
        ##tagging methods for W->FJ or W->jj
        self.pairalgos=pairalgos
        self.WtaggerConfig=WJID[year]
        ##systematics
        self.fjsysvars=fjsysvars
        self.jetsysvars=jetsysvars

        
        ##--ak4jet uncertainty sources
        #jsources=[]
        if jsyssources=="all":
            jsources=['jesFlavorQCD','jesRelativeBal','jesHF','jesBBEC1','jesEC2','jesAbsolute','jesAbsolute_'+str(year),'jesHF_'+str(year),'jesEC2_'+str(year),'jesRelativeSample_'+str(year),'jesBBEC1_'+str(year),'jesTotal','jer']
        if jsyssources=="correlate":
            jsources=['jesFlavorQCD','jesRelativeBal','jesHF','jesBBEC1','jesEC2','jesAbsolute','jesTotal']
        if jsyssources=="uncorrelate":
            jsources=['jesAbsolute_'+str(year),'jesHF_'+str(year),'jesEC2_'+str(year),'jesRelativeSample_'+str(year),'jesBBEC1_'+str(year),'jer']




        if jetsysvars=="all" or jetsysvars=="up" or jetsysvars=="down":

            directions=[]
            if jetsysvars=="all" : directions=['Up','Down']
            if jetsysvars=="up" : directions=['Up']
            if jetsysvars=="down" : directions=['Down']

            self.jetsysvars=[]
            for s in jsources:
                for d in directions:
                    self.jetsysvars.append(s+d)
            print "[directions]",directions
            print "[jsources]",jsources
        ##--Read MELA mass cfg--##
        self.mH_boost=MELAcfg[year]['mH_boost']
        self.mH_resol=MELAcfg[year]['mH_resol']


        self.cmssw_base = os.getenv('CMSSW_BASE')
        cmssw_arch = os.getenv('SCRAM_ARCH')
        ##To declare object only once
        self._MET_4v        = ROOT.TLorentzVector()
        #self._MET_big4v     = ROOT.TLorentzVector()

        self._lepton_4v     = ROOT.TLorentzVector()
        self._Wlep_4v       = ROOT.TLorentzVector()
        #self._Wlep_big4v    = ROOT.TLorentzVector()
        
        self._WhadBoost_4v = ROOT.TLorentzVector()
        self._WhadBoost_4v= ROOT.TLorentzVector()##FatJet momentum
	self._lnJ_4v        = ROOT.TLorentzVector() ## H@boosted region momentum

        #self._WhadResol_j1_4v    = ROOT.TLorentzVector()
        #self._WhadResol_j2_4v    = ROOT.TLorentzVector()
        self._WhadResol_4v       = ROOT.TLorentzVector()

	# TODO  let's think the usage of this MET_Z solution
	#self._lnJ_big4v     = ROOT.TLorentzVector()
	self._lnjj_4v       = ROOT.TLorentzVector()
	#self._lnjj_big4v    = ROOT.TLorentzVector()
	
        self.doSkim = doSkim
        self.PassAtLeastOne=False
        self.METtype = METtype

        self._Whad_j1_4v = ROOT.TLorentzVector()
        self._Whad_j2_4v = ROOT.TLorentzVector()

        self._vbfj1_4v = ROOT.TLorentzVector()
        self._vbfj2_4v = ROOT.TLorentzVector()
        

        #####################################
	# Cuts
        #####################################
        for name in HMlnjjVarsCuts[year]:##Get cuts from HMlnjjVars_Dev_jhchoi_cfg.py
            exec('self.'+name+' = HMlnjjVarsCuts[year]["'+name+'"]')
            ##eg) self.Wmass_CRlow = HMlnjjVarsCuts[year]["Wmass_CRlow"]

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

        # TODO high mass sample dependent mass and gamma
	#massH = 400
        #gsmH = self.g.GetBinContent(self.g.FindBin(massH))
        #self.mela = ROOT.MelaHighMassKDwCalc(13, massH, gsmH )
        self.mela = ROOT.MelaHighMassKDwCalc(13, 125, 0.00407 )##add 125GeV Higgs to mela model
        self.out = wrappedOutputTree
        self.debug = False
	if self.debug:
	  self.evtMyNum = 0


        '''
        self.fjsysvars=fjsysvars
        self.jetsysvars=jetsysvars
        self.pairalgos=pairalgos

        '''
        ##for boosted region##
        for wtag in self.WtaggerConfig:
            for fjsysvar in self.fjsysvars:
                for jsysvar in self.jetsysvars:
                    
                    nvar=0 ## number of varaitions. ->must be 0 Or 1
                    if fjsysvar!="nom":
                        nvar+=1
                    if jsysvar!="nom":
                        nvar+1
                    if nvar>1: ## over 1 var
                        continue
                    
                    self.OutBranchBoost(wtag,fjsysvar,jsysvar)
        ##for resolved region##
        for algo in self.pairalgos:
            for sysvar in self.jetsysvars:##resolved region itself is not affected by fatjet jec
                self.OutBranchResol(algo,sysvar)
        print "[HMlnjjVars_Dev_jhchoi8]beginFile Fin."
    def OutBranchBoost(self,wtag,fjsysvar,jsysvar):
        sysvar="nom"
        if fjsysvar!="nom":
            sysvar=fjsysvar
        if jsysvar!="nom":
            sysvar=jsysvar
        #meP'+ str(mH) + '_BstNoT_vbf_S'+_suffix
        ##Branch Naming convention 
        ###<Collection/Object>_<wtag>_<sys>_<X>  ##To use collection/object module
        ###if not collection or object
        ###<X>_<wtag>_<sys>
        ###e.g)nWtaggerFatjet_HP45_jesup_eta
        ###e.g)Whad_dM_jesTotalUp
        ###e.g)isResol_dM_jesTotalUp
        ###e.g)isBoost_HP50DDT_jmsup
        # ME
        # Mass dependent later maybe, let's go with already observed processes
        suffix=wtag+'_'+sysvar
        suffix_=suffix+"_"
        _suffix='_'+suffix
        _suffix_="_"+suffix+"_"
        self.MEbranches = []


        ##---MEKD---##
        for mass in self.mH_boost:
            #self.MEbranches.append('meP' + str(mass) + '_Bst_vbf_S')
            #self.MEbranches.append('meP' + str(mass) + '_Bst_vbf_B')
            self.MEbranches.append('meP' + str(mass) + '_Bst_ggf_S')
            self.MEbranches.append('meP' + str(mass) + '_Bst_ggf_B')
            self.MEbranches.append('meP' + str(mass) + '_Bst_ggf_B2')
        for brName in self.MEbranches:
            #print "[jhchoi]",brName+_suffix
            self.out.branch(brName+_suffix, "F")
        ##For Boosted
        ##--heavy scalar candidate--##
        self.out.branch('lnJ'+_suffix_+'pt',"F")
        self.out.branch('lnJ'+_suffix_+'mass',"F")
        self.out.branch('lnJ'+_suffix_+'minPtWOverM',"F")
        self.out.branch('lnJ'+_suffix_+'maxPtWOverM',"F")
        self.out.branch('lnJ'+_suffix_+'widx',"I")#lnJ_HP35_nom_widx
                
        ##---Bjet
        self.out.branch('BJetBoost'+_suffix_+'cjidx','I',lenVar='nBJetBoost'+_suffix)
        self.out.branch('BJetBstNotVBF'+_suffix_+'cjidx','I',lenVar='nBJetBstNotVBF'+_suffix)
        ##--Jet withi is not in wtagged fatjet
        self.out.branch('AddJetBoost'+_suffix_+"cjidx",'I',lenVar='nAddBoost'+_suffix)
        for x in ['pt','eta','phi','mass']:
            self.out.branch('AddJetBoost'+_suffix_+x,'F',lenVar='nAddBoost'+_suffix)
        
        ##--event flag
        self.out.branch('isBoostSR'+_suffix,'O')
        self.out.branch('isBoostSB'+_suffix,'O')
        self.out.branch('isVBF_Boost'+_suffix,'O')
        ##--VBF vars
        self.out.branch('VBFjjBoost_mjj'+_suffix,'F')
        self.out.branch('VBFjjBoost_dEta'+_suffix,'F')
        self.out.branch('max_mjj_Boost'+_suffix,'F')
        self.out.branch('dEta_of_max_mjj_Boost'+_suffix,'F')

        ##--VBF jets
        self.out.branch('VBFjjBoost_cjidx1'+_suffix,'I')
        self.out.branch('VBFjjBoost_cjidx2'+_suffix,'I')

    def OutBranchResol(self,algo,sysvar):
        ##Branch Naming convention
        ###<Collection/Object>_<algo>_<sys>_<X> ##To use collection/object module
        ###if not collection or object
        ###<X>_<algo>_<sys>
        suffix=algo+'_'+sysvar
        suffix_=suffix+"_"
        _suffix='_'+suffix
        _suffix_="_"+suffix+"_"

        self.MEbranches = []
        ##--MEKD
        for mass in self.mH_resol:
            #self.MEbranches.append('meP' + str(mass) + '_Res_vbf_S')
            #self.MEbranches.append('meP' + str(mass) + '_Res_vbf_B')
            self.MEbranches.append('meP' + str(mass) + '_Res_ggf_S')
            self.MEbranches.append('meP' + str(mass) + '_Res_ggf_B')
            self.MEbranches.append('meP' + str(mass) + '_Res_ggf_B2')

            
        for brName in self.MEbranches:
            #print "[jhchoi]",brName+_suffix
            self.out.branch(brName+_suffix, "F")

        ##---Resol Region kinemaics#lnjj_dM_nom_pt
        ##---Scalar candidate's momentum
        self.out.branch('lnjj'+_suffix_+'pt',"F")
        self.out.branch('lnjj'+_suffix_+'mass',"F")
        self.out.branch('lnjj'+_suffix_+'minPtWOverM',"F")
        self.out.branch('lnjj'+_suffix_+'maxPtWOverM',"F")
        self.out.branch('lnjj'+_suffix_+'Mt',"F")
        ##---Jet  not tagged as Whadronic
        self.out.branch('AddJetResol'+_suffix_+'cjidx','I',lenVar='nAddResol'+_suffix)
        for x in ['pt','eta','phi','mass']:
            self.out.branch('AddJetResol'+_suffix_+x,'F',lenVar='nAddResol'+_suffix)

        ##--event flags
        self.out.branch('isResolSR'+_suffix,"O")
        self.out.branch('isResolSB'+_suffix,"O")
        self.out.branch('isVBF_Resol'+_suffix,'O')
        ##--bjet
        self.out.branch('BJetResol'+_suffix_+'cjidx','I',lenVar='nBJetResol'+_suffix)
        self.out.branch('BJetResNotVBF'+_suffix_+'cjidx','I',lenVar='nBJetResNotVBF'+_suffix)
        
        ##--VBF vars
        self.out.branch('VBFjjResol_dEta'+_suffix,'F')
        self.out.branch('VBFjjResol_mjj'+_suffix,'F')
        self.out.branch('VBFjjResol_dEta'+_suffix,'F')
        self.out.branch('max_mjj_Resol'+_suffix,'F')
        self.out.branch('dEta_of_max_mjj_Resol'+_suffix,'F')
        ##--VBF jets
        self.out.branch('VBFjjResol_cjidx1'+_suffix,'I')
        self.out.branch('VBFjjResol_cjidx2'+_suffix,'I')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def initReaders(self,tree): # this function gets the pointers to Value and ArrayReaders and sets them in the C++ worker class
        pass


    def analyze(self, event):
        if self.debug:
          self.evtMyNum = self.evtMyNum +1

        self.PassAtLeastOne=False

	#if self.evtMyNum not in [945,947]: return True
        """process event, return True (go to next module) or False (fail, go to next event)"""
	# Wlep ############################ -> can be read from wlepbranches


        #Wlepbig=Object(event,"Wlepbig")
        lepton=Object(event,"Lepton",index=0) ##Take primary lepton

        #METbig=Object(event,self.METtype+"big")
        self._FatJet_col=Collection(event,"FatJet") ##FatJet coll to get Wtagger's momentum
        self._SubJet_col=Collection(event,"SubJet") ##Subjet to calc MEKD
        self._CleanJet_col=Collection(event,"CleanJet") ## CleanJets
        self._Jet_col=Collection(event,"Jet") ## Jet to get CleanJets' momenta



        ##read lepton / Wlep momentum from branches##
        self._lepton_4v.SetPtEtaPhiM(lepton.pt,lepton.eta,lepton.phi,0) ##Set Lepton momentum -> will be constant for an event
        
        
        ##For ME calc
        self.lepId = lepton.pdgId 
        lepId = self.lepId
        if lepId > 0: ##lep- -->+11/+13
          self.neutId = -lepId -1 ##anti nu
          self.WlepId   = -24 ##W- ->-24
          self.WhadId = +24 ##W+
        else : ##lep +
          self.neutId = -lepId + 1 ##nu
          self.WlepId   = +24 ##W+
          self.WhadId = -24 ##W-




        self.event=event
        # Boost ########################
        for wtag in self.WtaggerConfig: ##for wtaggers:
            #continue ## to test resol
            for fjsysvar in self.fjsysvars: ##for fatjet sys
                for jsysvar in self.jetsysvars: ##for jey sys
                    sysvar='nom'
                    nvar=0 ## to calculate number of varaitions for this (fjsysvar,jsysvar). ->must be 0 Or 1
                    if fjsysvar!="nom":
                        sysvar=fjsysvar
                        nvar+=1
                    if jsysvar!="nom":
                        sysvar=jsysvar
                        nvar+1
                    if nvar>1: ## number of variations must be 1.
                        continue
                    self.wtag=wtag
                    self.fjsysvar=fjsysvar
                    self.jsysvar=jsysvar
                    self.sysvar=sysvar
                    
                    self.SetLnJ() ## set objects' momentums!
                    self.CookLnJ() ## Set variables for boosted region
                    self.SetLnJME()
                    self.CookME()
                    self.FillBranchLnJ() 
                    
	# Resol #########################3
        for algo in self.pairalgos:
            #continue ##To Check Boosted
            for jsysvar in self.jetsysvars:
                self.algo=algo ## W->jj pairing algorithm name
                self.jsysvar=jsysvar
                self.SetLnjj()
                self.CookLnjj()
                self.SetLnjjME()
                self.CookME()
                self.FillBranchLnjj()
   	########################
	# Event Save Decision
	########################

        if self.doSkim and not self.PassAtLeastOne : return False

        if event.event % 10000 ==1 :##To flush memory of ttree
            #self.out._tree.AutoSave("FlushBaskets")
            print "[jhchoi]FlushBaskets event#=",event.event
            self.out._tree.AutoSave("FlushBaskets")


        return True
    def SetLnJ(self):

        ##Read Wtagger momentum with given wtag / fjsysvar / jsysvar
        WtaggerName="WtaggerFatjet_"+self.wtag+"_"+self.fjsysvar
        self.Wtag_coll=Collection(self.event,WtaggerName)
        self.Wlep=Object(self.event,"Wlep_"+self.jsysvar) ##Take Wlep object defined @ WlepMaker
        self.MET=Object(self.event,self.METtype+"_"+self.jsysvar) ##MET
        ##initialize momenta and flags
        self.initLnJ() 
        N=len(self.Wtag_coll)
        if N == 0: ##no wtagged fatjet
            return ## then, do not care the event
        if N == 1: ##only one wtagged fj
            self._WhadBoost_widx=0 ##take 1st one
        elif N >1 : ##Take one close to W mass to increase signal eff.
            dM=MaxLimit
            for ij, whad in enumerate(self.Wtag_coll):
                this_dM = abs(Wmass - whad.mass)
                if this_dM < dM:
                    #print "!!tag"
                    self._WhadBoost_widx=ij
        ##---now self._WhadBoost_widx is selected
        #print "[SetLnJ]self._WhadBoost_widx=",self._WhadBoost_widx

        self._MET_4v.SetPxPyPzE(self.MET.px,self.MET.py,self.MET.pz,self.MET.E) ##MET as well
        #self._MET_big4v.SetPtEtaPhiM(MET.px,MET.py,METbig.pz,METbig,.E)
	self._Wlep_4v.SetPtEtaPhiM(self.Wlep.pt,self.Wlep.eta,self.Wlep.phi,self.Wlep.mass) 
	#self._Wlep_big4v.SetPxPyPzE(Wlepbig.px,Wlepbig.py,Wlepbig.pz,Wlepbig.E)
	self._Wlep_Mt = self.Wlep.Mt
        self._WhadBoost_4v.SetPtEtaPhiM(self.Wtag_coll[self._WhadBoost_widx].pt, self.Wtag_coll[self._WhadBoost_widx].eta, self.Wtag_coll[self._WhadBoost_widx].phi, self.Wtag_coll[self._WhadBoost_widx].mass)
        self._lnJ_4v = self._Wlep_4v + self._WhadBoost_4v
        self._doCook=True
        self.PassAtLeastOne=True
                


    def initLnJ(self):
        #inactivates all falgs
        ##--For calc
        self._WhadBoost_widx=-1 
        self._doME = False
        self._doCook = False
        self._WhadBoost_4v.SetPtEtaPhiM(0,0,0,0)
        self._lnJ_4v.SetPtEtaPhiM(0,0,0,0)

        ##--common variables for CookME
        self._MassME=self.mH_boost
        self._isVBF_ME=False
        
        ##--variables to be stored in branches

        self._isBoostSR=False
        self._isBoostSB=False
        self._lnJ = {}
        self._lnJ['pt']=-1
        self._lnJ['mass']=-1
        self._lnJ['minPtWOverM']=-1
        self._lnJ['maxPtWOverM']=-1
        self._BJetBoost={}
        self._BJetBstNotVBF={}
        self._BJetBoost['cjidx']=[]
        self._BJetBstNotVBF['cjidx']=[]
        self._AddJetBoost={}
        for x in ['pt','eta','phi','mass','cjidx']:
            self._AddJetBoost[x]=[]

        self._isVBF_Boost=False
        self._VBFjjBoost_mjj=-1
        self._VBFjjBoost_dEta=-1
        self._max_mjj_Boost=-1
        self._dEta_of_max_mjj_Boost = -1
        self._VBFjjBoost_cjidx1 = -1
        self._VBFjjBoost_cjidx2 = -1



    def CookLnJ(self):
        if not self._doCook:return
        ## categrize Regions by Wfat mass##
        WfatMass = self._WhadBoost_4v.M()
        self._lnJ['pt']=self._lnJ_4v.Pt()
        self._lnJ['mass']=self._lnJ_4v.M()

        Wfat_pt=self._WhadBoost_4v.Pt()
        Wlep_pt=self._Wlep_4v.Pt()
        self._lnJ['minPtWOverM'] = min(Wfat_pt,Wlep_pt)/self._lnJ['mass']
        self._lnJ['maxPtWOverM'] = max(Wfat_pt,Wlep_pt)/self._lnJ['mass']

        if (WfatMass < self.Wmass_SRhigh and WfatMass > self.Wmass_SRlow):
            self._isBoostSR = True
            self._doME=True
           
            
        else: #The SB mass cut is already applied @ WtaggerProducer 
            self._isBoostSB = True
            self._doME=True
        

        ## VBF
        self.VBF_Boost()
        self.GetBJetsBoost()
    

    def VBF_Boost(self):
        if not self._doCook:return
        wphi=self._WhadBoost_4v.Phi()
        weta=self._WhadBoost_4v.Eta()
        N=len(self._CleanJet_col)
        if N < 2: return
        for i_cj in range(0,N):
            pt1,eta1,phi1,mass1 = self.CleanJet_PtEtaPhiM(i_cj)
            if pt1 < self.cut_VBFjet_pt: continue
            if abs(eta1) > self.cut_VBFjet_eta : continue
            if abs(eta1) > self.cut_jet_horn_etamin and abs(eta1) < self.cut_jet_horn_etammax: ##if in jet horn region
                if pt1 < self.cut_jet_horn_ptmin: continue
            if self.getDeltaR(wphi,weta,phi1,eta1) < 0.8 : continue ##jet cleaning
            for j_cj in range(0,N):
                if j_cj <= i_cj : continue
                pt2,eta2,phi2,mass2 = self.CleanJet_PtEtaPhiM(j_cj)
                if pt2 < self.cut_VBFjet_pt: continue
                if abs(eta2) > self.cut_VBFjet_eta : continue
                if abs(eta2) > self.cut_jet_horn_etamin and abs(eta2) < self.cut_jet_horn_etammax: ##if in jet horn region
                    if pt2 < self.cut_jet_horn_ptmin: continue
                if self.getDeltaR(wphi,weta,phi2,eta2)< 0.8 : continue ##jet cleaning
                this_dEta=abs(eta1-eta2)
                this_mjj = self.InvMassCalc(pt1,eta1,phi1,mass1,pt2,eta2,phi2,mass2)
                if (this_dEta > self.cut_VBF_dEta) and (this_mjj > self._VBFjjBoost_mjj) :
                    self._VBFjjBoost_dEta = this_dEta
                    self._VBFjjBoost_mjj = this_mjj
                    self._VBFjjBoost_cjidx1 = i_cj
                    self._VBFjjBoost_cjidx2 = j_cj
                    
                if this_mjj > self._max_mjj_Boost:
                    self._max_mjj_Boost = this_mjj
                    self._dEta_of_max_mjj_Boost = this_dEta
                    self._max_mjjBoost_cjidx1 = i_cj
                    self._max_mjjBoost_cjidx2 = j_cj

        if self._VBFjjBoost_mjj > self.cut_VBF_mjj : 
            self._isVBF_Boost = True
            
    def SetLnjj(self):

        self.initLnjj()
        _suffix="_"+self.algo+"_"+self.jsysvar
        exec("self._isResol=self.event.isResol"+_suffix)##read isresol
        if self._isResol:
            WjjtaggerName="Whad"+_suffix
            self.Wjjtag=Object(self.event,WjjtaggerName)
            self._WhadResol_4v.SetPtEtaPhiM(self.Wjjtag.pt,self.Wjjtag.eta,self.Wjjtag.phi,self.Wjjtag.mass)
            self._Whad_cjidx1 = self.Wjjtag.cjidx1
            self._Whad_cjidx2 = self.Wjjtag.cjidx2
            
            self.Wlep=Object(self.event,"Wlep_"+self.jsysvar) ##Take Wlep object defined @ WlepMaker
            self.MET=Object(self.event,self.METtype+"_"+self.jsysvar) ##MET
            self._MET_4v.SetPxPyPzE(self.MET.px,self.MET.py,self.MET.pz,self.MET.E) ##MET as well
            #self._MET_big4v.SetPtEtaPhiM(MET.px,MET.py,METbig.pz,METbig.E)
            self._Wlep_4v.SetPtEtaPhiM(self.Wlep.pt,self.Wlep.eta,self.Wlep.phi,self.Wlep.mass)
            #self._Wlep_big4v.SetPxPyPzE(Wlepbig.px,Wlepbig.py,Wlepbig.pz,Wlepbig.E)
            self._Wlep_Mt = self.Wlep.Mt


            self._doME=True
            self._doCook=True
            self.PassAtLeastOne=True

    def initLnjj(self):
        ##--For calc
        self._doME = False
        self._doCook = False
        self._WhadResol_4v.SetPtEtaPhiM(0,0,0,0)
        self._lnjj_4v.SetPtEtaPhiM(0,0,0,0)
        #self._WhadResol_j1_4v.SetPtEtaPhiM(0,0,0,0)
        #self._WhadResol_j2_4v.SetPtEtaPhiM(0,0,0,0)
        self._MassME=self.mH_resol
        self._isVBF_ME=False

        ##--x to fillbranch                                                                                                                                                       
        self._isResolSR=False
        self._isResolSB=False
        self._lnjj = {}
        self._lnjj['pt']=-1
        self._lnjj['mass']=-1
        self._lnjj['Mt']=-1
        self._lnjj['minPtWOverM']=-1
        self._lnjj['maxPtWOverM']=-1
        self._BJetResol={}
        self._BJetResNotVBF={}
        self._BJetResol['cjidx']=[]
        self._BJetResNotVBF['cjidx']=[]

        self._AddJetResol={}
        for x in ['pt','eta','phi','mass','cjidx']:
            self._AddJetResol[x]=[]

        self._isVBF_Resol=False
        self._VBFjjResol_mjj=-1
        self._VBFjjResol_dEta=-1
        self._max_mjj_Resol=-1
        self._dEta_of_max_mjj_Resol=-1
        self._VBFjjResol_cjidx1 = -1
        self._VBFjjResol_cjidx2 = -1




    def initP(self):
        self.P_vbf_S={}
        self.P_vbf_B={}
        self.P_ggf_S={}
        self.P_ggf_B={}
        self.P_ggf_B2={}
        
        for mH in self._MassME:
            self.P_vbf_S[mH] = -1
            self.P_vbf_B[mH] = -1
            self.P_ggf_S[mH] = -1
            self.P_ggf_B[mH] = -1
            self.P_ggf_B2[mH] = -1
            
    def SetLnJME(self):
        if self._doME:
            ###For CookME##
            #print "[SetLnJME]self._WhadBoost_widx=",self._WhadBoost_widx
            subJetI1=self._FatJet_col[self.Wtag_coll[self._WhadBoost_widx].fjetIdx].subJetIdx1
            subJetI2=self._FatJet_col[self.Wtag_coll[self._WhadBoost_widx].fjetIdx].subJetIdx2
            pt,eta,phi,mass=self.SubJet_PtEtaPhiM(subJetI1)
            self._Whad_j1_4v.SetPtEtaPhiM(pt,eta,phi,mass)##Whad daughter 1 in ME 
            pt,eta,phi,mass=self.SubJet_PtEtaPhiM(subJetI2)
            self._Whad_j2_4v.SetPtEtaPhiM(pt,eta,phi,mass)##whad daughter 1 in ME
            self._Whad_4v = self._WhadBoost_4v ##Whad momentum
            if self._VBFjjBoost_cjidx1> 0 and self._VBFjjBoost_cjidx2: ##To set up associated jets
                pt,eta,phi,mass=self.CleanJet_PtEtaPhiM(self._max_mjjBoost_cjidx1)
                self._vbfj1_4v.SetPtEtaPhiM(pt,eta,phi,mass)
                pt,eta,phi,mass=self.CleanJet_PtEtaPhiM(self._max_mjjBoost_cjidx2)
                self._vbfj2_4v.SetPtEtaPhiM(pt,eta,phi,mass)
                self._isVBF_ME = True

    def SetLnjjME(self):
        if self._doME:
            ###For CookME###self._Whad_cjidx1/self._Whad_cjidx2 ##CleanJet_PtEtaPhiM
            pt,eta,phi,mass=self.CleanJet_PtEtaPhiM(self._Whad_cjidx1)
            self._Whad_j1_4v.SetPtEtaPhiM(pt,eta,phi,mass)
            pt,eta,phi,mass=self.CleanJet_PtEtaPhiM(self._Whad_cjidx2)
            self._Whad_j2_4v.SetPtEtaPhiM(pt,eta,phi,mass)
            self._Whad_4v = self._WhadResol_4v
            if self._VBFjjResol_cjidx1>0 and self._VBFjjResol_cjidx2>0:
                pt,eta,phi,mass=self.CleanJet_PtEtaPhiM(self._max_mjjResol_cjidx1)
                self._vbfj1_4v.SetPtEtaPhiM(pt,eta,phi,mass)
                pt,eta,phi,mass=self.CleanJet_PtEtaPhiM(self._max_mjjResol_cjidx2)
                self._vbfj2_4v.SetPtEtaPhiM(pt,eta,phi,mass)

                self._isVBF_ME = True

    def CookME(self):
        self.initP() ##initialize all probabilities
        if self._doME: 
            # particle ids
            ##set daughters
            hDa_ids = ROOT.vector('int')()
            hDa_4Vs = ROOT.vector('TLorentzVector')()

            hDa_ids.push_back(int(self.WlepId)) 
            hDa_4Vs.push_back(self._Wlep_4v)
            hDa_ids.push_back(int(self.WhadId)) 
            hDa_4Vs.push_back(self._Whad_4v)
            WWda_ids = ROOT.vector('int')()
            WWda_4Vs = ROOT.vector('TLorentzVector')()

            WWda_ids.push_back(int(self.lepId))
            WWda_4Vs.push_back(self._lepton_4v)
            
            WWda_ids.push_back(int(self.neutId))
            WWda_4Vs.push_back(self._MET_4v)

            WWda_ids.push_back(int(0))
            WWda_4Vs.push_back(self._Whad_j1_4v)

            WWda_ids.push_back(int(0))
            WWda_4Vs.push_back(self._Whad_j2_4v)

            NoVBF_associate_ids = ROOT.vector('int')()
            NoVBF_associate_4Vs = ROOT.vector('TLorentzVector')()
            
            for mH in self._MassME:
                gsm = self.g.GetBinContent(self.g.FindBin(mH))
                self.mela.setMelaHiggsMassWidth(mH, gsm)
                # variable initialization

                if self.debug:
                    print "Probability for mass",mH
                if self.debug:
                    print "check ggf prob."


                '''
                naddjet=len(self._AddJetBoost['pt'])
                tmp_4V = ROOT.TLorentzVector()
                for i in range(naddjet):
                    pt=self._AddJetBoost['pt'][i]
                    eta=self._AddJetBoost['eta'][i]
                    phi=self._AddJetBoost['phi'][i]
                    mass=self._AddJetBoost['mass'][i]
                    if pt < self.cut_jet_pt: continue
                    if abs(eta) > self.cut_jet_eta : continue
                    tmp_4V.SetPtEtaPhiM(pt, eta, phi, mass)
                    #print 'pt, eta, phi, mass=',pt, eta, phi, mass
                    NoVBF_associate_ids.push_back( int(0) )
                    NoVBF_associate_4Vs.push_back( tmp_4V )
                '''
                
                self.mela.setCandidateDecayMode(ROOT.TVar.CandidateDecay_WW)
                self.mela.setupDaughtersNoMom(
                    False,
                    WWda_ids, WWda_4Vs,
                    NoVBF_associate_ids, NoVBF_associate_4Vs,
                    False )
                self.mela.setCurrentCandidateFromIndex(int(0))
                # TVar.CandidateDecay_Stable case: h->WW, ProdP : just 0 
                # TVar.CandidateDecay_Stable case: h->WW, DecP :  not supported
                # TVar.CandidateDecay_WW     case: h->WW, DecP :  not supported
                # TVar.CandidateDecay_WW     case: h->WW, ProdP : not supported -> same value for sig,bkg 
                #mePgg = self.mela.computeProdP(ROOT.TVar.HSMHiggs, ROOT.TVar.JHUGen, True)
                self.P_ggf_S[mH] = self.mela.computeDecP(ROOT.TVar.HSMHiggs, ROOT.TVar.MCFM, False)
                self.P_ggf_B[mH] = self.mela.computeDecP(ROOT.TVar.bkgWW,    ROOT.TVar.MCFM, True)
                self.P_ggf_B2[mH] = self.mela.computeDecP2(ROOT.TVar.bkgWW,    ROOT.TVar.MCFM, True)


                if self.debug:
                    print "NoVBF prob ==========================================="
                    print self.evtMyNum
                    #print "P_vbf_S",self.P_vbf_S[mH],"P_vbf_B",self.P_vbf_B[mH],"P_ggf_S",self.P_ggf_S[mH],"P_ggf_B",self.P_ggf_B[mH]
                
                                    
                if self._isVBF_ME:
                    pass ##Do not run vbfcase
                    #print "[jhchoi]VBFME"
                    ##void setIsVbfProd(bool IsVbf){_isVBF = IsVbf; return;}
                    NoVBF_associate_ids.push_back( int(0) )
                    NoVBF_associate_4Vs.push_back( self._vbfj1_4v )
                    NoVBF_associate_ids.push_back( int(0) )
                    NoVBF_associate_4Vs.push_back( self._vbfj2_4v )
                    if self.debug:
                        print "check VBF prob."
                    

                    self.mela.setCandidateDecayMode(ROOT.TVar.CandidateDecay_Stable)
                    #self.mela.setCandidateDecayMode(ROOT.TVar.CandidateDecay_WW)
                    self.mela.setupDaughtersNoMom(
                        True, ##isVBF
                        hDa_ids, hDa_4Vs,
                        #WWda_ids, WWda_4Vs,
                        NoVBF_associate_ids, NoVBF_associate_4Vs,
                        False )##isGenLevel
                    self.mela.setCurrentCandidateFromIndex(int(0))
                    self.P_vbf_S[mH] = self.mela.computeProdP(ROOT.TVar.HSMHiggs, ROOT.TVar.JHUGen, False)
                    self.P_vbf_B[mH] = self.mela.computeProdP(ROOT.TVar.bkgWW,    ROOT.TVar.JHUGen, True)
                    #if self._P_vbf_B[mH]!=0.:
                    #    print "[jhchoi]vbf sig/bkg=",self._P_vbf_S[mH] /self._P_vbf_B[mH]
                    #self._P_vbf_S[mH] = self.mela.computeDecP(ROOT.TVar.HSMHiggs, ROOT.TVar.MCFM, False)
                    #self._P_vbf_B[mH] = self.mela.computeDecP(ROOT.TVar.bkgWW,    ROOT.TVar.MCFM, True)

                    #self._P_vbf_S[mH] = self.mela.computeProdP(ROOT.TVar.HSMHiggs, ROOT.TVar.MCFM, False)
                    #self._P_vbf_B[mH] = self.mela.computeProdP(ROOT.TVar.bkgWW,    ROOT.TVar.MCFM, True)
                
            
    def FillBranchLnJ(self):
        #print "[FillBranchLnJ]self._WhadBoost_widx=",self._WhadBoost_widx
        suffix=self.wtag+"_"+self.sysvar
        _suffix="_"+suffix
        _suffix_="_"+suffix+"_"
        '''
        self._isBoostSR=False
        self._isBoostSB=False
        self._lnJ = {}
        self._lnJ['pt']=-1
        self._lnJ['mass']=-1
        self._lnJ['minPtWOverM']=-1
        self._lnJ['maxPtWOverM']=-1
        self._BJetBoost['cjidx']=[]
        self._BJetBstNotVBF['cjidx']=[]
        self._isVBF_Boost=False
        self._VBFjjBoost_mjj=-1
        self._VBFjjBoost_dEta=-1
        self._max_mjj_Boost=-1
        self._VBFjjBoost_cjidx1 = -1
        self._VBFjjBoost_cjidx2 = -1

        '''
        '''
        self.out.branch('lnJ'+_suffix_+'pt',"F")
        self.out.branch('lnJ'+_suffix_+'mass',"F")
        self.out.branch('lnJ'+_suffix_+'minPtWOverM',"F")
        self.out.branch('lnJ'+_suffix_+'maxPtWOverM',"F")


        self.out.branch('BJetBoost'+_suffix_+'cjidx','I',lenVar='nBJetBoost'+_suffix)
        self.out.branch('BJetBstNotVBF'+_suffix_+'cjidx','I',lenVar='nBJetBstNotVBF'+_suffix)

        self.out.branch('isVBF_Boost'+_suffix,'O')
        self.out.branch('VBFjjBoost_mjj'+_suffix,'F')
        self.out.branch('VBFjjBoost_dEta'+_suffix,'F')
        self.out.branch('max_mjj_Boost'+_suffix,'F')

        '''
        
        self.out.fillBranch('lnJ'+_suffix_+'pt',self._lnJ['pt'])
        self.out.fillBranch('lnJ'+_suffix_+'mass',self._lnJ['mass'])
        self.out.fillBranch('lnJ'+_suffix_+'minPtWOverM',self._lnJ['minPtWOverM'])
        self.out.fillBranch('lnJ'+_suffix_+'maxPtWOverM',self._lnJ['maxPtWOverM'])
        self.out.fillBranch('lnJ'+_suffix_+'widx',self._WhadBoost_widx)#lnJ_HP35_nom_widx
        
        self.out.fillBranch('BJetBoost'+_suffix_+'cjidx',self._BJetBoost['cjidx'])
        self.out.fillBranch('BJetBstNotVBF'+_suffix_+'cjidx',self._BJetBstNotVBF['cjidx'])
        for x in self._AddJetBoost:
            self.out.fillBranch("AddJetBoost"+_suffix_+x,self._AddJetBoost[x])

        self.out.fillBranch('isBoostSR'+_suffix, self._isBoostSR)
        self.out.fillBranch('isBoostSB'+_suffix, self._isBoostSB)

        self.out.fillBranch('isVBF_Boost'+_suffix, self._isVBF_Boost)
        self.out.fillBranch('VBFjjBoost_mjj'+_suffix, self._VBFjjBoost_mjj)
        self.out.fillBranch('VBFjjBoost_dEta'+_suffix, self._VBFjjBoost_dEta)
        self.out.fillBranch('max_mjj_Boost'+_suffix, self._max_mjj_Boost)
        self.out.fillBranch('dEta_of_max_mjj_Boost'+_suffix, self._dEta_of_max_mjj_Boost)#_dEta_of_max_mjj_Resol

        self.out.fillBranch('VBFjjBoost_cjidx1'+_suffix, self._VBFjjBoost_cjidx1)
        self.out.fillBranch('VBFjjBoost_cjidx2'+_suffix, self._VBFjjBoost_cjidx2)
        
        

        for mH in self._MassME:
            #self.out.fillBranch('meP'+ str(mH) + '_Bst_vbf_S'+_suffix,   self.P_vbf_S[mH])
            #self.out.fillBranch('meP'+ str(mH) + '_Bst_vbf_B'+_suffix,   self.P_vbf_B[mH])
            self.out.fillBranch('meP'+ str(mH) + '_Bst_ggf_S'+_suffix,   self.P_ggf_S[mH])
            self.out.fillBranch('meP'+ str(mH) + '_Bst_ggf_B'+_suffix,   self.P_ggf_B[mH])
            self.out.fillBranch('meP'+ str(mH) + '_Bst_ggf_B2'+_suffix,   self.P_ggf_B2[mH])
        
        
    def FillBranchLnjj(self):
        suffix=self.algo+'_'+self.jsysvar
        _suffix="_"+suffix
        _suffix_="_"+suffix+"_"

        '''
        self._isResolSR=False
        self._isResolSB=False
        self._lnjj = {}
        self._lnjj['pt']=-1
        self._lnjj['mass']=-1
        self._lnjj['Mt']=-1
        self._lnjj['minPtWOverM']=-1
        self._lnjj['maxPtWOverM']=-1
        self._BJetResol={}
        self._BJetResNotVBF={}
        self._BJetResol['cjidx']=[]
        self._BJetResNotVBF['cjidx']=[]

        self._AddJetResol={}
        for x in ['pt','eta','phi','mass','cjidx']:
            self._AddJetResol[x]=[]

        self._isVBF_Resol=False
        self._VBFjjResol_mjj=-1
        self._VBFjjResol_dEta=-1
        self._max_mjj_Resol=-1
        self._VBFjjResol_cjidx1 = -1
        self._VBFjjResol_cjidx2 = -1

        '''
        '''
        for mass in self.mH_resol:
            self.MEbranches.append('meP' + str(mass) + '_ResVBF_vbf_S')
            self.MEbranches.append('meP' + str(mass) + '_ResVBF_vbf_B')
            self.MEbranches.append('meP' + str(mass) + '_ResVBF_ggf_S')
            self.MEbranches.append('meP' + str(mass) + '_ResVBF_ggf_B')

            self.MEbranches.append('meP' + str(mass) + '_ResNoT_vbf_S')
            self.MEbranches.append('meP' + str(mass) + '_ResNoT_vbf_B')
            self.MEbranches.append('meP' + str(mass) + '_ResNoT_ggf_S')
            self.MEbranches.append('meP' + str(mass) + '_ResNoT_ggf_B')

        for brName in self.MEbranches:
            #print "[jhchoi]",brName+_suffix                                                                                                                                      
            self.out.branch(brName+_suffix, "F")

        ##---Resol Region kinemaics                                                                                                                                               
        self.out.branch('lnjj'+_suffix_+'pt',"F")
        self.out.branch('lnjj'+_suffix_+'mass',"F")
        self.out.branch('lnjj'+_suffix_+'minPtWOverM',"F")
        self.out.branch('lnjj'+_suffix_+'maxPtWOverM',"F")
        self.out.branch('lnjj'+_suffix_+'Mt',"F")

        self.out.branch('isResolSR'+_suffix,"O")
        self.out.branch('BJetResol'+_suffix_+'cjidx','I',lenVar='nBJetResol'+_suffix)
        self.out.branch('BJetResNotVBF'+_suffix_+'cjidx','I',lenVar='nBJetResNotVBF'+_suffix)
        self.out.branch('isVBF_Resol'+_suffix,'O')
        self.out.branch('VBFjjResol_dEta'+_suffix,'F')
        self.out.branch('VBFjjResol_mjj'+_suffix,'F')
        self.out.branch('VBFjjResol_dEta'+_suffix,'F')
        self.out.branch('max_mjj_Resol'+_suffix,'F')

        '''
        self.out.fillBranch('lnjj'+_suffix_+'pt',self._lnjj['pt'])
        self.out.fillBranch('lnjj'+_suffix_+'mass',self._lnjj['mass'])
        self.out.fillBranch('lnjj'+_suffix_+'Mt',self._lnjj['Mt'])
        self.out.fillBranch('lnjj'+_suffix_+'minPtWOverM',self._lnjj['minPtWOverM'])
        self.out.fillBranch('lnjj'+_suffix_+'maxPtWOverM',self._lnjj['maxPtWOverM'])

        self.out.fillBranch('BJetResol'+_suffix_+'cjidx',self._BJetResol['cjidx'])
        self.out.fillBranch('BJetResNotVBF'+_suffix_+'cjidx',self._BJetResNotVBF['cjidx'])
        for x in self._AddJetResol:
            self.out.fillBranch("AddJetResol"+_suffix_+x,self._AddJetResol[x])

        self.out.fillBranch('isResolSR'+_suffix, self._isResolSR)
        self.out.fillBranch('isResolSB'+_suffix, self._isResolSB)

        self.out.fillBranch('isVBF_Resol'+_suffix, self._isVBF_Resol)
        self.out.fillBranch('VBFjjResol_mjj'+_suffix, self._VBFjjResol_mjj)
        self.out.fillBranch('VBFjjResol_dEta'+_suffix, self._VBFjjResol_dEta)
        self.out.fillBranch('max_mjj_Resol'+_suffix, self._max_mjj_Resol)
        self.out.fillBranch('dEta_of_max_mjj_Resol'+_suffix, self._dEta_of_max_mjj_Resol)

        self.out.fillBranch('VBFjjResol_cjidx1'+_suffix, self._VBFjjResol_cjidx1)
        self.out.fillBranch('VBFjjResol_cjidx2'+_suffix, self._VBFjjResol_cjidx2)

        for mH in self._MassME:
            #self.out.fillBranch('meP'+ str(mH) + '_Res_vbf_S'+_suffix,   self.P_vbf_S[mH])
            #self.out.fillBranch('meP'+ str(mH) + '_Res_vbf_B'+_suffix,   self.P_vbf_B[mH])
            self.out.fillBranch('meP'+ str(mH) + '_Res_ggf_S'+_suffix,   self.P_ggf_S[mH])
            self.out.fillBranch('meP'+ str(mH) + '_Res_ggf_B'+_suffix,   self.P_ggf_B[mH])
            self.out.fillBranch('meP'+ str(mH) + '_Res_ggf_B2'+_suffix,   self.P_ggf_B2[mH])


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
    def GetBJetsBoost(self):
        bWP=self.bWP
        N=len(self._CleanJet_col)
        if N < 2: return
        wphi=self._WhadBoost_4v.Phi()
        weta=self._WhadBoost_4v.Eta()
        for i_cj in range(0,N): #
            pt,eta,phi,mass=self.CleanJet_PtEtaPhiM(i_cj)
            jet_idx=self._CleanJet_col[i_cj].jetIdx
            bAlgo=self._Jet_col[jet_idx].btagDeepB

            if pt < self.cut_bjet_pt :continue
            if abs(eta) > self.cut_bjet_eta:continue
            if self.getDeltaR(wphi,weta,phi,eta) < 0.8 : continue ##jet cleaning
            self._AddJetBoost['cjidx'].append(i_cj)
            self._AddJetBoost['pt'].append(pt)
            self._AddJetBoost['eta'].append(eta)
            self._AddJetBoost['phi'].append(phi)
            self._AddJetBoost['mass'].append(mass)
            if bAlgo < bWP:continue
            self._BJetBoost['cjidx'].append(i_cj) ## fill index of CleanJet 
	    if self._isVBF_Boost:
	      if i_cj != self._VBFjjBoost_cjidx1:
                  self._BJetBstNotVBF['cjidx'].append(i_cj)
              elif i_cj != self._VBFjjBoost_cjidx2:
                  self._BJetBstNotVBF['cjidx'].append(i_cj)

    def GetBJetsResol(self):
        ##->Set self._BJetResol_cjidx
        #self._CleanJet_col
        bWP=self.bWP
        N=self._CleanJet_col._len
        for i_cj in range(0,N):
            if i_cj == self._Whad_cjidx1 : continue
            if i_cj == self._Whad_cjidx2 : continue
            pt,eta,phi,mass=self.CleanJet_PtEtaPhiM(i_cj)
            j_idx= self._CleanJet_col[i_cj].jetIdx ##Jet Object index
            bAlgo= self._Jet_col[j_idx].btagDeepB

            if pt < self.cut_bjet_pt  :continue
            if abs(eta) > self.cut_bjet_eta:continue
            self._AddJetResol['cjidx'].append(i_cj)
            self._AddJetResol['pt'].append(pt)
            self._AddJetResol['eta'].append(eta)
            self._AddJetResol['phi'].append(phi)
            self._AddJetResol['mass'].append(mass)
            if bAlgo < bWP:continue
            self._BJetResol['cjidx'].append(i_cj) ## fill index of CleanJet
	    if self._isVBF_Resol:
	      if i_cj != self._VBFjjResol_cjidx1 : 
                  self._BJetResNotVBF['cjidx'].append(i_cj)
              elif i_cj != self._VBFjjResol_cjidx2 : 
                  self._BJetResNotVBF['cjidx'].append(i_cj)

            


    def VBF_Resol(self):
        if not self._isResol: return
        N=self._CleanJet_col._len
        if N < 4 : return

        for i_cj in range(0,N):
	    if i_cj == self._Whad_cjidx1 : continue
            if i_cj == self._Whad_cjidx2 : continue

            pt1,eta1,phi1,mass1 = self.CleanJet_PtEtaPhiM(i_cj)
            if pt1 < self.cut_VBFjet_pt : continue
            if abs(eta1) > self.cut_VBFjet_eta : continue

            for j_cj in range(0,N):
                if j_cj <= i_cj : continue ##doubly checked or the same one
	        if j_cj == self._Whad_cjidx1 : continue
                if j_cj == self._Whad_cjidx2 : continue

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
                    self._dEta_of_max_mjj_Resol = this_dEta
                    self._max_mjjResol_cjidx1 = i_cj
                    self._max_mjjResol_cjidx2 = j_cj
        ##--End of jet pair loop
        if self._VBFjjResol_mjj > self.cut_VBF_mjj : self._isVBF_Resol = True
 
    def CookLnjj(self):
        if not self._isResol : return
        self._lnjj_4v    = self._Wlep_4v    + self._WhadResol_4v
        self._lnjj_pt   = self._lnjj_4v.Pt()
        self._lnjj_mass = self._lnjj_4v.M()
        self._lnjj['pt']=self._lnjj_4v.Pt()
        self._lnjj['mass']=self._lnjj_4v.M()

        wleppt=self._Wlep_4v.Pt()
        whadpt=self._WhadResol_4v.Pt()
        self._minPtWOverMlnjj = min(wleppt, whadpt)/self._lnjj_mass
        self._maxPtWOverMlnjj = max(wleppt, whadpt)/self._lnjj_mass
        self._lnjj['minPtWOverM'] = min(wleppt, whadpt)/self._lnjj_mass
        self._lnjj['maxPtWOverM'] = max(wleppt, whadpt)/self._lnjj_mass

        Ljj_4v = self._lepton_4v + self._WhadResol_4v
	Ljj_pt = Ljj_4v.Pt()
        self._lnjj['Mt'] = math.sqrt(2.* Ljj_pt*self._MET_4v.Pt() * (1. - math.cos( Ljj_4v.DeltaPhi(self._MET_4v)) ))




        Whad_mass     = self._WhadResol_4v.M()

        if Whad_mass > self.Wmass_SRlow and Whad_mass < self.Wmass_SRhigh:
            self._isResolSR = True
        else:
            self._isResolSB = True
        ## VBF                                                                                                                                                                    
        self.VBF_Resol()
        self.GetBJetsResol()


    def CleanJet_PtEtaPhiM(self,cjidx):
        #self.jsysvar
        jidx=self._CleanJet_col[cjidx].jetIdx

        mass=self._Jet_col[jidx].mass
        exec("pt=self._Jet_col[jidx].pt_"+self.jsysvar) ##pt variation by jes/jer
        eta=self._CleanJet_col[cjidx].eta
        phi=self._CleanJet_col[cjidx].phi
        

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

    def SubJet_PtEtaPhiM(self,jidx):
        pt  = self._SubJet_col[jidx].pt
        eta = self._SubJet_col[jidx].eta
        phi = self._SubJet_col[jidx].phi
        mass= self._SubJet_col[jidx].mass
        return pt,eta,phi,mass

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

