# location to put: LatinoAnalysis/NanoGardener/python/data
###configuration###
##https://twiki.cern.ch/twiki/bin/view/CMS/JetWtagging
##W taggers
###Some categories are already corrected on JMS/JMR  @ nanoTool
###[2018]->tau21 HP45
###[2017]->tau21 HP45
###[2016]-> all id has the same JMS/JMR
##DDT ##https://arxiv.org/pdf/1603.00027.pdf
##Also evaluated JMS&JMR SD corr in tau21DDT region: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetWtagging#tau21DDT_0_43
###dictionary structure WJID[year][name] = {isDDT,tau21min:,tau21max:,}              

##https://twiki.cern.ch/twiki/bin/view/CMS/DeepAK8Tagging2018WPsSFs#DeepAK8_Nominal_W_boson_tagging
#https://raw.githubusercontent.com/cms-jet/deepAK8ScaleFactors/master/DeepAK8V2_Top_W_SFs.csv
##in Nano : FatJet_deepTag_WvsQCD
#https://cms-nanoaod-integration.web.cern.ch/integration/master-102X/mc102X_doc.html#FatJet


FATJETCUTS={
    '2018':{
        'ptmin':200.,
        'etamax':2.5,
        'msdmin':40.,
        'msdmax':250.,
    },
    '2017':{
        'ptmin':200.,
        'etamax':2.5,
        'msdmin':40.,
        'msdmax':250.,
    },

    '2016':{
        'ptmin':200.,
        'etamax':2.4,
        'msdmin':40.,
        'msdmax':250.,
    },


}

