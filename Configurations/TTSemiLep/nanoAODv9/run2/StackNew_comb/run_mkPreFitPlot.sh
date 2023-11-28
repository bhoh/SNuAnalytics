
with_mass=false

if $with_mass;
then
Config='configuration_run2_prefit_Low_mass.py'
Config_dbl='configuration_run2_dbl_prefit_Low_mass.py'
OutputFile='results_run2_PreFit_Low_mass.root'
#
#
mkPlot.py --pycfg=$Config --inputFile=$OutputFile --onlyPlot=cratio --scaleToPlot=1.7 --onlyCut=sng_4j_eleORmuCH_2b
mkPlot.py --pycfg=$Config_dbl --inputFile=$OutputFile --onlyPlot=cratio --scaleToPlot=1.7 --onlyCut=dbl_4j_eeORmmORemORme_offZ


Config='configuration_run2_prefit_High_mass.py'
Config_dbl='configuration_run2_dbl_prefit_High_mass.py'
OutputFile='results_run2_PreFit_High_mass.root'
#
#
mkPlot.py --pycfg=$Config --inputFile=$OutputFile --onlyPlot=cratio --scaleToPlot=1.7 --onlyCut=sng_4j_eleORmuCH_2b
mkPlot.py --pycfg=$Config_dbl --inputFile=$OutputFile --onlyPlot=cratio --scaleToPlot=1.7 --onlyCut=dbl_4j_eeORmmORemORme_offZ
else
Config='configuration_run2_prefit_Low.py'
Config_dbl='configuration_run2_dbl_prefit_Low.py'
OutputFile='results_run2_PreFit_Low.root'
#
#
mkPlot.py --pycfg=$Config --inputFile=$OutputFile --onlyPlot=cratio --scaleToPlot=1.7 --onlyCut=sng_4j_eleORmuCH_2b
mkPlot.py --pycfg=$Config_dbl --inputFile=$OutputFile --onlyPlot=cratio --scaleToPlot=1.7 --onlyCut=dbl_4j_eeORmmORemORme_offZ


Config='configuration_run2_prefit_High.py'
Config_dbl='configuration_run2_dbl_prefit_High.py'
OutputFile='results_run2_PreFit_High.root'
#
#
mkPlot.py --pycfg=$Config --inputFile=$OutputFile --onlyPlot=cratio --scaleToPlot=1.7 --onlyCut=sng_4j_eleORmuCH_2b
mkPlot.py --pycfg=$Config_dbl --inputFile=$OutputFile --onlyPlot=cratio --scaleToPlot=1.7 --onlyCut=dbl_4j_eeORmmORemORme_offZ
fi
