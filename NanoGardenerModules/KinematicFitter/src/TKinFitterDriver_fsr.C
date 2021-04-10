#include "TKinFitterDriver_fsr.h"

TKinFitterDriver::TKinFitterDriver(){

}


TKinFitterDriver::TKinFitterDriver(int DataYear_){

  DataYear = DataYear_;

  fitter = new TKinFitter("fitter","fitter");

  error_lepton.ResizeTo(1,1);
  error_neutrino_pxpypz.ResizeTo(3,3);

  error_lepton.Zero();
  error_neutrino_pxpypz.Zero();

  ts_correction = new TSCorrection(DataYear);
  //ts_correction->ReadFittedError("fit_error_pythia.txt");
  //ts_correction->ReadFittedMean("fit_mean_pythia.txt");

  fit_lepton = new TFitParticlePt();
  fit_neutrino_pxpypz =  new TFitParticleMCCart();
  //fit_neutrino_pz =  new TFitParticlePz();

  constrain_hadronic_top_M = new TFitConstraintM("hadronic_top_mass_constraint", "hadronic_top_mass_constraint", 0, 0, 172.5);
  //constrain_hadronic_top_MGaus = new TFitConstraintMGaus("hadronic_top_mass_constraint", "hadronic_top_mass_constraint", 0, 0, 172.5, 1.5);
  constrain_leptonic_top_M = new TFitConstraintM("leptonic_top_mass_constraint", "leptonic_top_mass_constraint", 0, 0, 172.5);
  //constrain_leptonic_top_MGaus = new TFitConstraintMGaus("leptonic_top_mass_constraint", "leptonic_top_mass_constraint", 0, 0, 172.5, 1.5);
  constrain_leptonic_W_M = new TFitConstraintM("leptonic_w_mass_constraint", "leptonic_w_mass_constraint", 0, 0, 80.4);
  //constrain_leptonic_W_MGaus = new TFitConstraintMGaus("leptonic_w_mass_constraint", "leptonic_w_mass_constraint", 0, 0, 80.4, 2.085);
  //cout <<"TKinFitterDriver::TKinFitterDriver : initialized" << endl;
  constrain_pX = new TFitConstraintEp("pX","pX",TFitConstraintEp::component::pX,0.);
  constrain_pY = new TFitConstraintEp("pY","pY",TFitConstraintEp::component::pY,0.);
}


TKinFitterDriver::~TKinFitterDriver(){
  delete fitter;

  for(auto* fit_par:fit_hadronic_top_b_jet){
  delete fit_par;
  }
  for(auto* fit_par:fit_leptonic_top_b_jet){
  delete fit_par;
  }
  for(auto* fit_par:fit_hadronic_w_ch_jet1){
  delete fit_par;
  }
  for(auto* fit_par:fit_hadronic_w_ch_jet2){
  delete fit_par;
  }
  for(auto* fit_par:fit_extra_jets){
  delete fit_par;
  }
  delete fit_lepton;
  delete fit_neutrino_pxpypz;
  //delete fit_neutrino_pz;

  delete constrain_hadronic_top_M;
  //delete constrain_hadronic_top_MGaus;
  delete constrain_leptonic_top_M;
  //delete constrain_leptonic_top_MGaus;
  delete constrain_leptonic_W_M;
  //delete constrain_leptonic_W_MGaus;
  delete constrain_pX;
  delete constrain_pY;
  delete ts_correction;
}


void TKinFitterDriver::SetDataYear(int i){
  DataYear = i;
}


void TKinFitterDriver::SetAllObjects(std::vector<TLorentzVector> jet_vector_,
                                     std::vector<bool> btag_vector_,
                                     TLorentzVector lepton_,
                                     TLorentzVector met_){

  //cout << "jet vector size " << jet_vector_.size() << endl; 
  //cout << "btag vector size " << btag_vector_.size() << endl; 
  jet_vector.clear();
  for(UInt_t i=0; i<jet_vector_.size(); i++){
    jet_vector.push_back(jet_vector_.at(i));
  }
  btag_vector.clear();
  for(UInt_t i=0; i<btag_vector_.size(); i++){
    btag_vector.push_back(btag_vector_.at(i));
  }
  njets = jet_vector.size();
  nbtags = std::accumulate(btag_vector.begin(), btag_vector.end(),0);

  permutation_vector.clear();
  for(int i(0); i<njets; i++){
    if(i==0) permutation_vector.push_back( HADRONIC_TOP_B );
    else if(i==1) permutation_vector.push_back( LEPTONIC_TOP_B );
    else if(i==2) permutation_vector.push_back( W_CH_UP_TYPE );
    else if(i==3) permutation_vector.push_back( W_CH_DOWN_TYPE );
    else permutation_vector.push_back( NONE );
    
  } 
  METv = met_;
  this->SetLepton(lepton_);
  
  //cout <<"TKinFitterDriver::SetAllObjects : " << endl;
}


void TKinFitterDriver::SetAllObjects(std::vector<TLorentzVector> jet_vector_,
                                     std::vector<double> btag_csv_vector_,
                                     double btag_cut_,
                                     TLorentzVector lepton_,
                                     TLorentzVector met_){
  btag_csv_vector = btag_csv_vector_;
  std::vector<bool> btag_vector_;
  for(UInt_t i=0; i<btag_csv_vector.size(); i++){
    if(btag_csv_vector.at(i)>btag_cut_){
      btag_vector_.push_back(true);
    }
    else{
      btag_vector_.push_back(false);
    }
  }

  this->SetAllObjects(jet_vector_,
                      btag_vector_,
                      lepton_,
                      met_
                     );

}


void TKinFitterDriver::SetJetPtResolution(std::vector<float> jetPtResolution_){
  jet_pt_resolution_vector.clear();
  for(auto& x : jetPtResolution_){
    jet_pt_resolution_vector.push_back(x);
  }
}

//void TKinFitterDriver::SetHadronicTopBJets(TLorentzVector jet_){
//  hadronic_top_b_jet = jet_;
//  double Pt = hadronic_top_b_jet.Pt();
//  double Eta = hadronic_top_b_jet.Eta();
//  double Phi = hadronic_top_b_jet.Phi();
//  this->SetJetError(&error_hadronic_top_b_jet, Pt, Eta, Phi, "b");
//  corr_hadronic_top_b_jet = ts_correction->GetCorrectedJet("b",hadronic_top_b_jet);
//  fit_hadronic_top_b_jet->~TFitParticlePt();
//  new(fit_hadronic_top_b_jet) TFitParticlePt("hadronic_top_b_jet",
//                                                    "hadronic_top_b_jet",
//                                                    &corr_hadronic_top_b_jet,
//                                                    &error_hadronic_top_b_jet
//                                                   );
//  //cout <<"TKinFitterDriver::SetHadronicTopBJets : " << endl;
//
//}


//void TKinFitterDriver::SetLeptonicTopBJets(TLorentzVector jet_){
//  leptonic_top_b_jet=jet_;
//  double Pt = leptonic_top_b_jet.Pt();
//  double Eta = leptonic_top_b_jet.Eta();
//  double Phi = leptonic_top_b_jet.Phi();
//  this->SetJetError(&error_leptonic_top_b_jet, Pt, Eta, Phi, "b");
//  //XXX when we vary only leptonic top b jet pt
//  //corr_leptonic_top_b_jet = ts_correction->GetCorrectedJet("b",leptonic_top_b_jet) + lepton + neutrino_pxpy + neutrino_pz;
//  //XXX when we vary only leptonic top b jet pt and neutrino_pxpy
//  //corr_leptonic_top_b_jet = ts_correction->GetCorrectedJet("b",leptonic_top_b_jet) + lepton + neutrino_pz;
//  corr_leptonic_top_b_jet = ts_correction->GetCorrectedJet("b",leptonic_top_b_jet);
//  fit_leptonic_top_b_jet->~TFitParticlePt();
//  new(fit_leptonic_top_b_jet) TFitParticlePt("leptonic_top_b_jet",
//                                                    "leptonic_top_b_jet",
//                                                    &corr_leptonic_top_b_jet,
//                                                    &error_leptonic_top_b_jet
//                                                   );
//  //cout <<"TKinFitterDriver::SetLeptonicTopBJets : " << endl;
//}
//
//
//void TKinFitterDriver::SetWCHUpTypeJets(TLorentzVector jet_){
//  hadronic_w_ch_jet1=jet_;
//  double Pt = hadronic_w_ch_jet1.Pt();
//  double Eta = hadronic_w_ch_jet1.Eta();
//  double Phi = hadronic_w_ch_jet1.Phi();
//  this->SetJetError(&error_hadronic_w_ch_jet1, Pt, Eta, Phi, "udsc");
//  corr_hadronic_w_ch_jet1 = ts_correction->GetCorrectedJet("udsc",hadronic_w_ch_jet1);
//  fit_hadronic_w_ch_jet1->~TFitParticlePt();
//  new(fit_hadronic_w_ch_jet1) TFitParticlePt("hadronic_w_ch_jet1",
//                                                    "hadronic_w_ch_jet1",
//                                                    &corr_hadronic_w_ch_jet1,
//                                                    &error_hadronic_w_ch_jet1
//                                                   );
//  //cout <<"TKinFitterDriver::SetWCHUpTypeJets : " << endl;
//}
//
//
//void TKinFitterDriver::SetWCHDownTypeJets(TLorentzVector jet_){
//  hadronic_w_ch_jet2=jet_;
//  double Pt = hadronic_w_ch_jet2.Pt();
//  double Eta = hadronic_w_ch_jet2.Eta();
//  double Phi = hadronic_w_ch_jet2.Phi();
//  TString flav =  nbtags>2 ? "b":"udsc";
//  this->SetJetError(&error_hadronic_w_ch_jet2, Pt, Eta, Phi, flav);
//  corr_hadronic_w_ch_jet2 = ts_correction->GetCorrectedJet(flav, hadronic_w_ch_jet2);
//  fit_hadronic_w_ch_jet2->~TFitParticlePt();
//  new(fit_hadronic_w_ch_jet2) TFitParticlePt("hadronic_w_ch_jet2",
//                                                    "hadronic_w_ch_jet2",
//                                                    &corr_hadronic_w_ch_jet2,
//                                                    &error_hadronic_w_ch_jet2
//                                                   );
//  //cout << "TKinFitterDriver::SetWCHDownTypeJets : " << endl;
//}

