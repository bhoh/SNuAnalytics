##----Which Region you are interested in--##
LIST_BST=['Boosted','Resolved']
LIST_REGION=['SB','TOP','SR']
###-----END---

import sys
import glob
##inputargument = yeartag
Year=str(sys.argv[1])
import os
import subprocess
from shutil import copyfile

##---change 
#WPandCut2016 -> WPandCut<Year>
#samples_2016 -> samples_<Year>
from ApplyYearTag import ApplyYearTag,ChangeString

##--create workspace area
workspace=os.getcwd()+'/../'+Year
scriptdir=workspace+'/script'
os.system('mkdir -p '+workspace)




##--cp configuration and variable
LIST_TEMPLATE=['configuration_template.py','variables_template.py']

for template in LIST_TEMPLATE:
    for bst in LIST_BST:
        for reg in LIST_REGION:
            newtemplate=workspace+'/'+template.replace('_template','_'+bst+'_'+reg)
            os.system('cp '+template+' '+newtemplate)
            ChangeString(newtemplate,'__REG__',reg)
            ChangeString(newtemplate,'__BST__',bst)
##--cp cuts
LIST_TEMPLATE=['cuts_Boosted_template.py','cuts_Resolved_template.py']
###----Make config/cuts
#for prod in LIST_PROD:
for reg in LIST_REGION:
    for template in LIST_TEMPLATE:
        #print template
        newtemplate=workspace+'/'+template
        newtemplate=newtemplate.replace('template.py',reg+'.py')

        ##--cp
        command='cp '+template+' '+newtemplate
        #print command
        
        if os.path.isfile(newtemplate):
            print '!!clean',newtemplate
            #os.system('rm '+newtemplate)
        os.system(command)
        #print 'cp ',template,newtemplate
        #copyfile(template,newtemplate)
        #subprocess.call(command.split(' '))
        ApplyYearTag(newtemplate,Year)
        ChangeString(newtemplate,'__REG__',reg)


##---cp directories

LIST_CPDIR=['JetPUID','MjjShapeWeight','PsScript','PdfQCDscaleScripts','SetupScripts','ShapeFromMela','SignalXsec','SysBranch','W_EWKNLO','script']
for cpdir in LIST_CPDIR:
    newdir=workspace+'/'+cpdir
    #if os.path.isdir(newdir):
    #    print "!!clean ",newdir
    #    os.system('rm -r '+newdir)
    #command='cp -r '+cpdir+' '+newdir
    #print command
    cplist=glob.glob(cpdir+'/*')
    for cp in cplist:
        command='cp '+cp+' '+newdir+'/'
        os.system(command)

    #ApplyYearTag
    pylist=glob.glob(newdir+'/*.py')
    shlist=glob.glob(newdir+'/*.sh')
    for f in pylist+shlist:
        ApplyYearTag(f,Year) ## 2016 -> <Year>


##--cp files
LIST_CP=['nuisances.py','aliases.py','plot.py']
for cp in LIST_CP:
    os.system('cp '+cp+' '+workspace+'/')
    newcp=workspace+'/'+cp
    ApplyYearTag(newcp,Year)
##---simple cp
LIST_CP=['samples_'+Year+'.py','WPandCut'+Year+'.py','TurnOnCombinedSamples.py','TurnOffCombinedSamples.py','Setup.sh','README.md','samples_test.py'] 
for cp in LIST_CP:
    os.system('cp '+cp+' '+workspace+'/')

##--cp workspace to workspace

os.system('cp '+workspace+'/nuisances.py '+workspace+'/nuisances_Boosted.py')
os.system('cp '+workspace+'/nuisances.py '+workspace+'/nuisances_Resolved.py')

os.system('cp '+workspace+'/aliases.py '+workspace+'/aliases_Boosted.py')
os.system('cp '+workspace+'/aliases.py '+workspace+'/aliases_Resolved.py')

##--cp MassPoints
os.system('rm -rf '+workspace+'/MassPoints')
os.system('cp -r MassPoints'+Year+' '+workspace+'/MassPoints')

##------RunningScript
#os.system('cp Histo_factory_run_test.sh '+scriptdir+'/')
#os.system('cp Histo_factory_run.sh '+scriptdir+'/')
##--Make PlotMakerRunning
LIST_FLV=['elemu','ele','mu']
LIST_BOOST=['Boosted','Resolved']
#LIST_REGION=['SB','SR','TOP']



os.system('mkdir -p logs/')
for reg in LIST_REGION:#configuration_Boosted_template.py
    for bst in LIST_BOOST:
        frun=open(scriptdir+'/RunPlotMakerRun_'+bst+'_'+reg+'.sh','w')    
        fsub=open(scriptdir+'/SubmitPlotMakerRun_'+bst+'_'+reg+'.sh','w')        
        for flv in LIST_FLV:
            f=open(scriptdir+'/PlotMakerRun_'+bst+'_'+reg+'_'+flv+'.sh','w')    
            os.system('cp '+workspace+'/plot.py '+workspace+'/plot_'+flv+'_'+bst+'.py')
            os.system('cp '+workspace+'/cuts_'+bst+'_'+reg+'.py '+workspace+'/cuts_'+bst+'_'+reg+'_'+flv+'.py')

            f.write('input=`ls rootFile*'+bst+'*'+reg+'*/hadd.root`\n')
            f.write('mkPlot.py --pycfg=configuration_'+bst+'_'+reg+'.py --inputFile=${input} --samplesFile=samples_'+Year+'_dummy.py --plotFile=plot_'+flv+'_'+bst+'.py --showIntegralLegend=1 --cutsFile=cuts_'+bst+'_'+reg+'_'+flv+'.py --outputDirPlots=plots_'+Year+'_'+bst+'_'+reg+'_'+flv+'\n')
            f.close()
            

            frun.write('source PlotMakerRun_'+bst+'_'+reg+'_'+flv+'.sh &> logs/PlotMakerRun_'+bst+'_'+reg+'_'+flv+'.log& \n')

            fsub.write('MYDIR=${PWD};command="cd ${MYDIR};source PlotMakerRun_'+bst+'_'+reg+'_'+flv+'.sh";python python_tool/ExportShellCondorSetup.py -c "${command}" -d workdir/workdir_PlotMakerRun_'+bst+'_'+reg+'_'+flv+' -n '+'PlotMakerRun_'+bst+'_'+reg+'_'+flv+'_'+Year+' -m 1 -s;')
        frun.close()

        
        #fsub.write('MYDIR=${PWD};command="input=`ls rootFile*'+bst+'*'+reg+'*/hadd.root;python python_tool/ExportShellCondorSetup.py -c "${command}" -d workdir/workdir_PlotMakerRun_'+bst+'_'+reg+' -n "PlotMakerRun_'+bst+'_'+reg+" -m 1')
        fsub.close()




##--aliasdir
aliasdir=workspace+'/myalias'
if os.path.isdir(aliasdir):
    os.system('rm -rf '+aliasdir)
os.system('cp -r myalias '+workspace+'/')
#ChangeString(file,from,to)
ChangeString(aliasdir+'/set_alias.sh','__MAINDIR__',workspace)
ChangeString(aliasdir+'/set_alias.sh','__YEAR__',Year)
##myalias
