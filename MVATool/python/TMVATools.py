from ROOT import TFile, TTree, TCut, TMVA, gROOT

try:
    from MLTools import MLTools
    from KerasModel import KerasModel
except ImportError:
    import os 
    CMSSW     = os.environ["CMSSW_BASE"]
    BASE_PATH = CMSSW + "/src/SNuAnalytics/MVATool/python/"
    sys.path.append(BASE_PATH)
    from KerasModel import KerasModel
    from MLTools import MLTools


#------
# ver.1
#-----
# what to imporve:
# 3 class of cfgs factory, prepare trees, book MVA methods
# apply weights

class TMVATools(MLTools):

  def __init__(self, cfgs):
    MLTools.__init__(self, cfgs)
    print """
  _    _  _____ _____ _   _  _____   _______ __  ____      __     
 | |  | |/ ____|_   _| \ | |/ ____| |__   __|  \/  \ \    / /\    
 | |  | | (___   | | |  \| | |  __     | |  | \  / |\ \  / /  \   
 | |  | |\___ \  | | | . ` | | |_ |    | |  | |\/| | \ \/ / /\ \  
 | |__| |____) |_| |_| |\  | |__| |    | |  | |  | |  \  / ____ \ 
  \____/|_____/|_____|_| \_|\_____|    |_|  |_|  |_|   \/_/    \_\
	   """ 
			                                  
    gROOT.SetBatch()
    TMVA.Tools.Instance()
    TMVA.PyMethodBase.PyInitialize()
    #print 'TMVATools:',self._cfgs['bookMethod']
    for method in self._cfgs['bookMethod']:
      if self._cfgs['bookMethod'][method]['type'] == TMVA.Types.kPyKeras:
	self.KerasModelComile()


  def KerasModelComile(self):
    print 'Keras is included, making a model compiled'
    myK = KerasModel()
    n_InputNodes   = self._cfgs['bookMethod']['Keras']['n_InputNodes']
    n_HiddenNodes  = self._cfgs['bookMethod']['Keras']['n_HiddenNodes']
    n_HiddenLayers = self._cfgs['bookMethod']['Keras']['n_HiddenLayers']
    hiddenActiv    = self._cfgs['bookMethod']['Keras']['hidden_Activation']
    outActiv       = self._cfgs['bookMethod']['Keras']['out_Activation']
    lossftn_x      = self._cfgs['bookMethod']['Keras']['lossftn']
    SGD_lr_x       = self._cfgs['bookMethod']['Keras']['SGD_lr']
    SGD_decay_x    = self._cfgs['bookMethod']['Keras']['SGD_decay']
    metrix_x       = self._cfgs['bookMethod']['Keras']['metrix']

    print 'InputNodes, HiddenNodes, HiddenLayers, Activation', n_InputNodes, n_HiddenNodes, n_HiddenLayers, hiddenActiv, outActiv
    #setHiddenLayers(self, n_Nodes_Input, n_Nodes_Hidden, n_hidden_Layers, activ='relu', l2_val = 1e-5)
    myK.setHiddenLayers( n_InputNodes, n_HiddenNodes, n_HiddenLayers, activ=hiddenActiv)
    ## Ouput layer
    # NOTE: Use following output types for the different tasks
    # Binary classification: 2 output nodes with 'softmax' activation
    # Regression: 1 output with any activation ('linear' recommended)
    # Multiclass classification: (number of classes) output nodes with 'softmax' activation
    #setOutLayer(self, n_Nodes_Out, activ = 'softmax')
    myK.setOutLayer(2, activ = outActiv)
    # Compile model
    # NOTE: Use following settings for the different tasks
    # Any classification: 'categorical_crossentropy' is recommended loss function
    # Regression: 'mean_squared_error' is recommended loss function
    myK.compile(lossftn= lossftn_x,
                     SGD_lr= SGD_lr_x, SGD_decay= SGD_decay_x,
                     metrix= metrix_x
                                    )
    #print 'save model'
    self.KerasModelName = self._cfgs['bookMethod']['Keras']['name']
    self.KerasModelName += '.h'+str(n_HiddenLayers)
    myK.save(self.KerasModelName)
    #myK.save("model.h5")
    #print 'summary'
    myK.summary()
    #print 'plot model' # This is not working at KISTI.....
    #myK.plot_mymodel("mymodelPlot.png")
    #outName = 'out_train_%s.root'% label

  #def SetConfig(self,cfgs):
  #  self._cfgs = cfgs


  def _setFactory(self,outFileName):
    print 'OutFileName', outFileName
    self._fout = TFile(outFileName,"RECREATE")
    self._factory = TMVA.Factory(self._cfgs['factory']['name'],
		                 self._fout,
				 self._cfgs['factory']['options']
                                )


  def _dataLoader(self,sigTreeNames,bkgTreeNames):
    self._data_loader = TMVA.DataLoader(self._cfgs['factory']['name'])

    for value in self._variables.values():
      self._data_loader.AddVariable(value['definition'],value['type'])

    for value in self._spectators.values():
      print 'spectator added:', value['definition']
      self._data_loader.AddSpectator(value['definition'])

    #----
    for sigTreeName in sigTreeNames:
      if "_Train" in sigTreeName:
        self._data_loader.AddSignalTree(self._trees[sigTreeName],1.0,"train")
      elif "_Test" in sigTreeName:
        self._data_loader.AddSignalTree(self._trees[sigTreeName],1.0,"test")
      else:
        #self._data_loader.AddSignalTree(self._trees[sigTreeName],1.0,"train_test")
        self._data_loader.AddTree(self._trees[sigTreeName],"Signal",1.0,"EventNum_mvaCHToCB%100<70", "train")#TMVA.Types.kTraining)
        self._data_loader.AddTree(self._trees[sigTreeName],"Signal",1.0,"EventNum_mvaCHToCB%100>=70","test")#TMVA.Types.kTesting)
        #raise Exception("[TMVATools.py] raise exception at _dataLoase")

    for bkgTreeName in bkgTreeNames:
      if "_Train" in bkgTreeName:
        self._data_loader.AddBackgroundTree(self._trees[bkgTreeName],1.0,"train")
      elif "_Test" in bkgTreeName:
        self._data_loader.AddBackgroundTree(self._trees[bkgTreeName],1.0,"test")
      else:
        #self._data_loader.AddBackgroundTree(self._trees[bkgTreeName],1.0,"train_test")
        self._data_loader.AddTree(self._trees[sigTreeName],"Background",1.0,"EventNum_mvaCHToCB%100<70", "train")#TMVA.Types.kTraining)
        self._data_loader.AddTree(self._trees[sigTreeName],"Background",1.0,"EventNum_mvaCHToCB%100>=70","test")#TMVA.Types.kTesting)
        #raise Exception("[TMVATools.py] raise exception at _dataLoase")

    self._data_loader.SetSignalWeightExpression(self._cfgs['factory']['weight'])
    self._data_loader.SetBackgroundWeightExpression(self._cfgs['factory']['weight'])

    self._data_loader.PrepareTrainingAndTestTree(TCut(self._cuts['sig']),
		                                TCut(self._cuts['bkg']),
                                                self._cfgs['prepareTrees']
			        	       )


  def _bookMethod(self):
    for method in self._cfgs['bookMethod']:
      if self._cfgs['bookMethod'][method]['type'] == TMVA.Types.kPyKeras:
        self._factory.BookMethod(self._data_loader,
	  	               self._cfgs['bookMethod'][method]['type'],
		               self._cfgs['bookMethod'][method]['name'],
			       self._cfgs['bookMethod'][method]['options']+':FilenameModel='+self.KerasModelName
			       )
      else:
        self._factory.BookMethod(self._data_loader,
	  	               self._cfgs['bookMethod'][method]['type'],
		               self._cfgs['bookMethod'][method]['name'],
			       self._cfgs['bookMethod'][method]['options']
			       )
      #self._factory.IgnoreEventsWithNegWeightsInTraining() not working, not this way TODO

  def doTrain(self, sigTreeNameList, bkgTreeNameList, outWeightsSuffix, outFileName, epoch=1):
    #if self._debug:
    #  print "doTrain: sigSampleList, bkgSampleList",sigTreeNameList, bkgTreeNameList
    self._setFactory(outFileName)
    self._dataLoader(sigTreeNameList, bkgTreeNameList)
    self._bookMethod()
    self._factory.TrainAllMethods()
    self._factory.TestAllMethods()
    self._factory.EvaluateAllMethods()
    self._getSignalReferenceCut(outWeightsSuffix)
    self._fout.Close()


  def doTest(self):
    pass

  def _getSignalReferenceCut(self,outWeightsSuffix):
    fOut = open('signal_reference_cut.txt','w')
    for method in self._cfgs['bookMethod']:
      cut = self._factory.GetMethod(self._cfgs['factory']['name'], self._cfgs['bookMethod'][method]['name']).GetSignalReferenceCut() # minimum requirement on the MVA output to declare an event signal-like
      out = "%s_%s		%s\n"%(self._cfgs['bookMethod'][method]['name'],outWeightsSuffix,cut)
      fOut.write(out)

    fOut.close()
