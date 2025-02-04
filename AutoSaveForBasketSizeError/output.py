import sys
from array import array
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.treeReaderArrayTools import setExtraBranch

_rootBranchType2PythonArray = { 'b':'B', 'B':'b', 'i':'I', 'I':'i', 'F':'f', 'D':'d', 'l':'L', 'L':'l', 'O':'B' }

class OutputBranch:
    def __init__(self, tree, name, rootBranchType, n=1, lenVar=None, title=None, limitedPrecision=False):
        n = int(n)
        self.buff   = array(_rootBranchType2PythonArray[rootBranchType], n*[0. if rootBranchType in 'FD' else 0])
        self.lenVar = lenVar
        self.n = n
        self.precision = ROOT.ReduceMantissaToNbitsRounding(limitedPrecision) if limitedPrecision and rootBranchType=='F' else lambda x : x
        #check if a branch was already there 
        existingBranch = tree.GetBranch(name)
        if (existingBranch):
          self.branch = existingBranch
          self.branch.SetAddress(self.buff)
        else:  
          if lenVar != None:
            self.branch = tree.Branch(name, self.buff, "%s[%s]/%s" % (name,lenVar,rootBranchType))
          elif n == 1:
            self.branch = tree.Branch(name, self.buff, name+"/"+rootBranchType)
          else:
            self.branch = tree.Branch(name, self.buff, "%s[%d]/%s" % (name,n,rootBranchType))
        if title: self.branch.SetTitle(title)

    def fill(self, val):
        #print "[jhchoi]fill2@outputbranch@output"
        if self.lenVar:
            if len(self.buff) < len(val): # realloc
                self.buff = array(self.buff.typecode, max(len(val),2*len(self.buff))*[0. if self.buff.typecode in 'fd' else 0])
                self.branch.SetAddress(self.buff)
            for i,v in enumerate(val): self.buff[i] = self.precision(v)
        elif self.n == 1: 
            self.buff[0] = self.precision(val)
        else:
            if len(val) != self.n: raise RuntimeError("Mismatch in filling branch %s of fixed length %d with %d values (%s)" % (self.Branch.GetName(),self.n,len(val),val))
            for i,v in enumerate(val): self.buff[i] = v
        #print "[jhchoi]end of fill2@outputbranch@output"
class OutputTree:
    def __init__(self, tfile, ttree, intree):
        self._file = tfile
        self._tree = ttree
        self._intree = intree
        self._branches = {} 
    def branch(self, name, rootBranchType, n=1, lenVar=None, title=None,limitedPrecision=False):
        if (lenVar != None) and (lenVar not in self._branches): #and (not self._tree.GetBranch(lenVar)):
            self._branches[lenVar] = OutputBranch(self._tree, lenVar, "i")
        self._branches[name] = OutputBranch(self._tree, name, rootBranchType, n=n, lenVar=lenVar, title=title,limitedPrecision=limitedPrecision)
        return self._branches[name]
    def fillBranch(self, name, val):
        br = self._branches[name]
        if br.lenVar and (br.lenVar in self._branches):
            self._branches[br.lenVar].buff[0] = len(val)
            setExtraBranch(self._intree,br.lenVar,len(val))
        br.fill(val)
        setExtraBranch(self._intree,name,val)
    def tree(self):
        return self._tree
    def fill(self):
        self._tree.Fill()
    def write(self):
        print "[jhchoi]write @OutputTree@output.py"
        print "autosave=",self._tree.GetAutoSave()
        print "[jhchoi]file.cd@write @OutputTree@output.py"
        self._file.cd()
        print "[jhchoi]_tree.write@write @OutputTree@output.py"
        print "autosave=",self._tree.GetAutoSave()

        ##---too slow!!---##
        print "Turn on AutoSave"
        print "self._tree.SetAutoSave()"
        self._tree.SetAutoSave()
        print "self._tree.AutoSave"
        self._tree.AutoSave("FlushBaskets")
        if self._tree.GetAutoSave() == 0:
            print "self._tree.GetAutoSave()=",self._tree.GetAutoSave()
            print "AutoSave is off. Start write"
            self._tree.Write()

