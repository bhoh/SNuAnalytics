#plot.py
#cuts_Boosted.py
import os
import sys
ListBoost=['Boosted','Resolved']
ListFlavor=['mu','ele','muele']
#ListProc=['GGF','VBF']
ListRegion=['TOP','SB','SR']


boosted=sys.argv[1]

print "[SpanPlotCut]",boosted

for flv in ListFlavor:
    for rg in ListRegion:

        os.system('cp plot.py '+'plot_'+boosted+'_'+flv+'_'+rg+'.py')
        #for proc in ListProc:
        os.system('cp cuts_'+boosted+'.py '+'cuts_'+boosted+'_'+rg+'_'+flv+'.py')
            #if boosted=="Resolved":os.system('cp cuts_Resolved.py '+'cuts_Resolved_'+flv+'_'+rg+'.py')
