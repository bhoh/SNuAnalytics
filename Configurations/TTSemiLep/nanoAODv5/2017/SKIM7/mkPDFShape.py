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

      outputDirPDF = {}
      self._outputDirPDF = outputDirPDF


    def makePDF(self, inputFile, outputDirPDF, cuts, samples, inputDir, nuisances, variables):
      self._cuts = cuts
      self._samples = samples
      self._variables = variables
      self._nuisances = nuisances
      self._outputDirPDF = outputDirPDF

      os.system ("mkdir " + outputDirPDF + "/")
      os.system ("cp " + inputFile + " " + outputDirPDF + "/results_unc.root" )
      fileIn = ROOT.TFile(inputFile, "READ")
      self._outFile = ROOT.TFile.Open( self._outputDirPDF + '/results_unc.root', 'UPDATE')

      for cutName in self._cuts :
        #print "cut = ", cutName, " :: ", cuts[cutName]
        for variableName in self._variables:
          #print "variable = ", variableName, " :: ", variables[variableName]
          for sampleName in self._samples:
            #print "sample = ", sampleName, " :: ", samples[sampleName]

            ### LHEScaleWeight ###
            if sampleName in nuisances['LHEScaleWeight']['samples']:
              histoNameNorm = '{CUT}/{VAR}/histo_{SAMPLE}'.format(CUT=cutName,
                                                                 VAR=variableName,
                                                                 SAMPLE=sampleName
                                                                )
              print histoNameNorm
              histoNorm = fileIn.Get(histoNameNorm)
              integralNorm = histoNorm.Integral()
              
              histoVar    = {}
              integralVar = {}
              diff_Plus  = -0.001
              diff_Minus = 0.001
              idxPlus = -1
              idxMinus = -1
              histoVar[-1] = histoNorm
              integralVar[-1] = integralNorm
              #for iVar in range(9):
              for iVar in [0,1,3,5,7,8]:
                histoNameVar  = '{CUT}/{VAR}/histo_{SAMPLE}_{NUIS}V{IDX}Var'.format(CUT=cutName,
                                                                                    VAR=variableName,
                                                                                    SAMPLE=sampleName,
                                                                                    NUIS=nuisances['LHEScaleWeight']['name'],
                                                                                    IDX=iVar
                                                                                   )
                histoVar_ =  fileIn.Get(histoNameVar)
                integralVar_ = histoVar_.Integral()
                histoVar[iVar] = histoVar_
                integralVar[iVar] = integralVar_

                diff = integralVar_ - integralNorm
                if diff > diff_Plus:
                  diff_Plus = diff
                  idxPlus = iVar
                if diff < diff_Minus:
                  diff_Minus = diff
                  idxMinus = iVar
              if idxPlus < 0 or idxMinus <0:
                print 'Something wrong in Scale variation'
                #exit()
              if not integralNorm==0:
                print 'Max Scale Up variation', diff_Plus/integralNorm, 'for',idxPlus
                print 'Max Scale Down variation', diff_Minus/integralNorm, 'for',idxMinus
              else:
                print 'Nnom is zero'
                pass
              self._outFile.cd('{CUT}/{VAR}'.format(CUT=cutName,VAR=variableName))
              histoNameUp  = 'histo_{SAMPLE}_{NUIS}Up'.format(SAMPLE=sampleName,
                                                              NUIS=nuisances['LHEScaleWeight']['name']
                                                             )
              histoNameDown = 'histo_{SAMPLE}_{NUIS}Down'.format(SAMPLE=sampleName,
                                                                 NUIS=nuisances['LHEScaleWeight']['name']
                                                                )

              histoUp = histoVar[idxPlus].Clone(histoNameUp)
              histoDown = histoVar[idxMinus].Clone(histoNameDown)
              histoUp.Write("",ROOT.TObject.kOverwrite)
              histoDown.Write("",ROOT.TObject.kOverwrite)
            ### END LHEScaleWeight ###

            ### LHEPdfWeight ###
            if sampleName in nuisances['LHEPdfWeight']['samples']:
              histoNameNorm = '{CUT}/{VAR}/histo_{SAMPLE}'.format(CUT=cutName,
                                                                 VAR=variableName,
                                                                 SAMPLE=sampleName
                                                                )
              print histoNameNorm
              histoNorm = fileIn.Get(histoNameNorm)
              histoCent = None
              NbinsX = histoNorm.GetNbinsX()
              print 'Total bin number',NbinsX
              BinVar =[0.]*NbinsX
              for iVar in range(len(nuisances['LHEPdfWeight']['samples'][sampleName])):
                histoNameVar  = '{CUT}/{VAR}/histo_{SAMPLE}_{NUIS}V{IDX}Var'.format(CUT=cutName,
                                                                                    VAR=variableName,
                                                                                    SAMPLE=sampleName,
                                                                                    NUIS=nuisances['LHEPdfWeight']['name'],
                                                                                    IDX=iVar
                                                                                   )
                histoVar_ = fileIn.Get(histoNameVar)
                if iVar == 0:
                  histoCent = histoVar_
                if not histoVar_:
                  print 'there is no',VariantName,'exiting......'
                  exit()
                for iBin in range(NbinsX):
                  central = histoCent.GetBinContent(iBin+1)
                  variant = histoVar_.GetBinContent(iBin+1)
                  #XXX HESSIAN
                  BinVar[iBin] = BinVar[iBin] + (central-variant)*(central-variant)
              LHEPdfNameUp   = 'histo_{SAMPLE}_{NUIS}Up'.format(SAMPLE=sampleName,
                                                                NUIS=nuisances['LHEPdfWeight']['name']
                                                               )
              LHEPdfNameDown = 'histo_{SAMPLE}_{NUIS}Down'.format(SAMPLE=sampleName,
                                                                NUIS=nuisances['LHEPdfWeight']['name']
                                                               )
              histoLHEPdfUp   = histoNorm.Clone(LHEPdfNameUp)
              histoLHEPdfDown = histoNorm.Clone(LHEPdfNameDown)

              for iBin in range(NbinsX):
                nominal = histoNorm.GetBinContent(iBin+1)
                central = histoCent.GetBinContent(iBin+1)
                if central != 0:
                  BinVarRate = math.sqrt(BinVar[iBin])/central
                  contentUp  = nominal*(1+BinVarRate)
                  contentDown  = nominal*(1-BinVarRate)
                else:
                  BinVarRate = math.sqrt(BinVar[iBin])
                  contentUp  = nominal + BinVarRate
                  contentDown  = nominal - BinVarRate
                print 'PDFError varRate for',iBin,'bin is',BinVarRate
                histoLHEPdfUp.SetBinContent(iBin+1, contentUp)
                histoLHEPdfDown.SetBinContent(iBin+1, contentDown)

              self._outFile.cd('{CUT}/{VAR}'.format(CUT=cutName,VAR=variableName))
              histoLHEPdfUp.Write("",ROOT.TObject.kOverwrite)
              histoLHEPdfDown.Write("",ROOT.TObject.kOverwrite)



      fileIn.Close()

if __name__ == '__main__':

  usage = 'usage: %prog [options]'
  parser = optparse.OptionParser(usage)
  
  parser.add_option('--outputDirPDF'   , dest='outputDirPDF'   , help='output directory for values and plots'           , default='./')
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
  print " outputDirPDF       = ", opt.outputDirPDF
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
  factory.makePDF( opt.inputFile ,opt.outputDirPDF, cuts, samples, opt.inputDir, nuisances, variables)
  
  print '... and now closing ...'


