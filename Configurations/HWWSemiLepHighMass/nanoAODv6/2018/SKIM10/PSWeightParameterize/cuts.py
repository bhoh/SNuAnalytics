ONLY_FINAL=True

import os
import sys
sys.path.append(os.getcwd())

print "ONLY_FINAL=",ONLY_FINAL
#-----Variable Deinition-----#
from WPandCut2018 import *

#cuts={}




supercut = '1'


##---Lepton Categorization---##
cuts['nocut']='1'
cuts['0cj']='nCleanGenJet==0'
cuts['1cj']='nCleanGenJet==1'
cuts['2cj']='nCleanGenJet==2'
cuts['3cj']='nCleanGenJet>=3'
#cuts['4cj']='nCleanGenJet==4'
#cuts['5cj']='nCleanGenJet==5'
#cuts['6cj']='nCleanGenJet>=6'

cuts['0j']='nGenJet==0'
cuts['1j']='nGenJet==1'
cuts['2j']='nGenJet==2'
cuts['3j']='nGenJet>=3'
#cuts['4j']='nGenJet==4'
#cuts['5j']='nGenJet==5'
#cuts['6j']='nGenJet>=6'

##---End of Boosted


print "Ncuts=",len(cuts)

