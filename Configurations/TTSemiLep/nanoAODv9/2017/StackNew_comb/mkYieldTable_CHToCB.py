import ROOT

#!/usr/bin/env python

import json
import sys
argv = sys.argv
sys.argv = argv[:1]
import ROOT
import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools
import logging
import collections
import os.path
import shutil

# Common Tools & batch
from LatinoAnalysis.Tools.commonTools import *

class YieldTableFactory:

    def __init__(self):
        pass


    def makeYieldTable( self, inputFile, outputDirYieldTable, variables, cuts, samples, structureFile, nuisances, plot, groupPlot):
        # categorize the sample names
        signal_ids = collections.OrderedDict() # id map of alternative_signals + cumulative_signals
        alternative_signals = ['']
        cumulative_signals = []
        data = []
        background_ids = collections.OrderedDict()
        
        # divide the list of samples among signal, background and data
        isig = 0
        ibkg = 1
        for sampleName in plot.keys() + groupPlot.keys():
          if sampleName not in structureFile:
            continue

          if structureFile[sampleName]['isSignal'] != 0:
            signal_ids[sampleName] = isig
            isig -= 1
          if structureFile[sampleName]['isSignal'] == 2 :
            alternative_signals.append(sampleName)
          if structureFile[sampleName]['isSignal'] == 1 :
            cumulative_signals.append(sampleName)
          if structureFile[sampleName]['isData'] == 1 :
            data.append(sampleName)
          if structureFile[sampleName]['isSignal'] == 0 and structureFile[sampleName]['isData'] == 0:
            background_ids[sampleName] = ibkg
            ibkg += 1

        print "Number of Signals:             " + str(len(signal_ids))
        print "Number of Alternative Signals: " + str(len(alternative_signals) - 1)
        print "Number of Cumulative Signals:  " + str(len(cumulative_signals))
        print "Number of Backgrounds:         " + str(len(background_ids))

        if not os.path.isdir(outputDirYieldTable + "/") :
          os.mkdir(outputDirYieldTable + "/")

        def getSubLists(input_list, key):
          sublists = []                                                             
          for name in input_list:
            if key in input_list[name]:
              for suffix in input_list[name][key]:
                subListName = (name,suffix)
                sublists.append(subListName)
            else:
              sublists.append((name,None))
          return sublists

        for cut, cat in getSubLists(cuts,'categories') :
          cutName = cut if cat==None else cut +'_'+ cat 
          print "cut = ", cutName
          try:
            shutil.rmtree(outputDirYieldTable + "/" + cutName)
          except OSError:
            pass
          os.mkdir(outputDirYieldTable + "/" + cutName)
          
          #
          # prepare the signals and background list of samples
          # after removing the ones not to be used in this specific phase space
          #
          cut_signals = []
          cut_backgrounds = []
          for snameList, idmap in [(cut_signals, signal_ids), (cut_backgrounds, background_ids)]:
            for sampleName in idmap:
              if 'removeFromCuts' in structureFile[sampleName] and cutName in structureFile[sampleName]['removeFromCuts']:
                # remove from the list
                print ' remove ', sampleName, ' from ', cutName
              else:
                snameList.append(sampleName)

          print "  sampleNames = ", cut_signals + cut_backgrounds
          
          # loop over variables
          for variableName, variable in variables.iteritems():
            if 'cuts' in variable and cut not in variable['cuts']:
              continue
              
            print "  variableName = ", variableName
            tagNameToAppearInDatacard = cutName
            # e.g.    hww2l2v_13TeV_of0j
            #         to be defined in cuts.py

            os.mkdir(outputDirYieldTable + "/" + cutName + "/" + variableName) 
            os.mkdir(outputDirYieldTable + "/" + cutName + "/" + variableName + "/shapes/") # and the folder for the root files 

            if os.path.isdir(inputFile):
              # ONLY COMPATIBLE WITH OUTPUTS MERGED TO SAMPLE LEVEL!!
              self._fileIn = {}
              for sampleName in samples:
                self._fileIn[sampleName] = ROOT.TFile.Open(inputFile+'/plots_%s_ALL_%s.root' % (self._tag, sampleName))
                if not self._fileIn[sampleName]:
                  raise RuntimeError('Input file for sample ' + sampleName + ' missing')
            else:
              self._fileIn = ROOT.TFile(inputFile, "READ")

            # prepare yields
            yieldsSig  = {}
            yieldsBkg  = {}
            yieldsData = {}

            # Bin to be killed
            #killBinSig = {}
            #killBinBkg = {}

            for snameList, yields in [(cut_signals, yieldsSig), (cut_backgrounds, yieldsBkg), (data, yieldsData)]:
              FlagIdx_data = 0
              for sampleName in snameList:
                if sampleName in groupPlot:
                  FlagIdx = 0
                  for subSample in groupPlot[sampleName]['samples']:
                    #print 'for',subSample,'in groupPlot'
                    if FlagIdx ==0:
                      histo = self._getHisto(cutName, variableName, subSample)
                    else:
                      histo_tmp = self._getHisto(cutName, variableName, subSample)
                      print 'adding', subSample,'to',sampleName
                      histo.Add(histo_tmp)
                    FlagIdx +=1
                  histo.SetName('histo_%s' %(sampleName))
                else:
                  histo = self._getHisto(cutName, variableName, sampleName)
                                                                                                                        
                # get the integral == rate from histogram
                if structureFile[sampleName]['isData'] == 1:
                  if FlagIdx_data == 0:
                    yields['data'] = histo.Integral()
                    histo.SetName("histo_Data")
                    FlagIdx_data += 1
                  else:
                    print 'There should be one data defined, exiting...................'
                    exit()
                else:
                   #if 'removeNegNomVal' in structureFile[sampleName] and structureFile[sampleName]['removeNegNomVal'] :
                   #  for iBin in range(0,histo.GetNbinsX()+2) :
                   #    BinContent = histo.GetBinContent(iBin)
                   #    if BinContent < 0.1 and not BinContent == 0:
                   #      print 'Killing Bin :' , sampleName , iBin , BinContent
                   #      if not sampleName in killBinSig : killBinSig[sampleName] = []
                   #      killBinSig[sampleName].append(iBin)
                   #      histo.SetBinContent(iBin,0.)
                    
                  yields[sampleName] = histo.Integral()
                                                                                                                        

            # Loop over alternative signal samples. One card per signal (there is always at least one entry (""))
            for signalName in alternative_signals:
              if signalName == '':
                signals = [name for name in cumulative_signals if name in cut_signals]
              else:
                if signalName not in cut_signals:
                  continue
                  
                signals = [signalName] + [name for name in cumulative_signals if name in cut_signals]

              processes = signals + cut_backgrounds
             
              print "    Alternative signal: " + str(signalName)
              alternativeSignalName  = str(signalName)
              alternativeSignalTitle = ""
              if alternativeSignalName != "":
                alternativeSignalTitle = "_" + str(signalName)

              # start creating the datacard 
              cardPath = outputDirYieldTable + "/" + cutName + "/" + variableName  + "/datacard" + alternativeSignalTitle + ".txt"
              print '    Writing to ' + cardPath 
              card = open( cardPath ,"w")

              print '      headers..'
              card.write('## Shape input card\n')
        
              if len(data) == 0:
                self._logger.warning( 'no data, no fun! ')
                #raise RuntimeError('No Data found!')
                yieldsData['data'] = 0

              card.write('observation %.0f\n' % yieldsData['data'])
            
              columndef = 30

              # adapt column length to long bin names            
              if len(tagNameToAppearInDatacard) >= (columndef -5) :
                columndef = len(tagNameToAppearInDatacard) + 7

              for name in signals :
                if len(name)>= (columndef -5) :
                    columndef = len(name) + 7


              print '      processes and rates..'
            
              card.write('bin'.ljust(80))
              card.write(''.join([tagNameToAppearInDatacard.ljust(columndef)] * (len(signals) + len(cut_backgrounds)))+'\n')
            
              card.write('process'.ljust(80))
              card.write(''.join(name.ljust(columndef) for name in signals))
              card.write(''.join(name.ljust(columndef) for name in cut_backgrounds))
              card.write('\n')

              card.write('process'.ljust(80))
              card.write(''.join(('%d' % signal_ids[name]).ljust(columndef) for name in signals))
              card.write(''.join(('%d' % background_ids[name]).ljust(columndef) for name in cut_backgrounds))
              card.write('\n')

              card.write('rate'.ljust(80))
              card.write(''.join(('%-.4f' % yieldsSig[name]).ljust(columndef) for name in signals))
              card.write(''.join(('%-.4f' % yieldsBkg[name]).ljust(columndef) for name in cut_backgrounds))
              card.write('\n')

              card.write('-'*100+'\n')

              print '      nuisances..'

              nuisanceGroups = collections.defaultdict(list)

              # add normalization and shape nuisances
              for nuisanceName, nuisance in nuisances.iteritems():
                if 'type' not in nuisance:
                  raise RuntimeError('Nuisance ' + nuisanceName + ' is missing the type specification')

                if nuisanceName == 'stat' or nuisance['type'] == 'rateParam':
                  # will deal with these later
                  continue

                # check if a nuisance can be skipped because not in this particular cut
                if 'cuts' in nuisance and cutName not in nuisance['cuts']:
                  continue

                if nuisance['type'] in ['lnN', 'lnU']:
                  entryName = nuisance['name']
                  card.write(entryName.ljust(80-20))
                  card.write((nuisance['type']).ljust(20))
                  if 'all' in nuisance and nuisance ['all'] == 1: # for all samples
                    card.write(''.join(('%-.4f' % nuisance['value']).ljust(columndef) for _ in processes))
                  else:
                    # apply only to selected samples
                    for sampleName in processes:
                      if sampleName in nuisance['samples']:
                        # in this case nuisance['samples'] is a dict mapping sample name to nuisance values in string
                        card.write(('%s' % nuisance['samples'][sampleName]).ljust(columndef))
                      else:
                        card.write(('-').ljust(columndef))


                if nuisance['type'] in ['shape','shapeN']:
                  #
                  # 'skipCMS' is a flag not to introduce "CMS" automatically in the name
                  #      of the nuisance.
                  #      It may be needed for combination purposes with ATLAS
                  #      and agreed upon for all CMS analyses.
                  #      For example: theoretical uncertainties on ggH with migration scheme 2017
                  #
                  if 'skipCMS' in nuisance and nuisance['skipCMS'] == 1:
                    entryName = nuisance['name']
                  else:
                    entryName = 'CMS_' + nuisance['name']

                  card.write(entryName.ljust(80-20))

                  print ">>>>>", nuisance['name'], " was derived as a shape uncertainty but is being treated as a lnN"
                  card.write(('lnN').ljust(20))
                  for sampleName in processes:
                    if ('all' in nuisance and nuisance['all'] == 1) or \
                            ('samples' in nuisance and sampleName in nuisance['samples']):
                      if sampleName in groupPlot:                                                                             
                        subIdx = 0
                        for subSample in groupPlot[sampleName]['samples']:
                          if subIdx == 0:
                            histo = self._getHisto(cutName, variableName, subSample)
                            if subSample in nuisance['samples']:
                              histoUp = self._getHisto(cutName, variableName, subSample, '_' + nuisance['name'] + 'Up') 
                              histoDown = self._getHisto(cutName, variableName, subSample, '_' + nuisance['name'] + 'Down')
                            else:
                              histoUp   = self._getHisto(cutName, variableName, subSample)
                              histoDown = self._getHisto(cutName, variableName, subSample)
                          else:
                            histo_tmp = self._getHisto(cutName, variableName, subSample)
                            if subSample in nuisance['samples']:
                              histoUp_tmp = self._getHisto(cutName, variableName, subSample, '_' + nuisance['name'] + 'Up') 
                              histoDown_tmp = self._getHisto(cutName, variableName, subSample, '_' + nuisance['name'] + 'Down')
                            else:
                              histoUp_tmp   = self._getHisto(cutName, variableName, subSample) 
                              histoDown_tmp = self._getHisto(cutName, variableName, subSample)
                            histo.Add(histo_tmp)
                            histoUp.Add(histoUp_tmp) 
                            histoDown.Add(histoDown_tmp)
                          subIdx += 1
                        histo.SetName('histo_%s' %(sampleName))
                        histoUp.SetName('histo_%s' %(sampleName+'_'+nuisance['name']+'Up')) 
                        histoDown.SetName('histo_%s' %(sampleName+'_'+nuisance['name']+'Down'))
                      else:
                        histo = self._getHisto(cutName, variableName, sampleName)
                        histoUp = self._getHisto(cutName, variableName, sampleName, '_' + nuisance['name'] + 'Up') 
                        histoDown = self._getHisto(cutName, variableName, sampleName, '_' + nuisance['name'] + 'Down')
                                                                                                                              
                      if (not histoUp or not histoDown):
                        print '########################################################################'
                        print 'Histogram for nuisance', nuisance['name'], 'on sample', sampleName, 'missing'
                        print '########################################################################'
                                                                                                                              
                        if self._skipMissingNuisance:
                          card.write(('-').ljust(columndef)) 
                          continue
                        else:
                          print 'Exiting....................................'
                          exit()


                      histoIntegral = histo.Integral()
                      histoUpIntegral = histoUp.Integral()
                      histoDownIntegral = histoDown.Integral()
                      if histoIntegral > 0. and histoUpIntegral > 0.:
                        diffUp = (histoUpIntegral - histoIntegral)/histoIntegral
                      else: 
                        diffUp = 0.

                      if histoIntegral > 0. and histoDownIntegral > 0.:
                        diffDo = (histoDownIntegral - histoIntegral)/histoIntegral
                      else:
                        diffDo = 0.

                      if 'symmetrize_syst' in nuisance and nuisance['symmetrize_ttsyst']:
                        diff = (diffUp - diffDo) * 0.5
                        if diff >= 1.:
                            # can't symmetrize
                            diffUp = diff * 2. - 0.999
                            diffDo = -0.999
                        elif diff <= -1.:
                            diffUp = -0.999
                            diffDo = -diff * 2. - 0.999
                        else:
                            diffUp = diff
                            diffDo = -diff
        
                      lnNUp = 1. + diffUp
                      lnNDo = 1. + diffDo

                      #  
                      # avoid 0.00/XXX and XXX/0.00 in the lnN --> ill defined nuisance
                      # if this happens put 0.00 ---> 1.00, meaning *no* effect of this nuisance
                      #              Done like this because it is very likely what you are experiencing 
                      #              is a MC fluctuation in the varied sample, that is the up/down histogram has 0 entries!
                      #
                      #              NB: with the requirement "histoUpIntegral > 0" and "histoDownIntegral > 0" this should never happen, 
                      #                  except for some strange coincidence of "AsLnN" ... 
                      #                  This fix is left, just for sake of safety
                      #
                      if lnNUp==0: lnNUp = 1.
                      if lnNDo==0: lnNDo = 1.

                      if abs(lnNUp - 1.) < 5.e-4 and abs(lnNDo - 1.) < 5.e-4:
                        card.write(('-').ljust(columndef))
                      else:
                        card.write((('%-.4f' % lnNUp)+"/"+('%-.4f' % lnNDo)).ljust(columndef))
                    else:
                      card.write(('-').ljust(columndef)) 

                  
                # closing block if type == lnN or shape
                card.write('\n')

                if 'group' in nuisance:
                  nuisanceGroups[nuisance['group']].append(entryName)

              for group in sorted(nuisanceGroups.iterkeys()):
                card.write('%s group = %s\n' % (group, ' '.join(nuisanceGroups[group])))

              card.write('\n')
              card.close()
    # _____________________________________________________________________________
    def _getHisto(self, cutName, variableName, sampleName, suffix = None):
        shapeName = '%s/%s/histo_%s' % (cutName, variableName, sampleName)
        if suffix:
            shapeName += suffix

        if type(self._fileIn) is dict:
            # by-sample ROOT file
            histo = self._fileIn[sampleName].Get(shapeName)
        else:
            # Merged single ROOT file
            histo = self._fileIn.Get(shapeName)

        if not histo:
            print shapeName, 'not found'

        self._fixNegativeBinAndError(histo)
      
        return histo

    def _fixNegativeBinAndError(self, histogram_to_be_fixed):
        # if a histogram has a bin < 0
        # then put the bin content to 0
        # and also if a histogram has uncertainties that go <0,
        # then put the uncertainty to the maximum allowed
  
        for ibin in range(1, histogram_to_be_fixed.GetNbinsX()+1) :
            if histogram_to_be_fixed.GetBinContent(ibin) < 0 :
                histogram_to_be_fixed.SetBinContent(ibin, 0) 
  
        # the SetBinError does not allow asymmetric -> fine, maximum uncertainty set
        for ibin in range(1, histogram_to_be_fixed.GetNbinsX()+1) :
            if histogram_to_be_fixed.GetBinContent(ibin) - histogram_to_be_fixed.GetBinErrorLow(ibin) < 0 :
                histogram_to_be_fixed.SetBinError(ibin, histogram_to_be_fixed.GetBinContent(ibin)) 


