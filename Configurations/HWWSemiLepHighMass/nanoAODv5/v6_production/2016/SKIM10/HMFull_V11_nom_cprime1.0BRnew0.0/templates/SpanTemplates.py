
import os
LIST_TEMPLATE=['configuration_Boosted_template.py','configuration_Resolved_template.py','cuts_Boosted_template.py','cuts_Resolved_template.py']
#template='configuration_template.py'

#LIST_BOOST=['Boosted','Resolved']
LIST_PROD=['GGF','VBF']
LIST_REGION=['SB','TOP','SR']



for prod in LIST_PROD:
    for reg in LIST_REGION:
        for template in LIST_TEMPLATE:
            ftemplate=open(template,'r')
            lines=ftemplate.readlines()
            newfile=template.replace('template',prod+'_'+reg)
            fnew=open('../'+newfile,'w')
            for line in lines:
                line=line.replace('__PROD__',prod)
                line=line.replace('__REG__',reg)
                #line=line.replace('__PROD__',prod)
                fnew.write(line)
            #newfile=template.replace('template',prod+'_'+reg)
            os.system('cp '+template+' ../'+newfile)

