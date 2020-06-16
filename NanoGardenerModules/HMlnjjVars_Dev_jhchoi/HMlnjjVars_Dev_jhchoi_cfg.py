# location to put: LatinoAnalysis/NanoGardener/python/data

HMlnjjVarsCuts={
    '2018':{
        #'Wmass_CRlow':40.,
        #'Wmass_CRhigh':250.,
        'cut_jet_pt':30.,
        'cut_jet_eta':2.5,
        'Wmass_SRlow':65.,
        'Wmass_SRhigh':105.,
        'cut_bjet_pt':20.,
        'cut_bjet_eta':2.5,
        'cut_VBFjet_pt':30.,
        'cut_VBFjet_eta':4.7,
        'cut_VBF_dEta':3.5,
        'cut_VBF_mjj':500.,
        'cut_jet_horn_ptmin':-1.,
        'cut_jet_horn_etamin':999.,
        'cut_jet_horn_etamax':-999.,
        'bWP':0.1241,
    },

    '2017':{
        'cut_jet_pt':30.,
        'cut_jet_eta':2.5,
        #'Wmass_CRlow':40.,
        #'Wmass_CRhigh':250.,
        'Wmass_SRlow':65.,
        'Wmass_SRhigh':105.,
        'cut_bjet_pt':20.,
        'cut_bjet_eta':2.5,
        'cut_VBFjet_pt':30.,
        'cut_VBFjet_eta':4.7,
        'cut_VBF_dEta':3.5,
        'cut_VBF_mjj':500.,
        'cut_jet_horn_ptmin':50.,
        'cut_jet_horn_etamin':2.5,
        'cut_jet_horn_etamax':3.2,
        'bWP':0.1522
    },


    '2016':{
        'cut_jet_pt':30.,
        'cut_jet_eta':2.4,
        #'Wmass_CRlow':40.,
        #'Wmass_CRhigh':250.,
        'Wmass_SRlow':65.,
        'Wmass_SRhigh':105.,
        'cut_bjet_pt':20.,
        'cut_bjet_eta':2.4,
        'cut_VBFjet_pt':30.,
        'cut_VBFjet_eta':4.7,
        'cut_VBF_dEta':3.5,
        'cut_VBF_mjj':500.,
        'cut_jet_horn_ptmin':-1.,
        'cut_jet_horn_etamin':999.,
        'cut_jet_horn_etamax':-999.,
        'bWP':0.2217,
    },
    
}
#HMlnjjVarsCuts['2017']= HMlnjjVarsCuts['2018']

MELAcfg={
    '2018':{
        'mH_boost':[400,900,1500],
        'mH_resol':[200,400],
    }
}
MELAcfg['2017']=MELAcfg['2018']
MELAcfg['2016']=MELAcfg['2018']



