import optparse
#nuisances.py

def MakeNuisancePy(SYSLIST,ALIAS):
    #SYSLIST=[]
    #ALIAS='test'
    f=open('nuisances.py','r')
    fnew=open('nuisances_'+ALIAS+'.py','w')
    
    lines=f.readlines()
    for line in lines:
        fnew.write(line)
        
        
    #for sys in SYSLIST:
    fnew.write("SYSLIST="+str(SYSLIST)+'\n')
    fnew.write('''
NUILIST=sorted(nuisances)
for nui in NUILIST:
      if not nui in SYSLIST:
        del nuisances[nui] 
    ''')
    f.close()
    fnew.close()
    print 'nuisances_'+ALIAS+'.py'
def MakeConfigPy(configpy,alias):
    #configuration_Boosted.py
    f=open(configpy,'r')
    newconfigpy=configpy.split('.py')[-2]+'_'+alias+'.py'
    print newconfigpy
    fnew=open(newconfigpy,'w')
    lines=f.readlines()
    for line in lines:
        fnew.write(line)
    fnew.write("outputDirPlots=plots_"+newconfigpy.replace('.py',''))
    f.close()
    fnew.close()
    
def ExportPlotMakerShell(plotmaker,alias,configpy):
    f=open(plotmaker,'r')
    newplotmaker=plotmaker.split('.sh')[-2]+'_'+alias+'.sh'
    print newplotmaker
    fnew=open(newplotmaker,'w')

    lines=f.readlines()
    for line in lines:
        if 'mkPlot.py' in line:
            line=line.replace('mkPlot.py','mkPlot.py --nuisancesFile=nuisances_'+alias+'.py')
        if ".log" in line:
            line=line.replace('.log','_'+alias+'.log')
        if '--pycfg' in line:
            
            line=line.replace('--pycfg='+configpy, "--pycfg="+configpy.split('.py')[-2]+'_'+alias+'.py')
        fnew.write(line)
    f.close()
    fnew.close()
    print newplotmaker,"is created"

if __name__ == '__main__':
   usage = 'usage: %prog [options]'
   parser = optparse.OptionParser(usage)
   parser.add_option("-s","--syslist",   dest="syslist", help="sys list")
   parser.add_option("-c","--confpy",   dest="configpy", help="configpy")
   parser.add_option("-a","--alias",   dest="alias", help="alias of this group")
   parser.add_option("-p","--plotmaker",   dest="plotmaker", help="plot maker shell to mimic")
   (options, args) = parser.parse_args()
   syslist=options.syslist
   syslist=syslist.split(',')
   alias=options.alias
   plotmaker=options.plotmaker
   configpy=options.configpy
   print '==-----=='
   print syslist
   print alias
   print plotmaker
   print configpy
   MakeNuisancePy(syslist,alias)
   ExportPlotMakerShell(plotmaker,alias,configpy)
   MakeConfigPy(configpy,alias)
