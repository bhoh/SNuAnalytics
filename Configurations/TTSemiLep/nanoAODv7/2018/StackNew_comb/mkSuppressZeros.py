#!/usr/bin/env python
import json
import sys
from sys import exit           
import ROOT
import optparse                
import LatinoAnalysis.Gardener.hwwtools as hwwtools
import os.path
import string                  
import logging                 
import LatinoAnalysis.Gardener.odict as odict
import traceback
from array import array        
from collections import OrderedDict
import math

import os

# 1. read hadded shape root files
# 2. read configuration files and then read cuts, samples, nuisances
# 3. find nuisance
# 4. get iVar
# 5. calc envelop
# 6. write histo
class ShapeFactory:
    _logger = logging.getLogger('ShapeFactory')

    # _____________________________________________________________________________
    def __init__(self):

      cuts = {}
      self._cuts = cuts

      samples = OrderedDict()
      self._samples = samples
      
      variables = {}
      self._variables = variables

      nuisances = {}
      self._nuisances = nuisances

      outputDirShape = {}
      self._outputDirShape = outputDirShape


    def makeSuppressZeros(self, inputFile, outputDirShape, cuts, samples, inputDir, nuisances, variables):
      self._cuts = cuts
      self._samples = samples
      self._variables = variables
      self._nuisances = nuisances
      self._outputDirShape = outputDirShape

      os.system ("mkdir " + outputDirShape + "/")
      os.system ("cp " + inputFile + " " + outputDirShape + "/results_suppressZeros.root" )
      fileIn = ROOT.TFile(inputFile, "READ")
      self._outFile = ROOT.TFile.Open( self._outputDirShape + '/results_suppressZeros.root', 'UPDATE')

      def getSubLists(input_list, key):
        sublists = []                                                             
        for name in input_list:
          if key in input_list[name]:
            for suffix in input_list[name][key]:
              subListName = name + '_' + suffix
              sublists.append(subListName)
          else:
            sublists.append(name)
        return sublists

      for cutName in getSubLists(self._cuts,'categories') :
        #print "cut = ", cutName, " :: ", cuts[cutName]
        for variableName in self._variables:
          #print "variable = ", variableName, " :: ", variables[variableName]
          for sampleName in getSubLists(self._samples,'subsamples'):
            #print "sample = ", sampleName, " :: ", samples[sampleName]
            histoNameNorm = '{CUT}/{VAR}/histo_{SAMPLE}'.format(CUT=cutName,
                                                               VAR=variableName,
                                                               SAMPLE=sampleName
                                                              )
            print histoNameNorm
            self._outFile.cd()
            histoNorm = fileIn.Get(histoNameNorm)
            histoNorm_new = self._suppressZeros(histoNorm)
            ##
            if 'CHToCB_M' in sampleName:
              histoNorm_new.Scale(0.01)
            ##
            self._outFile.cd('{CUT}/{VAR}'.format(CUT=cutName,VAR=variableName))
            histoNorm_new.Write("",ROOT.TObject.kOverwrite)

            for nuisanceName in self._nuisances:
              nuisanceType = nuisances[nuisanceName]['type']
              if nuisanceType in ['lnN', 'auto']:
                continue
              if sampleName not in nuisances[nuisanceName]['samples']:
                continue

              self._outFile.cd()
              histoNameUp  = '{CUT}/{VAR}/histo_{SAMPLE}_{NUIS}Up'.format(CUT=cutName,
                                                                         VAR=variableName,
                                                                         SAMPLE=sampleName,
                                                              NUIS=nuisances[nuisanceName]['name']
                                                             )
              histoNameDown = '{CUT}/{VAR}/histo_{SAMPLE}_{NUIS}Down'.format(CUT=cutName,
                                                                 VAR=variableName,
                                                                 SAMPLE=sampleName,
                                                                 NUIS=nuisances[nuisanceName]['name']
                                                                )
              
              print histoNameUp, histoNameDown
    
              histoUp   = fileIn.Get(histoNameUp)
              histoDown = fileIn.Get(histoNameDown)
              histoUp_new   = self._suppressZeros(histoUp)
              histoDown_new = self._suppressZeros(histoDown)
              ##
              if 'CHToCB_M' in sampleName:
                histoUp_new.Scale(0.01)
                histoDown_new.Scale(0.01)
              ##
              self._outFile.cd('{CUT}/{VAR}'.format(CUT=cutName,VAR=variableName))
              histoUp_new.Write("",ROOT.TObject.kOverwrite)
              histoDown_new.Write("",ROOT.TObject.kOverwrite)
              ### END Loop ###




      self._outFile.Close()
      fileIn.Close()


    def _suppressZeros(self, th1):
      th1_new = th1.Clone()
      for ibin in range(1, th1_new.GetNbinsX()+1) :
        if th1_new.GetBinContent(ibin) <= 0 :
          th1_new.SetBinContent(ibin, 10e-8) 
      # the SetBinError does not allow asymmetric -> fine, maximum uncertainty set
      for ibin in range(1, th1_new.GetNbinsX()+1) :
        if th1_new.GetBinContent(ibin) - th1_new.GetBinErrorLow(ibin) < 0 :
          th1_new.SetBinError(ibin, th1_new.GetBinContent(ibin)) 
      return th1_new


