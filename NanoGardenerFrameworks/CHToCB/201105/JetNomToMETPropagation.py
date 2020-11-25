import ROOT
import os
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class JetNomToMETPropagation(Module):

    def __init__(self,jetColl="CleanJet", METLIST=['PuppiMET','MET','RawMET']):

        self.jetColl = jetColl
        self.METLIST=METLIST

    def beginJob(self): 
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree

        for METtype in self.METLIST:
            self.out.branch(METtype+'_pt', 'F')
            self.out.branch(METtype+'_phi', 'F')

        self.out.branch(self.jetColl+'_pt','F',lenVar='n'+self.jetColl)
        

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass


       
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        self.orig_jet_coll = Collection(event, "Jet" ) ## we will get Jet_pt_nom / Jet_phi
        self.jet_coll = Collection(event, self.jetColl)
        
        nJet=len(self.jet_coll)##To update pt of cleanjetcollection
        self.corrPTs=[]


        #### MET_px = -sum( particle_px ) 
        ######MET_px_new = -sum(particle_px_new) = -sum( particle_px - particle_px + particle_px_new  )
        ######## = MET_px -sum(particle_px_new - particle_px)
        ###     => MET_px_new = MET_px - sum( dpx )
        self.JetPxSum_old=0
        self.JetPySum_old=0
        self.GetJetPxPySum_old() ## Set self.JetPxSum_old & self.JetPySum_old
        
        self.JetPxSum_new=0
        self.JetPySum_new=0
        self.GetJetPxPySum_new()
        
        dpx = self.JetPxSum_new - self.JetPxSum_old
        dpy = self.JetPySum_new - self.JetPySum_old


        for METtype in self.METLIST:
            origMET = Object(event, METtype)
            origMET_pt = origMET.pt
            origMET_phi = origMET.phi
            origMET_px = origMET_pt*math.cos(origMET_phi)
            origMET_py = origMET_pt*math.sin(origMET_phi)

            

            newMET_px = origMET_px - dpx
            newMET_py = origMET_py - dpy
            newMET_pt = math.sqrt(newMET_px**2 + newMET_py**2)
            newMET_phi = math.atan2(newMET_py,newMET_px)

            #if METtype=="PuppiMET":
            #    print "origMET_pt = ",origMET_pt
            #    print "newMET_pt = ",newMET_pt
            #    print "origMET_phi = ",origMET_phi
            #    print "newMET_phi = ",newMET_phi

            self.out.fillBranch(METtype+'_pt',newMET_pt)
            self.out.fillBranch(METtype+'_phi',newMET_phi)

        if nJet != len(self.corrPTs):
            print "!!!!!!![jhchoi]ERROR, len of cleanjet is not matched bf/after JEC"

        self.out.fillBranch(self.jetColl+'_pt',self.corrPTs)
        
        return True

    def GetJetPxPySum_old(self):
        for jet in self.jet_coll:
            pt=jet.pt
            phi=jet.phi
            self.JetPxSum_old+=pt*math.cos(phi)
            self.JetPySum_old+=pt*math.sin(phi)


    def GetJetPxPySum_new(self):
        for jet in self.jet_coll:
            jetidx=jet.jetIdx
            pt=self.orig_jet_coll[jetidx].pt_nom
            self.corrPTs.append(pt)
            phi=self.orig_jet_coll[jetidx].phi
            self.JetPxSum_new+=pt*math.cos(phi)
            self.JetPySum_new+=pt*math.sin(phi)
