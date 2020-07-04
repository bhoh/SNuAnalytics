#   parser.add_option("-c","--command",   dest="command", help="command to run")
#   parser.add_option("-d","--workdir",   dest="workdir", help="workarea")
#   parser.add_option("-s","--submit",   dest="submit",action="store_true", help="submit",default=False)

#python python_tool/ExportShellCondorSetup.py
CURDIR=$PWD
mycommand="cd $CURDIR;python python_tool/latino/CombineShapesNewOutput.py -c configuration_Boosted.py -f rootFile_2017_Boosted_SKIM10_HMVar10_Full_SBI/hadd.root -s ggHWWlnuqq_M400_S,ggHWWlnuqq_M400_I,ggWW,h125 -n ggHWWlnuqq_M400_SBI"
python python_tool/ExportShellCondorSetup.py -c "$mycommand" -d "test_dir" -s -n testexportshell
