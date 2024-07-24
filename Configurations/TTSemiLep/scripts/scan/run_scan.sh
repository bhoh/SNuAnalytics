WS_NAME=../workspace/Asym_fitted_dijet_M_DNN/M080Y2016noHIPMY2017Y2016HIPMY2018.txt.root
JOB_NAME=M120Y2016Y2017Y2018
# --alignEdges 1
#  --setParameters BR=0.0001 -t -1
combineTool.py $WS_NAME -M MultiDimFit --algo grid --points 300 --autoRange 10 --fastScan --alignEdges 1 -t -1 --rMin -1 --robustFit 1 --setParameters BR=0.001,ttbbXsec=1.36
python plot1DScan_CHToCB.py higgsCombine.Test.MultiDimFit.mH120.root -o scan --POI=BR
