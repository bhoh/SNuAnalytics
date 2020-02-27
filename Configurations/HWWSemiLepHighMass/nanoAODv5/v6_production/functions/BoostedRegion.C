#include <TFile.h>
#include <iostream>
#include <TLorentzVector.h>
#include <TTree.h>


//    'expr':'PrimaryFatJet_cjidx(Entry$,'+maxtau21+','+min_jetId+','+max_jetId+')',

namespace multidraw {

  extern thread_local TTree* currentTree;

}
UInt_t nCleanFatJet;

float CleanFatJet_pt[10];
float CleanFatJet_eta[10];
float CleanFatJet_phi[10];
float CleanFatJet_mass[10];
float CleanFatJet_tau21[10];
int CleanFatJet_jetIdx[10];

int FatJet_jetId[10];

float CleanJet_pt[20];
float CleanJet_eta[20];
float CleanJet_phi[20];
float CleanJet_jetIdx[20];



UInt_t nCleanJetNotFat;
int CleanJetNotFat_jetIdx[20];

float Jet_mass[30];



//UInt_t

//---variables
float Lepton_pt[10];
float Lepton_eta[10];
float Lepton_phi[10];
float MET_pt;
float MET_phi;

//float PuppiMET_pt;
//float PuppiMET_phi;

TLorentzVector Wlep,WWFat;
float sol1, sol2, met_pz_1, met_pz_2;


float VBF_jjdEta;
float VBF_Mjj;

int cjidx;

bool isFatJetEvent=false;
bool isVBFEvent=false;

//--To prevent memory leakage
//bool initialized = false;
//TString name_temp = "";



//1)----- FatJet Selector----//
void init_FindPrimaryFatJet(TTree* tree){
  //tree->ResetBranchAddresses();
  tree->SetBranchAddress("nCleanFatJet", &nCleanFatJet);
  tree->SetBranchAddress("CleanFatJet_pt", &CleanFatJet_pt);
  tree->SetBranchAddress("CleanFatJet_mass", &CleanFatJet_mass);
  tree->SetBranchAddress("CleanFatJet_eta", &CleanFatJet_eta);
  tree->SetBranchAddress("CleanFatJet_phi", &CleanFatJet_phi);
  tree->SetBranchAddress("CleanFatJet_tau21", &CleanFatJet_tau21);
  tree->SetBranchAddress("CleanFatJet_jetIdx", &CleanFatJet_jetIdx);
  tree->SetBranchAddress("FatJet_jetId", &FatJet_jetId);

}

int entry_FindPrimaryFatJet=-999;
TString f_FindPrimaryFatJet="";



