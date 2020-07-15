import sys
Year=str(sys.argv[1])
import os
LIST_TEMPLATE=['configuration_Boosted_template.py','configuration_Resolved_template.py','cuts_Boosted_template.py','cuts_Resolved_template.py']
#template='configuration_template.py'

#LIST_BOOST=['Boosted','Resolved']
#LIST_PROD=['GGF','VBF']
LIST_REGION=['SB','TOP','SR']


###----Make config/cuts
#for prod in LIST_PROD:
for reg in LIST_REGION:
    for template in LIST_TEMPLATE:
        ftemplate=open(template,'r')
        lines=ftemplate.readlines()
        newfile=template.replace('template',reg)
        fnew=open('../'+newfile,'w')
        for line in lines:
            #line=line.replace('__PROD__',prod)
            line=line.replace('__REG__',reg)
            line=line.replace('WPandCut2016','WPandCut'+Year)
            #line=line.replace('__PROD__',prod)
            fnew.write(line)
        #newfile=template.replace('template',prod+'_'+reg)
        os.system('cp '+template+' ../'+newfile)
        fnew.close()
        ftemplate.close()
##---cp
#FatJet_Jet_SysBranches.py
#PowhegXsec.py
#plot.py
#MakeKfactor.py
LIST_CP=['FatJet_Jet_SysBranches.py','PowhegXsec.py','plot.py','MakeKfactor.py','MakeQCDscalePdfPsNuisancePy.py','variables_Boosted.py','variables_Resolved.py','Histo_factory_run.sh','nuisances.py','MakeMELAWeightCut.py','FilterMelaReweights.py','aliases.py','MakeDummySamplePY.py']

for cp in LIST_CP:
    ftemplate=open(cp,'r')
    fnew=open('../'+cp,'w')
    lines=ftemplate.readlines()
    for line in lines:
        line=line.replace('WPandCut2016','WPandCut'+Year)
        line=line.replace('samples_2016','samples_'+Year)
        fnew.write(line)

    ftemplate.close()
    fnew.close()

##---simple cp
LIST_CP=['samples_'+Year+'.py','LHEPartWlepPt.cc','WPandCut'+Year+'.py','TurnOnCombinedSamples.py','TurnOffCombinedSamples.py','GetXsecInNtuple.py','MakeSampleDict.py','ngenjet.cc'] 
for cp in LIST_CP:
    os.system('cp '+cp+' ../')

##--cp module
os.system('cp LHEPartWlepPt.cc ../')

##--cp WPfile
os.system('cp WPandCut'+Year+'.py ../')

##--cp MassPoints
os.system('rm -rf ../MassPoints')
os.system('cp -r MassPoints'+Year+' ../MassPoints')

##--cp TurnOn/OffCombinedSamples.py
os.system('cp TurnOnCombinedSamples.py ../')
os.system('cp TurnOffCombinedSamples.py ../')
os.system('cp GetXsecInNtuple.py ../')

##--Make PlotMakerRunning
LIST_FLV=['elemu','ele','mu']
LIST_BOOST=['Boosted','Resolved']
#LIST_REGION=['SB','SR','TOP']

os.system('mkdir -p logs/')
for reg in LIST_REGION:#configuration_Boosted_template.py
    for bst in LIST_BOOST:
        frun=open('../RunPlotMakerRun_'+bst+'_'+reg+'.sh','w')    
        fsub=open('../SubmitPlotMakerRun_'+bst+'_'+reg+'.sh','w')        
        for flv in LIST_FLV:
            f=open('../PlotMakerRun_'+bst+'_'+reg+'_'+flv+'.sh','w')    
            os.system('cp ../plot.py ../plot_'+flv+'_'+bst+'.py')
            os.system('cp ../cuts_'+bst+'_'+reg+'.py ../cuts_'+bst+'_'+reg+'_'+flv+'.py')

            f.write('input=`ls rootFile*'+bst+'*'+reg+'*/hadd.root`\n')
            f.write('mkPlot.py --pycfg=configuration_'+bst+'_'+reg+'.py --inputFile=${input} --plotFile=plot_'+flv+'_'+bst+'.py --cutsFile=cuts_'+bst+'_'+reg+'_'+flv+'.py --outputDirPlots=plots_'+Year+'_'+bst+'_'+reg+'_'+flv+'\n')
            f.close()
            

            frun.write('source PlotMakerRun_'+bst+'_'+reg+'_'+flv+'.sh &> logs/PlotMakerRun_'+bst+'_'+reg+'_'+flv+'.log& \n')

            fsub.write('MYDIR=${PWD};command="cd ${MYDIR};source PlotMakerRun_'+bst+'_'+reg+'_'+flv+'.sh";python python_tool/ExportShellCondorSetup.py -c "${command}" -d workdir/workdir_PlotMakerRun_'+bst+'_'+reg+'_'+flv+' -n '+'PlotMakerRun_'+bst+'_'+reg+'_'+flv+' -m 1 -s;')
        frun.close()

        




        
        #fsub.write('MYDIR=${PWD};command="input=`ls rootFile*'+bst+'*'+reg+'*/hadd.root;python python_tool/ExportShellCondorSetup.py -c "${command}" -d workdir/workdir_PlotMakerRun_'+bst+'_'+reg+' -n "PlotMakerRun_'+bst+'_'+reg+" -m 1')
        fsub.close()
