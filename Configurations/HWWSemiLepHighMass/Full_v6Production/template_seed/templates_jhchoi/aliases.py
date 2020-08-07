import os
import copy
import inspect
import numpy as np

##---WP---##
from WPandCut2016 import *
_ALGO="_"+ALGO
_ALGO_="_"+ALGO+"_"
##-End WP--##

##--Get Boosted OR Resolved--##
if 'opt' in globals():
    configration_py=opt.aliasesFile
else:
    configration_py=sys.argv[0]

Boosted=False
Resolved=False
if 'Boosted' in configration_py:
    Boosted=True
if 'Resolved' in configration_py:
    Resolved=True
##End of 


configurations = '%s/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/' % os.getenv('CMSSW_BASE')
print configurations

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

###---Btag SF---###
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
    'expr': 'TMath::Exp(Sum$(TMath::Log((Jet_pt_nom[CleanJet_jetIdx]>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(Jet_pt_nom[CleanJet_jetIdx]<20 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}
#for shift in ['jes', 'lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
for shift in ['lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
    #aliases['Jet_btagSF_shapeFix_up_%s' % shift] = {                                                                                                         
    aliases['Jet_btagSF%sup_shapeFix' % shift] = {
        'class': 'BtagSF',
        'args': (btagSFSource, 'up_' + shift),
        'samples': mc
    }
    aliases['Jet_btagSF%sdown_shapeFix' % shift] = {
        'class': 'BtagSF',
        'args': (btagSFSource, 'down_' + shift),
        'samples': mc
    }
 
    aliases['btagSF%sup' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
        'samples': mc
    }

    aliases['btagSF%sdown' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
        'samples': mc
    }




puidSFSource = os.getcwd()+'/JetPUID/PUID_81XTraining_EffSFandUncties.root'

aliases['PUJetIdSF'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
        '.L '+os.getcwd()+'/JetPUID/pujetidsf_event_new.cc+'
    ],
    'class': 'PUJetIdEventSF',
    'args': (puidSFSource, Year, 'loose'),
    'samples': mc
}




##--common variabls for Boosted/Resolved
aliases['isBoost']={
    'expr':'(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0))'
}

aliases['isBoostSR']={
    'expr':'(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0) && (isBoostSR_'+WTAG+'_nom))'
}
aliases['isFinalBoostSR']={
    'expr':'(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0) && (isBoostSR_'+WTAG+'_nom) && ((nBJetBoost_'+WTAG+'_nom ==0)))'
}


###--Wtagger ID eff. SF
aliases['WtaggerSFnom']={
    #'expr' : '('+WtaggerSF+')'+'*(isBoost_'+WTAG+'_nom) + 1*(!isBoost_'+WTAG+'_nom)',
    #'expr' : 'isBoost_'+WTAG+'_nom ? ('+WtaggerSF+')'+' : 1',
    'expr' : '(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0) && (WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] > 65) && (WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] < 105) ) ? ('+WtaggerSF+')'+' : 1',
    'samples' : mc
}
aliases['WtaggerSFup']={
    #'expr' : 'isBoost_'+WTAG+'_nom ? ('+WtaggerSFup+')'+' : 1',
    #'expr' : '('+WtaggerSFup+')'+'*(isBoost_'+WTAG+'_nom) + 1*(!isBoost_'+WTAG+'_nom)',
    'expr' : '(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0) &&(WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] > 65) &&(WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] < 105)) ? ('+WtaggerSFup+')'+' : 1',
    'samples' : mc
}
aliases['WtaggerSFdown']={
    #'expr' : 'isBoost_'+WTAG+'_nom ? ('+WtaggerSFdown+')'+' : 1',
    #'expr' : '('+WtaggerSFdown+')'+'*(isBoost_'+WTAG+'_nom) + 1*(!isBoost_'+WTAG+'_nom)',
    'expr' : '(isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0) && (WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] > 65) && (WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] < 105) ) ? ('+WtaggerSFdown+')'+' : 1',
    'samples' : mc
}





##---TrigSF
aliases['trigWeight']={
    'expr' : 'TriggerEffWeight_1l*'+'(Lepton_isTightMuon_'+muWP+'[0]>0.5) + Trigger_sngEl*(Lepton_isTightElectron_'+eleWP+'[0]>0.5)', ##eletron trig_eff_SF isnot valid yet
    #'expr' : 'TriggerEffWeight_1l',
    'samples':mc
}
##--Lepton ISO/ID/RECO
aliases['LepWPweight']={
    'expr':'(((Lepton_isTightElectron_'+eleWP+'[0]>0.5)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'[0]'+')) + ((Lepton_isTightMuon_'+muWP+'[0]>0.5)*(Lepton_tightMuon_'+muWP+'_TotSF'+'[0]'+')))',
    'samples':mc
}

