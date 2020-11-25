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
        #('2016','Summer16_102X_nAODv5_Full2016v6','MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10','genCHToCB_2016','MC'),
        #('2016','Summer16_102X_nAODv5_Full2016v6','MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10','genCHToCB_2016','MC_signal'),
        #('2016','Summer16_102X_nAODv5_Full2016v6','MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10','genCHToCB_2016','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv5_Full2016v6','MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__genCHToCB_2016','kinFitTTSemiLep_2016','MC'),
        #('2016','Summer16_102X_nAODv5_Full2016v6','MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__genCHToCB_2016','kinFitTTSemiLep_2016','MC_signal'),
        #('2016','Summer16_102X_nAODv5_Full2016v6','MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__genCHToCB_2016','kinFitTTSemiLep_2016','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv5_Full2016v6','MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__kinFitTTSemiLep_2016','kinFitTTSemiLep_jetMETSyst_Total','MC'),
        #('2016','Summer16_102X_nAODv5_Full2016v6','MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__kinFitTTSemiLep_2016','kinFitTTSemiLep_jetMETSyst_uncorr','MC'),
        #('2016','Summer16_102X_nAODv5_Full2016v6','MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__kinFitTTSemiLep_2016','kinFitTTSemiLep_jetMETSyst_corr','MC'),
        #('2016','Summer16_102X_nAODv5_Full2016v6','MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__kinFitTTSemiLep_2016','kinFitTTSemiLep_jetMETSyst_Total','MC_signal'),
        #('2016','Summer16_102X_nAODv5_Full2016v6','MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__kinFitTTSemiLep_2016','kinFitTTSemiLep_jetMETSyst_uncorr','MC_signal'),
        #('2016','Summer16_102X_nAODv5_Full2016v6','MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__kinFitTTSemiLep_2016','kinFitTTSemiLep_jetMETSyst_corr','MC_signal'),
        #('2016','Summer16_102X_nAODv5_Full2016v6','MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10','kinFitTTSemiLep_2016','MC_ttsyst'),
        #('2016','Run2016_102X_nAODv5_Full2016v6','DATAl1loose2016v6__HMSemilepSKIMv6_10_data','kinFitTTSemiLep_2016','DATA'),
        #('2016','Run2016_102X_nAODv7_Full2016v7','DATAl1loose2016v7','DATACHToCBLepton2016v7','DATA'),
        #('2016','Run2016_102X_nAODv7_Full2016v7','DATAl1loose2016v7','CHToCBJetMETCorr_data','DATA'),
        #('2016','Run2016_102X_nAODv7_Full2016v7','DATAl1loose2016v7__CHToCBJetMETCorr_data','kinFitTTSemiLep_2016','DATA'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7','CHToCBJetMETCorr','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7','CHToCBJetMETCorr','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7','CHToCBJetMETCorr','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_TotalUp','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_TotalUp','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_TotalDown','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_TotalDown','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_uncorrUp','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_uncorrDown','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_corrUp','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_corrDown','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_TotalUp','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_TotalDown','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_uncorrUp','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_uncorrDown','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_corrUp','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_corrDown','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr__kinFitTTSemiLep_2016','UEPS','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr__kinFitTTSemiLep_2016','UEPS','MC_ttsyst'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr__kinFitTTSemiLep_2016','mvaTreeCHToCB','MC'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr__kinFitTTSemiLep_2016','mvaTreeCHToCB','MC_signal'),
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr__kinFitTTSemiLep_2016','mvaTreeCHToCB','MC_ttsyst'), #TT_TuneCUETP8M2T4_PSweights
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_TotalUp','MC_ttsyst'),  #TT_TuneCUETP8M2T4_PSweights
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_TotalDown','MC_ttsyst'),  #TT_TuneCUETP8M2T4_PSweights
        #
        # --- 2017 ---
        #
        #('2017','Fall2017_102X_nAODv7_Full2017v7','Prod','MCl1loose2017v7','MC_signal'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','Prod','MCl1loose2017v7','MC_ttsyst'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7','MCCorr2017v7','MC_signal'),
        #TODO rerun HDAMP
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7','MCCorr2017v7','MC_ttsyst'),
        #('2017','Run2017_102X_nAODv7_Full2017v7','DATAl1loose2017v7','DATACHToCBLepton2017v7','DATA'),
        #('2017','Run2017_102X_nAODv7_Full2017v7','DATAl1loose2017v7','CHToCBJetMETCorr_data','DATA'),
        #('2017','Run2017_102X_nAODv7_Full2017v7','DATAl1loose2017v7__CHToCBJetMETCorr_data','kinFitTTSemiLep_2017','DATA'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7','CHToCBJetMETCorr','MC'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7','CHToCBJetMETCorr','MC_ttsyst'),
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7','CHToCBJetMETCorr','MC_signal'),
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
        #('2018','Run2018_102X_nAODv7_Full2018v7','DATAl1loose2018v7','DATACHToCBLepton2018v7','DATA'),
        #('2018','Run2018_102X_nAODv7_Full2018v7','DATAl1loose2018v7','CHToCBJetMETCorr_data','DATA'),
        #('2018','Run2018_102X_nAODv7_Full2018v7','DATAl1loose2018v7__CHToCBJetMETCorr_data','kinFitTTSemiLep_2018','DATA'),
        ('2018','Run2018_102X_nAODv7_Full2018v7','DATAl1loose2018v7__CHToCBJetMETCorr_data__kinFitTTSemiLep_2018','mvaCHToCB_2018','DATA'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7','CHToCBJetMETCorr','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7','CHToCBJetMETCorr','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7','CHToCBJetMETCorr','MC_ttsyst'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_TotalUp','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_TotalDown','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_HEM','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_uncorrUp','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_uncorrDown','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_corrUp','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_corrDown','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_TotalUp','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_TotalDown','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_HEM','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_uncorrUp','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_uncorrDown','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_corrUp','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_corrDown','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018','MC_ttsyst'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr__kinFitTTSemiLep_2018','mvaTreeCHToCB','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr__kinFitTTSemiLep_2018','mvaTreeCHToCB','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr__kinFitTTSemiLep_2018','mvaTreeCHToCB','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr__kinFitTTSemiLep_2018','mvaCHToCB_2018','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr__kinFitTTSemiLep_2018','mvaCHToCB_2018','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr__kinFitTTSemiLep_2018','mvaCHToCB_2018','MC_ttsyst'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr__kinFitTTSemiLep_2018_jetMETSyst_TotalUp','mvaCHToCB_2018_jetMETSyst_TotalUp','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr__kinFitTTSemiLep_2018_jetMETSyst_TotalUp','mvaCHToCB_2018_jetMETSyst_TotalUp','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr__kinFitTTSemiLep_2018_jetMETSyst_TotalDown','mvaCHToCB_2018_jetMETSyst_TotalDown','MC'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr__kinFitTTSemiLep_2018_jetMETSyst_TotalDown','mvaCHToCB_2018_jetMETSyst_TotalDown','MC_signal'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr__kinFitTTSemiLep_2018','UEPS','MC_ttsyst'),
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr__kinFitTTSemiLep_2018__mvaCHToCB_2018','UEPS','MC_ttsyst'),


    ]

