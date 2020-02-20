from List_MX import *

SampleTemplate='samples_2018limit_MassTemplate.py'
StructureTemplate='structure_MassTemplate.py'


#List_MX=[200,210,250,300,350,400,500,550,600,650,700,750,800,900,1500,2000,2500,3000,4000,5000]
#List_MX=[200,210,250,300,350,400,500,550,600,650,700,750,800,900,1500,2000,2500,3000,4000,5000]
for MX in List_MX:


    ##SampleTemplate
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
    f_structure_template=open(StructureTemplate,'r')
    f_structure=open(StructureTemplate.replace('MassTemplate','M'+str(MX)),'w')
    
    structure_lines=f_structure_template.readlines()
    for line in structure_lines:
        if '__THIS_MASS__' in line:
            line=line.replace('__THIS_MASS__',str(MX))
        f_structure.write(line)
    f_structure_template.close()
    f_sample.close()




    

