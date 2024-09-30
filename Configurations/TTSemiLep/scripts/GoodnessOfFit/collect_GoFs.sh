#!/bin/sh
#ulimit -s unlimited
#set -e
cd /cms/ldap_home/bhoh/HiggsCombTool/CMSSW_10_6_4/src
#export SCRAM_ARCH=slc7_amd64_gcc820
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`

combineTool.py -M CollectGoodnessOfFit --input /cms_scratch/bhoh/toys/higgsCombine160.GoodnessOfFit.mH160.root /cms_scratch/bhoh/toys/higgsCombine0.GoodnessOfFit.mH160.*.root -m 160 -o gof.json



