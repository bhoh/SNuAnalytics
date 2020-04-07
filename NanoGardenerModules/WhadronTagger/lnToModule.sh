


#rm ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/Wtagger_cfg.py
#rm ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/modules/WtaggerProducer.py

#ln -s ${PWD}/Wtagger_cfg.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/Wtagger_cfg.py
#ln -s ${PWD}/WtaggerProducer.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/modules/WtaggerProducer.py

rm ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/Wjjtagger_cfg.py
rm ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/modules/WjjtaggerProducer.py

ln -s ${PWD}/Wjjtagger_cfg.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/data/Wjjtagger_cfg.py
ln -s ${PWD}/WjjtaggerProducer.py ${CMSSW_BASE}/src/LatinoAnalysis/NanoGardener/python/modules/WjjtaggerProducer.py


