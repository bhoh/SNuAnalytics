DIRLIST=(2016 2017 2018)

for dir in ${DIRLIST[@]};do
    
    ##--
    pushd $dir
    mkdir -p logs
    (source Setup.sh;source script/Histo_factory_run_test.sh) &> logs/SetupAndTestSubmit.log&
    popd
done