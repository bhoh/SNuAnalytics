pushd $1
getidx
popd
tar -cf $1.tar $1
scp $1.tar ${USER}@lxplus.cern.ch:/eos/user/j/jhchoi/www/HWW/
