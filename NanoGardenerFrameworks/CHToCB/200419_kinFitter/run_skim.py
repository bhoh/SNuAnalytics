import os, sys
import argparse
from samples_cfg import *


parser = argparse.ArgumentParser(description='run skim command')
parser.add_argument('-R', dest='R', action='store_true', default=False)
parser.add_argument('--dry-run', dest='pretend', action='store_true', default=False)
parser.add_argument('--samples', dest='samples', action='store', default='ALL')

opt = parser.parse_args()

run_keys = [
        #('2018','Autumn18_102X_nAODv6_Full2018v6','MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10','kinFitTTSemiLep_2018','MC'),
        #('2018','Autumn18_102X_nAODv6_Full2018v6','MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10','genCHToCB_2018','MC'),
        ('2018','Autumn18_102X_nAODv6_Full2018v6','MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__genCHToCB_2018','GenKinFitTTSemiLep_2018','MC'),
        #('2018','Autumn18_102X_nAODv6_Full2018v6','MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10','kinFitTTSemiLep_2018','MC_ttsyst'),
        #('2018','Autumn18_102X_nAODv6_Full2018v6','MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10','kinFitTTSemiLep_2018','MC_signal'),
        #('2018','Autumn18_102X_nAODv6_Full2018v6','MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10','genCHToCB_2018','MC_signal'),
        #('2018','Autumn18_102X_nAODv6_Full2018v6','MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__genCHToCB_2018','GenKinFitTTSemiLep_2018','MC_signal'),
        #('2018','Run2018_102X_nAODv6_Full2018v6','DATAl1loose2018v6__HMSemilepSKIMv6_10_data','kinFitTTSemiLep_2018','DATA'),
    ]

sleep_interval = {
        ('2018','Autumn18_102X_nAODv6_Full2018v6','MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10','kinFitTTSemiLep_2018','MC'):'5s',
        ('2018','Autumn18_102X_nAODv6_Full2018v6','MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10','kinFitTTSemiLep_2018','MC_ttsyst'):'5s',
        ('2018','Autumn18_102X_nAODv6_Full2018v6','MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10','kinFitTTSemiLep_2018','MC_signal'):'4h',
        ('2018','Run2018_102X_nAODv6_Full2018v6','DATAl1loose2018v6__HMSemilepSKIMv6_10_data','kinFitTTSemiLep_2018','DATA'):'5s',
    }

cmd_template = 'mkPostProc.py %s -p %s -i %s -s %s -b -T %s'
for key in run_keys:
    modCfg = ' '.join(modCfgs[key[0]][(key[1],key[4])])
    prod = key[1] #production
    inSkim = key[2] # input skim
    skim = key[3]  # skim to run
    if opt.samples=='ALL': # run for all samples defined in dictionary
      samples_string = ','.join(samples[key[0]][(key[1],key[4])])
    else: # run for opt.samples
      samples_string = opt.samples
    # fill commend template
    cmd = cmd_template%(modCfg,prod,inSkim,skim,samples_string)
    if opt.R:
        cmd += ' -R' #redo for existing skim
    if opt.pretend:
        cmd += ' --dry-run' # just creating running scripts
    print(cmd)
    os.system(cmd) # execute commend
    if key in sleep_interval:
        print('sleep for %s'%(sleep_interval[key]))
        os.system('sleep %s'%sleep_interval[key]) #sleep before next iteration




