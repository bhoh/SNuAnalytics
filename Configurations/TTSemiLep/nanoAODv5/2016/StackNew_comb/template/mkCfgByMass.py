#!/usr/bin/env python


template_directory = "."
save_directory = "../"

template_list = [
  "structure.py",
]

mass_list = ['075','080','085','090','100','110','120','130','140','150']

for template in template_list:
  for mass in mass_list:
    out_template = template.replace('.py','_M%s.py'%mass)
    with open(template_directory+'/'+template, 'r') as fIn:
      with open(save_directory+'/'+out_template, 'w') as fOut:
        for line in fIn.readlines():
          out = line.replace('<MASS>',mass)
          fOut.write(out)

