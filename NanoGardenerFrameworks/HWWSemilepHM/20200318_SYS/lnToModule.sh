#ln -s ${PWD}/HMlnjjVars_Dev_jhchoi.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/modules/HMlnjjVars_Dev_jhchoi.py
#ln -s ${PWD}/HMlnjjVars_Dev_jhchoi3.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/modules/HMlnjjVars_Dev_jhchoi3.py
#ln -s ${PWD}/BranchMapping_cfg.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/BranchMapping_cfg.py
#/cms/ldap_home/jhchoi/HWW_Analysis/slc7/For_Productionv6/CMSSW_10_2_14/src/LatinoAnalysis/NanoGardener/python/data

#not working ln
mv ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/BranchMapping_cfg.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/BranchMapping_cfg.py_orig
cp BranchMapping_cfg.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/BranchMapping_cfg.py 
