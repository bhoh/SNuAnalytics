import os
import sys
import math
sys.path.insert(0, "python_tool/latino/")
sys.path.insert(0, "MassPoints")
from List_MX import *
from HistoParser import HistoParser
from WPandCut2017 import *
from array import array
import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gErrorIgnoreLevel=ROOT.kFatal

    




def GetOptPoint(lep,M_S,cut,isBoost,input_histo,bkg=['DY','QCD_EM','QCD_bcToE','QCD_MU','WW','WZ','ZZ','WWW','WWZ','WZZ','ZZZ','Wjets0j','Wjets1j','Wjets2j','top',]):

    #myana=OptimizeMEKD()
    #myana.bkg=[]

    #MELA_MASS_BOOST
    #MELA_C_BOOST

    #C='0.0003'
    #M_model="900"
    #M_S='1500'
    #lep='ele'
    prefix='MEKD_Bst'
    region='Boost'
    if isBoost:
        prefix='MEKD_Bst'
        region='Boost'
    else:
        prefix='MEKD_Res'
        region='Resol'


    f=input_histo
    #cut=lep+'CH__BoostedggF__SR__METOver40__PtOverM04'
    RESULTDIR='RESULT_'+region+'/'+lep+'/ggf_signal_M'+M_S+'/'
    os.system('mkdir -p '+RESULTDIR)
    
    print "M(Signal)=",M_S
    print "lep=",lep

    #cut='eleCH__BoostedggF__SR__METOver40__PtOverM04'
    #x=['MEKD_Bst_C_'+C+'_M'+M_model ]
    #bkg=['DY','QCD_EM','QCD_bcToE','QCD_MU','WW','WZ','ZZ','WWW','WWZ','WZZ','ZZZ','Wjets0j','Wjets1j','Wjets2j','top',]
    if lep=='ele':
        bkg.remove('QCD_MU')
    if lep=='mu':
        bkg.remove('QCD_EM')
        bkg.remove('QCD_bcToE')
    sig=['ggHWWlnuqq_M'+M_S]
    
    #f='rootFile_2017_Boosted_SKIM10_HMVar10_MEKDOPT/hadd.root'
    #scorenames=[]

    mydict={
        'bkg':{
            'cuts':[cut],
            'variables':[prefix+'_C_'+C+'_M'+str(M_model) for M_model in MELA_MASS_BOOST for C in MELA_C_BOOST[M_model]],
            'FileName':f,
            'samples':bkg
        },
        'sig':{
            'cuts':[cut],
            'variables':[prefix+'_C_'+C+'_M'+str(M_model) for M_model in MELA_MASS_BOOST for C in MELA_C_BOOST[M_model]],
            'FileName':f,
            'samples':sig
            }
    }

    myana=HistoParser(mydict)
    myana.mydict['AUC']={}
    myana.mydict['AUC'][cut]={}
    myana.mydict['ROCCurve']={}
    myana.mydict['ROCCurve'][cut]={}
    myana.mydict['sig_pass']={}
    myana.mydict['sig_pass'][cut]={}
    myana.mydict['bkg_pass']={}
    myana.mydict['bkg_pass'][cut]={}
    myana.mydict['sig_total']={}
    myana.mydict['sig_total'][cut]={}
    myana.mydict['bkg_total']={}
    myana.mydict['bkg_total'][cut]={}
    myana.mydict['sig_eff']={}
    myana.mydict['sig_eff'][cut]={}
    myana.mydict['bkg_eff']={}
    myana.mydict['bkg_eff'][cut]={}
    myana.mydict['sgn']={}
    myana.mydict['sgn'][cut]={}
    print "-Calc ROC-"
    c=ROOT.TCanvas()
    for scorename in mydict['bkg']['variables']:
        
        #c=ROOT.TCanvas()
        h_bkg=myana.mydict['bkg']['histo'][cut][scorename]['Sum']
        #c.SaveAs('test.png')
        Nbins=h_bkg.GetNbinsX()
        
    
    
        bkg_weight=ROOT.vector('float')()
        bkg_score=ROOT.vector('float')()
        sig_weight=ROOT.vector('float')()
        sig_score=ROOT.vector('float')()

        bkg_weight_sum=0
        sig_weight_sum=0
        bkg_weight_sum0p5=0
        sig_weight_sum0p5=0
        for i in range(0,Nbins+1):
            
            weight=myana.mydict['bkg']['histo'][cut][scorename]['Sum'].GetBinContent(i)
            score=myana.mydict['bkg']['histo'][cut][scorename]['Sum'].GetBinCenter(i)
            if weight<0:weight=0
            bkg_weight.push_back(weight)
            bkg_score.push_back(score)
            bkg_weight_sum+=weight
            if i > Nbins/2:
                bkg_weight_sum0p5+=weight
            weight=myana.mydict['sig']['histo'][cut][scorename]['Sum'].GetBinContent(i)
            score=myana.mydict['sig']['histo'][cut][scorename]['Sum'].GetBinCenter(i)
            if weight<0:weight=0
            sig_weight.push_back(weight)
            sig_score.push_back(score)
            sig_weight_sum+=weight
            if i > Nbins/2:
                sig_weight_sum0p5+=weight
        ##--Draw MEDK distribution
        c.Clear()
        _leg=ROOT.TLegend(0.1,0.8,0.28,0.9)
        hsig=myana.mydict['sig']['histo'][cut][scorename]['Sum'].Clone()
        hsig.SetTitle(lep+'CH, '+scorename)
        hsig.Rebin(400)
        hsig.SetStats(0)
        hsig.Scale(1/hsig.Integral())
        hsig.SetLineColor(ROOT.kRed)
        hbkg=myana.mydict['bkg']['histo'][cut][scorename]['Sum'].Clone()
        hbkg.Rebin(400)
        hbkg.Scale(1/hbkg.Integral())
        hbkg.SetStats(0)
        hbkg.SetLineColor(ROOT.kBlue)
        _leg.AddEntry(hsig,'sig')
        _leg.AddEntry(hbkg,'bkg')
        hsig.Draw()
        hbkg.Draw("SAME")
        _leg.Draw()
        c.SaveAs(RESULTDIR+'/'+scorename+'.png')
        c.SaveAs(RESULTDIR+'/'+scorename+'.pdf')
        ##TMVA
        roc=ROOT.TMVA.ROCCurve(sig_score,bkg_score,sig_weight,bkg_weight)
        gr=roc.GetROCCurve()
        gr.SetTitle("ROC, "+scorename)
        c.Clear()
        gr.GetYaxis().SetTitle("P_SIG")
        gr.GetXaxis().SetTitle("1-P_BKG")
        gr.Draw()
        #c.SaveAs("test.png")
        c.SaveAs(RESULTDIR+'/'+'ROC_'+scorename+'.png')
        c.SaveAs(RESULTDIR+'/'+'ROC_'+scorename+'.pdf')
        
        #--store integram
        f=open(RESULTDIR+'/Integral_'+scorename+'.txt','w')
        f.write('bkg_weight_sum='+str(bkg_weight_sum)+'\n')
        f.write('sig_weight_sum='+str(sig_weight_sum)+'\n')
        #bkg_weight_sum,bkg_weight_sum
        f.close()
        ft=ROOT.TFile.Open(RESULTDIR+"/ROC_Obj_"+scorename+'.root',"RECREATE")
        gr.Write(scorename)
        myana.mydict['sig']['histo'][cut][scorename]['Sum'].Write('sig_'+scorename)
        myana.mydict['bkg']['histo'][cut][scorename]['Sum'].Write('bkg_'+scorename)
        ft.Close()
        AUC= roc.GetROCIntegral() 
        #return AUC
        myana.mydict['AUC'][cut][scorename]=AUC
        myana.mydict['ROCCurve'][cut][scorename]=gr
        
        myana.mydict['sig_pass'][cut][scorename]=sig_weight_sum0p5
        myana.mydict['bkg_pass'][cut][scorename]=bkg_weight_sum0p5
        myana.mydict['sig_total'][cut][scorename]=sig_weight_sum
        myana.mydict['bkg_total'][cut][scorename]=bkg_weight_sum
        myana.mydict['sig_eff'][cut][scorename]=sig_weight_sum0p5/sig_weight_sum
        myana.mydict['bkg_eff'][cut][scorename]=bkg_weight_sum0p5/bkg_weight_sum
        myana.mydict['sgn'][cut][scorename]=sig_weight_sum0p5/math.sqrt(bkg_weight_sum0p5+sig_weight_sum0p5)
        
    print "-end Calc ROC-"
    #print myana.mydict['AUC']
    gr_dict = {
        'AUC':{
            'nocondition':{
                'passcondition':"passcondition=True",
                'max':-1,
                'max_C':-1,
                'max_M_model':-1,
            },
            'sigeff0p5':{
                'passcondition':"passcondition=myana.mydict['sig_eff'][cut][scorename]>0.5",
                'max':-1,
                'max_C':-1,
                'max_M_model':-1,
            },
            'allpass':{
                'passcondition':"passcondition=(myana.mydict['sig_pass'][cut][scorename]==myana.mydict['sig_totoal'][cut][scorename]) and (myana.mydict['bkg_pass'][cut][scorename]==myana.mydict['bkg_total'][cut][scorename])",
                'max':-1,
                'max_C':-1,
                'max_M_model':-1,
            }

            #'mg':ROOT.TMultiGraph(),
            #'leg':ROOT.TLegend(0.1,0.8,0.28,0.9)
        },
        'sgn':{
            'nocondition':{
                'passcondition':"passcondition=True",
                'max':-1,
                'max_C':-1,
                'max_M_model':-1,
                #'mg':ROOT.TMultiGraph(),
                #'leg':ROOT.TLegend(0.1,0.8,0.28,0.9)
            },
            'sigeff0p5':{
                'passcondition':"passcondition=myana.mydict['sig_eff'][cut][scorename]>0.5",
                'max':-1,
                'max_C':-1,
                'max_M_model':-1,
            },
            'allpass':{
                'passcondition':"passcondition=(myana.mydict['sig_pass'][cut][scorename]==myana.mydict['sig_totoal'][cut][scorename]) and (myana.mydict['bkg_pass'][cut][scorename]==myana.mydict['bkg_total'][cut][scorename])",
                'max':-1,
                'max_C':-1,
                'max_M_model':-1,
            }
        }
    }
    
    #mg_sgn=ROOT.TMultiGraph()
    dict_style={
        0:{
            'color':ROOT.kRed,
        },
        1:{
            'color':ROOT.kBlue,
        },
        2:{
            'color':ROOT.kGreen-2,
        },
        
        3:{
            'color':ROOT.kYellow-2
        },
    }
        #leg=ROOT.TLegend(0.1,0.8,0.28,0.9)    
        
        
    for kind in gr_dict:##AUC or sgn graph
        for condition in gr_dict[kind]:
            gr_dict[kind][condition]['mg']=ROOT.TMultiGraph()
            gr_dict[kind][condition]['leg']=ROOT.TLegend(0.1,0.8,0.28,0.9)
            style_idx=0##for each M_model
            print "-Ana",kind,condition,"-"
            for M_model in MELA_MASS_BOOST:
                gr_dict[kind][condition][M_model]={}
                gr_dict[kind][condition][M_model]['C'],gr_dict[kind][condition][M_model][kind]=array( 'd' ),array( 'd' )
                for C in MELA_C_BOOST[M_model]:
                    scorename=prefix+'_C_'+C+'_M'+str(M_model)
                    #myana.mydict['AUC'][cut][scorename]
                    #AUC=myana.mydict['AUC'][cut][scorename]
                    #sgn=myana.mydict['sgn'][cut][scorename]
                    #gr_dict.SetPoint(idx,float(C),int(M_model),AUC)
                    gr_dict[kind][condition][M_model]['C'].append(float(C))
                    #gr_dict[M_model]['AUC'].append(float(AUC))
                    #gr_dict[M_model]['sgn'].append(float(sgn))
                    gr_dict[kind][condition][M_model][kind].append(float(myana.mydict[kind][cut][scorename]))
                    exec(gr_dict[kind][condition]['passcondition'])
                    if (float(myana.mydict[kind][cut][scorename]) > gr_dict[kind][condition]['max']) and passcondition:
                        gr_dict[kind][condition]['max']=float(myana.mydict[kind][cut][scorename])
                        gr_dict[kind][condition]['max_C']=C
                        gr_dict[kind][condition]['max_M_model']=M_model
                        gr_dict[kind][condition]['max_style_idx']=style_idx
                                    
                gr_dict[kind][condition][M_model]['gr']=ROOT.TGraph(len(gr_dict[kind][condition][M_model]['C']),gr_dict[kind][condition][M_model]['C'],gr_dict[kind][condition][M_model][kind])
                gr_dict[kind][condition][M_model]['gr'].SetTitle("M_model="+str(M_model))
                gr_dict[kind][condition][M_model]['gr'].SetLineColor(dict_style[style_idx]['color'])
                gr_dict[kind][condition][M_model]['gr'].SetLineWidth(2)
                gr_dict[kind][condition][M_model]['gr'].SetMarkerColor(dict_style[style_idx]['color'])
                gr_dict[kind][condition][M_model]['gr'].SetMarkerStyle(2)
                gr_dict[kind][condition]['mg'].Add(gr_dict[kind][condition][M_model]['gr'])
                gr_dict[kind][condition]['leg'].AddEntry(gr_dict[kind][condition][M_model]['gr'])

                style_idx+=1
            print "-End Ana",kind,condition,"-"
        

        
        

    for kind in gr_dict:
        for condition in gr_dict[kind]:
            print "--",kind,condition,"--"
            print "max=",gr_dict[kind][condition]['max']
            print "max_C",gr_dict[kind][condition]['max_C']
            print "max_M_model",gr_dict[kind][condition]['max_M_model']
            scorename=prefix+'_C_'+str(gr_dict[kind][condition]['max_C'])+'_M'+str(gr_dict[kind][condition]['max_M_model'])
            print "significance=",myana.mydict['sgn'][cut][scorename]
            print "AUC=",myana.mydict['AUC'][cut][scorename]
            print "sig_eff",myana.mydict['sig_eff'][cut][scorename]
            print "bkg_eff",myana.mydict['bkg_eff'][cut][scorename]
            
            
            #c=ROOT.TCanvas()
            c.Clear()
            gr_dict[kind][condition]['maxline']=ROOT.TLine(float(gr_dict[kind][condition]['max_C']),0.2,float(gr_dict[kind][condition]['max_C']),1)##TLine (Double_t x1, Double_t y1, Double_t x2, Double_t y2)
            gr_dict[kind][condition]['maxline'].SetLineWidth(2)
            gr_dict[kind][condition]['maxline'].SetLineStyle(2)
            gr_dict[kind][condition]['maxline'].SetLineColor(dict_style[gr_dict[kind][condition]['max_style_idx']]['color'])
            gr_dict[kind][condition]['mg'].SetTitle("M(signal)="+str(M_S)+', '+lep+'CH, max@C='+str(gr_dict[kind][condition]['max_C'])+',M_model='+str(gr_dict[kind][condition]['max_M_model'])+ ';C;'+kind )
            
            gr_dict[kind][condition]['mg'].Draw("AP")
            gr_dict[kind][condition]['maxline'].Draw("SAME")
            gr_dict[kind][condition]['leg'].Draw()
            c.SetLogx()
            
            #--Save MaxPoint
            f=open(RESULTDIR+'/max'+kind+'_'+cut+'point.txt','w')
            f.write('c='+str(gr_dict[kind][condition]['max_C'])+'\n')
            f.write('M_model='+str(gr_dict[kind][condition]['max_M_model'])+'\n')
            f.write(kind+'='+str(gr_dict[kind][condition]['max'])+'\n')
            f.close()
            #c.SaveAs("test.png")
            c.SaveAs(RESULTDIR+"/"+kind+"_"+cut+"_C.png")
            c.SaveAs(RESULTDIR+"/"+kind+"_"+cut+"_C.pdf")
            
            
            #x=prefix+'_C_'+C+'_M'+str(M_model) 
            #myana.mydict['ROCCurve'][cut][x]
        

if __name__ == '__main__':
    lep='ele'
    cut=lep+'CH__BoostedggF__SR__METOver40__PtOverM04'
    M_S='1500'
    isBoost=True
    input_histo='rootFile_2017_Boosted_SKIM10_HMVar10_MEKDOPT/hadd.root'
    GetOptPoint(lep,M_S,cut,isBoost,input_histo)
