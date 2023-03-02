
from variables import Variables
from options import *
try:
  from MLTools_ttToHplus import MLTools
  from TMVATools_ttToHplus import TMVATools
except ImportError:
  import os, sys
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/MVATool/python/"
  sys.path.append(BASE_PATH)
  from MLTools_ttToHplus import MLTools
  from TMVATools_ttToHplus import TMVATools

from KerasModel_ttToHplus import KerasModel
#from KerasModel_ttToHplus_conv import KerasModel
#from KerasModel_ttToHplus_conv_res_test import KerasModel

for option_key in options.keys():

  mvaVars = Variables()
  for key in options[option_key]['variables']:
    setattr(mvaVars, key, options[option_key]['variables'][key])
  print(len(mvaVars.getVariables().keys()))
  m = KerasModel()
  m.defineModel_3layer(len(mvaVars.getVariables().keys()))
  m.compile()
  m.save("model_{OPTION}.h5".format(OPTION=option_key))
  m.summary()
