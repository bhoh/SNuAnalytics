
for year in 2016 2017 2018
#for year in 2018
  do
    for sig in High Low
    #for sig in High
      do
        suffix=${sig}_${year}
        XML_DIR=TMVAClassification_CHToCB_${suffix}/weights_CHToCB_${suffix}
        XML_PATH=${XML_DIR}/TMVAClassification_DNN.weights.xml
        echo ${XML_PATH}
        sed -i 's/MVATool\/scripts/NanoGardenerFrameworks\/CHToCB\/201209/g' ${XML_PATH}
        sed -i 's/TMVAClassification\/weights\/TrainedModel_DNN\.h5/TMVAClassification_CHToCB_'${suffix}'\/weights_CHToCB_'${suffix}'\/TrainedModel_DNN\.h5/g' ${XML_PATH}
        sed -i 's/TMVAClassification_CHToCB_'${suffix}'\/weights_CHToCB_'${suffix}'\/TrainedModel_DNN\.h5/\/cms\/ldap_home\/bhoh\/latinos\/CMSSW_10_6_4\/src\/SNuAnalytics\/NanoGardenerFrameworks\/CHToCB\/201209\/TMVAClassification_CHToCB_'${suffix}'\/weights_CHToCB_'${suffix}'\/TrainedModel_DNN\.h5/g' ${XML_PATH}
      done
  done