void TKinFitterDriver::SetHadronicTopBJets(TLorentzVector jet_, double resolution_, std::vector<TLorentzVector> fsr_jet_, std::vector<double> fsr_resolution_){
  hadronic_top_b_jet.clear();
  hadronic_top_b_jet.push_back(jet_);
  //
  double Pt = hadronic_top_b_jet.at(0).Pt();
  error_hadronic_top_b_jet.clear();
  error_hadronic_top_b_jet.emplace_back(1,1);
  error_hadronic_top_b_jet.at(0).Zero();
  error_hadronic_top_b_jet.at(0)(0,0) = resolution_*resolution_*Pt*Pt;
  corr_hadronic_top_b_jet.clear();
  corr_hadronic_top_b_jet.push_back(hadronic_top_b_jet.at(0));
  // push back fsr jets
  for(unsigned i(0); i != fsr_jet_.size(); i++){
    hadronic_top_b_jet.push_back(fsr_jet_.at(i));
    double Pt_fsr = fsr_jet_.at(i).Pt();
    error_hadronic_top_b_jet.emplace_back(1,1);
    error_hadronic_top_b_jet.back().Zero();
    error_hadronic_top_b_jet.back()(0,0) = fsr_resolution_.at(i)*fsr_resolution_.at(i)*Pt_fsr*Pt_fsr;
    corr_hadronic_top_b_jet.push_back(fsr_jet_.at(i));
  }
  // make TAbsFitParticle object
  for(auto* fit_par:fit_hadronic_top_b_jet){
    delete fit_par;
  }
  fit_hadronic_top_b_jet.clear();
  for(unsigned i(0); i != corr_hadronic_top_b_jet.size(); i++){
    fit_hadronic_top_b_jet.push_back(new TFitParticlePt("hadronic_top_b_jet",
                                                         "hadronic_top_b_jet",
                                                         &corr_hadronic_top_b_jet.at(i),
                                                         &error_hadronic_top_b_jet.at(i)
                                                        )
                                     );
 
  }
  //cout <<"TKinFitterDriver::SetHadronicTopBJets : " << endl;
}


void TKinFitterDriver::SetLeptonicTopBJets(TLorentzVector jet_, double resolution_, std::vector<TLorentzVector> fsr_jet_, std::vector<double> fsr_resolution_){
  leptonic_top_b_jet.clear();
  leptonic_top_b_jet.push_back(jet_);
  //
  double Pt = leptonic_top_b_jet.at(0).Pt();
  error_leptonic_top_b_jet.clear();
  error_leptonic_top_b_jet.emplace_back(1,1);
  error_leptonic_top_b_jet.at(0).Zero();
  error_leptonic_top_b_jet.at(0)(0,0) = resolution_*resolution_*Pt*Pt;
  corr_leptonic_top_b_jet.clear();
  corr_leptonic_top_b_jet.push_back(leptonic_top_b_jet.at(0));
  // push back fsr jets
  for(unsigned i(0); i != fsr_jet_.size(); i++){
    leptonic_top_b_jet.push_back(fsr_jet_.at(i));
    double Pt_fsr = fsr_jet_.at(i).Pt();
    error_leptonic_top_b_jet.emplace_back(1,1);
    error_leptonic_top_b_jet.back().Zero();
    error_leptonic_top_b_jet.back()(0,0) = fsr_resolution_.at(i)*fsr_resolution_.at(i)*Pt_fsr*Pt_fsr;
    corr_leptonic_top_b_jet.push_back(fsr_jet_.at(i));
  }
  // make TAbsFitParticle object
  for(auto* fit_par:fit_leptonic_top_b_jet){
    delete fit_par;
  }
  fit_leptonic_top_b_jet.clear();
  for(unsigned i(0); i != corr_leptonic_top_b_jet.size(); i++){
    fit_leptonic_top_b_jet.push_back(new TFitParticlePt("leptonic_top_b_jet",
                                                         "leptonic_top_b_jet",
                                                         &corr_leptonic_top_b_jet.at(i),
                                                         &error_leptonic_top_b_jet.at(i)
                                                        )
                                     );
 
  }


}


void TKinFitterDriver::SetWCHUpTypeJets(TLorentzVector jet_, double resolution_, std::vector<TLorentzVector> fsr_jet_, std::vector<double> fsr_resolution_){
  hadronic_w_ch_jet1.clear();
  hadronic_w_ch_jet1.push_back(jet_);
  //
  double Pt = hadronic_w_ch_jet1.at(0).Pt();
  error_hadronic_w_ch_jet1.clear();
  error_hadronic_w_ch_jet1.emplace_back(1,1);
  error_hadronic_w_ch_jet1.at(0).Zero();
  error_hadronic_w_ch_jet1.at(0)(0,0) = resolution_*resolution_*Pt*Pt;
  corr_hadronic_w_ch_jet1.clear();
  corr_hadronic_w_ch_jet1.push_back(hadronic_w_ch_jet1.at(0));
  // push back fsr jets
  for(unsigned i(0); i != fsr_jet_.size(); i++){
    hadronic_w_ch_jet1.push_back(fsr_jet_.at(i));
    double Pt_fsr = fsr_jet_.at(i).Pt();
    error_hadronic_w_ch_jet1.emplace_back(1,1);
    error_hadronic_w_ch_jet1.back().Zero();
    error_hadronic_w_ch_jet1.back()(0,0) = fsr_resolution_.at(i)*fsr_resolution_.at(i)*Pt_fsr*Pt_fsr;
    corr_hadronic_w_ch_jet1.push_back(fsr_jet_.at(i));
  }
  // make TAbsFitParticle object
  for(auto* fit_par:fit_hadronic_w_ch_jet1){
    delete fit_par;
  }
  fit_hadronic_w_ch_jet1.clear();
  for(unsigned i(0); i != corr_hadronic_w_ch_jet1.size(); i++){
    fit_hadronic_w_ch_jet1.push_back(new TFitParticlePt("hadronic_w_ch_jet1",
                                                         "hadronic_w_ch_jet1",
                                                         &corr_hadronic_w_ch_jet1.at(i),
                                                         &error_hadronic_w_ch_jet1.at(i)
                                                        )
                                     );
 
  }

  //cout <<"TKinFitterDriver::SetWCHUpTypeJets : " << endl;
}


void TKinFitterDriver::SetWCHDownTypeJets(TLorentzVector jet_, double resolution_, std::vector<TLorentzVector> fsr_jet_, std::vector<double> fsr_resolution_){
  hadronic_w_ch_jet2.clear();
  hadronic_w_ch_jet2.push_back(jet_);
  //
  double Pt = hadronic_w_ch_jet2.at(0).Pt();
  error_hadronic_w_ch_jet2.clear();
  error_hadronic_w_ch_jet2.emplace_back(1,1);
  error_hadronic_w_ch_jet2.at(0).Zero();
  error_hadronic_w_ch_jet2.at(0)(0,0) = resolution_*resolution_*Pt*Pt;
  corr_hadronic_w_ch_jet2.clear();
  corr_hadronic_w_ch_jet2.push_back(hadronic_w_ch_jet2.at(0));
  // push back fsr jets
  for(unsigned i(0); i != fsr_jet_.size(); i++){
    hadronic_w_ch_jet2.push_back(fsr_jet_.at(i));
    double Pt_fsr = fsr_jet_.at(i).Pt();
    error_hadronic_w_ch_jet2.emplace_back(1,1);
    error_hadronic_w_ch_jet2.back().Zero();
    error_hadronic_w_ch_jet2.back()(0,0) = fsr_resolution_.at(i)*fsr_resolution_.at(i)*Pt_fsr*Pt_fsr;
    corr_hadronic_w_ch_jet2.push_back(fsr_jet_.at(i));
  }
  // make TAbsFitParticle object

  for(auto* fit_par:fit_hadronic_w_ch_jet2){
    delete fit_par;
  }
  fit_hadronic_w_ch_jet2.clear();
  for(unsigned i(0); i != corr_hadronic_w_ch_jet2.size(); i++){
    fit_hadronic_w_ch_jet2.push_back(new TFitParticlePt("hadronic_w_ch_jet2",
                                                         "hadronic_w_ch_jet2",
                                                         &corr_hadronic_w_ch_jet2.at(i),
                                                         &error_hadronic_w_ch_jet2.at(i)
                                                        )
                                     );
 
  }

  //cout << "TKinFitterDriver::SetWCHDownTypeJets : " << endl;
}

