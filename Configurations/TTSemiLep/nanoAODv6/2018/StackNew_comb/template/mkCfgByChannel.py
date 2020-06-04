#!/usr/bin/env python


template_directory = "."
save_directory = "../"

template_list = [
  "configuration.py",
  "configuration_comb.py",
  "configuration_withSig.py",
  "configuration_PostFit_b.py",
  "configuration_PostFit_M130to150_b.py",
  "cuts.py",
  "nuisances_all.py",
  "plot_noSig.py",
  "plot.py",
  "plot_comb.py",
  "samples_2018.py",
  "variables.py",
]

channel_list = [
  ("","DATA"),
  ("_ele","SingleElectron"),
  ("_mu","SingleMuon"),
]

for template in template_list:
  for ch in channel_list:
    out_template = template.replace('.py','%s.py'%ch[0])
    with open(template_directory+'/'+template, 'r') as fIn:
      with open(save_directory+'/'+out_template, 'w') as fOut:
        for line in fIn.readlines():
          out = line.replace('<CH>',ch[0]).replace('<DATA>',ch[1])
          fOut.write(out)

