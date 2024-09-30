import ROOT

text_file = open("condor_GenerateToys.sh", "w")
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

# no SR
PARMS2='mask_Y2016HIPM__sng_4j_eleCH_3b=1,mask_Y2016HIPM__sng_4j_muCH_3b=1,mask_Y2016noHIPM__sng_4j_eleCH_3b=1,mask_Y2016noHIPM__sng_4j_muCH_3b=1,mask_Y2017__sng_4j_eleCH_3b=1,mask_Y2017__sng_4j_muCH_3b=1,mask_Y2018__sng_4j_eleCH_3b=1,mask_Y2018__sng_4j_muCH_3b=1,mask_Y2016HIPM__dbl_4j_ee=0,mask_Y2016HIPM__dbl_4j_mm=0,mask_Y2016noHIPM__dbl_4j_ee=0,mask_Y2016noHIPM__dbl_4j_mm=0,mask_Y2017__dbl_4j_ee=0,mask_Y2017__dbl_4j_mm=0,mask_Y2018__dbl_4j_ee=0,mask_Y2018__dbl_4j_mm=0,mask_Y2016HIPM__dbl_4j_em=0,mask_Y2016noHIPM__dbl_4j_em=0,mask_Y2017__dbl_4j_em=0,mask_Y2018__dbl_4j_em=0,mask_Y2018__dbl_4j_me=0,mask_Y2017__dbl_4j_me=0,mask_Y2016HIPM__dbl_4j_me=0,mask_Y2016HIPM__sng_4j_eleCH_2b=0,mask_Y2016HIPM__sng_4j_muCH_2b=0,mask_Y2016noHIPM__dbl_4j_me=0,mask_Y2016noHIPM__sng_4j_eleCH_2b=0,mask_Y2016noHIPM__sng_4j_muCH_2b=0,mask_Y2017__sng_4j_eleCH_2b=0,mask_Y2017__sng_4j_muCH_2b=0,mask_Y2018__sng_4j_eleCH_2b=0,mask_Y2018__sng_4j_muCH_2b=0'
#no MASK
PARMS3='mask_Y2016HIPM__sng_4j_eleCH_3b=0,mask_Y2016HIPM__sng_4j_muCH_3b=0,mask_Y2016noHIPM__sng_4j_eleCH_3b=0,mask_Y2016noHIPM__sng_4j_muCH_3b=0,mask_Y2017__sng_4j_eleCH_3b=0,mask_Y2017__sng_4j_muCH_3b=0,mask_Y2018__sng_4j_eleCH_3b=0,mask_Y2018__sng_4j_muCH_3b=0,mask_Y2016HIPM__dbl_4j_ee=0,mask_Y2016HIPM__dbl_4j_mm=0,mask_Y2016noHIPM__dbl_4j_ee=0,mask_Y2016noHIPM__dbl_4j_mm=0,mask_Y2017__dbl_4j_ee=0,mask_Y2017__dbl_4j_mm=0,mask_Y2018__dbl_4j_ee=0,mask_Y2018__dbl_4j_mm=0,mask_Y2016HIPM__dbl_4j_em=0,mask_Y2016noHIPM__dbl_4j_em=0,mask_Y2017__dbl_4j_em=0,mask_Y2018__dbl_4j_em=0,mask_Y2018__dbl_4j_me=0,mask_Y2017__dbl_4j_me=0,mask_Y2016HIPM__dbl_4j_me=0,mask_Y2016HIPM__sng_4j_eleCH_2b=0,mask_Y2016HIPM__sng_4j_muCH_2b=0,mask_Y2016noHIPM__dbl_4j_me=0,mask_Y2016noHIPM__sng_4j_eleCH_2b=0,mask_Y2016noHIPM__sng_4j_muCH_2b=0,mask_Y2017__sng_4j_eleCH_2b=0,mask_Y2017__sng_4j_muCH_2b=0,mask_Y2018__sng_4j_eleCH_2b=0,mask_Y2018__sng_4j_muCH_2b=0'

start_if = 'if [ $1 -eq {IDX} ]; then'
commend  = '  combine -M GenerateOnly -d {WS} --toysFrequentist --bypassFrequentistFit -t {N_TOYS} --saveToys --setParameters {PARAMS},BR={BR_value} -s {SEED} -n {BR} -m {MASS}'
end_if   = 'fi'

def getAsymResult(BR, mass):
  fname = "/cms_scratch/bhoh/toys/higgsCombineTest.AsymptoticLimits.mH{MASS}.root".format(MASS=mass)
  f     = ROOT.TFile(fname, "READ")
  t     = f.Get("limit")

  out_BR = None
  if BR == '0':
    out_BR = BR
  elif BR == '-1sigma':
    t.GetEntry(1)
    out_BR = t.limit
  elif BR == 'median':
    t.GetEntry(2)
    out_BR = t.limit
  elif BR == '1sigma':
    t.GetEntry(3)
    out_BR = t.limit
  elif BR == '0.01':
    out_BR = BR
  return str(out_BR)


idx = 0
out_string = ''
for mass in ['75', '80', '85', '90', '100', '110', '120', '130', '140', '150', '160']:
  for seed in range(50):
    for BR in ['0','-1sigma','median','1sigma']:
      ws = "morphedWorkspace_fitDiagnostics{MASS}.root".format(MASS=mass)
      BR_value = getAsymResult(BR,mass)
      out_string += start_if.format(IDX=idx)  + '\n'
      out_string += commend.format(WS=ws, N_TOYS=10, PARAMS=PARMS3, SEED=seed, MASS=mass, BR=BR, BR_value=BR_value)   + '\n'
      out_string += end_if    + '\n'
      # update index
      idx +=1

print>>text_file,out_string
text_file.close()

import os
os.system('chmod +x condor_GenerateToys.sh')