void TKinFitterDriver::SetExtraJets(std::vector<TLorentzVector> extra_jet_, std::vector<double> extra_resolution_){
  corr_extra_jets.clear();
  // push back extra jets
  for(unsigned i(0); i != extra_jet_.size(); i++){
    corr_extra_jets.push_back(extra_jet_.at(i));
    double Pt_extra = extra_jet_.at(i).Pt();
    error_extra_jets.emplace_back(1,1);
    error_extra_jets.back().Zero();
    error_extra_jets.back()(0,0) = extra_resolution_.at(i)*extra_resolution_.at(i)*Pt_extra*Pt_extra;
  }
  // make TAbsFitParticle object
  for(auto* fit_par:fit_extra_jets){
    delete fit_par;
  }
  fit_extra_jets.clear();
  for(unsigned i(0); i != corr_extra_jets.size(); i++){
    fit_extra_jets.push_back(new TFitParticlePt("extra_jets",
                                                         "extra_jets",
                                                         &corr_extra_jets.at(i),
                                                         &error_extra_jets.at(i)
                                                        )
                                     );
 
  }

  //cout << "TKinFitterDriver::SetExtraJets : " << endl;
}

void TKinFitterDriver::SetLepton(TLorentzVector lepton_){
  lepton=lepton_;
  double Pt = lepton.Pt();
  double Eta = lepton.Eta();
  error_lepton(0,0)=TMath::Power(0.02*Pt,2);
  fit_lepton->~TFitParticlePt();
  new(fit_lepton) TFitParticlePt("lepton",
                                        "lepton",
                                        &lepton,
                                        &error_lepton
                                       );
  //cout << "TKinFitterDriver::SetLepton : " << endl;
}


void TKinFitterDriver::SetMET(TLorentzVector met_){
  METv = met_;
}


void TKinFitterDriver::SetMETShift(double met_pt_up, double met_pt_down, double met_phi_up, double met_phi_down){
  
  double met_pt = METv.Pt();
  double met_phi = METv.Phi();
  MET_pt_shift = std::max(fabs(met_pt_up-met_pt), fabs(met_pt-met_pt_down));
  MET_phi_shift = std::max(fabs(met_phi_up-met_phi), fabs(met_phi-met_phi_down));
}


void TKinFitterDriver::SetMETShift(double met_shiftX, double met_shiftY){
  
  double met_px = METv.Px();
  double met_py = METv.Py();
  double met_phi = METv.Phi();

  MET_pt_shift = met_shiftX; //XXX pt->px, phi->py
  MET_phi_shift = met_shiftY; //XXX pt->px, phi->py
  //MET_pt_shift = met_shiftX*TMath::Cos(met_phi) - met_shiftY*TMath::Sin(met_phi);
  //MET_phi_shift = met_shiftX*TMath::Sin(met_phi) + met_shiftY*TMath::Cos(met_phi);
  //
  //cout << "debug" << endl;
  //cout << MET_pt_shift << endl;
  //cout << MET_phi_shift << endl;
}


void TKinFitterDriver::SetNeutrino(TLorentzVector met_, int i){

  double met_px = met_.Px();
  double met_py = met_.Py();
  double pz = neutrino_pz_sol[i];
  neutrino_pxpypz.SetPxPyPzE(met_px, met_py, pz, TMath::Sqrt(met_.E()*met_.E()+pz*pz));
  neutrino_vec3 = neutrino_pxpypz.Vect();

  double MET_error_px2=0., MET_error_py2=0.;
  for(unsigned int i(0); i<jet_pt_resolution_vector.size(); i++){
    double jet_pt_resolution = jet_pt_resolution_vector.at(i);
    double jet_pt  = jet_vector.at(i).Pt();
    double jet_phi = jet_vector.at(i).Phi();
    MET_error_px2 += TMath::Power(jet_pt_resolution*jet_pt*TMath::Cos(jet_phi), 2);
    MET_error_py2 += TMath::Power(jet_pt_resolution*jet_pt*TMath::Sin(jet_phi), 2);
  }

  double lepton_px = lepton.Px();
  double lepton_py = lepton.Py();
  double lepton_pz = lepton.Pz();
  double error_pz2 = (  MET_error_px2 * TMath::Power(met_px+lepton_px, 2)
                     + MET_error_py2 * TMath::Power(met_py+lepton_py, 2)
                    );
  error_pz2 /= std::max(0.0001, TMath::Power(pz + lepton_pz, 2)); // to prevent zero division

  error_neutrino_pxpypz(0,0) = std::max(0.0001, MET_error_px2);  
  error_neutrino_pxpypz(1,1) = std::max(0.0001, MET_error_py2);
  error_neutrino_pxpypz(2,2) = std::max(0.0001, error_pz2);
  fit_neutrino_pxpypz->~TFitParticleMCCart();
  new(fit_neutrino_pxpypz) TFitParticleMCCart("neutrino_pxpypz",
                                          "neutrino_pxpypz",
                                          &neutrino_vec3,
                                          0.,
                                          //&error_neutrino_pxpypz
                                          NULL
                                         );
  
  //fit_neutrino_pz->~TFitParticlePz();
  //new(fit_neutrino_pz) TFitParticlePz("neutrino_pz",
  //  	                      "neutrino_pz",
  //  			      &neutrino_pz,
  //  			      NULL
  //  			      );
  
  //cout << "TKinFitterDriver::SetNeutrino : " << endl;
}


void TKinFitterDriver::SetNeutrinoSmallerPz(TLorentzVector met_){
  this->SetMET(met_);
  this->Sol_Neutrino_Pz();
  if(IsRealNeuPz){
    if(fabs(neutrino_pz_sol[0]) < fabs(neutrino_pz_sol[1])){
      this->SetNeutrino(METv, 0);
    }
    else{
      this->SetNeutrino(METv, 1);
    }
  }
}