bool FindPrimaryFatJet(int entry, float maxtau21, int min_jetId, int max_jetId){


  if( (f_FindPrimaryFatJet != multidraw::currentTree->GetCurrentFile()->GetName()) ){
    init_FindPrimaryFatJet(multidraw::currentTree);  
  }

  else if( entry_FindPrimaryFatJet == entry ){ //if both file and entry are already set
    return isFatJetEvent;
  }

  f_FindPrimaryFatJet=multidraw::currentTree->GetCurrentFile()->GetName(); 
  entry_FindPrimaryFatJet=entry;

  multidraw::currentTree->GetEntry(entry);
  //int nCleanFatJet = CleanFatJet_pt.size();

  float this_pt = 200;
  
  cjidx=-1;
  for(unsigned int i=0; i < nCleanFatJet; i++){
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
    isFatJetEvent=false;
    return false;
  }
  isFatJetEvent=true;
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


float WFatJet_tau21(int entry,float maxtau21, int min_jetId, int max_jetId){
  FindPrimaryFatJet(entry,maxtau21,min_jetId,max_jetId);
  if(cjidx<0){
    return -999.;}
  
  return CleanFatJet_tau21[cjidx];
}


//----2) Make Wlep 

void init_WlepMaker(TTree* tree, TString METtype){

  //tree->ResetBranchAddresses();
  tree->SetBranchAddress("Lepton_pt", &Lepton_pt);
  tree->SetBranchAddress("Lepton_eta", &Lepton_eta);
  tree->SetBranchAddress("Lepton_phi", &Lepton_phi);
  tree->SetBranchAddress(METtype+"MET_pt", &MET_pt);
  tree->SetBranchAddress(METtype+"MET_phi", &MET_phi);

}


int entry_SetWlep=-999;
TString f_SetWlep="";


void SetWlep(int entry,TString METtype){

  if( (f_SetWlep != multidraw::currentTree->GetCurrentFile()->GetName()) ){
    init_WlepMaker(multidraw::currentTree, METtype);  
  }
  else if( entry_SetWlep == entry ){ //if both file and entry are already set
    return;
  }

  f_SetWlep = multidraw::currentTree->GetCurrentFile()->GetName(); // 
  entry_SetWlep= entry;

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

  float wlep_px = lep_pt*cos(lep_phi) + met_pt*cos(met_phi);
  float wlep_py = lep_pt*sin(lep_phi) + met_pt*sin(met_phi);
  float wlep_pz = lep_pz + met_pz;
  float wlep_E  = lep_E  + sqrt(pow(met_pz,2) + pow(met_pt,2));

  Wlep.SetPxPyPzE(wlep_px, wlep_py, wlep_pz, wlep_E);
}


//---Return Puppi
float WlepPuppi_pt(int entry){  SetWlep(entry,"Puppi"); return Wlep.Pt();}
float WlepPuppi_mass(int entry){  SetWlep(entry,"Puppi"); return Wlep.M();}
float WlepPuppi_eta(int entry){  SetWlep(entry,"Puppi");return Wlep.Eta();}
float WlepPuppi_phi(int entry){  SetWlep(entry,"Puppi"); return Wlep.Phi();}
float WlepPuppi_met_pz_1(int entry){  SetWlep(entry,"Puppi"); return met_pz_1;}
float WlepPuppi_met_pz_2(int entry){  SetWlep(entry,"Puppi"); return met_pz_2;}

//--Return PF
float WlepPF_pt(int entry){SetWlep(entry,"PF");return Wlep.Pt();}
float WlepPF_mass(int entry){  SetWlep(entry,"PF");return Wlep.M();}
float WlepPF_eta(int entry){  SetWlep(entry,"PF");  return Wlep.Eta();}
float WlepPF_phi(int entry){  SetWlep(entry,"PF");  return Wlep.Phi();}
float WlepPF_met_pz_1(int entry){  SetWlep(entry,"PF");  return met_pz_1;}
float WlepPF_met_pz_2(int entry){  SetWlep(entry,"PF");  return met_pz_2;}


//---4)VBF selection
void init_VBF(TTree* tree){

  //tree->ResetBranchAddresses();
  tree->SetBranchAddress("CleanJet_pt", &CleanJet_pt);
  tree->SetBranchAddress("CleanJet_eta", &CleanJet_eta);
  tree->SetBranchAddress("CleanJet_phi", &CleanJet_phi);
  tree->SetBranchAddress("CleanJet_jetIdx", &CleanJet_jetIdx);
  tree->SetBranchAddress("CleanJetNotFat_jetIdx", &CleanJetNotFat_jetIdx);
  tree->SetBranchAddress("nCleanJetNotFat", &nCleanJetNotFat);
  tree->SetBranchAddress("Jet_mass", &Jet_mass);


}


int entry_SetVBF=-999;
TString f_SetVBF="";

bool SetVBF(int entry){

  if( (f_SetVBF != multidraw::currentTree->GetCurrentFile()->GetName()) ){
    init_VBF(multidraw::currentTree);  
  }
  else if( entry_SetVBF == entry ){ //if both file and entry are already set
    return isVBFEvent;
  }

  f_SetVBF = multidraw::currentTree->GetCurrentFile()->GetName();
  entry_SetVBF= entry;

  multidraw::currentTree->GetEntry(entry);
  if(nCleanJetNotFat<2){
    return false;
  }

  VBF_jjdEta = -9999.;
  VBF_Mjj  = -9999.;

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
      if(ci>=cj) continue;
      
      float pt2 = CleanJet_pt[cj];
      if(pt2<30) continue;
      float eta2 = CleanJet_eta[cj];
      float phi2 = CleanJet_phi[cj];
      float mass2 = Jet_mass[CleanJetNotFat_jetIdx[cj]];



      TLorentzVector v1,v2;
      v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1);
      v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2);


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
  if(VBF_jjdEta < 3.5){
    isVBFEvent=false;
    return false;
  }
  isVBFEvent=true;
  return true;

}


float Get_VBF_jjdEta(int entry){
  isVBFEvent=SetVBF(entry);
  if(!isVBFEvent){
    return -9999;
  }
  else{
    return VBF_jjdEta;
  }

}


float Get_VBF_Mjj(int entry){
  isVBFEvent=SetVBF(entry);
  if(!isVBFEvent){
    return -9999;
  }
  else{
    return VBF_Mjj;
  }

}
