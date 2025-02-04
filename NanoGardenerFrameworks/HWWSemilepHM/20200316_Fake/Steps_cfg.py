Steps = {

  'HMSemilepFake2016' : {
      'isChain'    : True ,
      'do4MC'      : True  ,
      'do4Data'    : True  ,
    'selection'    : '"nLepton>=1  && Lepton_pt[0]>30 \
                          && (  Lepton_isTightElectron_mva_90p_Iso2016[0] > 0.5 \
                             || Lepton_isTightMuon_cut_Tight80x[0] > 0.5 ) \
                        && Alt$(Lepton_pt[1],0)<=10 && Alt$(Lepton_isLoose[1],1)> 0.5 \
                         && (  Alt$(Lepton_isTightElectron_mva_90p_Iso2016[1], 0) < 0.5 \
                             && Alt$(Lepton_isTightMuon_cut_Tight80x[1],0) < 0.5 )  \
                        "' ,
    'subTargets'   : ['fakeWstep1l'],
  },

  'HMSemilepFake2017' : {
    'isChain'    : True ,
    'do4MC'      : True  ,
    'do4Data'    : True  ,
    'selection'    : '"nLepton>=1  && Lepton_pt[0]>30 \
    && Alt$(Lepton_pt[1],0)<=10 && Alt$(Lepton_isLoose[1],1)> 0.5 \
    && (  Alt$(Lepton_isTightElectron_mvaFall17V1Iso_WP90[1], 0) < 0.5 \
    && Alt$(Lepton_isTightMuon_cut_Tight_HWWW[1],0) < 0.5 )  \
    "',
    'subTargets'   : ['fakeWstep1l'],
  },


  'HMSemilepFake2018' : {
    'isChain'    : True ,
    'do4MC'      : True  ,
    'do4Data'    : True  ,
    'selection'    : '"nLepton>=1  && Lepton_pt[0]>30 \
    && Alt$(Lepton_pt[1],0)<=10 && Alt$(Lepton_isLoose[1],1)> 0.5 \
    && (  Alt$(Lepton_isTightElectron_mvaFall17V1Iso_WP90[1], 0) < 0.5 \
    && Alt$(Lepton_isTightMuon_cut_Tight_HWWW[1],0) < 0.5 )  \
    "',
    'subTargets'   : ['fakeWstep1l'],
  },



  'fakeWstep1l'   : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonFakeWMaker',
                  'declare'    : '',
                  'module'     : 'LeptonFakeWMaker("RPLME_CMSSW", min_nlep=1)',
              },


}
