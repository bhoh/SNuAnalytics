import ROOT
import os



def ParseTxtOutput(Year,txtpath):
    #elePtBins=[0., 30., 35., 36.,37.,38.,40.,42.,45.,50.,65.,70.,80.,100.,200.,]
    #eleEtaBins=[-2.5, -2.1, -1.570, -1.440, -0.800, 0., 0.800, 1.440, 1.570, 2.100, 2.500]
    
    ##--read txt
    elePtBins=[]
    eleEtaBins=[]

    f=open(txtpath,'r')
    lines=f.readlines()
    for line in lines:
        values=line.split()
        etalow=float(values[0])
        etahigh=float(values[1])
        ptlow=float(values[2])
        pthigh=float(values[3])

        eleEtaBins.append(etalow)
        eleEtaBins.append(etahigh)

        elePtBins.append(ptlow)
        elePtBins.append(pthigh)
    
    f.close()
    elePtBins=sorted(list(set(elePtBins)))
    eleEtaBins=sorted(list(set(eleEtaBins)))


    ##--convert to python dict
    Eff={}
    for ieta in range(0,len(eleEtaBins)-1):

        for ipt in range(0,len(elePtBins)-1):
            etalow=eleEtaBins[ieta]
            etahigh=eleEtaBins[ieta+1]

            ptlow=elePtBins[ipt]
            pthigh=elePtBins[ipt+1]


            if not etalow in Eff : Eff[etalow]={}
            if not ptlow in Eff[etalow] : Eff[etalow][ptlow]={}


    for line in lines:
        values=line.split()
        etalow=float(values[0])
        etahigh=float(values[1])
        ptlow=float(values[2])
        pthigh=float(values[3])

        eff=float(values[4])
        errlow=float(values[5])
        errhigh=float(values[6])

        Eff[etalow][ptlow]['eff']=eff
        Eff[etalow][ptlow]['errlow']=errlow
        Eff[etalow][ptlow]['errhigh']=errhigh
        
        print etalow,etahigh,ptlow,pthigh,eff,errlow,errhigh
    ##--SaveOutput
    
    #Year=2016
    
    os.system('mkdir -p EffOutput/')
    outputname='EffOutput/'+str(Year)+'__Data.py'
    f=open(outputname,'w')
    f.write('TrigEffData='+str(Eff))
    f.close()



if __name__ == '__main__':
    ##--
    #Year=2016
    #txtpath='DataEffFromLatino/2016/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_Legacy2016.txt'
    dict_txt={
        '2016':'DataEffFromLatino/2016/HLT_Ele27_WPTight_Gsf_OR_Ele25_eta2p1_WPTight_Legacy2016.txt',
        '2017B':'DataEffFromLatino/2017/Ele35_pt_eta_efficiency_withSys_Run2017B.txt',
        '2017CDE':'DataEffFromLatino/2017/Ele35_pt_eta_efficiency_withSys_Run2017CDE.txt',
        '2017F':'DataEffFromLatino/2017/Ele35_pt_eta_efficiency_withSys_Run2017F.txt',
        '2018':'DataEffFromLatino/2018/Ele32_pt_eta_efficiency_withSys_Run2018.txt',
    }
    for Year in dict_txt:
        txtpath=dict_txt[Year]
        ParseTxtOutput(Year,txtpath)
    
