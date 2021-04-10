#!/bin/bash
#export X509_USER_PROXY=/cms/ldap_home/bhoh/.proxy
#voms-proxy-info
#export SCRAM_ARCH=slc7_amd64_gcc820
#export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
#source $VO_CMS_SW_DIR/cmsset_default.sh
#cd /cms/ldap_home/bhoh/latinos/CMSSW_10_6_4
#eval `scramv1 ru -sh`
#ulimit -c 0

cd /cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/MVATool/scripts
python test_gpu_available.py

