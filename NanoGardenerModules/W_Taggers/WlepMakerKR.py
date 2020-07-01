import ROOT
import math
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

Wmass=80.4
class WlepMakerKR(Module):
    def __init__(self,METtype='PuppiMET',jsysvars='all',year=2017,jsyssources="all"):
        print "==init WlepMakerKR=="
        self.METtype = METtype

        ##declare
        self._MET_4v        = ROOT.TLorentzVector()
        self._MET_big4v     = ROOT.TLorentzVector()
        self._lepton_4v     = ROOT.TLorentzVector()
        self._Wlep_4v       = ROOT.TLorentzVector()
        self._Wlep_big4v    = ROOT.TLorentzVector()
        self.jsysvars=jsysvars
        #jsources=[]
        ##--ak4jet uncertainty sources
        if jsyssources=="all":
            jsources=['jesFlavorQCD','jesRelativeBal','jesHF','jesBBEC1','jesEC2','jesAbsolute','jesAbsolute_'+str(year),'jesHF_'+str(year),'jesEC2_'+str(year),'jesRelativeSample_'+str(year),'jesBBEC1_'+str(year),'jesTotal','jer']
        if jsyssources=="correlate":
            jsources=['jesFlavorQCD','jesRelativeBal','jesHF','jesBBEC1','jesEC2','jesAbsolute','jesTotal']
        if jsyssources=="uncorrelate":
            jsources=['jesAbsolute_'+str(year),'jesHF_'+str(year),'jesEC2_'+str(year),'jesRelativeSample_'+str(year),'jesBBEC1_'+str(year),'jer']




        if jsysvars=='all' or jsysvars=="up" or jsysvars=="down":
            directions=[]
            if jsysvars=='all':directions=['Up','Down']
            if jsysvars=="up":directions=["Up"]
            if jsysvars=="down":directions=["Down"]
            print "[WlepMakerKR]Run all regrouped set of sys"
            self.jsysvars=['nom']
            for s in jsources:
                for d in directions:
                    self.jsysvars.append(s+d)
            print "[directions]=",directions
            print "[jsources]",jsources

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        for jsysvar in self.jsysvars:
            suffix=jsysvar
            _suffix="_"+suffix
            _suffix_="_"+suffix+"_"
            for var in ['pt','eta','phi','mass','Mt','E','bigmass','bigE']:
                self.out.branch("Wlep"+_suffix_+var  , "F")
            for var in ['E','pz','mass']:
                self.out.branch("Wlepbig"+_suffix_+var,"F")
            self.out.branch(self.METtype+_suffix_+'pz1', "F")
            self.out.branch(self.METtype+_suffix_+'pz2', "F")
            self.out.branch(self.METtype+_suffix_+'px', "F")
            self.out.branch(self.METtype+_suffix_+'py', "F")
            self.out.branch(self.METtype+_suffix_+'pt', "F")
            self.out.branch(self.METtype+_suffix_+'E', "F")
            self.out.branch(self.METtype+_suffix_+'pz', "F")
            self.out.branch(self.METtype+_suffix_+'big_E', "F")
            self.out.branch(self.METtype+_suffix_+'big_pz', "F")
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def Get_MET_pt_phi(self): ##propagate jet momentum sysvar to MET
        self.JetPxSum_old=0
        self.JetPySum_old=0
        self.GetJetPxPySum_old()
        
        self.JetPxSum_new=0
        self.JetPySum_new=0
        self.GetJetPxPySum_new()
        
        dpx = self.JetPxSum_new - self.JetPxSum_old
        dpy = self.JetPySum_new - self.JetPySum_old

        origMET_pt = self._MET.pt
        origMET_phi = self._MET.phi
        origMET_px = origMET_pt*math.cos(origMET_phi)
        origMET_py = origMET_pt*math.sin(origMET_phi)

        newMET_px = origMET_px - dpx
        newMET_py = origMET_py - dpy
        newMET_pt = math.sqrt(newMET_px**2 + newMET_py**2)
        newMET_phi = math.atan2(newMET_py,newMET_px)

        return newMET_pt,newMET_phi

    def GetJetPxPySum_old(self):
        for cjet in self._CleanJet_col:
            pt=cjet.pt
            phi=cjet.phi
            self.JetPxSum_old+=pt*math.cos(phi)
            self.JetPySum_old+=pt*math.sin(phi)
    def GetJetPxPySum_new(self):
        for cjet in self._CleanJet_col:
            jetidx=cjet.jetIdx
            exec("pt=self._Jet_col[jetidx].pt_"+self.jsysvar)
            phi=self._Jet_col[jetidx].phi
            self.JetPxSum_new+=pt*math.cos(phi)
            self.JetPySum_new+=pt*math.sin(phi)




    def analyze(self, event):
        _Lepton = Object(event, 'Lepton', index=0)
        self._MET = Object(event, self.METtype)
        self._CleanJet_col = Collection(event, "CleanJet")
        self._Jet_col = Collection(event, "Jet")
        for jsysvar in self.jsysvars:
            self.jsysvar=jsysvar
            suffix=jsysvar
            _suffix="_"+suffix
            _suffix_="_"+suffix+"_"

            lepton_pt  = _Lepton.pt
            lepton_eta = _Lepton.eta
            lepton_phi = _Lepton.phi
            lepton_pz  = lepton_pt*math.sinh(lepton_eta)
            lepton_E   = lepton_pt*math.cosh(lepton_eta)
            self._lepton_4v.SetPtEtaPhiM(lepton_pt,lepton_eta,lepton_phi,0)
            met_pt, met_phi  = self.Get_MET_pt_phi()
            
            mu = (Wmass*Wmass)/2 + lepton_pt*met_pt*math.cos(met_phi-lepton_phi)
            met_pz1 = mu*lepton_pz/pow(lepton_pt,2)
            met_pz2 = (  mu*lepton_pz/(lepton_pt**2)  )**2 - ( (lepton_E*met_pt)**2 - mu**2 )/(lepton_pt**2)
            if met_pz2 < 0:
                met_pz = met_pz1
                met_bigZ = met_pz1
            else:
                sol1 = met_pz1 + math.sqrt(met_pz2)
                sol2 = met_pz1 - math.sqrt(met_pz2)
                if abs(sol1) < abs(sol2):
                    met_pz = sol1
                    met_bigZ = sol2
                else:
                    met_pz = sol2
                    met_bigZ = sol1
            met_px   =  met_pt*math.cos(met_phi)
            met_py   =  met_pt*math.sin(met_phi)
            met_E    =  math.sqrt(met_pz**2 + met_pt**2)
            met_bigE =  math.sqrt(met_bigZ**2 + met_pt**2)
            wlep_px    = lepton_pt*math.cos(lepton_phi) + met_pt*math.cos(met_phi)
            wlep_py    = lepton_pt*math.sin(lepton_phi) + met_pt*math.sin(met_phi)
            wlep_pz    = lepton_pz + met_pz
            wlep_bigPz = lepton_pz + met_bigZ
            wlep_E     = lepton_E  + math.sqrt(met_pz**2   + met_pt**2)
            wlep_bigE  = lepton_E  + math.sqrt(met_bigZ**2 + met_pt**2)
            self._Wlep_4v.SetPxPyPzE(   wlep_px,wlep_py,wlep_pz,   wlep_E)
            # TODO use this big4v for the event test, which could enhence the mH resolution                                                                                           
            self._Wlep_big4v.SetPxPyPzE(wlep_px,wlep_py,wlep_bigPz,wlep_bigE)

            _Wlep_Mt = math.sqrt(2*lepton_pt*met_pt*(1-math.cos(lepton_phi - met_phi ) ) )

            



            ##Fill branches
            self.out.fillBranch('Wlep'+_suffix_+'pt',self._Wlep_4v.Pt())
            self.out.fillBranch('Wlep'+_suffix_+'eta',self._Wlep_4v.Eta())
            self.out.fillBranch('Wlep'+_suffix_+'phi',self._Wlep_4v.Phi())
            self.out.fillBranch('Wlep'+_suffix_+'mass',self._Wlep_4v.M())
            self.out.fillBranch('Wlep'+_suffix_+'E',self._Wlep_4v.E())
            self.out.fillBranch('Wlep'+_suffix_+'Mt'  ,_Wlep_Mt)

            self.out.fillBranch('Wlepbig'+_suffix_+'mass',self._Wlep_big4v.M())
            self.out.fillBranch('Wlepbig'+_suffix_+'E',wlep_bigE)
            self.out.fillBranch('Wlepbig'+_suffix_+'pz',wlep_bigPz)
            
            self.out.fillBranch(self.METtype+_suffix_+'pz1',met_pz1) ##MET_pz = pz1+-sqrt(pz2)
            self.out.fillBranch(self.METtype+_suffix_+'pz2',met_pz2)
            
            self.out.fillBranch(self.METtype+_suffix_+'px',met_px) ##MET_pz = pz1+-sqrt(pz2)
            self.out.fillBranch(self.METtype+_suffix_+'py',met_py) ##MET_pz = pz1+-sqrt(pz2)
            self.out.fillBranch(self.METtype+_suffix_+'pt',met_pt) ##MET_pz = pz1+-sqrt(pz2)
            
            self.out.fillBranch(self.METtype+_suffix_+'E',met_E) ##MET_pz = pz1+-sqrt(pz2)
            self.out.fillBranch(self.METtype+_suffix_+'pz',met_pz)
            
            self.out.fillBranch(self.METtype+_suffix_+'big_E',met_bigE) ##MET_pz = pz1+-sqrt(pz2)
            self.out.fillBranch(self.METtype+_suffix_+'big_pz',met_bigZ)
        return True
