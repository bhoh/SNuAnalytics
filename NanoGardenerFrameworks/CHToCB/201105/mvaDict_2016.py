import ROOT
from collections import OrderedDict
import os,sys

CMSSW     = os.environ["CMSSW_BASE"]
BASE_PATH = CMSSW + "/src/SNuAnalytics/MVATool/scripts/"
print(BASE_PATH)
sys.path.append(BASE_PATH)
from test_ttToHplus_catCut import variables


inputVars = OrderedDict()

for key in variables:
  definition = variables[key]['definition']
  if ':=' in definition:
    new_key = definition.split(' := ')[1]
    inputVars[new_key] = new_key
  else:
    inputVars[definition] = definition


print(inputVars)


mvaDic = { 
            'BDT_High' : {
                          'type'      : 'BDT::BDT_800_MinNodeSize2of10',  
                          'xmlFile'   : 'SNuAnalytics/NanoGardenerFrameworks/CHToCB/201105/TMVAClassification_CHToCB_High_2016/weights_CHToCB_High_2016/TMVAClassification_BDT_800_MinNodeSize2of10.weights.xml',
                          'inputVars' : inputVars,
                       } ,
           'DNN_High' : {
                          'type'      : 'PyKeras::DNN',  
                          'xmlFile'   : 'SNuAnalytics/NanoGardenerFrameworks/CHToCB/201105/TMVAClassification_CHToCB_High_2016/weights_CHToCB_High_2016/TMVAClassification_DNN.weights.xml',
                          'inputVars' : inputVars,
                       } ,
            'BDT_Low' : {
                          'type'      : 'BDT::BDT_800_MinNodeSize2of10',  
                          'xmlFile'   : 'SNuAnalytics/NanoGardenerFrameworks/CHToCB/201105/TMVAClassification_CHToCB_Low_2016/weights_CHToCB_Low_2016/TMVAClassification_BDT_800_MinNodeSize2of10.weights.xml',
                          'inputVars' : inputVars,
                       } ,
           'DNN_Low' : {
                          'type'      : 'PyKeras::DNN',  
                          'xmlFile'   : 'SNuAnalytics/NanoGardenerFrameworks/CHToCB/201105/TMVAClassification_CHToCB_Low_2016/weights_CHToCB_Low_2016/TMVAClassification_DNN.weights.xml',
                          'inputVars' : inputVars,
                       } ,
         }

print(mvaDic)