void TKinFitterDriver::SetCurrentPermutationJets(bool fsr_recover){

  hadronic_top_b_jet_idx=-1;
  leptonic_top_b_jet_idx=-1;
  w_ch_up_type_jet_idx=-1;
  w_ch_down_type_jet_idx=-1;

  for(UInt_t i=0; i<permutation_vector.size(); i++){
    JET_ASSIGNMENT jet_assignment_idx = permutation_vector.at(i);
    if( jet_assignment_idx == HADRONIC_TOP_B ) hadronic_top_b_jet_idx=i;
    else if( jet_assignment_idx == LEPTONIC_TOP_B ) leptonic_top_b_jet_idx=i;
    else if( jet_assignment_idx == W_CH_UP_TYPE ) w_ch_up_type_jet_idx=i;
    else if( jet_assignment_idx == W_CH_DOWN_TYPE ) w_ch_down_type_jet_idx=i;
  }
  //cout << k << l << m << n << endl;
  // using ts-correction
  //this->SetHadronicTopBJets( jet_vector.at(k) );
  //this->SetLeptonicTopBJets( jet_vector.at(l) );
  //this->SetWCHUpTypeJets( jet_vector.at(m) );
  //this->SetWCHDownTypeJets( jet_vector.at(n) );
  
  // if permutation is NONE, find the closest jet among selected four jets.
  // check if dR<0.8 with the closest jet and softer than the closest jet.
  // push_back to fsr_vector for correspoing four jets.
  //
  std::vector<TLorentzVector> fsr_hadronic_top_b_jet;
  std::vector<TLorentzVector> fsr_leptonic_top_b_jet;
  std::vector<TLorentzVector> fsr_w_ch_up_type_jet;
  std::vector<TLorentzVector> fsr_w_ch_down_type_jet;
  std::vector<TLorentzVector> extra_jets;
  std::vector<double> fsr_hadronic_top_b_jet_resolution;
  std::vector<double> fsr_leptonic_top_b_jet_resolution;
  std::vector<double> fsr_w_ch_up_type_jet_resolution;
  std::vector<double> fsr_w_ch_down_type_jet_resolution;
  std::vector<double> extra_jets_resolution;
  if(fsr_recover){
    for(UInt_t i=0; i<permutation_vector.size(); i++){
      JET_ASSIGNMENT jet_assignment_idx = permutation_vector.at(i);
      double dR_hadronic_top_b_jet, dR_leptonic_top_b_jet, dR_w_ch_up_type_jet, dR_w_ch_down_type_jet;
      double dPt_hadronic_top_b_jet, dPt_leptonic_top_b_jet, dPt_w_ch_up_type_jet, dPt_w_ch_down_type_jet;
      if( jet_assignment_idx != JET_ASSIGNMENT::NONE ){
        continue;
      }
      dR_hadronic_top_b_jet = jet_vector.at(jet_assignment_idx).DeltaR(jet_vector.at(hadronic_top_b_jet_idx));
      dR_leptonic_top_b_jet = jet_vector.at(jet_assignment_idx).DeltaR(jet_vector.at(leptonic_top_b_jet_idx));
      dR_w_ch_up_type_jet   = jet_vector.at(jet_assignment_idx).DeltaR(jet_vector.at(w_ch_up_type_jet_idx));
      dR_w_ch_down_type_jet = jet_vector.at(jet_assignment_idx).DeltaR(jet_vector.at(w_ch_down_type_jet_idx));
      dPt_hadronic_top_b_jet = jet_vector.at(hadronic_top_b_jet_idx).Pt() - jet_vector.at(jet_assignment_idx).Pt();
      dPt_leptonic_top_b_jet = jet_vector.at(leptonic_top_b_jet_idx).Pt() - jet_vector.at(jet_assignment_idx).Pt();
      dPt_w_ch_up_type_jet   = jet_vector.at(w_ch_up_type_jet_idx).Pt()   - jet_vector.at(jet_assignment_idx).Pt();
      dPt_w_ch_down_type_jet = jet_vector.at(w_ch_down_type_jet_idx).Pt() - jet_vector.at(jet_assignment_idx).Pt();
      // find cloest jet among four jets
      double min_dR=9999;
      double dR[4]  = {dR_hadronic_top_b_jet, dR_leptonic_top_b_jet, dR_w_ch_up_type_jet, dR_w_ch_down_type_jet};
      double dPt[4] = {dPt_hadronic_top_b_jet, dPt_leptonic_top_b_jet, dPt_w_ch_up_type_jet, dPt_w_ch_down_type_jet};
      for(int i(0); i<4; i++){
        if(dR[i]<min_dR && dPt[i] >0){
          min_dR = dR[i];
        }
      }
      if(min_dR >= 0.8){
        extra_jets.push_back(jet_vector.at(jet_assignment_idx));
        extra_jets_resolution.push_back(jet_pt_resolution_vector.at(jet_assignment_idx));
      }
      else if(min_dR == dR_hadronic_top_b_jet){
        fsr_hadronic_top_b_jet.push_back(jet_vector.at(jet_assignment_idx));
        fsr_hadronic_top_b_jet_resolution.push_back(jet_pt_resolution_vector.at(jet_assignment_idx));
      }
      else if(min_dR == dR_leptonic_top_b_jet){
        fsr_leptonic_top_b_jet.push_back(jet_vector.at(jet_assignment_idx));
        fsr_leptonic_top_b_jet_resolution.push_back(jet_pt_resolution_vector.at(jet_assignment_idx));
      }
      else if(min_dR == dR_w_ch_up_type_jet){
        fsr_w_ch_up_type_jet.push_back(jet_vector.at(jet_assignment_idx));
        fsr_w_ch_up_type_jet_resolution.push_back(jet_pt_resolution_vector.at(jet_assignment_idx));
      }
      else if(min_dR == dR_w_ch_down_type_jet){
        fsr_w_ch_down_type_jet.push_back(jet_vector.at(jet_assignment_idx));
        fsr_w_ch_down_type_jet_resolution.push_back(jet_pt_resolution_vector.at(jet_assignment_idx));
      }

    }
  }
  else{
    for(UInt_t i=0; i<permutation_vector.size(); i++){
      JET_ASSIGNMENT jet_assignment_idx = permutation_vector.at(i);
      if( jet_assignment_idx != JET_ASSIGNMENT::NONE ){
        continue;
      }
      extra_jets.push_back(jet_vector.at(jet_assignment_idx));
      extra_jets_resolution.push_back(jet_pt_resolution_vector.at(jet_assignment_idx));
    }
  }

  // using jetMET POG jer
  this->SetHadronicTopBJets( jet_vector.at(hadronic_top_b_jet_idx), jet_pt_resolution_vector.at(hadronic_top_b_jet_idx), fsr_hadronic_top_b_jet, fsr_hadronic_top_b_jet_resolution);
  this->SetLeptonicTopBJets( jet_vector.at(leptonic_top_b_jet_idx), jet_pt_resolution_vector.at(leptonic_top_b_jet_idx),  fsr_leptonic_top_b_jet, fsr_leptonic_top_b_jet_resolution);
  this->SetWCHUpTypeJets( jet_vector.at(w_ch_up_type_jet_idx), jet_pt_resolution_vector.at(w_ch_up_type_jet_idx),  fsr_w_ch_up_type_jet, fsr_w_ch_up_type_jet_resolution);
  this->SetWCHDownTypeJets( jet_vector.at(w_ch_down_type_jet_idx), jet_pt_resolution_vector.at(w_ch_down_type_jet_idx),  fsr_w_ch_down_type_jet, fsr_w_ch_down_type_jet_resolution);
  this->SetExtraJets( extra_jets, extra_jets_resolution);

}


bool TKinFitterDriver::Check_BJet_Assignment(){

  int nbtags_in_four_jets=0;
  int w_ch_up_type_jet_idx=-1;
  int w_ch_down_type_jet_idx=-1;
  for(UInt_t i=0; i<permutation_vector.size(); i++){
    JET_ASSIGNMENT jet_assignment_idx = permutation_vector.at(i);
    bool IsBTagged = btag_vector.at(i);
    if(nbtags>=2){
      if( jet_assignment_idx == HADRONIC_TOP_B && IsBTagged ) nbtags_in_four_jets+=1;
      else if( jet_assignment_idx == LEPTONIC_TOP_B && IsBTagged ) nbtags_in_four_jets+=1;

      if( jet_assignment_idx == W_CH_UP_TYPE)   w_ch_up_type_jet_idx   = i;
      else if( jet_assignment_idx == W_CH_DOWN_TYPE) w_ch_down_type_jet_idx = i;
    }


  }

  bool true_bjet_assignment=false;
  if(nbtags>=2 && nbtags_in_four_jets==2){
    if(btag_csv_vector.at(w_ch_up_type_jet_idx) <= btag_csv_vector.at(w_ch_down_type_jet_idx)){
      true_bjet_assignment=true;
    }
    else{
      //pass
    }
  }

  //cout << "TKinFitterDriver::Check_BJet_Assignment : " << endl; 
  return true_bjet_assignment;
}

TLorentzVector VectorSum(std::vector<TLorentzVector> vector_){
  TLorentzVector out_vector(0,0,0,0);
  for(auto &x : vector_){
    out_vector = out_vector + x;
  }
  return out_vector;
}


bool TKinFitterDriver::Kinematic_Cut(){
  TLorentzVector hadronic_top_b_jet_ = VectorSum(hadronic_top_b_jet);
  TLorentzVector leptonic_top_b_jet_ = VectorSum(leptonic_top_b_jet);
  TLorentzVector hadronic_w_ch_jet1_ = VectorSum(hadronic_w_ch_jet1);
  TLorentzVector hadronic_w_ch_jet2_ = VectorSum(hadronic_w_ch_jet2);
  TLorentzVector hadronic_top = hadronic_top_b_jet_ + hadronic_w_ch_jet1_ + hadronic_w_ch_jet2_;
  //TLorentzVector leptonic_top = leptonic_top_b_jet + lepton + neutrino_pxpy + neutrino_pz;
  TLorentzVector leptonic_top = leptonic_top_b_jet_ + lepton + neutrino_pxpypz;
  double hadronic_top_mass = hadronic_top.M();
  double leptonic_top_mass = leptonic_top.M();

         // jet pt cut. If 3b>=, one of b tagged jet in hadronic side allowed to be below 30GeV
  return (hadronic_w_ch_jet1.at(0).Pt() > 30. &&
          (
           (nbtags==2 &&
            (hadronic_w_ch_jet2.at(0).Pt() > 30. && hadronic_top_b_jet.at(0).Pt() > 30.)
           ) ||
           (nbtags>=3 &&
            ((hadronic_w_ch_jet2.at(0).Pt() > 20. && hadronic_top_b_jet.at(0).Pt() > 30.)||
            (hadronic_w_ch_jet2.at(0).Pt() > 30. && hadronic_top_b_jet.at(0).Pt() > 20.))
           )
          ) &&
          leptonic_top_b_jet.at(0).Pt() > 30.
         ) &&
         // tighter M_top cut to compansate increasing combinatorics
         ((njets ==4 && hadronic_top_mass > 100 && hadronic_top_mass < 240) ||
          (njets ==5 && hadronic_top_mass > 120 && hadronic_top_mass < 220) ||
          (njets >=6 && hadronic_top_mass > 140 && hadronic_top_mass < 200)) &&
         //(leptonic_top_mass > 100 && leptonic_top_mass < 240) &&
         (leptonic_top_b_jet_+lepton).M() < 150 &&   //Mbl
         (fabs(hadronic_top.DeltaPhi(leptonic_top)) > 1.5);
}

bool TKinFitterDriver::Quality_Cut(){
  return fabs(this->CalcEachChi2(fit_hadronic_top_b_jet))<9 && // 9 for 3 sigma
         fabs(this->CalcEachChi2(fit_leptonic_top_b_jet))<9 &&
         fabs(this->CalcEachChi2(fit_hadronic_w_ch_jet1))<9 &&
         fabs(this->CalcEachChi2(fit_hadronic_w_ch_jet2))<9;
}