if __name__ == '__main__':

  usage = 'usage: %prog [options]'
  parser = optparse.OptionParser(usage)
  
  parser.add_option('--outputDirShape'   , dest='outputDirShape'   , help='output directory for values and plots'           , default='./')
  parser.add_option('--inputFile'      , dest='inputFile'      , help='input file with histograms'                      , default='input.root')
  parser.add_option('--inputDir'       , dest='inputDir'       , help='input directory where to find the default trees' , default='./data/')
  parser.add_option('--nuisancesFile'  , dest='nuisancesFile'  , help='file with nuisances configurations'         , default=None)
  
  # read default parsing options as well
  hwwtools.addOptions(parser)
  hwwtools.loadOptDefaults(parser)
  (opt, args) = parser.parse_args()
  
  #sys.argv.append( '-b' )
  #ROOT.gROOT.SetBatch()
  print " configuration file = ", opt.pycfg
  
  print " inputFile          = ", opt.inputFile
  print " outputDirShape       = ", opt.outputDirShape
  print " inputDir           = ", opt.inputDir
  
  if not opt.debug:
    pass
  elif opt.debug == 2:
    print 'Logging level set to DEBUG (%d)' % opt.debug
    logging.basicConfig( level=logging.DEBUG )
  elif opt.debug == 1:
    print 'Logging level set to INFO (%d)' % opt.debug
    logging.basicConfig( level=logging.INFO )
  
  
  factory = ShapeFactory()
  
  cuts = {}
  if os.path.exists(opt.cutsFile) :
    handle = open(opt.cutsFile,'r')
    exec(handle)
    handle.close()
  
  samples = OrderedDict()
  if os.path.exists(opt.samplesFile) :
    handle = open(opt.samplesFile,'r')
    exec(handle)
    handle.close()
  
  variables = {}
  print opt.variablesFile
  if os.path.exists(opt.variablesFile) :
    handle = open(opt.variablesFile,'r')
    exec(handle)
    handle.close()
    #in case some variables need a compiled function
    for variableName, variable in variables.iteritems():
      if variable.has_key('linesToAdd'):
        linesToAdd = variable['linesToAdd']
        for line in linesToAdd:
          ROOT.gROOT.ProcessLineSync(line)




  nuisances = {}
  if os.path.exists(opt.nuisancesFile) :
    handle = open(opt.nuisancesFile,'r')
    exec(handle)
    handle.close()
  
  
  # ~~~~
  factory.makeSuppressZeros( opt.inputFile ,opt.outputDirShape, cuts, samples, opt.inputDir, nuisances, variables)
  
  print '... and now closing ...'


