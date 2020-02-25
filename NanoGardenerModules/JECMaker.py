from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jecUncertainties import jecUncertProducer 

class JECMaker(jecUncertProducer, object):
    '''
    Jet Energy Correction Module (running on CleanJet's)
    ''' 
    def __init__(self, globalTag, types=['Total'], jetFlav='AK4PFchs',jetCo="CleanJet"):
       super(JECMaker, self).__init__(globalTag, uncerts=types, jetFlavour=jetFlav, jetColl=jetCo) ##call parent class 
       types_str = 'CorrectionTypes = '
       for typ in types:
           types_str += typ
           types_str += ', '
       print('JECMaker: globaTag = ' + globalTag + ', ' + types_str + 'JetFlavour = ' + jetFlav)

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        print "beginFile JECMaker.py"
        oBrList = wrappedOutputTree._tree.GetListOfBranches()
        #print "--output branches--"
        #for br in oBrList:
        #    print br.GetName()
        #iBrList = inputTree.GetListOfBranches()
        #print "--input branches--"
        #for br in iBrList:
        #    print br.GetName()



        self.out = wrappedOutputTree
        for u,branchname in self.uncerts :
            print 'u=',u,'branchname=',branchname
            self.out.branch(branchname, "F", lenVar="n"+self.jetColl)

