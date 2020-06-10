#!/usr/bin/env python

import sys
from batchTools  import *

if __name__ == '__main__':
    combine_base = '/cms/ldap_home/bhoh/HiggsCombTool/CMSSW_10_6_4/src/HiggsAnalysis/CombinedLimit'
    PWD = '/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv5/2017/StackNew_comb/scripts/batch'
    #
    # ---- stat only ----
    #options="--rAbsAcc 0 --rRelAcc 0.00500000001 --cminPreScan --cminPreFit 2 --cminDefaultMinimizerTolerance 0.1 --cminDefaultMinimizerType Minuit2 --cminDefaultMinimizerAlgo Simplex --cminFallbackAlgo Minuit2,1:1.0 --cminApproxPreFitTolerance 0 --X-rtd MINIMIZER_MaxCalls=9999999 --minosAlgo stepping --rMax 0.01 --verbose 9 --freezeNuisanceGroups theory,experimental "
    # ---- freeze nuisance group ----
    #options="--rAbsAcc 0 --rRelAcc 0.00500000001 --cminPreScan --cminPreFit 2 --cminDefaultMinimizerTolerance 0.1 --cminFallbackAlgo Minuit2,1:1.0 --cminApproxPreFitTolerance 0 --X-rtd MINIMIZER_MaxCalls=9999999 --minosAlgo bisection --rMax 0.01 --verbose 1 --freezeNuisanceGroups experimental "
    # --- all ---
    options="--rAbsAcc 0 --rRelAcc 0.00500000001 --cminPreScan --cminSingleNuisFit --cminDefaultMinimizerTolerance 0.1 --cminDefaultMinimizerType Minuit2 --cminDefaultMinimizerAlgo Simplex --cminFallbackAlgo GSLMultiMin,BFGS2,1:0.1 --minosAlgo bisection --rMax 0.01 --verbose 4 "
    #options="--rAbsAcc 0 --rRelAcc 0.001000000000000001 --cminPreScan --cminPreFit 1 --cminDefaultMinimizerTolerance 1.0 --cminFallbackAlgo Minuit2,1:1.0 --X-rtd MINIMIZER_MaxCalls=9999999 --minosAlgo bisection --rMax 0.01 -t 50 "
    seed = '12345'
    #nPoints = 1000
    #points = [0.00000000000001+0.00000000000001*i*i*i*i for i in range(nPoints)] # from 0.00001 to 500 points with 0.00005 steps
    #
    bpostFix=''
    tag = 'CHToCB'
    stepList   = ['ALL']
    targetList = [ '075', '080', '085', '090', '100', '110', '120', '130', '140', '150']
    #targetList = [ 'toy%s'%i for i in range(1) ]
    #targetList = [ 'point%s'%i for i in range(nPoints) ]
    jobs = batchJobs('mkCombine',tag,stepList,targetList,','.join(['Targets']),bpostFix,True)
    jobs.nThreads = 1
    jobs.AddPy2Sh()
    jobs.InitPy("import os, sys")
    jobs.InitPy('sys.path.append("{PWD}")'.format(PWD=PWD))
    #jobs.InitPy('os.system("%s")'%("cd {COMBINE_BASE}".format(COMBINE_BASE=combine_base)))
    #jobs.InitPy('os.system("%s")'%("eval `scramv1 ru -sh`"))
    jobs.InitPy("from doCombi_batch import LimitCalc")
    for i, iTarget in enumerate(targetList):
      #seed     = str(10000+i)
      options_ = options
      #options_ += ' --singlePoint %.14f'%(points[i])
      commend  = "#%s\n"%iTarget
      commend += "m = LimitCalc(False,'All','All','All','AsymptoticLimits',\"{OPTIONS}\",'','',False, '{SEED}')\n".format(OPTIONS=options_,SEED=seed)
      #mass = '120' # for test
      mass = iTarget
      commend += "m.SetMass('{MASS}')\n".format(MASS=mass)
      commend += "m.CombineCards(False)\n"
      commend += "m.Text_to_Workspace(False)\n"
      commend += "m.Combine(True)\n"
      jobs.AddPy(stepList[0],iTarget,"{COMMEND}".format(COMMEND=commend))
    jobs.Sub('','168:00:00',True)
