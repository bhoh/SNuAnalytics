#ln -s ${PWD}/HMlnjjVars_Dev_jhchoi.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/modules/HMlnjjVars_Dev_jhchoi.py
#ln -s ${PWD}/HMlnjjVars_Dev_jhchoi3.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/modules/HMlnjjVars_Dev_jhchoi3.py
#ln -s ${PWD}/HEMveto.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/modules/HEMveto.py
#ln -s ${PWD}/HEMweight.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/modules/HEMweight.py


MODULES=(
jetmetHelperRun2Regrouped.py
jetmetUncertainties.py
HEMweight.py
JetNomToMETPropagation.py
)

for m in ${MODULES[@]};do
    rm ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/modules/${m}
    ln -s ${PWD}/${m} ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/modules/${m}
    
done
