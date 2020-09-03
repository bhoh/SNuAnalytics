#samples[<year>][<kind>]

#samples = {
#  '2016' : {
#        ('<prod>','DATA') :[
#            ],
#        ('<prod>','MC') :[
#            ],
#        ('<prod>','MC_ttsyst') :[
#            ],
#        ('<prod>','MC_signal') :[
#            ],
#      },
#  '2017' : {
#        ('<prod>','DATA') :[
#            ],
#        ('<prod>','MC') :[
#            ],
#        ('<prod>','MC_ttsyst') :[
#            ],
#        ('<prod>','MC_signal') :[
#            ],
#      },
#  '2018' : {
#        ('<prod>','DATA') :[
#            ],
#        ('<prod>','MC') :[
#            ],
#        ('<prod>','MC_ttsyst') :[
#            ],
#        ('<prod>','MC_signal') :[
#            ],
#      },
#
#}

#sample defs. per year and production

samples = {
  '2016' : {
        ('Summer16_102X_nAODv7_Full2016v7','MC_signal') :[
                'CHToCB_M075',
                'CHToCB_M080',
                'CHToCB_M085',
                'CHToCB_M090',
                'CHToCB_M100',
                'CHToCB_M110',
                'CHToCB_M120',
                'CHToCB_M130',
                'CHToCB_M140',
                'CHToCB_M150',
                'CHToCB_M160',
            ],
        ('Summer16_102X_nAODv7_Full2016v7','MC_ttsyst') :[
                'TT_TuneCUETP8M2T4Up',
                'TT_TuneCUETP8M2T4Down',
                'TT_hdampUp',
                'TT_hdampDown',
                'TT_mtopUp',
                'TT_mtopDown',
                'TT_TuneCUETP8M2T4_PSweights',
            ],

      },
  '2017' : {
        ('Fall2017_102X_nAODv7_Full2017v7','MC_signal') :[
                'CHToCB_M075',
                'CHToCB_M080',
                'CHToCB_M085',
                'CHToCB_M090',
                'CHToCB_M100',
                'CHToCB_M110',
                'CHToCB_M120',
                'CHToCB_M130',
                'CHToCB_M140',
                'CHToCB_M150',
                'CHToCB_M160',
            ],
        ('Fall2017_102X_nAODv7_Full2017v7','MC_ttsyst') :[
                'TTToSemiLeptonic_TuneCP5Up',
                'TTToSemiLeptonic_TuneCP5Down',
                'TTTo2L2Nu_TuneCP5Up',
                'TTTo2L2Nu_TuneCP5Down',
                'TTToSemiLeptonic_hdampUp',
                'TTToSemiLeptonic_hdampDown',
                'TTTo2L2Nu_hdampUp',
                'TTTo2L2Nu_hdampDown',
                'TTToSemiLeptonic_mtopUp',
                'TTToSemiLeptonic_mtopDown',
                'TTTo2L2Nu_mtopUp', 
                'TTTo2L2Nu_mtopDown',
            ],
      },
  '2018' : {
        ('Autumn18_102X_nAODv7_Full2018v7','MC_signal') :[
                     'CHToCB_M075',
                     'CHToCB_M080',
                     'CHToCB_M085',
                     'CHToCB_M090',
                     'CHToCB_M100',
                     'CHToCB_M110',
                     'CHToCB_M120',
                     'CHToCB_M130',
                     'CHToCB_M140',
                     'CHToCB_M150',
                     'CHToCB_M160',
            ],
        ('Autumn18_102X_nAODv7_Full2018v7','MC_ttsyst') :[
                'TTToSemiLeptonic_TuneCP5Up',
                'TTToSemiLeptonic_TuneCP5Down',
                'TTTo2L2Nu_TuneCP5Up',
                'TTTo2L2Nu_TuneCP5Down',
                'TTToSemiLeptonic_hdampUp',
                'TTToSemiLeptonic_hdampDown',
                'TTTo2L2Nu_hdampUp',
                'TTTo2L2Nu_hdampDown',
                'TTToSemiLeptonic_mtopUp',
                'TTToSemiLeptonic_mtopDown',
                'TTTo2L2Nu_mtopUp', 
                'TTTo2L2Nu_mtopDown',
            ],
      },

}

# post-processing configuration per year and production
# will modify this by skim-steps! ('<prod>',<step>,<data_or_MC_or_Other>)
# ('<prod>','ELSE',<data_or_MC_or_Other>)
modCfgs = {
  '2016' : {
        ('Summer16_102X_nAODv7_Full2016v7','MC_signal') :[
              '--sitescfg SNuAnalytics/PostProcess/ChargedHiggsToCB/Sites_cfg.py',
              '--modcfg SNuAnalytics/NanoGardenerFrameworks/CHToCB/200831_l1/Steps_cfg.py',
              '--datacfg SNuAnalytics/PostProcess/ChargedHiggsToCB/Productions_cfg.py',
            ],
        ('Summer16_102X_nAODv7_Full2016v7','MC_ttsyst') :[
              '--sitescfg SNuAnalytics/PostProcess/ChargedHiggsToCB/Sites_cfg.py',
              '--modcfg SNuAnalytics/NanoGardenerFrameworks/CHToCB/200831_l1/Steps_cfg.py',
              '--datacfg SNuAnalytics/PostProcess/ChargedHiggsToCB/Productions_cfg.py',
            ],
      },
  '2017' : {
        ('Fall2017_102X_nAODv7_Full2017v7','MC_signal') :[
              '--sitescfg SNuAnalytics/PostProcess/ChargedHiggsToCB/Sites_cfg.py',
              '--modcfg SNuAnalytics/NanoGardenerFrameworks/CHToCB/200831_l1/Steps_cfg.py',
              '--datacfg SNuAnalytics/PostProcess/ChargedHiggsToCB/Productions_cfg.py',
            ],
        ('Fall2017_102X_nAODv7_Full2017v7','MC_ttsyst') :[
              '--sitescfg SNuAnalytics/PostProcess/ChargedHiggsToCB/Sites_cfg.py',
              '--modcfg SNuAnalytics/NanoGardenerFrameworks/CHToCB/200831_l1/Steps_cfg.py',
              '--datacfg SNuAnalytics/PostProcess/ChargedHiggsToCB/Productions_cfg.py',
            ],
      },
  '2018' : {
        ('Autumn18_102X_nAODv7_Full2018v7','MC_signal') :[
              '--sitescfg SNuAnalytics/PostProcess/ChargedHiggsToCB/Sites_cfg.py',
              '--modcfg SNuAnalytics/NanoGardenerFrameworks/CHToCB/200831_l1/Steps_cfg.py',
              '--datacfg SNuAnalytics/PostProcess/ChargedHiggsToCB/Productions_cfg.py',
            ],
        ('Autumn18_102X_nAODv7_Full2018v7','MC_ttsyst') :[
              '--sitescfg SNuAnalytics/PostProcess/ChargedHiggsToCB/Sites_cfg.py',
              '--modcfg SNuAnalytics/NanoGardenerFrameworks/CHToCB/200831_l1/Steps_cfg.py',
              '--datacfg SNuAnalytics/PostProcess/ChargedHiggsToCB/Productions_cfg.py',
            ],
      },

}


