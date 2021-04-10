pushd .;
echo $1
cd $1;
mkdir donefile;
mkdir hadd;
mkdir tmp1; hadd -j 10 -d tmp1 hadd1.root *DATA*.root;
mv hadd*.root hadd;
mv *DATA*.root donefile;
mkdir tmp2; hadd -j 10 -d tmp2 hadd2.root *TT*.root;
mv hadd*.root hadd;
mv *TT*.root donefile;
mkdir tmp3; hadd -j 10 -d tmp3 hadd3.root *CHToCB*.root;
mv hadd*.root hadd;
mv *CHToCB*.root donefile;
mkdir tmp4; hadd -j 10 -d tmp4 hadd4.root *.root;
mv hadd*.root hadd;
mv *.root donefile;
mkdir tmp5; hadd -j 10 -d tmp5 hadd.root hadd/*.root;
popd;
