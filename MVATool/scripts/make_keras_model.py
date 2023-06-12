
import os, sys
from variables import Variables
from options import *
try:
  from MLTools_ttToHplus import MLTools
  from TMVATools_ttToHplus import TMVATools
except ImportError:
  CMSSW     = os.environ["CMSSW_BASE"]
  BASE_PATH = CMSSW + "/src/SNuAnalytics/MVATool/python/"
  sys.path.append(BASE_PATH)
  from MLTools_ttToHplus import MLTools
  from TMVATools_ttToHplus import TMVATools

from KerasModel_ttToHplus import KerasModel
#from KerasModel_ttToHplus_conv import KerasModel
#from KerasModel_ttToHplus_conv_res_test import KerasModel

os.system("mkdir -p cms_scratch/bhoh/mva")

for option_key in options.keys():

  mvaVars = Variables()
  for key in options[option_key]['variables']:
    setattr(mvaVars, key, options[option_key]['variables'][key])
  print(len(mvaVars.getVariables().keys()))
  if 'DNN' not in option_key:
    continue
  m = options[option_key]['model']()
  m.defineModel_3layer(len(mvaVars.getVariables().keys()))
  m.compile()
  m.save("/cms_scratch/bhoh/mva/model_{OPTION}.h5".format(OPTION=option_key))
  m.summary()
