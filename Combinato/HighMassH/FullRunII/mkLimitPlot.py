import os
import sys
import ROOT


##--Read SMLike Higgs Xsec
sys.path.insert(0,os.getcwd()+'/../data/SMLike')
sys.path.insert(0,os.getcwd()+'/../data/')
sys.path.insert(0,'python_tool/Histo/')
sys.path.insert(0,'../python_tool/Histo/')
from TGraphHelper import *
from XSEC import HWW_XSEC as SMLike_XSEC
#print SMLike_XSEC



#-----Main function
def mkLimitPlot(savepathlist,modeltag,conflist,sqrtS,lumi,setlogy=True,xaxis="m_{X} (GeV)",yaxis='Limit 95% CL_{s} on #sigma_{X#rightarrowWW} [pb]'):
    if len(conflist)==0:
        print "!!no input!!, exit"
        return 
    #-----conflist=[conf1,conf2,conf3,...]
    '''
    conf= {
    'alias':alias, in legend
    'xlist':[],
    'ylist':[],
    'linecolor':[]
    'linestyle':[]
    'fillcolor':[]
    'drawoption':'l same' '3 same'
    'optcommand':command to be exec(string)
    }
    '''
    ##---Make ROOT.TGraphAsymmErrors from conf
    xmin=99999
    xmax=-99999
    ymin=99999
    ymax=-99999
    nmax=-99999
    for conf in conflist:

        ##No ErrorArea TGraph
        if not 'xerrl_list' in conf and not 'xerrh_list' in conf and not 'yerrl_list' in conf and not 'yerrh_list' in conf:
            conf['tgr']=TGraph_Maker(conf['xlist'],conf['ylist'])
        ###if ErrorArea exists
        else:
            if not 'xerrl_list' in conf:
                conf['xerrl_list']=[0]*len(conf['xlist'])
            if not 'xerrh_list' in conf:
                conf['xerrh_list']=[0]*len(conf['xlist'])
            if not 'yerrl_list' in conf:
                conf['yerrl_list']=[0]*len(conf['ylist'])
            if not 'yerrh_list' in conf:
                conf['yerrh_list']=[0]*len(conf['ylist'])
            #def TGraph_Maker(xlist,ylist):
            #def TGraphAsymmErrors_Maker(xlist,ylist,xerrl_list,xerrh_list,yerrl_list,yerrh_list)
            conf['tgr']=TGraphAsymmErrors_Maker(conf['xlist'],conf['ylist'],conf['xerrl_list'],conf['xerrh_list'],conf['yerrl_list'],conf['yerrh_list'])
        #print "min(conf['xlist'])=",min(conf['xlist'])
        if min(conf['xlist'])<xmin : xmin=min(conf['xlist']) 
        if max(conf['xlist'])>xmax : xmax=max(conf['xlist']) 
        if min(conf['ylist'])<ymin : ymin=min(conf['ylist']) 
        if max(conf['ylist'])>ymax : ymax=max(conf['ylist']) 
        if len(conf['xlist'])>nmax : nmax=len(conf['xlist'])
        conf['tgr'].SetLineWidth(4)
        conf['tgr'].SetLineColor(conf['linecolor'])
        conf['tgr'].SetLineStyle(conf['linestyle'])
        conf['tgr'].SetFillColor(conf['fillcolor'])

    print 'ymax=',ymax   
        

   

    ##--canvas
    tcanvas = ROOT.TCanvas( 'tcanvas', 'distro',800,800)
    tcanvas.SetLogy(setlogy)
    ##---frame object
    frame = ROOT.TH2F("frame","",nmax,xmin,xmax,100,ymin*0.1,ymax*10)
    frame.SetStats(0)
    #frame.SetYTitle("Limit 95% CL_{s} on #sigma_{X#rightarrowWW} [pb]")
    frame.SetYTitle(yaxis)
    frame.GetYaxis().SetTitleSize(0.05)
    frame.GetYaxis().SetLabelSize(0.03)
    frame.GetYaxis().SetTitleOffset(0.8)
    #frame.SetXTitle("m_{X} (GeV)")
    frame.SetXTitle(xaxis)
    frame.GetXaxis().SetTitleSize(0.035)
    frame.GetXaxis().SetLabelSize(0.03)
    #frame.GetXaxis().SetTitleOffset(1.5)
    frame.GetXaxis().SetTitleOffset(1)
    #tgr_cls_exp_pm2.GetHistogram().SetYTitle("Limit on B(t #rightarrow H^{+}b) with B(H^{+}#rightarrow c#bar{b}) = 1");
    frame.Draw()

    ##--Option
    for conf in conflist:
        if 'optcommand' in conf:
            exec(conf['optcommand'])

    ##--Draw
    for conf in conflist:
        conf['tgr'].Draw(conf['drawoption'])
    
    
    ##---style 
    import CMS_lumi as CMS_lumi

    CMS_lumi.lumi_13TeV=str(lumi)+' fb^{-1}'
    CMS_lumi.lumiTextSize=0.4
    CMS_lumi.cmsTextSize=0.4
    CMS_lumi.writeExtraText=1
    CMS_lumi.extraText="Preliminary"
    CMS_lumi.relPosX = 0.12
    CMS_lumi.lumi_sqrtS = sqrtS
    iPeriod = 4
    iPos  = 0
    CMS_lumi.CMS_lumi(tcanvas, iPeriod, iPos)

    ##--SetLegend
    leg= ROOT.TLegend(0.5,0.75,0.95,0.90)
    leg.SetFillColor(0)
    leg.SetBorderSize(1)
    leg.SetTextFont(8)
    leg.SetTextSize(20)
    for conf in conflist:
        leg.AddEntry(conf['tgr'],conf['alias'])

    leg.Draw("same")

    drawmodeltag= ROOT.TLatex(300,50, modeltag)
    drawmodeltag.Draw("same")
    for savepath in savepathlist:
        tcanvas.SaveAs(savepath)



