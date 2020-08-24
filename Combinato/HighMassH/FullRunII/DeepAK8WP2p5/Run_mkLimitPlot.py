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
    SMLike={}
    xlist_SMLike=sorted(list(set(SMLike_XSEC['GGF']).intersection(set(SMLike_XSEC['VBF']))))
    ylist_SMLike=[]
    ylist_SMLike_ggfonly=[]
    ylist_SMLike_vbfonly=[]
    for mass in xlist_SMLike:
        ylist_SMLike.append(SMLike_XSEC['GGF'][mass]+SMLike_XSEC['VBF'][mass])
        ylist_SMLike_ggfonly.append(SMLike_XSEC['GGF'][mass])
        ylist_SMLike_vbfonly.append(SMLike_XSEC['VBF'][mass])
    SMLike['floating']={
        'alias':'SM-Like Scenario',
        'xlist':xlist_SMLike,
        'ylist':ylist_SMLike,
        'linecolor':2,
        'linestyle':1,
        'fillcolor':0,
        'drawoption':'l same',
        
    }
    ##--ggfonly SMLike

    SMLike['ggfonly']={
        'alias':'SM-Like Scenario',
        'xlist':xlist_SMLike,
        'ylist':ylist_SMLike_ggfonly,
        'linecolor':2,
        'linestyle':1,
        'fillcolor':0,
        'drawoption':'l same',
        
    }
    ##--vbfonly
    SMLike['vbfonly']={
        'alias':'SM-Like Scenario',
        'xlist':xlist_SMLike,
        'ylist':ylist_SMLike_vbfonly,
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
    NomBest={}
    ObsHIG_17_033={}
    for fvbf in ['floating','ggfonly','vbfonly']:
        Read=open('BestLimit/AsymptoticLimit__'+fvbf+'.py','r')
        exec(Read)
        Read.close()
        XWWBest=XWW
        del XWW

        xlist_best=[]
        ylist_best=[]
        for mass in sorted(XWWBest):
            if not 'exp50' in XWWBest[mass]: continue
            #print mass
            xlist_best.append(mass)
            ylist_best.append(XWWBest[mass]['exp50'])
            
        NomBest[fvbf]={
            'alias':'best among 3yrs',
            'xlist':xlist_best,
            'ylist':ylist_best,
            'linecolor':1,
            'linestyle':2,
            'fillcolor':0,
            'drawoption':'l same'
        }

        ##--HIG-17-033
        if fvbf=='floating':
            filename='floatingfvbf'
        else:
            filename=fvbf
        Read=open('../data/HIG-17-033/'+filename+'.py', 'r')
        exec(Read) #AsymptoticLimit_floatingfvbf={'200': 6.7733
        Read.close()
        exec('HIG_17_033=AsymptoticLimit_'+filename)
        exec('del AsymptoticLimit_'+filename)
        
        xlist_hig17033=[]
        for mass in sorted(HIG_17_033):
            xlist_hig17033.append(float(mass))
        xlist_hig17033=sorted(xlist_hig17033)
        ylist_hig17033=[]
        for mass in xlist_hig17033:
            ylist_hig17033.append(float(HIG_17_033[str(int(mass))]))

        ObsHIG_17_033[fvbf]={
            'alias':'HIG-17-033',
            'xlist':xlist_hig17033,
            'ylist':ylist_hig17033,
            'linecolor':4,
            'linestyle':1,
            'fillcolor':0,
            'drawoption':'l same'
        }



    conflist_ggfonly=[]
    conflist_ggfonly.append(NomBest['ggfonly'])
    conflist_ggfonly.append(SMLike['ggfonly'])
    conflist_ggfonly.append(ObsHIG_17_033['ggfonly'])

    conflist_vbfonly=[]
    conflist_vbfonly.append(NomBest['vbfonly'])
    conflist_vbfonly.append(SMLike['vbfonly'])
    conflist_vbfonly.append(ObsHIG_17_033['vbfonly'])

    conflist_floating=[]
    conflist_floating.append(NomBest['floating'])
    conflist_floating.append(SMLike['floating'])
    conflist_floating.append(ObsHIG_17_033['floating'])
    #mkLimitPlot(savepath,modeltag,conflist,sqrtS,lumi,xaxis="m_{X} (GeV)",yaxis='Limit 95% CL_{s} on #sigma_{X#rightarrowWW} [pb]'):




    mkLimitPlot(['./floating.pdf'],'floating f_{vbf}',conflist_floating,13,137)
    mkLimitPlot(['./ggfonly.pdf'],'ggflony',conflist_ggfonly,13,137)
    mkLimitPlot(['./vbfonly.pdf'],'vbfonly',conflist_vbfonly,13,137)
