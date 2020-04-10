import os
import ROOT
import sys
import math
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.Wjjtagger_cfg import MYALGO,JETCUTS

Wmass=80.4


class WjjtaggerProducer(Module):
    def __init__(self, year,pairalgos=['dMchi2Resolution','dM'],sysvars='all'):
        self.sysvars=sysvars
        self.year=str(int(year))
        if sysvars=='all':
            print "[WjjtaggerProducer]Run all regrouped set of sys"
            self.sysvars=[]
            for s in ['jesFlavorQCD','jesRelativeBal','jesHF','jesBBEC1','jesEC2','jesAbsolute','jesAbsolute_'+str(year),'jesHF_'+str(year),'jesEC2_'+str(year),'jesRelativeSample_'+str(year),'jesBBEC1_'+str(year),'jesTotal','jer']:
                for d in ['Up','Down']:
                    self.sysvars.append(s+d)
        self.pairalgos=pairalgos
        self.init_JetResolution(year)
                    
    def init_JetResolution(self,Year):##You don;t have to look into this :)
        print "--Initialize JetResolution reader---"
        cmssw_base = os.getenv('CMSSW_BASE')
        if int(Year) == 2016:
          jerInputFileName = "Summer16_25nsV1_DATA_PtResolution_AK4PFchs.txt"
          jerInputFileSource="https://raw.githubusercontent.com/cms-jet/JRDatabase/master/textFiles/Summer16_25nsV1_DATA/Summer16_25nsV1_DATA_PtResolution_AK4PFchs.txt"
        elif int(Year) == 2017:
          jerInputFileName = "Fall17_V3_DATA_PtResolution_AK4PFchs.txt"
          jerInputFileSource = "https://raw.githubusercontent.com/cms-jet/JRDatabase/master/textFiles/Fall17_V3_DATA/Fall17_V3_DATA_PtResolution_AK4PFchs.txt"
        elif int(Year) == 2018:
          jerInputFileName = "Autumn18_V7_DATA_PtResolution_AK4PFchs.txt"
          jerInputFileSource = "https://raw.githubusercontent.com/cms-jet/JRDatabase/master/textFiles/Autumn18_V7_DATA/Autumn18_V7_DATA_PtResolution_AK4PFchs.txt"
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
        for var in self.sysvars:
            for algo in self.pairalgos:
                self.out.branch('isResol_'+algo+"_"+var,"O")
                objname='Whad_'+algo+"_"+var
                for x in ['pt','eta','phi','mass','ScoreToLeast']:
                    self.out.branch(objname+"_"+x,'F')
                self.out.branch(objname+'_cjidx1','I')
                self.out.branch(objname+'_cjidx2','I')
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        ##initialize
        self._isResol={}
        self._Whad={}

        self.CleanJet_col = Collection(event, 'CleanJet')
        self.Jet_col = Collection(event, 'Jet')
        self.rho = event.fixedGridRhoFastjetAll##For deriving resulution

        for var in self.sysvars:
            self._isResol[var]={}
            self._Whad[var]={}
            
            for algo in self.pairalgos:
                self._isResol[var][algo]=False
                self._Whad[var][algo]={
                    'cjidx1':-1,
                    'cjidx2':-1,
                    'pt':-1.,
                    'eta':-999.,
                    'phi':-999.,
                    'mass':-1,
                    'ScoreToLeast':sys.float_info.max,
                }
                #print "var=",var
                #print "algo=",algo
                self._Whad[var][algo]['4v']=ROOT.TLorentzVector()



                exec('self.WhadMaker("'+algo+'","'+var+'")')

        
        for var in self.sysvars:
            for algo in self.pairalgos:
                
                self._Whad[var][algo]['pt']=self._Whad[var][algo]['4v'].Perp()
                self._Whad[var][algo]['eta']=self._Whad[var][algo]['4v'].Eta()
                self._Whad[var][algo]['phi']=self._Whad[var][algo]['4v'].Phi()
                self._Whad[var][algo]['mass']=self._Whad[var][algo]['4v'].M()
 
                self.out.fillBranch('isResol_'+algo+"_"+var, self._isResol[var][algo])
               
                objname='Whad_'+algo+"_"+var                
                for x in ['pt','eta','phi','mass','ScoreToLeast','cjidx1','cjidx2']:
                    self.out.fillBranch(objname+"_"+x,self._Whad[var][algo][x])
                

        return True

    def WhadMaker(self,algo_,var_):
        algo=algo_
        var=var_
        ScoreToLeast=sys.float_info.max
        Whad_mass=-9999
        N=len(self.CleanJet_col)
        for i_cj in range(0,N):
            pt1,eta1,phi1,mass1, qgl1 = self.CleanJet_PtEtaPhiMQgl(i_cj,var)
            if pt1 < JETCUTS[self.year]['ptmin'] : continue
            if abs(eta1) < JETCUTS[self.year]['etamax'] : continue
            for j_cj in range(0,N):
                if j_cj <= i_cj : continue
                pt2,eta2,phi2,mass2,qgl2 = self.CleanJet_PtEtaPhiMQgl(j_cj,var)
                if pt2 < JETCUTS[self.year]['ptmin'] : continue
                if abs(eta2) < JETCUTS[self.year]['etamax'] : continue
                
                thisScore = sys.float_info.max
                if algo=="dM":
                    thisScore = self.CalcDM(pt1,eta1,phi1,mass1,\
                                            pt2,eta2,phi2,mass2)
                elif algo=="dMchi2Resolution":
                    thisScore = self.CalcChi2DMReolsution(pt1,eta1,phi1,mass1,\
                                                          pt2,eta2,phi2,mass2)
                elif algo=="dMchi2Resolutionqgl":
                    thisScore = self.CalcChi2DMReolsutionQgl(pt1,eta1,phi1,mass1,qgl1,\
                                                             pt2,eta2,phi2,mass2,qgl2)
                elif algo=="HighPTjj":
                    thisScore = self.CalcHighPTjj(pt1,eta1,phi1,mass1,\
                                            pt2,eta2,phi2,mass2)
                elif algo=="LowPTjj":
                    thisScore = self.CalcLowPTjj(pt1,eta1,phi1,mass1,\
                                            pt2,eta2,phi2,mass2)


                if thisScore < ScoreToLeast:
                    ScoreToLeast = thisScore
                    v1=ROOT.TLorentzVector()
                    v2=ROOT.TLorentzVector()
                    v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
                    v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2)
                    self._Whad[var][algo]['cjidx1'] = i_cj
                    self._Whad[var][algo]['cjidx2'] = j_cj
                    self._Whad[var][algo]['4v'] = v1+v2
        Whad_mass=self._Whad[var][algo]['4v'].M()
        self._Whad[var][algo]['ScoreToLeast'] = ScoreToLeast
        if Whad_mass > 40 and Whad_mass < 250 : self._isResol[var][algo] = True#self._isResol[var][algo]
        if ScoreToLeast==sys.float_info.max : self._isResol[var][algo] = False ##for safety
        if self._Whad[var][algo]['cjidx1'] < 0 : self._isResol[var][algo] = False #for safty
        if self._Whad[var][algo]['cjidx2'] < 0 : self._isResol[var][algo] = False #for safty
        

    def CleanJet_PtEtaPhiMQgl(self,cjidx,var):
        jidx=self.CleanJet_col[cjidx].jetIdx ##original jet index
        exec("mass=self.Jet_col[jidx].mass_"+var) ##mass
        exec("pt=self.Jet_col[jidx].pt_"+var) ##mass
        eta=self.Jet_col[jidx].eta
        phi=self.Jet_col[jidx].phi
        qgl=self.Jet_col[jidx].qgl

        return pt,eta,phi,mass,qgl

    

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
    def CalcChi2DMReolsution(self,\
               pt1, eta1, phi1, mass1,\
               pt2, eta2, phi2, mass2):

        v1=ROOT.TLorentzVector()
        v2=ROOT.TLorentzVector()
        v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
        v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2)
        #rho=event.fixedGridRhoFastjetAll
        resol1= self.getJetPtResolution(v1,self.rho)
        resol2= self.getJetPtResolution(v2,self.rho)
        M=(v1+v2).M()
        ##--j1 up--##
        v1.SetPtEtaPhiM(pt1*(1+resol1), eta1, phi1, mass1*(1+resol1) )
        M_j1up = (v1+v2).M()
        ##--j1 do--##
        v1.SetPtEtaPhiM(pt1*(1-resol1), eta1, phi1, mass1*(1-resol1) )
        M_j1do = (v1+v2).M()
        ##--j2 up--##
        v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
        v2.SetPtEtaPhiM(pt2*(1+resol2),eta2,phi2,mass2*(1+resol2))
        M_j2up = (v1+v2).M()
        ##--j2 do--##
        v2.SetPtEtaPhiM(pt2*(1-resol2),eta2,phi2,mass2*(1-resol2))
        M_j2do = (v1+v2).M()
        sigma2=(M-M_j1up)**2 + (M-M_j1do)**2 +(M-M_j2up)**2 +(M-M_j2do)**2
        this_Chi2=(M-Wmass)**2/sigma2


        return this_Chi2

    def CalcChi2DMReolsutionQgl(self,\
                                pt1, eta1, phi1, mass1, qgl1,\
                                pt2, eta2, phi2, mass2, qgl2):
        
        if qgl1 < 0 : return sys.float_info.max
        if qgl2 < 0 : return sys.float_info.max
        v1=ROOT.TLorentzVector()
        v2=ROOT.TLorentzVector()
        v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
        v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2)
        #rho=event.fixedGridRhoFastjetAll
        resol1= self.getJetPtResolution(v1,self.rho)
        resol2= self.getJetPtResolution(v2,self.rho)
        M=(v1+v2).M()
        ##--j1 up--##
        v1.SetPtEtaPhiM(pt1*(1+resol1), eta1, phi1, mass1*(1+resol1) )
        M_j1up = (v1+v2).M()
        ##--j1 do--##
        v1.SetPtEtaPhiM(pt1*(1-resol1), eta1, phi1, mass1*(1-resol1) )
        M_j1do = (v1+v2).M()
        ##--j2 up--##
        v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
        v2.SetPtEtaPhiM(pt2*(1+resol2),eta2,phi2,mass2*(1+resol2))
        M_j2up = (v1+v2).M()
        ##--j2 do--##
        v2.SetPtEtaPhiM(pt2*(1-resol2),eta2,phi2,mass2*(1-resol2))
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



    def CalcHighPTjj(self,\
               pt1, eta1, phi1, mass1,\
               pt2, eta2, phi2, mass2):

        v1=ROOT.TLorentzVector()
        v2=ROOT.TLorentzVector()
        v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
        v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2)

        ptjj=(v1+v2).Pt()
        Mjj=(v1+v2).M()
        if Mjj <40 : return sys.float_info.max
        if Mjj >250 : return sys.float_info.max

        return -1*ptjj
    def CalcLowPTjj(self,\
                    pt1, eta1, phi1, mass1,\
                    pt2, eta2, phi2, mass2):

        v1=ROOT.TLorentzVector()
        v2=ROOT.TLorentzVector()
        v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1)
        v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2)

        ptjj=(v1+v2).Pt()
        Mjj=(v1+v2).M()
        if Mjj <40 : return sys.float_info.max
        if Mjj >250 : return sys.float_info.max

        return ptjj

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
