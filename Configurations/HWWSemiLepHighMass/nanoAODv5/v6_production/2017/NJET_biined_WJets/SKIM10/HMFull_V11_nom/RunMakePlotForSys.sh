#   parser.add_option("-s","--syslist",   dest="syslist", help="sys list")
#   parser.add_option("-a","--alias",   dest="alias", help="alias of this group")
#   parser.add_option("-p","--plotmaker",   dest="plotmaker", help="plot maker shell to mimic")

plotmaker1=Plot_maker_run_Boosted_tmp.sh
plotmaker2=Plot_maker_run_Resolved_tmp.sh

SYSGROUP=jesFlavorQCD,jesRelativeBal,jesHF,jesBBEC1,jesEC2,jesAbsolute,jesAbsolute_2017,jesHF_2017,jesEC2_2017,jesRelativeSample_2017,jesBBEC1_2017,jer
ALIAS="JES"

python MakePlotForSys.py -s ${SYSGROUP} -a ${ALIAS} -p ${plotmaker1} -c configuration_Boosted.py
source ${plotmaker1%.sh}_${ALIAS}.sh
python MakePlotForSys.py -s ${SYSGROUP} -a ${ALIAS} -p ${plotmaker2} -c configuration_Resolved.py
source ${plotmaker2%.sh}_${ALIAS}.sh

SYSGROUP=btag_shape_lf,btag_shape_hf,btag_shape_hfstats1,btag_shape_hfstats2,btag_shape_lfstats1,btag_shape_lfstats2,btag_shape_cferr1,btag_shape_cferr2
ALIAS="btag"

python MakePlotForSys.py -s ${SYSGROUP} -a ${ALIAS} -p ${plotmaker1} -c configuration_Boosted.py
source ${plotmaker1%.sh}_${ALIAS}.sh
python MakePlotForSys.py -s ${SYSGROUP} -a ${ALIAS} -p ${plotmaker2} -c configuration_Resolved.py
source ${plotmaker2%.sh}_${ALIAS}.sh

SYSGROUP=QCDscaleAccept
ALIAS="QCDscaleAccept"

python MakePlotForSys.py -s ${SYSGROUP} -a ${ALIAS} -p ${plotmaker1} -c configuration_Boosted.py
source ${plotmaker1%.sh}_${ALIAS}.sh
python MakePlotForSys.py -s ${SYSGROUP} -a ${ALIAS} -p ${plotmaker2} -c configuration_Resolved.py
source ${plotmaker2%.sh}_${ALIAS}.sh

SYSGROUP=pdfAccept
ALIAS="pdfAccept"

python MakePlotForSys.py -s ${SYSGROUP} -a ${ALIAS} -p ${plotmaker1} -c configuration_Boosted.py
source ${plotmaker1%.sh}_${ALIAS}.sh
python MakePlotForSys.py -s ${SYSGROUP} -a ${ALIAS} -p ${plotmaker2} -c configuration_Resolved.py
source ${plotmaker2%.sh}_${ALIAS}.sh

SYSGROUP=jer
ALIAS="JER"
python MakePlotForSys.py -s ${SYSGROUP} -a ${ALIAS} -p ${plotmaker1} -c configuration_Boosted.py
source ${plotmaker1%.sh}_${ALIAS}.sh
python MakePlotForSys.py -s ${SYSGROUP} -a ${ALIAS} -p ${plotmaker2} -c configuration_Resolved.py
source ${plotmaker2%.sh}_${ALIAS}.sh

SYSGROUP=fatjes,fatjer,fatjms,fatjmr
ALIAS=FATJET
python MakePlotForSys.py -s ${SYSGROUP} -a ${ALIAS} -p ${plotmaker1} -c configuration_Boosted.py
source ${plotmaker1%.sh}_${ALIAS}.sh
python MakePlotForSys.py -s ${SYSGROUP} -a ${ALIAS} -p ${plotmaker2} -c configuration_Resolved.py
source ${plotmaker2%.sh}_${ALIAS}.sh
