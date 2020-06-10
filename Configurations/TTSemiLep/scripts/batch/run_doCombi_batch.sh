
# -- making snapshot
#
#python doCombi_batch.py -Year='All' -M='MultiDimFit' -options='--saveWorkspace --cminPreScan --cminPreFit 1 --verbose 9'
#python doCombi.py -Year='All' -options='--rAbsAcc 0 --rRelAcc 0.005000000000000001 --cminPreScan --cminPreFit 1 --verbose 9'
python doCombi_batch.py -Year='All' -options='--rRelAcc 0.005000000000000001 --cminPreScan --cminPreFit 100 --verbose 9 --minosAlgo minos -t 100'
#python doCombi.py -Year='All' -options='--rAbsAcc 0 --rRelAcc 0.005000000000000001 --cminPreScan --cminPreFit 1 --verbose 9' -snapshot
#python doCombi.py -Year='All' -options='-t -1 --rAbsAcc 0 --rRelAcc 0.005000000000000001 --cminPreScan --cminPreFit 1 ' -snapshot
#
# -- pre-fit expectation and significance
#
#python doCombi.py -Year='All' -options='-t -1 --rAbsAcc 0.1 --rRelAcc 0.005000000000000001 --cminPreScan --cminPreFit 1'
#python doCombi.py -Year='All' -options='-t -1 --rAbsAcc 0.1 --rRelAcc 0.005000000000000001 --cminPreScan --cminPreFit 1 --setParameters BR10ToMinus7=0.01'
#python doCombi.py -Year='All' -M='Significance' -options='-t -1 --cminPreScan --cminPreFit 1 --setParameters BR10ToMinus7=0.1'
#
# -- likilhood scan
#
#python doCombi.py -Year='All' -M='HybridNew' -options='--LHCmode LHC-limits --cminPreScan --cminPreFit 1 --singlePoint 100  --saveToys --saveHybridResult -T 500' -snapshot
#
#
#
# -- crab
#python doCombi_batch.py -Year='All' -M='HybridNew' -options='--LHCmode LHC-limits --singlePoint 100:1000:100 -T 300 -s -1 --saveToys --saveHybridResult  --dry-run'
#source /cvmfs/cms.cern.ch/crab3/crab.sh;
#cd /cms/ldap_home/bhoh/HiggsCombTool/CMSSW_10_6_4/python/CombineHarvester/
#cmsenv
#cd -
#python doCombi_batch.py -Year='All' -M='HybridNew' -options='--LHCmode LHC-limits --singlePoint 100:1000:100 -T 100 -s -1 --saveToys --saveHybridResult  ' -batch='--job-mode crab3 --task-name CHToCBM{MASS}-combine-test --custom-crab custom_crab.py --dry-run'
