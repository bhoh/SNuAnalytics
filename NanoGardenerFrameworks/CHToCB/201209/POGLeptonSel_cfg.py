import copy

LepFilter_dict = {
   'Loose': 'isLoose',
   'Veto': 'isVeto',
   'WgStar': 'isWgs',
   'isLoose': 'FakeObjWP',
   'isVeto': 'VetoObjWP',
   'isWgs': 'WgStarObjWP'
}



####################### Electron WP ##################################

ElectronWP = {  

###____________________Full2018v6_ForNewWPs__________________________ For nAODv6
'Full2018v7': {


## ------------  

 'VetoObjWP' : { 
           'HLTsafe' : { 
                         'cuts' : { 
                               # Common cuts
                               'True' :
                                [
                                  'False'
                                ] ,             
                                   },
                       } ,
                 } ,
  
 # ------------ 
 'FakeObjWP'  : {

           'HLTsafe' : { 
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                   [
                                    'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"]) < 2.5' ,
                                    'electron_col[LF_idx]["cutBased"] >= 2',  #loose
                                    'electron_col[LF_idx]["pt"]>15.',
                                   ] ,
                                #impact cuts
                                'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                 #gap veto
                                 'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"]) <=1.56 and abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"]) >= 1.4442' :
                                   [
                                     'False'
                                   ] ,
                                  },
                       } ,

                 } ,
 
# ------------ 
'TightObjWP' : {

          # ----- mvaFall17V1Iso

          'POGTight':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                    'electron_col[LF_idx]["cutBased"] >= 4',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v7/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v7_POG/2018_ElectronTight.root',
                                  } ,
                         #XXX
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v7/mvaFall17V1Iso_WP90/',

                              } ,


             },

 # ------------ 
 'WgStarObjWP' : {

         'mvaFall17V1Iso_WP90' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_Fall17_V1"] >= 3',
                                     'electron_col[LF_idx]["mvaFall17V1noIso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                  ] ,
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    'electron_col[LF_idx]["sieie"] < 0.03 ' ,                           
                                    'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' ,
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  '0.06',
                                ],
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                [
                                  'None' 
                                ],
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                [
                                  'None' 
                                ],
                                  },
                         'iso': ['pfRelIso03_all', 0.3],
                         # FIXME: Update for 2018
                         'tkSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v5/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v5/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2018runABCD.txt',
                                  } ,
                             } ,

                 } ,

},


'Full2017v7': {


## ------------  

 'VetoObjWP' : { 
           'HLTsafe' : { 
                         'cuts' : { 
                               # Common cuts
                               'True' :
                                [
                                  'False'
                                ] ,             
                                   },
                       } ,
                 } ,

 'FakeObjWP'  : {

           'HLTsafe' : { 
                         'cuts' : {
                                # Common cuts
                                'True' :
                                   [
                                    'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"]) < 2.5' ,
                                    'electron_col[LF_idx]["cutBased"] >= 2',  #loose
                                    'electron_col[LF_idx]["pt"]>15.',
                                   ] ,
                                #impact cuts
                                'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                 #gap veto
                                 'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"]) <=1.56 and abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"]) >= 1.4442' :
                                   [
                                     'False'
                                   ] ,
                                  },
                       } ,

                 } ,
 
# ------------ 
'TightObjWP' : {

          # ----- mvaFall17V1Iso

          'POGTight':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                    'electron_col[LF_idx]["cutBased"] >= 4',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v7/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v7/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v7/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v7/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v7/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',

                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v7_POG/2017_ElectronTight.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v7_POG/2017_ElectronTight.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v7_POG/2017_ElectronTight.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v7_POG/2017_ElectronTight.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v7_POG/2017_ElectronTight.root',
                                  } ,
                         #XXX
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v7/mvaFall17V1Iso_WP90/',

                              } ,


             },

 # ------------ 
 'WgStarObjWP' : {

         'mvaFall17Iso_WP90' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_Fall17_V1"] >= 3',
                                     'electron_col[LF_idx]["mvaFall17V1noIso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                  ] ,
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                   'electron_col[LF_idx]["sieie"] < 0.03 ' ,
                                   'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' ,
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  '0.06',
                                ],
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                [
                                  'None' 
                                ],
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                [
                                  'None' 
                                ],
                                  },
                         'iso': ['pfRelIso03_all', 0.3],
                         'tkSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runB.txt' ,
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runC.txt' ,
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runD.txt' ,
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runE.txt' ,
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runF.txt' ,
                                  } ,
                             } ,

                 } ,

},

