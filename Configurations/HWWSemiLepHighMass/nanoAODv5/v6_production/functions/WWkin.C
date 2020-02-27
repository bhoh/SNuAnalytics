#include <iostream>
#include <TLorentzVector.h>
#include <TTree.h>
#include "DeclareBranch.h"

namespace multidraw {
  extern thread_local TTree* currentTree;
}


//float CleanFatJet_pt[10];
//float CleanFatJet_eta[10];
//float CleanFatJet_phi[10];
//float CleanFatJet_mass[10];


void init_WWkin(TTree* tree){

  tree->ResetBranchAddresses();
  tree->SetBranchAddress("CleanFatJet_pt", &CleanFatJet_pt);
  tree->SetBranchAddress("CleanFatJet_eta", &CleanFatJet_eta);
  tree->SetBranchAddress("CleanFatJet_phi", &CleanFatJet_phi);
  tree->SetBranchAddress("CleanFatJet_mass", &CleanFatJet_mass);
  

}

bool SetWWFat(int entry, float Wlep_pt, float Wlep_eta, float Wlep_phi, float Wlep_mass, int PrimaryFatJet_cjidx){
  
  if(name_temp != multidraw::currentTree->GetCurrentFile()->GetName()){
    cout << "name_temp = " << name_temp << endl;
    name_temp = multidraw::currentTree->GetCurrentFile()->GetName();
    cout << "name_temp = " << name_temp << endl;
    initialized = false;
  }
  if (!initialized){
    init_WWkin(multidraw::currentTree);
    cout << "check init" << endl;
    initialized = true;
  }

  if (PrimaryFatJet_cjidx<0){
    return false;
  }
  init_WWkin(multidraw::currentTree);
  multidraw::currentTree->GetEntry(entry);


  TLorentzVector v1,v2;
  //---wlep
  v1.SetPxPyPzE(Wlep_pt,Wlep_eta,Wlep_phi,Wlep_mass);
  //---whad
  v2.SetPtEtaPhiM(CleanFatJet_pt[PrimaryFatJet_cjidx],CleanFatJet_eta[PrimaryFatJet_cjidx],CleanFatJet_phi[PrimaryFatJet_cjidx],CleanFatJet_mass[PrimaryFatJet_cjidx]);
  WWFat=(v1+v2);
  return true;
}

float WWFat_mass(int entry, float Wlep_pt, float Wlep_eta, float Wlep_phi, float Wlep_mass, int PrimaryFatJet_cjidx){
  bool isWFatEvent=SetWWFat(entry, Wlep_pt, Wlep_eta, Wlep_phi, Wlep_mass, PrimaryFatJet_cjidx);
  if(!isWFatEvent){
    return -999.;
  }
  else{
    return WWFat.M();
  }
}


float WWFat_pt(int entry, float Wlep_pt, float Wlep_eta, float Wlep_phi, float Wlep_mass, int PrimaryFatJet_cjidx){
  bool isWFatEvent=SetWWFat(entry, Wlep_pt, Wlep_eta, Wlep_phi, Wlep_mass, PrimaryFatJet_cjidx);
  if(!isWFatEvent){
    return -999.;
  }
  else{
    return WWFat.Pt();
  }
}


float WWFat_eta(int entry, float Wlep_pt, float Wlep_eta, float Wlep_phi, float Wlep_mass, int PrimaryFatJet_cjidx){
  bool isWFatEvent=SetWWFat(entry, Wlep_pt, Wlep_eta, Wlep_phi, Wlep_mass, PrimaryFatJet_cjidx);
  if(!isWFatEvent){
    return -999.;
  }
  else{
    return WWFat.Eta();
  }
}


float WWFat_phi(int entry, float Wlep_pt, float Wlep_eta, float Wlep_phi, float Wlep_mass, int PrimaryFatJet_cjidx){
  bool isWFatEvent=SetWWFat(entry, Wlep_pt, Wlep_eta, Wlep_phi, Wlep_mass, PrimaryFatJet_cjidx);
  if(!isWFatEvent){
    return -999.;
  }
  else{
    return WWFat.Phi();
  }
}
