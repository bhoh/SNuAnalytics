mkdir tmp
hadd -d tmp -j 4 hadd_0-0.root plots_*CHToCB*[0-4].root
hadd -d tmp -j 4 hadd_0-1.root plots_*CHToCB*[5-9].root
hadd -d tmp -j 4 hadd_1-0.root plots_*DATA*[0-4].root
hadd -d tmp -j 4 hadd_1-1.root plots_*DATA*[5-9].root
hadd -d tmp -j 4 hadd_2-0.root plots_*DY*[0-4].root
hadd -d tmp -j 4 hadd_2-1.root plots_*DY*[5-9].root
hadd -d tmp -j 4 hadd_3-0.root plots_*QCD*[0-4].root
hadd -d tmp -j 4 hadd_3-1.root plots_*QCD*[5-9].root
hadd -d tmp -j 4 hadd_4-0.root plots_*ST*[0-4].root
hadd -d tmp -j 4 hadd_4-1.root plots_*ST*[5-9].root
hadd -d tmp -j 4 hadd_5-0.root plots_*TTLJ*[0-4].root
hadd -d tmp -j 4 hadd_5-1.root plots_*TTLJ*[5-9].root
hadd -d tmp -j 4 hadd_6-0.root plots_*TTLL*[0-4].root
hadd -d tmp -j 4 hadd_6-1.root plots_*TTLL*[5-9].root
hadd -d tmp -j 4 hadd_7.root plots_*TTWjets*.root
hadd -d tmp -j 4 hadd_0.root plots_*TTZjets*.root
hadd -d tmp -j 4 hadd_8.root plots_*Wjets*.root
hadd -d tmp -j 4 hadd_9.root plots_*WW*.root
hadd -d tmp -j 4 hadd_10.root plots_*WZ*.root
hadd -d tmp -j 4 hadd_11.root plots_*ZZ*.root

hadd -d tmp -j 4 hadd.root hadd_*.root
