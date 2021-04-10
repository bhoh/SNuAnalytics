export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch

PYTHON_TOOL_PATH=/cms/ldap_home/bhoh/latinos/jobs/python_tool/ExportShellCondorSetup.py
TARGET_PATH=${PWD}/$1
#CMD_TO_RUN='(cd '$TARGET_PATH') && (cd '$TARGET_PATH'; pwd)'
CMD_TO_RUN_DATA='(cd '$TARGET_PATH') && (hadd -j 10 hadd_DATA.root '$TARGET_PATH'/*DATA*.root)'
CMD_TO_RUN_TTLL='(cd '$TARGET_PATH') && (hadd -j 10 hadd_TTLL.root '$TARGET_PATH'/*TTLL*.root)'
CMD_TO_RUN_TTLJ='(cd '$TARGET_PATH') && (hadd -j 10 hadd_TTLJ.root '$TARGET_PATH'/*TTLJ*.root)'
CMD_TO_RUN_CHToCB='(cd '$TARGET_PATH') && (hadd -j 10 hadd_CHToCB.root '$TARGET_PATH'/*CHToCB*.root)'
# ST, QCD, DY, Wjets, TTWjets, TTZjets
CMD_TO_RUN_nonTT='(cd '$TARGET_PATH') && (hadd -j 10 hadd_nonTT.root '$TARGET_PATH'/*ST*.root '$TARGET_PATH'/*QCD*.root '$TARGET_PATH'/*DY*.root '$TARGET_PATH'/*Wjets*.root '$TARGET_PATH'/*TTWjets*.root '$TARGET_PATH'/*TTZjets*.root '$TARGET_PATH'/*ZZ*.root '$TARGET_PATH'/*WZ*.root '$TARGET_PATH'/*WW*.root)'
#WORK_DIR='hadd_batch'
#JOB_NAME='hadd_TTLL'


python $PYTHON_TOOL_PATH -c "$CMD_TO_RUN_DATA"   -d hadd_DATA -n hadd_DATA -m 10 -s
python $PYTHON_TOOL_PATH -c "$CMD_TO_RUN_TTLL"   -d hadd_TTLL -n hadd_TTLL_2016 -m 10 -s
python $PYTHON_TOOL_PATH -c "$CMD_TO_RUN_TTLJ"   -d hadd_TTLJ -n hadd_TTLJ_2016 -m 10 -s
python $PYTHON_TOOL_PATH -c "$CMD_TO_RUN_CHToCB" -d hadd_CHToCB -n hadd_CHToCB_2016 -m 10 -s
python $PYTHON_TOOL_PATH -c "$CMD_TO_RUN_nonTT"  -d hadd_nonTT -n hadd_nonTT_2016 -m 10 -s