aliases['LepWPCut']={
    'expr':'(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
}

aliases['SFweight']={
    'expr':SFweight,
    'samples':mc
}



aliases['nJetPassBKin']={
    'expr':'Sum$(Jet_pt_nom[CleanJet_jetIdx]>20 && abs(CleanJet_eta)<2.5)'
}

aliases['JetMultplicity']={
    'expr':'Sum$(Jet_pt_nom[CleanJet_jetIdx]>'+jetptmin+' && abs(CleanJet_eta)<'+jetetamax+')'
}

aliases['JetMultplicity_eta4p7']={
    'expr':'Sum$(Jet_pt_nom[CleanJet_jetIdx]>'+jetptmin+' && abs(CleanJet_eta)<4.7)'
}


for M_MELA in MELA_MASS_BOOST:
    for C in MELA_C_BOOST:
        M=str(M_MELA)
        C=str(C)
        P_S='meP'+M+'_Bst_ggf_S_'+WTAG+'_nom'
        P_B='meP'+M+'_Bst_ggf_B_'+WTAG+'_nom'
        P_B_S=P_B+'/'+P_S
        aliases['MEKD_Bst_C_'+C+'_M'+str(M)]={
            'expr':P_S+'>0 ? '+'1/(1+'+C+'*'+P_B_S+')'+':-1'
        }


for M_MELA in MELA_MASS_RESOL:
    for C in MELA_C_RESOL:
        M=str(M_MELA)
        C=str(C)
        P_S='meP'+M+'_Res_ggf_S_'+ALGO+'_nom'
        P_B='meP'+M+'_Res_ggf_B_'+ALGO+'_nom'
        P_B_S=P_B+'/'+P_S
        aliases['MEKD_Res_C_'+C+'_M'+str(M)]={
            'expr':P_S+'>0 ? '+'1/(1+'+C+'*'+P_B_S+')'+':-1'
        }



##--some missing branch
#PuppiMET_nom_pt
#aliases['PuppiMET_nom_pt']={
#    'expr':'sqrt(PuppiMET_nom_px*PuppiMET_nom_px+PuppiMET_nom_py*PuppiMET_nom_py)'
#}

if Year=='2018':
    lastcopy = (1 << 13)
    aliases['topGenPtOTF'] = {
        'expr': 'Sum$((GenPart_pdgId == 6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
        'samples': ['top']
    }

    aliases['antitopGenPtOTF'] = {
        'expr': 'Sum$((GenPart_pdgId == -6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
        'samples': ['top']
    }

    aliases['Top_pTrw'] = {
        #'expr': '(topGenPtOTF * antitopGenPtOTF > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPtOTF) - 0.000134*topGenPtOTF + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPtOTF) - 0.000134*antitopGenPtOTF + 0.973))) + (topGenPtOTF * antitopGenPtOTF <= 0.)',
        #    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPt) - 0.000134*topGenPt + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPt) - 0.000134*antitopGenPt + 0.973))) + (topGenPt * antitopGenPt <= 0.)',
        'expr':'1',
        'samples': ['top']
    }


if Year=='2017':

    aliases['Top_pTrw'] = {
        'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPt) - 0.000134*topGenPt + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPt) - 0.000134*antitopGenPt + 0.973))) + (topGenPt * antitopGenPt <= 0.)',
        'samples': ['top']
    }

if Year=='2016':
    aliases['Top_pTrw']={

        'expr':'(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPt) - 0.000134*topGenPt + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPt) - 0.000134*antitopGenPt + 0.973))) * (TMath::Sqrt(TMath::Exp(1.61468e-03 + 3.46659e-06*topGenPt - 8.90557e-08*topGenPt*topGenPt) * TMath::Exp(1.61468e-03 + 3.46659e-06*antitopGenPt - 8.90557e-08*antitopGenPt*antitopGenPt))) + (topGenPt * antitopGenPt <= 0.)', # Same Reweighting as other years, but with additional fix for tune CUET -> CP5                                                                                     
        'samples':['top']
    }