void TKinFitterDriver::SetConstraint(){
  //TODO: will update to be able to set top-mass
  // reset constrain
  constrain_hadronic_top_M->Clear();
  new(constrain_hadronic_top_M) TFitConstraintM("hadronic_top_mass_constraint", "hadronic_top_mass_constraint", 0, 0, 172.5);
  for(auto* fit_par : fit_hadronic_top_b_jet){
    constrain_hadronic_top_M->addParticle1(fit_par);
  }
  for(auto* fit_par : fit_hadronic_w_ch_jet1){
    constrain_hadronic_top_M->addParticle1(fit_par);
  }
  for(auto* fit_par : fit_hadronic_w_ch_jet2){
    constrain_hadronic_top_M->addParticle1(fit_par);
  }
  //constrain_hadronic_top_MGaus->Clear();
  //constrain_hadronic_top_MGaus->addParticles1(fit_hadronic_top_b_jet, fit_hadronic_w_ch_jet1, fit_hadronic_w_ch_jet2);
  constrain_leptonic_top_M->Clear();
  new(constrain_leptonic_top_M) TFitConstraintM("leptonic_top_mass_constraint", "leptonic_top_mass_constraint", 0, 0, 172.5);
  for(auto* fit_par : fit_leptonic_top_b_jet){
    constrain_leptonic_top_M->addParticle1(fit_par);
  }
  constrain_leptonic_top_M->addParticle1(fit_lepton);
  constrain_leptonic_top_M->addParticle1(fit_neutrino_pxpypz);
  //constrain_leptonic_top_MGaus->Clear();
  //constrain_leptonic_top_MGaus->addParticles1(fit_leptonic_top_b_jet, fit_lepton, fit_neutrino_pxpy, fit_neutrino_pz);
  constrain_leptonic_W_M->Clear();
  new(constrain_leptonic_W_M) TFitConstraintM("leptonic_w_mass_constraint", "leptonic_w_mass_constraint", 0, 0, 80.4);
  constrain_leptonic_W_M->addParticles1(fit_neutrino_pxpypz, fit_lepton); // lepton is included in fit_neutrino_pz
  //constrain_leptonic_W_MGaus->Clear();
  //constrain_leptonic_W_MGaus->addParticles1(fit_lepton, fit_neutrino_pxpy, fit_neutrino_pz);
  

  constrain_pX->Clear();
  constrain_pY->Clear();
  new(constrain_pX) TFitConstraintEp("pX","pX",TFitConstraintEp::component::pX,0.);
  new(constrain_pY) TFitConstraintEp("pY","pY",TFitConstraintEp::component::pY,0.);
  for(auto* fit_par : fit_hadronic_top_b_jet){
    constrain_pX->addParticle(fit_par);
    constrain_pY->addParticle(fit_par);
  }
  for(auto* fit_par : fit_leptonic_top_b_jet){
    constrain_pX->addParticle(fit_par);
    constrain_pY->addParticle(fit_par);
  }
  for(auto* fit_par : fit_hadronic_w_ch_jet1){
    constrain_pX->addParticle(fit_par);
    constrain_pY->addParticle(fit_par);
  }
  for(auto* fit_par : fit_hadronic_w_ch_jet2){
    constrain_pX->addParticle(fit_par);
    constrain_pY->addParticle(fit_par);
  }
  for(auto* fit_par : fit_extra_jets){
    constrain_pX->addParticle(fit_par);
    constrain_pY->addParticle(fit_par);
  }
  for(auto* fit_par : std::vector<TAbsFitParticle*>({fit_lepton, fit_neutrino_pxpypz})){
    constrain_pX->addParticle(fit_par);
    constrain_pY->addParticle(fit_par);
  }
  //
  double pX = constrain_pX->getInitValue();
  double pY = constrain_pY->getInitValue();
  constrain_pX->setConstraint(pX);
  constrain_pY->setConstraint(pY);
}


void TKinFitterDriver::SetFitter(){
  fitter->reset();
  //add MeasParticles to vary Et,Eta,Phi
  for(auto* fit_par : fit_hadronic_top_b_jet){
    fitter->addMeasParticle( fit_par );
  }
  for(auto* fit_par : fit_leptonic_top_b_jet){
    fitter->addMeasParticle( fit_par );
  }
  for(auto* fit_par : fit_hadronic_w_ch_jet1){
    fitter->addMeasParticle( fit_par );
  }
  for(auto* fit_par : fit_hadronic_w_ch_jet2){
    fitter->addMeasParticle( fit_par );
  }
  for(auto* fit_par : fit_extra_jets){
    fitter->addMeasParticle( fit_par );
  }
  //add UnmeasParticles not to vary Et,Eta,Phi
  // Also, Px, Py should be constrained
  fitter->addMeasParticle( fit_lepton );
  fitter->addUnmeasParticle( fit_neutrino_pxpypz );
  //add Constraint
  fitter->addConstraint( constrain_hadronic_top_M );
  //fitter->addConstraint( constrain_hadronic_top_MGaus );
  fitter->addConstraint( constrain_leptonic_top_M );
  //fitter->addConstraint( constrain_leptonic_top_MGaus );
  fitter->addConstraint( constrain_leptonic_W_M );
  //fitter->addConstraint( constrain_leptonic_W_MGaus );
  fitter->addConstraint( constrain_pX );
  fitter->addConstraint( constrain_pY );
  //Set convergence criteria
  fitter->setMaxNbIter( 50 ); //50 is default
  fitter->setMaxDeltaS( 1e-2 );
  fitter->setMaxF( 1e-1 ); //1e-1 is default
  fitter->setVerbosity(1);
  //cout << "TKinFitterDriver::SetFitter : " << endl;
}


void TKinFitterDriver::Fit(){
  this->SetConstraint();
  this->SetFitter();
  this->SaveResults();
}


