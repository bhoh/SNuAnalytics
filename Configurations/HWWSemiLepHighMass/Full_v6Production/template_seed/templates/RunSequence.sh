#00) Make configuration
echo "Make configuration ==============================="
echo "Your choice if you use SpanTemplates.py or SpanTemplates_incConfDir.py"
#pushd templates
#python SpanTemplates.py 2017
#popd

echo "Using SpanTemplates_incConfDir.py"
python SpanTemplates_incConfDir.py 2017


<<Comment1
Comment1

<<Comment2
#0)Predefine
echo "Making kfactor ===================================="
#python MakeKfactor.py
#-Melacut 
#>python MakeMELAWeightCut.py
#-QCD/PDF/PS
python MakeQCDscalePdfPsNuisancePy.py
#--Make dummy version of sample.py for  improvement of speed and batch run 
python MakeDummySamplePY.py
#--python tool repository
git clone git@github.com:soarnsoar/python_tool.git

Comment2

<<Comment3
#1)HistoFactory
echo 'Making Histograms'

#->[Please Check] actually defined at WPandCut2017
#>>UseRegroupJES=True in nuisances.py
#>>CombineMultiV=False , CombineWjets=False in nuisances.py & sample_2018.py, CombineH125 =False
#HistoFactory.sh
. Histo_factory_run.sh

2)Make PDF/QCD scale shape
>>git clone git@github.com:soarnsoar/python_tool.git
>>[2016]RunMakeQCDscale_Rms_Shape.sh
>>[2017/2018]RunMakeQCDscale_SymhessianAs_Shape.sh


2-1)Combine ggWW--
>>a)Check high stat mass points
>>RunCheckEntriesInSR_per_process.sh
>>>cat rootFile*Boosted*/hadddir_ggHWWlnuqq_M*/*.txt
>>>cat rootFile*Resolved*/hadddir_ggHWWlnuqq_M*/*.txt
>>choose the mass points to use for ggWW and make list in Make_ggww_shape.sh

b)Haddgghww125Shape.sh
>>check by 
cat rootFile*Boosted*/hadddir_ggHWWlnuqq_M125/*.err
cat rootFile*Resolved*/hadddir_ggHWWlnuqq_M125/*.err

>>c)combine high stat samples
>>after finishing hadd condorjob
>>Make_ggww_shape.sh

2-1-1)Combine qqWWqq using vbs and vbfh125
>>Hadd_qqWWqqShape.sh
----after finishing qqWWqq hadd condorjobs
>>Make_qqwwqq_shape.sh

2-2)Combine VV,Wjets,h125
a)Make hadd files for each process
>>source HaddWjetsH125MultiV.sh

b)Make Combined Shapes
after finishing haddwjetsh125multiv condorjob
>>MakeWjetsH125MultiVShape.sh
~3min (maximum)

2-3)Make SBI shape using S/I/ggWW,WWJJ/h125
a)Make hadd files for S,B,I
>>source HaddSBI.sh

b)Make SBI Shapes
>>after finishing hadd condorjob
>>source MakeSBIshape.sh
~12min

3)Hadd
>HaddInBatch.sh

5-1)Draw plots
[in plot.py,nuisances.py]CombineMultiV=True , CombineWjets=True in nuisances.py & sample_2017.py, CombineH125 =True

Comment3
