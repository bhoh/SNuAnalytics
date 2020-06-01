##Note##
1)configuration_Boosted(Resolved).py
	->Boosted/Resolved region is separated. But samples_2016.py is commone for boosted/resolved regions.
	->turn off nuisances part to reduce running time. Use it only for final.

2)WPandCut2016.py
	->to make common configuration for all 3 years.
	->For Fatjet WP => dictionary object 'WJID'
	->For Wjjtagger WP => dictionary object 'MYALGO'
	->Jet cut(different only for 2016) => dictionary object 'JETCUTS'
3)aliases.py
	->MET is defined only for px,py,pz... 
	->define PuppiMET_nom_pt
	->naming 'nom' is needed to get systematic shapes.
4)variables_Boosted(Resolved).py /
	->Set isFinal=False to get various kin. distribution
	->if isFinal == True, only M(WW) shape is produced.
5)



##How to Run nominal
1) Make histograms of each shape
source Histo_factory_run.sh


2) Plot Maker
source Plot_maker_run_Boosted.sh
source Plot_maker_run_Resolved.sh