void TKinFitterDriver::SaveResults(){

  fit_result.status=-1; // -1 means fit not performed
  fit_result.status = fitter->fit();
  //cout << "TKinFitterDriver::Fit :  " << fit_result.status << endl;
  // save kinematic variable before fit
  TLorentzVector hadronic_top_b_jet_ = VectorSum(hadronic_top_b_jet);
  TLorentzVector leptonic_top_b_jet_ = VectorSum(leptonic_top_b_jet);
  TLorentzVector hadronic_w_ch_jet1_ = VectorSum(hadronic_w_ch_jet1);
  TLorentzVector hadronic_w_ch_jet2_ = VectorSum(hadronic_w_ch_jet2);
  TLorentzVector corr_hadronic_top_b_jet_ = VectorSum(corr_hadronic_top_b_jet);
  TLorentzVector corr_hadronic_w_ch_jet1_ = VectorSum(corr_hadronic_w_ch_jet1);
  TLorentzVector corr_hadronic_w_ch_jet2_ = VectorSum(corr_hadronic_w_ch_jet2);
  TLorentzVector hadronic_top = hadronic_top_b_jet_ + hadronic_w_ch_jet1_ + hadronic_w_ch_jet2_;
  TLorentzVector leptonic_W = neutrino_pxpypz + lepton;
  TLorentzVector leptonic_top = leptonic_top_b_jet_ + leptonic_W;
  fit_result.hadronic_top_M = hadronic_top.M();
  fit_result.hadronic_top_pt = hadronic_top.Pt();
  fit_result.leptonic_top_M = leptonic_top.M();
  fit_result.leptonic_top_pt = leptonic_top.Pt();
  fit_result.leptonic_W_M = leptonic_W.M();
  fit_result.IsRealNeuPz = IsRealNeuPz;

  fit_result.hadronic_top_b_pt = hadronic_top_b_jet_.Pt();
  fit_result.leptonic_top_b_pt = leptonic_top_b_jet_.Pt();
  fit_result.w_ch_up_type_pt = hadronic_w_ch_jet1_.Pt();
  fit_result.w_ch_down_type_pt = hadronic_w_ch_jet2_.Pt();
  
  fit_result.hadronic_top_b_jet_idx = hadronic_top_b_jet_idx;
  fit_result.leptonic_top_b_jet_idx = leptonic_top_b_jet_idx;
  fit_result.w_ch_up_type_jet_idx = w_ch_up_type_jet_idx;
  fit_result.w_ch_down_type_jet_idx = w_ch_down_type_jet_idx;

  fit_result.hadronic_top_b_jet_pull = (*fit_hadronic_top_b_jet.at(0)->getPull())(0,0);
  fit_result.leptonic_top_b_jet_pull = (*fit_leptonic_top_b_jet.at(0)->getPull())(0,0);
  fit_result.w_ch_up_type_jet_pull = (*fit_hadronic_w_ch_jet1.at(0)->getPull())(0,0);
  fit_result.w_ch_down_type_jet_pull = (*fit_hadronic_w_ch_jet2.at(0)->getPull())(0,0);
                                      
  //
  ///////
  int down_type_jet_b_tagged = 0;
  for(UInt_t i=0; i<permutation_vector.size(); i++){
    JET_ASSIGNMENT jet_assignment_idx = permutation_vector.at(i);
    bool IsBTagged = btag_vector.at(i);
    if( jet_assignment_idx == W_CH_DOWN_TYPE){
      if(IsBTagged){
        down_type_jet_b_tagged=1;
      }
      else{
        //pass
      }
      break;
    }
  }
  fit_result.down_type_jet_b_tagged = down_type_jet_b_tagged;
  ///////
  //
  fit_result.chi2 = 9999;
  //if(fit_result.status!=-10){ // -10 means singular matrix
    // save S and F
    fit_result.currS = fitter->getS();
    fit_result.deltaS = fitter->getDeltaS();
    fit_result.hadronic_top_mass_F = constrain_hadronic_top_M->getCurrentValue();
    //fit_result.hadronic_top_mass_F = constrain_hadronic_top_MGaus->getCurrentValue();
    fit_result.leptonic_top_mass_F = constrain_leptonic_top_M->getCurrentValue();
    //fit_result.leptonic_top_mass_F = constrain_leptonic_top_MGaus->getCurrentValue();
    fit_result.leptonic_w_mass_F = constrain_leptonic_W_M->getCurrentValue();
    //fit_result.leptonic_w_mass_F = constrain_leptonic_W_MGaus->getCurrentValue();
    // re-calculate chi2,
    //chi2 term comes from constraint is not accurate
    fit_result.chi2 = this->CalcChi2("all");
    fit_result.chi2_lep = this->CalcChi2("lep");
    fit_result.chi2_had = this->CalcChi2("had");
    fit_result.lambda = fitter->getLambda();

    fit_result.init_pX = constrain_pX->getInitValue();
    fit_result.init_pY = constrain_pY->getInitValue();
    fit_result.fitted_pX = constrain_pX->getCurrentValue();
    fit_result.fitted_pY = constrain_pY->getCurrentValue();

    // calc. dijet mass
    TLorentzVector fitted_jet1_(0,0,0,0);
    TLorentzVector fitted_jet2_(0,0,0,0);
    TLorentzVector fitted_jet3_(0,0,0,0);
    for(auto* fit_par : fit_hadronic_w_ch_jet1){
       const TLorentzVector *tmp_jet_const = fit_par->getCurr4Vec();
       TLorentzVector tmp_jet(tmp_jet_const->Px(), tmp_jet_const->Py(), tmp_jet_const->Pz(), tmp_jet_const->E());
       fitted_jet1_ = fitted_jet1_ + tmp_jet;
    }
    for(auto* fit_par : fit_hadronic_w_ch_jet2){
       const TLorentzVector *tmp_jet_const = fit_par->getCurr4Vec();
       TLorentzVector tmp_jet(tmp_jet_const->Px(), tmp_jet_const->Py(), tmp_jet_const->Pz(), tmp_jet_const->E());
       fitted_jet2_ = fitted_jet2_ + tmp_jet;
    }
    for(auto* fit_par : fit_hadronic_top_b_jet){
       const TLorentzVector *tmp_jet_const = fit_par->getCurr4Vec();
       TLorentzVector tmp_jet(tmp_jet_const->Px(), tmp_jet_const->Py(), tmp_jet_const->Pz(), tmp_jet_const->E());
       fitted_jet3_ = fitted_jet3_ + tmp_jet;
    }
    const TLorentzVector *fitted_jet1 = &fitted_jet1_;
    const TLorentzVector *fitted_jet2 = &fitted_jet2_;
    const TLorentzVector *fitted_jet3 = &fitted_jet3_;
    const TLorentzVector fitted_dijet = (*fitted_jet1) + (*fitted_jet2);
    const TLorentzVector fitted_dijet_high = fitted_jet3->Pt()>fitted_jet2->Pt() ? (*fitted_jet1) + (*fitted_jet3):fitted_dijet;
    const TLorentzVector fitted_dijet_new1 = fitted_jet3->Pt()>fitted_jet2->Pt()+30 ? (*fitted_jet1) + (*fitted_jet3):fitted_dijet;
    fit_result.fitted_dijet_M = fitted_dijet.M(); // save dijet mass
    fit_result.fitted_dijet_M_high = fitted_dijet_high.M(); // save dijet mass
    fit_result.fitted_dijet_M_new1 = fitted_dijet_new1.M(); // save dijet mass
    //fit_result.fitted_dijet_M_new2 = this->ComparingInHadTopRestFrame(fitted_jet1,fitted_jet2,fitted_jet3);
    fit_result.fitted_dijet_M_new2 = 1.;
    TLorentzVector initial_dijet = hadronic_w_ch_jet1_ + hadronic_w_ch_jet2_;
    TLorentzVector initial_dijet_high = fitted_jet3->Pt()>fitted_jet2->Pt() ? hadronic_w_ch_jet1_ + hadronic_top_b_jet_:initial_dijet;
    fit_result.initial_dijet_M = initial_dijet.M(); // save dijet mass
    fit_result.initial_dijet_M_high = initial_dijet_high.M(); // save dijet mass
    TLorentzVector corrected_dijet = corr_hadronic_w_ch_jet1_ + corr_hadronic_w_ch_jet2_;
    TLorentzVector corrected_dijet_high = fitted_jet3->Pt()>fitted_jet2->Pt() ? corr_hadronic_w_ch_jet1_ + corr_hadronic_top_b_jet_:corrected_dijet;
    fit_result.corrected_dijet_M = corrected_dijet.M(); // save dijet mass
    fit_result.corrected_dijet_M_high = corrected_dijet_high.M(); // save dijet mass
  //}
  //cout << "TKinFitterDriver::Fit : " << endl;

}

double TKinFitterDriver::ComparingInHadTopRestFrame(const TLorentzVector *jet1,const TLorentzVector *jet2, const TLorentzVector *had_top_b_jet){
  const TLorentzVector fitted_had_top = *jet1 + *jet2 + *had_top_b_jet;
  const TLorentzVector w_ch_cand1 = *jet1 + *jet2;
  const TLorentzVector w_ch_cand2 = *jet1 + *had_top_b_jet;

  TVector3 had_top_boost_vector = fitted_had_top.BoostVector();
  TLorentzVector w_ch_cand1_top_rest  = TLorentzVector(w_ch_cand1.Px(), w_ch_cand1.Py(), w_ch_cand1.Pz(), w_ch_cand1.E());
  TLorentzVector top_b_cand1_top_rest = TLorentzVector(had_top_b_jet->Px(), had_top_b_jet->Py(), had_top_b_jet->Pz(), had_top_b_jet->E());
  TLorentzVector w_ch_cand2_top_rest  = TLorentzVector(w_ch_cand2.Px(), w_ch_cand2.Py(), w_ch_cand2.Pz(), w_ch_cand2.E());
  TLorentzVector top_b_cand2_top_rest = TLorentzVector(jet2->Px(), jet2->Py(), jet2->Pz(), jet2->E());

  w_ch_cand1_top_rest.Boost(-had_top_boost_vector);
  top_b_cand1_top_rest.Boost(-had_top_boost_vector);
  w_ch_cand2_top_rest.Boost(-had_top_boost_vector);
  top_b_cand2_top_rest.Boost(-had_top_boost_vector);

  double out_mass;
  if(fabs(w_ch_cand1_top_rest.DeltaPhi(top_b_cand1_top_rest)) > fabs(w_ch_cand2_top_rest.DeltaPhi(top_b_cand2_top_rest))){
    out_mass = w_ch_cand1.M();
  }
  else{
    out_mass = w_ch_cand2.M();
  }
  return out_mass;
}

double TKinFitterDriver::CalcChi2(TString option){
  double chi2=0;
  double NDF=0;
  // jets
  if(option == "had" || option == "all"){
  for(auto* fit_par : fit_hadronic_top_b_jet){
    chi2 += this->CalcEachChi2(fit_par);
  }
  for(auto* fit_par : fit_leptonic_top_b_jet){
    chi2 += this->CalcEachChi2(fit_par);
  }
  for(auto* fit_par : fit_hadronic_w_ch_jet1){
    chi2 += this->CalcEachChi2(fit_par);
  }
  for(auto* fit_par : fit_hadronic_w_ch_jet2){
    chi2 += this->CalcEachChi2(fit_par);
  }
  NDF += fit_hadronic_top_b_jet.size() + fit_leptonic_top_b_jet.size() + fit_hadronic_w_ch_jet1.size() + fit_hadronic_w_ch_jet2.size();
  }
  if(option == "lep" || option == "all"){
  //lepton
  chi2 += this->CalcEachChi2(fit_lepton);
  //chi2 += this->CalcEachChi2(fit_neutrino_pxpypz);
  for(auto* fit_par : fit_extra_jets){
    chi2 += this->CalcEachChi2(fit_par);
  }
  NDF += 1 + fit_extra_jets.size() - 2; // lepton + extra jets - constraint
  }
  // mass constraints
  chi2 += this->CalcEachChi2(constrain_leptonic_W_M, 2.085);
  //chi2 += this->CalcEachChi2(constrain_leptonic_W_MGaus);
  //chi2 += this->CalcEachChi2(constrain_hadronic_top_MGaus);
  chi2 += this->CalcEachChi2(constrain_hadronic_top_M, 1.5);
  //chi2 += this->CalcEachChi2(constrain_leptonic_top_MGaus);
  chi2 += this->CalcEachChi2(constrain_leptonic_top_M, 1.5);
  return chi2/NDF;
}

double TKinFitterDriver::CalcEachChi2(TAbsFitParticle* ptr){

  const TMatrixD* iniPar = ptr->getParIni();
  const TMatrixD* currPar = ptr->getParCurr();
  const TMatrixD* covMatrix = ptr->getCovMatrix();
  double S = 0.;

  for(int i(0); i<iniPar->GetNcols(); i++){
    double deltaY = (*iniPar)(i,i) - (*currPar)(i,i);
    S += deltaY*deltaY/(*covMatrix)(i,i);
  }
  return S;
}

