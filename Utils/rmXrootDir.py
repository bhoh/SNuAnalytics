from os import *
from os.path import *
mcDir='/xrootd/store/user/jhchoi/Latino/HWWNano/Run2017_102X_nAODv5_Full2017v6/DATAl1loose2017v6__HMSemilepSkimJHv6_7_data__HMlnjjVars_Dev'
#mcDir='/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSkimJHv6_7__HMlnjjVars_Dev'
#mcDir='/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__HMSemilepSkimJH2017v6_5__HMlnjjLepVetoBWRew__HMlnjjVars_Dev'
#mcDir='/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__Semilep2017__HMlnjjSelBWRew_Dev'
#mcDir='/xrootd/store/user/jhchoi/Latino/HWWNano/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__Semilep2017__HMlnjjSelBWRew_Dev__HMlnjjVarsGen'
#dataDir='/xrootd/store/user/jhchoi/Latino/HWWNano/Run2017_102X_nAODv4_Full2017v5/DATAl1loose2017v5__Semilep2017__HMlnjjSel2017'

targetDir = mcDir
#targetDir = dataDir


file_list = [f for f in listdir(targetDir) if isfile(join(targetDir, f))]

print file_list
yesNo = input('Do you really want to earase?["yes", "no"]')
if yesNo == 'yes':
  print 'Earasing directory',targetDir
  for afile in file_list:
    print 'removing', afile
    cmd = "xrdfs cms-xrdr.private.lo:2094 rm "+targetDir.replace("xrootd","xrd") +"/" + afile
    #print 'cmd',cmd
    system(cmd)
else: print 'Not removing', targetDir

lscmd = 'ls -ltrh '+targetDir
system(lscmd)
