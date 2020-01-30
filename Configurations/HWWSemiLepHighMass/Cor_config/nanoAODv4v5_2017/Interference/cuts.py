#import my.Wlep_sel
#import my.final_fatjetsel



#supercut = 'nCleanFatJet==1'



#-----Variable Deinition-----#


cuts['GenPass']= 'GenEvtFlag==1 || GenEvtFlag==2'
cuts['GenBoosted'] = 'GenEvtFlag==1'
cuts['GenResolved']= 'GenEvtFlag==2'
cuts['El']= 'abs(Lepton_pdgId[0])==11'
cuts['Mu']= 'abs(Lepton_pdgId[0])==13'

