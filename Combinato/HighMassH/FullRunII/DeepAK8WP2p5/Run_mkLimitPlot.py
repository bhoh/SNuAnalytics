import os
import sys
import ROOT


##--Read SMLike Higgs Xsec
sys.path.insert(0,os.getcwd())
sys.path.insert(0,os.getcwd()+'/../')
from mkLimitPlot import *
sys.path.insert(0,os.getcwd()+'/../data/SMLike')
sys.path.insert(0,os.getcwd()+'/../data/')


from XSEC import HWW_XSEC as SMLike_XSEC
#print SMLike_XSEC

##---Make Configuration
if __name__ == '__main__':

    '''                                                                                                                                                                                                         conf= {                                                                                                                                                                                                     'alias':alias, in legend                                                                                                                                                                                   'xlist':[],                                                                                                                                                                                                'ylist':[],                                                                                                                                                                                                'linecolor':[]                                                                                                                                                                                             'linestyle':[]                                                                                                                                                                                             'fillcolor':[]                                                                                                                                                                                             'drawoption':'l same' '3 same'                                                                                                                                                                             'optcommand':command to be exec(string)                                                                                                                                                                    }                                                                                                                                                                                                       
    '''



    ##---Read SM-Like
    #SMLike_XSEC['GGF'][130]=xsec
    
    xlist_SMLike=sorted(list(set(SMLike_XSEC['GGF']).intersection(set(SMLike_XSEC['VBF']))))
    ylist_SMLike=[]
    for mass in xlist_SMLike:
        ylist_SMLike.append(SMLike_XSEC['GGF'][mass]+SMLike_XSEC['VBF'][mass])

    SMLike={
        'alias':'SM-Like Scenario',
        'xlist':xlist_SMLike,
        'ylist':ylist_SMLike,
        'linecolor':2,
        'linestyle':1,
        'fillcolor':0,
        'drawoption':'l same',
        
    }


    ##---Read floating
    #XWW={130: {'Resolved': {'commbine': {'2017': {'exp84': 299.0888
    #Limit/AsymptoticLimit__floating.py
    #sys.path.insert(0,'Limit')
    #from AsymptoticLimit__floating import XWW as XWW2016
    Read=open('Limit/AsymptoticLimit__floating.py','r')
    exec(Read)
    Read.close()
    XWW2016=XWW
    del XWW


    xlist_2016=[]
    ylist_2016=[]
    for mass in sorted(XWW2016):
        if not 'Boosted' in XWW2016[mass]:continue
        if not '2016' in XWW2016[mass]['Boosted']['commbine'] : continue
        xlist_2016.append(mass)
        ylist_2016.append(XWW2016[mass]['Boosted']['commbine']['2016']['exp50'])
        #ylist_2016.append(XWW2016[mass]['Boosted']['combine']['2016']['exp50'])
    NomBoosted2016={
        'alias':'Boosted, 2016',
        'xlist':xlist_2016,
        'ylist':ylist_2016,
        'linecolor':1,
        'linestyle':2,
        'fillcolor':0,
        'drawoption':'l same'
    }
    
    ##---END

    ##--BestLimit
    #XWW={130: {'exp84': 299.0888,
    #sys.path.insert(0,'BestLimit')
    #from AsymptoticLimit__floating import XWW as XWWBest
    #print XWWBest
    Read=open('BestLimit/AsymptoticLimit__floating.py','r')
    exec(Read)
    Read.close()
    XWWBest=XWW
    del XWW

    xlist_best=[]
    ylist_best=[]
    for mass in sorted(XWWBest):
        if not 'exp50' in XWWBest[mass]: continue
        print mass
        xlist_best.append(mass)
        ylist_best.append(XWWBest[mass]['exp50'])

    NomBest={
        'alias':'best among 3yrs',
        'xlist':xlist_best,
        'ylist':ylist_best,
        'linecolor':1,
        'linestyle':2,
        'fillcolor':0,
        'drawoption':'l same'
    }



    conflist=[]
    conflist.append(NomBest)
    conflist.append(SMLike)
    #mkLimitPlot(savepath,modeltag,conflist,sqrtS,lumi,xaxis="m_{X} (GeV)",yaxis='Limit 95% CL_{s} on #sigma_{X#rightarrowWW} [pb]'):
    mkLimitPlot(['./test.pdf'],'floating f_{vbf}',conflist,13,137)
