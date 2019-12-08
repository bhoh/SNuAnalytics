import ROOT

class TakeFileHisto:
  def __init__(self, filename):
      self.filename = filename
      try:
          print 'opening', filename
          self.file = ROOT.TFile.Open(filename,'read')
      except Exception as err:
          print 'Um problem opening',filename
          print err
          exit()
        
  def getHisto(self, histName):
      try:
          hist = self.file.Get(histName)
      except Exception as err:
          print 'Um problem getting',histName
          print err
          exit()
      if hist:
          return hist
      else:
          raise RuntimeError('Unable to retrieve histogram named {0} from {1}'.format(histName, self.filename))
