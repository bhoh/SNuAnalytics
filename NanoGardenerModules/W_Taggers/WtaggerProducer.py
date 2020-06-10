import ROOT
import math
import sys
maxfloat=sys.float_info.max
minfloat=sys.float_info.min
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetSmearer import jetSmearer
from PhysicsTools.NanoAODTools.postprocessing.tools import matchObjectCollection, matchObjectCollectionMultiple
from LatinoAnalysis.NanoGardener.data.Wtagger_cfg import WJID,FATJETCUTS
###configuration###
##https://twiki.cern.ch/twiki/bin/view/CMS/JetWtagging
##W taggers
###Some categories are already corrected on JMS/JMR  @ nanoTool
##DDT ##https://arxiv.org/pdf/1603.00027.pdf
##Also evaluated JMS&JMR SD corr in tau21DDT region: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetWtagging#tau21DDT_0_43
###dictionary structure WJID[year][name] = {c_DDT,tau21min:,tau21max:,}              

#print WJID
#WJID[year][name]={
#C_DDT,tau21min,tau21max,
#JER:{'nom','up','down'}
#JES:
#effSF
#}


#https://github.com/cms-jet/PuppiSoftdropMassCorr/
##--FatJet variables after puppi msoftdrop mass correction/JEC/Smearing->
#FatJet_pt_raw*FatJet_corr_JEC*FatJet_corr_JER, ->use FatJet_pt_nom
#msoftdrop without JMR/JMS ->FatJet_msoftdrop_raw* FatJet_msoftdrop_corr_PUPPI * FatJet_corr_JER ->then JMS/JMR
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
jecTagsMC = {'2016' : 'Summer16_07aug2017_V11_MC',
             '2017' : 'Fall17_17Nov2017_V32_MC',
             '2018' : 'Autumn18_V19_MC'}
jerTagsMC = {'2016' : 'Summer16_25nsV1_MC',
             '2017' : 'Fall17_V3_MC',
             '2018' : 'Autumn18_V7_MC'
            }


