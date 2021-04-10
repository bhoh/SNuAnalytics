import os, sys
import argparse
from samples_cfg import *


parser = argparse.ArgumentParser(description='run skim command')
parser.add_argument('-R', dest='R', action='store_true', default=False)
parser.add_argument('--dry-run', dest='pretend', action='store_true', default=False)
parser.add_argument('--samples', dest='samples', action='store', default='ALL')

opt = parser.parse_args()

run_keys = [
        #
        # --- 2016 ---
        #
        #('2016','Summer16_102X_nAODv7_Full2016v7','Prod','MCl1loose2016v7','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','Prod','MCl1loose2016v7','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7','MCCorr2016v7','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7','MCCorr2016v7','MC_ttsyst'),
        #('2016','Run2016_102X_nAODv7_Full2016v7','Prod','DATACHToCBLepton2016v7','DATA'),
        #('2016','Run2016_102X_nAODv7_Full2016v7','DATACHToCBLepton2016v7','CHToCBJetMETCorr_data','DATA'),
        #('2016','Run2016_102X_nAODv7_Full2016v7','DATACHToCBLepton2016v7__CHToCBJetMETCorr_data','kinFitTTSemiLepV4_2016','DATA'),
        #('2016','Run2016_102X_nAODv7_Full2016v7','DATACHToCBLepton2016v7__CHToCBJetMETCorr_data__kinFitTTSemiLepV4_2016','mvaCHToCB_2016','DATA'),
        #('2016','Run2016_102X_nAODv7_Full2016v7','DATAl1loose2016v7','CHToCBJetMETCorr_data','DATA'),
        #('2016','Run2016_102X_nAODv7_Full2016v7','DATAl1loose2016v7__CHToCBJetMETCorr_data','kinFitTTSemiLep_2016','DATA'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','Prod','CHToCBLepton2016v7','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','Prod','CHToCBLepton2016v7','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','Prod','CHToCBLepton2016v7','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7','CHToCBJetMETCorr2016v7','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7','CHToCBJetMETCorr2016v7','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7','CHToCBJetMETCorr2016v7','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_TotalUp','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_TotalDown','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_TotalUp','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_TotalDown','MC_signal'),

        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesAbsolute_uncorr','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesBBEC1_uncorr','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesEC2_uncorr','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesHF_uncorr','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesRelativeSample_uncorr','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesAbsolute','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesBBEC1','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesEC2','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesFlavorQCD','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesHF','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesRelativeBal','MC'),


        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesAbsolute_uncorr','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesBBEC1_uncorr','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesEC2_uncorr','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesHF_uncorr','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesRelativeSample_uncorr','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesAbsolute','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesBBEC1','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesEC2','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesFlavorQCD','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesHF','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesRelativeBal','MC_signal'),


        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_TotalUp','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_TotalDown','MC_ttsyst'),

        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesAbsolute_uncorr','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesBBEC1_uncorr','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesEC2_uncorr','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesHF_uncorr','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesRelativeSample_uncorr','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesAbsolute','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesBBEC1','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesEC2','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesFlavorQCD','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesHF','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016_jetMETSyst_jesRelativeBal','MC_ttsyst'),

        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesAbsolute_uncorr',      'mvaCHToCB_2016_jetMETSyst_jesAbsolute_uncorr',      'MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesBBEC1_uncorr',         'mvaCHToCB_2016_jetMETSyst_jesBBEC1_uncorr',         'MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesEC2_uncorr',           'mvaCHToCB_2016_jetMETSyst_jesEC2_uncorr',           'MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesHF_uncorr',            'mvaCHToCB_2016_jetMETSyst_jesHF_uncorr',            'MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesRelativeSample_uncorr','mvaCHToCB_2016_jetMETSyst_jesRelativeSample_uncorr','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesAbsolute',             'mvaCHToCB_2016_jetMETSyst_jesAbsolute',             'MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesBBEC1',                'mvaCHToCB_2016_jetMETSyst_jesBBEC1',                'MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesEC2',                  'mvaCHToCB_2016_jetMETSyst_jesEC2',                  'MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesFlavorQCD',            'mvaCHToCB_2016_jetMETSyst_jesFlavorQCD',            'MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesHF',                   'mvaCHToCB_2016_jetMETSyst_jesHF',                   'MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesRelativeBal',          'mvaCHToCB_2016_jetMETSyst_jesRelativeBal',          'MC_ttsyst'),

        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesAbsolute_uncorr',      'mvaCHToCB_2016_jetMETSyst_jesAbsolute_uncorr',      'MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesBBEC1_uncorr',         'mvaCHToCB_2016_jetMETSyst_jesBBEC1_uncorr',         'MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesEC2_uncorr',           'mvaCHToCB_2016_jetMETSyst_jesEC2_uncorr',           'MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesHF_uncorr',            'mvaCHToCB_2016_jetMETSyst_jesHF_uncorr',            'MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesRelativeSample_uncorr','mvaCHToCB_2016_jetMETSyst_jesRelativeSample_uncorr','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesAbsolute',             'mvaCHToCB_2016_jetMETSyst_jesAbsolute',             'MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesBBEC1',                'mvaCHToCB_2016_jetMETSyst_jesBBEC1',                'MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesEC2',                  'mvaCHToCB_2016_jetMETSyst_jesEC2',                  'MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesFlavorQCD',            'mvaCHToCB_2016_jetMETSyst_jesFlavorQCD',            'MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesHF',                   'mvaCHToCB_2016_jetMETSyst_jesHF',                   'MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesRelativeBal',          'mvaCHToCB_2016_jetMETSyst_jesRelativeBal',          'MC'),

        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesAbsolute_uncorr',      'mvaCHToCB_2016_jetMETSyst_jesAbsolute_uncorr',      'MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesBBEC1_uncorr',         'mvaCHToCB_2016_jetMETSyst_jesBBEC1_uncorr',         'MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesEC2_uncorr',           'mvaCHToCB_2016_jetMETSyst_jesEC2_uncorr',           'MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesHF_uncorr',            'mvaCHToCB_2016_jetMETSyst_jesHF_uncorr',            'MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesRelativeSample_uncorr','mvaCHToCB_2016_jetMETSyst_jesRelativeSample_uncorr','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesAbsolute',             'mvaCHToCB_2016_jetMETSyst_jesAbsolute',             'MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesBBEC1',                'mvaCHToCB_2016_jetMETSyst_jesBBEC1',                'MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesEC2',                  'mvaCHToCB_2016_jetMETSyst_jesEC2',                  'MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesFlavorQCD',            'mvaCHToCB_2016_jetMETSyst_jesFlavorQCD',            'MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesHF',                   'mvaCHToCB_2016_jetMETSyst_jesHF',                   'MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_jesRelativeBal',          'mvaCHToCB_2016_jetMETSyst_jesRelativeBal',          'MC_signal'),


        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016','UEPS','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016','mvaTreeCHToCB','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016','mvaTreeCHToCB','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016','mvaCHToCB_2016','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_TotalUp','mvaCHToCB_2016_jetMETSyst_TotalUp','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_TotalDown','mvaCHToCB_2016_jetMETSyst_TotalDown','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016','mvaCHToCB_2016','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016__mvaCHToCB_2016','UEPS','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_TotalUp','mvaCHToCB_2016_jetMETSyst_TotalUp','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_TotalDown','mvaCHToCB_2016_jetMETSyst_TotalDown','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016','mvaCHToCB_2016','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_TotalUp','mvaCHToCB_2016_jetMETSyst_TotalUp','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7__kinFitTTSemiLepV4_2016_jetMETSyst_TotalDown','mvaCHToCB_2016_jetMETSyst_TotalDown','MC_signal'),

        #
        # --- 2017 ---
        #
        #('2017','Fall2017_102X_nAODv7_Full2017v7','Prod','MCl1loose2017v7','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','Prod','MCl1loose2017v7','MC_ttsyst'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7','MCCorr2017v7','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7','MCCorr2017v7','MC_ttsyst'),
        #('2017','Run2017_102X_nAODv7_Full2017v7','Prod','DATACHToCBLepton2017v7','DATA'),
        #('2017','Run2017_102X_nAODv7_Full2017v7','DATACHToCBLepton2017v7','CHToCBJetMETCorr_data','DATA'),
        #('2017','Run2017_102X_nAODv7_Full2017v7','DATACHToCBLepton2017v7__CHToCBJetMETCorr_data','kinFitTTSemiLepV4_2017','DATA'),
        #('2017','Run2017_102X_nAODv7_Full2017v7','DATACHToCBLepton2017v7__CHToCBJetMETCorr_data__kinFitTTSemiLepV4_2017','mvaCHToCB_2017','DATA'),
        #('2017','Run2017_102X_nAODv7_Full2017v7','DATAl1loose2017v7__CHToCBJetMETCorr_data','kinFitTTSemiLep_2017','DATA'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','Prod','CHToCBLepton2017v7','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','Prod','CHToCBLepton2017v7','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','Prod','CHToCBLepton2017v7','MC_ttsyst'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7','CHToCBJetMETCorr2017v7','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7','CHToCBJetMETCorr2017v7','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7','CHToCBJetMETCorr2017v7','MC_ttsyst'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_TotalUp','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_TotalDown','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesAbsolute_uncorr','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesBBEC1_uncorr','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesEC2_uncorr','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesHF_uncorr','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesRelativeSample_uncorr','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesAbsolute','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesBBEC1','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesEC2','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesFlavorQCD','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesHF','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesRelativeBal','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_TotalUp','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_TotalDown','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesAbsolute_uncorr','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesBBEC1_uncorr','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesEC2_uncorr','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesHF_uncorr','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesRelativeSample_uncorr','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesAbsolute','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesBBEC1','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesEC2','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesFlavorQCD','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesHF','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017_jetMETSyst_jesRelativeBal','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017','MC_ttsyst'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017','UEPS','MC_ttsyst'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017','mvaTreeCHToCB','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017','mvaTreeCHToCB','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017','mvaCHToCB_2017','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_TotalUp','mvaCHToCB_2017_jetMETSyst_TotalUp','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_TotalDown','mvaCHToCB_2017_jetMETSyst_TotalDown','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesAbsolute_uncorr',      'mvaCHToCB_2017_jetMETSyst_jesAbsolute_uncorr',      'MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesBBEC1_uncorr',         'mvaCHToCB_2017_jetMETSyst_jesBBEC1_uncorr',         'MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesEC2_uncorr',           'mvaCHToCB_2017_jetMETSyst_jesEC2_uncorr',           'MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesHF_uncorr',            'mvaCHToCB_2017_jetMETSyst_jesHF_uncorr',            'MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesRelativeSample_uncorr','mvaCHToCB_2017_jetMETSyst_jesRelativeSample_uncorr','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesAbsolute',             'mvaCHToCB_2017_jetMETSyst_jesAbsolute',             'MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesBBEC1',                'mvaCHToCB_2017_jetMETSyst_jesBBEC1',                'MC'),
        ('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesEC2',                  'mvaCHToCB_2017_jetMETSyst_jesEC2',                  'MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesFlavorQCD',            'mvaCHToCB_2017_jetMETSyst_jesFlavorQCD',            'MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesHF',                   'mvaCHToCB_2017_jetMETSyst_jesHF',                   'MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesRelativeBal',          'mvaCHToCB_2017_jetMETSyst_jesRelativeBal',          'MC'),
        #
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesAbsolute_uncorr',      'mvaCHToCB_2017_jetMETSyst_jesAbsolute_uncorr',      'MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesBBEC1_uncorr',         'mvaCHToCB_2017_jetMETSyst_jesBBEC1_uncorr',         'MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesEC2_uncorr',           'mvaCHToCB_2017_jetMETSyst_jesEC2_uncorr',           'MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesHF_uncorr',            'mvaCHToCB_2017_jetMETSyst_jesHF_uncorr',            'MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesRelativeSample_uncorr','mvaCHToCB_2017_jetMETSyst_jesRelativeSample_uncorr','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesAbsolute',             'mvaCHToCB_2017_jetMETSyst_jesAbsolute',             'MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesBBEC1',                'mvaCHToCB_2017_jetMETSyst_jesBBEC1',                'MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesEC2',                  'mvaCHToCB_2017_jetMETSyst_jesEC2',                  'MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesFlavorQCD',            'mvaCHToCB_2017_jetMETSyst_jesFlavorQCD',            'MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesHF',                   'mvaCHToCB_2017_jetMETSyst_jesHF',                   'MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_jesRelativeBal',          'mvaCHToCB_2017_jetMETSyst_jesRelativeBal',          'MC_signal'),


        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017','mvaCHToCB_2017','MC_ttsyst'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017__mvaCHToCB_2017','UEPS','MC_ttsyst'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017','mvaCHToCB_2017','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_TotalUp','mvaCHToCB_2017_jetMETSyst_TotalUp','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7__kinFitTTSemiLepV4_2017_jetMETSyst_TotalDown','mvaCHToCB_2017_jetMETSyst_TotalDown','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_TotalUp','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_TotalDown','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_uncorrUp','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_uncorrDown','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_corrUp','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_corrDown','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_TotalUp','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_TotalDown','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_uncorrUp','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_uncorrDown','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_corrUp','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_corrDown','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017','MC_ttsyst'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr__kinFitTTSemiLep_2017','mvaTreeCHToCB','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr__kinFitTTSemiLep_2017','mvaTreeCHToCB','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr__kinFitTTSemiLep_2017','UEPS','MC_ttsyst'),
        #
        # --- 2018 ---
        #
        #('2018','Autumn18_102X_nAODv7_Full2018v7','Prod','MCl1loose2018v7','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','Prod','MCl1loose2018v7','MC_ttsyst'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7','MCCorr2018v7','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7','MCCorr2018v7','MC_ttsyst'),
        #('2018','Run2018_102X_nAODv7_Full2018v7','Prod','DATACHToCBLepton2018v7','DATA'),
        #('2018','Run2018_102X_nAODv7_Full2018v7','DATACHToCBLepton2018v7','CHToCBJetMETCorr_data','DATA'),
        #('2018','Run2018_102X_nAODv7_Full2018v7','DATACHToCBLepton2018v7__CHToCBJetMETCorr_data','kinFitTTSemiLepV4_2018','DATA'),
        ('2018','Run2018_102X_nAODv7_Full2018v7','DATACHToCBLepton2018v7__CHToCBJetMETCorr_data__kinFitTTSemiLepV4_2018','mvaCHToCB_2018','DATA'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','Prod','CHToCBLepton2018v7','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','Prod','CHToCBLepton2018v7','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','Prod','CHToCBLepton2018v7','MC_ttsyst'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7','CHToCBJetMETCorr2018v7','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7','CHToCBJetMETCorr2018v7','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7','CHToCBJetMETCorr2018v7','MC_ttsyst'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018','MC_ttsyst'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_TotalUp','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_TotalDown','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesAbsolute_uncorr','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesBBEC1_uncorr','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesEC2_uncorr','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesHF_uncorr','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesRelativeSample_uncorr','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesAbsolute','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesBBEC1','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesEC2','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesFlavorQCD','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesHF','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesRelativeBal','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_HEM','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_TotalUp','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_TotalDown','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesAbsolute_uncorr','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesBBEC1_uncorr','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesEC2_uncorr','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesHF_uncorr','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesRelativeSample_uncorr','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesAbsolute','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesBBEC1','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesEC2','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesFlavorQCD','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesHF','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesRelativeBal','MC_signal'),

        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_HEM','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018','UEPS','MC_ttsyst'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018','mvaTreeCHToCB','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018','mvaTreeCHToCB','MC_signal'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018','mvaCHToCB_2018','MC'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_TotalUp','mvaCHToCB_2018_jetMETSyst_TotalUp','MC'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_TotalDown','mvaCHToCB_2018_jetMETSyst_TotalDown','MC'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_HEM','mvaCHToCB_2018_jetMETSyst_HEM','MC'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesAbsolute_uncorr',      'mvaCHToCB_2018_jetMETSyst_jesAbsolute_uncorr',      'MC'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesBBEC1_uncorr',         'mvaCHToCB_2018_jetMETSyst_jesBBEC1_uncorr',         'MC'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesEC2_uncorr',           'mvaCHToCB_2018_jetMETSyst_jesEC2_uncorr',           'MC'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesHF_uncorr',            'mvaCHToCB_2018_jetMETSyst_jesHF_uncorr',            'MC'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesRelativeSample_uncorr','mvaCHToCB_2018_jetMETSyst_jesRelativeSample_uncorr','MC'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesAbsolute',             'mvaCHToCB_2018_jetMETSyst_jesAbsolute',             'MC'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesBBEC1',                'mvaCHToCB_2018_jetMETSyst_jesBBEC1',                'MC'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesEC2',                  'mvaCHToCB_2018_jetMETSyst_jesEC2',                  'MC'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesFlavorQCD',            'mvaCHToCB_2018_jetMETSyst_jesFlavorQCD',            'MC'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesHF',                   'mvaCHToCB_2018_jetMETSyst_jesHF',                   'MC'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesRelativeBal',          'mvaCHToCB_2018_jetMETSyst_jesRelativeBal',          'MC'),

        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018','mvaCHToCB_2018','MC_ttsyst'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018__mvaCHToCB_2018','UEPS','MC_ttsyst'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018','mvaCHToCB_2018','MC_signal'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_TotalUp','mvaCHToCB_2018_jetMETSyst_TotalUp','MC_signal'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_TotalDown','mvaCHToCB_2018_jetMETSyst_TotalDown','MC_signal'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_HEM','mvaCHToCB_2018_jetMETSyst_HEM','MC_signal'),
        #
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesAbsolute_uncorr',      'mvaCHToCB_2018_jetMETSyst_jesAbsolute_uncorr',      'MC_signal'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesBBEC1_uncorr',         'mvaCHToCB_2018_jetMETSyst_jesBBEC1_uncorr',         'MC_signal'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesEC2_uncorr',           'mvaCHToCB_2018_jetMETSyst_jesEC2_uncorr',           'MC_signal'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesHF_uncorr',            'mvaCHToCB_2018_jetMETSyst_jesHF_uncorr',            'MC_signal'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesRelativeSample_uncorr','mvaCHToCB_2018_jetMETSyst_jesRelativeSample_uncorr','MC_signal'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesAbsolute',             'mvaCHToCB_2018_jetMETSyst_jesAbsolute',             'MC_signal'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesBBEC1',                'mvaCHToCB_2018_jetMETSyst_jesBBEC1',                'MC_signal'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesEC2',                  'mvaCHToCB_2018_jetMETSyst_jesEC2',                  'MC_signal'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesFlavorQCD',            'mvaCHToCB_2018_jetMETSyst_jesFlavorQCD',            'MC_signal'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesHF',                   'mvaCHToCB_2018_jetMETSyst_jesHF',                   'MC_signal'),
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7__kinFitTTSemiLepV4_2018_jetMETSyst_jesRelativeBal',          'mvaCHToCB_2018_jetMETSyst_jesRelativeBal',          'MC_signal'),



    ]

