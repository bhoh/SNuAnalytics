# /xrootd//store/user/jhchoi/Latino/HWWNano/
# Sites_cfg: /xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/
# changed to /xrd/store/user/jhchoi/Latino/HWWNano/
# L1Loose

source TurnOnDryRun.sh

SAMPLES=(
DYJetsToLL_M-10to50-LO
DYJetsToLL_M-50-LO_ext1
DYJetsToLL_M-50-LO_ext2
DYJetsToLL_M-10to50
DYJetsToLL_M-10to50_ext1
DYJetsToLL_M-50_ext2
DYJetsToLL_M-50-UEup
DYJetsToLL_M-50-UEdo
DYJetsToLL_M-50-PSup
DYJetsToLL_M-50-PSdo
DYJetsToLL_M-5to50_HT-70to100
DYJetsToLL_M-5to50_HT-100to200
DYJetsToLL_M-5to50_HT-100to200_ext1
DYJetsToLL_M-5to50_HT-200to400
DYJetsToLL_M-5to50_HT-200to400_ext1
DYJetsToLL_M-5to50_HT-400to600
DYJetsToLL_M-5to50_HT-400to600_ext1
DYJetsToLL_M-5to50_HT-600toinf
DYJetsToLL_M-50_HT-70to100
DYJetsToLL_M-50_HT-100to200
DYJetsToLL_M-50_HT-100to200_ext1
DYJetsToLL_M-50_HT-200to400
DYJetsToLL_M-50_HT-200to400_ext1
DYJetsToLL_M-50_HT-400to600
DYJetsToLL_M-50_HT-400to600_ext1
DYJetsToLL_M-50_HT-600to800
DYJetsToLL_M-50_HT-800to1200
DYJetsToLL_M-50_HT-1200to2500
DYJetsToLL_M-50_HT-2500toinf
QCD_Pt-15to20_MuEnrichedPt5
QCD_Pt-20toInf_MuEnrichedPt15
QCD_Pt-20to30_EMEnriched
QCD_Pt-30to50_EMEnriched
QCD_Pt-50to80_EMEnriched
QCD_Pt-80to120_EMEnriched
QCD_Pt-120to170_EMEnriched
QCD_Pt-170to300_EMEnriched
QCD_Pt-300toInf_EMEnriched
QCD_Pt_15to20_bcToE
QCD_Pt_20to30_bcToE
QCD_Pt_30to80_bcToE
QCD_Pt_80to170_bcToE
QCD_Pt_170to250_bcToE
QCD_Pt_250toInf_bcToE
TTToSemiLeptonic
TTTo2L2Nu
ST_t-channel_top
ST_t-channel_antitop
ST_tW_antitop
ST_tW_top
ST_s-channel
TTWJetsToLNu
TTWJetsToQQ
TTZjets
WJetsToLNu_HT70_100
WJetsToLNu_HT100_200
WJetsToLNu_HT100_200_ext1
WJetsToLNu_HT100_200_ext2
WJetsToLNu_HT200_400
WJetsToLNu_HT200_400_ext1
WJetsToLNu_HT200_400_ext2
WJetsToLNu_HT400_600
WJetsToLNu_HT400_600_ext1
WJetsToLNu_HT600_800
WJetsToLNu_HT600_800_ext1
WJetsToLNu_HT800_1200
WJetsToLNu_HT800_1200_ext1
WJetsToLNu_HT1200_2500
WJetsToLNu_HT1200_2500_ext1
WJetsToLNu_HT2500_inf
WJetsToLNu_HT2500_inf_ext1
WJetsToLNu
WJetsToLNu_ext2
WWToLNuQQ
WWToLNuQQ_AMCNLOFXFX
WZ
WZ_ext
ZZ
ZZ_ext1
WWW
WWZ
WZZ
ZZZ
WWG
WpWmJJ_EWK_QCD_noHiggs
)
source Add_VHtautauWWJJ.sh

#SAMPLES=(WJetsToLNu)

EXCLUDE=()

#--Run--#
SAMPLE_LIST=''
EXCLUDE_LIST=''
for s in ${SAMPLES[@]};do SAMPLE_LIST=${s}','${SAMPLE_LIST};done
for e in ${EXCLUDE[@]};do EXCLUDE_LIST=${e}','${EXCLUDE_LIST};done

#----Central
#mkPostProc.py -p Summer16_102X_nAODv5_Full2016v6 -i Prod -s MCl1loose2016v6 -T ${SAMPLE_LIST} -b
#mkPostProc.py -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6 -s MCCorr2016v6 -T ${SAMPLE_LIST} -b
#mkPostProc.py -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6 -s HMSemilepSkimJHv6_7 -T ${SAMPLE_LIST} -b
#mkPostProc.py -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6__HMSemilepSkimJHv6_7 -s HMlnjjVars_Dev_jhchoi7 -T ${SAMPLE_LIST} -b


#mkPostProc.py -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6__HMSemilepSkimJH2016v6_5 -s HMlnjjVars_Dev_jhchoi -T ${SAMPLE_LIST} -b
#mkPostProc.py -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6__HMSemilepSkimJH2016v6_5 -s HMlnjjVars_Dev_jhchoi2 -T ${SAMPLE_LIST} -b
modcfg="--modcfg SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200406_HMSemilepSKIMv6_10/Steps_cfg.py"
#mkPostProc.py ${modcfg} -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6 -s HMSemilepSKIMv6_10 -T ${SAMPLE_LIST} -b
modcfg="--modcfg SNuAnalytics/NanoGardenerModules/HMlnjjVars_Dev_jhchoi/Steps_cfg_HMlnjjVars_V11.py"
#mkPostProc.py ${modcfg} -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10 -s HMFull_V11_nom -T ${SAMPLE_LIST} -b
#mkPostProc.py ${modcfg} -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10 -s BWReweight -T ${SAMPLE_LIST} -b






##jetsys


mkPostProc.py ${modcfg} -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10 -s HMFull_V11_jetsysdown_uncorrelate -T ${SAMPLE_LIST} -b
mkPostProc.py ${modcfg} -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10 -s HMFull_V11_jetsysup_uncorrelate -T ${SAMPLE_LIST} -b

#mkPostProc.py ${modcfg} -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10 -s HMFull_V11_jetsysdown_correlate -T ${SAMPLE_LIST} -b
#mkPostProc.py ${modcfg} -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10 -s HMFull_V11_jetsysup_correlate -T ${SAMPLE_LIST} -b

mkPostProc.py ${modcfg} -p Summer16_102X_nAODv5_Full2016v6 -i MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10 -s HMFull_V11_fatjetsys -T ${SAMPLE_LIST} -b




#SAMPLE_LIST=ZZZ
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
    mkPostProc.py ${modcfg} -p Summer16_102X_nAODv5_Full2016v6 -i  MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10 -s ${sys} -b -T ${SAMPLE_LIST}
done




SAMPLES=()
EXCLUDE=()


unset -f condor_submit