class WtaggerProducer(Module):
    def __init__(self,isData, year,sysvars=['nom','jesup','jesdown','jerup','jerdown','jmsup','jmsdown','jmrup','jmrdown']): ##jes,jer,jms,jmr
        self.sysvars=sysvars
        self.year=year
        self.isData=isData
        if isData:
            print "--This is datarun--"
            self.sysvars=['nom']
        globalTag=jecTagsMC[str(self.year)]
        jetType="AK8PFPuppi"
        jerTag = jerTagsMC[str(self.year)]
        if not self.isData:
            self.jerInputFileName = jerTag + "_PtResolution_" + jetType + ".txt"
            self.jerUncertaintyInputFileName = jerTag + "_SF_"  + jetType + ".txt"
            self.jmrVals=[1.,1.,1.] ##cent up down            
            self.jetSmearer = jetSmearer(globalTag, jetType, self.jerInputFileName, self.jerUncertaintyInputFileName, self.jmrVals)

        self.genJetBranchName = "GenJetAK8"
        self.genSubJetBranchName = "SubGenJetAK8"
        self.jetBranchName = "FatJet"
        self.subJetBranchName = "SubJet"
        self.WtaggerConfig=WJID[str(self.year)]

    def beginJob(self):
        print "--beginJob--"
        if not self.isData:
            print "this is MCrun"
            self.jetSmearer.beginJob()
        
    def endJob(self):
        print "--endJob--"
        if not self.isData:
            print "this is MCrun"
            self.jetSmearer.endJob()
        
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        print "--beginFile--"
        self.out = wrappedOutputTree
        for tagname in self.WtaggerConfig:
            for var in self.sysvars:
                objname="isBoost_"+tagname+"_"+var
                self.out.branch(objname,"O")
                #for x in ['pt','eta','phi','mass','tau21ddt','effSF','effSFup','effSFdown']:
                for x in ['pt','eta','phi','mass','tau21ddt','deepTag','deepTagMD']:
                    collname='WtaggerFatjet_'+tagname+'_'+var
                    self.out.branch(collname+'_'+x, "F", lenVar="n"+collname )
                self.out.branch(collname+"_fjetIdx","I",lenVar="n"+collname)

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        print "--endFile--"
        pass


    def analyze(self, event): ##apply JMS/JMR for each id
        #print "--analyze--"
        if not self.isData : self.jetSmearer.setSeed(event)

        self.jets = Collection(event, self.jetBranchName )
        self.subJets = Collection(event, self.subJetBranchName )
        self.lepton = Object(event,"Lepton",index=0) ##Take primary lepton
        lepton_eta=self.lepton.eta
        lepton_phi=self.lepton.eta

        ptmin=FATJETCUTS[str(self.year)]['ptmin']
        etamax=FATJETCUTS[str(self.year)]['etamax']
        msdmin=FATJETCUTS[str(self.year)]['msdmin']
        msdmax=FATJETCUTS[str(self.year)]['msdmax']
        #print "ptmin,etamax,msdmin,msdmax=",ptmin,etamax,msdmin,msdmax

        if not self.isData: ##for MC, use gen infos
            genJets = Collection(event, self.genJetBranchName )
            genSubJets = Collection(event, self.genSubJetBranchName )

            genSubJetMatcher = matchObjectCollectionMultiple( genJets, genSubJets, dRmax=0.8 )
            pairs = matchObjectCollection(self.jets, genJets)

        ##initialize  Wtagger Collections (nSystematic)*(ntag)
        WtaggerColl={} ##WtaggerColl[tagname][systematicvar][pt,eta,phi,mass,tau21ddt,effSF]
        for tagname in self.WtaggerConfig:
            WtaggerColl[tagname]={}
            for var in self.sysvars:
                WtaggerColl[tagname][var]={
                    'pt':[],
                    'eta':[],
                    'phi':[],
                    'mass':[],
                    'tau21ddt':[],
                    'deepTag':[],
                    'deepTagMD':[],
                    'fjetIdx':[],
                    #'effSF':[],
                    #'effSFup':[],
                    #'effSFdown':[],
                }
            
        for tagname, wtag in self.WtaggerConfig.items(): ## from WJID
            #if tagname!='HP45':continue
            C_DDT=0
            tau21min=minfloat
            tau21max=maxfloat
            deepTag_min=minfloat
            deepTagMD_min=minfloat
            if 'tau21min' in wtag:
                C_DDT=wtag['C_DDT']
                tau21min=wtag['tau21min']
                tau21max=wtag['tau21max']
            if 'deepTag_min' in wtag:
                deepTag_min=wtag['deepTag_min']
            if 'deepTagMD_min' in wtag:
                deepTagMD_min=wtag['deepTagMD_min']

            #effSF=[1,1,1]
            jet_msdcorr_jmrNomVal, jet_msdcorr_jmrUpVal, jet_msdcorr_jmrDownVal = 1, 1, 1
            jmsNomVal,jmsDownVal,jmsUpVal = 1, 1, 1
            #if not self.isData : ##for MC, get JMR/JMS values
               # effSF=wtag['effSF']
            
            

            
            if (not self.isData) and ('JMR' in wtag) and ('JMS' in wtag): ##for MC, get JMR/JMS values
                self.jetSmearer.jmr_vals=[ wtag['JMR']['nom'], wtag['JMR']['up'], wtag['JMR']['down'] ]
                jmsNomVal, jmsDownVal, jmsUpVal = [ wtag['JMS']['nom'], wtag['JMS']['up'], wtag['JMS']['down'] ] ##jms for each id






            for ij, jet in enumerate(self.jets):##FatJet loop
                ##puppi sd correction##
                if jet.subJetIdx1 >= 0 and jet.subJetIdx2 >= 0 :
                    groomedP4 = self.subJets[ jet.subJetIdx1 ].p4() + self.subJets[ jet.subJetIdx2].p4() #check subjet jecs
                else :
                    groomedP4 = None ## [jhchoi]non 2 subjets cases
                puppisd_total=jet.msoftdrop_corr_PUPPI
                if groomedP4 != None:
                    groomedP4.SetPtEtaPhiM(groomedP4.Perp(), groomedP4.Eta(), groomedP4.Phi(), groomedP4.M()*puppisd_total)
                jet_msdcorr_raw = groomedP4.M() if groomedP4 != None else 0.0 # now apply the mass correction to the raw value
                if jet_msdcorr_raw < 0.0:
                    jet_msdcorr_raw *= -1.0
                if not self.isData:
                    ##jms/jmr smearing
                    genJet = pairs[jet]
                    genGroomedSubJets = genSubJetMatcher[genJet] if genJet != None else None
                    genGroomedJet = genGroomedSubJets[0].p4() + genGroomedSubJets[1].p4() if genGroomedSubJets != None and len(genGroomedSubJets) >= 2 else None
                    ( jet_msdcorr_jmrNomVal, jet_msdcorr_jmrUpVal, jet_msdcorr_jmrDownVal ) = self.jetSmearer.getSmearValsM(groomedP4, genGroomedJet) if groomedP4 != None and genGroomedJet != None else (0.,0.,0.)

                

                ###sys sources -> jes/jer/jms/jmr 
                ###pt -> FatJet_pt_nom,
                ###pt,jer-> FatJet_pt_jerUp, FatJet_pt_jerDown
                ###pt,jes-> FatJet_pt_jesTotalUp, FatJet_pt_jesTotalDown
                ###pt,jms-> FatJet_pt_nom
                ###pt,jmr-> FatJet_pt_nom

                ###msoftdrop -> FatJet_msoftdrop_raw* FatJet_msoftdrop_corr_PUPPI * FatJet_corr_JER * jet_msdcorr_jmrNomVal * jmsNomVal
                ##mosftdrop,jer -> FatJet_msoftdrop_raw* FatJet_msoftdrop_corr_PUPPI * FatJet_corr_JER * jet_msdcorr_jmrNomVal * jmsNom Val * FatJet_msoftdrop_jerUp/FatJet_msoftdrop_nom ##reuse ratio
                ##mosftdrop,jes -> FatJet_msoftdrop_raw* FatJet_msoftdrop_corr_PUPPI * FatJet_corr_JER * jet_msdcorr_jmrNomVal * jmsNomVal * FatJet_msoftdrop_jesTotalUp/FatJet_msoftdrop_nom    ##reuse retio
                ###msoftdrop, jmr -> FatJet_msoftdrop_raw* FatJet_msoftdrop_corr_PUPPI * FatJet_corr_JER * jet_msdcorr_jmrUpVal * jmsNomVal 
                ###Msoftdrop, jms -> Fatjet_msoftdrop_raw* FatJet_msoftdrop_corr_PUPPI * FatJet_corr_JER * jet_msdcorr_jmrNomVal * jmsUpVal
                
                
                ##treat them later

                ##nominal
                for var in self.sysvars:
                    #print "----var=>",var,"----"
                    isWtagged=True
                    exec("pt,eta,phi,mass=self.SetJetP4_"+var+"(jet,jet_msdcorr_jmrNomVal,jmsNomVal, jmsDownVal, jmsUpVal, jet_msdcorr_jmrUpVal, jet_msdcorr_jmrDownVal)")
                    #print "pt,eta,phi,mass",pt,eta,phi,mass
                    #tau21=999999.
                    tau21ddt=maxfloat
                    tau1=jet.tau1
                    tau2=jet.tau2
                    deepTag=jet.deepTag_WvsQCD
                    deepTagMD=jet.deepTagMD_WvsQCD
                    if tau1!=0 and mass !=0:
                        tau21 = tau2/tau1
                        tau21ddt=tau21+C_DDT*math.log(mass**2/pt)##use tau21ddt generally(if not ddt id, tau21ddt=tau21
                    if tau21ddt > tau21max: isWtagged=False
                    if tau21ddt < tau21min: isWtagged=False
                    if deepTag < deepTag_min : isWtagged=False
                    if deepTagMD < deepTagMD_min : isWtagged=False
                    if pt < ptmin : isWtagged=False
                    if abs(eta) > etamax : isWtagged=False
                    if mass < msdmin : isWtagged=False
                    if mass > msdmax : isWtagged=False
                    if self.getDeltaR(phi,eta,lepton_phi,lepton_eta) < 0.8 : isWtagged=False
                    if isWtagged:
                        #for x in ['pt','eta','phi','mass','tau21ddt','effSF']:
                        WtaggerColl[tagname][var]['pt'].append(pt)
                        WtaggerColl[tagname][var]['eta'].append(eta)
                        WtaggerColl[tagname][var]['phi'].append(phi)
                        WtaggerColl[tagname][var]['mass'].append(mass)
                        WtaggerColl[tagname][var]['tau21ddt'].append(tau21ddt)
                        WtaggerColl[tagname][var]['deepTag'].append(deepTag)
                        WtaggerColl[tagname][var]['deepTagMD'].append(deepTagMD)
                        WtaggerColl[tagname][var]['fjetIdx'].append(ij)
                        #WtaggerColl[tagname][var]['effSF'].append(effSF['nom'])
                        #WtaggerColl[tagname][var]['effSFup'].append(effSF['up'])
                        #WtaggerColl[tagname][var]['effSFdown'].append(effSF['down'])
                        


                        #print "pt=",pt, "eta=",eta, "phi=",phi,"mass=",mass,"tau21ddt=",tau21ddt
                        #print "jet_msdcorr_jmrNomVal, jet_msdcorr_jmrUpVal, jet_msdcorr_jmrDownVal",jet_msdcorr_jmrNomVal, jet_msdcorr_jmrUpVal, jet_msdcorr_jmrDownVal
                        #print "jmsNomVal, jmsDownVal, jmsUpVal",jmsNomVal, jmsDownVal, jmsUpVal
                        
                        #print "effSF, effSFup, effSFdown = ",effSF['nom'],effSF['up'],effSF['down']

        for tagname in self.WtaggerConfig:
            for var in self.sysvars:
                ##Define flag##
                isBoost=False
                if len(WtaggerColl[tagname][var]['pt'])>0: ##if there's Wtagged fatjet->True 
                    isBoost=True
                #print isBoost
                objname="isBoost_"+tagname+"_"+var
                self.out.fillBranch(objname,isBoost)
                collname='WtaggerFatjet_'+tagname+'_'+var
                for x in WtaggerColl[tagname][var]:
                    self.out.fillBranch(collname+'_'+x,WtaggerColl[tagname][var][x])
        return True
    ##--Nominal--##
    def SetJetP4_nom(self,jet,jet_msdcorr_jmrNomVal,jmsNomVal, jmsDownVal, jmsUpVal, jet_msdcorr_jmrUpVal, jet_msdcorr_jmrDownVal):
        pt=jet.pt_nom
        eta=jet.eta
        phi=jet.phi
        #print "jet.msoftdrop_raw,jet.msoftdrop_corr_PUPPI,jet.corr_JER,jet_msdcorr_jmrNomVal,jmsNomVal",jet.msoftdrop_raw,jet.msoftdrop_corr_PUPPI,jet.corr_JER,jet_msdcorr_jmrNomVal,jmsNomVal
        if not self.isData :
            msoftdrop=jet.msoftdrop_raw*jet.msoftdrop_corr_PUPPI*jet.corr_JER*jet_msdcorr_jmrNomVal*jmsNomVal
        else:
            msoftdrop = jet.msoftdrop_nom
        return pt,eta,phi,msoftdrop
    ###--JES--###
    def SetJetP4_jesup(self,jet,jet_msdcorr_jmrNomVal,jmsNomVal, jmsDownVal, jmsUpVal, jet_msdcorr_jmrUpVal, jet_msdcorr_jmrDownVal):
        pt=jet.pt_jesTotalUp
        eta=jet.eta
        phi=jet.phi
        msoftdrop=jet.msoftdrop_raw*jet.msoftdrop_corr_PUPPI*jet.corr_JER*jet_msdcorr_jmrNomVal*jmsNomVal
        return pt,eta,phi,msoftdrop

    def SetJetP4_jesdown(self,jet,jet_msdcorr_jmrNomVal,jmsNomVal, jmsDownVal, jmsUpVal, jet_msdcorr_jmrUpVal, jet_msdcorr_jmrDownVal):
        pt=jet.pt_jesTotalDown
        eta=jet.eta
        phi=jet.phi
        msoftdrop=jet.msoftdrop_raw*jet.msoftdrop_corr_PUPPI*jet.corr_JER*jet_msdcorr_jmrNomVal*jmsNomVal
        return pt,eta,phi,msoftdrop


    ###--JER--###
    def SetJetP4_jerup(self,jet,jet_msdcorr_jmrNomVal,jmsNomVal, jmsDownVal, jmsUpVal, jet_msdcorr_jmrUpVal, jet_msdcorr_jmrDownVal):
        pt=jet.pt_jerUp
        eta=jet.eta
        phi=jet.phi
        msoftdrop=0
        if jet.msoftdrop_nom!=0:
            msoftdrop=jet.msoftdrop_raw*jet.msoftdrop_corr_PUPPI*jet.corr_JER*jet_msdcorr_jmrNomVal*jmsNomVal
        return pt,eta,phi,msoftdrop

    def SetJetP4_jerdown(self,jet,jet_msdcorr_jmrNomVal,jmsNomVal, jmsDownVal, jmsUpVal, jet_msdcorr_jmrUpVal, jet_msdcorr_jmrDownVal):
        pt=jet.pt_jerDown
        eta=jet.eta
        phi=jet.phi
        msoftdrop=jet.msoftdrop_raw*jet.msoftdrop_corr_PUPPI*jet.corr_JER*jet_msdcorr_jmrNomVal*jmsNomVal
        return pt,eta,phi,msoftdrop

    ###--JMS--###
    def SetJetP4_jmsup(self,jet,jet_msdcorr_jmrNomVal,jmsNomVal, jmsDownVal, jmsUpVal, jet_msdcorr_jmrUpVal, jet_msdcorr_jmrDownVal):
        pt=jet.pt_nom
        eta=jet.eta
        phi=jet.phi
        msoftdrop=jet.msoftdrop_raw*jet.msoftdrop_corr_PUPPI*jet.corr_JER*jet_msdcorr_jmrNomVal*jmsUpVal 
        return pt,eta,phi,msoftdrop

    def SetJetP4_jmsdown(self,jet,jet_msdcorr_jmrNomVal,jmsNomVal, jmsDownVal, jmsUpVal, jet_msdcorr_jmrUpVal, jet_msdcorr_jmrDownVal):
        pt=jet.pt_nom
        eta=jet.eta
        phi=jet.phi
        msoftdrop=jet.msoftdrop_raw*jet.msoftdrop_corr_PUPPI*jet.corr_JER*jet_msdcorr_jmrNomVal*jmsDownVal 

        return pt,eta,phi,msoftdrop

    ###--JMS--###
    def SetJetP4_jmrup(self,jet,jet_msdcorr_jmrNomVal,jmsNomVal, jmsDownVal, jmsUpVal, jet_msdcorr_jmrUpVal, jet_msdcorr_jmrDownVal):
        pt=jet.pt_nom
        eta=jet.eta
        phi=jet.phi
        msoftdrop=jet.msoftdrop_raw*jet.msoftdrop_corr_PUPPI*jet.corr_JER*jet_msdcorr_jmrUpVal*jmsNomVal
        #FatJet_msoftdrop_raw* FatJet_msoftdrop_corr_PUPPI * FatJet_corr_JER * jet_msdcorr_jmrUpVal * jmsNomVal
        return pt,eta,phi,msoftdrop

    def SetJetP4_jmrdown(self,jet,jet_msdcorr_jmrNomVal,jmsNomVal, jmsDownVal, jmsUpVal, jet_msdcorr_jmrUpVal, jet_msdcorr_jmrDownVal):
        pt=jet.pt_nom
        eta=jet.eta
        phi=jet.phi
        msoftdrop=jet.msoftdrop_raw*jet.msoftdrop_corr_PUPPI*jet.corr_JER*jet_msdcorr_jmrDownVal*jmsNomVal
        return pt,eta,phi,msoftdrop
    def getDeltaR(self, phi1, eta1, phi2, eta2):
        dphi = phi1 - phi2
        if dphi > ROOT.TMath.Pi(): dphi -= 2*ROOT.TMath.Pi()
        if dphi < -ROOT.TMath.Pi(): dphi += 2*ROOT.TMath.Pi()
        deta = eta1 - eta2
        deltaR = math.sqrt((deta*deta) + (dphi*dphi))
        return deltaR
