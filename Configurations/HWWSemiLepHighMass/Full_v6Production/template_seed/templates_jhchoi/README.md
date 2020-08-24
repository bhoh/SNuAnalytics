##----Make workspace
python SpanTemplates.py 2016
##workspace=../2016



##---go to workspace
cd ../2016


##---setup
source Setup.sh

##---TestRun
source script/Histo_factory_run_test.sh &> logs/Histo_factory_run_test.log&

##---Submit
source script/Histo_factory_run.sh &> logs/Histo_factory_run.log&


##---PDF/QCDscale
python PdfQCDscaleScripts/RunMakeQCDscale_SymhessianAs_Shape.py sub


##---ggww qqwwqq from mela
python ShapeFromMela/Run_Make_ggww_qqwwqq_shape.py
->>Check jobs by whether there's no remaining jidfile


##---Make SBI shape
python ShapeSBI/Run_Make_sbi.py
->>Check jobs by whether there's no remaining jidfile

##---Hadd
source script/HaddInBatch.sh