import ROOT as rt
from ROOT import TFile, TTree, TChain

import os,sys
import logging


class MLTools():

  def __init__(self, Config):
    self._trees = {}
    self._fout = None
    self._variables = {}
    self._spectators = {}
    self._cuts = {}
    self._cfgs = Config
    self._debug = True

  def __del__(self):
    pass

  #def SetMLTools(self,tools):
  #  self._tools = tools()

  def InitTreeVariableCuts(self):
    self._trees = {}
    self._fout = None
    self._variables = {}
    self._spectators = {}
    self._cuts = {}

  def SetTrees(self,sampleName,tree_name,inFiles):
    inputDir = ''
    # get chained ttree
    self._treeName = "%s_%s"%(sampleName,tree_name)
    trees = self._connectInputs( inFiles, inputDir, tree_name,False)
    self._trees[self._treeName]= trees

  def SetVariables(self,variables):
    self._variables = variables

  def SetSpectators(self,spectors):
    self._spectators = spectors


  def SetCuts(self,cuts):
    self._cuts = cuts


  #def SetConfigs(self,Configs):
  #  self._tools.SetConfigs(Configs)
    
  #def doTrain(self, sigTreeName, bkgTreeName, outWeightsSuffix, outFileName, epoch=1):
  #  self._tools.doTrain( sigTreeName, bkgTreeName, outWeightsSuffix, outFileName, epoch)
  #  #os.system('mv TMVAClassification/weights TMVAClassification/weights_%s'%(outWeightsSuffix))

  #def doTest(self):
  #  self._tools.doTest()

  def _connectInputs(self, inFiles, inputDir, tree_name, skipMissingFiles, friendsDir = None, skimListDir = None):
    tree = TChain(tree_name)
    for aFile in inFiles:
      #print(aFile)
      tree.Add(aFile)
    return tree

