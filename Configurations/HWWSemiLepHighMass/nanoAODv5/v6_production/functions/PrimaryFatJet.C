#include <iostream>
#include <TLorentzVector.h>
#include <TTree.h>

#include "DeclareBranch.h"

//    'expr':'PrimaryFatJet_cjidx(Entry$,'+maxtau21+','+min_jetId+','+max_jetId+')',

namespace multidraw {

  extern thread_local TTree* currentTree;

}



//std::vector<Float_t> CleanFatJet_pt;
//std::vector<Float_t> CleanFatJet_tau21;
//std::vector<int> CleanFatJet_jetIdx;
//std::vector<int> FatJet_jetId;

//UInt_t nCleanFatJet;
//float CleanFatJet_pt[10];
//float CleanFatJet_tau21[10];
//int CleanFatJet_jetIdx[10];
//int FatJet_jetId[10];


void init(TTree* tree){
  tree->ResetBranchAddresses();
  tree->SetBranchAddress("nCleanFatJet", &nCleanFatJet);
  tree->SetBranchAddress("CleanFatJet_pt", &CleanFatJet_pt);
  tree->SetBranchAddress("CleanFatJet_mass", &CleanFatJet_mass);
  tree->SetBranchAddress("CleanFatJet_tau21", &CleanFatJet_tau21);
  tree->SetBranchAddress("CleanFatJet_jetIdx", &CleanFatJet_jetIdx);
  tree->SetBranchAddress("FatJet_jetId", &FatJet_jetId);

}


bool FindPrimaryFatJet(int entry,float maxtau21, int min_jetId, int max_jetId){


  if(name_temp != multidraw::currentTree->GetCurrentFile()->GetName()){
    cout << "name_temp = " << name_temp << endl;
    name_temp = multidraw::currentTree->GetCurrentFile()->GetName();
    cout << "name_temp = " << name_temp << endl;
    initialized = false;
  }
  if (!initialized){
    init(multidraw::currentTree);
    cout << "check init" << endl;
    initialized = true;
  }


  multidraw::currentTree->GetEntry(entry);
  //int nCleanFatJet = CleanFatJet_pt.size();

  float this_pt = 200;
  
  cjidx=-1;
  for(int i=0; i < nCleanFatJet; i++){
    float tau21 = CleanFatJet_tau21[i];
    float pt    = CleanFatJet_pt[i];
    float jetId = FatJet_jetId[CleanFatJet_jetIdx[i]];
    float mass = CleanFatJet_mass[i];
    if (mass < 40 ) continue;
    if (mass > 250 ) continue;
    if( tau21 > maxtau21 ) continue;
    if(pt < this_pt) continue;
    if(jetId<min_jetId) continue;
    if(jetId>max_jetId) continue;
    cjidx=i;
  }
  
  //std::cout << "cjidx=>" << cjidx<<std::endl;
  if(cjidx<0){
    return false;
  }
  return true;

}
float WFatJet_pt(int entry,float maxtau21, int min_jetId, int max_jetId){
  FindPrimaryFatJet(entry,maxtau21,min_jetId,max_jetId);
  if(cjidx<0){
    return -999.;}
  
  return CleanFatJet_pt[cjidx];
}


float WFatJet_eta(int entry,float maxtau21, int min_jetId, int max_jetId){
  FindPrimaryFatJet(entry,maxtau21,min_jetId,max_jetId);
  if(cjidx<0){
    return -999.;}
  
  return CleanFatJet_eta[cjidx];
}

float WFatJet_phi(int entry,float maxtau21, int min_jetId, int max_jetId){
  FindPrimaryFatJet(entry,maxtau21,min_jetId,max_jetId);
  if(cjidx<0){
    return -999.;}
  
  return CleanFatJet_phi[cjidx];
}

float WFatJet_mass(int entry,float maxtau21, int min_jetId, int max_jetId){
  FindPrimaryFatJet(entry,maxtau21,min_jetId,max_jetId);
  if(cjidx<0){
    return -999.;}
  
  return CleanFatJet_mass[cjidx];
}
