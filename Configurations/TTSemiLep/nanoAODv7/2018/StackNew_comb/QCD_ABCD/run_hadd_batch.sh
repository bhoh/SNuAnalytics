export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch

PYTHON_TOOL_PATH=/cms/ldap_home/bhoh/latinos/jobs/python_tool/ExportShellCondorSetup.py
pushd .
cd $1
TARGET_PATH=${PWD}
#CMD_TO_RUN='(cd '$TARGET_PATH') && (cd '$TARGET_PATH'; pwd)'
CMD_TO_RUN_DATA0='(cd '$TARGET_PATH') && (hadd -j 10 -d /cms_scratch/bhoh hadd_DATA0.root '$TARGET_PATH'/*DATA*[0-4].root)'
CMD_TO_RUN_DATA1='(cd '$TARGET_PATH') && (hadd -j 10 -d /cms_scratch/bhoh hadd_DATA1.root '$TARGET_PATH'/*DATA*[5-9].root)'
CMD_TO_RUN_TTLL0='(cd '$TARGET_PATH') && (hadd -j 10 -d /cms_scratch/bhoh hadd_TTLL0.root '$TARGET_PATH'/*TTLL*[0-3].root)'
CMD_TO_RUN_TTLL1='(cd '$TARGET_PATH') && (hadd -j 10 -d /cms_scratch/bhoh hadd_TTLL1.root '$TARGET_PATH'/*TTLL*[4-6].root)'
CMD_TO_RUN_TTLL2='(cd '$TARGET_PATH') && (hadd -j 10 -d /cms_scratch/bhoh hadd_TTLL2.root '$TARGET_PATH'/*TTLL*[7-9].root)'
CMD_TO_RUN_TTLJ0='(cd '$TARGET_PATH') && (hadd -j 10 -d /cms_scratch/bhoh hadd_TTLJ0.root '$TARGET_PATH'/*TTLJ*[0-3].root)'
CMD_TO_RUN_TTLJ1='(cd '$TARGET_PATH') && (hadd -j 10 -d /cms_scratch/bhoh hadd_TTLJ1.root '$TARGET_PATH'/*TTLJ*[4-6].root)'
CMD_TO_RUN_TTLJ2='(cd '$TARGET_PATH') && (hadd -j 10 -d /cms_scratch/bhoh hadd_TTLJ2.root '$TARGET_PATH'/*TTLJ*[7-9].root)'
CMD_TO_RUN_CHToCB0='(cd '$TARGET_PATH') && (hadd -j 10 -d /cms_scratch/bhoh hadd_CHToCB0.root '$TARGET_PATH'/*CHToCB*[0-3].root)'
CMD_TO_RUN_CHToCB1='(cd '$TARGET_PATH') && (hadd -j 10 -d /cms_scratch/bhoh hadd_CHToCB1.root '$TARGET_PATH'/*CHToCB*[4-6].root)'
CMD_TO_RUN_CHToCB2='(cd '$TARGET_PATH') && (hadd -j 10 -d /cms_scratch/bhoh hadd_CHToCB2.root '$TARGET_PATH'/*CHToCB*[7-9].root)'
# ST, QCD, DY, Wjets, TTWjets, TTZjets
CMD_TO_RUN_nonTT='(cd '$TARGET_PATH') && (hadd -j 10 -d /cms_scratch/bhoh hadd_nonTT.root '$TARGET_PATH'/*ST*.root '$TARGET_PATH'/*QCD*.root '$TARGET_PATH'/*DY*.root '$TARGET_PATH'/*Wjets*.root '$TARGET_PATH'/*TTWjets*.root '$TARGET_PATH'/*TTZjets*.root '$TARGET_PATH'/*ZZ*.root '$TARGET_PATH'/*WZ*.root '$TARGET_PATH'/*WW*.root)'
#WORK_DIR='hadd_batch'
#JOB_NAME='hadd_TTLL'

mkdir -p 'hadd_DATA0'  
mkdir -p 'hadd_DATA1'  
mkdir -p 'hadd_TTLL0'  
mkdir -p 'hadd_TTLL1'  
mkdir -p 'hadd_TTLL2'  
mkdir -p 'hadd_TTLJ0'  
mkdir -p 'hadd_TTLJ1'  
mkdir -p 'hadd_TTLJ2'  
mkdir -p 'hadd_CHToCB0'
mkdir -p 'hadd_CHToCB1'
mkdir -p 'hadd_CHToCB2'
mkdir -p 'hadd_nonTT' 

python $PYTHON_TOOL_PATH -c "$CMD_TO_RUN_DATA0"   -d 'hadd_DATA0'   -n hadd_DATA0_2018 -m 10 -s
python $PYTHON_TOOL_PATH -c "$CMD_TO_RUN_DATA1"   -d 'hadd_DATA1'   -n hadd_DATA1_2018 -m 10 -s
python $PYTHON_TOOL_PATH -c "$CMD_TO_RUN_TTLL0"   -d 'hadd_TTLL0'   -n hadd_TTLL0_2018 -m 10 -s
python $PYTHON_TOOL_PATH -c "$CMD_TO_RUN_TTLL1"   -d 'hadd_TTLL1'   -n hadd_TTLL1_2018 -m 10 -s
python $PYTHON_TOOL_PATH -c "$CMD_TO_RUN_TTLL2"   -d 'hadd_TTLL2'   -n hadd_TTLL2_2018 -m 10 -s
python $PYTHON_TOOL_PATH -c "$CMD_TO_RUN_TTLJ0"   -d 'hadd_TTLJ0'   -n hadd_TTLJ0_2018 -m 10 -s
python $PYTHON_TOOL_PATH -c "$CMD_TO_RUN_TTLJ1"   -d 'hadd_TTLJ1'   -n hadd_TTLJ1_2018 -m 10 -s
python $PYTHON_TOOL_PATH -c "$CMD_TO_RUN_TTLJ2"   -d 'hadd_TTLJ2'   -n hadd_TTLJ2_2018 -m 10 -s
python $PYTHON_TOOL_PATH -c "$CMD_TO_RUN_CHToCB0" -d 'hadd_CHToCB0' -n hadd_CHToCB0_2018 -m 10 -s
python $PYTHON_TOOL_PATH -c "$CMD_TO_RUN_CHToCB1" -d 'hadd_CHToCB1' -n hadd_CHToCB1_2018 -m 10 -s
python $PYTHON_TOOL_PATH -c "$CMD_TO_RUN_CHToCB2" -d 'hadd_CHToCB2' -n hadd_CHToCB2_2018 -m 10 -s
python $PYTHON_TOOL_PATH -c "$CMD_TO_RUN_nonTT"   -d 'hadd_nonTT'  -n hadd_nonTT_2018 -m 10 -s

popd
