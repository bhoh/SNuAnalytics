pushd plots_semilep/
getidx
popd
tar -cf plots_semilep.tar plots_semilep/
scp plots_semilep.tar ${USER}@lxplus.cern.ch:/eos/user/j/jhchoi/www/HWW/
