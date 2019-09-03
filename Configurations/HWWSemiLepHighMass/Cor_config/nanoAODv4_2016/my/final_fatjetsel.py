##--Preselection--##
List_isfatjet_in_BoostPresel=[]

##--bveto--##
List_isfatjet_inBoostPreselBveto=[]


##--SB--##
List_isfatjet_in_SB=[]
#List_isfatjet_in_SB=[]

##--SR--##
List_isfatjet_inSR=[]

##--TT--##
List_isfatjet_inTT=[]




for i in range(0,10):

    ##--About the ith FatJet--##
    fatjet_id_cut='(Alt$(FatJet_jetId['+str(i)+'],0))'
    tau21_cut='(Alt$(FatJet_tau2[0],9999.)/Alt$(FatJet_tau1[0],1) < 0.4)'
    fatjet_pt_cut='(Alt$(FatJet_pt['+str(i)+'],-1) > 200)'
    fatjet_eta_cut='(abs(Alt$(FatJet_eta['+str(i)+'],999))<2.4)'
    fatjet_tightlep_clean='( sqrt( pow( Alt$( FatJet_eta['+str(i)+']-Lepton_eta[0],0 ) ,2  ) + pow( Alt$( FatJet_phi['+str(i)+']-Lepton_phi[0],0 ) ,2 )   ) > 0.8  ) '
    fatjet_msoftdropcut='(FatJet_msoftdrop['+str(i)+'] > 40)'

    
    ##PreSelection##
    pass_BoostPreselFatJetCut='('+'&&'.join([fatjet_id_cut,tau21_cut,fatjet_pt_cut,fatjet_eta_cut,fatjet_tightlep_clean,fatjet_msoftdropcut])+')'
    List_isfatjet_in_BoostPresel.append(pass_BoostPreselFatJetCut)



    ##For all addtional jet, find bjet##
    List_isaddbjet=[]
    for j in range(0,20):
        addjet_id_cut='(Alt$(Jet_jetId['+str(j)+'],-1)>0)'
        addjet_pt_cut='(Alt$(Jet_pt['+str(j)+'],-1)>20)'
        addjet_eta_cut='(Alt$(fabs(Jet_eta['+str(j)+'],999)) < 2.4)'
        addjet_not_in_fatjet='1'
        bool_list_addjet_not_in_fatjet=[]
        for sub_i in range(0,10):

            addjet_not_in_fatjet='((j!=Alt$(FatJet_subJetIdx1['+str(sub_i)+'],-1))&&(j!=Alt$(FatJet_subJetIdx2['+str(sub_i)+'],-1)))'
            bool_list_addjet_not_in_fatjet.append(addjet_not_in_fatjet)

        addjet_not_in_fatjet='&&'.join(bool_list_addjet_not_in_fatjet)
        ##now jth jet is an addtional jet##                                                                                                  
        #jth jet must not be btagged                                                                                                         
        #btagDeepB==deepcsv                                                                                                                  
        addjet_btag='(Alt$(Jet_DeepB['+str(j)+'],1) > 0.2217)'
        addjet_isbjet='('+('&&'.join([addjet_id_cut,addjet_pt_cut,addjet_eta_cut,addjet_not_in_fatjet,addjet_btag]))+')'
        List_isaddbjet.append(addjet_isbjet)

        
    is_bevent=  "("+("||".join(List_isaddbjet))+")"    
    pass_bveto= "(!"+is_bevent+")"


    ##--Preselection+bvetro--## inverse of TTbar CR ##
    List_isfatjet_inBoostPreselBveto.append(pass_BoostPreselFatJetCut+'*'+pass_bveto)
    ###Done. btag###

    ##--SR--##
    msoftdropcut_SR='(FatJet_msoftdrop['+str(i)+'] >65 && FatJet_msoftdrop['+str(i)+']<105)'
    pass_SREvent='('+pass_BoostPreselFatJetCut+'&&'+msoftdropcut_SR+'&& '+pass_bveto+')'
    List_isfatjet_inSR.append(pass_SREvent)



    ##--SB--##
    msoftdropcut_SB='('+'(!'+msoftdropcut_SR+')&&'+'(FatJet_msoftdrop['+str(i)+']<250))'
    pass_SBEvent='('+pass_BoostPreselFatJetCut+'&&'+msoftdropcut_SB+'&& '+pass_bveto+')'
    List_isfatjet_in_SB.append(pass_SBEvent)


    
    ##--TTbar CR--##
    pass_TTEvent='('+pass_BoostPreselFatJetCut+'&&'+is_bevent+')'
    List_isfatjet_inTT.append(pass_TTEvent)

    
    


nFatJet_inBoostPresel='+'.join(List_isfatjet_in_BoostPresel)
isBoostPreselEvent='||'.join(List_isfatjet_in_BoostPresel)

List_isfatjet_inBoostPreselBveto='+'.join(List_isfatjet_inBoostPreselBveto)
isBoostPreselEvent='||'.join(List_isfatjet_inBoostPreselBveto)


nFatJet_inSB='+'.join(List_isfatjet_in_SB)
isSBEvent='||'.join(List_isfatjet_in_SB)

nFatJet_inSR='+'.join(List_isfatjet_inSR)
isSREvent='||'.join(List_isfatjet_inSR)

nFatJet_inTT='+'.join(List_isfatjet_inTT)
isTTEvent='||'.join(List_isfatjet_inTT)

print isTTEvent

#print nFinalFatJet
#print isFinalFatJetEvent