double TKinFitterDriver::CalcPull(TAbsFitParticle* ptr){
  //(*fit_hadronic_top_b_jet->getPull())(0,0);
  const TMatrixD* covMatrix = ptr->getPull();
  double S = 0.;

  //ptr->Print();
  // 4 parm for jets, 1 parm for lep, 3 parm for neu
  // 8 params total, 3 mass constraint
  for(int i(0); i< min(1,covMatrix->GetNrows()); i++){ // min() is used not to include neu pz fit err. 
    double pull = (*covMatrix)(i,0);
    S += pull*pull;
    //cout << "i col: " << i << "\t\tS: " << S << endl;
  }
  return S;
}


double TKinFitterDriver::CalcEachChi2(TFitConstraintM* ptr, double width){
  double S = 0.;
  double deltaY = ptr->getCurrentValue();
  S = (deltaY*deltaY)/(width*width);
  return S;
}


double TKinFitterDriver::CalcEachChi2(TFitConstraintMGaus* ptr){
  return ptr->getChi2();
}

double TKinFitterDriver::CalcEachChi2(std::vector<TFitParticlePt*> ptrs){
  double out=0;
  for(auto ptr:ptrs)
    out += this->CalcEachChi2(ptr);
  out /= ptrs.size();
  return out;
}

void TKinFitterDriver::FitCurrentPermutation(){
  fit_result_vector.clear();
  this->Fit();
  fit_result_vector.push_back(fit_result);
}


void TKinFitterDriver::FindBestChi2Fit(bool UseLeading4Jets, bool IsHighMassFitter){
  fit_result_vector.clear();
  fit_result_vector.shrink_to_fit();
  // status -1 : fit not performed
  fit_result.status=-1;


  if(njets<4 || nbtags<2){
    return;
  }
  //cout << ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" << endl;
  //cout << "start jet permutation" << endl;
  //cout << ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" << endl;
  // for debug
  double best_chi2=99999999;
  unsigned nFSR1, nFSR2, nFSR3, nFSR4;
  do{
      if(this->Check_BJet_Assignment() == false) continue;
      // loop to try no fsr recover and fsr recover
      //for(int i_fsr(0); i_fsr<2; i_fsr++){
      for(int i_fsr(0); i_fsr<1; i_fsr++){
        if(i_fsr==0){
          this->SetCurrentPermutationJets(false);
        }
        else if(i_fsr==1){
          this->SetCurrentPermutationJets(true);
        }
        //nu pz
        this->Sol_Neutrino_Pz();
        for(int i_pz(0); i_pz<2; i_pz++) { // neu. pz loop
  	      if(IsRealNeuPz){
  	        this->SetNeutrino(METv, i_pz);
  	      }
  	      else{
  	        this->SetNeutrino(METv, 0);
            i_pz++; // to break the loop after the first iteration
  	      }

          if(this->Kinematic_Cut() == false) continue;
          this->Fit();
          if(this->Quality_Cut() == false) continue;
          //  cout << "result hadronic top mass :" << fit_result.hadronic_top_M << endl;
          //  cout << "result hadronic top pt :" << fit_result.hadronic_top_pt << endl;
          //  cout << "result dijet mass        :" << fit_result.fitted_dijet_M << endl;
          //  cout << "result chi2_had          :" << fit_result.chi2_had << endl;
          //  cout << "result chi2_lep          :" << fit_result.chi2_lep << endl;
          //  cout << "result chi2              :" << fit_result.chi2 << endl;
  	      fit_result_vector.push_back(fit_result);
          if(best_chi2 > fit_result.chi2){
            best_chi2 = fit_result.chi2;
            nFSR1     = hadronic_top_b_jet.size();
            nFSR2     = leptonic_top_b_jet.size();
            nFSR3     = hadronic_w_ch_jet1.size();
            nFSR4     = hadronic_w_ch_jet2.size();
          }
        }
      }
    }while(this->NextPermutation(UseLeading4Jets));
  //if(best_chi2 < 99999999){
  //cout << ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" << endl;
  //cout << best_chi2 << endl;
  //cout << nFSR1     << endl;
  //cout << nFSR2     << endl;
  //cout << nFSR3     << endl;
  //cout << nFSR4     << endl;
  //cout << ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" << endl;
  //}
  std::sort(fit_result_vector.begin(), fit_result_vector.end(), Chi2Comparing);
  //std::sort(fit_result_vector.begin(), fit_result_vector.end(), HadTopMComparing);
  //std::sort(fit_result_vector.begin(), fit_result_vector.end(), HadTopPtComparing);
  //std::sort(fit_result_vector.begin(), fit_result_vector.end(), LepTopPtComparing);
  //std::sort(fit_result_vector.begin(), fit_result_vector.end(), TopPtComparing);

  if(IsHighMassFitter){
    std::sort(fit_result_vector.begin(), fit_result_vector.end(), HighMassFitter);
  }

}


int TKinFitterDriver::GetStatus(){
  return fit_result.status;
}


double TKinFitterDriver::GetChi2(){
  return fit_result.chi2;
}


double TKinFitterDriver::GetFittedDijetMass(){
  return fit_result.fitted_dijet_M;
}


double TKinFitterDriver::GetInitialDijetMass(){
  return fit_result.initial_dijet_M;
}


double TKinFitterDriver::GetCorrectedDijetMass(){
  return fit_result.corrected_dijet_M;
}


int TKinFitterDriver::GetBestStatus(){
  int out=-1;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).status;
  }
  return out;
}


double TKinFitterDriver::GetBestChi2(){
  double out=-1;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).chi2;
  }
  return out==9999 ? -1. : out;
}

double TKinFitterDriver::GetBestLambda(){
  double out=-1;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).lambda;
  }
  return out==9999 ? -1. : out;
}

int TKinFitterDriver::GetBestDownTypeJetBTagged(){
  int out=-1;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).down_type_jet_b_tagged;
  }
  return out;
}

double TKinFitterDriver::GetBestFittedDijetMass(){
  double out=-1;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).fitted_dijet_M;
  }
  return out;
}


double TKinFitterDriver::GetBestFittedDijetMass_high(){
  double out=-1;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).fitted_dijet_M_high;
  }
  return out;
}


double TKinFitterDriver::GetBestInitialDijetMass(){
  double out=-1;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).initial_dijet_M;
  }
  return out;
}


double TKinFitterDriver::GetBestInitialDijetMass_high(){
  double out=-1;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).initial_dijet_M_high;
  }
  return out;
}


double TKinFitterDriver::GetBestCorrectedDijetMass(){
  double out=-1;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).corrected_dijet_M;
  }
  return out;
}


double TKinFitterDriver::GetBestCorrectedDijetMass_high(){
  double out=-1;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).corrected_dijet_M_high;
  }
  return out;
}


double TKinFitterDriver::GetBestHadronicTopMass(){
  double out=-100;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).hadronic_top_M;
  }
  return out;
}

double TKinFitterDriver::GetBestHadronicTopPt(){
  double out=-100;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).hadronic_top_pt;
  }
  return out;
}

double TKinFitterDriver::GetBestLeptonicTopMass(){
  double out=-100;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).leptonic_top_M;
  }
  return out;
}


double TKinFitterDriver::GetBestLeptonicWMass(){
  double out=-100;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).leptonic_W_M;
  }
  return out;
}


bool TKinFitterDriver::GetBestIsRealNeuPz(){
  bool out=false;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).IsRealNeuPz;
  }
  return out;
}


double TKinFitterDriver::GetBestHadronicTopMassF(){
  double out=-100;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).hadronic_top_mass_F;
  }
  return out;
}

int TKinFitterDriver::GetBestHadronicTopBJetIdx(){
  int out=-1;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).hadronic_top_b_jet_idx;
  }
  return out;
}

int TKinFitterDriver::GetBestLeptonicTopBJetIdx(){
  double out=-1;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).leptonic_top_b_jet_idx;
  }
  return out;
}

int TKinFitterDriver::GetBestHadronicWCHUpTypeJetIdx(){
  double out=-1;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).w_ch_up_type_jet_idx;
  }
  return out;
}

int TKinFitterDriver::GetBestHadronicWCHDownTypeJetIdx(){
  int out=-1;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).w_ch_down_type_jet_idx;
  }
  return out;
}

double TKinFitterDriver::GetBestHadronicTopBJetPull(){
  double out=-1;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).hadronic_top_b_jet_pull;
  }
  return out;
}
double TKinFitterDriver::GetBestLeptonicTopBJetPull(){
  double out=-1;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).leptonic_top_b_jet_pull;
  }
  return out;
}



double TKinFitterDriver::GetBestHadronicWCHUptypeJetIdxPull(){
  double out=-1;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).w_ch_up_type_jet_pull;
  }
  return out;
}
double TKinFitterDriver::GetBestHadronicWCHDowntypeJetIdxPull(){
  double out=-1;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).w_ch_down_type_jet_pull;
  }
  return out;
}





double TKinFitterDriver::GetBestLeptonicTopMassF(){
  double out=-100;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).leptonic_top_mass_F;
  }
  return out;
}


double TKinFitterDriver::GetBestLeptonicWMassF(){
  double out=-100;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).leptonic_w_mass_F;
  }
  return out;
}


