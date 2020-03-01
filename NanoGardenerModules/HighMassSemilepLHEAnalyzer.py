import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import sys
import math
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection ,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module


class HighMassSemilepLHEAnalyzer(Module):
    def __init__(self):
        pass

    def beginJob(self):
        pass
    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        # New Branches

        self.out.branch('LHE_mWW', "F") 
        self.out.branch('LHE_mWlep', "F") 
        self.out.branch('LHE_mWhad', "F") 
        self.out.branch('LHE_nGluon', "I") 
        self.out.branch('LHE_nNonWparton', "I")
        self.out.branch('GEN_mH','F')

        


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    
    def analyze(self, event):
        doPrint=False
        LHEPart_coll = Collection(event, "LHEPart")
        GenPart_coll = Collection(event, "GenPart")
        
        nLHEPart = len(LHEPart_coll)
        Wlep=ROOT.TLorentzVector()
        Whad=ROOT.TLorentzVector()
        nGluon=0
        nNonWparton=0
        LHE=Object(event, 'LHE')
        
        Generator=Object(event, 'Generator')
        mHinGen=0
        
        
        NonW_partons={} ##List of TLorentzVectors

            

        ##Particle Level mH##
        for i,p in enumerate(GenPart_coll):
            i_mother=p.genPartIdxMother
            
            if i_mother<0:continue
            if GenPart_coll[i_mother].status==21 and p.pdgId==25: ## Higgs from incoming partons                                                  
                mHinGen=p.mass



        ##Genlevel info##
        idx_NonW_partons=0
        #print "-----GEN------"
        #print 'Generator_id1=',Generator.id1
        #print 'Generator_id2=',Generator.id2

        for i,p in enumerate(GenPart_coll):
            i_mother=p.genPartIdxMother
            this_part=ROOT.TLorentzVector()
            this_part.SetPtEtaPhiM(p.pt, p.eta, p.phi, p.mass)
            if i_mother<0:
                #print 'i=',i,'p.status=,',p.status,'i_mother=',i_mother,'pdgId=',p.pdgId,'px=',this_part.Px(),'py=',this_part.Py(),'pz=',this_part.Pz(),'m=',this_part.M(),'pt=',this_part.Pt()
                continue
            #if GenPart_coll[i_mother].status==21 or p.status==21 or GenPart_coll[i_mother].pdgId==25 :
                #print 'i=',i,'p.status=',p.status,'i_mother=',i_mother,'pdgId=',p.pdgId,'px=',this_part.Px(),'py=',this_part.Py(),'pz=',this_part.Pz(),'m=',this_part.M(),'pt=',this_part.Pt()
            
            if GenPart_coll[i_mother].status==21 and p.pdgId!=25 and (abs(p.pdgId) in [1,2,3,4,5,21]): ## not Higgs but from incoming partons
                this_part=ROOT.TLorentzVector()
                this_part.SetPtEtaPhiM(p.pt, p.eta, p.phi, p.mass)
                NonW_partons[idx_NonW_partons]={'pdgId':p.pdgId, 'px':this_part.Px(), 'py':this_part.Py(), 'pz':this_part.Pz(),'M':this_part.M(),'pt':p.pt,'eta':p.eta,'phi':p.phi}
                idx_NonW_partons+=1
                


        ##LHElevel info##
        ##Select NonWparton##
        for i_nwp in NonW_partons: ##for each non-W parton in GenLevel
            pt = NonW_partons[i_nwp]['pt']
            eta = NonW_partons[i_nwp]['eta']
            phi = NonW_partons[i_nwp]['phi']
            mass = NonW_partons[i_nwp]['M']
            pdgId=NonW_partons[i_nwp]['pdgId']


            NonW_partons[i_nwp]['i_LHE']=-1

            this_nwp=ROOT.TLorentzVector()
                
            this_nwp.SetPtEtaPhiM(pt,eta,phi,mass)
                


            dP2=sys.float_info.max ##momentum difference


            for i,p in enumerate(LHEPart_coll):
                this_pcand=ROOT.TLorentzVector()
                this_pcand.SetPtEtaPhiM(p.pt, p.eta, p.phi, p.mass)
                this_dP2=this_nwp.Dot(this_pcand)

                ## if this candidate is the same flavor-parton and smaller momentum difference
                ##->Set it to the new nonW parton
                if p.pdgId == pdgId and this_dP2 < dP2:
                    NonW_partons[i_nwp]['i_LHE']=i
                    dP2=this_dP2
                        
        if NonW_partons[i_nwp]['i_LHE']==-1:
            print "!!!!!!!!!!!!!!Not matched LHE final and Gen Status21"
            doPrint=True

        ##---Check whether no LHE pdgid in incoming
        HasIncomingPdgId=False
        for i_nwp in NonW_partons:
            LHEidx=NonW_partons[i_nwp]['i_LHE']
            LHEpdgId=LHEPart_coll[LHEidx].pdgId
            if LHEpdgId == Generator.id1:
                HasIncomingPdgId=True
            elif LHEpdgId == Generator.id2:
                HasIncomingPdgId=True
        if not HasIncomingPdgId:
            print "Incoming parton id != outgoing parton not from higgs"
            doPrint=True


        #doPrint=False
        for i,p in enumerate(LHEPart_coll):
            this_part=ROOT.TLorentzVector()
            this_part.SetPtEtaPhiM(p.pt, p.eta, p.phi, p.mass)


            if p.pdgId == 21:
                nGluon+=1
            

            isNonWparton=False
            for i_nwp in NonW_partons:
                if NonW_partons[i_nwp]['i_LHE']==i: isNonWparton=True

                
            if isNonWparton:
                nNonWparton+=1
                #print 'i=',i,'pdgId=',p.pdgId,'px=',this_part.Px(),'py=',this_part.Py(),'pz=',this_part.Pz(),'m=',this_part.M(),'pt=',this_part.Pt()
                continue

            if abs(p.pdgId) in [11,12,13,14,15,16]:
                Wlep+=this_part

            elif abs(p.pdgId) in [1,2,3,4,5]:
                Whad+=this_part
                

            
            
        #if nLHEPart>4:
        if nLHEPart != 4+nNonWparton:
            print nLHEPart,'!=',nNonWparton
            doPrint=True
        if Generator.id1==Generator.id2 and Generator.id1==21:
            doPrint=True
            print "gluongluon "
            print 'Generator.id1=',Generator.id1
            print 'Generator.id2=',Generator.id2
            
        #doPrint=True
        if doPrint:
            print "----No=",event.event,"----"
            print "---LHE-------------"
            for i,p in enumerate(LHEPart_coll):
                this_part=ROOT.TLorentzVector()
                this_part.SetPtEtaPhiM(p.pt, p.eta, p.phi, p.mass)
                print 'i=',i,'pdgId=',p.pdgId,'px=',this_part.Px(),'py=',this_part.Py(),'pz=',this_part.Pz(),'m=',this_part.M(),'pt=',this_part.Pt()
            print "---GEN------"
            for i,p in enumerate(GenPart_coll):
                i_mother=p.genPartIdxMother
                this_part=ROOT.TLorentzVector()
                this_part.SetPtEtaPhiM(p.pt, p.eta, p.phi, p.mass)
                if i_mother<0:
                    print 'i=',i,'p.status=,',p.status,'i_mother=',i_mother,'pdgId=',p.pdgId,'px=',this_part.Px(),'py=',this_part.Py(),'pz=',this_part.Pz(),'m=',this_part.M(),'pt=',this_part.Pt()                                                                                                                                                                   
                    continue
                if GenPart_coll[i_mother].status==21 or p.status==21 or GenPart_coll[i_mother].pdgId==25 :                                                                           
                    print 'i=',i,'p.status=',p.status,'i_mother=',i_mother,'pdgId=',p.pdgId,'px=',this_part.Px(),'py=',this_part.Py(),'pz=',this_part.Pz(),'m=',this_part.M(),'pt=',this_part.Pt()                                                                                                                                                                    

            print 'mWW=',(Wlep+Whad).M()
            print 'mWlep=',(Wlep).M()
            print 'mWhad=',(Whad).M()
            print 'Vpt=',LHE.Vpt
            print 'Generator_id1=',Generator.id1
            print 'Generator_id2=',Generator.id2
            print 'Generator.x1=',Generator.x1
            print 'Generator.x2=',Generator.x2
            print 'Generator.xpdf1=',Generator.xpdf1
            print 'Generator.xpdf2=',Generator.xpdf2
            print 'nGluon=',nGluon
            print 'nNonWparton=',nNonWparton
            print 'nLHEPart=',nLHEPart
            if nNonWparton!=len(NonW_partons):
                print "nNonWparton!=len(NonW_partons)"
                print 'len(NonW_partons)=',len(NonW_partons)


        self.out.fillBranch('LHE_mWW', (Wlep+Whad).M() )
        self.out.fillBranch('LHE_mWlep', (Wlep).M())
        self.out.fillBranch('LHE_mWhad', (Whad).M())
        self.out.fillBranch('LHE_nGluon', nGluon)
        self.out.fillBranch('LHE_nNonWparton', nNonWparton)
        self.out.fillBranch('GEN_mH',mHinGen)
        return True


