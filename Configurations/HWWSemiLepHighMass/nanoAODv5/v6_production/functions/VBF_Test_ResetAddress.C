#include "TFile.h"
#include <iostream>
#include <TLorentzVector.h>
#include <TTree.h>
//#include "DeclareBranch.h"

namespace multidraw {
  extern thread_local TTree* currentTree;
}


bool initialized = false;
TString name_temp = "";

float CleanJet_pt[20];
float CleanJet_eta[20];
float CleanJet_phi[20];
int CleanJet_jetIdx[20];
int CleanJetNotFat_jetIdx[20];
UInt_t nCleanJetNotFat;
float Jet_mass[30];


void init_VBF(TTree* tree){

  tree->ResetBranchAddresses();
  tree->SetBranchAddress("CleanJet_pt", &CleanJet_pt);
  tree->SetBranchAddress("CleanJet_eta", &CleanJet_eta);
  tree->SetBranchAddress("CleanJet_phi", &CleanJet_phi);
  tree->SetBranchAddress("CleanJet_jetIdx", &CleanJet_jetIdx);
  tree->SetBranchAddress("CleanJetNotFat_jetIdx", &CleanJetNotFat_jetIdx);
  tree->SetBranchAddress("nCleanJetNotFat", &nCleanJetNotFat);
  tree->SetBranchAddress("Jet_mass", &Jet_mass);


}

bool SetVBF(int entry){


  if(name_temp != multidraw::currentTree->GetCurrentFile()->GetName()){
    cout << "name_temp = " << name_temp << endl;
    name_temp = multidraw::currentTree->GetCurrentFile()->GetName();
    cout << "name_temp = " << name_temp << endl;
    initialized = false;
  }
  if (!initialized){
    init_VBF(multidraw::currentTree);
    cout << "check init" << endl;
    initialized = true;
  }


  multidraw::currentTree->GetEntry(entry);




  if(nCleanJetNotFat<2){
    return false;
  }
  
  float VBF_jjdEta = -9999.;
  float VBF_Mjj  = -9999.;
  
  int Njet=nCleanJetNotFat;
  for(int ci = 0; ci < Njet; ci++ ){
    //--momentum of 1st jet
    float pt1 = CleanJet_pt[ci];
    if(pt1<30){
      continue;
    }
    float eta1 = CleanJet_eta[ci];
    float phi1 = CleanJet_phi[ci];
    float mass1 = Jet_mass[CleanJetNotFat_jetIdx[ci]];

    for(int cj = 0; cj < Njet; cj++){
      if(ci>=cj)continue;
      float pt2 = CleanJet_pt[cj];
      float eta2 = CleanJet_eta[cj];
      float phi2 = CleanJet_phi[cj];
      float mass2 = Jet_mass[CleanJetNotFat_jetIdx[cj]];



      TLorentzVector v1,v2;
      v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1);
      v2.SetPtEtaPhiM(pt1,eta1,phi1,mass1);
      

      float this_dEta = fabs(eta1-eta2);
      float this_Mjj  = (v1+v2).M();

      if(this_Mjj < 500 ) continue;
      if(this_dEta < 3.5 ) continue;
      if(this_dEta > VBF_jjdEta){
	VBF_jjdEta=this_dEta;
	VBF_Mjj=this_Mjj;
      }

    }
  }
  if(VBF_jjdEta < 3.5) return false;
    
  return true;
  
}
