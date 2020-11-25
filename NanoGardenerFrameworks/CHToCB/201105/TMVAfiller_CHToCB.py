import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os
import array
from collections import OrderedDict 

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.framework.BranchMapping import mappedOutputTree, mappedEvent

#      mvaDic = { 'nameMva' : {
#                                'type'      : 'BDT' ,  
#                                'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/....'   ,
#                                'inputVars' : { 'var1Name' : 'var1Expression' ,
#                                                'var2Name' : 'var2Expression' ,
#                                              } 
#                             } ,
#               } 

class TMVAfiller_CHToCB(Module):
    def __init__(self,mvaCfgFile, syst_suffix='nom', branch_map=''):
        self._syst_suffix = syst_suffix

        cmssw_base = os.getenv('CMSSW_BASE')
        mvaFile = cmssw_base+'/src/LatinoAnalysis/NanoGardener/python/'+mvaCfgFile
        if os.path.exists(mvaFile):
          handle = open(mvaFile,'r')
          exec(handle)
          self.mvaDic = mvaDic
          handle.close()
        print self.mvaDic
        self.mvaDic = mvaDic
        self._branch_map = branch_map

        #PyKeras
        loadKeras = False
        for iMva in self.mvaDic : 
          if 'PyKeras' in self.mvaDic[iMva]['type'] : loadKeras = True  
        if loadKeras : 
          from os import environ
          environ['KERAS_BACKEND'] = 'tensorflow'
          ROOT.TMVA.PyMethodBase.PyInitialize()

        cmssw_base = os.getenv('CMSSW_BASE') 
        for iMva in self.mvaDic :
          self.mvaDic[iMva]['reader'] = ROOT.TMVA.Reader("V")
          self.mvaDic[iMva]['inputs'] = []
          jVar=0
          for iVar in self.mvaDic[iMva]['inputVars'] :
            self.mvaDic[iMva]['inputs'].append(array.array('f',[0]))
            #self.mvaDic[iMva]['reader'].AddVariable(iVar,self.mvaDic[iMva]['inputs'][jVar])
            print(iVar)
            self.mvaDic[iMva]['reader'].AddVariable(iVar,self.mvaDic[iMva]['inputs'][jVar])
            jVar+=1
          self.mvaDic[iMva]['reader'].BookMVA(self.mvaDic[iMva]['type'],cmssw_base+'/src/'+self.mvaDic[iMva]['xmlFile'])      

    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = mappedOutputTree(wrappedOutputTree, mapname=self._branch_map) 
        self.itree = inputTree
        for iMva in self.mvaDic :
          self.out.branch(iMva+'_%s'%self._syst_suffix, 'F')
    
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        event = mappedEvent(event, mapname=self._branch_map)

        fillDummy = False

        if not hasattr(event,'csv_jet0_mvaCHToCB_%s'%self._syst_suffix):
          fillDummy = True

        if fillDummy:
          for iMva in self.mvaDic :
            self.out.fillBranch(iMva+'_%s'%self._syst_suffix, -10)
        else:
          csv_jet0_mvaCHToCB = getattr(event,'csv_jet0_mvaCHToCB_%s'%self._syst_suffix) 
          csv_jet1_mvaCHToCB = getattr(event,'csv_jet1_mvaCHToCB_%s'%self._syst_suffix)
          csv_jet2_mvaCHToCB = getattr(event,'csv_jet2_mvaCHToCB_%s'%self._syst_suffix)
          #(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3
          #(csv_jet0_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)*(csv_jet0_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)
          #(csv_jet1_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)*(csv_jet1_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)
          #(csv_jet2_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)*(csv_jet2_mvaCHToCB-(csv_jet0_mvaCHToCB+csv_jet1_mvaCHToCB+csv_jet2_mvaCHToCB)/3)
          dijet_deltaR0_mvaCHToCB        = getattr(event,'dijet_deltaR0_mvaCHToCB_%s'%self._syst_suffix)
          dijet_deltaR1_mvaCHToCB        = getattr(event,'dijet_deltaR1_mvaCHToCB_%s'%self._syst_suffix)
          Hplus_b_deltaR0_mvaCHToCB      = getattr(event,'Hplus_b_deltaR0_mvaCHToCB_%s'%self._syst_suffix)
          Hplus_b_deltaR1_mvaCHToCB      = getattr(event,'Hplus_b_deltaR1_mvaCHToCB_%s'%self._syst_suffix)
          bb_deltaR_mvaCHToCB            = getattr(event,'bb_deltaR_mvaCHToCB_%s'%self._syst_suffix)
          min_deltaR_bb_event_mvaCHToCB  = getattr(event,'min_deltaR_bb_event_mvaCHToCB_%s'%self._syst_suffix)
          HT_btagged_M                   = getattr(event,'HT_btagged_M_%s'%self._syst_suffix)
          HT_not_btagged_M               = getattr(event,'HT_not_btagged_M_%s'%self._syst_suffix)

          for iMva in self.mvaDic :
            jVar=0
            for iVar in self.mvaDic[iMva]['inputVars'] :  
              self.mvaDic[iMva]['inputs'][jVar][0] = eval(self.mvaDic[iMva]['inputVars'][iVar])
              jVar+=1
            #print "====== ",iMva
            #print self.mvaDic[iMva]['inputVars'].keys()
            #print self.mvaDic[iMva]['inputs']   
            val = self.mvaDic[iMva]['reader'].EvaluateMVA(self.mvaDic[iMva]['type'])
            #print val
            self.out.fillBranch(iMva+'_%s'%self._syst_suffix, val)
            #self.out.fillBranch(iMva, self.mvaDic[iMva]['reader'].EvaluateMVA(self.mvaDic[iMva]['type']))

        return True

