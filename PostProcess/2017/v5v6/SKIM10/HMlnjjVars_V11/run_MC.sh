# /xrootd//store/user/jhchoi/Latino/HWWNano/
# Sites_cfg: /xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/
# changed to /xrd/store/user/jhchoi/Latino/HWWNano/
# L1Loose

source TurnOnDryRun.sh



SAMPLES=(
DYJetsToLL_M-5to50-LO
DYJetsToLL_M-10to50-LO
DYJetsToLL_M-10to50-LO_ext1
DYJetsToLL_M-50-LO
DYJetsToLL_M-50-LO_ext1
DYJetsToLL_M-50
DYJetsToLL_M-4to50_HT-100to200
DYJetsToLL_M-4to50_HT-100to200_ext1
DYJetsToLL_M-4to50_HT-200to400
DYJetsToLL_M-4to50_HT-200to400_ext1
DYJetsToLL_M-4to50_HT-400to600
DYJetsToLL_M-4to50_HT-400to600_ext1
DYJetsToLL_M-4to50_HT-600toInf
DYJetsToLL_M-4to50_HT-600toInf_ext1
DYJetsToLL_M-50_HT-100to200
DYJetsToLL_M-50_HT-200to400
DYJetsToLL_M-50_HT-200to400_ext1
DYJetsToLL_M-50_HT-400to600_ext1
DYJetsToLL_M-50_HT-600to800
DYJetsToLL_M-50_HT-800to1200
DYJetsToLL_M-50_HT-1200to2500
DYJetsToLL_M-50_HT-2500toInf
QCD_Pt-15to20_MuEnrichedPt5
QCD_Pt-20to30_MuEnrichedPt5
QCD_Pt-30to50_MuEnrichedPt5
QCD_Pt-50to80_MuEnrichedPt5
QCD_Pt-80to120_MuEnrichedPt5
QCD_Pt-120to170_MuEnrichedPt5
QCD_Pt-170to300_MuEnrichedPt5
QCD_Pt-300to470_MuEnrichedPt5
QCD_Pt-470to600_MuEnrichedPt5
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
TTToSemiLeptonic
TTTo2L2Nu_PSWeights
ST_t-channel_top
ST_t-channel_antitop
ST_tW_antitop
ST_tW_top
ST_s-channel
TTWjets
TTWjets_ext1
TTZjets
TTZjets_ext1
WJetsToLNu-0J
WJetsToLNu-1J
WJetsToLNu-2J
WW-LO
WWToLNuQQ
QCD_Pt_20to30_bcToE
QCD_Pt_20to30_bcToE_newpmx
QCD_Pt_30to80_bcToE
QCD_Pt_80to170_bcToE
QCD_Pt_170to250_bcToE
QCD_Pt_250toInf_bcToE
QCD_Pt_170to300
QCD_Pt_170to300_ext1
WZ
ZZ
ZZZ
WWW
WZZ
WWZ
WpWmJJ_EWK_QCD_noHiggs
WpWmJJ_EWK_QCD_noTop_noHiggs
WpWmJJ_EWK_noTop
)
source Add_VHtautauWWJJ.sh
EXCLUDE=()

#--Run--#
SAMPLE_LIST=''
EXCLUDE_LIST=''
for s in ${SAMPLES[@]};do SAMPLE_LIST=${s}','${SAMPLE_LIST};done
for e in ${EXCLUDE[@]};do EXCLUDE_LIST=${e}','${EXCLUDE_LIST};done
#echo ${SAMPLE_LIST}
#echo ${EXCLUDE_LIST}

######################
# Option: -R(redo)
######################

#modcfg='--modcfg SNuAnalytics/NanoGardenerFrameworks/Steps_cfg.py'

#--l1Prod--#
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i Prod -s MCl1loose2017v6 -b -T ${SAMPLE_LIST}
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6 -s MCCorr2017v6 -b -T ${SAMPLE_LIST}


##SKIM10
#modcfg="--modcfg SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200406_HMSemilepSKIMv6_10/Steps_cfg.py"
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6 -s HMSemilepSKIMv6_10 -b -T ${SAMPLE_LIST}


##Analyzer
modcfg="--modcfg SNuAnalytics/NanoGardenerModules/HMlnjjVars_Dev_jhchoi/Steps_cfg_HMlnjjVars_V11.py" ##HMFull_V11_nom
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s HMFull_V11_nom -T ${SAMPLE_LIST} -b
##JetSys -> HMFull_V11_jetsysdown_uncorrelate



mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s HMFull_V11_jetsysdown_uncorrelate -T ${SAMPLE_LIST} -b

mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s HMFull_V11_jetsysup_uncorrelate -T ${SAMPLE_LIST} -b
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s HMFull_V11_jetsysdown_correlate -T ${SAMPLE_LIST} -b
#mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s HMFull_V11_jetsysup_correlate -T ${SAMPLE_LIST} -b
mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s HMFull_V11_fatjetsys -T ${SAMPLE_LIST} -b

#mkPostProc.py -p Fall2017_102X_nAODv5_Full2017v6 -i MCl1loose2017v6__MCCorr2017v6 -s HMSemilepSkimJHv6_7 -T ZZZ


##--Systematics
SYSLIST=()
##--Lepton momentum Scale--##
ANA=HMFull_V11_nom
SYSLIST+=(${ANA}_ElepTup)
SYSLIST+=(${ANA}_ElepTdo)
SYSLIST+=(${ANA}_MupTup)
SYSLIST+=(${ANA}_MupTdo)
SYSLIST+=(${ANA}_METup)
SYSLIST+=(${ANA}_METdo)

for sys in ${SYSLIST[@]};do
    echo "---$sys---"
    continue
    mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s ${sys} -b -T ${SAMPLE_LIST}
    #mkPostProc.py ${modcfg} -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10 -s ${sys} -b -T ZZZ ##To Test
done


##--Test
#mkPostProc.py -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6__MCCorr2017v6 -s ElepTup_suffix -b -T WW-LO
#mkPostProc.py -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6__MCCorr2017v6 -s METup_suffix -b -T WW-LO
#mkPostProc.py -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6__MCCorr2017v6 -s FATJESup_suffix_total -b -T WW-LO
#mkPostProc.py -p Fall2017_102X_nAODv5_Full2017v6 -i  MCl1loose2017v6__MCCorr2017v6 -s JESup_suffix_total -b -T WW-LO


SAMPLES=()
EXCLUDE=()





unset -f condor_submit


