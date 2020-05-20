import os
import copy
import inspect
import sys
sys.path.insert(0, "MassPoints")
from List_melaKDmass import *




eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'



configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations)

aliases['BoostVbfSR']    = {
                           'expr' : '(isBoostSR && isVBF_Boost  && nBJetBoostVBF==0)'
			   }
aliases['BoostNoVbfSR'] = {
                           'expr' : '(isBoostSR && !isVBF_Boost && nBJetBoost==0)' 
			   }
aliases['ResolVbfSR']    = {
                           'expr' : '(isResolSR && isVBF_Resol  && nBJetResolVBF==0)' 
			   }
aliases['ResolNoVbfSR'] = {
                           'expr' : '(isResolSR && !isVBF_Resol && nBJetResol==0)'
			   }

for mass in List_melaKDmass:
  aliases['P_BstGF'+str(mass)] = {
      'expr' : 'meP'+str(mass)+'_BstNoT_ggf_S > 0 ? (meP'+str(mass) + '_BstNoT_ggf_S)/(meP'+str(mass) + '_BstNoT_ggf_S + meP' + str(mass) + '_BstNoT_ggf_B ) : -1'
      }

  aliases['P_RsvGF'+str(mass)] = {
      'expr' : 'meP'+str(mass)+'_ResNoT_ggf_S > 0 ? meP'+str(mass) + '_ResNoT_ggf_S/(meP'+str(mass) + '_ResNoT_ggf_S + meP' + str(mass) + '_ResNoT_ggf_B ) : -1'
      }



mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]


btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_94XSF_V2_B_F.csv' % os.getenv('CMSSW_BASE')

aliases['Jet_btagSF_shapeFix'] = {
    'linesToAdd': [
        'gSystem->Load("libCondFormatsBTauObjects.so");',
        'gSystem->Load("libCondToolsBTau.so");',
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
        '.L %s/patches/btagsfpatch.cc+' % configurations
    ],
    'class': 'BtagSF',
    'args': (btagSFSource,),
    'samples': mc
}





aliases['btagSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}

#for shift in ['jes', 'lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
#    #aliases['Jet_btagSF_shapeFix_up_%s' % shift] = {
#    aliases['Jet_btagSF%sup_shapeFix' % shift] = {
#        'class': 'BtagSF',
#        'args': (btagSFSource, 'up_' + shift),
#        'samples': mc
#    }
#    aliases['Jet_btagSF%sdown_shapeFix' % shift] = {
#        'class': 'BtagSF',
#        'args': (btagSFSource, 'down_' + shift),
#        'samples': mc
#    }
#    '''
#    for targ in ['bVeto', 'bReq']:
#        alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
#        alias['expr'] = alias['expr'].replace('btagSF_shapeFix', 'btagSF_shapeFix_up_%s' % shift)
#
#        alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
#        alias['expr'] = alias['expr'].replace('btagSF_shapeFix', 'btagSF_shapeFix_down_%s' % shift)
#    '''
#    
#
#    aliases['btagSF%sup' % shift] = {
#        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
#        'samples': mc
#    }
#
#    aliases['btagSF%sdown' % shift] = {
#        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
#        'samples': mc
#    }
