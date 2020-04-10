

##1) Too flush basket every 10000events, add following lines to your analyze function. 
###Example) LeptonSFMaker.py
if event.event % 10000 ==1 :##To flush memory of ttree                                                                                                                    
            #self.out._tree.AutoSave("FlushBaskets")                                                                                                                              
            self.out._tree.AutoSave("FlushBaskets")

##2) Then, go to nanoTools
##${CMSSW_BASE}/src/PhysicsTools/NanoAODTools/python/postprocessing/framework/output.py
## def write(self) of class OutputTree,
#find "self._tree.Write()"
#replace it to following lines


 
        self._tree.SetAutoSave()
        print "self._tree.AutoSave"
        self._tree.AutoSave("FlushBaskets")
        if self._tree.GetAutoSave() == 0:
            print "self._tree.GetAutoSave()=",self._tree.GetAutoSave()
            print "AutoSave is off. Start write"
            self._tree.Write()
