# /xrootd//store/user/jhchoi/Latino/HWWNano/
# Sites_cfg: /xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/
# changed to /xrd/store/user/jhchoi/Latino/HWWNano/
# L1Loose
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v4 -i Prod -s MCl1loose2016 -b





##--MCCorr2016_SemiLep--##
SAMPLES=()
'''
SAMPLES=(\
GluGluHToWWToLNuQQ_M125 GluGluHToWWToLNuQQ_M700 GluGluHToWWToLNuQQ_M4000 GluGluHToWWToLNuQQ_M5000 \
VBFHToWWToLNuQQ_M125 VBFHToWWToLNuQQ_M450 VBFHToWWToLNuQQ_M4000 VBFHToWWToLNuQQ_M5000\
WGJJ \
Zg \
WWToLNuQQ \
WWToLNuQQ_AMCNLOFXFX \
WZ \
WZ_ext \
WZ_AMCNLO \
WZTo2L2Q \
WZTo1L3Nu \
WZTo1L1Nu2Q \
ZZ \
Wg_MADGRAPHMLM \
Wg_AMCNLOFXFX \
Wg_AMCNLOFXFX_ext2 \
Wg_AMCNLOFXFX_ext3 \
QCD_Pt_15to20_bcToE \
QCD_Pt_20to30_bcToE \
QCD_Pt_30to80_bcToE \
QCD_Pt_80to170_bcToE \
QCD_Pt_170to250_bcToE \
QCD_Pt_250toInf_bcToE \
TTToSemiLeptonic \
ST_tW_antitop \
ST_tW_top \
ST_s-channel \
ST_t-channel_antitop \
ST_t-channel_top \
TTWJetsToLNu \
TTWJetsToQQ \
TTZToQQ \
TTZjets \
WJetsToLNu_HT70_100 \
WJetsToLNu_HT100_200 \
WJetsToLNu_HT100_200_ext1 \
WJetsToLNu_HT100_200_ext2 \
WJetsToLNu_HT200_400 \
WJetsToLNu_HT200_400_ext1 \
WJetsToLNu_HT200_400_ext2 \
WJetsToLNu_HT400_600 \
WJetsToLNu_HT400_600_ext1 \
WJetsToLNu_HT600_800 \
WJetsToLNu_HT600_800_ext1 \
WJetsToLNu_HT800_1200 \
WJetsToLNu_HT800_1200_ext1 \
WJetsToLNu_HT1200_2500 \
WJetsToLNu_HT1200_2500_ext1 \
WJetsToLNu_HT2500_inf \
WJetsToLNu_HT2500_inf_ext1 \
WJetsToLNu-LO \
WJetsToLNu-LO_ext2 \
WJetsToLNu \
WJetsToLNu_ext2 \
DYJetsToLL_M-10to50-LO \
DYJetsToLL_M-50-LO \
DYJetsToLL_M-50-LO_ext1 \
DYJetsToLL_M-50-LO_ext2 \
DYJetsToLL_M-10to50 \
DYJetsToLL_M-10to50_ext1 \
DYJetsToLL_M-50 \
DYJetsToLL_M-50_ext1 \
DYJetsToLL_M-50_ext2 \
DYJetsToLL_M-50-UEup \
DYJetsToLL_M-50-UEdo \
DYJetsToLL_M-50-PSup \
DYJetsToLL_M-50-PSdo \

)
'''
SAMPLES=(
WZ
WZ_ext
WZ_AMCNLO
WZTo1L1Nu2Q
ZZ
WW-LO
WW-LOext1
WWToLNuQQ
WWToLNuQQ_AMCNLOFXFX
TTToSemiLeptonic
TT_TuneCUETP8M2T4
ST_t-channel_top
ST_t-channel_antitop
ST_tW_antitop
ST_tW_top
ST_s-channel
ST_tW_antitop_noHad_ext1
ST_tW_antitop_noHad
ST_tW_top_noHad
ST_tW_top_noHad_ext1
TTWJetsToLNu
TTWJetsToQQ
TTZToQQ
TTZjets
TTZToLLNuNu_M-10_ext2
TTZToLLNuNu_M-10_ext3
WJetsToLNu
WJetsToLNu_ext2
WJetsToLNu-LO
WJetsToLNu-LO_ext2
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
QCD_Pt_15to20_bcToE
QCD_Pt_20to30_bcToE
QCD_Pt_30to80_bcToE
QCD_Pt_80to170_bcToE
QCD_Pt_170to250_bcToE
QCD_Pt_250toInf_bcToE
QCD_Pt-15to20_MuEnrichedPt5
QCD_Pt-20toInf_MuEnrichedPt15
QCD_Pt-20to30_EMEnriched
QCD_Pt-50to80_EMEnriched
QCD_Pt-50to80_EMEnriched_ext1
GluGluHToWWToLNuQQ_M125
GluGluHToWWToLNuQQ_M135
GluGluHToWWToLNuQQ_M140
GluGluHToWWToLNuQQ_M145
GluGluHToWWToLNuQQ_M160
GluGluHToWWToLNuQQ_M165
GluGluHToWWToLNuQQ_M170
GluGluHToWWToLNuQQ_M175
GluGluHToWWToLNuQQ_M180
GluGluHToWWToLNuQQ_M190
GluGluHToWWToLNuQQ_M200
GluGluHToWWToLNuQQ_M210
GluGluHToWWToLNuQQ_M250
GluGluHToWWToLNuQQ_M300
GluGluHToWWToLNuQQ_M350
GluGluHToWWToLNuQQ_M400
GluGluHToWWToLNuQQ_M500
GluGluHToWWToLNuQQ_M600
GluGluHToWWToLNuQQ_M700
GluGluHToWWToLNuQQ_M800
GluGluHToWWToLNuQQ_M900
GluGluHToWWToLNuQQ_M1500
GluGluHToWWToLNuQQ_M2000
GluGluHToWWToLNuQQ_M2500
GluGluHToWWToLNuQQ_M3000
GluGluHToWWToLNuQQ_M4000
GluGluHToWWToLNuQQ_M5000
VBFHToWWToLNuQQ_M120
VBFHToWWToLNuQQ_M124
VBFHToWWToLNuQQ_M125
VBFHToWWToLNuQQ_M140
VBFHToWWToLNuQQ_M160
VBFHToWWToLNuQQ_M165
VBFHToWWToLNuQQ_M190
VBFHToWWToLNuQQ_M200
VBFHToWWToLNuQQ_M230
VBFHToWWToLNuQQ_M250
VBFHToWWToLNuQQ_M300
VBFHToWWToLNuQQ_M350
VBFHToWWToLNuQQ_M400
VBFHToWWToLNuQQ_M450
VBFHToWWToLNuQQ_M550
VBFHToWWToLNuQQ_M600
VBFHToWWToLNuQQ_M650
VBFHToWWToLNuQQ_M700
VBFHToWWToLNuQQ_M800
VBFHToWWToLNuQQ_M1000
VBFHToWWToLNuQQ_M2000
VBFHToWWToLNuQQ_M2500
VBFHToWWToLNuQQ_M4000
VBFHToWWToLNuQQ_M5000
ggZH_HToWW_M125
HZJ_HToTauTau_M125
HWminusJ_HToWW_M125
HWplusJ_HToWW_M125
HWminusJ_HToTauTau_M125
HWplusJ_HToTauTau_M125
HZJ_HToWW_M120
HZJ_HToWW_M125
)
EXCLUDE=()