###____________________Full2016v7________ : for nAODv6
'Full2016v7': {

## ------------
 'VetoObjWP' : {
           'HLTsafe' : {
                         'cuts' : {
                               # Common cuts
                               'True' :
                                [
                                  'False'
                                  #'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                  #'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1 ' ,
                                ] ,
                                   },
                       } ,
                 } ,

 'FakeObjWP'  : {

           'HLTsafe' : { 
                         'cuts' : {
                                # Common cuts
                                'True' :
                                   [
                                    'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"]) < 2.5' ,
                                    'electron_col[LF_idx]["cutBased"] >= 2',  #loose
                                    'electron_col[LF_idx]["pt"]>15.',
                                    'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1' , #HLT safe
                                   ] ,
                                #impact cuts
                                'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                 #gap veto
                                 'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"]) <=1.56 and abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"]) >= 1.4442' :
                                   [
                                     'False'
                                   ] ,
                                  },
                       } ,

                 } ,
 
# ------------ 
'TightObjWP' : {

          # ----- mvaFall17V1Iso

          'POGTight':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                    'electron_col[LF_idx]["cutBased"] >= 4',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v7/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v7_POG/2016_ElectronTight.root',
                                  } ,

                              } ,


             },




 # ------------ 
 'WgStarObjWP' : {

          'mva_90p_Iso2016':  {
                         'cuts' : {
                                # Common cuts
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                     'electron_col[LF_idx]["mvaSpring16GP_WP90"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                        'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  'None',
                                ],
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                [
                                 '0.05880'
                                ],
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                [
                                 '0.0571'
                                ],
                                  },
                         'iso': ['pfRelIso03_all', 0.3],
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/egammaEffi_passingMVA80Xwp90HWW.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016/mva90pIso2016/',        
                              } ,

                } ,
},


}

####################### Muon WP ######################################

MuonWP = {

###____________________Full2018v7__________________________
'Full2018v7': {

## ------------  
 'VetoObjWP' : { 
      'HLTsafe' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                                 ]
                                  } ,
                   }
               } ,

 # ------------ 
 'FakeObjWP'  : {

      'HLTsafe' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'muon_col[LF_idx]["pt"]>15.' ,
                                   'muon_col[LF_idx]["pfRelIso04_all"] < 0.225',
                                 ] ,
                                  } ,

                       } ,
                 
                 } ,

 # ------------ 
 'TightObjWP' :  {

      'cut_Tight_POG' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [ 
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'muon_col[LF_idx]["pfRelIso04_all"] < 0.15',
                                 ] ,
                                  } ,
                         'idSF':  {
                                    '1-1' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v7_POG/ID_TH2_SFs_pt_abseta.root'],
                                    #txt
                                    #'1-1' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v7_POG/data.txt', 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v7_POG/mc.txt' ],
                                  } ,
                         'isoSF': {
                                    '1-1' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v7/ISO_TH2_SFs_pt_eta.root'],
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v7/cut_Tight_HWWW/',

                       } ,


                 } ,

 # -------------
 'WgStarObjWP' : {
     'cut_Tight_HWW' : { 
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   #'(muon_col[LF_idx]["pfRelIso04_all"] - self.ConeOverlapPt(lepton_col, iLep)/muon_col[LF_idx]["pt"]) < 0.15',
                                   ##'muon_col[LF_idx]["trackIso"]/muon_col[LF_idx]["pt"] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,
                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  '0.15',
                                ],
                                # Low pt
                                'muon_col[LF_idx]["pt"] <= 20.0' :
                                [
                                  'None' 
                                ],
                                # High pt
                                'muon_col[LF_idx]["pt"] > 20.0' :
                                [
                                  'None' 
                                ],
                                  },
                         'iso': ['pfRelIso04_all', 0.4],
                         'idSF':  {
                                    '1-1' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/ID_TH2_SFs_pt_eta.root'],
                                  } ,
                         'isoSF': {
                                    '1-1' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/ISO_TH2_SFs_pt_eta.root'],
                                  } ,
                       } ,
 
                 }, 
},