double TKinFitterDriver::GetBestDeltaS(){
  double out=-100;
  if(fit_result_vector.size()>0){
    out =fit_result_vector.at(0).deltaS;
  }
  return out;
}


std::vector<double> TKinFitterDriver::GetHadronicTopMassVector(bool IsConverge){
  std::vector<double> out_vector;
  for(auto &x : fit_result_vector){
    if(IsConverge==true && x.status==0){
      out_vector.push_back(x.hadronic_top_M);
    }
    else if(IsConverge==false && x.status!=0){
      out_vector.push_back(x.hadronic_top_M);
    }
  }
  return out_vector;
}


std::vector<double> TKinFitterDriver::GetHadronicTopBPtVector(bool IsConverge){
  std::vector<double> out_vector;
  for(auto &x : fit_result_vector){
    if(IsConverge==true && x.status==0){
      out_vector.push_back(x.hadronic_top_b_pt);
    }
    else if(IsConverge==false && x.status!=0){
      out_vector.push_back(x.hadronic_top_b_pt);
    }
  }
  return out_vector;
}


std::vector<double> TKinFitterDriver::GetLeptonicTopBPtVector(bool IsConverge){
  std::vector<double> out_vector;
  for(auto &x : fit_result_vector){
    if(IsConverge==true && x.status==0){
      out_vector.push_back(x.leptonic_top_b_pt);
    }
    else if(IsConverge==false && x.status!=0){
      out_vector.push_back(x.leptonic_top_b_pt);
    }
  }
  return out_vector;
}


std::vector<double> TKinFitterDriver::GetWCHDownTypePtVector(bool IsConverge){
  std::vector<double> out_vector;
  for(auto &x : fit_result_vector){
    if(IsConverge==true && x.status==0){
      out_vector.push_back(x.w_ch_up_type_pt);
    }
    else if(IsConverge==false && x.status!=0){
      out_vector.push_back(x.w_ch_up_type_pt);
    }
  }
  return out_vector;
}


std::vector<double> TKinFitterDriver::GetWCHUpTypePtVector(bool IsConverge){
  std::vector<double> out_vector;
  for(auto &x : fit_result_vector){
    if(IsConverge==true && x.status==0){
      out_vector.push_back(x.w_ch_down_type_pt);
    }
    else if(IsConverge==false && x.status!=0){
      out_vector.push_back(x.w_ch_down_type_pt);
    }
  }
  return out_vector;
}


const std::vector<TKinFitterDriver::ResultContainer>* TKinFitterDriver::GetResults(){
  return &fit_result_vector;
}


bool TKinFitterDriver::NextPermutation(bool UseLeading4Jets){

  std::vector<TKinFitterDriver::JET_ASSIGNMENT>::iterator begin = permutation_vector.begin();
  std::vector<TKinFitterDriver::JET_ASSIGNMENT>::iterator end   = permutation_vector.end();
  if(UseLeading4Jets){
    end = begin+4;
  }
  else{
    if(end - begin > 7){ // upto 7th leading jets
      end = begin+7;
    }
    else{
      //pass
    }
  }
  return std::next_permutation(begin,end); //permutation in range of [begin,end)
}


void TKinFitterDriver::SetJetError(TMatrixD *matrix,  double Pt, double Eta, double Phi, TString flavour_key){
  (*matrix)(0,0) = TMath::Power(Pt*this->JetErrorPt(Pt, Eta, flavour_key), 2);
  //(*matrix)(1,1) = TMath::Power(Eta*this->JetErrorEta(Et, Eta, flavour_key), 2);
  //(*matrix)(2,2) = TMath::Power(Phi*this->JetErrorPhi(Et, Eta, flavour_key), 2);
}


double TKinFitterDriver::JetErrorPt(double Pt, double Eta, TString flavour_key){
  return ts_correction->GetFittedError("Pt", flavour_key, Pt, Eta);
}


double TKinFitterDriver::JetErrorEta(double Pt, double Eta, TString flavour_key){
  return ts_correction->GetFittedError("Eta", flavour_key, Pt, Eta);
}


double TKinFitterDriver::JetErrorPhi(double Pt, double Eta, TString flavour_key){
  return ts_correction->GetFittedError("Phi", flavour_key, Pt, Eta);
}


void TKinFitterDriver::Sol_Neutrino_Pz(){
  
  double lepton_mass =  lepton.M();

  double k = 80.4*80.4/2.0 - lepton_mass*lepton_mass/2.0 + lepton.Px()*METv.Px() + lepton.Py()*METv.Py();
  double a = TMath::Power(lepton.Px(), 2.0) + TMath::Power(lepton.Py(), 2.0);
  double b = -2*k*lepton.Pz();                                                           
  double c = TMath::Power(lepton.Pt(), 2.0)*TMath::Power(METv.Pt(), 2.0) - TMath::Power(k, 2.0);

  double determinant = TMath::Power(b, 2.0) - 4*a*c;
  
  //cout << "determinant = " << determinant << endl;
  
  //real soluion
  if(determinant>=0){
    neutrino_pz_sol[0] = (-b + TMath::Sqrt(determinant))/(2*a);                      
    neutrino_pz_sol[1] = (-b - TMath::Sqrt(determinant))/(2*a);                      
    IsRealNeuPz = true;
  }
  else{
    neutrino_pz_sol[0] = -b/(2*a);
    this->Resol_Neutrino_Pt();
    IsRealNeuPz = false;
  }

}


void TKinFitterDriver::Resol_Neutrino_Pt(){

  //cout << "Kinematic_Fitter_MVA::Resol_Neutino_Pt" << endl;
    
  //recal MET
  double lepton_mass = lepton.M();
  double cosine = TMath::Cos(METv.Phi());
  double sine = TMath::Sin(METv.Phi());
  
  double a = lepton.E()*lepton.E() - lepton.Pz()*lepton.Pz() - TMath::Power(lepton.Px()*cosine + lepton.Py()*sine , 2.0);
  double b = (lepton.Px()*cosine + lepton.Py()*sine)*(lepton_mass*lepton_mass - 80.4*80.4);
  double determinant = TMath::Power(lepton_mass*lepton_mass - 80.4*80.4, 2.)*(lepton.E()*lepton.E() - lepton.Pz()*lepton.Pz());
  
  //cout << "a = " << a << endl;
  //cout << "b = " << b << endl;
  //cout << "det = "<< determinant << endl;

  double met_recal[2];
  met_recal[0] = (-b + TMath::Sqrt(determinant))/2./a;
  met_recal[1] = (-b - TMath::Sqrt(determinant))/2./a;
  
  double mass_diff[2];
  TLorentzVector met_recal_vector[2];
  for(Int_t i=0; i<2; i++)
    {
      met_recal_vector[i].SetPxPyPzE(met_recal[i]*cosine, met_recal[i]*sine, 0, met_recal[i]);
      
      TLorentzVector w_lnu;
      w_lnu = lepton + met_recal_vector[i];
      
      double w_lnu_mass = w_lnu.M();
      mass_diff[i] = TMath::Abs(80.4 - w_lnu_mass);
      
      //cout << METv.Pt() << "\t" << met_recal[i] << "\t" << w_lnu.M() << "\t" << mass_diff[i] << endl;
    }
  //cout << endl;
  
  if(mass_diff[0]<mass_diff[1]) recal_METv = met_recal_vector[0];
  else recal_METv = met_recal_vector[1];
  
}


bool TKinFitterDriver::Chi2Comparing(const TKinFitterDriver::ResultContainer& rc1, const TKinFitterDriver::ResultContainer& rc2){
  return (rc1.chi2 < rc2.chi2);
}
bool TKinFitterDriver::HadTopMComparing(const TKinFitterDriver::ResultContainer& rc1, const TKinFitterDriver::ResultContainer& rc2){
  // if chi2 is same compare hadronic_top_M
  return (fabs(rc1.hadronic_top_M-172.5) < fabs(rc2.hadronic_top_M-172.5)) ||  (fabs(rc1.hadronic_top_M-172.5) == fabs(rc2.hadronic_top_M-172.5) && (rc1.chi2 < rc2.chi2));
}

bool TKinFitterDriver::HighMassFitter(const TKinFitterDriver::ResultContainer& rc1, const TKinFitterDriver::ResultContainer& rc2){
  bool out; 
  out=(rc1.chi2 < rc2.chi2) ||
      (
       (rc1.chi2 == rc2.chi2) &&
       (rc1.hadronic_top_b_pt < rc1.w_ch_down_type_pt) &&
       (rc2.hadronic_top_b_pt >= rc2.w_ch_down_type_pt)
      );
  return out;
}


bool TKinFitterDriver::HadTopPtComparing(const TKinFitterDriver::ResultContainer& rc1, const TKinFitterDriver::ResultContainer& rc2){
  return (rc1.hadronic_top_pt > rc2.hadronic_top_pt);
}


bool TKinFitterDriver::LepTopPtComparing(const TKinFitterDriver::ResultContainer& rc1, const TKinFitterDriver::ResultContainer& rc2){
  return (rc1.leptonic_top_pt > rc2.leptonic_top_pt);
}


bool TKinFitterDriver::TopPtComparing(const TKinFitterDriver::ResultContainer& rc1, const TKinFitterDriver::ResultContainer& rc2){
  return (rc1.chi2 < 10.) && (rc1.hadronic_top_pt > rc2.hadronic_top_pt);
}
