import os 
#from os.path import *

inFile = open("failedJobFiles.txt","r")

file_list = inFile.read().splitlines()

print file_list
#yesNo = input('Do you really want to earase?["yes", "no"]')
#if yesNo == 'yes':
#  print 'Earasing directory',targetDir
for afile in file_list:
  print 'removing', afile
  cmd = "xrdfs cms-xrdr.private.lo:2094 rm "+ afile.replace("xrootd","xrd")
  print 'cmd',cmd
  os.system(cmd)
#else: print 'Not removing', targetDir
#
#lscmd = 'ls -ltrh '+targetDir
#system(lscmd)
