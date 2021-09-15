#ln -s ${PWD}/HMlnjjVars_Dev_jhchoi.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/modules/HMlnjjVars_Dev_jhchoi.py
#ln -s ${PWD}/HMlnjjVars_Dev_jhchoi3.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/modules/HMlnjjVars_Dev_jhchoi3.py
#ln -s ${PWD}/HEMveto.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/modules/HEMveto.py
#ln -s ${PWD}/HEMweight.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/modules/HEMweight.py

MODULES=(
POGLeptonSFMaker.py
HEMweight.py
jetmetUncertainties.py
jetmetHelperRun2Regrouped.py
JetNomToMETPropagation.py
TMVAfiller_CHToCB.py
)

DIRS=(
Full2018v7_POG
Full2017v7_POG
Full2016v7_POG
)

FORMULAS=(
POGLeptonSel_cfg.py
formulasToAdd_DATA_CHToCB_Full2018v7.py
formulasToAdd_DATA_CHToCB_Full2017v7.py
formulasToAdd_DATA_CHToCB_Full2016v7.py
formulasToAdd_MC_CHToCB_Full2018v7.py
formulasToAdd_MC_CHToCB_Full2017v7.py
formulasToAdd_MC_CHToCB_Full2016v7.py
)

for m in ${MODULES[@]};do
    rm ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/modules/${m}
    ln -s ${PWD}/${m} ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/modules/${m}
    
done

for m in ${FORMULAS[@]};do
    rm ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/${m}
    ln -s ${PWD}/${m} ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/${m}
    
done

for m in ${DIRS[@]};do
    rm -r ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/scale_factor/${m}
    ln -sf ${PWD}/${m} ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/scale_factor/${m}
    
done

mkdir -p ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/MVA/CHToCB/
rm ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/MVA/CHToCB/mvaDict_2018.py
ln -s ${PWD}/mvaDict_2018.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/MVA/CHToCB/mvaDict_2018.py
rm ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/MVA/CHToCB/mvaDict_2017.py
ln -s ${PWD}/mvaDict_2018.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/MVA/CHToCB/mvaDict_2017.py
rm ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/MVA/CHToCB/mvaDict_2016.py
ln -s ${PWD}/mvaDict_2018.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/MVA/CHToCB/mvaDict_2016.py
