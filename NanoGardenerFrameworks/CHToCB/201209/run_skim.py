import os, sys
import argparse
from samples_cfg import *
from aliases_cfg import *


parser = argparse.ArgumentParser(description='run skim command')
parser.add_argument('-R', dest='R', action='store_true', default=False)
parser.add_argument('--dry-run', dest='pretend', action='store_true', default=False)
parser.add_argument('--samples', dest='samples', action='store', default='ALL')
parser.add_argument('--aliases', dest='aliases', action='store', default='ALL')
parser.add_argument('--years', dest='years', action='store', default='ALL')

opt = parser.parse_args()



cmd_template = 'mkPostProc.py %s -p %s -i %s -s %s -b -T %s'

#
run_keys_ = []
if opt.aliases=='ALL':
  for key in aliases:
    run_keys_.extend(aliases[key])
else:
  aliases_keys = str(opt.aliases).split(',')
  for key in aliases_keys:
    run_keys_.extend(aliases[key])


for key in run_keys_:
    modCfg = ' '.join(modCfgs[key[0]][(key[1],key[4])])
    prod = key[1] #production
    inSkim = key[2] # input skim
    skim = key[3]  # skim to run
    if opt.samples=='ALL': # run for all samples defined in dictionary
      samples_string = ','.join(samples[key[0]][(key[1],key[4])])
    else: # run for opt.samples
      samples_string = opt.samples

    # skip years not specified
    if opt.years=='ALL':
      pass
    else:
      years = str(opt.years).split(',')
      if key[0] not in years:
        print("skip year:    ",  key)
        continue

    # fill commend template
    cmd = cmd_template%(modCfg,prod,inSkim,skim,samples_string)
    if opt.R:
      cmd += ' -R' #redo for existing skim
    if opt.pretend:
      cmd += ' --dry-run' # just creating running scripts
    if 'UEPS' in opt.aliases:
      cmd += ' | tee %s_%s.log &'%(prod,inSkim)  #run in bkg jobs
      print(cmd)
      os.system(cmd) # execute commend
      os.system('sleep 3m')
    else:
      print(cmd)
      os.system(cmd) # execute commend


