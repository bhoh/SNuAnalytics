
#for nuis in CMS_btag_cferr1 CMS_btag_hfstats2_2017 CMS_btag_lfstats1_2017 CMS_btag_lfstats2_2017 CMS_eff_ele_2016 CMS_eff_ele_2017 CMS_jer_2016 CMS_jesAbsolute_2016 CMS_jesAbsolute_2018 CMS_jesEC2_2017 CMS_jesEC2_2018 CMS_ttbar_isr lumi_13TeV_Ghosts
for nuis in CMS_ttbar_isr
do
    combine -M MultiDimFit -n _paramFit_Test_$nuis --algo impact --redefineSignalPOIs BR10ToMinus7 -P $nuis  --floatOtherPOIs 1 --saveInactivePOI 1 --robustFit 1 --points 50000 -t -1 -m 130 -d ../workspace/M130Y2016muCH4j2b__4j3b__eleCH4j2b__4j3b__Y2017muCH4j2b__4j3b__eleCH4j2b__4j3b__Y2018muCH4j2b__HEMveto4j3b__HEMvetoeleCH4j2b__HEMveto4j3b__HEMveto.txt.root --cminPreScan --cminPreFit 1
done
