import os
import copy
import inspect
import numpy as np

##---WP2017---##
from WPandCut2018 import *


aliases['nCleanGenJet'] = {
    'linesToAdd': ['.L '+os.getcwd()+'/ngenjet.cc+'
    ],
    'class': 'CountGenJet',
}