aliases['LHEPartWlepPt'] = {
    #'linesToAdd': ['.L %s/HWWSemiLepHighMass/Full2017/LHEPartWlepPt.cc+' % configurations],
    'linesToAdd':['.L '+os.getcwd()+'/W_EWKNLO/LHEPartWlepPt.cc+'],
    'class': 'LHEPartWlepPt',
    'samples': ['Wjets0j', 'Wjets1j','Wjets2j']
}
data = np.genfromtxt(os.getenv('CMSSW_BASE')+'/src/LatinoAnalysis/Gardener/python/data/ewk/kewk_w.dat', skip_header=2, skip_footer=7)
weight_string = "("
uncert_string = "("
for row in data:
    low  = row[0]
    high = row[1]
    weight = (1+row[2])
    ucert = row[3]

    weight_string+="({}<LHEPartWlepPt[0] && LHEPartWlepPt[0]<={})*{}+".format(low, high, weight)
    uncert_string+="({}<LHEPartWlepPt[0] && LHEPartWlepPt[0]<={})*{}+".format(low, high, weight)
# remove trailing + sign and close parentheses
weight_string=weight_string[:-1]+")"
uncert_string=uncert_string[:-1]+")"

aliases['EWK_W_correction'] = {
    'expr': weight_string,
    'samples': ['Wjets0j', 'Wjets1j','Wjets2j']
}
aliases['EWK_W_correction_uncert'] = {
    'expr': uncert_string,
    # 'samples': 'Wjets'
    'samples': ['Wjets0j', 'Wjets1j','Wjets2j']
}

aliases['dPhi_WW_boosted']={
    #'expr':' ((isBoost_'+WTAG+'_nom)&&(lnJ_'+WTAG+'_nom_widx >=0)) ? (WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi)-2*3.1415927*(  (WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi) > 3.1415927) + 2*3.1415927*((WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi) < 3.1415927) : -100.'
    'expr':' ('+aliases['isBoost']['expr']+') ? (WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi)-2*3.1415927*(  (WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi) > 3.1415927) + 2*3.1415927*((WtaggerFatjet_'+WTAG+'_nom_phi[lnJ_'+WTAG+'_nom_widx]-Wlep_nom_phi) < 3.1415927) : -100.'
}


aliases['dPhi_WW_resolved']={
    'expr':'(Whad'+_ALGO_+'nom_phi-Wlep_nom_phi)-2*3.1415927*(  (Whad'+_ALGO_+'nom_phi-Wlep_nom_phi) > 3.1415927) + 2*3.1415927*((Whad'+_ALGO_+'nom_phi-Wlep_nom_phi) < 3.1415927)'
}


#aliases['nCleanGenJet'] = {
#    'linesToAdd': ['.L '+os.getcwd()+'/ngenjet.cc+'
#    ],
#    'class': 'CountGenJet',
#    'samples': mc

#}

#aliases['GenJet_HT'] = {
#    'expr':'Sum$(GenJet_pt)',
#    'samples':mc
#}

##---python name
import sys
sys.path.insert(0, "MjjShapeWeight")
from MjjShapeWeight import DICT_MjjShapeW

if 'opt' in globals():
    configration_py=opt.aliasesFile
else:
    configration_py=sys.argv[0]

##---MjjShapeSys --configuration
if Boosted:
    #WmassVariable=' ((isBoost_'+WTAG+'_nom && (lnJ_'+WTAG+'_nom_widx >=0)) ? WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] : -1)'
    WmassVariable=' (('+aliases['isBoost']['expr']+') ? WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx] : -1)'
    bst='Boosted'
if Resolved:
    WmassVariable='Whad'+_ALGO_+'nom_mass'
    bst='Resolved'
print "[WmassVariable]",WmassVariable


#slope=DICT_MjjShapeW[Year][bst]['slope']
slope=DICT_MjjShapeW['combined'][bst]['slope']
#intercept=DICT_MjjShapeW[Year][bst]['intercept']
intercept=DICT_MjjShapeW['combined'][bst]['intercept']
slope=str(slope)
intercept=str(intercept)
massbins=[40,45,50,55,65,70,75,80,85,90,95,100,105,110,115,120,125,130,150,170,200,250]
bincenter_list=[]
for idx in range(0,len(massbins)-1):
    lowbin=str(massbins[idx])
    highbin=str(massbins[idx+1])
    center=str((massbins[idx]+massbins[idx+1])/2)
    bincenter_list.append(' ((  ('+WmassVariable+' > '+lowbin+') && ('+WmassVariable+' <='+highbin+')  )*'+center+') ') ##wmass * slope