sleep_interval = {
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018','MC_ttsyst'):'30m',

        ('2016','Summer16_102X_nAODv7_Full2016v7','CHToCBLepton2016v7__CHToCBJetMETCorr2016v7','kinFitTTSemiLepV4_2016','MC'):'1h',
        ('2017','Fall2017_102X_nAODv7_Full2017v7','CHToCBLepton2017v7__CHToCBJetMETCorr2017v7','kinFitTTSemiLepV4_2017','MC'):'1h',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018','MC'):'1h',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesAbsolute_uncorr','MC'):'1h',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesBBEC1_uncorr','MC'):'1h',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesEC2_uncorr','MC'):'1h',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesHF_uncorr','MC'):'2h',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesRelativeSample_uncorr','MC'):'2h',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesAbsolute','MC'):'2h',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesBBEC1','MC'):'2h',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesEC2','MC'):'2h',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesFlavorQCD','MC'):'2h',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesHF','MC'):'2h',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesRelativeBal','MC'):'2h',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesAbsolute_uncorr','MC_signal'):'5m',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesBBEC1_uncorr','MC_signal'):'5m',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesEC2_uncorr','MC_signal'):'5m',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesHF_uncorr','MC_signal'):'5m',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesRelativeSample_uncorr','MC_signal'):'5m',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesAbsolute','MC_signal'):'5m',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesBBEC1','MC_signal'):'5m',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesEC2','MC_signal'):'5m',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesFlavorQCD','MC_signal'):'5m',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesHF','MC_signal'):'5m',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','CHToCBLepton2018v7__CHToCBJetMETCorr2018v7','kinFitTTSemiLepV4_2018_jetMETSyst_jesRelativeBal','MC_signal'):'5m',



    }

cmd_template = 'mkPostProc.py %s -p %s -i %s -s %s -b -T %s'
for key in run_keys:
    modCfg = ' '.join(modCfgs[key[0]][(key[1],key[4])])
    prod = key[1] #production
    inSkim = key[2] # input skim
    skim = key[3]  # skim to run
    if opt.samples=='ALL': # run for all samples defined in dictionary
      samples_string = ','.join(samples[key[0]][(key[1],key[4])])
    else: # run for opt.samples
      samples_string = opt.samples
    # fill commend template
    cmd = cmd_template%(modCfg,prod,inSkim,skim,samples_string)
    if opt.R:
        cmd += ' -R' #redo for existing skim
    if opt.pretend:
        cmd += ' --dry-run' # just creating running scripts
    print(cmd)
    os.system(cmd) # execute commend
    if key in sleep_interval:
        print('sleep for %s'%(sleep_interval[key]))
        os.system('sleep %s'%sleep_interval[key]) #sleep before next iteration




