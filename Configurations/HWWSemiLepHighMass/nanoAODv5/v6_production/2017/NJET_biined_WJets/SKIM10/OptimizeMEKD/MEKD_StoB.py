from array import array
import ROOT
ROOT.gROOT.SetBatch(True)
import sys
sys.path.insert(0, "python_tool/latino/")
from HistoParser import HistoParser
from WPandCut2017 import MELA_C_BOOST
dict_eleCH={
    'bkg':{
        'cuts':['eleCH__BoostedggF__SR__METOver40__PtOverM04'],
        #'variables':['MEKD_Bst_C_0.003_M900'],
        'variables':[],
        'FileName':'rootFile_2017_Boosted_SKIM10_HMVar10_MEKDOPT/hadd.root',
        'samples':['DY','QCD_EM','QCD_bcToE','WW','WWW','WWZ','WZ','WZZ','ZZZ','ZZ','Wjets0j','Wjets1j','Wjets2j','WpWmJJ_EWK_QCD_noHiggs','top',]        
    },
    'sig':{
        'cuts':['eleCH__BoostedggF__SR__METOver40__PtOverM04'],
        #'variables':['MEKD_Bst_C_0.003_M900'],
        'variables':[],
        'FileName':'rootFile_2017_Boosted_SKIM10_HMVar10_MEKDOPT/hadd.root',
        'samples':['ggHWWlnuqq_M1500'],
    },
}


ModelMass=1500
#MELA_C_BOOST[M]
scale=1000
for C in MELA_C_BOOST[ModelMass]:
    dict_eleCH['bkg']['variables'].append('MEKD_Bst_C_'+C+'_M'+str(ModelMass))
    dict_eleCH['sig']['variables'].append('MEKD_Bst_C_'+C+'_M'+str(ModelMass))


eleCH=HistoParser(dict_eleCH)
#    test.mydict['gr1']['histo']['eleCH__BoostedggF__SR__METOver40__PtOverM04']['MEKD_Bst_C_0.003_M900']['DATA'].Draw()
#    test.mydict['gr1']['histo']['eleCH__BoostedggF__SR__METOver40__PtOverM04']['MEKD_Bst_C_0.003_M900']['Sum'].Draw()
Result={
    'bkg':{
        'Yield':{},
        'Eff':{},
        'Pass':{},
        'Color':ROOT.kRed
    },
    'sig':{
        'Yield':{},
        'Eff':{},
        'Pass':{},
        'Color':ROOT.kBlue
    }
}
for C in sorted(MELA_C_BOOST[ModelMass]):
    
    print C
    for sb in ['sig','bkg']:
        
        Result[sb]['Yield'][C]=eleCH.mydict[sb]['histo']['eleCH__BoostedggF__SR__METOver40__PtOverM04']['MEKD_Bst_C_'+C+'_M'+str(ModelMass)]['Sum'].Integral()
        
        Result[sb]['Eff'][C]=eleCH.mydict[sb]['histo']['eleCH__BoostedggF__SR__METOver40__PtOverM04']['MEKD_Bst_C_'+C+'_M'+str(ModelMass)]['Sum'].GetMean()
        
        Result[sb]['Pass'][C]=Result[sb]['Yield'][C]*Result[sb]['Eff'][C]


#
#Result[sb]['Eff'][C]
c1=ROOT.TCanvas()
n=len(MELA_C_BOOST[ModelMass])



mg=ROOT.TMultiGraph()
leg=ROOT.TLegend(0.1,0.7,0.48,0.9)

idx=0
for sb in ['bkg','sig']:
#for sb in ['bkg']:
    Result[sb]['x'], Result[sb]['y'] = array( 'd' ), array( 'd' )
    for C in sorted(MELA_C_BOOST[ModelMass]):

        Result[sb]['x'].append(float(C))
        Result[sb]['y'].append(Result[sb]['Eff'][C])

    Result[sb]['Eff']['gr'] = ROOT.TGraph(len(Result[sb]['x']),Result[sb]['x'],Result[sb]['y'])
    Result[sb]['Eff']['gr'].SetTitle("ModelM="+str(ModelMass))
    Result[sb]['Eff']['gr'].SetLineColor( Result[sb]['Color'] )
    Result[sb]['Eff']['gr'].SetLineWidth( 0 )
    Result[sb]['Eff']['gr'].SetMarkerColor( Result[sb]['Color'] )
    Result[sb]['Eff']['gr'].SetMarkerStyle( 21 )
    Result[sb]['Eff']['gr'].SetFillColor( Result[sb]['Color'] )
    Result[sb]['Eff']['gr'].GetXaxis().SetTitle( 'C' )
    #Result[sb]['Eff']['gr'].GetYaxis().SetTitle( 'S/B*'+str(scale) )
    
    #mg.Add(Result[sb]['Eff']['gr'],'cp')

    Result[sb]['Eff']['gr'].SetMaximum(1.)
    Result[sb]['Eff']['gr'].SetMinimum(0.)
    leg.AddEntry(Result[sb]['Eff']['gr'],sb)
    mg.Add(Result[sb]['Eff']['gr'])
    #Result[sb]['Eff']['gr'].Draw( 'ACP SAME' )
    #Result[sb]['Eff']['gr'].Draw( 'AP SAME' )
    idx+=1
#mg.SetTitle("ModelM="+str(ModelMass))

mg.SetTitle("ModelM="+str(ModelMass)+ ';C;MEKD tag Eff' )
mg.Draw("AP")
leg.Draw()
c1.Update()
#c1.GetFrame().SetFillColor( 21 )
c1.GetFrame().SetBorderSize( 12 )
c1.Modified()
c1.Update()
#c1.SetLogy()
c1.SetLogx()
c1.SaveAs('test.png')