sleep_interval = {
        #('2016','Summer16_102X_nAODv5_Full2016v6','MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__genCHToCB_2016','kinFitTTSemiLep_2016','MC'):'1h',
        #('2016','Run2016_102X_nAODv5_Full2016v6','DATAl1loose2016v6__HMSemilepSKIMv6_10_data','kinFitTTSemiLep_2016','DATA'):'1h',
        #('2016','Summer16_102X_nAODv5_Full2016v6','MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__kinFitTTSemiLep_2016','kinFitTTSemiLep_jetMETSyst_uncorr','MC'):'1h',
        #('2016','Summer16_102X_nAODv5_Full2016v6','MCl1loose2016v6__MCCorr2016v6__HMSemilepSKIMv6_10__kinFitTTSemiLep_2016','kinFitTTSemiLep_jetMETSyst_corr','MC'):'1h',
        #('2017','Fall2017_102X_nAODv5_Full2017v6','MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10','kinFitTTSemiLep_2017','MC'):'1h',
        #('2017','Fall2017_102X_nAODv5_Full2017v6','MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__kinFitTTSemiLep_2017','kinFitTTSemiLep_jetMETSyst_uncorr','MC'):'1h',
        #('2017','Fall2017_102X_nAODv5_Full2017v6','MCl1loose2017v6__MCCorr2017v6__HMSemilepSKIMv6_10__kinFitTTSemiLep_2017','kinFitTTSemiLep_jetMETSyst_corr','MC'):'1h',
        #('2018','Autumn18_102X_nAODv6_Full2018v6','MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10','kinFitTTSemiLep_2018','MC'):'5s',
        #('2018','Autumn18_102X_nAODv6_Full2018v6','MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__kinFitTTSemiLep_2018','kinFitTTSemiLep_jetMETSyst_uncorr','MC'):'1h',
        #('2018','Autumn18_102X_nAODv6_Full2018v6','MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10__kinFitTTSemiLep_2018','kinFitTTSemiLep_jetMETSyst_corr','MC'):'1h',
        #('2018','Autumn18_102X_nAODv6_Full2018v6','MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10','kinFitTTSemiLep_2018','MC_ttsyst'):'5s',
        #('2018','Autumn18_102X_nAODv6_Full2018v6','MCl1loose2018v6__MCCorr2018v6__HMSemilepSKIMv6_10','kinFitTTSemiLep_2018','MC_signal'):'4h',
        #('2018','Run2018_102X_nAODv6_Full2018v6','DATAl1loose2018v6__HMSemilepSKIMv6_10_data','kinFitTTSemiLep_2018','DATA'):'5s',
        #('2016','Run2016_102X_nAODv7_Full2016v7','DATAl1loose2016v7','CHToCBJetMETCorr_data','DATA'):'1h',
        #('2017','Run2017_102X_nAODv7_Full2017v7','DATAl1loose2017v7','CHToCBJetMETCorr_data','DATA'):'1h',
        #('2018','Run2018_102X_nAODv7_Full2018v7','DATAl1loose2018v7','CHToCBJetMETCorr_data','DATA'):'1h',
        ('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_TotalDown','MC'):'1h',
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_uncorrUp','MC'):'1h',
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_uncorrDown','MC'):'1h',
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_corrUp','MC'):'1h',
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_corrDown','MC'):'1h',
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016','MC_signal'):'30m',
        ('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_TotalUp','MC_signal'):'30m',
        ('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_TotalDown','MC_signal'):'30m',
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_uncorrUp','MC_signal'):'30m',
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_uncorrDown','MC_signal'):'30m',
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_corrUp','MC_signal'):'30m',
        #('2016','Summer16_102X_nAODv7_Full2016v7','MCl1loose2016v7__MCCorr2016v7__CHToCBJetMETCorr','kinFitTTSemiLep_2016_jetMETSyst_corrDown','MC_signal'):'30m',
        #('2016','Run2016_102X_nAODv7_Full2016v7','DATAl1loose2016v7__CHToCBJetMETCorr_data','kinFitTTSemiLep_2016','DATA'):'30m',
        #('2017','Run2017_102X_nAODv7_Full2017v7','DATAl1loose2017v7__CHToCBJetMETCorr_data','kinFitTTSemiLep_2017','DATA'):'1h',
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017','MC'):'15m',
        ('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_TotalUp','MC'):'15m',
        ('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_TotalDown','MC'):'15m',
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_uncorrUp','MC'):'15m',
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_uncorrDown','MC'):'15m',
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_corrUp','MC'):'15m',
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_corrDown','MC'):'15m',
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017','MC_signal'):'15m',
        ('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_TotalUp','MC_signal'):'15m',
        ('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_TotalDown','MC_signal'):'15m',
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_uncorrUp','MC_signal'):'15m',
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_uncorrDown','MC_signal'):'15m',
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_corrUp','MC_signal'):'15m',
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017_jetMETSyst_corrDown','MC_signal'):'15m',
        #('2017','Fall2017_102X_nAODv7_Full2017v7','MCl1loose2017v7__MCCorr2017v7__CHToCBJetMETCorr','kinFitTTSemiLep_2017','MC_ttsyst'):'15m',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_TotalUp','MC'):'30m',
        ('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_TotalDown','MC'):'30m',
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_uncorrUp','MC'):'30m',
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_uncorrDown','MC'):'30m',
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_corrUp','MC'):'30m',
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_corrDown','MC'):'30m',
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018','MC_signal'):'30m',
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_TotalUp','MC_signal'):'30m',
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_TotalDown','MC_signal'):'30m',
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_uncorrUp','MC_signal'):'30m',
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_uncorrDown','MC_signal'):'30m',
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_corrUp','MC_signal'):'30m',
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018_jetMETSyst_corrDown','MC_signal'):'30m',
        #('2018','Autumn18_102X_nAODv7_Full2018v7','MCl1loose2018v7__MCCorr2018v7__CHToCBJetMETCorr','kinFitTTSemiLep_2018','MC_ttsyst'):'30m',



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




