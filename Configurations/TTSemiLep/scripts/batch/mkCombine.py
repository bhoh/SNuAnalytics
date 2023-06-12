#!/usr/bin/env python

import sys
from batchTools  import *
from datacards import datacards
from options import options
from doCombi_batch import base_dir
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TrueOrNotTrue')
    parser.add_argument('--dry-run',dest='dryrun',help="False or True", default=False, action='store_true')

    args = parser.parse_args()


    combine_base = '/cms/ldap_home/bhoh/HiggsCombTool/CMSSW_10_6_4/src/HiggsAnalysis/CombinedLimit'
    PWD = '/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/batch'
    
    seed = '12349'
    #nPoints = 1000
    #points = [0.00000000000001+0.00000000000001*i*i*i*i for i in range(nPoints)] # from 0.00001 to 500 points with 0.00005 steps
    #

    #
    bpostFix=''

    for tag in datacards:
      ###
      job_tag = tag
      stepList   = ['ALL']
      #targetList = [ '080' ]
      #targetList = [ '120' ]
      #targetList = [ '080', '085', '090', '100', '110', '120', '130', '140', '150', '160']
      targetList = [ '075', '080', '080_yield', '085', '090', '100', '110', '120', '130', '140', '150', '160']
      #targetList = [ 'toy%s'%i for i in range(1) ]
      #targetList = [ 'point%s'%i for i in range(nPoints) ]
      jobs = batchJobs('mkCombine',job_tag,stepList,targetList,','.join(['Targets']),bpostFix,True)
      jobs.nThreads = 1
      jobs.AddPy2Sh()
      jobs.InitPy("import os, sys")
      jobs.InitPy('sys.path.append("{PWD}")'.format(PWD=PWD))
      #jobs.InitPy('os.system("%s")'%("cd {COMBINE_BASE}".format(COMBINE_BASE=combine_base)))
      #jobs.InitPy('os.system("%s")'%("eval `scramv1 ru -sh`"))
      jobs.InitPy("from doCombi_batch import LimitCalc")
      for i, iTarget in enumerate(targetList):
        #seed     = str(10000+i)
        options_ = options[tag]['options']
        method_  = options[tag]['method']
        #options_ += ' --singlePoint %.14f'%(points[i])
        commend  = "#%s\n"%iTarget
        commend += "m = LimitCalc(False,'All','All',\"{METHOD}\",\"{OPTIONS}\",'','',False, '{SEED}')\n".format(METHOD=method_,OPTIONS=options_,SEED=seed)
        #mass = '120' # for test
        mass = iTarget
        commend += "m.SetMass('{MASS}')\n".format(MASS=mass)
        commend += "m.CombineCards('{TAG}','{MASS}',True)\n".format(TAG=tag,MASS=mass)
        commend += "m.Text_to_Workspace('{TAG}','{MASS}',True)\n".format(TAG=tag,MASS=mass)
        if not args.dryrun:
          commend += "m.Combine('{TAG}','{MASS}',True)\n".format(TAG=tag,MASS=mass)
        else:
          commend += "m.Combine('{TAG}','{MASS}',False)\n".format(TAG=tag,MASS=mass)
        jobs.AddPy(stepList[0],iTarget,"{COMMEND}".format(COMMEND=commend))
      jobs.Sub('','168:00:00',True)