bincenter_list=[]
for idx in range(0,len(massbins)-1):
    lowbin=str(massbins[idx])
    highbin=str(massbins[idx+1])
    center=str((massbins[idx]+massbins[idx+1])/2)
    bincenter_list.append(' ((  ('+WmassVariable+' > '+lowbin+') && ('+WmassVariable+' <='+highbin+')  )*'+center+') ') ##wmass * slope
wmass='+'.join(bincenter_list) ##wmass
##wmass bin center
aliases['wmass']={
    'expr':wmass
}
##--weight for make slope shape
aliases['SlopeWeight']={
    'expr':'wmass > 0 ? (250-wmass)/210. : 0'
}
##----reweight                                                                                                                                                                                             
aliases['MjjShape']={
    'expr':'wmass > 0 ? '+intercept+'+'+slope+'*(250-wmass)/210. : 0'
}
##----if not reweight (if you don't want it or to measure fitting param)
if not MjjShapeCorr:
    aliases['MjjShape']={
        'expr':'1'
    }

##---[END]MjjShapeSys--##



##--Simple Expression for plotting--##
##--common variabls for Boosted/Resolved

aliases['nAK4Jet']={
    'expr':'Sum$(Jet_pt_nom[CleanJet_jetIdx]>'+jetptmin+' && abs(CleanJet_eta)<'+jetetamax+')'
}
aliases['nAK4Jet_eta4p7']={
    'expr':'Sum$(Jet_pt_nom[CleanJet_jetIdx]>'+jetptmin+' && abs(CleanJet_eta)<4.7)'
}

aliases['LeadingJet_BtagScore']={
    'expr':'Jet_btagDeepB[CleanJet_jetIdx[0]]'
}
aliases['LeadingJet_pt']={
    'expr':'Jet_pt_nom[CleanJet_jetIdx[0]]'
}
aliases['LeadingJet_eta']={
    'expr':'Jet_eta[CleanJet_jetIdx[0]]'
}

aliases['SubLeadingJet_BtagScore']={
    'expr':'Jet_btagDeepB[CleanJet_jetIdx[1]]'
}
aliases['SubLeadingJet_pt']={
    'expr':'Jet_pt_nom[CleanJet_jetIdx[1]]'
}
aliases['SubLeadingJet_eta']={
    'expr':'Jet_eta[CleanJet_jetIdx[1]]'
}
 


##--BJet--##
if Boosted:
    aliases['nBJet']={
        'expr':'nBJetBoost_'+WTAG+'_nom'
    }
if Resolved:
    aliases['nBJet']={
        'expr':'nBJetResol_'+ALGO+'_nom'
    }


##--addjet--##
if Boosted:
    aliases['AddJet_BtagScore']={
        'expr':'Jet_btagDeepB[CleanJet_jetIdx[AddJetBoost_'+WTAG+'_nom_cjidx]]'
    }
    aliases['nAddJet']={
        'expr':'Sum$(AddJetBoost_'+WTAG+'_nom_cjidx>=0)'
    }
    aliases['AddJet_eta']={
        'expr':'AddJetBoost_'+WTAG+'_nom_eta'
    }
    aliases['AddJet_pt']={
        'expr':'AddJetBoost_'+WTAG+'_nom_pt'
    }

    aliases['LeadingAddJet_BtagScore']={
        'expr':'Jet_btagDeepB[CleanJet_jetIdx[AddJetBoost_'+WTAG+'_nom_cjidx[0]]]'
    }
    aliases['LeadingAddJet_eta']={
        'expr':'AddJetBoost_'+WTAG+'_nom_eta[0]'
    }
    aliases['LeadingAddJet_pt']={
        'expr':'AddJetBoost_'+WTAG+'_nom_pt[0]'
    }


    aliases['SubLeadingAddJet_BtagScore']={
        'expr':'Jet_btagDeepB[CleanJet_jetIdx[AddJetBoost_'+WTAG+'_nom_cjidx[1]]]'
    }
    aliases['SubLeadingAddJet_eta']={
        'expr':'AddJetBoost_'+WTAG+'_nom_eta[1]'
    }
    aliases['SubLeadingAddJet_pt']={
        'expr':'AddJetBoost_'+WTAG+'_nom_pt[1]'
    }