WJID={
    '2018':{
        'HP35':{
            'C_DDT':0.,
            'tau21min':-1.,
            'tau21max':0.35,
            'JMS':{'nom':0.999, 'up':1.001,'down':0.997},
            'JMR':{'nom':1.108, 'up':1.1142,'down':1.074},
            'effSF':{'nom':0.964, 'up':0.994, 'down':0.932},

            },
        'HP45':{
            'C_DDT':0.,
            'tau21min':-1,
            'tau21max':0.45,
            'JMS':{'nom':0.997,'up':1.001,'down':0.993},
            'JMR':{'nom':1.243,'up':1.284,'down':1.202},
            'effSF':{'nom':0.980, 'up':1.007, 'down':0.953},

        },
        'HP43DDT':{
            'C_DDT':0.082,
            'tau21min':-1.,
            'tau21max':0.43,
            'JMS':{'nom':1.,'up':1.010,'down':0.990},
            'JMR':{'nom':1.124,'up':1.208,'down':1.04},
            'effSF':{'nom':0.823,'up':1.033,'down':0.613},

        },
        'HP50DDT':{
            'C_DDT':0.082,
            'tau21min':-1,
            'tau21max':0.50,
            'JMS':{'nom':1.001,'up':1.003,'down':0.900},
            'JMR':{'nom':1.146,'up':1.185,'down':1.107},
            'effSF':{'nom':0.899,'up':1.077,'down':721},
            
        },
        'DeepAK8WP5':{
            'deepTag_min':0.458,
        },
        'DeepAK8WP2p5':{
            'deepTag_min':0.762,
        },
        'DeepAK8WP1':{
            'deepTag_min':0.918,
        },
        'DeepAK8WP0p5':{
            'deepTag_min':0.961,
        },
        ##Mass Decorrlated
        'DeepAK8WP5MD':{
            'deepTagMD_min':0.245,
        },
        'DeepAK8WP2p5MD':{
            'deepTagMD_min':0.479,
        },
        'DeepAK8WP1MD':{
            'deepTagMD_min':0.704,
        },
        'DeepAK8WP0p5MD':{
            'deepTagMD_min':0.806,
        },
    },

    '2017':{
        'HP45':{
            'C_DDT':0,
            'tau21min':-1,
            'tau21max':0.45,
            'JMS':{'nom':0.982,'up':0.984,'down':0.980},
            'JMR':{'nom':1.092,'up':1.131,'down':1.053},
            'effSF':{'nom':0.97,'up':1.03,'down':0.91},
            
        },
        'HP43DDT':{
            'C_DDT':0.080,
            'tau21min':-1,
            'tau21max':0.43,
            'JMS':{'nom':0.983,'up':0.990,'down':0.976},
            'JMR':{'nom':1.080,'up':1.161,'down':0.999},
            'effSF':{'nom':0.955,'up':1.076,'down':0.834},
            
        },
        'DeepAK8WP5':{
            'deepTag_min':0.467,
        },
        'DeepAK8WP2p5':{
            'deepTag_min':0.772,
        },
        'DeepAK8WP1':{
            'deepTag_min':0.925,
        },
        'DeepAK8WP0p5':{
            'deepTag_min':0.964,
            
        },
        ##Mass Decorrlated
        'DeepAK8WP5MD':{
            'deepTagMD_min':0.258,
        },
        'DeepAK8WP2p5MD':{
            'deepTagMD_min':0.506,
            
        },
        'DeepAK8WP1MD':{
            'deepTagMD_min':0.739,
        },
        'DeepAK8WP0p5MD':{
            'deepTagMD_min':0.838,
            
        },
    },
    '2016':{
        'HP35':{
            'C_DDT':0.,
            'tau21min':-1.,
            'tau21max':0.35,
            'JMS':{'nom':1.,'up':1.0094,'down':0.9906},
            'JMR':{'nom':1.,'up':1.2,'down':0.8},
            'effSF':{'nom':0.99,'up':1.1,'down':0.88},
            
        },
        'HP40':{
            'C_DDT':0.,
            'tau21min':-1.,
            'tau21max':0.40,
            'JMS':{'nom':1.,'up':1.0094,'down':0.9906},
            'JMR':{'nom':1.,'up':1.2,'down':0.8},
            'effSF':{'nom':1.,'up':1.06,'down':0.94},
            
        },

        'HP55':{
            'C_DDT':0.,
            'tau21min':-1.,
            'tau21max':0.55,
            'JMS':{'nom':1.,'up':1.0094,'down':0.9906},
            'JMR':{'nom':1.,'up':1.2,'down':0.8},
            'effSF':{'nom':1.03,'up':1.17,'down':0.89},
            
        },
        'HP43DDT':{
            'C_DDT':0.08,
            'tau21min':-1.,
            'tau21max':0.43,
            'JMS':{'nom':1.014,'up':1.021, 'down':1.007},
            'JMR':{'nom':1.086,'up':1.176,'down':0.996},
            'effSF':{'nom':0.937,'up':1.04,'down':0.834},
            
        },
        'DeepAK8WP5':{
            'deepTag_min':0.475,
            
        },
        'DeepAK8WP2p5':{
            'deepTag_min':0.763,
            
        },
        'DeepAK8WP1':{
            'deepTag_min':0.918,
            
        },
        'DeepAK8WP0p5':{
            'deepTag_min':0.960,
        },
        ##Mass Decorrlated
        'DeepAK8WP5MD':{
            'deepTagMD_min':0.274,
        
        },
        'DeepAK8WP2p5MD':{
            'deepTagMD_min':0.506,
        },
        'DeepAK8WP1MD':{
            'deepTagMD_min':0.731,
        },
        'DeepAK8WP0p5MD':{
            'deepTagMD_min':0.828,
        },
        
    }
}


