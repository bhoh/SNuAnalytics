source TurnOnDryRun.sh

SAMPLES=(
DYJetsToLL_M-4to50_HT-200to400
DYJetsToLL_M-4to50_HT-400to600
DYJetsToLL_M-4to50_HT-600toInf
DYJetsToLL_M-10to50-LO_ext1
DYJetsToLL_M-10to50-LO
DYJetsToLL_M-50
DYJetsToLL_M-50-LO
DYJetsToLL_M-50_HT-70to100
DYJetsToLL_M-50_HT-100to200
DYJetsToLL_M-50_HT-200to400
DYJetsToLL_M-50_HT-400to600
DYJetsToLL_M-50_HT-600to800
DYJetsToLL_M-50_HT-800to1200
DYJetsToLL_M-50_HT-1200to2500
DYJetsToLL_M-50_HT-2500toInf
QCD_Pt-15to20_MuEnrichedPt5
QCD_Pt-20to30_MuEnrichedPt5
QCD_Pt-30to50_MuEnrichedPt5
QCD_Pt-50to80_MuEnrichedPt5
QCD_Pt-80to120_MuEnrichedPt5
QCD_Pt-80to120_MuEnrichedPt5_ext1
QCD_Pt-120to170_MuEnrichedPt5
QCD_Pt-120to170_MuEnrichedPt5_ext1
QCD_Pt-170to300_MuEnrichedPt5
QCD_Pt-300to470_MuEnrichedPt5
QCD_Pt-300to470_MuEnrichedPt5_ext3
QCD_Pt-470to600_MuEnrichedPt5
QCD_Pt-470to600_MuEnrichedPt5_ext1
QCD_Pt-600to800_MuEnrichedPt5
QCD_Pt-800to1000_MuEnrichedPt5
QCD_Pt-1000toInf_MuEnrichedPt5
QCD_Pt-15to20_EMEnriched
QCD_Pt-20to30_EMEnriched
QCD_Pt-30to50_EMEnriched
QCD_Pt-50to80_EMEnriched
QCD_Pt-80to120_EMEnriched
QCD_Pt-120to170_EMEnriched
QCD_Pt-170to300_EMEnriched
QCD_Pt-300toInf_EMEnriched
ST_t-channel_top
ST_t-channel_antitop
ST_tW_top_ext1
ST_tW_antitop_ext1
ST_s-channel_ext1
TTToSemiLeptonic
TTTo2L2Nu
TTToSemiLeptonic_ext3
TTZjets
TTWjets
WJetsToLNu-0J
WJetsToLNu-1J
WJetsToLNu-2J
WW-LO
WWToLNuQQ
WWToLNuQQ_AMCATNLO
WZ
ZZ
WWW
WWZ
WZZ
ZZZ
QCD_Pt_20to30_bcToE
QCD_Pt_30to80_bcToE
QCD_Pt_80to170_bcToE
QCD_Pt_170to250_bcToE
QCD_Pt_250toInf_bcToE
WpWmJJ_EWK_QCD_noHiggs
)
source Add_VHtautauWWJJ.sh
#--Run--#

SAMPLE_LIST=''
EXCLUDE_LIST=''
for s in ${SAMPLES[@]};do SAMPLE_LIST=${s}','${SAMPLE_LIST};done
for e in ${EXCLUDE[@]};do EXCLUDE_LIST=${e}','${EXCLUDE_LIST};done


######################
# Option: -R(redo)
######################
#--l1Prod--#
#mkPostProc.py -p Autumn18_102X_nAODv6_Full2018v6 -i Prod -s MCl1loose2018v6 -b -T ${SAMPLE_LIST} 
#mkPostProc.py -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6 -s MCCorr2018v6 -b -T ${SAMPLE_LIST} 
#mkPostProc.py -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6 -s HMSemilepSkimJHv6_HMvar7 -b -T ${SAMPLE_LIST}
modcfg="--modcfg SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200406_HMSemilepSKIMv6_10/Steps_cfg.py"
 
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6 -s HMSemilepSKIMv6_10 -b -T ${SAMPLE_LIST} 

modcfg="--modcfg SNuAnalytics/NanoGardenerModules/HMlnjjVars_Dev_jhchoi/Steps_cfg_HMlnjjVars_V11.py"
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_V11_nom -b -T ${SAMPLE_LIST}

#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s BWReweight -b -T ${SAMPLE_LIST}



mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_V11_jetsysdown_uncorrelate -b -T ${SAMPLE_LIST}
mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_V11_jetsysup_uncorrelate -b -T ${SAMPLE_LIST}

#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_V11_jetsysdown_correlate -b -T ${SAMPLE_LIST}
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_V11_jetsysup_correlate -b -T ${SAMPLE_LIST}

mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_V11_fatjetsys -b -T ${SAMPLE_LIST}



#SAMPLE_LIST=ZZZ;echo "!!!!TEST JOB!!!!"

SYSLIST=()
ANA=HMFull_V11_nom

SYSLIST+=(${ANA}_ElepTup)
SYSLIST+=(${ANA}_ElepTdo)
SYSLIST+=(${ANA}_MupTup)
SYSLIST+=(${ANA}_MupTdo)
SYSLIST+=(${ANA}_METup)
SYSLIST+=(${ANA}_METdo)

for sys in ${SYSLIST[@]};do
    continue
    echo "---$sys---"
    mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s ${sys} -b -T ${SAMPLE_LIST}
done

unset -f condor_submit