###____________________Full2017v7__________________________
'Full2017v7': {

## ------------  
 'VetoObjWP' : { 
      'HLTsafe' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                                 ]
                                  } ,
                   }
               } ,

 # ------------ 
 'FakeObjWP'  : {

      'HLTsafe' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'muon_col[LF_idx]["pt"]>15.' ,
                                   'muon_col[LF_idx]["pfRelIso04_all"] < 0.225',
                                 ] ,
                                  } ,

                       } ,
                 
                 } ,

 # ------------ 
 'TightObjWP' :  {

      'cut_Tight_POG' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [ 
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'muon_col[LF_idx]["pfRelIso04_all"] < 0.15',
                                 ] ,
                                  } ,
                         'idSF':  {
                                    '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v7_POG/ID_TH2_SFs_pt_abseta.root'],
                                    #txt
                                    #'1-1' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v7_POG/data.txt', 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v7_POG/mc.txt' ],
                                  } ,
                         'isoSF': {
                                    '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v7/muonISO_cut_Tight_HWW_combined.root'],
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v7/cut_Tight_HWWW/',

                       } ,


                 } ,


 # -------------
 'WgStarObjWP' : {
     'cut_Tight_HWW' : { 
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   #'(muon_col[LF_idx]["pfRelIso04_all"] - self.ConeOverlapPt(lepton_col, iLep)/muon_col[LF_idx]["pt"]) < 0.15',
                                   ##'muon_col[LF_idx]["trackIso"]/muon_col[LF_idx]["pt"] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,
                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  '0.15',
                                ],
                                # Low pt
                                'muon_col[LF_idx]["pt"] <= 20.0' :
                                [
                                  'None' 
                                ],
                                # High pt
                                'muon_col[LF_idx]["pt"] > 20.0' :
                                [
                                  'None' 
                                ],
                                  },
                         'iso': ['pfRelIso04_all', 0.4],
                         # Negligible, POG recommended to set to 1.
                         #'tkSF':  {
                         #           '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/muon_tracker_eff_Full2017.root' ,
                         #         } ,
                         #'tkSFerror': 0.01,
                         'idSF':  {
                                    '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/muonID_cut_Tight_HWW_combined.root'],
                                  } ,
                         'isoSF': {
                                    '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/muonISO_cut_Tight_HWW_combined.root'],
                                  } ,
                       } ,
 
                 }, 
},

###____________________Full2016v7__________________________

'Full2016v7': {

## ------------  
 'VetoObjWP' : { 
      'HLTsafe' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                                   'muon_col[LF_idx]["pt"] > 10.0' ,
                                 ]
                                  } ,
                   }
               } ,

 # ------------ 
 'FakeObjWP'  : {

      'HLTsafe' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'muon_col[LF_idx]["pt"]>15.' ,
                                   'muon_col[LF_idx]["pfRelIso04_all"] < 0.225',
                                 ] ,
                                  } ,

                       } ,
                 
                 } ,

 # ------------ 
 'TightObjWP' :  {

      'cut_Tight_POG' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [ 
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'muon_col[LF_idx]["pfRelIso04_all"] < 0.15',
                                 ] ,
                                  } ,
                         'idSF':  {
                                    '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v7_POG/2016_RunBCDEF_SF_ID.root'],
                                    '6-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v7_POG/2016_RunGH_SF_ID.root'],
                                    #txt
                                    #'1-1' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v7_POG/data.txt', 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v7_POG/mc.txt' ],
                                  } ,
                         'isoSF': {
                                    '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v7/muonISO_TH2_SFs_pt_eta.root' ] ,
                                    '6-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v7/muonISO_TH2_SFs_pt_eta.root' ] ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016v7/Tight80X/',

                       } ,


                 } ,




# -------------
 'WgStarObjWP' : {
     'cut_Tight80x' : { 
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   ##'muon_col[LF_idx]["trackIso"]/muon_col[LF_idx]["pt"] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,

                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  '0.15',
                                ],
                                # Low pt
                                'muon_col[LF_idx]["pt"] <= 20.0' :
                                [
                                  'None' 
                                ],
                                # High pt
                                'muon_col[LF_idx]["pt"] > 20.0' :
                                [
                                  'None' 
                                ],
                                  },
                         'iso': ['pfRelIso04_all', 0.4],
                         'idSF':  {
                                    '1-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/muonID_TH2_SFs_pt_eta.root' ] ,
                                  } ,
                         'isoSF':  {
                                    '1-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/muonISO_TH2_SFs_pt_eta.root' ] ,
                                   } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016/Tight80X/',         
                       } ,
 
                 }, 

},





}

 
if __name__ == '__main__':
    print('_______________LepFilter_dict___________')
    print(LepFilter_dict)
    print('') 
    print('_______________ElectronWP_______________')
    print('')
    for key in ElectronWP:
        print('__________' + key + '__________')
        print('')
        for typ in ElectronWP[key]:
            print('_____' + typ + '_____')
            for entr in ElectronWP[key][typ]:
                print(entr + ' =')
                print(ElectronWP[key][typ][entr]['cuts'])
                print('')
                for info in ElectronWP[key][typ][entr]:
                    if not (info == 'cuts'):
                        print(info)
                        print(ElectronWP[key][typ][entr][info])
                        print('')
    print('_______________MuonWP___________________')
    print('')
    for key in MuonWP:
        print('__________' + key + '__________')
        print('')
        for typ in MuonWP[key]:
            print('_____' + typ + '_____')
            for entr in MuonWP[key][typ]:
                print(entr + ' =')
                print(MuonWP[key][typ][entr]['cuts'])
                print('')
                for info in MuonWP[key][typ][entr]:
                    if not (info == 'cuts'):
                        print(info)
                        print(MuonWP[key][typ][entr][info])
                        print('')

