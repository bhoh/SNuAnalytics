rm ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/Wtagger_cfg.py
rm ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/modules/WtaggerProducer.py

ln -s ${PWD}/Wtagger_cfg.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/Wtagger_cfg.py
ln -s ${PWD}/WtaggerProducer.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/modules/WtaggerProducer.py