##---Make Configuration
def SetConfList():
    '''                                                                                                                                                                                                         conf= {                                                                                                                                                                                                     'alias':alias, in legend                                                                                                                                                                                   'xlist':[],                                                                                                                                                                                                'ylist':[],                                                                                                                                                                                                'linecolor':[]                                                                                                                                                                                             'linestyle':[]                                                                                                                                                                                             'fillcolor':[]                                                                                                                                                                                             'drawoption':'l same' '3 same'                                                                                                                                                                             'optcommand':command to be exec(string)                                                                                                                                                                    }                                                                                                                                                                                                       
    '''
    conflist=[]

    #SMLike_XSEC['GGF'][130]=xsec
    
    xlist_SMLike=sorted(list(set(SMLike_XSEC['GGF']).intersection(set(SMLike_XSEC['VBF']))))
    ylist_SMLike=[]
    for mass in xlist_SMLike:
        ylist_SMLike.append(SMLike_XSEC['GGF'][mass]+SMLike_XSEC['VBF'][mass])

    SMLike={
        'alias':'SM-Like Scenario',
        'xlist':xlist_SMLike,
        'ylist':[5,4,3,2,1,0],
        'linecolor':1,
        'linestyle':1,
        'fillcolor':0,
        'drawoption':'l same',
        
    }


    test2={
        'alias':'test2',
        'xlist':[0,1,2,3,4,5],
        'ylist':[1,2,3,4,5,6],
        'linecolor':3,
        'linestyle':2,
        'fillcolor':0,
        'drawoption':'l same',
        
    }
    conflist.append(test1)
    conflist.append(test2)

    return conflist

if __name__ == '__main__':
    
    conflist=SetConfList()
    #mkLimitPlot(savepath,modeltag,conflist,sqrtS,lumi,xaxis="m_{X} (GeV)",yaxis='Limit 95% CL_{s} on #sigma_{X#rightarrowWW} [pb]'):
    mkLimitPlot(['./test.pdf'],'hi',conflist,13,137)
