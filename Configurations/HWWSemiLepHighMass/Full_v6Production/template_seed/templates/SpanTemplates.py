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
LIST_CP=['FatJet_Jet_SysBranches.py','PowhegXsec.py','plot.py','MakeKfactor.py','MakeQCDscalePdfPsNuisancePy.py','variables_Boosted.py','variables_Resolved.py','Histo_factory_run.sh','nuisances.py','MakeMELAWeightCut.py','FilterMelaReweights.py','aliases.py']

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
