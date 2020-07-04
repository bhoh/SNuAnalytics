#
#parser.add_argument("-f", dest='histofile')
#parser.add_argument("-p", dest='process')
#parser.add_argument("-c", dest='cutname')
#parser.add_argument("-v", dest='varname')
#parser.add_argument("-n", dest='nuisance')

#histofile=old2/rootFile_2017_Boosted_SKIM10_HMVar10_Full_SBI/hadd.root
histofile=rootFile_2017_Boosted_SKIM10_HMVar10_Full_SBI/plots_2017_Boosted_SKIM10_HMVar10_Full_SBI_ALL_WWJJ.root
#process=top
process=WWJJ
cut=___BoostedGGF__SR__METOver40__PtOverM04___
varname=Event
nuisance=QCDscaleAccept
nuisance=pdfAccept
nuisance=CMS_fatjmr_2017
#nuisance=CMS_jesAbsolute
echo $histofile
echo $process
echo $cut
echo $varname
echo $nuisance

python python_tool/latino/CheckNuisanceImpact.py -f $histofile -p $process -c $cut -v $varname -n $nuisance