#--Run--#
SAMPLE_LIST=''
EXCLUDE_LIST=''
for s in ${SAMPLES[@]};do 
    if [ -z "${s}" ];then
	continue
    fi
    SAMPLE_LIST=${s}','${SAMPLE_LIST};
done
for e in ${EXCLUDE[@]};do 
    if [ -z "${e}" ];then
	continue
    fi
    EXCLUDE_LIST=${e}','${EXCLUDE_LIST};
done
#echo ${SAMPLE_LIST}
#echo ${EXCLUDE_LIST}


#--l1 prod--#
mkPostProc.py -p Summer16_102X_nAODv4_Full2016v4 -i Prod -s MCl1loose2016 -b -T ${SAMPLE_LIST}
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v4 -i Prod -s MCl1loose2016 -b

#--Corr Step--#
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v4 -i MCl1loose2016 -s MCCorr2016 -b -T ${SAMPLE_LIST}

#--add PreselFatJet--#
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v4 -i MCl1loose2016__MCCorr2016 -s FatJetPresel_semilep -T GluGluHToWWToLNuQQ_M5000
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v4 -i MCl1loose2016__MCCorr2016 -s FatJetPresel_semilep -T ${SAMPLE_LIST} -b
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v4 -i MCl1loose2016__MCCorr2016 -s FatJetPreselWlep_semilep -T ${SAMPLE_LIST} -b
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v4 -i MCl1loose2016__MCCorr2016 -s FatJetPreselCleaning_semilep -T ${SAMPLE_LIST} -b
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v4 -i MCl1loose2016__MCCorr2016 -s FatJetPreselCleaningWlep_semilep -T ${SAMPLE_LIST} -b
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v4 -i MCl1loose2016__MCCorr2016 -s FatJetPreselCleaningWlep_semilep -T ${SAMPLE_LIST} -b

#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v4 -i MCl1loose2016__MCCorr2016 -s FatJetPreselCleaning_semilep_v2 -T GluGluHToWWToLNuQQ_M5000
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v4 -i MCl1loose2016__MCCorr2016 -s FatJetPreselCleaning_semilep_v2 -T ${SAMPLE_LIST} -b
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v4 -i MCl1loose2016__MCCorr2016 -s preselfatjetMaker -T GluGluHToWWToLNuQQ_M5000

#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v4 -i MCl1loose2016__MCCorr2016__FatJetPreselCleaning_semilep_v2 -s wlepMaker -T ${SAMPLE_LIST} -b
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v4 -i MCl1loose2016__MCCorr2016__FatJetPreselCleaning_semilep_v2 -s wlepMaker -T GluGluHToWWToLNuQQ_M5000 



SAMPLES=()
EXCLUDE=()