##Add effSF for DeepAK8 ##python python Parser_DeepAK8SF.py
WJID['2018']['DeepAK8WP0p5']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=200&& WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<300 )*0.87+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<400 )*0.86+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<800 )*0.85+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=800)*0.85\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<300 )*0.93+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<400 )*0.91+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<800 )*0.91+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=800)*0.91\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<300 )*0.81+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<400 )*0.81+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<800 )*0.8+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=800)*0.8\
    ',        
}
WJID['2018']['DeepAK8WP0p5MD']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<300 )*0.73+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<400 )*0.67+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<800 )*0.75+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=800)*0.75\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<300 )*0.8+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<400 )*0.73+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<800 )*0.82+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=800)*0.82\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<300 )*0.67+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<400 )*0.61+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<800 )*0.67+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=800)*0.67\
    ',        
}
WJID['2018']['DeepAK8WP1']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<300 )*0.97+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<400 )*0.9+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<800 )*0.91+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=800)*0.91\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<300 )*1.04+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<400 )*0.96+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<800 )*0.98+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=800)*0.98\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<300 )*0.9+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<400 )*0.84+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<800 )*0.84+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=800)*0.84\
    ',        
}
WJID['2018']['DeepAK8WP1MD']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<300 )*0.86+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<400 )*0.77+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<800 )*0.78+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=800)*0.78\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<300 )*0.92+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<400 )*0.81+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<800 )*0.83+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=800)*0.83\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<300 )*0.8+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<400 )*0.73+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<800 )*0.73+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=800)*0.73\
    ',        
}
WJID['2018']['DeepAK8WP2p5']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<300 )*1.1+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<400 )*0.96+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<800 )*1.04+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=800)*1.04\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<300 )*1.17+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<400 )*1.04+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<800 )*1.16+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=800)*1.16\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<300 )*1.01+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<400 )*0.89+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<800 )*0.94+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=800)*0.94\
    ',        
}
WJID['2018']['DeepAK8WP2p5MD']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<300 )*0.91+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<400 )*0.86+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<800 )*0.9+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=800)*0.9\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<300 )*0.96+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<400 )*0.9+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<800 )*0.94+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=800)*0.94\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<300 )*0.86+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<400 )*0.83+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<800 )*0.86+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=800)*0.86\
    ',        
}
WJID['2018']['DeepAK8WP5']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<300 )*1.04+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<400 )*1.03+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<800 )*1.07+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=800)*1.07\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<300 )*1.06+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<400 )*1.12+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<800 )*1.11+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=800)*1.11\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<300 )*1.02+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<400 )*0.94+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<800 )*1.03+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=800)*1.03\
    ',        
}
WJID['2018']['DeepAK8WP5MD']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<300 )*0.96+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<400 )*0.93+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<800 )*0.96+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=800)*0.96\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<300 )*0.99+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<400 )*0.95+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<800 )*0.99+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=800)*0.99\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<300 )*0.93+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<400 )*0.9+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<800 )*0.93+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=800)*0.93\
    ',        
}
WJID['2017']['DeepAK8WP0p5']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<300 )*1.0+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<400 )*0.78+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<800 )*0.82+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=800)*0.82\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<300 )*1.08+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<400 )*0.88+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<800 )*0.9+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=800)*0.9\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<300 )*0.93+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<400 )*0.67+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<800 )*0.74+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=800)*0.74\
    ',        
}
WJID['2017']['DeepAK8WP0p5MD']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<300 )*0.9+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<400 )*0.78+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<800 )*0.79+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=800)*0.79\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<300 )*0.97+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<400 )*0.84+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<800 )*0.86+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=800)*0.86\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<300 )*0.83+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<400 )*0.73+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<800 )*0.72+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=800)*0.72\
    ',        
}
WJID['2017']['DeepAK8WP1']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<300 )*1.03+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<400 )*0.91+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<800 )*0.88+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=800)*0.88\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<300 )*1.12+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<400 )*0.99+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<800 )*0.97+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=800)*0.97\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<300 )*0.93+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<400 )*0.84+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<800 )*0.8+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=800)*0.8\
    ',        
}
WJID['2017']['DeepAK8WP1MD']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<300 )*0.85+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<400 )*0.82+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<800 )*0.85+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=800)*0.85\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<300 )*0.91+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<400 )*0.87+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<800 )*0.91+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=800)*0.91\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<300 )*0.79+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<400 )*0.77+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<800 )*0.79+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=800)*0.79\
    ',        
}
WJID['2017']['DeepAK8WP2p5']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<300 )*1.19+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<400 )*1.03+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<800 )*0.95+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=800)*0.95\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<300 )*1.23+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<400 )*1.15+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<800 )*1.08+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=800)*1.08\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<300 )*1.15+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<400 )*0.93+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<800 )*0.84+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=800)*0.84\
    ',        
}
WJID['2017']['DeepAK8WP2p5MD']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<300 )*0.94+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<400 )*0.92+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<800 )*0.93+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=800)*0.93\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<300 )*0.99+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<400 )*0.96+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<800 )*0.98+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=800)*0.98\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<300 )*0.89+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<400 )*0.88+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<800 )*0.88+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=800)*0.88\
    ',        
}
WJID['2017']['DeepAK8WP5']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<300 )*1.05+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<400 )*1.04+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<800 )*1.09+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=800)*1.09\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<300 )*1.09+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<400 )*1.15+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<800 )*1.17+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=800)*1.17\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<300 )*1.01+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<400 )*0.93+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<800 )*1.01+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=800)*1.01\
    ',        
}
WJID['2017']['DeepAK8WP5MD']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<300 )*1.0+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<400 )*0.94+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<800 )*0.95+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=800)*0.95\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<300 )*1.04+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<400 )*0.97+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<800 )*0.98+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=800)*0.98\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<300 )*0.96+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<400 )*0.91+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<800 )*0.92+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=800)*0.92\
    ',        
}
WJID['2016']['DeepAK8WP0p5']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<300 )*1.04+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<400 )*0.93+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<800 )*0.68+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=800)*0.68\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<300 )*1.14+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<400 )*1.03+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<800 )*0.79+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=800)*0.79\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<300 )*0.95+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<400 )*0.83+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]<800 )*0.57+\
    (WtaggerFatjet_DeepAK8WP0p5_nom_pt[lnJ_DeepAK8WP0p5_nom_widx]>=800)*0.57\
    ',        
}
WJID['2016']['DeepAK8WP0p5MD']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<300 )*0.82+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<400 )*0.9+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<800 )*0.82+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=800)*0.82\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<300 )*0.91+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<400 )*0.97+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<800 )*0.9+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=800)*0.9\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<300 )*0.74+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<400 )*0.84+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]<800 )*0.75+\
    (WtaggerFatjet_DeepAK8WP0p5MD_nom_pt[lnJ_DeepAK8WP0p5MD_nom_widx]>=800)*0.75\
    ',        
}
WJID['2016']['DeepAK8WP1']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<300 )*1.13+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<400 )*0.9+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<800 )*0.73+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=800)*0.73\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<300 )*1.25+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<400 )*1.0+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<800 )*0.82+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=800)*0.82\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<300 )*1.03+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<400 )*0.81+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]<800 )*0.64+\
    (WtaggerFatjet_DeepAK8WP1_nom_pt[lnJ_DeepAK8WP1_nom_widx]>=800)*0.64\
    ',        
}
WJID['2016']['DeepAK8WP1MD']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<300 )*0.91+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<400 )*0.94+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<800 )*0.89+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=800)*0.89\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<300 )*0.99+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<400 )*1.0+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<800 )*0.96+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=800)*0.96\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<300 )*0.83+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<400 )*0.88+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]<800 )*0.82+\
    (WtaggerFatjet_DeepAK8WP1MD_nom_pt[lnJ_DeepAK8WP1MD_nom_widx]>=800)*0.82\
    ',        
}
WJID['2016']['DeepAK8WP2p5']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<300 )*1.18+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<400 )*0.99+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<800 )*0.95+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=800)*0.95\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<300 )*1.26+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<400 )*1.1+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<800 )*1.09+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=800)*1.09\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<300 )*1.1+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<400 )*0.9+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]<800 )*0.84+\
    (WtaggerFatjet_DeepAK8WP2p5_nom_pt[lnJ_DeepAK8WP2p5_nom_widx]>=800)*0.84\
    ',        
}
WJID['2016']['DeepAK8WP2p5MD']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<300 )*0.95+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<400 )*0.99+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<800 )*0.93+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=800)*0.93\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<300 )*1.01+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<400 )*1.03+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<800 )*0.99+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=800)*0.99\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<300 )*0.9+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<400 )*0.95+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]<800 )*0.87+\
    (WtaggerFatjet_DeepAK8WP2p5MD_nom_pt[lnJ_DeepAK8WP2p5MD_nom_widx]>=800)*0.87\
    ',        
}
WJID['2016']['DeepAK8WP5']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<300 )*1.05+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<400 )*1.07+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<800 )*1.09+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=800)*1.09\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<300 )*1.07+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<400 )*1.11+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<800 )*1.25+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=800)*1.25\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<300 )*1.03+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<400 )*1.03+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]<800 )*0.93+\
    (WtaggerFatjet_DeepAK8WP5_nom_pt[lnJ_DeepAK8WP5_nom_widx]>=800)*0.94\
    ',        
}
WJID['2016']['DeepAK8WP5MD']['effSF']={

    'nom':'    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<300 )*1.05+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<400 )*1.01+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<800 )*0.94+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=800)*0.94\
    ',
    'up':'    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<300 )*1.08+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<400 )*1.04+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<800 )*1.0+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=800)*1.0\
    ',
    'down':'    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=200 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<300 )*1.02+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=300 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<400 )*0.98+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=400 && WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]<800 )*0.88+\
    (WtaggerFatjet_DeepAK8WP5MD_nom_pt[lnJ_DeepAK8WP5MD_nom_widx]>=800)*0.88\
    ',        
}
