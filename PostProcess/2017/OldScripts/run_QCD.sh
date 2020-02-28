# /xrootd//store/user/jhchoi/Latino/HWWNano/
# Sites_cfg: /xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/
# changed to /xrd/store/user/jhchoi/Latino/HWWNano/
# L1Loose


SAMPLES=(
QCD_HT200to300
QCD_HT300to500
QCD_HT700to1000
QCD_HT1000to1500
QCD_Pt-15to20_MuEnrichedPt5
QCD_Pt-20to30_MuEnrichedPt5
QCD_Pt-30to50_MuEnrichedPt5
QCD_Pt-50to80_MuEnrichedPt5
QCD_Pt-80to120_MuEnrichedPt5
QCD_Pt-120to170_MuEnrichedPt5
QCD_Pt-170to300_MuEnrichedPt5
#QCD_Pt-300to470_MuEnrichedPt5
#QCD_Pt-470to600_MuEnrichedPt5
QCD_Pt-20to30_EMEnriched
QCD_Pt-30to50_EMEnriched
QCD_Pt-50to80_EMEnriched
)

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


#--l1Prod--#
#mkPostProc.py -p Fall2017_102X_nAODv4_Full2017v4 -i Prod -s MCl1loose2017v2 -b -T ${SAMPLE_LIST}
mkPostProc.py -p Fall2017_102X_nAODv4_Full2017v5 -i Prod -s MCl1loose2017v5 -b -T ${SAMPLE_LIST}
#--Corr--#
#mkPostProc.py -p Fall2017_102X_nAODv4_Full2017v4 -i MCl1loose2017v2 -s MCCorr2017_SemiLep -b -T ${SAMPLE_LIST} -E ${EXCLUDE_LIST}
#mkPostProc.py -p Fall2017_102X_nAODv4_Full2017v5 -i MCl1loose2017v5 -s MCCorr2017v5 -b -T ${SAMPLE_LIST}

#--semilep--#
#mkPostProc.py -p Fall2017_102X_nAODv4_Full2017v5 -i MCl1loose2017v5__MCCorr2017v5 -s Semilep2017 -b -T ${SAMPLE_LIST}

#mkPostProc.py -p Fall2017_102X_nAODv4_Full2017v5 -i MCl1loose2017v5__MCCorr2017v5__Semilep2017 -s HMlnjjSel2017 -T ${SAMPLE_LIST} -b
#mkPostProc.py -p Fall2017_102X_nAODv4_Full2017v5 -i MCl1loose2017v5__MCCorr2017v5__Semilep2017 -s HMlnjjSel2017 -T ${SAMPLE_LIST} -b
#mkPostProc.py -p Fall2017_102X_nAODv4_Full2017v5 -i MCl1loose2017v5__MCCorr2017v5__Semilep2017 -s HMlnjjSel_New -T ${SAMPLE_LIST} -b




SAMPLES=()
EXCLUDE=()
