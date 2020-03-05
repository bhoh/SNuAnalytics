#include <iostream>
#include <TLorentzVector.h>
#include <TTree.h>
#include <math.h>
#include "DeclareBranch.h"
//    'expr':'PrimaryFatJet_cjidx(Entry$,'+maxtau21+','+min_jetId+','+max_jetId+')',
using namespace std;
namespace multidraw {

  extern thread_local TTree* currentTree;

}



//std::vector<Float_t> CleanFatJet_pt;
//std::vector<Float_t> CleanFatJet_tau21;
//std::vector<int> CleanFatJet_jetIdx;
//std::vector<int> FatJet_jetId;

//float Lepton_pt[10];
//float Lepton_eta[10];
//float Lepton_phi[10];
//float MET_pt;
//float MET_phi;




void init_WlepMaker(TTree* tree, TString METtype){

  tree->ResetBranchAddresses();
  tree->SetBranchAddress("Lepton_pt", &Lepton_pt);
  tree->SetBranchAddress("Lepton_eta", &Lepton_eta);
  tree->SetBranchAddress("Lepton_phi", &Lepton_phi);
  tree->SetBranchAddress(METtype+"MET_pt", &MET_pt);
  tree->SetBranchAddress(METtype+"MET_phi", &MET_phi);
  
}



//float WlepPuppi_pt(int entry){
//  return WlepPuppi(entry).Pt();
//}




void SetWlep(int entry,TString METtype){
  if(name_temp != multidraw::currentTree->GetCurrentFile()->GetName()){
    cout << "name_temp = " << name_temp << endl;
    name_temp = multidraw::currentTree->GetCurrentFile()->GetName();
    cout << "name_temp = " << name_temp << endl;
    initialized = false;
  }
  if (!initialized){
    init_WlepMaker(multidraw::currentTree,METtype);    
    cout << "check init" << endl;
    initialized = true;
  }

  

  //cout<<"start WlepMaker"<<endl;
  multidraw::currentTree->GetEntry(entry);
  
  //--Set W mass--//
  float wmass=80.4;
  //--Get the momentum of objects--//
  float lep_pt  = Lepton_pt[0];
  float lep_phi = Lepton_phi[0];
  float lep_eta = Lepton_eta[0];
  float lep_pz  = lep_pt*sinh(lep_eta);
  float lep_E   = lep_pt*cosh(lep_eta);
  float met_pt  = MET_pt;
  float met_phi = MET_phi;
  
  //met_pz solution = met_pz_1 +-sqrt(met_pz_2)
  float mu       = (wmass*wmass)/2 + lep_pt*met_pt*cos(met_phi-lep_phi);
  met_pz_1 = mu*lep_pz/pow(lep_pt,2);
  met_pz_2 = pow( mu*lep_pz/(lep_pt*lep_pt), 2 ) - ( pow(lep_E*met_pt, 2) - mu*mu )/pow(lep_pt,2);
  

  //--Let's get the neutrino's pz
  float met_pz=0;
  //1) complex -> Get only real part
  if (met_pz_2 < 0) met_pz = met_pz_1;
  //2) real solution
  else{
    sol1 = met_pz_1+sqrt(met_pz_2);
    sol2 = met_pz_1-sqrt(met_pz_2);
    if(fabs(sol1) < fabs(sol2)){
      met_pz = sol1;
    }
    else{
      met_pz = sol2;
    }
  }
  /*
  cout<<"before if met_pz_1"<<endl;
  if(x=="met_pz_1"){
    return met_pz_1;
  }
  else if(x=="met_pz_2"){
    return met_pz_2;
  }
  cout<<"after if met_pz_2"<<endl;*/
  //W momentum

  float wlep_px = lep_pt*cos(lep_phi) + met_pt*cos(met_phi);
  float wlep_py = lep_pt*sin(lep_phi) + met_pt*sin(met_phi);
  float wlep_pz = lep_pz + met_pz;
  float wlep_E  = lep_E  + sqrt(pow(met_pz,2) + pow(met_pt,2));
  
  //TLorentzVector v_wlep;
  //v_wlep.SetPxPyPzE(wlep_px, wlep_py, wlep_pz, wlep_E);
  Wlep.SetPxPyPzE(wlep_px, wlep_py, wlep_pz, wlep_E);
  /*
  if(x=="wlep_px"){
    return wlep_px;
  }
  if(x=="wlep_py"){
    return wlep_py;
  }
  if(x=="wlep_pz"){
    return wlep_pz;
  }
  if(x=="wlep_E"){
    return wlep_E;
  }
  if(x=="wlep_pt"){
    return v_wlep.Pt();
  }
  if(x=="wlep_eta"){
    return v_wlep.Eta();
  }
  if(x=="wlep_phi"){
    return v_wlep.Phi();
  }
  if(x=="wlep_mass"){
    return v_wlep.M();;
  }
  std::cout<<"[jhchoi, WlepMaker]Non matched variable for "<<x<<std::endl;
  return -999.;
 */
}

//---Return Puppi
float WlepPuppi_pt(int entry){
  SetWlep(entry,"Puppi");
  return Wlep.Pt();
}

float WlepPuppi_mass(int entry){
  SetWlep(entry,"Puppi");
  return Wlep.M();
}


float WlepPuppi_eta(int entry){
  SetWlep(entry,"Puppi");
  return Wlep.Eta();
}

float WlepPuppi_phi(int entry){
  SetWlep(entry,"Puppi");
  return Wlep.Phi();
}

float WlepPuppi_met_pz_1(int entry){
  SetWlep(entry,"Puppi");
  return met_pz_1;
}
float WlepPuppi_met_pz_2(int entry){
  SetWlep(entry,"Puppi");
  return met_pz_2;
}


//--Return PF 

float WlepPF_pt(int entry){
  SetWlep(entry,"PF");
  return Wlep.Pt();
}

float WlepPF_mass(int entry){
  SetWlep(entry,"PF");
  return Wlep.M();
}


float WlepPF_eta(int entry){
  SetWlep(entry,"PF");
  return Wlep.Eta();
}

float WlepPF_phi(int entry){
  SetWlep(entry,"PF");
  return Wlep.Phi();
}
float WlepPF_met_pz_1(int entry){
  SetWlep(entry,"PF");
  return met_pz_1;
}
float WlepPF_met_pz_2(int entry){
  SetWlep(entry,"PF");
  return met_pz_2;
}
