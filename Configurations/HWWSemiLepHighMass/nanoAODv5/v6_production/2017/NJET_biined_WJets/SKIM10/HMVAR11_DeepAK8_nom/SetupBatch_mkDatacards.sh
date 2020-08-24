
SUBMIT=true
YEAR=2017

##--Make ARR_MASS
DefineList=`python MassPoints/List_MX_common.py`
#echo ARR_MASS=$DefineList                                                                                                                                                        
ARR_MASS=$DefineList

##--batch workdir
BatchDir="BatchDir"
mkdir -p $BatchDir
CURDIR=`pwd`

pushd $BatchDir
ARR_MASS=(1000)
for MX in ${ARR_MASS[@]};do
    exe=Run_mkDatacards_${MX}_exe.sh
    chmod u+x $exe
    echo '#!/bin/bash' > ${exe}
    echo "export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch" >> ${exe}
    echo "export X509_USER_PROXY=/cms/ldap_home/${USER}/.proxy" >> ${exe}
    echo "voms-proxy-info" >> ${exe}
    echo "export SCRAM_ARCH=${SCRAM_ARCH}" >> ${exe}
    echo "export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch" >> ${exe}
    echo 'source $VO_CMS_SW_DIR/cmsset_default.sh' >> ${exe}
    
    echo "cd ${CMSSW_BASE}/src;cd src/;eval `scramv1 ru -sh`">> ${exe}
    echo "cd ${CURDIR};" >> ${exe}
    echo "source Run_mkDatacards_MX.sh ${MX}" >> ${exe}
    echo "[ $? -eq 0 ] && mv ${BatchDir}/Run_mkDatacards_${MX}.jid ${BatchDir}/Run_mkDatacards_${MX}.done" >> ${exe}
    jds=Run_mkDatacards_${MX}.jds
    jid=Run_mkDatacards_${MX}.jid
    echo "executable = ${exe}" > ${jds}
    echo "output = Run_mkDatacards_${MX}.out" >> ${jds}
    echo "error = Run_mkDatacards_${MX}.err" >> ${jds}
    echo "log = Run_mkDatacards_${MX}.log" >> ${jds}
    echo "request_cpus = 1" >> ${jds}
    echo "accounting_group=group_cms " >> ${jds}
    echo "JobBatchName = Run_mkDatacards_${MX}_${YEAR}" >> ${jds}
    echo "queue" >> ${jds}

    if [ ${SUBMIT} = true ];then
	echo "condor_submit ${jds} &> ${jid}"
	condor_submit ${jds} &> ${jid}
    fi
done

popd