if __name__ == '__main__':
    sys.argv = argv
    
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--tag'                , dest='tag'               , help='Tag used for the shape file name'           , default=None)
    parser.add_option('--sigset'             , dest='sigset'            , help='Signal samples [SM]'                        , default='SM')
    parser.add_option('--outputDirYieldTable'  , dest='outputDirYieldTable' , help='output directory'                           , default='./')
    parser.add_option('--inputFile'          , dest='inputFile'         , help='input directory'                            , default='./input.root')
    parser.add_option('--structureFile'      , dest='structureFile'     , help='file with datacard configurations'          , default=None )
    parser.add_option('--nuisancesFile'      , dest='nuisancesFile'     , help='file with nuisances configurations'         , default=None )
    parser.add_option('--cardList'           , dest="cardList"          , help="List of cuts to produce datacards"          , default=[], type='string' , action='callback' , callback=list_maker('cardList',','))
    parser.add_option('--skipMissingNuisance', dest='skipMissingNuisance', help="Don't write nuisance lines when histograms are missing", default=False, action='store_true')
          
    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()


    print " configuration file = ", opt.pycfg
    
    print " inputFile =                  ", opt.inputFile
    print " outputDirYieldTable =          ", opt.outputDirYieldTable
 
    if not opt.debug:
      pass
    elif opt.debug == 2:
      print 'Logging level set to DEBUG (%d)' % opt.debug
      logging.basicConfig( level=logging.DEBUG )
    elif opt.debug == 1:
      print 'Logging level set to INFO (%d)' % opt.debug
      logging.basicConfig( level=logging.INFO )

    if opt.nuisancesFile == None :
      print " Please provide the nuisances structure if you want to add nuisances "

    if opt.structureFile == None :
      print " Please provide the datacard structure "
      exit ()

    ROOT.TH1.SetDefaultSumw2(True)
      
    factory = YieldTableFactory()
    
    ## load the samples
    samples = {}
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()

    ## load the cuts
    cuts = {}
    if os.path.exists(opt.cutsFile) :
      handle = open(opt.cutsFile,'r')
      exec(handle)
      handle.close()

    ## load the variables
    variables = {}
    if os.path.exists(opt.variablesFile) :
      handle = open(opt.variablesFile,'r')
      exec(handle)
      handle.close()

    groupPlot = collections.OrderedDict()
    plot = {}
    legend = {}
    if os.path.exists(opt.plotFile) :
      handle = open(opt.plotFile,'r')
      exec(handle)
      handle.close()

    ## load the nuisances
    nuisances = collections.OrderedDict()
    if os.path.exists(opt.nuisancesFile) :
      handle = open(opt.nuisancesFile,'r')
      exec(handle)
      handle.close()

    import LatinoAnalysis.ShapeAnalysis.utils as utils

    subsamplesmap = utils.flatten_samples(samples)
    categoriesmap = utils.flatten_cuts(cuts)

    utils.update_variables_with_categories(variables, categoriesmap)
    utils.update_nuisances_with_subsamples(nuisances, subsamplesmap)
    utils.update_nuisances_with_categories(nuisances, categoriesmap)




    ## load the structure file (use flattened sample and cut names)
    structure = collections.OrderedDict()
    if os.path.exists(opt.structureFile) :
      handle = open(opt.structureFile,'r')
      exec(handle)
      handle.close()

    ## command-line cuts restrictions
    if len(opt.cardList)>0:
      try:
        newCuts = []
        for iCut in opt.cardList:
          for iOptim in optim:
            newCuts.append(iCut+'_'+iOptim)
        opt.cardList = newCuts
        print opt.cardList
      except:
        print "No optim dictionary"
      cut2del = []
      for iCut in cuts:
        if not iCut in opt.cardList : cut2del.append(iCut)
      for iCut in cut2del : del cuts[iCut]   
    
    factory.makeYieldTable( opt.inputFile, opt.outputDirYieldTable, variables, cuts, samples, structure, nuisances, plot, groupPlot)
