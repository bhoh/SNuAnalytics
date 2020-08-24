#source TurnOnDryRun.sh

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
GluGluHToWWToLNuQQ_M115
GluGluHToWWToLNuQQ_M120
GluGluHToWWToLNuQQ_M124
GluGluHToWWToLNuQQ_M125
GluGluHToWWToLNuQQ_M126
GluGluHToWWToLNuQQ_M130
GluGluHToWWToLNuQQ_M135
GluGluHToWWToLNuQQ_M140
GluGluHToWWToLNuQQ_M145
GluGluHToWWToLNuQQ_M150
GluGluHToWWToLNuQQ_M155
GluGluHToWWToLNuQQ_M160
GluGluHToWWToLNuQQ_M165
GluGluHToWWToLNuQQ_M170
GluGluHToWWToLNuQQ_M175
GluGluHToWWToLNuQQ_M180
GluGluHToWWToLNuQQ_M190
GluGluHToWWToLNuQQ_M200
GluGluHToWWToLNuQQ_M210
GluGluHToWWToLNuQQ_M230
GluGluHToWWToLNuQQ_M250
GluGluHToWWToLNuQQ_M270
GluGluHToWWToLNuQQ_M300
GluGluHToWWToLNuQQ_M350
GluGluHToWWToLNuQQ_M400
GluGluHToWWToLNuQQ_M450
GluGluHToWWToLNuQQ_M500
GluGluHToWWToLNuQQ_M550
GluGluHToWWToLNuQQ_M600
GluGluHToWWToLNuQQ_M650
GluGluHToWWToLNuQQ_M700
GluGluHToWWToLNuQQ_M750
GluGluHToWWToLNuQQ_M800
GluGluHToWWToLNuQQ_M900
GluGluHToWWToLNuQQ_M1000
GluGluHToWWToLNuQQ_M1500
GluGluHToWWToLNuQQ_M2000
GluGluHToWWToLNuQQ_M2500
GluGluHToWWToLNuQQ_M3000
GluGluHToWWToLNuQQ_M4000
GluGluHToWWToLNuQQ_M5000
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
VBFHToWWToLNuQQ_M115
VBFHToWWToLNuQQ_M120
VBFHToWWToLNuQQ_M124
VBFHToWWToLNuQQ_M125
VBFHToWWToLNuQQ_M126
VBFHToWWToLNuQQ_M130
VBFHToWWToLNuQQ_M135
VBFHToWWToLNuQQ_M140
VBFHToWWToLNuQQ_M145
VBFHToWWToLNuQQ_M150
VBFHToWWToLNuQQ_M155
VBFHToWWToLNuQQ_M160
VBFHToWWToLNuQQ_M165
VBFHToWWToLNuQQ_M170
VBFHToWWToLNuQQ_M175
VBFHToWWToLNuQQ_M180
VBFHToWWToLNuQQ_M190
VBFHToWWToLNuQQ_M200
VBFHToWWToLNuQQ_M210
VBFHToWWToLNuQQ_M230
VBFHToWWToLNuQQ_M250
VBFHToWWToLNuQQ_M270
VBFHToWWToLNuQQ_M300
VBFHToWWToLNuQQ_M350
VBFHToWWToLNuQQ_M400
VBFHToWWToLNuQQ_M450
VBFHToWWToLNuQQ_M500
VBFHToWWToLNuQQ_M550
VBFHToWWToLNuQQ_M600
VBFHToWWToLNuQQ_M650
VBFHToWWToLNuQQ_M700
VBFHToWWToLNuQQ_M750
VBFHToWWToLNuQQ_M800
VBFHToWWToLNuQQ_M900
VBFHToWWToLNuQQ_M1000
VBFHToWWToLNuQQ_M1500
VBFHToWWToLNuQQ_M2000
VBFHToWWToLNuQQ_M2500
VBFHToWWToLNuQQ_M3000
VBFHToWWToLNuQQ_M4000
VBFHToWWToLNuQQ_M5000
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

modcfg="--modcfg SNuAnalytics/NanoGardenerModules/HMlnjjVars_Dev_jhchoi/Steps_cfg.py"
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_nom -b -T ${SAMPLE_LIST}

mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s BWReweight -b -T ${SAMPLE_LIST}



#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_jetsysdown_uncorrelate -b -T ${SAMPLE_LIST}
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_jetsysup_uncorrelate -b -T ${SAMPLE_LIST}

#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_jetsysdown_correlate -b -T ${SAMPLE_LIST}
#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_jetsysup_correlate -b -T ${SAMPLE_LIST}

#mkPostProc.py ${modcfg} -p Autumn18_102X_nAODv6_Full2018v6 -i  MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10 -s HMFull_jhchoi10_fatjetsys -b -T ${SAMPLE_LIST}



#SAMPLE_LIST=ZZZ;echo "!!!!TEST JOB!!!!"

SYSLIST=()
ANA=HMFull_jhchoi10_nom

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
