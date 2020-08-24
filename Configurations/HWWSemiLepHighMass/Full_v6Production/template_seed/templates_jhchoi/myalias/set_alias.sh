#MAINDIR=__MAINDIR__


alias submit_test__YEAR__="cd __MAINDIR__;source script/Histo_factory_run_test.sh;cd -"
alias standalonetest__YEAR__='cd __MAINDIR__;source script/Histo_factory_run_test_standalone.sh;cd -'

function submitshape__YEAR__(){
    
    BST=$1
    REG=$2

    echo "------------"
    echo "Submit HistoFactory"
    echo "Boosted/Resolved -> "$BST
    echo "Region (SB/SR/TOP)-> "$REG
    echo "[DIR]""__MAINDIR__"
    cd __MAINDIR__
    source script/Histo_factory_run_BST_REG.sh $BST $REG
    cd -
}