if Resolved:
    aliases['AddJet_BtagScore']={
        'expr':'Jet_btagDeepB[CleanJet_jetIdx[AddJetResol_'+ALGO+'_nom_cjidx]]'
    }
    aliases['nAddJet']={
        'expr':"Sum$(AddJetResol_dMchi2Resolution_nom_cjidx>=0)"
    }
    aliases['AddJet_eta']={
        'expr':'AddJetResol_'+ALGO+'_nom_eta'
    }
    aliases['AddJet_pt']={
        'expr':'AddJetResol_'+ALGO+'_nom_pt'
    }

    aliases['LeadingAddJet_BtagScore']={
        'expr':'Jet_btagDeepB[CleanJet_jetIdx[AddJetResol_'+ALGO+'_nom_cjidx[0]]]'
    }
    aliases['LeadingAddJet_eta']={
        'expr':'AddJetResol_'+ALGO+'_nom_eta[0]'
    }
    aliases['LeadingAddJet_pt']={
        'expr':'AddJetResol_'+ALGO+'_nom_pt[0]'
    }


    aliases['SubLeadingAddJet_BtagScore']={
        'expr':'Jet_btagDeepB[CleanJet_jetIdx[AddJetResol_'+ALGO+'_nom_cjidx[1]]]'
    }
    aliases['SubLeadingAddJet_eta']={
        'expr':'AddJetResol_'+ALGO+'_nom_eta[1]'
    }
    aliases['SubLeadingAddJet_pt']={
        'expr':'AddJetResol_'+ALGO+'_nom_pt[1]'
    }


##--Hadronic W--##

if Boosted:
    ##--Hadronic W--##
    aliases['HadronicW_mass']={
        'expr':'WtaggerFatjet_'+WTAG+'_nom_mass[lnJ_'+WTAG+'_nom_widx]'
    }
    aliases['HadronicW_pt']={
        'expr':'WtaggerFatjet_'+WTAG+'_nom_pt[lnJ_'+WTAG+'_nom_widx]'
    }
    aliases['HadronicW_Score']={}
    if 'HP' in WTAG:
        aliases['HadronicW_Score']['expr']='WtaggerFatjet_'+WTAG+'_nom_tau21ddt[lnJ_'+WTAG+'_nom_widx]'
    if 'DeepAK8' in WTAG:
        if not 'MD' in WTAG:
            aliases['HadronicW_Score']['expr']='WtaggerFatjet_'+WTAG+'_nom_deepTag[lnJ_'+WTAG+'_nom_widx]'
        else:
            aliases['HadronicW_Score']['expr']='WtaggerFatjet_'+WTAG+'_nom_deepTagMD[lnJ_'+WTAG+'_nom_widx]'

if Resolved:
    aliases['HadronicW_mass']={
        'expr':'Whad'+_ALGO_+'nom_mass'
    }
    aliases['HadronicW_pt']={
        'expr':'Whad'+_ALGO_+'nom_pt'
    }
    aliases['HadronicW_Score']={}
    aliases['HadronicW_Score']['expr']='Whad'+_ALGO_+'nom_ScoreToLeast'



##--WW--##
if Boosted:
    aliases['WW_mass']={
        'expr':'lnJ_'+WTAG+'_nom_mass'
    }
    aliases['WW_pt_over_mass']={
        'expr':'lnJ_'+WTAG+'_nom_minPtWOverM'
    }
    

if Resolved:
    aliases['WW_mass']={
        'expr':'lnjj_'+ALGO+'_nom_mass'
    }
    aliases['WW_pt_over_mass']={
        'expr':'lnjj_'+ALGO+'_nom_minPtWOverM'
    }
    aliases['WW_Mt']={
        'expr':'lnjj'+_ALGO_+'nom_Mt'
    }


##--VBF--
if Boosted:
    aliases['maxmjj_mass_jj_VBF']={
        'expr':'max_mjj_Boost_'+WTAG+'_nom'
    }
    aliases['maxmjj_dEta_jj_VBF']={
        'expr':'dEta_of_max_mjj_Boost_'+WTAG+'_nom'
    }


    aliases['mass_jj_VBF']={
        'expr':'VBFjjBoost_mjj_'+WTAG+'_nom'
    }

    aliases['dEta_jj_VBF']={
        'expr':'VBFjjBoost_dEta_'+WTAG+'_nom'
    }

if Resolved:
    aliases['maxmjj_mass_jj_VBF']={
        'expr':'max_mjj_Resol_'+ALGO+'_nom'
    }
    aliases['maxmjj_dEta_jj_VBF']={
        'expr':'dEta_of_max_mjj_Resol_'+ALGO+'_nom'
    }

    aliases['mass_jj_VBF']={
        'expr':'VBFjjResol_mjj_'+ALGO+'_nom'
    }
    aliases['dEta_jj_VBF']={
        'expr':'VBFjjResol_dEta_'+ALGO+'_nom'
    }
    