def CheckFromHiggs(p,GenPart_coll):
    FromHiggs=False
    i_mother=p.genPartIdxMother
    while i_mother >=0:

        if GenPart_coll[i_mother].pdgId==25:
            FromHiggs=True
        i_mother=GenPart_coll[i_mother].genPartIdxMother
    return FromHiggs


'''
            print "=====Gen========"
            Wlep_GEN=ROOT.TLorentzVector()
            Whad_GEN=ROOT.TLorentzVector()

            for i,p in enumerate(GenPart_coll):
                doPrint=False
                #if p.statusFlags in [7,11]:                                                                                                                  
                i_mother=p.genPartIdxMother
                this_part=ROOT.TLorentzVector()
                this_part.SetPtEtaPhiM(p.pt, p.eta, p.phi, p.mass)

                                                                                                                                                              
                if p.status in [21,22,23] :                                                                                                                   
                    doPrint=True                                                                                                                              
                    if abs(p.pdgId) in [1,2,3,4,5] and CheckFromHiggs(p,GenPart_coll):                                                                        
                        Whad_GEN+=this_part                                                                                                                   
                    elif abs(p.pdgId) in [11,12,13,14,15,16] and CheckFromHiggs(p,GenPart_coll):                                                              
                        Wlep_GEN+=this_part                                                                                                                   
                                                                                                                                                              
                                                                                                                                                              
                                                                                                                                                              
            print 'mWlep in Gen=',Wlep_GEN.M()                                                                                                                
            print 'mWhad in Gen=',Whad_GEN.M()                                                                                                                
            print 'mWW   in GEN=',(Wlep_GEN+Whad_GEN).M()                                                                                                     

                if i_mother<0:continue
                if GenPart_coll[i_mother].status==21:
                    doPrint=True

                if doPrint:
                    print 'i=',i,'pdgId=',p.pdgId,'genPartIdxMother=',p.genPartIdxMother,'p.status',p.status,'px=',this_part.Px(),'py=',this_part.Py(),'pz=',this_part.Pz(),'m=',this_part.M(),'pt=',this_part.Pt()

'''
