python SetupScripts/MakeKfactor.py
python SetupScripts/MakeMELAWeightCut.py
python SetupScripts/MakeQCDscalePdfPsNuisancePy.py
python SetupScripts/MakeDummySamplePY.py

##----Make Datacards env
pushd MassPoints
python MakeSampleStructurePythons.py
popd 


git clone git@github.com:soarnsoar/python_tool.git


##--set alias
source myalias/set_alias.sh
