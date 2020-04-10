import ROOT
import math
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

Wmass=80.4
class WlepMaker(Module):
    def __init__(self,METtype='PuppiMET'):
        self.METtype = METtype

        ##declare
        self._MET_4v        = ROOT.TLorentzVector()
        self._MET_big4v     = ROOT.TLorentzVector()
        self._lepton_4v     = ROOT.TLorentzVector()
        self._Wlep_4v       = ROOT.TLorentzVector()
        self._Wlep_big4v    = ROOT.TLorentzVector()


    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree

        for var in ['pt','eta','phi','mass','Mt','E','bigmass','bigE']:
            self.out.branch("Wlep_"+var  , "F")
        self.out.branch(self.METtype+'_pz1', "F")
        self.out.branch(self.METtype+'_pz2', "F")
        self.out.branch(self.METtype+'_E', "F")
        self.out.branch(self.METtype+'_Pz', "F")
        self.out.branch(self.METtype+'_bigE', "F")
        self.out.branch(self.METtype+'_bigZ', "F")
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass


    def analyze(self, event):
        _Lepton = Object(event, 'Lepton', index=0)
        _MET = Object(event, self.METtype)

        lepton_pt  = _Lepton.pt
        lepton_eta = _Lepton.eta
        lepton_phi = _Lepton.phi
        lepton_pz  = lepton_pt*math.sinh(lepton_eta)
        lepton_E   = lepton_pt*math.cosh(lepton_eta)
        self._lepton_4v.SetPtEtaPhiM(lepton_pt,lepton_eta,lepton_phi,0)
        met_pt  = _MET.pt
        met_phi = _MET.phi
        mu = (Wmass*Wmass)/2 + lepton_pt*met_pt*math.cos(met_phi-lepton_phi)
        _MET_pz1 = mu*lepton_pz/pow(lepton_pt,2)
        _MET_pz2 = (  mu*lepton_pz/(lepton_pt**2)  )**2 - ( (lepton_E*met_pt)**2 - mu**2 )/(lepton_pt**2)
        if _MET_pz2 < 0:
            _MET_pz = _MET_pz1
            _MET_bigZ = _MET_pz1
        else:
            sol1 = _MET_pz1 + math.sqrt(_MET_pz2)
            sol2 = _MET_pz1 - math.sqrt(_MET_pz2)
            if abs(sol1) < abs(sol2):
                _MET_pz = sol1
                _MET_bigZ = sol2
            else:
                _MET_pz = sol2
                _MET_bigZ = sol1
        met_px   =  met_pt*math.cos(met_phi)
        met_py   =  met_pt*math.sin(met_phi)
        met_E    =  math.sqrt(_MET_pz**2 + met_pt**2)
        met_bigE =  math.sqrt(_MET_bigZ**2 + met_pt**2)
        wlep_px    = lepton_pt*math.cos(lepton_phi) + met_pt*math.cos(met_phi)
        wlep_py    = lepton_pt*math.sin(lepton_phi) + met_pt*math.sin(met_phi)
        wlep_pz    = lepton_pz + _MET_pz
        wlep_bigPz = lepton_pz + _MET_bigZ
        wlep_E     = lepton_E  + math.sqrt(_MET_pz**2   + met_pt**2)
        wlep_bigE  = lepton_E  + math.sqrt(_MET_bigZ**2 + met_pt**2)
        self._Wlep_4v.SetPxPyPzE(   wlep_px,wlep_py,wlep_pz,   wlep_E)
        # TODO use this big4v for the event test, which could enhence the mH resolution                                                                                           
        self._Wlep_big4v.SetPxPyPzE(wlep_px,wlep_py,wlep_bigPz,wlep_bigE)

        _Wlep_Mt = math.sqrt(2*lepton_pt*met_pt*(1-math.cos(lepton_phi - met_phi ) ) )

        ##Fill branches
        self.out.fillBranch('Wlep_pt',self._Wlep_4v.Pt())
        self.out.fillBranch('Wlep_eta',self._Wlep_4v.Eta())
        self.out.fillBranch('Wlep_phi',self._Wlep_4v.Phi())
        self.out.fillBranch('Wlep_mass',self._Wlep_4v.M())
        self.out.fillBranch('Wlep_E',self._Wlep_4v.E())
        self.out.fillBranch('Wlep_Mt'  ,_Wlep_Mt)
        self.out.fillBranch('Wlep_bigmass',self._Wlep_big4v.M())
        self.out.fillBranch('Wlep_bigE',self._Wlep_big4v.E())

        self.out.fillBranch(self.METtype+'_pz1',_MET_pz1) ##MET_pz = pz1+-sqrt(pz2)
        self.out.fillBranch(self.METtype+'_pz2',_MET_pz2)

        self.out.fillBranch(self.METtype+'_E',met_E) ##MET_pz = pz1+-sqrt(pz2)
        self.out.fillBranch(self.METtype+'_Pz',_MET_pz)

        self.out.fillBranch(self.METtype+'_bigE',met_bigE) ##MET_pz = pz1+-sqrt(pz2)
        self.out.fillBranch(self.METtype+'_bigZ',_MET_bigZ)
        return True