class FullOutput(OutputTree):
    def __init__(
            self,
            inputFile,
            inputTree,
            outputFile,
            branchSelection=None,
            outputbranchSelection=None,
            fullClone=False,
            maxEntries=None,
            firstEntry=0,
            provenance=False,
            jsonFilter=None
    ):
        outputFile.cd()

        
        self.outputbranchSelection = outputbranchSelection
        self.maxEntries = maxEntries
        self.firstEntry = firstEntry
        if fullClone:
            outputTree = inputTree.CopyTree('1', "", maxEntries if maxEntries else ROOT.TVirtualTreePlayer.kMaxEntries, firstEntry)
        else:            
            outputTree = inputTree.CloneTree(0)
            
        # enable back all branches in inputTree, then disable for computation
        # the branches as requested in branchSelection
        inputTree.SetBranchStatus("*",1)
        if branchSelection:
            branchSelection.selectBranches(inputTree)

        OutputTree.__init__(self, outputFile, outputTree, inputTree)
        self._inputTree = inputTree
        self._otherTrees = {}
        self._otherObjects = {}
        for k in inputFile.GetListOfKeys():
            kn = k.GetName()
            if kn == "Events":
                continue # this we are doing
            elif kn in ("MetaData", "ParameterSets"):
                if provenance: self._otherTrees[kn] = inputFile.Get(kn).CopyTree('1' if firstEntry == 0 else '0') # treat content of other trees as if associated to event 0
            elif kn in ("LuminosityBlocks", "Runs"):
                if not jsonFilter: self._otherTrees[kn] = inputFile.Get(kn).CopyTree('1' if firstEntry == 0 else '0')
                elif firstEntry == 0:
                    _isRun = (kn=="Runs")
                    _it = inputFile.Get(kn)
                    _ot = _it.CloneTree(0)
                    for ev in _it:
                        if (jsonFilter.filterRunOnly(ev.run) if _isRun else jsonFilter.filterRunLumi(ev.run,ev.luminosityBlock)): _ot.Fill()
                    self._otherTrees[kn] = _ot
            elif k.GetClassName() == "TTree":
                print "Not copying unknown tree %s" % kn
            else:
                self._otherObjects[kn] = inputFile.Get(kn)
    def fill(self):
        #print "[jhchoi]fill@Fulloutput@output"
        self._inputTree.readAllBranches()
        self._tree.Fill()
        #print "[jhchoi]end of fill@Fulloutput@output"
    def write(self):
        #print >> sys.stderr, "[jhchoi]write@Fulloutput@output"
        print "[jhchoi]write@Fulloutput@output"
        print "autosave=",self._tree.GetAutoSave()
        if self.outputbranchSelection:
            self.outputbranchSelection.selectBranches(self._tree)
            print "[jhchoi]outputbranch selection end write@Fulloutput@output"
        print >> sys.stderr, "[jhchoi]start tree copy write@Fulloutput@output"
        print "autosave=",self._tree.GetAutoSave()
        print "autosave before copytree"
        self._tree.AutoSave("FlushBaskets")
        self._tree = self.tree().CopyTree('1', "", self.maxEntries if self.maxEntries else ROOT.TVirtualTreePlayer.kMaxEntries, self.firstEntry)
        print "autosave=",self._tree.GetAutoSave()
        print "[jhchoi]end tree copy write@Fulloutput@output"
        print "[jhchoi]outputtree.write tree copy write@Fulloutput@output"

        OutputTree.write(self)
        print "[jhchoi]end of outputtree.write tree copy write@Fulloutput@output"
        print "autosave=",self._tree.GetAutoSave()

        print >> sys.stderr, "[jhchoi]iteration of trees writing"

        for t in self._otherTrees.itervalues():
            t.Write()
        print >> sys.stderr, "[jhchoi]end of iteration of trees"


        print >> sys.stderr, "[jhchoi]start write other object write@Fulloutput@output"

        for on,ov in self._otherObjects.iteritems():
            self._file.WriteTObject(ov,on)
        print >> sys.stderr, "[jhchoi]end of write @fulloutput@output"
class FriendOutput(OutputTree):
    def __init__(self, inputFile, inputTree, outputFile, treeName="Friends"):
        outputFile.cd()
        outputTree = ROOT.TTree(treeName,"Friend tree for "+inputTree.GetName())
        OutputTree.__init__(self, outputFile, outputTree, inputTree)

