
text_file = open("condor_SignalInjectionTest.sh", "w")
print>>text_file,'''#!/bin/sh
ulimit -s unlimited
set -e
cd /cms/ldap_home/bhoh/HiggsCombTool/CMSSW_10_6_4/src
export SCRAM_ARCH=slc7_amd64_gcc820
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
mkdir -p /cms_scratch/bhoh/toys
cd /cms_scratch/bhoh/toys

'''

#no MASK
PARMS3='mask_Y2016HIPM__sng_4j_eleCH_3b=0,mask_Y2016HIPM__sng_4j_muCH_3b=0,mask_Y2016noHIPM__sng_4j_eleCH_3b=0,mask_Y2016noHIPM__sng_4j_muCH_3b=0,mask_Y2017__sng_4j_eleCH_3b=0,mask_Y2017__sng_4j_muCH_3b=0,mask_Y2018__sng_4j_eleCH_3b=0,mask_Y2018__sng_4j_muCH_3b=0,mask_Y2016HIPM__dbl_4j_ee=0,mask_Y2016HIPM__dbl_4j_mm=0,mask_Y2016noHIPM__dbl_4j_ee=0,mask_Y2016noHIPM__dbl_4j_mm=0,mask_Y2017__dbl_4j_ee=0,mask_Y2017__dbl_4j_mm=0,mask_Y2018__dbl_4j_ee=0,mask_Y2018__dbl_4j_mm=0,mask_Y2016HIPM__dbl_4j_em=0,mask_Y2016noHIPM__dbl_4j_em=0,mask_Y2017__dbl_4j_em=0,mask_Y2018__dbl_4j_em=0,mask_Y2018__dbl_4j_me=0,mask_Y2017__dbl_4j_me=0,mask_Y2016HIPM__dbl_4j_me=0,mask_Y2016HIPM__sng_4j_eleCH_2b=0,mask_Y2016HIPM__sng_4j_muCH_2b=0,mask_Y2016noHIPM__dbl_4j_me=0,mask_Y2016noHIPM__sng_4j_eleCH_2b=0,mask_Y2016noHIPM__sng_4j_muCH_2b=0,mask_Y2017__sng_4j_eleCH_2b=0,mask_Y2017__sng_4j_muCH_2b=0,mask_Y2018__sng_4j_eleCH_2b=0,mask_Y2018__sng_4j_muCH_2b=0'


start_if = 'if [ $1 -eq {IDX} ]; then'
#commend  = '  combine -M GenerateOnly -d {WS} --toysFrequentist --bypassFrequentistFit -t {N_TOYS} --saveToys --setParameters {PARAMS},BR={BR} -s {SEED} -n {BR} -m {MASS}'
commend  = '  combine -M FitDiagnostics -d {WS} --toysFile higgsCombine{BR}.GenerateOnly.mH{MASS}.{SEED}.root -m {MASS} --toysFrequentist -t {N_TOYS} -n {MASS}_{BR}_{SEED} -s {SEED} --rMin -1 --setParameters {PARAMS} --cminDefaultMinimizerStrategy 0'
# --robustFit 1 --setRobustFitTolerance 0.1 --stepSize 0.1
end_if   = 'fi'

idx = 0
out_string = ''
for mass in ['75', '80', '85', '90', '100', '110', '120', '130', '140', '150', '160']:
  for seed in range(50):
    for BR in ['0','-1sigma','median','1sigma']:
      ws = "morphedWorkspace_fitDiagnostics{MASS}.root".format(MASS=mass)
      out_string += start_if.format(IDX=idx)  + '\n'
      out_string += commend.format(WS=ws, N_TOYS=10, SEED=seed, MASS=mass, BR=BR, PARAMS=PARMS3)   + '\n'
      out_string += end_if    + '\n'
      # update index
      idx +=1

print>>text_file,out_string
text_file.close()

import os
os.system('chmod +x condor_SignalInjectionTest.sh')
