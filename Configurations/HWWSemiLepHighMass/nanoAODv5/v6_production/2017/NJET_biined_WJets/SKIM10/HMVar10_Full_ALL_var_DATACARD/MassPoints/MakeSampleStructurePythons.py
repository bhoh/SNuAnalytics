from List_MX import *
from List_MX_VBF import *


List_MX_common=list(set(List_MX).intersection(List_MX_VBF))

List_SampleTemplate=['samples_2017limit_MassTemplate_ele.py','samples_2017limit_MassTemplate_mu.py']
List_StructureTemplate=['structure_MassTemplate_ele.py','structure_MassTemplate_mu.py']




for MX in List_MX_common:

    print MX
    ##SampleTemplate
    for SampleTemplate in List_SampleTemplate:
        f_sample_template=open(SampleTemplate,'r')
        f_sample=open(SampleTemplate.replace('MassTemplate','M'+str(MX)),'w')
        
        sample_lines=f_sample_template.readlines()
        for line in sample_lines:
            if '__THIS_MASS__' in line:
                line=line.replace('__THIS_MASS__',str(MX))
            f_sample.write(line)
    
        f_sample_template.close()
        f_sample.close()

    ##StructureTemplate
    for StructureTemplate in List_StructureTemplate:
        f_structure_template=open(StructureTemplate,'r')
        f_structure=open(StructureTemplate.replace('MassTemplate','M'+str(MX)),'w')
        
        structure_lines=f_structure_template.readlines()
        for line in structure_lines:
            if '__THIS_MASS__' in line:
                line=line.replace('__THIS_MASS__',str(MX))
            f_structure.write(line)
        f_structure_template.close()
        f_sample.close()




    

